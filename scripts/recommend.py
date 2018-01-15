import os
import re
import sys
import yaml
import binascii
import random
import MeCab
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

RE_FRONT_MATTER = re.compile('---\n([\s\S]*?\n)---\n')
RE_PATH_TO_PERMALINK = re.compile('(/note/.+?)(\.md|\.html)')

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


def extract_contents(paths):
    contents = []
    for path in paths:
        with open(path) as f:
            content = f.read()

        m = RE_FRONT_MATTER.search(content)

        # remove front matter
        content = content.replace(m.group(0), '')
        contents.append(content)
    return contents


def path_to_permalink(path):
    return RE_PATH_TO_PERMALINK.search(path).group(1) + '/'


def recommend_content_based_cf(paths, topk=3):
    """Content-based collaborative filtering
    """

    samples = extract_contents(paths)

    # build model
    vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, tokenizer=tokenizer)
    tfidf = vectorizer.fit_transform(samples)
    similarities = cosine_similarity(tfidf)

    for i, path in enumerate(paths):
        # find top-k most-similar articles (except for target article itself which is similarity=1.0)
        top_indices = np.argsort(similarities[i, :])[::-1][1:(topk + 1)]
        yield (path, [path_to_permalink(paths[j]) for j in top_indices])


def recommend_minhash(paths, n_hashes=10, n_shingle=3, topk=3):
    """MinHash-based approximated similarity computation

    References:
    - https://github.com/chrisjmccormick/MinHash/blob/master/runMinHashExample.py
    - http://i.stanford.edu/~ullman/mmds/ch3n.pdf
    """

    docs = extract_contents(paths)
    n_docs = len(docs)

    # convert doc string into a set of shingles
    docs_shingles = [set() for i in range(n_docs)]
    shingle_words = []
    for i, doc in enumerate(docs):
        for word in tokenizer(doc):
            shingle_words.append(word)

            # wait until `n_shingle` words are observed
            if len(shingle_words) < n_shingle:
                continue

            # hash the shingle to a 32-bit integer id
            shingle = ' '.join(shingle_words)
            shingle_id = binascii.crc32(shingle.encode()) & 0xffffffff

            docs_shingles[i].add(shingle_id)

            del shingle_words[0]

    max_shingle_id = 2 ** 32 - 1  # we created shingle id as a 32-bit integer
    prime_above_max_shingle_id = 4294967311  # http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php

    # make hash functions
    #   Our random hash function will take the form of:
    #     h(x) = (a*x + b) % c
    #   where 'x' is the input value, 'a' and 'b' are random coefficients, and 'c' is
    #   a prime number just greater than `max_shingle_id`.
    coefficients = []
    while len(coefficients) < n_hashes:
        a = random.randint(0, max_shingle_id)
        b = random.randint(0, max_shingle_id)

        # avoid to create the exactly same hash function
        if (a, b) not in coefficients:
            coefficients.append((a, b))

    # generate MinHash signatures
    docs_signatures = []
    for shingles in docs_shingles:

        # for each hash function
        signature = []
        for a, b in coefficients:
            min_hash = prime_above_max_shingle_id + 1
            for shingle in shingles:
                h = (a * shingle_id + b) % prime_above_max_shingle_id

                if h < min_hash:
                    min_hash = h
            signature.append(min_hash)

        docs_signatures.append(signature)

    for i in range(n_docs):
        jaccard_similarities = np.zeros(n_docs)
        i_signature = docs_signatures[i]
        for j in range(n_docs):
            if i == j:  # skip target doc itself; similarity = 1.0
                continue
            j_signature = docs_signatures[i]

            cnt = 0
            for k in range(n_hashes):
                cnt += (i_signature[k] == j_signature[k])

            jaccard_similarities[j] = cnt / n_hashes

        # find top-k most-similar articles
        top_indices = np.argsort(jaccard_similarities)[::-1][:topk]
        yield (paths[i], [path_to_permalink(paths[j]) for j in top_indices])


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

    if len(sys.argv) > 1 and sys.argv[1] == 'minhash':
        rec = recommend_minhash(paths, n_hashes=10, n_shingle=3, topk=3)
    else:
        rec = recommend_content_based_cf(paths, topk=3)

    for path, recos in rec:
        process_article(path, recos)


if __name__ == '__main__':
    main()
