"""How an authored study-guide practice query becomes a generator deep link."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml
from conftest import diagnostic_codes, fixture_repo, run_qualc
from pydantic import ValidationError
from qualc.diagnostics import DiagnosticCode
from qualc.publication import PublicationManifest, QueryItem, load_publications
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


def manifest(*topics: str, kind: str = "problem") -> dict[str, object]:
    """A one-section Topology guide whose only item is a panel over `topics`."""
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
                "items": [
                    {
                        "query": {
                            "kind": kind,
                            "topics": list(topics),
                            "limit": 5,
                            "review": {"mode": "any"},
                        }
                    }
                ],
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


def test_checked_in_guide_sections_have_one_scoped_practice_target_per_kind() -> None:
    """Each asked kind gets one practice escape hatch, not a topic-bucket stack."""
    publications = Path(__file__).resolve().parents[1] / "publications"

    for guide in load_publications(publications):
        for section in guide.sections:
            queries = [item.query for item in section.items if isinstance(item, QueryItem)]
            for kind in ("problem", "exercise"):
                same_kind = [query for query in queries if query.kind == kind]
                assert len(same_kind) <= 1, f"{guide.id}/{section.slug} has {len(same_kind)} {kind} practice queries"
                if same_kind:
                    assert same_kind[0].topics, f"{guide.id}/{section.slug} has an unscoped {kind} practice query"


def test_semisimplicity_guide_resolves_its_named_terms() -> None:
    """The guide named for representations and semisimplicity links both definitions."""
    publications = Path(__file__).resolve().parents[1] / "publications"
    [algebra] = [guide for guide in load_publications(publications) if guide.id == "GUIDE-ALGEBRA"]
    section = next(section for section in algebra.sections if section.slug == "semisimplicity-and-representations")

    assert "[representation](../../wiki/algebra/representations/index.html)" in section.lede
    assert "[semisimple](../../tag/D-CYAJI.html)" in section.lede


def test_a_problem_query_is_only_a_deep_link_into_the_generator(tmp_path: Path) -> None:
    """The guide records the filter; only the generator evaluates it."""
    work = fixture_repo(
        tmp_path,
        {
            "PRB-CPT-TOP.md": PROBLEM.format(
                id="PRB-CPT-TOP",
                title="A compact Hausdorff space is normal",
                area="topology",
                topic="compactness",
                body="Let $X$ be compact Hausdorff. Show $X$ is normal.",
            ),
            "PRB-CPT-RA.md": PROBLEM.format(
                id="PRB-CPT-RA",
                title="A continuous function on a compact interval is uniformly continuous",
                area="real-analysis",
                topic="compactness",
                body="Let $f$ be continuous on $[0,1]$. Show $f$ is uniformly continuous.",
            ),
        },
    )
    (work / "publications" / "topology-guide.yaml").write_text(yaml.safe_dump(manifest("compactness"), sort_keys=False))

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    page = read_html(work / "build" / "quarto" / "_site" / "guide" / "GUIDE-TOPOLOGY" / "compactness.html")
    panels = page.root.find_all("div", **{"class": "panel generator-link"})
    assert len(panels) == 1
    links = panels[0].find_all("a")
    assert len(links) == 1
    assert links[0].attrs["href"] == "../../generate.html?area=topology&kind=problem&topic=compactness"
    assert panels[0].attrs["data-query-kind"] == "problem"
    assert "data-count" not in panels[0].attrs


def test_a_generator_link_preserves_every_topic_in_the_authored_family(tmp_path: Path) -> None:
    """A multi-topic guide query must not silently narrow to its first topic."""
    work = fixture_repo(
        tmp_path,
        {
            "PRB-CPT.md": PROBLEM.format(
                id="PRB-CPT",
                title="A compact Hausdorff space is normal",
                area="topology",
                topic="compactness",
                body="Let $X$ be compact Hausdorff. Show $X$ is normal.",
            ),
            "PRB-CON.md": PROBLEM.format(
                id="PRB-CON",
                title="The continuous image of a connected space is connected",
                area="topology",
                topic="connectedness",
                body="Let $f: X \\to Y$ be continuous and $X$ connected. Show $f(X)$ is connected.",
            ),
            "PRB-SEP.md": PROBLEM.format(
                id="PRB-SEP",
                title="A metric space is normal",
                area="topology",
                topic="continuity",
                body="Let $X$ be a metric space. Show $X$ is normal.",
            ),
        },
    )
    guide = manifest("compactness", "connectedness")
    (work / "publications" / "topology-guide.yaml").write_text(yaml.safe_dump(guide, sort_keys=False))

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    page = read_html(work / "build" / "quarto" / "_site" / "guide" / "GUIDE-TOPOLOGY" / "compactness.html")
    panels = page.root.find_all("div", **{"class": "panel generator-link"})
    assert len(panels) == 1
    links = panels[0].find_all("a")
    assert links[0].attrs["href"] == "../../generate.html?area=topology&kind=problem&topic=compactness&topic=connectedness"
    assert "data-count" not in panels[0].attrs


def test_an_exercise_query_preserves_its_kind_without_needing_a_matching_card(tmp_path: Path) -> None:
    """Rendering a generator link never snapshots the catalog at build time."""
    work = fixture_repo(tmp_path, {})
    (work / "publications" / "topology-guide.yaml").write_text(yaml.safe_dump(manifest("compactness", kind="exercise"), sort_keys=False))

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    page = read_html(work / "build" / "quarto" / "_site" / "guide" / "GUIDE-TOPOLOGY" / "compactness.html")
    panel = page.root.find_all("div", **{"class": "panel generator-link"})[0]
    link = panel.find_all("a")[0]
    assert link.attrs["href"] == "../../generate.html?area=topology&kind=exercise&topic=compactness"


def test_the_generator_can_realize_the_complete_guide_filter(tmp_path: Path) -> None:
    """The destination understands kind plus an OR-family of repeated topics."""
    work = fixture_repo(tmp_path)
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    generator_path = work / "build" / "quarto" / "_site" / "generate.html"
    page = read_html(generator_path)
    kind = page.root.find_all("select", id="gen-kind")[0]
    assert [(option.attrs["value"], option.text) for option in kind.find_all("option")] == [
        ("problem", "Problems"),
        ("exercise", "Exercises"),
    ]

    topics = page.root.find_all("select", id="gen-topic")[0]
    assert "multiple" in topics.attrs

    source = generator_path.read_text()
    assert 'const topics=p.getAll("topic");' in source
    assert "const filters={kind};" in source
    assert "filters.topic={any:topics};" in source


def test_reference_material_cannot_be_selected_by_a_publication_query() -> None:
    """A guide authors reference material explicitly; it never derives a catalog panel."""
    guide = manifest("compactness", kind="definition")

    with pytest.raises(ValidationError) as exc_info:
        PublicationManifest.model_validate(guide)

    assert "Input should be 'problem' or 'exercise'" in str(exc_info.value)


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


def test_a_section_that_names_and_queries_a_card_lists_it_once(tmp_path: Path) -> None:
    """A guide section surfaces a card once, however many ways it reaches it.

    The section names `PRB-CPT` as a `ref:` and also carries a topic query that
    matches the same card. Each used to append its own Guide Appearance, so the
    card page listed the one section twice.
    """
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
    manifest = {
        "schema": "qual/publication@2",
        "id": "GUIDE-TOPOLOGY",
        "kind": "study-guide",
        "title": "Topology",
        "lede": "A short topology guide.",
        "sections": [
            {
                "slug": "compactness",
                "title": "Compactness",
                "parent": "GUIDE-TOPOLOGY",
                "lede": "Open covers and finite subcovers.",
                "items": [
                    {"ref": "PRB-CPT"},
                    {
                        "query": {
                            "kind": "problem",
                            "topics": ["compactness"],
                            "limit": 5,
                            "review": {"mode": "any"},
                        }
                    },
                ],
            }
        ],
    }
    (work / "publications" / "topology-guide.yaml").write_text(yaml.safe_dump(manifest, sort_keys=False))

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    card = read_html(work / "build" / "quarto" / "_site" / "tag" / "PRB-CPT.html")
    groups = card.root.find_all("section", **{"data-relation-group": "guide-appearances"})
    assert len(groups) == 1
    assert [li.text for li in groups[0].find_all("li")] == ["Compactness"]


def test_a_query_match_is_not_a_guide_appearance(tmp_path: Path) -> None:
    """A generator query points outward; its result set is not displayed guide content."""
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
    (work / "publications" / "topology-guide.yaml").write_text(yaml.safe_dump(manifest("compactness"), sort_keys=False))

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    card = read_html(work / "build" / "quarto" / "_site" / "tag" / "PRB-CPT.html")
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


def test_a_guide_breadcrumb_is_where_the_page_is_filed(tmp_path: Path) -> None:
    """A guide section's `parent` is the section it assumes, not its place.

    Walking that chain made the breadcrumb a prerequisite list -- `Algebra /
    Preliminaries / Rings and Ideals / Modules / Linear Algebra` -- while the
    same crumb in the wiki was a folder path. The sidebar is where the
    prerequisite tree belongs; the breadcrumb says where the page is.
    """
    work = fixture_repo(
        tmp_path,
        {
            "PRB-CPT.md": PROBLEM.format(
                id="PRB-CPT",
                title="Compact",
                area="topology",
                topic="compactness",
                body="Show it.",
            )
        },
    )
    (work / "publications" / "topology-guide.yaml").write_text(yaml.safe_dump(reference_manifest("second"), sort_keys=False))

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    site = work / "build" / "quarto" / "_site"

    # `second` names `first` as its parent, and `first` names the guide.
    section = read_html(site / "guide" / "GUIDE-TOPOLOGY" / "second.html")
    crumbs = section.root.find_all("nav", **{"class": "breadcrumbs"})[0].find_all("a")
    assert [(link.text, link.attrs["href"]) for link in crumbs] == [
        ("Guides", "../../guides.html"),
        ("Topology", "../GUIDE-TOPOLOGY.html"),
        ("Second", "second.html"),
    ]

    root = read_html(site / "guide" / "GUIDE-TOPOLOGY.html")
    root_crumbs = root.root.find_all("nav", **{"class": "breadcrumbs"})[0].find_all("a")
    assert [(link.text, link.attrs["href"]) for link in root_crumbs] == [
        ("Guides", "../guides.html"),
        ("Topology", "GUIDE-TOPOLOGY.html"),
    ]
