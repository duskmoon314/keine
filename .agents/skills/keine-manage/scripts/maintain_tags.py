"""
Build docs/tags index files from document frontmatter
"""

from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Tuple

import frontmatter

DOCS_DIR = Path("docs")
TAGS_DIR = DOCS_DIR / "tags"


def check_date_str(stem: str) -> bool:
    try:
        datetime.strptime(stem, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def scan_docs() -> Dict[str, List[Tuple[str, str, str, str]]]:
    """
    Scan all knowledge entries, Returns {tag: [(date, title, filename, description)]}
    """

    tag_map: Dict[str, List[Tuple[str, str, str, str]]] = defaultdict(list)

    for md_file in sorted(DOCS_DIR.glob("*.md")):
        # Only files starting with "yyyy-mm-dd" are valid entry
        # If not valid, skip
        date_prefix = md_file.stem[:10]
        if not check_date_str(date_prefix):
            continue

        with md_file.open() as f:
            post = frontmatter.load(f)

            title = post.get("title", md_file.stem)
            description = post.get("description", "")
            tags = post.get("tags", [])

            # Ensure tags is always a list
            if not isinstance(tags, list):
                tags = [tags] if tags else []

            for tag in tags:
                tag_map[str(tag)].append(
                    (date_prefix, str(title), md_file.name, str(description))
                )

    return tag_map


def write_tag_file(tag: str, entries: List[Tuple[str, str, str, str]]) -> Path:
    """
    Write a tag's index file
    """
    TAGS_DIR.mkdir(parents=True, exist_ok=True)

    entries.sort(key=lambda e: e[0], reverse=True)

    def format_entry(title: str, filename: str, description: str) -> str:
        line = f"- [{title}](../{filename})"
        if description:
            line += f" — {description}"
        return line

    with open(TAGS_DIR / f"{tag}.md", "w") as f:
        f.writelines(
            [
                "---\n",
                f"tag: {tag}\n",
                "---\n\n",
                "\n".join(
                    format_entry(title, filename, desc)
                    for _, title, filename, desc in entries
                ),
            ]
        )

    return TAGS_DIR / f"{tag}.md"


def remove_stale_tags(active_tags: Set[str]):
    """
    Remove stale tag files
    """
    if not TAGS_DIR.exists():
        return

    for tag_file in TAGS_DIR.glob("*.md"):
        tag = tag_file.stem
        if tag not in active_tags:
            tag_file.unlink()
            print(f"Removed stale tag file: {tag_file}")


def main():
    tag_map = scan_docs()

    print(f"Found {len(tag_map)} tags")

    for tag, entries in sorted(tag_map.items()):
        path = write_tag_file(tag, entries)
        print(f"{path} ({len(entries)} entries)")

    remove_stale_tags(set(tag_map.keys()))

    print("Done")


if __name__ == "__main__":
    main()
