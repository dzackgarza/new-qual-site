"""How authored guide-page topics become problem-browser deep links."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml
from conftest import diagnostic_codes, fixture_repo, run_qualc
from pydantic import ValidationError
from qualc.diagnostics import DiagnosticCode
from qualc.publication import PublicationManifest, load_publications
from test_invariants import read_html

PROBLEM = """---
schema: qual/card@1
id: {id}
kind: problem
title: {title}
classification:
  areas:
  - {area}
  topics:
  - {topic}
relations: []
review: draft
---

::: problem
{body}
:::
"""


def manifest(*topics: str) -> dict[str, object]:
    """A one-section Topology guide whose page is classified by topics."""
    return {
        "schema": "qual/publication@2",
        "id": "GUIDE-TOPOLOGY",
        "kind": "study-guide",
        "title": "Topology",
        "lede": "One path through the point-set material the qual asks about.",
        "sections": [
            {
                "slug": "compactness",
                "title": "Compactness",
                "parent": "GUIDE-TOPOLOGY",
                "lede": "Open covers, finite subcovers, and what compactness buys.",
                "topics": list(topics),
                "items": [],
            }
        ],
    }


def reference_manifest(section: str, ref: str = "PRB-CPT") -> dict[str, object]:
    sections = []
    for slug, title in (("first", "First"), ("second", "Second")):
        items = [{"ref": ref}] if slug == section else []
        sections.append(
            {
                "slug": slug,
                "title": title,
                "parent": "GUIDE-TOPOLOGY",
                "lede": f"The {title.lower()} section.",
                "items": items,
            }
        )
    return {
        "schema": "qual/publication@2",
        "id": "GUIDE-TOPOLOGY",
        "kind": "study-guide",
        "title": "Topology",
        "lede": "A short topology guide.",
        "sections": sections,
    }


def _problem(card_id: str, title: str, area: str, topic: str, body: str) -> tuple[str, str]:
    return f"{card_id}.md", PROBLEM.format(id=card_id, title=title, area=area, topic=topic, body=body)


@pytest.fixture(scope="module")
def guide_site(tmp_path_factory: pytest.TempPathFactory) -> Path:
    """One Topology guide whose sections each carry what one test reads.

    `compactness` is classified by one topic and names no card; `family` is
    classified by two topics; `explicit` is classified by a topic and also
    names PRB-CPT, and assumes `compactness` as its parent. PRB-CPT-TOP
    matches the compactness topic and no section
    names it.
    """
    cards = dict(
        [
            _problem("PRB-CPT", "A compact Hausdorff space is normal", "topology", "compactness", "Let $X$ be compact Hausdorff. Show $X$ is normal."),
            _problem("PRB-CPT-TOP", "A closed subset of a compact space is compact", "topology", "compactness", "Let $K$ be closed in a compact space. Show $K$ is compact."),
            _problem(
                "PRB-CPT-RA",
                "A continuous function on a compact interval is uniformly continuous",
                "real-analysis",
                "compactness",
                "Let $f$ be continuous on $[0,1]$. Show $f$ is uniformly continuous.",
            ),
            _problem(
                "PRB-CON",
                "The continuous image of a connected space is connected",
                "topology",
                "connectedness",
                "Let $f: X \\to Y$ be continuous and $X$ connected. Show $f(X)$ is connected.",
            ),
            _problem("PRB-SEP", "A metric space is normal", "topology", "continuity", "Let $X$ be a metric space. Show $X$ is normal."),
        ]
    )
    work = fixture_repo(tmp_path_factory.mktemp("guide"), cards)

    def section(slug: str, title: str, topics: list[str], refs: list[str], parent: str = "GUIDE-TOPOLOGY") -> dict[str, object]:
        return {"slug": slug, "title": title, "parent": parent, "lede": f"The {slug} section.", "topics": topics, "items": [{"ref": ref} for ref in refs]}

    guide = {
        "schema": "qual/publication@2",
        "id": "GUIDE-TOPOLOGY",
        "kind": "study-guide",
        "title": "Topology",
        "lede": "One path through the point-set material the qual asks about.",
        "sections": [
            section("compactness", "Compactness", ["compactness"], []),
            section("family", "Family", ["compactness", "connectedness"], []),
            section("explicit", "Explicit", ["compactness"], ["PRB-CPT"], parent="compactness"),
        ],
    }
    (work / "publications" / "topology-guide.yaml").write_text(yaml.safe_dump(guide, sort_keys=False))
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr
    return work / "build" / "quarto" / "_site"


def test_checked_in_guide_sections_store_topics_on_the_page_not_as_query_items() -> None:
    """Problem discovery follows section metadata; `items` contains only refs."""
    publications = Path(__file__).resolve().parents[1] / "publications"

    for guide in load_publications(publications):
        for section in guide.sections:
            assert all(item.ref for item in section.items)


def test_semisimplicity_guide_resolves_its_named_terms() -> None:
    """The guide named for representations and semisimplicity links both definitions."""
    publications = Path(__file__).resolve().parents[1] / "publications"
    [algebra] = [guide for guide in load_publications(publications) if guide.id == "GUIDE-ALGEBRA"]
    section = next(section for section in algebra.sections if section.slug == "semisimplicity-and-representations")

    assert "[representation](../../wiki/algebra/representations/index.html)" in section.lede
    assert "[semisimple](../../tag/D-CYAJI.html)" in section.lede


def test_guide_page_topics_are_only_a_deep_link_into_the_problem_browser(guide_site: Path) -> None:
    """The guide classifies its page; only the central browser evaluates that classification."""
    page = read_html(guide_site / "guide" / "GUIDE-TOPOLOGY" / "compactness.html")
    panels = page.root.find_all("div", **{"class": "panel problem-browse-link"})
    assert len(panels) == 1
    links = panels[0].find_all("a")
    assert len(links) == 1
    assert links[0].attrs["href"] == "../../problems.html?area=topology&topic=compactness"
    assert "data-count" not in panels[0].attrs


def test_a_problem_browser_link_preserves_every_topic_in_the_authored_family(guide_site: Path) -> None:
    """Multi-topic page metadata must not silently narrow to its first topic."""
    page = read_html(guide_site / "guide" / "GUIDE-TOPOLOGY" / "family.html")
    panels = page.root.find_all("div", **{"class": "panel problem-browse-link"})
    assert len(panels) == 1
    links = panels[0].find_all("a")
    assert links[0].attrs["href"] == "../../problems.html?area=topology&topic=compactness&topic=connectedness"
    assert "data-count" not in panels[0].attrs


def test_the_problem_browser_owns_filtering_sampling_and_legacy_generate_redirect(built_fixture: Path) -> None:
    """One interface filters all matches and can sample/print from that result set."""
    work = built_fixture

    site = work / "build" / "quarto" / "_site"
    browser = read_html(site / "problems.html")
    assert len(browser.root.find_all("table", id="problem-table")) == 1
    assert len(browser.root.find_all("button", id="practice-sample")) == 1
    assert len(browser.root.find_all("button", id="practice-print")) == 1
    assert len(browser.root.find_all("section", id="practice-sheet")) == 1

    markup = (site / "problems.html").read_text()
    assert "dataTables.searchPanes.min.js" in markup
    table_script = (site / "assets" / "scripts" / "catalog-tables.js").read_text()
    assert "preSelect" in table_script
    assert ".getAll(key)" in table_script
    assert "collection-problems.json" in table_script
    assert "pageLength: 50" in table_script
    assert "listing-more" not in markup

    legacy = (site / "generate.html").read_text()
    assert 'new URL("problems.html",document.baseURI)' in legacy
    assert 'target.searchParams.set("sample","8")' in legacy
    assert "location.replace(target.href)" in legacy


@pytest.mark.parametrize("obsolete", ["kind", "limit", "review", "query"])
def test_publication_section_rejects_obsolete_query_fields(obsolete: str) -> None:
    """The section stores topics directly; no query/runtime object remains."""
    guide = manifest("compactness")
    sections = guide["sections"]
    assert isinstance(sections, list)
    section = sections[0]
    assert isinstance(section, dict)
    section[obsolete] = {} if obsolete in {"review", "query"} else 5

    with pytest.raises(ValidationError) as exc_info:
        PublicationManifest.model_validate(guide)

    assert "Extra inputs are not permitted" in str(exc_info.value)


def test_a_named_card_moves_with_its_publication_section(tmp_path: Path) -> None:
    work = fixture_repo(
        tmp_path,
        {
            "PRB-CPT.md": PROBLEM.format(
                id="PRB-CPT",
                title="A compact Hausdorff space is normal",
                area="topology",
                topic="compactness",
                body="Let $X$ be compact Hausdorff. Show $X$ is normal.",
            )
        },
    )
    manifest_path = work / "publications" / "topology-guide.yaml"
    manifest_path.write_text(yaml.safe_dump(reference_manifest("first"), sort_keys=False))
    first_build = run_qualc("build", work)
    assert first_build.returncode == 0, first_build.stderr

    manifest_path.write_text(yaml.safe_dump(reference_manifest("second"), sort_keys=False))
    second_build = run_qualc("build", work)
    assert second_build.returncode == 0, second_build.stderr

    first = read_html(work / "build" / "quarto" / "_site" / "guide" / "GUIDE-TOPOLOGY" / "first.html")
    second = read_html(work / "build" / "quarto" / "_site" / "guide" / "GUIDE-TOPOLOGY" / "second.html")
    # A referenced card is transcluded as its Stacks statement block, whose id is
    # the card id; it belongs to whichever section names it, not both.
    assert first.root.find_all("div", id="PRB-CPT") == []
    blocks = second.root.find_all("div", id="PRB-CPT")
    assert len(blocks) == 1
    assert "qual-section" in blocks[0].attrs["class"].split()


def test_a_section_topic_does_not_duplicate_its_explicit_card_appearance(guide_site: Path) -> None:
    """Topic metadata discovers problems but only an explicit ref is a guide appearance.

    PRB-CPT matches the topic of all three sections and is named by one.
    """
    card = read_html(guide_site / "tag" / "PRB-CPT.html")
    groups = card.root.find_all("section", **{"data-relation-group": "guide-appearances"})
    assert len(groups) == 1
    assert [li.text for li in groups[0].find_all("li")] == ["Explicit"]


def test_a_topic_match_is_not_a_guide_appearance(guide_site: Path) -> None:
    """Page topics point outward; matching cards are not displayed guide content."""
    card = read_html(guide_site / "tag" / "PRB-CPT-TOP.html")
    assert card.root.find_all("section", **{"data-relation-group": "guide-appearances"}) == []


def test_check_names_a_publication_reference_no_card_answers(tmp_path: Path) -> None:
    """Deleting a card a guide names has to fail the check, not the build.

    Merging five duplicate pairs left the algebra guide pointing at two ids that
    no longer existed. `check` reported the corpus sound and the next build died
    on the first missing reference, which is the wrong end of the run to learn
    it: the guide is corpus state, and a reference with no card is a corpus
    error.
    """
    work = fixture_repo(tmp_path, {})
    manifest = reference_manifest("first", ref="PRB-GONE")
    (work / "publications" / "topology-guide.yaml").write_text(yaml.safe_dump(manifest, sort_keys=False))

    assert diagnostic_codes(work) == [DiagnosticCode.PUBLICATION_REFERENCE_MISSING]


def test_a_guide_breadcrumb_is_where_the_page_is_filed(guide_site: Path) -> None:
    """A guide section's `parent` is the section it assumes, not its place.

    Walking that chain made the breadcrumb a prerequisite list -- `Algebra /
    Preliminaries / Rings and Ideals / Modules / Linear Algebra` -- while the
    same crumb in the wiki was a folder path. The sidebar is where the
    prerequisite tree belongs; the breadcrumb says where the page is.
    """
    site = guide_site

    section = read_html(site / "guide" / "GUIDE-TOPOLOGY" / "explicit.html")
    crumbs = section.root.find_all("nav", **{"class": "breadcrumbs"})[0].find_all("a")
    assert [(link.text, link.attrs["href"]) for link in crumbs] == [
        ("Guides", "../../guides.html"),
        ("Topology", "../GUIDE-TOPOLOGY.html"),
        ("Explicit", "explicit.html"),
    ]

    root = read_html(site / "guide" / "GUIDE-TOPOLOGY.html")
    root_crumbs = root.root.find_all("nav", **{"class": "breadcrumbs"})[0].find_all("a")
    assert [(link.text, link.attrs["href"]) for link in root_crumbs] == [
        ("Guides", "../guides.html"),
        ("Topology", "GUIDE-TOPOLOGY.html"),
    ]
