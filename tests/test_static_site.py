"""What the emitted HTML says: which links resolve, which assets are owned,
and the order and shape a listing page presents its contents in."""

from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path

import pytest
from conftest import fixture_repo, run_qualc
from qualc.emit import mathjax_header
from qualc.static_site import StandardPage, build_asset_catalog, write_page
from test_invariants import Element, read_html


def _mathjax_macros(header: str) -> dict[str, str]:
    match = re.search(r"macros: (\{.*?\}), inlineMath", header)
    assert match is not None, "the header must embed the macros JSON"
    parsed: dict[str, str] = json.loads(match.group(1))
    return parsed


def test_mathjax_macro_names_omit_the_tex_escape() -> None:
    header = mathjax_header({r"\DD": r"\mathbb{D}", r"\inner": r"\langle #1,#2\rangle"})

    macros = _mathjax_macros(header)
    assert macros["DD"] == r"\mathbb{D}"
    assert r"\DD" not in macros
    assert macros["inner"] == [r"\langle #1,#2\rangle", 2]


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []
        self.srcs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if value is None:
                continue
            if key == "href":
                self.hrefs.append(value)
            elif key == "src":
                self.srcs.append(value)


def test_nested_page_rewrites_card_and_asset_links(tmp_path: Path) -> None:
    assets_root = tmp_path / "assets"
    image = assets_root / "figures" / "diagram.png"
    image.parent.mkdir(parents=True)
    image.write_bytes(b"image")
    site_root = tmp_path / "_site"

    write_page(
        site_root,
        Path("tag/P-ONE.html"),
        {"title": "One"},
        '<p><a href="P-TWO">Two</a><a href="assets/figures/diagram.png">Asset</a><img src="../../assets/figures/diagram.png"></p>',
        "",
        {"P-TWO": Path("tag/P-TWO.html")},
        build_asset_catalog(assets_root),
        StandardPage(),
    )

    links = LinkCollector()
    links.feed((site_root / "tag" / "P-ONE.html").read_text())
    assert {"P-TWO.html", "../assets/figures/diagram.png"} <= set(links.hrefs)
    assert "../assets/figures/diagram.png" in links.srcs
    assert (site_root / "assets" / "figures" / "diagram.png").samefile(image)


def test_missing_asset_fails_the_build(tmp_path: Path) -> None:
    assets_root = tmp_path / "assets"
    assets_root.mkdir()

    with pytest.raises(ValueError, match="referenced asset does not exist"):
        write_page(
            tmp_path / "_site",
            Path("tag/P-ONE.html"),
            {"title": "One"},
            '<img src="../../assets/figures/missing.png">',
            "",
            {},
            build_asset_catalog(assets_root),
            StandardPage(),
        )


PACKET_PROBLEM = """---
schema: qual/card@1
id: P-PACKET-1
kind: problem
title: Classify the groups of order $pq$
classification:
  areas:
  - algebra
  topics:
  - Groups
relations: []
review: draft
---

::: problem
Let $p < q$ be primes. Classify the groups of order $pq$ up to isomorphism.
:::
"""

COMPILATION_LISTING_A_SIBLING = """---
schema: qual/card@1
id: SRC-PACKET
kind: collection
title: Algebra qual packet
classification:
  areas:
  - algebra
  topics:
  - Groups
relations: []
review: draft
source:
  source_kind: compilation
  area: algebra
  date:
    kind: year
    year: 2019
  sections:
  - name: Reprinted exam
    problems:
    - SRC-UGA-FIX
  - name: Additional problems
    problems:
    - P-PACKET-1
---

::: remark
A compilation reprints whole exams. Those entries are collections, not problems.
:::
"""


