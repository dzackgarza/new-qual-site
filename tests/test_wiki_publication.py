"""The authored wiki is a first-class source, not a sidecar."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

import pytest
from conftest import diagnostic_codes
from qualc.diagnostics import DiagnosticCode
from qualc.emit import SearchRecordKind

ROOT = Path(__file__).resolve().parent.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "kinds"


def wiki_md(body: str, *, order: int = 0, title: str | None = None) -> str:
    lines = ["---", f"order: {order}"]
    if title is not None:
        lines.append(f"title: {title}")
    lines.extend(["---", "", body])
    return "\n".join(lines) if body.endswith("\n") else "\n".join(lines) + "\n"


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


class WikiNavigationParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_wiki_navigation = False
        self.details: list[tuple[int, str, bool]] = []
        self.links: list[tuple[str, str, bool]] = []
        self._details_open: list[bool] = []
        self._summary_text: list[str] | None = None
        self._link: tuple[str, bool] | None = None
        self._link_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "nav" and attributes.get("aria-label") == "Wiki":
            self.in_wiki_navigation = True
        elif self.in_wiki_navigation and tag == "details":
            self._details_open.append("open" in attributes)
        elif self.in_wiki_navigation and tag == "summary":
            self._summary_text = []
        elif self.in_wiki_navigation and tag == "a":
            href = attributes["href"]
            assert href is not None
            self._link = (href, attributes.get("aria-current") == "page")
            self._link_text = []

    def handle_data(self, data: str) -> None:
        if self._summary_text is not None:
            self._summary_text.append(data)
        if self._link is not None:
            self._link_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.in_wiki_navigation and tag == "summary":
            assert self._summary_text is not None
            self.details.append(
                (
                    len(self._details_open),
                    "".join(self._summary_text).strip(),
                    self._details_open[-1],
                )
            )
            self._summary_text = None
        elif self.in_wiki_navigation and tag == "a":
            assert self._link is not None
            href, current = self._link
            self.links.append(("".join(self._link_text).strip(), href, current))
            self._link = None
            self._link_text = []
        elif self.in_wiki_navigation and tag == "details":
            self._details_open.pop()
        elif self.in_wiki_navigation and tag == "nav":
            self.in_wiki_navigation = False


class WikiBacklinkParser(HTMLParser):
    """The generated incoming-link section, not the sidebar and not the page body."""

    def __init__(self) -> None:
        super().__init__()
        self.titles: list[str] = []
        self.hrefs: list[str] = []
        self._in_section = False
        self._link_href: str | None = None
        self._link_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "section" and attributes.get("data-relation-group") == "wiki-backlinks":
            self._in_section = True
        elif self._in_section and tag == "a":
            href = attributes["href"]
            assert href is not None
            self._link_href = href
            self._link_text = []

    def handle_data(self, data: str) -> None:
        if self._link_href is not None:
            self._link_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._in_section and tag == "a":
            assert self._link_href is not None
            self.titles.append("".join(self._link_text).strip())
            self.hrefs.append(self._link_href)
            self._link_href = None
            self._link_text = []
        elif self._in_section and tag == "section":
            self._in_section = False


def fixture_repo(tmp_path: Path) -> Path:
    work = tmp_path / "repo"
    for sub in ("vocabularies", "site"):
        shutil.copytree(ROOT / sub, work / sub)
    shutil.copytree(FIXTURES, work / "corpus")
    (work / "publications").mkdir()
    assets = work / "assets" / "figures"
    assets.mkdir(parents=True)
    (assets / "diagram.png").write_bytes(b"fixture image")
    wiki = work / "wiki"
    wiki.mkdir()
    (wiki / "index.md").write_text(wiki_md("# Fixture index\n\nSee [[PRB-INDEXP|the index problem]] and [the details](details.md).\n\n![diagram](figures/diagram.png)\n"))
    (wiki / "details.md").write_text(wiki_md("# Fixture details\n\nThe page reference survived.\n", order=1))
    return work


def run(command: str, root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "qualc", command, "--root", str(root)],
        capture_output=True,
        text=True,
        check=False,
    )


def test_build_emits_every_authored_page_and_resolves_real_links(
    tmp_path: Path,
) -> None:
    work = fixture_repo(tmp_path)
    result = run("build", work)
    assert result.returncode == 0, result.stderr

    output = work / "build" / "quarto"
    site = output / "_site"
    manifest = json.loads((output / "wiki-manifest.json").read_text())
    assert {entry["source"] for entry in manifest} == {"index.md", "details.md"}
    assert {entry["route"] for entry in manifest} == {
        "wiki/index.html",
        "wiki/details.html",
    }

    links = LinkCollector()
    links.feed((site / "wiki" / "index.html").read_text())
    assert {"../tag/PRB-INDEXP.html", "details.html"} <= set(links.hrefs)
    assert "../assets/figures/diagram.png" in links.srcs
    assert (site / "assets" / "figures" / "diagram.png").read_bytes() == b"fixture image"

    records = json.loads((site / "search.json").read_text())
    page = next(record for record in records if record["url"] == "wiki/index.html")
    assert SearchRecordKind(page["kind"]) == SearchRecordKind.PAGE
    assert "fixture index" in page["search"]


def test_incoming_wiki_links_are_generated_from_the_resolved_graph(tmp_path: Path) -> None:
    """Who points at a page is the inverse of the wikilinks already resolved.

    The markdown does not list incoming links. The fixture index points at
    details.md and at PRB-INDEXP; those targets must show that, and a page
    nothing cites must not grow a handwritten 'linked from' list.
    """
    work = fixture_repo(tmp_path)
    assert "What links to this" not in (work / "wiki" / "details.md").read_text()

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    site = work / "build" / "quarto" / "_site"
    details = WikiBacklinkParser()
    details.feed((site / "wiki" / "details.html").read_text())
    assert details.titles == ["Fixture index"]
    assert details.hrefs == ["index.html"]

    index = WikiBacklinkParser()
    index.feed((site / "wiki" / "index.html").read_text())
    assert index.titles == []
    assert index.hrefs == []

    card = WikiBacklinkParser()
    card.feed((site / "tag" / "PRB-INDEXP.html").read_text())
    assert card.titles == ["Fixture index"]
    assert card.hrefs == ["../wiki/index.html"]


def test_wiki_tree_is_complete_on_root_and_nested_pages(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path)
    wiki = work / "wiki"
    (wiki / "algebra").mkdir()
    (wiki / "algebra" / "index.md").write_text(wiki_md("# Algebra\n", order=2, title="Algebra"))
    (wiki / "algebra" / "groups.md").write_text(wiki_md("# Groups\n", order=1))
    (wiki / "topology").mkdir()
    (wiki / "topology" / "index.md").write_text(wiki_md("# Topology\n", order=3, title="Topology"))
    (wiki / "topology" / "compactness.md").write_text(wiki_md("# Compactness\n", order=1))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    page = work / "build" / "quarto" / "_site" / "wiki" / "algebra" / "groups.html"
    navigation = WikiNavigationParser()
    navigation.feed(page.read_text())

    assert navigation.details == [(1, "Algebra", True), (1, "Topology", False)]
    assert ("Groups", "groups.html", True) in navigation.links
    assert ("Compactness", "../topology/compactness.html", False) in navigation.links

    index_navigation = WikiNavigationParser()
    index_navigation.feed((page.parents[1] / "index.html").read_text())

    assert index_navigation.details == [(1, "Algebra", False), (1, "Topology", False)]
    assert ("Fixture index", "index.html", True) in index_navigation.links
    assert ("Groups", "algebra/groups.html", False) in index_navigation.links
    assert ("Compactness", "topology/compactness.html", False) in index_navigation.links


def test_wiki_sidebar_uses_title_and_order_metadata(tmp_path: Path) -> None:
    """A folder's label and place among siblings are the index page's title and order."""
    work = fixture_repo(tmp_path)
    wiki = work / "wiki"
    (wiki / "z-first").mkdir()
    (wiki / "z-first" / "index.md").write_text(wiki_md("# First\n", order=10, title="First"))
    (wiki / "z-first" / "note.md").write_text(wiki_md("# First note\n", order=1))
    (wiki / "a-second").mkdir()
    (wiki / "a-second" / "index.md").write_text(wiki_md("# Second\n", order=20, title="Second"))
    (wiki / "a-second" / "note.md").write_text(wiki_md("# Second note\n", order=1))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    navigation = WikiNavigationParser()
    navigation.feed((work / "build" / "quarto" / "_site" / "wiki" / "index.html").read_text())
    assert navigation.details == [(1, "First", False), (1, "Second", False)]


def test_wiki_index_page_is_the_directory_node(tmp_path: Path) -> None:
    """A folder's index.md is that folder in the tree, not a sibling of its children."""
    work = fixture_repo(tmp_path)
    wiki = work / "wiki"
    (wiki / "10_Algebra").mkdir()
    (wiki / "10_Algebra" / "index.md").write_text(wiki_md("# Syllabus\n", order=2, title="Algebra"))
    (wiki / "10_Algebra" / "groups.md").write_text(wiki_md("# Groups\n", order=1))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    site = work / "build" / "quarto" / "_site" / "wiki"
    navigation = WikiNavigationParser()
    navigation.feed((site / "10_Algebra" / "groups.html").read_text())

    titles = [title for title, _, _ in navigation.links]
    assert titles.count("Algebra") == 1
    assert "Syllabus" not in titles
    assert ("Algebra", "index.html", False) in navigation.links
    assert ("Groups", "groups.html", True) in navigation.links
    assert (1, "Algebra", True) in navigation.details


