"""The authored wiki is a first-class source, not a sidecar."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path

import pytest
from conftest import SUBJECTS, diagnostic_codes, write_subject_branches
from qualc.diagnostics import DiagnosticCode
from qualc.emit import SearchRecordKind
from qualc.wiki import slug

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
        self.links: list[tuple[str, str, str]] = []
        self._link: tuple[str, str] | None = None
        self._link_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "a" and attributes.get("href") is not None:
            href = attributes["href"]
            assert href is not None
            class_value = attributes["class"] if "class" in attributes else None
            classes = class_value if class_value is not None else ""
            self._link = (href, classes)
            self._link_text = []
        for key, value in attrs:
            if value is None:
                continue
            if key == "href":
                self.hrefs.append(value)
            elif key == "src":
                self.srcs.append(value)

    def handle_data(self, data: str) -> None:
        if self._link is not None:
            self._link_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._link is not None:
            href, classes = self._link
            text = re.sub(r"\s+", " ", "".join(self._link_text)).strip()
            self.links.append((href, classes, text))
            self._link = None
            self._link_text = []


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


@dataclass
class Transclusion:
    """One card rendered into a wiki page in the position its link stood."""

    card_id: str
    label: str
    heading: str
    tag_href: str
    inner_labels: list[str]
    text: str


class TransclusionParser(HTMLParser):
    """Every `div.qual-transclusion` in the page body, in reading order."""

    def __init__(self) -> None:
        super().__init__()
        self.blocks: list[Transclusion] = []
        self._depth: int | None = None
        self._open = 0
        self._current: Transclusion | None = None
        self._part: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        classes = (attributes["class"] or "").split() if "class" in attributes else []
        label = attributes["data-label"] if "data-label" in attributes else None
        if tag == "div":
            self._open += 1
            if "qual-transclusion" in classes:
                identifier = attributes["id"]
                assert identifier is not None and label is not None
                self._depth = self._open
                self._current = Transclusion(
                    card_id=identifier,
                    label=label,
                    heading="",
                    tag_href="",
                    inner_labels=[],
                    text="",
                )
            elif self._current is not None and "qual-section" in classes:
                assert label is not None
                self._current.inner_labels.append(label)
        if self._current is None:
            return
        if tag == "p" and "qual-section-title" in classes and not self._current.heading:
            self._part = "heading"
        elif tag == "a" and "qual-section-tag" in classes:
            href = attributes["href"]
            assert href is not None
            self._current.tag_href = href

    def handle_data(self, data: str) -> None:
        if self._current is None:
            return
        if self._part == "heading":
            self._current.heading += data
        else:
            self._current.text += data

    def handle_endtag(self, tag: str) -> None:
        if tag == "p":
            self._part = None
        elif tag == "div":
            if self._current is not None and self._open == self._depth:
                self._current.heading = re.sub(r"\s+", " ", self._current.heading).strip()
                self._current.text = re.sub(r"\s+", " ", self._current.text).strip()
                self.blocks.append(self._current)
                self._current = None
                self._depth = None
            self._open -= 1


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
    write_subject_branches(work)
    return work


def test_a_standalone_image_is_a_figure_and_a_spaced_page_name_slugs(tmp_path: Path) -> None:
    """An image alone in a paragraph is a figure whether or not it has a caption.

    Pandoc's `implicit_figures` covers `![caption](src)` only; `![](src)`
    reached the page as a bare `<img>` inside a paragraph, with nothing to bound
    a tall image. Both spellings carry one class so one rule styles them.

    "Some Page.md" is an ordinary Obsidian filename and was an unreadable URL.
    The filename stays as authored and the route slugs, so the link a reader
    copies has no escape in it rather than a percent-encoded one.
    """
    work = fixture_repo(tmp_path)
    (work / "wiki" / "Some Page.md").write_text(wiki_md("# Some page\n\n![](figures/diagram.png)\n", order=2))
    (work / "wiki" / "index.md").write_text(wiki_md("# Fixture index\n\n![captioned](figures/diagram.png)\n\nSee [[Some Page]].\n"))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    site = work / "build" / "quarto" / "_site"
    index = (site / "wiki" / "index.html").read_text()
    uncaptioned = (site / "wiki" / "some-page.html").read_text()
    assert '<figure class="qual-figure">' in uncaptioned
    assert "<figcaption" not in uncaptioned
    assert 'class="qual-figure"' in index
    assert "<figcaption" in index

    links = LinkCollector()
    links.feed(index)
    assert "some-page.html" in links.hrefs
    assert not [href for href in links.hrefs if " " in href or "%20" in href]


PROMPTED_CARD = """---
schema: qual/card@1
id: DEF-NOWHERE
kind: definition
title: Nowhere dense
prompts:
- Give an example of a set that is not nowhere dense.
- Is $\\QQ$ nowhere dense?
classification:
  areas:
  - real-analysis
  topics:
  - Topology
