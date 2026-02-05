#!/usr/bin/env python3
"""
Update article categories based on the category mapping.

This script processes all articles under _content/{en,ja}/note/* and applies
the Current -> New category mapping defined in category_mapping.md to the
categories front matter variable.
"""

import re
from pathlib import Path
from typing import List, Dict

# Category mapping for English articles
EN_MAPPING = {
    "Data Science & Analytics": "Data & Algorithms",
    "Machine Learning": "Data & Algorithms",
    "Recommender Systems": "Recommender Systems",
    "Programming": "Engineering",
    "Business": "Society & Business",
    "Life & Work": "Life & Reflection",
    "Design": "Design",
    "Conference": "Events",
}

# Category mapping for Japanese articles
JA_MAPPING = {
    "機械学習": "データ・アルゴリズム",
    "データサイエンス": "データ・アルゴリズム",
    "情報推薦": "推薦システム",
    "プログラミング": "エンジニアリング",
    "ビジネス": "社会・ビジネス",
    "生活・人生": "人生・思索",
    "エッセイ": "人生・思索",
    "デザイン": "デザイン",
    "読書記録": "読書",
    "イベント参加記": "イベント",
    "英語学習": "言語",
    "自然言語処理": "データ・アルゴリズム",
    "コンピュータシステム": "エンジニアリング",
}


def extract_front_matter(content: str) -> tuple:
    """
    Extract front matter from markdown content.

    Returns:
        tuple: (front_matter, body, start_delimiter, end_delimiter)
    """
    # Match YAML front matter delimited by ---
    pattern = r'^(---\n)(.*?)(---\n)(.*)'
    match = re.match(pattern, content, re.DOTALL)

    if match:
        return match.group(2), match.group(4), match.group(1), match.group(3)

    return None, content, None, None


def parse_categories(front_matter: str) -> tuple:
    """
    Parse categories from front matter.

    Returns:
        tuple: (categories_list, categories_line, other_front_matter)
    """
    categories = []
    categories_line = None
    other_lines = []

    for line in front_matter.split('\n'):
        if line.startswith('categories:'):
            categories_line = line
            # Extract categories from the list format
            # Format: categories: [Category1, Category2]
            match = re.search(r'\[(.*?)\]', line)
            if match:
                cats_str = match.group(1)
                # Split by comma and clean up
                categories = [cat.strip() for cat in cats_str.split(',')]
        else:
            other_lines.append(line)

    return categories, categories_line, '\n'.join(other_lines)


def map_categories(categories: List[str], mapping: Dict[str, str]) -> List[str]:
    """
    Apply category mapping to a list of categories.

    Returns:
        List of new categories (deduplicated and sorted)
    """
    new_categories = set()

    for cat in categories:
        # Map the category or keep it as is if not in mapping
        new_cat = mapping.get(cat, cat)
        new_categories.add(new_cat)

    # Return sorted list for consistency
    return sorted(list(new_categories))


def format_categories_line(categories: List[str]) -> str:
    """
    Format categories as a YAML list.
    """
    if not categories:
        return "categories: []"

    cats_str = ", ".join(categories)
    return f"categories: [{cats_str}]"