@pytest.mark.parametrize(
    ("pages", "code"),
    [
        ({"index.md": wiki_md("# Root\n\n[[does-not-exist]]\n")}, DiagnosticCode.PAGE_REFERENCE_MISSING),
        (
            {
                "index.md": wiki_md("# Root\n\n[[same]]\n"),
                "a/index.md": wiki_md("# A folder\n", order=1, title="A"),
                "a/same.md": wiki_md("# A\n", order=1),
                "b/index.md": wiki_md("# B folder\n", order=2, title="B"),
                "b/same.md": wiki_md("# B\n", order=1),
            },
            DiagnosticCode.PAGE_REFERENCE_AMBIGUOUS,
        ),
    ],
)
def test_check_rejects_missing_or_ambiguous_page_references(
    tmp_path: Path,
    pages: dict[str, str],
    code: DiagnosticCode,
) -> None:
    """A reference that resolves to nothing, and one that resolves to two pages,
    are different failures and must stay distinguishable. Asserting the code
    rather than the wording is what keeps them apart -- both messages contain
    "wiki page reference"."""
    work = fixture_repo(tmp_path)
    wiki = work / "wiki"
    for path in wiki.rglob("*.md"):
        path.unlink()
    for relative, text in pages.items():
        path = wiki / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    assert diagnostic_codes(work) == [code]


