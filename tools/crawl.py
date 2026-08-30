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

import collections
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


def main() -> int:
    pages = {p.resolve() for p in SITE.rglob("*.html")}
    # Nothing links the 404 page: the server serves it for a path that is not a
    # page, so it is unreachable by construction rather than by defect.
    roots = {(SITE / "404.html").resolve()}
    broken: collections.Counter[str] = collections.Counter()
    seen: set[pathlib.Path] = set()
    queue = [(SITE / "index.html").resolve()]
    while queue:
        page = queue.pop()
        if page in seen:
            continue
        seen.add(page)
        for target in targets(page):
            if not target.exists():
                broken[str(page.relative_to(SITE))] += 1
            elif target.suffix == ".html" and target not in seen:
                queue.append(target)
    orphans = sorted(str(p.relative_to(SITE)) for p in pages - seen - roots)
    print(f"{len(pages)} pages, {len(seen & pages)} reachable from the home page")
    for source, count in broken.most_common():
        print(f"  {source}: {count} link(s) to a page that is not there")
    for orphan in orphans:
        print(f"  nothing links {orphan}")
    return 1 if broken or orphans else 0


if __name__ == "__main__":
    sys.exit(main())
