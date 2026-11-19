"""Every site page the README links to is a page the build emits.

The README is the front door: a reader who has not opened the site yet follows
its links, and they are absolute URLs, so nothing in the build can check them.
When the listing of sources moved from `exams.html` to `sources.html`, the
README kept naming the old page and "Browse sources" led to the 404 page until
someone read it. The routes the site emits are the four standard pages, the
wiki's own index, and one page per guide manifest, so those are what a README
link may name.
"""

from __future__ import annotations

import re

from conftest import ROOT
from qualc.publication import load_publications
from qualc.wiki import SITE_PAGES

SITE = "https://dzackgarza.github.io/new-qual-site/"
LINK = re.compile(re.escape(SITE) + r"([^\s)\]\"'>]*)")


def emitted_routes() -> set[str]:
    """The page paths the site builds, relative to the deployed root."""
    guides = {f"guide/{manifest.id}.html" for manifest in load_publications(ROOT / "publications")}
    return {"index.html", "wiki/index.html", *SITE_PAGES, *guides}


def test_readme_links_name_pages_the_site_builds() -> None:
    readme = (ROOT / "README.md").read_text()
    routes = emitted_routes()
    linked = [(line, path) for line, text in enumerate(readme.splitlines(), start=1) for path in LINK.findall(text)]
    assert linked, "README names no page of the site"
    dead = [(line, path) for line, path in linked if (path.split("?")[0].split("#")[0] or "index.html") not in routes]
    assert not dead, f"README links pages the site does not build: {dead}"