def update_article_categories(filepath: Path, mapping: Dict[str, str], dry_run: bool = False) -> dict:
    """
    Update categories in a single article file.

    Returns:
        dict with update information
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            'success': False,
            'error': f"Failed to read file: {e}",
            'filepath': str(filepath)
        }

    # Extract front matter
    front_matter, body, start_delim, end_delim = extract_front_matter(content)

    if front_matter is None:
        return {
            'success': False,
            'error': "No front matter found",
            'filepath': str(filepath)
        }

    # Parse categories
    categories, categories_line, other_front_matter = parse_categories(front_matter)

    if not categories_line:
        return {
            'success': False,
            'error': "No categories found in front matter",
            'filepath': str(filepath)
        }

    # Map categories
    old_categories = categories.copy()
    new_categories = map_categories(categories, mapping)

    # Check if anything changed
    if set(old_categories) == set(new_categories):
        return {
            'success': True,
            'changed': False,
            'filepath': str(filepath),
            'old_categories': old_categories,
            'new_categories': new_categories
        }

    # Format new categories line
    new_categories_line = format_categories_line(new_categories)

    # Reconstruct front matter
    new_front_matter_lines = []
    for line in front_matter.split('\n'):
        if line.startswith('categories:'):
            new_front_matter_lines.append(new_categories_line)
        else:
            new_front_matter_lines.append(line)

    new_front_matter = '\n'.join(new_front_matter_lines)

    # Reconstruct full content
    new_content = start_delim + new_front_matter + '\n' + end_delim + body

    # Write back to file (unless dry run)
    if not dry_run:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
        except Exception as e:
            return {
                'success': False,
                'error': f"Failed to write file: {e}",
                'filepath': str(filepath)
            }

    return {
        'success': True,
        'changed': True,
        'filepath': str(filepath),
        'old_categories': old_categories,
        'new_categories': new_categories
    }


def process_directory(dir_path: Path, mapping: Dict[str, str], dry_run: bool = False):
    """
    Process all markdown files in a directory.
    """
    results = {
        'total': 0,
        'changed': 0,
        'unchanged': 0,
        'errors': 0,
        'details': []
    }

    # Get all markdown and HTML files
    md_files = sorted(dir_path.glob('*.md'))
    html_files = sorted(dir_path.glob('*.html'))
    all_files = md_files + html_files

    for file_path in all_files:
        results['total'] += 1
        result = update_article_categories(file_path, mapping, dry_run)
        results['details'].append(result)

        if result['success']:
            if result.get('changed', False):
                results['changed'] += 1
            else:
                results['unchanged'] += 1
        else:
            results['errors'] += 1

    return results


def print_results(language: str, results: dict, verbose: bool = False):
    """
    Print processing results.
    """
    print(f"\n{'='*60}")
    print(f"{language} Articles Processing Results")
    print(f"{'='*60}")
    print(f"Total files processed: {results['total']}")
    print(f"Files changed: {results['changed']}")
    print(f"Files unchanged: {results['unchanged']}")
    print(f"Errors: {results['errors']}")

    if verbose:
        print(f"\n{'-'*60}")
        print("Detailed Changes:")
        print(f"{'-'*60}")

        for detail in results['details']:
            if detail['success'] and detail.get('changed', False):
                filename = Path(detail['filepath']).name
                print(f"\n{filename}")
                print(f"  Old: {detail['old_categories']}")
                print(f"  New: {detail['new_categories']}")

        if results['errors'] > 0:
            print(f"\n{'-'*60}")
            print("Errors:")
            print(f"{'-'*60}")
            for detail in results['details']:
                if not detail['success']:
                    filename = Path(detail['filepath']).name
                    print(f"\n{filename}")
                    print(f"  Error: {detail.get('error', 'Unknown error')}")


def main():
    """
    Main function to process all articles.
    """
    import argparse

    parser = argparse.ArgumentParser(
        description='Update article categories based on category mapping'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without modifying files'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed output'
    )
    parser.add_argument(
        '--workspace',
        type=str,
        default='/Users/takuti/src/github.com/takuti/takuti.me',
        help='Path to the workspace root'
    )

    args = parser.parse_args()

    workspace = Path(args.workspace)

    # Process English articles
    en_dir = workspace / '_content' / 'en' / 'note'
    if en_dir.exists():
        en_results = process_directory(en_dir, EN_MAPPING, args.dry_run)
        print_results("English", en_results, args.verbose)
    else:
        print(f"Error: English directory not found: {en_dir}")

    # Process Japanese articles
    ja_dir = workspace / '_content' / 'ja' / 'note'
    if ja_dir.exists():
        ja_results = process_directory(ja_dir, JA_MAPPING, args.dry_run)
        print_results("Japanese", ja_results, args.verbose)
    else:
        print(f"Error: Japanese directory not found: {ja_dir}")

    # Print summary
    if args.dry_run:
        print(f"\n{'='*60}")
        print("DRY RUN MODE - No files were modified")
        print("Run without --dry-run to apply changes")
        print(f"{'='*60}")


if __name__ == '__main__':
    main()
