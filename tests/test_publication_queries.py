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
from conftest import fixture_repo, run_qualc
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
                            "kind": "problem",
                            "topics": list(topics),
                            "limit": 5,
                            "review": {"mode": "any"},
                        }
                    }
                ],
            }
        ],
    }


def reference_manifest(section: str) -> dict[str, object]:
    sections = []
    for slug, title in (("first", "First"), ("second", "Second")):
        items = [{"ref": "PRB-CPT"}] if slug == section else []
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


def test_a_subject_guide_panel_lists_only_that_subject(tmp_path: Path) -> None:
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
    panels = page.root.find_all("section", **{"class": "panel publication-query"})
    assert len(panels) == 1
    listed = {link.attrs["href"] for link in panels[0].find_all("a")}

    # Both problems carry `compactness`; only the topology one belongs to this
    # guide. The real-analysis problem is the defect this proves absent.
    assert listed == {"../../tag/PRB-CPT-TOP.html"}
    assert panels[0].attrs["data-count"] == "1"


def test_a_panel_naming_several_topics_lists_a_problem_carrying_any_of_them(
    tmp_path: Path,
) -> None:
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
    panels = page.root.find_all("section", **{"class": "panel publication-query"})
    listed = {link.attrs["href"] for link in panels[0].find_all("a")}

    # No card carries both terms, so conjunction returns nothing and the build
    # fails before it reaches here. `PRB-SEP` carries neither and proves the
    # panel is still a query rather than the whole subject.
    assert listed == {"../../tag/PRB-CPT.html", "../../tag/PRB-CON.html"}
    assert panels[0].attrs["data-count"] == "2"


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
