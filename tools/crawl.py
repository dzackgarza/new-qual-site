"""Follow every link of the built site from the home page.

`qualc check` resolves each link against the pages the build will write, and
`test_every_internal_link_resolves_to_a_page_the_build_wrote` holds that. Neither
answers the other direction: whether a reader starting at the home page can get
to a page at all. A collection and the problems it lists link each other, so a
group of pages can resolve every link it writes and still be an island nothing
outside it points at.

Run it after `just build`:

    uv run python tools/crawl.py
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
import urllib.parse

SITE = pathlib.Path(__file__).resolve().parent.parent / "build" / "quarto" / "_site"
LINK = re.compile(r'(?:href|src)="([^"]+)"')
OFF_SITE = ("http:", "https:", "mailto:", "data:", "#", "//", "${")


def targets(page: pathlib.Path) -> list[pathlib.Path]:
    """What one page points at, as paths on disk."""
    out: list[pathlib.Path] = []
    for raw in LINK.findall(page.read_text(errors="replace")):
        if raw.startswith(OFF_SITE):
            continue
        path = urllib.parse.unquote(raw.split("#")[0].split("?")[0])
        if not path:
            continue
        base = SITE if path.startswith("/") else page.parent
        target = (base / path.lstrip("/")).resolve()
        out.append((target / "index.html").resolve() if target.is_dir() else target)
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--links-only",
        action="store_true",
        help="fail only on broken internal links/assets; do not fail on orphan pages",
    )
    args = parser.parse_args(argv)

    pages = {p.resolve() for p in SITE.rglob("*.html")}
    # Nothing links the 404 page: the server serves it for a path that is not a
    # page, so it is unreachable by construction rather than by defect.
    roots = {(SITE / "404.html").resolve()}
    broken: list[tuple[str, str]] = []

    # Link validity is a property of every published page, including pages that
    # are currently unreachable from the home page. Reachability is a separate
    # graph question below.
    for page in sorted(pages):
        for target in targets(page):
            if not target.exists():
                broken.append(
                    (
                        str(page.relative_to(SITE)),
                        str(target.relative_to(SITE)) if target.is_relative_to(SITE) else str(target),
                    )
                )

    seen: set[pathlib.Path] = set()
    queue = [(SITE / "index.html").resolve()]
    while queue:
        page = queue.pop()
        if page in seen:
            continue
        seen.add(page)
        for target in targets(page):
            if target.exists() and target.suffix == ".html" and target not in seen:
                queue.append(target)
    orphans = sorted(str(p.relative_to(SITE)) for p in pages - seen - roots)
    print(f"{len(pages)} pages, {len(seen & pages)} reachable from the home page")
    for source, target_name in broken:
        print(f"  broken: {source} -> {target_name}")
    if not args.links_only:
        for orphan in orphans:
            print(f"  nothing links {orphan}")
    return 1 if broken or (orphans and not args.links_only) else 0


if __name__ == "__main__":
    sys.exit(main())
