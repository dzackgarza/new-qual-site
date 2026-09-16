"""A card whose front matter repeats a key is unreadable, not silently merged.

YAML's safe loader keeps the last of two equal keys. Two writers appending to
one card produced two `audit:` lists, and single-card validation reported the
card sound while one list was discarded.
"""

from __future__ import annotations

from pathlib import Path

from conftest import diagnostic_codes, fixture_repo
from qualc.diagnostics import DiagnosticCode

REPEATED_TITLE = """---
schema: qual/card@1
id: P-TWOTITLES
kind: problem
title: The first title
title: The second title
classification:
  areas: [algebra]
  topics: [Groups]
relations: []
review: draft
---

::: problem
Show that a group of prime order is cyclic.
:::
"""


def test_a_repeated_front_matter_key_makes_the_card_unreadable(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path, {"P-TWOTITLES.md": REPEATED_TITLE})

    assert DiagnosticCode.CARD_UNREADABLE in diagnostic_codes(work)
