import os

from prelims import StaticSitePostsHandler
from prelims.processor import LastModifiedDateExtractor


def run(lang):
    path_dir = os.path.join(
        os.path.dirname(__file__), '..', '..', '_content', lang)
    handler = StaticSitePostsHandler(path_dir)
    lastmod_extractor = LastModifiedDateExtractor()
    handler.register_processor(lastmod_extractor)
    handler.execute()


def main():
    run('en')
    run('ja')


if __name__ == '__main__':
    main()
