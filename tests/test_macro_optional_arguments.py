r"""A macro declared with an optional first parameter travels as declared.

`\surjectsvia` is declared `\newcommand{\surjectsvia}[2][]{...}`: two parameters,
the first optional and empty by default. Reading only the body lost that, so the
mirror handed MathJax two mandatory parameters, and `\surjectsvia{\exp}` rendered
with `\exp` below the arrow and a bare `(` above it, while the same source under
the author's preamble renders `\exp` above the arrow (#164). The declaration, not
the body alone, is what both renderers need.
"""

from __future__ import annotations

import json
import re

import sync_macros
from qualc.emit import mathjax_header, tex_preamble

BODY = r"\xrightarrow[#1]{#2} { \mathrel{\mkern-16mu}\rightarrow }\,"
DECLARATION = "\\newcommand{\\surjectsvia}[2][]{" + BODY + "}\n"


def test_the_optional_parameter_is_read_off_the_declaration() -> None:
    assert sync_macros.definitions(DECLARATION)["surjectsvia"] == [BODY, 2, ""]


def test_a_macro_without_an_optional_parameter_is_its_body() -> None:
    assert sync_macros.definitions("\\newcommand{\\dd}{\\mathrm{d}}\n")["dd"] == "\\mathrm{d}"


def test_the_emitted_preamble_declares_the_optional_parameter() -> None:
    assert tex_preamble({"\\surjectsvia": [BODY, 2, ""]}) == (
        "\\newcommand{\\surjectsvia}[2][]{" + BODY + "}"
    )


def test_mathjax_receives_the_optional_default() -> None:
    header = mathjax_header({"\\surjectsvia": [BODY, 2, ""]})
    match = re.search(r"macros: (\{.*?\}), inlineMath", header)
    assert match is not None, "the header must embed the macros JSON"
    assert json.loads(match.group(1))["surjectsvia"] == [BODY, 2, ""]
