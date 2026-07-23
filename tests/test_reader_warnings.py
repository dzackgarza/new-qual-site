"""A pandoc warning while reading a card is a build failure.

`qualc` discarded pandoc's stderr, so a card pandoc had complained about was
indexed anyway. That is the defect this file guards: the compiler should not
store a parse the parser said it was unsure of, whatever the reason.

The trigger below is synthetic, and deliberately labelled as such. It is *not* a
hazard the corpus exhibits -- there is no card, and no file in qual-wiki, that
provokes it. It is here because it is the smallest input that makes pandoc emit
a reader warning while producing a plausible-looking AST, which is exactly the
shape the guard exists to catch.

What it is, for the record, because it was twice diagnosed wrongly:

`\\qty` is two different LaTeX macros. In `physics` it is the auto-sizing
delimiter `\\qty{...}`, one argument, which is what this corpus writes. In
`siunitx` v3 it is `\\qty{number}{unit}`, two arguments. Pandoc's LaTeX reader
implements the siunitx one, so given a single group it keeps scanning for the
second argument and consumes the closing `:::` and every block after it:

    \\qty{3}{\\metre}   ->  RawInline "\\qty{3}{\\metre}", div closes
    \\qty{3}          ->  RawInline "\\qty{3}\\n:::\\n\\nafter", div swallowed

It is not "an unknown macro running away" -- `\\foobar{x}` parses fine and closes
the div. It is a known macro with a missing argument, and a name collision
between two packages.

None of this reaches the corpus, because `\\qty` there is always inside math, and
pandoc hands math to MathJax without parsing it. Both `$\\qty{x}$` and
`\\[ \\qty{x} \\]` are `Math` nodes with the div intact.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from qualc.model import parse_card

# `\qty{3}` in text mode: correct physics-package usage, wrong package as far as
# pandoc is concerned, and no corpus card is written this way.
SWALLOWED = """---
schema: qual/card@1
id: E-SWALLOW
kind: example
title: A card whose closing fence is eaten by a half-applied macro
classification:
  areas: [algebra]
  topics: [groups]
relations: []
review: draft
---

::: example
\\qty{3}
:::

This paragraph is outside the example.
"""


def test_a_reader_warning_fails_the_build(tmp_path: Path) -> None:
    p = tmp_path / "E-SWALLOW.md"
    p.write_text(SWALLOWED)
    with pytest.raises(Exception) as excinfo:
        parse_card(p)
    assert "unclosed" in str(excinfo.value).lower(), excinfo.value


def test_qty_in_math_is_untouched(tmp_path: Path) -> None:
    """The corpus's actual usage, asserted so the guard is not read as a ban on it."""
    p = tmp_path / "E-MATH.md"
    p.write_text(SWALLOWED.replace("\\qty{3}", "$\\qty{3}$").replace("E-SWALLOW", "E-MATH"))
    kinds = [k for k, _ in parse_card(p).sections]
    assert kinds == ["example"], kinds


def test_the_real_corpus_reads_without_warnings() -> None:
    """The gate is worth nothing if the corpus does not pass it."""
    from qualc.model import discover

    for path in discover(Path(__file__).resolve().parent.parent / "corpus"):
        parse_card(path)
