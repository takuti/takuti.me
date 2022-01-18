import os
import re
import MeCab
import requests

from prelims import StaticSitePostsHandler
from prelims.processor import OpenGraphMediaExtractor, Recommender


RE_VALID_WORD = re.compile(r'^[ぁ-んーァ-ヶー一-龠a-zA-Zａ-ｚＡ-Ｚ]+$')
RE_INVALID_WORD = re.compile(r'^([^一-龠]{1,2}|[ぁ-んー]{1,3})$')


tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
tagger.parse('')


# https://gist.github.com/sebleier/554280
STOPWORDS_GIST = 'https://gist.githubusercontent.com/rg089/' + \
    '35e00abf8941d72d419224cfd5b5925d/raw/' + \
    '12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt'
stopwords_list = requests.get(STOPWORDS_GIST).content
stopwords = set(stopwords_list.decode().splitlines())


def tokenizer(doc):
    # TODO: more aggressive preprocessing e.g., filtering out URLs
    def get_tokens(text):
        node = tagger.parseToNode(text)
        while node:
            yield node.surface.lower()
            node = node.next

    return [token for token in get_tokens(doc)
            if 2 <= len(token) <= 15 and
            RE_VALID_WORD.match(token) and
            not RE_INVALID_WORD.match(token) and
            token not in stopwords]


def run(lang):
    path_dir = os.path.join(
        os.path.dirname(__file__), '..', '..', '_content', lang, 'note')
    permalink_base = '' if lang == 'en' else '/ja'
    permalink_base += '/note'
    handler = StaticSitePostsHandler(path_dir)
    recommender = Recommender(permalink_base=permalink_base, max_df=0.95,
                              tokenizer=tokenizer)
    handler.register_processor(recommender)
    file_path_extractor = OpenGraphMediaExtractor(image_base='/images')
    handler.register_processor(file_path_extractor)
    handler.execute()


def main():
    run('en')
    run('ja')


if __name__ == '__main__':
    main()