def test_check_rejects_a_page_with_no_order(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path)
    (work / "wiki" / "index.md").write_text("# Root\n")
    (work / "wiki" / "details.md").unlink()
    assert diagnostic_codes(work) == [DiagnosticCode.PAGE_MISSING_ORDER]


def test_check_rejects_a_directory_with_no_index_page(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path)
    (work / "wiki" / "algebra").mkdir()
    (work / "wiki" / "algebra" / "groups.md").write_text(wiki_md("# Groups\n", order=1))
    assert diagnostic_codes(work) == [DiagnosticCode.PAGE_DIRECTORY_MISSING_INDEX]


def test_a_citation_renders_against_the_bibliography(tmp_path: Path) -> None:
    """Pandoc reads `[@key]` as a citation and leaves the key as the element's
    own text, so without citeproc the reader is shown `[@dummit_foote_2004]`.
    citeproc resolves it against `references.bib`: the reader gets an author-date
    reference in place and a bibliography entry to look it up in."""
    work = fixture_repo(tmp_path)
    (work / "wiki" / "index.md").write_text(wiki_md("# Fixture index\n\nReferences: [@DF04], [@Smi].\n"))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    # Pandoc's HTML writer wraps its output, so a name can straddle two lines.
    html = (work / "build" / "quarto" / "_site" / "wiki" / "index.html").read_text()
    assert "@DF04" not in html

    # The reference is only half of it: the key resolves to a work the reader can
    # find, in a generated bibliography carrying the library's metadata.
    # Read as text: Better BibTeX protects title case with a `nocase` span, so a
    # title is not contiguous in the markup. The style is the committed alphabetic
    # one, which labels a reference `[DuFo04]` rather than `(Dummit and Foote 2004)`.
    text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html))
    assert "[DuFo04]" in text
    assert "[Smit]" in text
    assert "Dummit, D. S. and R. M. Foote" in text
    assert "Wiley, 2004" in text
    assert "Smith, R." in text

    records = json.loads((work / "build" / "quarto" / "_site" / "search.json").read_text())
    index = next(record for record in records if record["url"] == "wiki/index.html")
    assert "dummit, d. s. and r. m. foote" in index["search"]
    # Pandoc records the citeproc request in the document metadata. The page is
    # searchable for what it says, not for the names of the files it was built with.
    assert "references.bib" not in index["search"]
    assert "style.csl" not in index["search"]


def test_check_rejects_a_citation_the_bibliography_does_not_define(
    tmp_path: Path,
) -> None:
    """citeproc renders a key it cannot resolve as `**key?**`, which would reach
    the page. The build stops at the named diagnostic instead."""
    work = fixture_repo(tmp_path)
    (work / "wiki" / "index.md").write_text(wiki_md("# Fixture index\n\nSee [@bourbaki_1970].\n"))
    for path in (work / "wiki").rglob("*.md"):
        if path.name != "index.md":
            path.unlink()

    assert diagnostic_codes(work) == [DiagnosticCode.UNKNOWN_CITATION]


def test_a_figure_captioned_with_its_own_filename_loses_the_caption(
    tmp_path: Path,
) -> None:
    """Pandoc's implicit-figure syntax makes the caption out of the alt text, and
    the authored vault wrote the attachment path there. A written caption is a
    caption and stays; a path is the file's name and is not one."""
    work = fixture_repo(tmp_path)
    (work / "wiki" / "index.md").write_text(wiki_md("# Fixture index\n\n![figures/diagram.png](figures/diagram.png)\n\n![The Tube Lemma](figures/diagram.png)\n"))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    page = (work / "build" / "quarto" / "_site" / "wiki" / "index.html").read_text()
    captions = re.findall(r"<figcaption[^>]*>(.*?)</figcaption>", page)
    assert captions == ["The Tube Lemma"]
