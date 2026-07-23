"""A pandoc warning while reading a card is a build failure.

`qualc` discarded pandoc's stderr, so a card pandoc had complained about was
indexed anyway. That is what this guards.

Read the provenance of the fixture below before citing it for anything.

**The input is mine, not the corpus's.** No card and no file in qual-wiki
provokes it; the measured count is zero across all 263 authored files. `\\qty` is
a math-mode macro and nobody writes it in text mode. It appeared in text mode
only because the reader was misconfigured: without `tex_math_single_backslash`
the `\\[ ... \\]` delimiters were consumed as escaped brackets, so the math
*contents* were spilled into the text-mode parser. Fixing the dialect took the
warning count from 19 to 0. The fixture below re-enacts that misconfiguration by
hand, which is the only way to reach this state now.

So this is a demonstration that the gate fires, not evidence of a hazard. It was
originally written up as the latter, along with three successive explanations of
pandoc's internals, none of which I could support:

  1. "an unknown macro runs away" -- refuted by `\\foobar{x}`, which bounds fine;
  2. "pandoc implements siunitx's two-argument `\\qty`" -- taken from a web-search
     paraphrase, never checked against pandoc's source or documentation;
  3. anything about packages or macro semantics. Pandoc passes raw TeX through.

What is measured, and all that is claimed, with pandoc 3.6.1 in text mode:

    \\qty{3}{\\metre}  ->  raw-TeX span ends there
    \\qty{3}          ->  raw-TeX span runs to end of input, taking `:::` with it
    \\foobar{x}       ->  span ends there

Something decides the extent of a raw-TeX span and it varies by input. What, I do
not know, and the gate does not depend on knowing.

The corpus's actual usage is asserted in `test_qty_in_math_is_untouched` so this
file cannot be misread as a finding against `\\qty`.
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
