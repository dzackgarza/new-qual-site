"""A card page shows its hint above its solutions.

A hint stops being a hint once the answer is already on the screen above it.
The order is not the order the blocks arrive in: a problem may write a solution
into its own body and carry a hint as a separate card, and appending the related
cards after the body puts that hint below the solution it was meant to precede.
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

::: solution
Counting Sylow 7-subgroups gives $n_7 \\in \\{1, 8\\}$. If $n_7 = 8$ the
$8 \\cdot 6 = 48$ elements of order 7 leave exactly 8 others, which must form
the unique Sylow 2-subgroup.
:::
"""

HINT = """---
schema: qual/card@1
id: H-SELFANS
kind: hint
title: Count the elements of order seven
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
relations:
- kind: hints-at
  target: P-SELFANS
review: draft
---

::: hint
Count the elements of order $7$ and see how many are left over.
:::
"""


def test_a_card_page_shows_its_hint_above_its_solutions(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path, {"P-SELFANS.md": PROBLEM_ANSWERING_ITSELF, "H-SELFANS.md": HINT})

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    page = (work / "build" / "quarto" / "_site" / "tag" / "P-SELFANS.html").read_text()
    labels = [re.sub(r"<[^>]+>", "", summary).strip().split(":")[0] for summary in SUMMARY.findall(page)]

    assert labels == ["Hint", "Solution"], labels
