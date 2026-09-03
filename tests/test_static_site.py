"""What the emitted HTML says: which links resolve, which assets are owned,
and the order and shape a listing page presents its contents in."""

from __future__ import annotations

import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path

import pytest
from conftest import fixture_repo, run_qualc
from qualc.emit import mathjax_header
from qualc.static_site import Listing, StandardPage, build_asset_catalog, write_page
from test_invariants import Element, read_html

LISTING_KEY = re.compile(r'data-pagefind-sort="listing:([^"]*)"')


def listing_key(page: Path) -> str:
    """The order key a page carries, which is the order its listing shows."""
    match = LISTING_KEY.search(page.read_text())
    assert match is not None, f"no listing sort key on {page}"
    return html.unescape(match.group(1))


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
        StandardPage(Listing()),
    )

    links = LinkCollector()
    links.feed((site_root / "tag" / "P-ONE.html").read_text())
    assert {"P-TWO.html", "../assets/figures/diagram.png"} <= set(links.hrefs)
    assert "../assets/figures/diagram.png" in links.srcs
    assert (site_root / "assets" / "figures" / "diagram.png").samefile(image)


def test_every_page_carries_generation_and_repository_footer(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    revision = "0123456789abcdef0123456789abcdef01234567"
    monkeypatch.setenv("GITHUB_SHA", revision)
    assets_root = tmp_path / "assets"
    assets_root.mkdir()
    site_root = tmp_path / "_site"

    write_page(
        site_root,
        Path("tag/P-FOOTER.html"),
        {"title": "Footer fixture"},
        "<p>Mathematics.</p>",
        "",
        {},
        build_asset_catalog(assets_root),
        StandardPage(Listing()),
    )

    built = read_html(site_root / "tag" / "P-FOOTER.html")
    footer = built.root.find_all("footer", **{"class": "site-footer"})
    assert len(footer) == 1
    times = footer[0].find_all("time")
    assert len(times) == 1
    assert times[0].text.startswith("Generated ")
    assert times[0].attrs["datetime"].endswith("Z")
    revision_links = [a for a in footer[0].find_all("a") if a.text == "Revision 012345678"]
    assert len(revision_links) == 1
    assert revision_links[0].attrs["href"] == f"https://github.com/dzackgarza/new-qual-site/commit/{revision}"
    source = footer[0].find_all("a", **{"class": "footer-repository"})
    assert len(source) == 1
    assert source[0].attrs["href"] == "https://github.com/dzackgarza/new-qual-site"
    assert source[0].attrs["aria-label"] == "Source repository on GitHub"
    assert source[0].find_all("svg") != []


def test_problem_lists_survive_display_math_and_keep_nested_items(tmp_path: Path) -> None:
    """Display math inside one item must not flatten the authored list to prose."""
    card = r"""---
schema: qual/card@1
id: P-LIST
kind: problem
title: Units and maximal ideals in a power-series ring
classification:
  areas: [algebra]
  topics: [Rings]
relations: []
review: draft
---

::: problem
Let $R$ be a ring.

- Show that
  $$
  \sum_{i=0}^\infty a_i x^i \in R[[x]]^\times \iff a_0 \in R^\times.
  $$
- If $R$ is a field:
  - show that the zero-constant-term series form a maximal ideal;
  - show that it is the unique maximal ideal.
:::
"""
    work = fixture_repo(tmp_path, {"P-LIST.md": card})

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    page = read_html(work / "build" / "quarto" / "_site" / "tag" / "P-LIST.html")
    statement = page.root.find_all("div", **{"class": "card-statement"})[0]
    assert len(statement.find_all("ul")) == 2
    assert any(item.find_all("ul") for item in statement.find_all("li"))
    assert any(item.find_all("span", **{"class": "math display"}) for item in statement.find_all("li"))


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
            StandardPage(Listing()),
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
    """A card's page is under `exam/`, `source/` or `tag/`, and links agree.

    `SRC-PACKET` lists a sibling collection among its contents, which is the
    shape the real compilations use. A link written for it as a problem points
    at `tag/SRC-UGA-FIX.html`, and nothing writes that file.
    """
    work = fixture_repo(
        tmp_path,
        {
            "SRC-PACKET.md": COMPILATION_LISTING_A_SIBLING,
            "P-PACKET-1.md": PACKET_PROBLEM,
        },
    )

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    site = work / "build" / "quarto" / "_site"
    assert (site / "source" / "SRC-PACKET.html").exists()

    # Card links only. A fixture corpus has no wiki, so the navbar's wiki entry
    # has nothing to resolve to and says nothing about how cards are routed.
    dead = []
    for page in sorted(site.rglob("*.html")):
        links = LinkCollector()
        links.feed(page.read_text())
        for href in links.hrefs:
            target = href.split("#")[0]
            if not re.search(r"(?:^|/)(?:tag|exam|source)/[A-Z]", target):
                continue
            if not (page.parent / target).resolve().exists():
                dead.append(f"{page.relative_to(site)} -> {href}")
    assert dead == []


def test_the_not_found_page_resolves_its_links_from_the_site_root(
    tmp_path: Path,
) -> None:
    """404.html is served for a request at any depth, so `../` cannot be used.

    It installs a `<base>` naming the site root instead. The stylesheet and the
    script cannot be written as tags at all: Chrome's preload scanner fetches
    them against the address the reader asked for before any script runs, and
    the page arrives unstyled. The same script that sets the base creates them.
    """
    work = fixture_repo(tmp_path)

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    page = (work / "build" / "quarto" / "_site" / "404.html").read_text()
    head = page.split("</head>", 1)[0]
    assert 'href="styles.css"' not in head
    assert 'src="app.js"' not in head
    assert head.index('createElement("base")') < head.index('root + "styles.css"')
    assert 'root + "app.js"' in head

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


def test_exams_lists_the_sittings_of_a_year_in_the_order_they_were_sat(
    tmp_path: Path,
) -> None:
    """Spring 2019 was sat before Fall 2019, so it is listed first.

    Ordering by card id put Fall ahead of Spring in every year on the real
    site, because `FALL` precedes `SPRING`. The listing asks the index for the
    rows it shows, so the order it shows them in is the key each page carries.
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

    site = work / "build" / "quarto" / "_site"
    # SRC-UGA-FIX is the fixture corpus's own Spring 2019 sitting.
    sittings = ["SRC-UGA-FIX", "SRC-UGA-FALL-2019", "SRC-UGA-SPRING-2020"]
    keyed = sorted(sittings, key=lambda name: listing_key(site / "exam" / f"{name}.html"))
    assert keyed == sittings


FORMULA_TITLED_PROBLEM = """---
schema: qual/card@1
id: P-PACKET-2
kind: problem
title: $\\mathbb{Z}[x]$ is not a principal ideal domain
classification:
  areas:
  - algebra
  topics:
  - Groups
relations: []
review: draft
---

::: problem
Exhibit an ideal of $\\mathbb{Z}[x]$ that no single element generates.
:::
"""


def test_the_problem_browser_groups_by_area_and_leads_with_prose_titles(
    tmp_path: Path,
) -> None:
    """483 of the 4921 titles begin with mathematics, and `$` sorts under every
    letter, so ordering by the raw title opened the page on a wall of formulas
    with nothing above them naming a subject.
    """
    work = fixture_repo(
        tmp_path,
        {"P-PACKET-1.md": PACKET_PROBLEM, "P-PACKET-2.md": FORMULA_TITLED_PROBLEM},
    )

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    site = work / "build" / "quarto" / "_site"
    prose = listing_key(site / "tag" / "P-PACKET-1.html")
    formula = listing_key(site / "tag" / "P-PACKET-2.html")
    assert prose.startswith("algebra|"), prose
    assert prose < formula, (prose, formula)

    # The page carries the controls and nothing else: the rows come from the
    # index, a page of them at a time.
    page = (site / "problems.html").read_text()
    assert 'id="listing-results"' in page
    assert "listing-row" not in page


def test_the_source_index_lists_every_collection_under_its_kind(tmp_path: Path) -> None:
    """The listing held only the 338 sittings.

    Munkres, 586 problems and the largest collection on the site, was one of the
    43 that appeared on no index at all: a reader reached it from a problem card
    or not at all. The index now answers the listing, so what puts a collection
    on it is the filter its own page carries.
    """
    work = fixture_repo(tmp_path)

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    site = work / "build" / "quarto" / "_site"
    # A sitting is under `exam/`. A compilation, a homework sheet and a textbook
    # are not exams, and calling their pages exams is what `source/` fixes.
    filed = {
        "exam/SRC-UGA-FIX.html": "university-exam",
        "source/SRC-NEILNOTES.html": "compilation",
        "source/SRC-HW.html": "homework",
        "source/SRC-DUMMIT.html": "textbook",
    }
    for route, kind in filed.items():
        page = (site / route).read_text()
        assert f'data-pagefind-filter="source_kind:{kind}"' in page, route
        assert "data-pagefind-body" in page, route

    offered = read_html(site / "exams.html").root.find_all("select", id="listing-source_kind")[0]
    assert {option.attrs["value"] for option in offered.find_all("option")} == set(filed.values())


def test_problem_filters_group_each_label_with_its_control(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path)

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    page = read_html(work / "build" / "quarto" / "_site" / "problems.html")
    filters = page.root.find_all("div", **{"class": "listing-filters"})
    assert len(filters) == 1
    labels = [child for child in filters[0].children if isinstance(child, Element) and child.tag == "label"]
    controls = [[child.tag for child in label.children if isinstance(child, Element)] for label in labels]
    assert controls == [["input"], ["select"], ["select"], ["select"], ["select"]]


def test_a_subject_is_called_what_its_wiki_branch_calls_it(tmp_path: Path) -> None:
    """A subject is a wiki folder, and the branch's own title is its name.

    Every label used to be the area id with hyphens swapped and title case
    applied, which agreed with the registry that also listed the areas only
    because nobody had made the two disagree yet. Generate had a second version
    of the same problem: it read its areas out of the problem data, so it
    offered the same subjects in whatever order the first problem carrying each
    happened to appear.
    """
    work = fixture_repo(tmp_path)
    branch = work / "wiki" / "Algebra" / "index.md"
    branch.write_text(branch.read_text().replace("title: Algebra", "title: Abstract Algebra"))

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    site = work / "build" / "quarto" / "_site"

    select = read_html(site / "problems.html").root.find_all("select", id="listing-area")[0]
    browse = [(option.attrs["value"], option.text) for option in select.find_all("option")]
    assert browse == [("algebra", "Abstract Algebra")]

    embedded = re.search(r"const AREAS=(\{.*?\});", (site / "generate.html").read_text())
    assert embedded is not None, "the generator must embed the area names"
    assert list(json.loads(embedded.group(1)).items()) == browse

    # A row shows the same name, which it reads off the control rather than
    # being sent a second copy of.


def test_the_build_emits_a_contents_rail_from_authored_headings(tmp_path: Path) -> None:
    """The in-page Contents rail is built at compile time, not in the browser.

    A page's own <h2>/<h3> become the rail, in document order, each anchor
    resolving to an id written onto the heading; an <h3> is marked a
    subsection. This is the guarantee app.js used to provide at load, now the
    compiler's.
    """
    work = fixture_repo(tmp_path)
    (work / "wiki" / "Algebra" / "reading-order.md").write_text(
        "---\ntitle: Reading Order\norder: 5\n---\n\n# Reading Order\n\n## Groups\n\ntext\n\n### Sylow\n\nmore\n\n## Rings\n\neven more\n"
    )

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    built = read_html(work / "build" / "quarto" / "_site" / "wiki" / "algebra" / "reading-order.html")
    aside = built.root.find_all("aside", id="page-toc")[0]
    assert [a.attrs["href"] for a in aside.find_all("a")] == [
        "#groups",
        "#sylow",
        "#rings",
    ]
    assert [a.text for a in aside.find_all("a")] == ["Groups", "Sylow", "Rings"]
    assert [li.attrs.get("class", "") for li in aside.find_all("li")] == [
        "",
        "toc-subsection",
        "",
    ]

    body = built.root.find_all("article", **{"class": "page-body"})[0]
    heading_ids = {h.attrs["id"] for h in body.find_all("h2")} | {h.attrs["id"] for h in body.find_all("h3")}
    assert heading_ids == {"groups", "sylow", "rings"}
    # The same rail is offered as a disclosure where the layout hides the rail.
    assert built.root.find_all("details", **{"class": "page-toc-narrow"}) != []


def test_contents_rail_excludes_relation_apparatus(tmp_path: Path) -> None:
    site_root = tmp_path / "_site"
    assets_root = tmp_path / "assets"
    assets_root.mkdir()
    write_page(
        site_root,
        Path("tag/P-ONE.html"),
        {"title": "One"},
        (
            "<h2>Authored section</h2><p>Mathematics.</p>"
            '<section class="relation-group" data-relation-group="wiki-backlinks">'
            "<h2>What links to this</h2><ul><li>Backlink</li></ul></section>"
        ),
        "",
        {},
        build_asset_catalog(assets_root),
        StandardPage(Listing()),
    )

    built = read_html(site_root / "tag" / "P-ONE.html")
    aside = built.root.find_all("aside", id="page-toc")[0]
    assert aside.text.startswith("Contents")
    assert [a.text for a in aside.find_all("a")] == ["Authored section"]
    body = built.root.find_all("article", **{"class": "page-body"})[0]
    relation = body.find_all("section", **{"data-relation-group": "wiki-backlinks"})[0]
    assert relation.find_all("h2")[0].text == "What links to this"
