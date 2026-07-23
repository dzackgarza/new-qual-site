"""A pandoc warning while reading a card is a build failure.

`tex_math_single_backslash` fixed the `\\[ ... \\]` reading, and with it every
unclosed-div warning currently in qual-wiki. It did not fix the mechanism
underneath, which is independent of `\\[`:

    :::{.example}
    \\qty{ x }
    :::

    after

pandoc's raw-TeX inline parser starts on `\\qty` and does not stop at the fence.
The AST is `RawInline (Format "tex") "\\qty{ x }\\n:::\\n\\nafter"` -- the closing
`:::` and the whole rest of the document are inside the raw chunk. `\\alpha{ x }`
in the same position is bounded correctly, and declaring `\\newcommand{\\qty}`
does not help: pandoc expands it and still runs to the end.

It happens to be harmless in qual-wiki today only because every `\\qty` there
sits inside `\\[ ... \\]`, which is now Math and so never reaches that parser.
That is luck, not a property of the corpus, and losing the tail of a file
silently is the exact failure this compiler exists to prevent.

pandoc already reports it. The fix is to stop discarding what it says.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from qualc.model import parse_card

SWALLOWED = """---
schema: qual/card@1
id: E-SWALLOW
kind: example
title: A card whose closing fence is eaten by an unresolvable macro
classification:
  areas: [algebra]
  topics: [groups]
relations: []
review: draft
---

::: example
\\qty{ x }
:::

This paragraph is outside the example.
"""


def test_a_reader_warning_fails_the_build(tmp_path: Path) -> None:
    p = tmp_path / "E-SWALLOW.md"
    p.write_text(SWALLOWED)
    with pytest.raises(Exception) as excinfo:
        parse_card(p)
    assert "unclosed" in str(excinfo.value).lower() or "warning" in str(excinfo.value).lower(), excinfo.value


def test_the_real_corpus_reads_without_warnings() -> None:
    """The gate is worth nothing if the corpus does not pass it."""
    from qualc.model import discover

    for path in discover(Path(__file__).resolve().parent.parent / "corpus"):
        parse_card(path)
