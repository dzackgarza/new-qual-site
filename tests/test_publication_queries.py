"""A study guide's catalog panel is scoped to that guide's subject.

The panel is titled "More from the catalog" and sits inside a subject section,
so a problem from another subject in it is a wrong answer, not a wide one.
Topic terms are shared across subjects -- `integrals` carries both real- and
complex-analysis problems in the real corpus -- so topic alone cannot scope it.
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
  - compactness
relations: []
review: draft
---

::: problem
{body}
:::
"""

MANIFEST = {
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
                        "topics": ["compactness"],
                        "limit": 5,
                        "review": {"mode": "any"},
                    }
                }
            ],
        }
    ],
}


def test_a_subject_guide_panel_lists_only_that_subject(tmp_path: Path) -> None:
    work = fixture_repo(
        tmp_path,
        {
            "PRB-CPT-TOP.md": PROBLEM.format(
                id="PRB-CPT-TOP",
                title="A compact Hausdorff space is normal",
                area="topology",
                body="Let $X$ be compact Hausdorff. Show $X$ is normal.",
            ),
            "PRB-CPT-RA.md": PROBLEM.format(
                id="PRB-CPT-RA",
                title="A continuous function on a compact interval is uniformly continuous",
                area="real-analysis",
                body="Let $f$ be continuous on $[0,1]$. Show $f$ is uniformly continuous.",
            ),
        },
    )
    (work / "publications" / "topology-guide.yaml").write_text(yaml.safe_dump(MANIFEST, sort_keys=False))

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