relations: []
review: draft
---

::: definition
$A$ is **nowhere dense** iff the closure of $A$ has empty interior.
:::
"""


def test_a_cards_review_prompts_render_wherever_the_card_does(tmp_path: Path) -> None:
    """A prompt is the question this card answers, so it goes where the card goes.

    One block per prompt and none at all without them: the field is a list
    because one statement can be asked for in several ways, and a card that
    carries no question must not grow an empty container to say so.
    """
    work = fixture_repo(tmp_path)
    (work / "corpus" / "DEF-NOWHERE.md").write_text(PROMPTED_CARD)
    (work / "wiki" / "index.md").write_text(wiki_md("# Fixture index\n\n[[DEF-NOWHERE]]\n\n[[LEM-FRATTINI]]\n"))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    site = work / "build" / "quarto" / "_site"
    expected = [
        '<div class="review-question">Give an example of a set that is not nowhere dense.</div>',
        '<div class="review-question">Is $\\QQ$ nowhere dense?</div>',
    ]
    card_page = (site / "tag" / "DEF-NOWHERE.html").read_text()
    assert [block for block in expected if block in card_page] == expected

    wiki_page = (site / "wiki" / "index.html").read_text()
    assert [block for block in expected if block in wiki_page] == expected
    # The statement is the answer, so the question follows it.
    assert wiki_page.index("empty interior") < wiki_page.index("review-question")
    # LEM-FRATTINI carries no prompts and gains nothing.
    assert wiki_page.count("review-question") == len(expected)
    assert "review-question" not in (site / "tag" / "LEM-FRATTINI.html").read_text()


def test_a_card_shows_only_the_relation_panels_it_has(tmp_path: Path) -> None:
    """A heading whose body reads "None." tells the reader nothing.

    Two of the three panels were empty on a typical card. An empty panel is
    dropped and a card with no relations at all loses the band, rather than
    framing three headings around the word "None."
    """
    work = fixture_repo(tmp_path)
    result = run("build", work)
    assert result.returncode == 0, result.stderr

    tags = work / "build" / "quarto" / "_site" / "tag"
    problem = (tags / "PRB-INDEXP.html").read_text()
    assert re.findall(r'data-relation-group="([a-z-]+)"', problem) == ["backlinks", "wiki-backlinks"]
    assert "None." not in problem

    lemma = (tags / "LEM-FRATTINI.html").read_text()
    assert "relation-groups" not in lemma


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
    branches = {f"{subject}/index.md" for subject, _ in SUBJECTS}
    assert {entry["source"] for entry in manifest} == {"index.md", "details.md"} | branches
    assert {entry["route"] for entry in manifest} == {"wiki/index.html", "wiki/details.html"} | {"wiki/" + slug(subject) + "/index.html" for subject, _ in SUBJECTS}

    links = LinkCollector()
    links.feed((site / "wiki" / "index.html").read_text())
    assert {"../tag/PRB-INDEXP.html", "details.html"} <= set(links.hrefs)
    assert "../assets/figures/diagram.png" in links.srcs
    assert (site / "assets" / "figures" / "diagram.png").read_bytes() == b"fixture image"

    records = json.loads((site / "search.json").read_text())
    page = next(record for record in records if record["url"] == "wiki/index.html")
    assert SearchRecordKind(page["kind"]) == SearchRecordKind.WIKI
    assert "fixture index" in page["search"]


def test_bare_card_reference_uses_the_card_title(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path)
    (work / "wiki" / "index.md").write_text(wiki_md("# Fixture index\n\nCompare [[PRB-INDEXP]] with the rest.\n"))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    html = (work / "build" / "quarto" / "_site" / "wiki" / "index.html").read_text()
    links = LinkCollector()
    links.feed(html)
    link_texts = [text for _, _, text in links.links]
    assert "Show a subgroup of index $p$ in a $p\\dash$group is normal" in link_texts
    assert "PRB-INDEXP" not in link_texts


def test_a_reference_whose_text_is_mathematics_is_marked_as_such(tmp_path: Path) -> None:
    """The anchor says its own text typesets, so the stylesheet can act on it.

    `PRB-INDEXP` is titled "... index $p$ in a $p\\dash$group ...", and that
    title becomes the link text. Without the class nothing in the markup
    distinguishes it from a link reading three plain words, and the underline
    is drawn straight through the typeset mathematics.
    """
    work = fixture_repo(tmp_path)
    (work / "wiki" / "index.md").write_text(wiki_md("# Fixture index\n\nCompare [[PRB-INDEXP]] with [[DEF-PGROUP|the plain words]].\n"))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    links = LinkCollector()
    links.feed((work / "build" / "quarto" / "_site" / "wiki" / "index.html").read_text())
    marked = {href: "qual-link-math" in classes for href, classes, _ in links.links}
    assert marked["../tag/PRB-INDEXP.html"] is True
    assert marked["../tag/DEF-PGROUP.html"] is False


def test_a_standalone_reference_transcludes_the_card_it_names(tmp_path: Path) -> None:
    """A paragraph of nothing but card links is the statements, not links to them.

    Two links written on one line are two blocks. Each is one labelled section:
    the kind and the position on the page label it, its heading reads as the
    card's name followed by the tag that permalinks it, and there is no second
    labelled box nested inside. A reference inside a sentence names somewhere
    else and stays a link.
    """
    work = fixture_repo(tmp_path)
    # Two links on one line and a third on the next: markdown joins adjacent
    # lines into one paragraph, separating them by a soft break rather than a
    # space, and most of the corpus is authored that way. Both separators have
    # to be seen through for the paragraph to count as links and nothing else.
    (work / "wiki" / "index.md").write_text(wiki_md("# Fixture index\n\n[[DEF-PGROUP]] [[LEM-FRATTINI]]\n[[THM-SYLOW]]\n\nAs [[PRB-INDEXP]] shows.\n"))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    html = (work / "build" / "quarto" / "_site" / "wiki" / "index.html").read_text()
    blocks = TransclusionParser()
    blocks.feed(html)
    assert [block.card_id for block in blocks.blocks] == ["DEF-PGROUP", "LEM-FRATTINI", "THM-SYLOW"]
    assert [block.label for block in blocks.blocks] == ["Definition 1", "Lemma 1", "Theorem 1"]
    assert [block.heading for block in blocks.blocks] == [
        "$p$-group (Tag DEF-PGROUP)",
        "Frattini argument (Tag LEM-FRATTINI)",
        "Sylow's first theorem (Tag THM-SYLOW)",
    ]
    assert [block.tag_href for block in blocks.blocks] == [
        "../tag/DEF-PGROUP.html",
        "../tag/LEM-FRATTINI.html",
        "../tag/THM-SYLOW.html",
    ]
    assert [block.inner_labels for block in blocks.blocks] == [[], [], []]
    assert "if its order is a power of the prime" in blocks.blocks[0].text
    assert "a Sylow" in blocks.blocks[1].text
    assert "has a subgroup of order" in blocks.blocks[2].text

    links = LinkCollector()
    links.feed(html)
    assert [classes for href, classes, _ in links.links if href == "../tag/DEF-PGROUP.html"] == ["qual-section-tag"]
    # The class this repository writes, not the one pandoc writes: `wikilink`
    # sits in the link's classes on 3.10 and in its title on 3.6.
    inline = [classes.split() for href, classes, _ in links.links if href == "../tag/PRB-INDEXP.html"]
    assert [[name for name in classes if name.startswith("qual-")] for classes in inline] == [["qual-link-math"]]


def test_a_card_referenced_twice_on_a_page_is_transcluded_once(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path)
    (work / "wiki" / "index.md").write_text(wiki_md("# Fixture index\n\n[[DEF-PGROUP]]\n\n[[LEM-FRATTINI]]\n\n[[DEF-PGROUP]]\n"))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    blocks = TransclusionParser()
    blocks.feed((work / "build" / "quarto" / "_site" / "wiki" / "index.html").read_text())
    assert [block.card_id for block in blocks.blocks] == ["DEF-PGROUP", "LEM-FRATTINI"]
    assert [block.label for block in blocks.blocks] == ["Definition 1", "Lemma 1"]


DIVERGENT_CARD = """---
schema: qual/card@1
id: PRP-TRACES
kind: proposition
title: Characteristic polynomials via traces of exterior powers
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: {.proposition title="Useful computational trick"}
The coefficients of $\\chi_A$ are the traces of the exterior powers of $A$.
:::

