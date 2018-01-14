import os
import re
import yaml
import MeCab
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

RE_FRONT_MATTER = re.compile('---\n([\s\S]*?\n)---\n')

tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
tagger.parse('')


def tokenizer(doc):
    # TODO: more aggressive preprocessing e.g., filtering out URLs
    def get_tokens(text):
        node = tagger.parseToNode(text)
        while node:
            yield node.surface.lower()
            node = node.next

    return [token for token in get_tokens(doc)]


def compute_similarities(paths):
    samples = []
    for path in paths:
        with open(path) as f:
            content = f.read()

        m = RE_FRONT_MATTER.search(content)

        # remove front matter
        content = content.replace(m.group(0), '')
        samples.append(content)

    vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, tokenizer=tokenizer)
    tfidf = vectorizer.fit_transform(samples)
    return cosine_similarity(tfidf)


def process_article(path, recommend_permalinks):
    with open(path) as f:
        content = f.read()

    m = RE_FRONT_MATTER.search(content)
    front_matter = yaml.load(m.group(1))

    front_matter['recommendations'] = recommend_permalinks
    with open(path, 'w') as f:
        f.write(content.replace(m.group(1), yaml.dump(front_matter, allow_unicode=True)))


def main():
    path_dir = os.path.join(os.path.dirname(__file__), '..', '_content', 'note')
    paths = [os.path.join(path_dir, f) for f in os.listdir(path_dir)]

    similarities = compute_similarities(paths)

    permalink_extractor = re.compile('(/note/.+?)(\.md|\.html)')
    for i, path in enumerate(paths):
        # find top-3 most-similar articles (except for target article itself which is similarity=1.0)
        top_indices = np.argsort(similarities[i, :])[::-1][1:4]
        process_article(path, [permalink_extractor.search(paths[j]).group(1) + '/' for j in top_indices])


if __name__ == '__main__':
    main()
