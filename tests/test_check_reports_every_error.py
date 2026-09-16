"""`qualc check` reports every independent error in one run (issue #89).

An unreadable card used to stop validation before the corpus-level checks and
the wiki ran, so a second, unrelated error in another file stayed invisible
until the first was repaired and the check rerun. With several authors writing
at once, each saw only whichever error sorted first.
"""

from __future__ import annotations

from pathlib import Path

from conftest import diagnostic_codes, fixture_repo
from qualc.diagnostics import DiagnosticCode

UNREADABLE = """---
schema: qual/card@1
id: P-BROKENYAML
kind: problem
title: [unclosed
---

::: problem
State something.
:::
"""

UNKNOWN_AREA = """---
schema: qual/card@1
id: P-NOAREA
kind: problem
title: A problem filed under an area that does not exist
classification:
  areas: [numerology]
  topics: [groups]
relations: []
review: draft
---

::: problem
Show that every group of prime order is cyclic.
:::
"""

BROKEN_WIKI_LINK = """---
title: Orphan page
order: 2
---

# Orphan page

See [[A page that does not exist]].
"""


def test_one_check_reports_card_corpus_and_wiki_errors_together(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path, {"broken.md": UNREADABLE, "noarea.md": UNKNOWN_AREA})
    (work / "wiki" / "Algebra" / "orphan.md").write_text(BROKEN_WIKI_LINK)

    codes = set(diagnostic_codes(work))

    assert DiagnosticCode.CARD_UNREADABLE in codes
    assert DiagnosticCode.UNKNOWN_AREA in codes
    assert DiagnosticCode.PAGE_REFERENCE_MISSING in codes