::: {.proof title="of a"}
Expand the determinant.
:::

::: {.proof title="of b"}
Compare degrees.
:::
"""


def test_a_transcluded_card_is_named_by_its_yaml_title(tmp_path: Path) -> None:
    """The card's name has one owner: YAML `title`. The body attribute is not it.

    582 cards carry a name in both places and 85 of them diverge, the body
    string being the junk one -- here "Useful computational trick" over a real
    name. Sibling blocks of one kind are numbered, which is what the authored
    "of a"/"of b" labels stood in for; a nested `title=` is a part label and
    still renders.
    """
    work = fixture_repo(tmp_path)
    (work / "corpus" / "PRP-TRACES.md").write_text(DIVERGENT_CARD)
    (work / "wiki" / "index.md").write_text(wiki_md("# Fixture index\n\n[[PRP-PIDX]] [[WRN-SYLOWCOUNT]] [[PRP-TRACES]]\n"))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    blocks = TransclusionParser()
    blocks.feed((work / "build" / "quarto" / "_site" / "wiki" / "index.html").read_text())
    # A label counts its own kind on the page. One sequence across every kind
    # put "Warning 2" on a page with one warning: the label asserts what it
    # counts, and the second proposition is the page's second proposition.
    assert [block.label for block in blocks.blocks] == ["Proposition 1", "Warning 1", "Proposition 2"]
    block = blocks.blocks[2]
    assert block.heading == "Characteristic polynomials via traces of exterior powers (Tag PRP-TRACES)"
    assert "Useful computational trick" not in block.heading
    assert block.inner_labels == ["Proof 1", "Proof 2"]

    card_page = (work / "build" / "quarto" / "_site" / "tag" / "PRP-TRACES.html").read_text()
    # The authored title qualifies the block's own label -- "Proof 1 (of a)" --
    # so it is bracketed and carries the class the label line is built from,
    # not the class a card's name uses.
    assert '<p class="qual-section-qualifier">(of a)</p>' in card_page
    assert '<p class="qual-section-qualifier">(of b)</p>' in card_page


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
    (wiki / "Algebra").mkdir(exist_ok=True)
    (wiki / "Algebra" / "index.md").write_text(wiki_md("# Algebra\n", order=2, title="Algebra"))
    (wiki / "Algebra" / "groups.md").write_text(wiki_md("# Groups\n", order=1))
    (wiki / "Topology").mkdir(exist_ok=True)
    (wiki / "Topology" / "index.md").write_text(wiki_md("# Topology\n", order=3, title="Topology"))
    (wiki / "Topology" / "compactness.md").write_text(wiki_md("# Compactness\n", order=1))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    page = work / "build" / "quarto" / "_site" / "wiki" / "algebra" / "groups.html"
    navigation = WikiNavigationParser()
    navigation.feed(page.read_text())

    assert navigation.details == [(1, "Algebra", True), (1, "Topology", False)]
    assert ("Groups", "groups.html", True) in navigation.links
    assert ("Compactness", "../topology/compactness.html", False) in navigation.links
    # A folder's own page is its summary, and is offered once. The label used to
    # be written again as the folder's first child: the same word on two lines,
    # one expanding and one navigating.
    assert [link for link in navigation.links if link[0] == "Algebra"] == [("Algebra", "index.html", False)]

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
    (wiki / "Algebra" / "index.md").write_text(wiki_md("# Syllabus\n", order=2, title="Algebra"))
    (wiki / "Algebra" / "groups.md").write_text(wiki_md("# Groups\n", order=1))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    site = work / "build" / "quarto" / "_site" / "wiki"
    navigation = WikiNavigationParser()
    navigation.feed((site / "algebra" / "groups.html").read_text())

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
    write_subject_branches(work)
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
    (work / "wiki" / "no-index-here").mkdir()
    (work / "wiki" / "no-index-here" / "groups.md").write_text(wiki_md("# Groups\n", order=1))
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


TWO_SOLUTIONS = """---
schema: qual/card@1
id: PRB-TWOWAYS
kind: problem
title: The integral of a holomorphic kernel is holomorphic
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
relations: []
review: draft
---