def test_every_internal_link_resolves_to_a_page_the_build_wrote(tmp_path: Path) -> None:
    """A card's page is under `exam/` or `tag/` by its kind, and links agree.

    `SRC-PACKET` lists a sibling collection among its contents, which is the
    shape the real compilations use. A link written for it as a problem points
    at `tag/SRC-UGA-FIX.html`, and nothing writes that file.
    """
    work = fixture_repo(
        tmp_path,
        {"SRC-PACKET.md": COMPILATION_LISTING_A_SIBLING, "P-PACKET-1.md": PACKET_PROBLEM},
    )

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    site = work / "build" / "quarto" / "_site"
    assert (site / "exam" / "SRC-PACKET.html").exists()

    # Card links only. A fixture corpus has no wiki, so the navbar's wiki entry
    # has nothing to resolve to and says nothing about how cards are routed.
    dead = []
    for page in sorted(site.rglob("*.html")):
        links = LinkCollector()
        links.feed(page.read_text())
        for href in links.hrefs:
            target = href.split("#")[0]
            if not re.search(r"(?:^|/)(?:tag|exam)/[A-Z]", target):
                continue
            if not (page.parent / target).resolve().exists():
                dead.append(f"{page.relative_to(site)} -> {href}")
    assert dead == []


def test_the_not_found_page_resolves_its_links_from_the_site_root(tmp_path: Path) -> None:
    """404.html is served for a request at any depth, so `../` cannot be used.

    It installs a `<base>` naming the site root instead, and that has to happen
    before the first URL in the head, or the stylesheet is fetched against the
    address the reader asked for and the page arrives unstyled.
    """
    work = fixture_repo(tmp_path)

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    page = (work / "build" / "quarto" / "_site" / "404.html").read_text()
    head = page.split("</head>", 1)[0]
    assert head.index('createElement("base")') < head.index('href="styles.css"')

    links = LinkCollector()
    links.feed(page)
    nav = [href for href in links.hrefs if not href.startswith("data:")]
    assert "problems.html" in nav
    assert [href for href in nav if href.startswith(("../", "/"))] == []


def _uga_sitting(card_id: str, year: int, term: str) -> str:
    return f"""---
schema: qual/card@1
id: {card_id}
kind: collection
title: UGA Algebra qualifying exam, {term.title()} {year}
classification:
  areas:
  - algebra
  topics:
  - Groups
relations: []
review: draft
source:
  source_kind: university-exam
  institution: uga
  area: algebra
  date:
    kind: academic-term
    year: {year}
    term: {term}
---

::: remark
One sitting.
:::
"""


def test_exams_lists_the_sittings_of_a_year_in_the_order_they_were_sat(tmp_path: Path) -> None:
    """Spring 2019 was sat before Fall 2019, so it is listed first.

    Ordering by card id put Fall ahead of Spring in every year on the real
    site, because `FALL` precedes `SPRING`.
    """
    work = fixture_repo(
        tmp_path,
        {
            "SRC-UGA-FALL-2019.md": _uga_sitting("SRC-UGA-FALL-2019", 2019, "fall"),
            "SRC-UGA-SPRING-2020.md": _uga_sitting("SRC-UGA-SPRING-2020", 2020, "spring"),
        },
    )

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    links = LinkCollector()
    links.feed((work / "build" / "quarto" / "_site" / "exams.html").read_text())
    # SRC-UGA-FIX is the fixture corpus's own Spring 2019 sitting.
    sittings = [href for href in links.hrefs if href.startswith("exam/SRC-UGA")]
    assert sittings == [
        "exam/SRC-UGA-FIX.html",
        "exam/SRC-UGA-FALL-2019.html",
        "exam/SRC-UGA-SPRING-2020.html",
    ]


def test_problem_filters_group_each_label_with_its_control(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path)

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    page = read_html(work / "build" / "quarto" / "_site" / "problems.html")
    filters = page.root.find_all("div", **{"class": "problem-filters"})
    assert len(filters) == 1
    labels = [child for child in filters[0].children if isinstance(child, Element) and child.tag == "label"]
    controls = [[child.tag for child in label.children if isinstance(child, Element)] for label in labels]
    assert controls == [["input"], ["select"], ["select"], ["select"], ["select"]]
