"""A card page gives hints their own disclosure tier before solutions.

Hints and solutions are sections of the problem/exercise card. A hint stops
being a hint once the answer is already on the screen above it, so authored
problem bodies place `.hint` before `.solution`.
"""

from __future__ import annotations

import re
from pathlib import Path

from conftest import fixture_repo, run_qualc

SUMMARY = re.compile(r"<summary[^>]*>(.*?)</summary>", re.S)

PROBLEM_ANSWERING_ITSELF = """---
schema: qual/card@1
id: P-SELFANS
kind: problem
title: A problem whose own body carries a solution
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
relations: []
review: draft
---

::: problem
Let $G$ be a group of order $56$. Show that $G$ has a normal Sylow subgroup.
:::

::: hint
Count the elements of order $7$ and see how many are left over.
:::

::: solution
Counting Sylow 7-subgroups gives $n_7 \\in \\{1, 8\\}$. If $n_7 = 8$ the
$8 \\cdot 6 = 48$ elements of order 7 leave exactly 8 others, which must form
the unique Sylow 2-subgroup.
:::
"""


def test_a_card_page_shows_its_hint_above_its_solutions(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path, {"P-SELFANS.md": PROBLEM_ANSWERING_ITSELF})

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    page = (work / "build" / "quarto" / "_site" / "tag" / "P-SELFANS.html").read_text()
    labels = [re.sub(r"<[^>]+>", "", summary).strip().split(":")[0] for summary in SUMMARY.findall(page)]

    assert labels == ["Hint", "Solution"], labels
