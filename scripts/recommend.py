import os
import re
import yaml
import MeCab
import numpy as np
from collections import OrderedDict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

RE_FRONT_MATTER = re.compile('---\n([\s\S]*?\n)---\n')
RE_PATH_TO_PERMALINK = re.compile('((/ja){0,1}/note/.+?)(\.md|\.html)')
RE_VALID_WORD = re.compile('^[ぁ-んーァ-ヶー一-龠a-zA-Zａ-ｚＡ-Ｚ]+$')
RE_INVALID_WORD = re.compile('^([^一-龠]{1,2}|[ぁ-んー]{1,3})$')
RE_PATH_TO_IMAGE = re.compile('/images/.+?(?:\.jpg|\.jpeg|\.png)')

RE_FILTERS = [
    re.compile('<.*?>'),  # HTML tag
    re.compile('^(\$\$|```)(.*)\n(.*\n)+(\$\$|```)', re.MULTILINE),  # Markdown codefence / math block
    re.compile('https?:\/\/[\S]+')  # URL
]

tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
tagger.parse('')


def tokenizer(doc):
    # TODO: more aggressive preprocessing e.g., filtering out URLs
    def get_tokens(text):
        node = tagger.parseToNode(text)
        while node:
            yield node.surface.lower()
            node = node.next

    return [token for token in get_tokens(doc) if 2 <= len(token) <= 15 and
            RE_VALID_WORD.match(token) and not RE_INVALID_WORD.match(token)]


def extract_contents(paths):
    for path in paths:
        with open(path) as f:
            content = f.read()

        m = RE_FRONT_MATTER.search(content)

        if m is None:
            yield (path, '')
            continue

        # avoid recommending draft articles by making their contents empty
        front_matter = yaml.load(m.group(1))
        if 'draft' in front_matter and front_matter['draft']:
            yield (path, '')
            continue

        # remove front matter
        content = content.replace(m.group(0), '')

        for re_filter in RE_FILTERS:
            content = re_filter.sub('', content)

        yield (path, content)

def path_to_permalink(path):
    return RE_PATH_TO_PERMALINK.search(path).group(1) + '/'


def recommend_content_based_cf(articles, topk=3):
    """Content-based collaborative filtering
    """
    # build model
    vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, tokenizer=tokenizer, stop_words='english')

    tfidf = vectorizer.fit_transform(articles.values())

    indices = tfidf.toarray().argsort(axis=1, kind='stable')[:, ::-1]
    keywords = np.array(vectorizer.get_feature_names())[indices]

    similarities = cosine_similarity(tfidf)

    paths = list(articles.keys())
    for i, path in enumerate(paths):
        # find top-k most-similar articles (except for target article itself which is similarity=1.0)
        top_indices = np.argsort(similarities[i, :], kind='stable')[::-1][1:(topk + 1)]
        recommend_permalinks = [path_to_permalink(paths[j]) for j in top_indices]

        yield (
            path, {
                'keywords': keywords[i, :10].tolist(),
                'recommendations': recommend_permalinks
            }
        )


def find_images(articles):
    for path, content in articles.items():
        images = RE_PATH_TO_IMAGE.findall(content)
        if len(images) == 0:
            continue
        yield (path, {'images': images})


def process_article(path, custom_front_matter):
    with open(path) as f:
        content = f.read()

    m = RE_FRONT_MATTER.search(content)
    if m is None:
        return

    front_matter = yaml.load(m.group(1))
    # "images" shouldn't be overrode if already exist
    if 'images' in front_matter and 'images' in custom_front_matter:
        del custom_front_matter['images']
    front_matter = {**front_matter, **custom_front_matter}

    with open(path, 'w') as f:
        f.write(content.replace(m.group(1), yaml.dump(front_matter, allow_unicode=True)))


def run(lang):
    path_dir = os.path.join(os.path.dirname(__file__), '..', '_content', lang, 'note')
    paths = [os.path.join(path_dir, f) for f in os.listdir(path_dir)]

    articles = OrderedDict(extract_contents(paths))

    update_ops = dict(recommend_content_based_cf(articles, topk=3))
    for path, front_matter in find_images(articles):  # merge
        process_article(path, {**update_ops[path], **front_matter})


def main():
    run('en')
    run('ja')


if __name__ == '__main__':
    main()
