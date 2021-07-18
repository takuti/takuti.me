import os
import re
import yaml
import MeCab
import numpy as np
from urllib.parse import quote
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

RE_FRONT_MATTER = re.compile('---\n([\s\S]*?\n)---\n')
RE_PATH_TO_PERMALINK = re.compile('((/ja){0,1}/note/.+?)(\.md|\.html)')
RE_VALID_WORD = re.compile('^[ぁ-んーァ-ヶー一-龠a-zA-Zａ-ｚＡ-Ｚ]+$')
RE_INVALID_WORD = re.compile('^([^一-龠]{1,2}|[ぁ-んー]{1,3})$')

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
    contents = []
    for path in paths:
        with open(path) as f:
            content = f.read()

        m = RE_FRONT_MATTER.search(content)

        if m is None:
            contents.append('')
            continue

        # avoid recommending draft articles by making their contents empty
        front_matter = yaml.load(m.group(1))
        if 'draft' in front_matter and front_matter['draft']:
            contents.append('')
            continue

        # remove front matter
        content = content.replace(m.group(0), '')

        for re_filter in RE_FILTERS:
            content = re_filter.sub('', content)

        contents.append(content)
    return contents


def path_to_permalink(path):
    return RE_PATH_TO_PERMALINK.search(path).group(1) + '/'


def recommend_content_based_cf(paths, topk=3):
    """Content-based collaborative filtering
    """

    samples = extract_contents(paths)

    # build model
    vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, tokenizer=tokenizer, stop_words='english')

    tfidf = vectorizer.fit_transform(samples)

    indices = tfidf.toarray().argsort(axis=1, kind='stable')[:, ::-1]
    keywords = np.array(vectorizer.get_feature_names())[indices]

    similarities = cosine_similarity(tfidf)

    for i, path in enumerate(paths):
        # find top-k most-similar articles (except for target article itself which is similarity=1.0)
        top_indices = np.argsort(similarities[i, :], kind='stable')[::-1][1:(topk + 1)]
        recommend_permalinks = [path_to_permalink(paths[j]) for j in top_indices]

        yield (path, keywords[i, :10].tolist(), recommend_permalinks)


def process_article(path, keywords, recommend_permalinks):
    with open(path) as f:
        content = f.read()

    m = RE_FRONT_MATTER.search(content)
    if m is None:
        return

    front_matter = yaml.load(m.group(1))

    front_matter['keywords'] = keywords
    front_matter['recommendations'] = recommend_permalinks

    og_image = 'https://res.cloudinary.com/takuti/image/upload/l_text:'
    if front_matter['lang'] == 'ja':
        og_image += 'Sawarabi%20Gothic_32_bold:'
    else:
        og_image += 'Open%20Sans_32:'
    og_image += quote(front_matter['title'].replace('/', ' ')) + ',co_rgb:eee,w_800,c_fit/v1626628472/takuti_bgimyl.jpg'
    front_matter['images'] = [og_image]

    with open(path, 'w') as f:
        f.write(content.replace(m.group(1), yaml.dump(front_matter, allow_unicode=True)))


def run(lang):
    path_dir = os.path.join(os.path.dirname(__file__), '..', '_content', lang, 'note')
    paths = [os.path.join(path_dir, f) for f in os.listdir(path_dir)]

    res = recommend_content_based_cf(paths, topk=3)
    for path, keywords, recommend_permalinks in res:
        process_article(path, keywords, recommend_permalinks)


def main():
    run('en')
    run('ja')


if __name__ == '__main__':
    main()
