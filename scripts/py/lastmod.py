import os
import re
from pathlib import Path
from datetime import datetime

import git
from prelims import StaticSitePostsHandler
from prelims.processor import LastModifiedDateExtractor


class ContentOnlyLastModifiedDateExtractor(LastModifiedDateExtractor):
    """
    LastModified date extractor that only updates when actual content changes.

    This prevents infinite loops caused by front matter updates being counted
    as file changes.
    """

    def __init__(self):
        super().__init__()
        self._repo = None

    def process(self, posts, allow_overwrite=True):
        for post in posts:
            date = self._lastmod_from_git(post.path)
            post.update("lastmod", date, allow_overwrite)

    def _extract_front_matter(self, content):
        """Extract front matter and content separately."""
        # Match YAML front matter (--- ... ---)
        match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
        if match:
            return match.group(1), match.group(2)
        return "", content

    def _get_last_content_change_date(self, file_path):
        """Get the last commit date where actual content (not front matter) changed."""
        if self._repo is None:
            # Initialize repo on first use
            self._repo = git.Repo(search_parent_directories=True)

        try:
            # Ensure we have an absolute path
            abs_file_path = Path(file_path).resolve()

            # Get commit history for this file
            commits = list(self._repo.iter_commits(paths=str(abs_file_path)))

            # Read current content (excluding front matter)
            with open(abs_file_path, 'r', encoding='utf-8') as f:
                current_content = f.read()
            _, current_body = self._extract_front_matter(current_content)

            # Default to now if we can't find a change date
            last_content_change = datetime.now()

            # Check older commits to find if they have the same content
            # If an older commit has the same body, it means recent commits only changed front matter
            for commit in commits:
                try:
                    # Get file content at this commit
                    # Convert to posix path (forward slashes) for git tree navigation
                    relative_path = abs_file_path.relative_to(Path(self._repo.working_dir).resolve()).as_posix()
                    blob = commit.tree / relative_path
                    old_content = blob.data_stream.read().decode('utf-8')
                    _, old_body = self._extract_front_matter(old_content)

                    # If bodies match, this older commit had the same content
                    # Update the date to this older commit
                    if old_body.strip() == current_body.strip():
                        last_content_change = commit.committed_datetime
                    else:
                        # Content differs, we've found where it actually changed
                        break
                except Exception as e:
                    # File might not exist in this commit
                    break

            return last_content_change
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None

    def _lastmod_from_git(self, file_path):
        """Override to use content-only change detection."""
        lastmod = self._get_last_content_change_date(file_path)
        return lastmod.strftime('%Y-%m-%d') if lastmod else None


def run(lang):
    path_dir = os.path.join(
        os.path.dirname(__file__), '..', '..', '_content', lang)
    handler = StaticSitePostsHandler(path_dir)
    lastmod_extractor = ContentOnlyLastModifiedDateExtractor()
    handler.register_processor(lastmod_extractor)
    handler.execute()


def main():
    run('en')
    run('ja')
    run('fr')


if __name__ == '__main__':
    main()
