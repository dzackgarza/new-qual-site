"""`\\[ ... \\]` is display mathematics, and the reader has to be told so.

Pandoc's `markdown` reader does not treat `\\[` as math. With `raw_tex` on — the
default — it reads the fragment as raw LaTeX instead, and two things follow:

1. The mathematics is destroyed on the way through. `\\int_{\\mathbb{R}}` comes
   back out as ``\\int`{=tex}*{`\\mathbb{R}`{=tex}}``: the subscript underscore
   has become an emphasis marker. Four cards in `corpus/` are already stored in
   that state, written by the importer.
2. The raw-TeX reader consumes past the end of the fenced div. A `::: example`
   whose body contains `\\qty{ x }` inside `\\[ ... \\]` swallows its own closing
   `:::` and everything after it, which pandoc reports as an unclosed div. That
   accounts for all 19 such warnings across qual-wiki's 263 authored files —
   they are a reader misconfiguration here, not missing fences there.

The fix is the `tex_math_single_backslash` extension at every markdown read.
"""

from __future__ import annotations

from pathlib import Path

import panflute as pf
import pytest
from qualc.model import parse_card

CARD = """---
schema: qual/card@1
id: P-MATH1
kind: problem
title: A problem stated with display mathematics
classification:
  areas: [real-analysis]
  topics: [integrals]
relations: []
review: draft
---

::: problem
Show that
\\[
\\int_{\\mathbb{R}} f = \\int_0^{\\infty} m(\\qty{ x : f(x) > t }) \\,dt
.\\]
:::

::: remark
This sentence is outside the problem and must stay outside it.
:::
"""


@pytest.fixture
def card(tmp_path: Path) -> Path:
    p = tmp_path / "P-MATH1.md"
    p.write_text(CARD)
    return p


def test_display_math_reaches_the_ast_as_math(card: Path) -> None:
    from qualc.model import from_ast

    doc = from_ast(parse_card(card).ast)
    maths = [el.text for el in doc.walk(lambda e, d: e).content[0].content[0].content if isinstance(el, pf.Math)]
    assert maths, "the \\[ ... \\] block must parse as Math, not raw TeX"
    assert "\\int_{\\mathbb{R}}" in maths[0], maths[0]


def test_the_subscript_survives_a_round_trip(card: Path) -> None:
    """The importer's failure, reproduced: read markdown, write it back.

    Read as raw TeX, `\\int_{\\mathbb{R}}` returns as
    ``\\int`{=tex}*{`\\mathbb{R}`{=tex}}`` -- the subscript underscore reinterpreted
    as an emphasis marker. Four cards in `corpus/` are stored in that state.
    """
    from qualc.model import from_ast

    doc = from_ast(parse_card(card).ast)
    back: str = pf.convert_text(doc, input_format="panflute", output_format="markdown", extra_args=["--wrap=preserve"])
    assert "{=tex}" not in back, back
    assert "\\int_{\\mathbb{R}}" in back, back


def test_raw_tex_does_not_swallow_the_closing_fence(card: Path) -> None:
    """`\\qty` is unknown to pandoc, and unknown macros consume past the fence."""
    sections = parse_card(card).sections
    assert [k for k, _ in sections] == ["problem", "remark"], sections
    problem_text = next(text for kind, text in sections if kind == "problem")
    assert "must stay outside it" not in problem_text, problem_text
