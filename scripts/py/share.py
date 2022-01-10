import os
import re
import sys
import tweepy
from git import Repo
from prelims import Post
from urllib.parse import urljoin


BASE_URL = 'https://takuti.me'
DEFAULT_LANG = 'en'
CONTENT_PATH_BASE = '_content/'
RE_CONTENT_FILE_PATH = re.compile(
    r'^_content/((en|ja)/(note/(.+?)))(\.md|\.html)$')


def is_new_file(stat_dict):
    """
    >>> is_new_file({'insertions': 1, 'deletions': 1, 'lines': 2})
    False

    >>> is_new_file({'insertions': 72, 'deletions': 0, 'lines': 72})
    True

    >>> is_new_file({'insertions': 3, 'deletions': 3, 'lines': 3})
    False
    """
    return stat_dict['insertions'] == stat_dict['lines'] and \
        stat_dict['deletions'] == 0


def get_new_contents(commit):
    for path, stat_dict in commit.stats.files.items():
        if is_new_file(stat_dict) and \
                RE_CONTENT_FILE_PATH.match(path) is not None:
            yield Post.load(path)


def get_summary(post, splitter='\n'):
    r"""Follow Hugo's summary selection order.

    https://gohugo.io/content-management/summaries/#summary-selection-order

    >>> get_summary(Post('', {}, '', 'Hello, world.'))
    'Hello, world.'

    >>> get_summary(Post('', {}, '', 'Hello\nworld.'))
    'Hello'

    >>> get_summary(Post('', {}, '', 'Hello\nworld.\n\n<!--more-->Foo\nBar'),
    ...             splitter='<!--more-->')
    'Hello\nworld.'

    >>> get_summary(Post('', {'summary': 'Good morning'}, '', 'Hello, world.'))
    'Good morning'
    """
    if 'summary' in post.front_matter:
        return post.front_matter['summary']
    return post.content.split(splitter)[0].strip()


def path_to_url(path):
    """
    >>> path_to_url('_content/en/note/aaa.md')
    'https://takuti.me/note/aaa/'

    >>> path_to_url('_content/ja/note/aaa.md')
    'https://takuti.me/ja/note/aaa/'

    >>> path_to_url('_content/ja/note/bbb.html')
    'https://takuti.me/ja/note/bbb/'
    """
    m = RE_CONTENT_FILE_PATH.search(path)
    assert m is not None
    lang = m.group(2)
    permalink = m.group(3) if lang == DEFAULT_LANG else m.group(1)
    return urljoin(BASE_URL, permalink) + '/'


def tweet(text):
    auth = tweepy.OAuthHandler(os.environ.get('TWITTER_CONSUMER_KEY'),
                               os.environ.get('TWITTER_CONSUMER_SECRET'))
    auth.set_access_token(os.environ.get('TWITTER_ACCESS_TOKEN'),
                          os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'))
    api = tweepy.API(auth)
    res = api.update_status(text)
    print(f'Tweeted: {text}')
    print(res)


def run():
    root_dir = os.path.join(os.path.dirname(__file__), '..', '..')
    repo = Repo(root_dir)
    assert not repo.bare

    reference_commit = repo.head.commit if len(sys.argv) == 1 \
        else repo.commit(sys.argv[1])

    posts = list(get_new_contents(reference_commit))
    if len(posts) != 1:
        print(f'{len(posts)} new contents are in the latest commit. Skipping.')
        return
    summary = get_summary(posts[0])
    url = path_to_url(posts[0].path)
    tweet(f'{summary} {url}')


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    run()
