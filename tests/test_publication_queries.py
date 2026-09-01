"""What a study guide's catalog panel is allowed to list.

The panel is titled "More from the catalog" and sits inside a subject section,
so a problem from another subject in it is a wrong answer, not a wide one.
Topic terms are shared across subjects -- `integrals` carries both real- and
complex-analysis problems in the real corpus -- so topic alone cannot scope it.

Within the subject, several topics name a family: topic vocabulary is finer than
a section, and a section about convergence covers four terms of it. A panel
naming them lists a problem carrying any one.
"""

from __future__ import annotations

from pathlib import Path

import yaml
from conftest import diagnostic_codes, fixture_repo, run_qualc
from qualc.diagnostics import DiagnosticCode
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


DEFINITION = """---
schema: qual/card@1
id: {id}
kind: definition
title: {title}
classification:
  areas:
  - topology
  topics:
  - {topic}
relations: []
review: draft
---

::: {{.definition}}
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


def test_a_problem_panel_is_a_deep_link_into_the_generator(tmp_path: Path) -> None:
    """A problem query does not re-list the catalog; it points into it.

    The generator owns the listing, so the guide keeps a single call to action
    carrying the area and zero-in on the topic. The count is still scoped to the
    subject: the real-analysis problem carries `compactness` but belongs to a
    different area, and it must not enter the count -- the defect this proves
    absent.
    """
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
    assert links[0].attrs["href"] == "../../generate.html?area=topology&topic=compactness"

    # The generator is single-select over topic, so `compactness` is zeroed in;
    # the RA problem never enters the scoped count.
    assert panels[0].attrs["data-count"] == "1"
    assert panels[0].attrs["data-query-kind"] == "problem"


def test_a_problem_panel_count_spans_the_topics_it_names(tmp_path: Path) -> None:
    """`run_query` still ORs the topics; a card carrying any one is counted.

    The guide's wording names the family -- several topics under one section
    lead. `PRB-CPT` and `PRB-CON` each carry one named topic and are both in;
    `PRB-SEP` carries neither and proves the panel tracks the query, not the
    whole subject.
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
    assert panels[0].attrs["data-count"] == "2"

    # The first topic scopes the deep link; the generator's single select cannot
    # span a family, and the family is what run_query counted.
    links = panels[0].find_all("a")
    assert links[0].attrs["href"] == "../../generate.html?area=topology&topic=compactness"


def test_a_definition_panel_still_offers_a_static_listing(tmp_path: Path) -> None:
    """The generator drills problems; a definition is reference, not practice.

    Only problem and exercise kinds become a deep link. A definition stays a
    `publication-query` panel -- a heading and the cards that carry the term --
    because a reader does not go to the generator to drill a definition.
    """
    work = fixture_repo(
        tmp_path,
        {
            "D-CPT.md": DEFINITION.format(
                id="D-CPT",
                title="Compact",
                topic="compactness",
                body="A space is compact when every open cover has a finite subcover.",
            )
        },
    )
    (work / "publications" / "topology-guide.yaml").write_text(yaml.safe_dump(manifest("compactness", kind="definition"), sort_keys=False))

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    page = read_html(work / "build" / "quarto" / "_site" / "guide" / "GUIDE-TOPOLOGY" / "compactness.html")
    panels = page.root.find_all("section", **{"class": "panel publication-query"})
    assert len(panels) == 1
    assert panels[0].attrs["data-query-kind"] == "definition"
    listed = {link.attrs["href"] for link in panels[0].find_all("a")}
    assert listed == {"../../tag/D-CPT.html"}
    assert panels[0].attrs["data-count"] == "1"


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
    assert first.root.find_all("section", **{"data-card-id": "PRB-CPT"}) == []
    assert len(second.root.find_all("section", **{"data-card-id": "PRB-CPT"})) == 1


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