::: problem
Show that the integral is holomorphic off the curve.
:::

::: {.solution title="Using Morera"}
Integrate over every triangle.
:::

::: {.solution title="Using limit definition"}
Differentiate under the integral.
:::
"""


def test_a_solution_names_its_method_before_it_is_opened(tmp_path: Path) -> None:
    """Two solutions on one card showed two disclosures both reading "Solution".

    The authored label is what tells them apart, and a disclosure is closed when
    the reader chooses: the summary is the only place the label can act. Putting
    it in the body instead would hide the distinction behind the click it is
    supposed to inform.
    """
    work = fixture_repo(tmp_path)
    (work / "corpus" / "PRB-TWOWAYS.md").write_text(TWO_SOLUTIONS)

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    card_page = (work / "build" / "quarto" / "_site" / "tag" / "PRB-TWOWAYS.html").read_text()
    assert "<summary>Solution: Using Morera</summary>" in card_page
    assert "<summary>Solution: Using limit definition</summary>" in card_page


FOOTNOTED_CARD = """---
schema: qual/card@1
id: PRB-ASIDE
kind: problem
title: The open mapping theorem for holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Open Mapping Theorem
relations: []
review: draft
---

::: problem
Show that a non-constant holomorphic map is open.
:::

::: solution
Let $f: U\\to \\CC$.^[Using the argument principle.]
Pick $w_0$ in the image and bound $f$ below on a small circle.
:::
"""


def test_a_footnote_reaches_the_page_as_a_sidenote(tmp_path: Path) -> None:
    """The note belongs beside the line that raises it, not in a list at the foot.

    Every note in the corpus is a technique aside on its own sentence -- "Using
    the argument principle", "Keyhole contour" -- and pandoc's arrangement puts
    that a scroll away from the step it explains. The markdown written beside
    the HTML keeps the real footnote: only the page is rearranged.
    """
    work = fixture_repo(tmp_path)
    (work / "corpus" / "PRB-ASIDE.md").write_text(FOOTNOTED_CARD)

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    # Pandoc's HTML writer wraps long lines, so the attribute can land on the
    # line after the tag it belongs to.
    card_page = re.sub(r"\s+", " ", (work / "build" / "quarto" / "_site" / "tag" / "PRB-ASIDE.html").read_text())
    assert '<span class="sidenote-number"></span><span class="sidenote">Using the argument principle.</span>' in card_page
    assert 'class="footnotes' not in card_page

    # The markdown beside it keeps a real footnote -- reference style, which is
    # what pandoc's markdown writer emits -- and no sidenote markup at all.
    source = (work / "build" / "quarto" / "tag" / "PRB-ASIDE.qmd").read_text()
    assert "[^1]: Using the argument principle." in source
    assert "sidenote" not in source


class ReadingOrderParser(HTMLParser):
    """The previous and next links under a wiki page, with where each lands."""

    def __init__(self) -> None:
        super().__init__()
        self._in_order = False
        self._collect: list[str] | None = None
        self.entries: list[tuple[str, str]] = []
        self._title = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        classes = dict(attrs).get("class", "") or ""
        if tag == "nav" and "reading-order" in classes:
            self._in_order = True
        elif self._in_order and tag in {"a", "span"} and (tag == "a" or "reading-section" in classes):
            self._collect = []

    def handle_data(self, data: str) -> None:
        if self._collect is not None:
            self._collect.append(data)

    def handle_endtag(self, tag: str) -> None:
        if not self._in_order:
            return
        if tag == "a" and self._collect is not None:
            self._title = "".join(self._collect).strip()
            self.entries.append((self._title, ""))
            self._collect = None
        elif tag == "span" and self._collect is not None:
            self.entries[-1] = (self._title, "".join(self._collect).strip())
            self._collect = None
        elif tag == "nav":
            self._in_order = False


def test_a_reading_link_that_leaves_the_folder_says_where_it_lands(tmp_path: Path) -> None:
    """Reading order runs on past the end of a folder.

    From Algebra > Quals the previous page was `Final Exam`, three folders away
    under Exercises, and the link said only `Final Exam`. A link to a sibling
    says nothing extra: that is not a crossing.
    """
    work = fixture_repo(tmp_path)
    algebra = work / "wiki" / "Algebra"
    (algebra / "exercises").mkdir(parents=True)
    (algebra / "quals").mkdir()
    (algebra / "index.md").write_text(wiki_md("# Algebra\n", order=2, title="Algebra"))
    (algebra / "exercises" / "index.md").write_text(wiki_md("# Exercises\n", order=1, title="Exercises"))
    (algebra / "exercises" / "sheet-one.md").write_text(wiki_md("# Sheet One\n", order=1))
    (algebra / "exercises" / "sheet-two.md").write_text(wiki_md("# Sheet Two\n", order=2))
    (algebra / "quals" / "index.md").write_text(wiki_md("# Quals\n", order=2, title="Quals"))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    site = work / "build" / "quarto" / "_site" / "wiki" / "algebra"

    # Reading Exercises: back to the folder itself, on to a sibling sheet.
    sheet = ReadingOrderParser()
    sheet.feed((site / "exercises" / "sheet-one.html").read_text())
    assert sheet.entries == [("Exercises", ""), ("Sheet Two", "")]

    # Quals is the next folder along, and the page before it is three levels
    # away under Exercises.
    quals = ReadingOrderParser()
    quals.feed((site / "quals" / "index.html").read_text())
    assert quals.entries == [("Sheet Two", "in Algebra / Exercises")]


class BreadcrumbParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._in_crumbs = False
        self._text: list[str] | None = None
        self.crumbs: list[tuple[str, str, bool]] = []
        self._href = ""
        self._current = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "nav" and "breadcrumbs" in (attributes.get("class") or ""):
            self._in_crumbs = True
        elif self._in_crumbs and tag == "a":
            self._href = attributes["href"] or ""
            self._current = attributes.get("aria-current") == "page"
            self._text = []

    def handle_data(self, data: str) -> None:
        if self._text is not None:
            self._text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._in_crumbs and tag == "a" and self._text is not None:
            self.crumbs.append(("".join(self._text).strip(), self._href, self._current))
            self._text = None
        elif tag == "nav":
            self._in_crumbs = False


def test_a_breadcrumb_is_where_the_page_is_filed(tmp_path: Path) -> None:
    """One meaning, on every page that has one: the trail down to this page.

    A wiki subject's landing page had a single crumb repeating its own heading,
    because the wiki's index is filed beside the subjects rather than above
    them and walking the folder chain never reached it.
    """
    work = fixture_repo(tmp_path)
    algebra = work / "wiki" / "Algebra"
    (algebra / "groups").mkdir(parents=True)
    (algebra / "index.md").write_text(wiki_md("# Algebra\n", order=2, title="Algebra"))
    (algebra / "groups" / "index.md").write_text(wiki_md("# Groups\n", order=1, title="Groups"))
    (algebra / "groups" / "sylow.md").write_text(wiki_md("# Sylow\n", order=1))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    site = work / "build" / "quarto" / "_site" / "wiki"

    page = BreadcrumbParser()
    page.feed((site / "algebra" / "groups" / "sylow.html").read_text())
    assert page.crumbs == [
        ("Wiki", "../../index.html", False),
        ("Algebra", "../index.html", False),
        ("Groups", "index.html", False),
        ("Sylow", "sylow.html", True),
    ]

    # A subject landing page reaches the wiki root rather than naming itself.
    subject = BreadcrumbParser()
    subject.feed((site / "algebra" / "index.html").read_text())
    assert subject.crumbs == [("Wiki", "../index.html", False), ("Algebra", "index.html", True)]

    # The wiki root is its own root: nowhere to go up to, so no breadcrumb.
    root = BreadcrumbParser()
    root.feed((site / "index.html").read_text())
    assert root.crumbs == []


def test_a_wiki_page_can_point_at_the_rest_of_the_site(tmp_path: Path) -> None:
    """The wiki index says what the guides are for, and links to them.

    Every href in a wiki page was read as a card id, an asset, or a wiki page,
    so naming a site page failed the build as a missing wiki page. A page three
    folders down cannot spell the way back itself, so the name is written from
    the site root and the page writer makes it relative.
    """
    work = fixture_repo(tmp_path)
    deep = work / "wiki" / "Algebra" / "groups"
    deep.mkdir(parents=True)
    (work / "wiki" / "Algebra" / "index.md").write_text(wiki_md("# Algebra\n", order=2, title="Algebra"))
    (deep / "index.md").write_text(wiki_md("# Groups\n\nSee the [guides](guides.html) and the [browser](problems.html).\n", order=1, title="Groups"))

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    site = work / "build" / "quarto" / "_site"
    body = LinkCollector()
    body.feed((site / "wiki" / "algebra" / "groups" / "index.html").read_text())
    assert "../../../guides.html" in body.hrefs
    assert "../../../problems.html" in body.hrefs
    assert (site / "guides.html").exists()
