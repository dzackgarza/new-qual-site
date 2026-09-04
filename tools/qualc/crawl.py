"""Follow every reader-visible navigation edge of the built site from home.

`qualc check` resolves each link against the pages the build will write, and
`test_every_internal_link_resolves_to_a_page_the_build_wrote` holds that. Neither
answers the other direction: whether a reader starting at the home page can get
to a page at all. A collection and the problems it lists link each other, so a
group of pages can resolve every link it writes and still be an island nothing
outside it points at.

Not every reader-visible edge is a literal ``href`` in the emitted HTML. The
problem and source browsers load canonical URLs from JSON, and the global
Pagefind search can reach every indexed document. Those are navigation surfaces,
not exceptions to reachability, so this crawler follows them explicitly. It also
validates the JSON-backed URLs as internal links; otherwise a broken browser row
could pass ``--links-only`` merely because JavaScript creates its anchor later.

Run it after `just build`:

    uv run python tools/crawl.py
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import urllib.parse
from dataclasses import dataclass
from typing import Any

SITE = pathlib.Path(__file__).resolve().parents[2] / "build" / "quarto" / "_site"
LINK = re.compile(r'(?:href|src)="([^"]+)"')
OFF_SITE = ("http:", "https:", "mailto:", "data:", "#", "//", "${")
DATA_URLS = ("problems.json", "sources.json", "collection-problems.json")


@dataclass(frozen=True)
class CrawlResult:
    pages: frozenset[pathlib.Path]
    seen: frozenset[pathlib.Path]
    broken: tuple[tuple[str, str], ...]
    orphans: tuple[str, ...]


def _target(raw: str, base: pathlib.Path, site: pathlib.Path) -> pathlib.Path | None:
    if raw.startswith(OFF_SITE):
        return None
    path = urllib.parse.unquote(raw.split("#")[0].split("?")[0])
    if not path:
        return None
    parent = site if path.startswith("/") else base
    target = (parent / path.lstrip("/")).resolve()
    return (target / "index.html").resolve() if target.is_dir() else target


def targets(page: pathlib.Path, site: pathlib.Path = SITE) -> list[pathlib.Path]:
    """What one page points at, as paths on disk."""
    out: list[pathlib.Path] = []
    for raw in LINK.findall(page.read_text(errors="replace")):
        target = _target(raw, page.parent, site)
        if target is not None:
            out.append(target)
    return out


def _json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text())


def browser_targets(site: pathlib.Path = SITE) -> dict[pathlib.Path, list[pathlib.Path]]:
    """Canonical URLs rendered by the JavaScript problem/source browsers."""
    out: dict[pathlib.Path, list[pathlib.Path]] = {}
    for page_name, data_name in (("problems.html", "problems.json"), ("exams.html", "sources.json")):
        data_path = site / data_name
        if not data_path.exists():
            continue
        rows = _json(data_path)["rows"]
        out[(site / page_name).resolve()] = [target for row in rows if (target := _target(row["url"], site, site)) is not None]
    return out


def data_urls(site: pathlib.Path = SITE) -> list[tuple[str, pathlib.Path]]:
    """Every internal URL that client-side catalog code can turn into an anchor."""
    out: list[tuple[str, pathlib.Path]] = []
    for name in DATA_URLS:
        path = site / name
        if not path.exists():
            continue
        data = _json(path)
        urls: list[str]
        if name == "collection-problems.json":
            urls = [item["url"] for source in data.values() for item in source["items"]]
        else:
            urls = [row["url"] for row in data["rows"]]
        for raw in urls:
            target = _target(raw, site, site)
            if target is not None:
                out.append((name, target))
    return out


def crawl(site: pathlib.Path = SITE) -> CrawlResult:
    site = site.resolve()
    pages = frozenset(p.resolve() for p in site.rglob("*.html"))
    # These are server/compatibility routes, not destinations a reader is
    # expected to discover in navigation.
    roots = {(site / "404.html").resolve(), (site / "generate.html").resolve()}
    broken: list[tuple[str, str]] = []

    # Link validity is a property of every published page, including pages that
    # are currently unreachable from home. Reachability is a separate graph
    # question below.
    for page in sorted(pages):
        for target in targets(page, site):
            if not target.exists():
                broken.append(
                    (
                        str(page.relative_to(site)),
                        str(target.relative_to(site)) if target.is_relative_to(site) else str(target),
                    )
                )

    # DataTables creates these anchors at runtime, so validate them separately.
    for source, target in data_urls(site):
        if not target.exists():
            broken.append(
                (
                    source,
                    str(target.relative_to(site)) if target.is_relative_to(site) else str(target),
                )
            )

    indexed = frozenset(page for page in pages if "data-pagefind-body" in page.read_text(errors="replace"))
    dynamic = browser_targets(site)
    seen: set[pathlib.Path] = set()
    queue = [(site / "index.html").resolve()]
    search_opened = False
    while queue:
        page = queue.pop()
        if page in seen:
            continue
        seen.add(page)
        if not page.exists() or page.suffix != ".html":
            continue
        text = page.read_text(errors="replace")
        outgoing = targets(page, site)
        if page in dynamic:
            outgoing.extend(dynamic[page])
        # The shared search dialog is a genuine site-wide navigation surface.
        # Pagefind indexes precisely the documents marked data-pagefind-body;
        # once a reachable page exposes that dialog, all indexed documents are
        # discoverable through search results.
        if not search_opened and 'id="site-search"' in text:
            outgoing.extend(indexed)
            search_opened = True
        for target in outgoing:
            if target.exists() and target.suffix == ".html" and target not in seen:
                queue.append(target)

    orphans = tuple(sorted(str(p.relative_to(site)) for p in pages - seen - roots))
    return CrawlResult(
        pages=pages,
        seen=frozenset(seen),
        broken=tuple(broken),
        orphans=orphans,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--links-only",
        action="store_true",
        help="fail only on broken internal links/assets; do not fail on orphan pages",
    )
    args = parser.parse_args(argv)

    result = crawl()
    print(f"{len(result.pages)} pages, {len(result.seen & result.pages)} reachable from the home page")
    for source, target_name in result.broken:
        print(f"  broken: {source} -> {target_name}")
    if not args.links_only:
        for orphan in result.orphans:
            print(f"  nothing links {orphan}")
    return 1 if result.broken or (result.orphans and not args.links_only) else 0


if __name__ == "__main__":
    sys.exit(main())
