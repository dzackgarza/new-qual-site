"""Wiki filesystem measurements for a human to read.

Named for exactly what they measured. They do not decide titles, sameness,
classification, or whether a body is empty enough to discard. They are not
wired to `qualc check`, `just test`, or the build: a finding is a candidate,
never an instruction to act.

    uv run python tools/wiki_doctor.py
    uv run python tools/wiki_doctor.py --json
    uv run python tools/wiki_doctor.py --only obsidian-embed-syntax
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from qualc.wiki import _split_front_matter, discover

REPO = Path(__file__).resolve().parent.parent

ORDER_FLOOR = 100001

HEADING_LINE = re.compile(r"^#{1,6}\s+\S")
WIKILINK_LINE = re.compile(r"^\s*(?:[-*]\s+(?:\[[ xX]\]\s+)?|\d+\.\s+)?!?\[\[[^\]\n]+\]\]\s*$")
TASK_LIST_ITEM = re.compile(r"^\s*(?:[-*]|\d+\.)\s+\[[ xX]\]\s+")
HASH_RESOURCES_ONLY = re.compile(r"^\s*#resources/\S+\s*$")
TAGS_COLON = re.compile(r"^\s*Tags:")
# The wiki marker "#todo" is matched as a whole token (never "#todolist", never inside a URL) because Obsidian tags are complete words.
HASH_TODO = re.compile(r"(?<![/\w])#todo\b")  # grain: ignore (wiki tag)
OBSIDIAN_EMBED = re.compile(r"!\[\[")
# Host-shaped notion.so / notion.site only — not mynotion.so or notion.soccer.
NOTION_HOST = re.compile(r"(?:^|[/.])notion\.(?:so|site)(?:/|$|\?|#)")


@dataclass
class PageRecord:
    rel: Path
    metadata: dict[str, object]
    body: str


@dataclass
class Check:
    name: str
    findings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.findings


def _wiki_label(rel: Path) -> str:
    return f"wiki/{rel.as_posix()}"


def load_pages(wiki_root: Path) -> tuple[list[PageRecord], list[str]]:
    pages: list[PageRecord] = []
    unreadable: list[str] = []
    if not wiki_root.is_dir():
        return pages, unreadable
    for path in discover(wiki_root):
        rel = path.relative_to(wiki_root)
        try:
            metadata, body = _split_front_matter(path.read_text(), path)
        except (OSError, TypeError, ValueError, yaml.YAMLError) as exc:
            unreadable.append(f"{_wiki_label(rel)}: {exc}")
            continue
        pages.append(PageRecord(rel=rel, metadata=metadata, body=body))
    return pages, unreadable


def check_unreadable_wiki_pages(_pages: list[PageRecord], unreadable: list[str]) -> Check:
    return Check("unreadable-wiki-pages", sorted(unreadable))


def check_empty_bodies(pages: list[PageRecord]) -> Check:
    return Check(
        "empty-bodies",
        sorted(_wiki_label(page.rel) for page in pages if not page.body.strip()),
    )


def check_order_at_least_100001(pages: list[PageRecord]) -> Check:
    findings: list[str] = []
    for page in pages:
        value = page.metadata.get("order")
        if isinstance(value, bool) or not isinstance(value, int):
            continue
        if value >= ORDER_FLOOR:
            findings.append(f"{_wiki_label(page.rel)}: order {value}")
    return Check("order-at-least-100001", sorted(findings))


def check_one_markdown_child_directories(pages: list[PageRecord]) -> Check:
    """A directory whose markdown children are index.md and exactly one other
    file, with no markdown in any subdirectory."""
    by_dir: dict[Path, list[PageRecord]] = defaultdict(list)
    for page in pages:
        by_dir[page.rel.parent].append(page)
    findings: list[str] = []
    for directory, members in by_dir.items():
        indexes = [page for page in members if page.rel.stem.lower() == "index"]
        others = [page for page in members if page.rel.stem.lower() != "index"]
        if len(indexes) != 1 or len(others) != 1:
            continue
        descendants = [page for page in pages if directory in page.rel.parents and page.rel.parent != directory]
        if descendants:
            continue
        child = others[0].rel.name
        location = "wiki" if directory == Path(".") else _wiki_label(directory)
        findings.append(f"{location} (index.md + {child})")
    return Check("one-markdown-child-directories", sorted(findings))


def check_sibling_duplicate_titles(pages: list[PageRecord]) -> Check:
    """Two or more pages in one directory share the same authored title: value.

    Pages with no title field are not given one."""
    by_parent_title: dict[tuple[Path, str], list[str]] = defaultdict(list)
    for page in pages:
        title = page.metadata.get("title")
        if not isinstance(title, str) or not title.strip():
            continue
        by_parent_title[(page.rel.parent, title.strip())].append(page.rel.name)
    findings = [
        (f"{'wiki' if parent == Path('.') else _wiki_label(parent)}: title {title!r} on {', '.join(sorted(names))}")
        for (parent, title), names in by_parent_title.items()
        if len(names) > 1
    ]
    return Check("sibling-duplicate-titles", sorted(findings))


def check_obsidian_embed_syntax(pages: list[PageRecord]) -> Check:
    return Check(
        "obsidian-embed-syntax",
        sorted(_wiki_label(page.rel) for page in pages if OBSIDIAN_EMBED.search(page.body)),
    )


def check_notion_so_or_notion_site_urls(pages: list[PageRecord]) -> Check:
    return Check(
        "notion-so-or-notion-site-urls",
        sorted(_wiki_label(page.rel) for page in pages if NOTION_HOST.search(page.body)),
    )


def check_hash_todo_markers(pages: list[PageRecord]) -> Check:
    return Check(
        "hash-todo-markers",
        sorted(_wiki_label(page.rel) for page in pages if HASH_TODO.search(page.body)),
    )


def check_tags_colon_lines(pages: list[PageRecord]) -> Check:
    return Check(
        "tags-colon-lines",
        sorted(_wiki_label(page.rel) for page in pages if any(TAGS_COLON.match(line) for line in page.body.splitlines())),
    )


def check_hash_resources_only_lines(pages: list[PageRecord]) -> Check:
    return Check(
        "hash-resources-only-lines",
        sorted(_wiki_label(page.rel) for page in pages if any(HASH_RESOURCES_ONLY.match(line) for line in page.body.splitlines())),
    )


def check_task_list_item_lines(pages: list[PageRecord]) -> Check:
    findings: list[str] = []
    for page in pages:
        count = sum(1 for line in page.body.splitlines() if TASK_LIST_ITEM.match(line))
        if count:
            findings.append(f"{_wiki_label(page.rel)}: {count}")
    return Check("task-list-item-lines", sorted(findings))


def check_heading_or_wikilink_only_bodies(pages: list[PageRecord]) -> Check:
    """Every non-blank line is an ATX heading or a wikilink (optional list marker).

    Empty bodies are `empty-bodies`, not this check."""
    findings: list[str] = []
    for page in pages:
        lines = [line for line in page.body.splitlines() if line.strip()]
        if not lines:
            continue
        if all(HEADING_LINE.match(line) or WIKILINK_LINE.match(line) for line in lines):
            findings.append(_wiki_label(page.rel))
    return Check("heading-or-wikilink-only-bodies", sorted(findings))


CHECKS = {
    "empty-bodies": check_empty_bodies,
    "order-at-least-100001": check_order_at_least_100001,
    "one-markdown-child-directories": check_one_markdown_child_directories,
    "sibling-duplicate-titles": check_sibling_duplicate_titles,
    "obsidian-embed-syntax": check_obsidian_embed_syntax,
    "notion-so-or-notion-site-urls": check_notion_so_or_notion_site_urls,
    "hash-todo-markers": check_hash_todo_markers,
    "tags-colon-lines": check_tags_colon_lines,
    "hash-resources-only-lines": check_hash_resources_only_lines,
    "task-list-item-lines": check_task_list_item_lines,
    "heading-or-wikilink-only-bodies": check_heading_or_wikilink_only_bodies,
}
ALL = ["unreadable-wiki-pages", *CHECKS]


def run(names: list[str], *, root: Path = REPO) -> list[Check]:
    pages, unreadable = load_pages(root / "wiki")
    checks: list[Check] = []
    for name in names:
        if name == "unreadable-wiki-pages":
            checks.append(check_unreadable_wiki_pages(pages, unreadable))
        else:
            checks.append(CHECKS[name](pages))
    return checks


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="wiki_doctor")
    ap.add_argument("--root", type=Path, default=REPO)
    ap.add_argument("--only", action="append", choices=ALL, help="run one check (repeatable)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--full", action="store_true", help="print every finding, not the first 20")
    args = ap.parse_args(argv)

    checks = run(args.only or ALL, root=args.root)
    if args.json:
        print(
            json.dumps(
                [
                    {
                        "check": check.name,
                        "ok": check.ok,
                        "findings": check.findings,
                    }
                    for check in checks
                ],
                indent=2,
            )
        )
    else:
        for check in checks:
            status = "ok" if check.ok else f"{len(check.findings)} finding(s)"
            print(f"{check.name}: {status}")
            shown = check.findings if args.full else check.findings[:20]
            for line in shown:
                print(f"    {line}")
            if not args.full and len(check.findings) > 20:
                print(f"    ... {len(check.findings) - 20} more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
