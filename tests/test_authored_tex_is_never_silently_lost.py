"""Authored TeX that the site cannot show fails `qualc check` instead of vanishing.

Two ways mathematics reached a page as nothing:

* Pandoc reads a TeX command written in prose as raw TeX and the HTML writer
  drops it, so `A \\foo{group} is a set.` rendered as `A is a set.`. The one
  supported inline command is `\\dfn{term}`, which marks a term being defined.
* A math span calling a macro that neither the preamble (`vocabularies/macros.json`)
  nor MathJax defines rendered as red source, and `check` reported OK (issue #87).
"""

from __future__ import annotations

import re
from pathlib import Path

from conftest import diagnostic_codes, fixture_repo, run_qualc
from qualc.diagnostics import DiagnosticCode


def definition(card_id: str, body: str) -> str:
    return f"""---
schema: qual/card@1
id: {card_id}
kind: definition
title: A definition used by the TeX tests
classification:
  areas: [algebra]
  topics: [Groups]
relations: []
review: draft
---

::: definition
{body}
:::
"""


def test_an_unsupported_inline_tex_command_is_reported(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path, {"D-RAWTEX.md": definition("D-RAWTEX", "A \\textsc{normal} subgroup is fixed by conjugation.")})

    assert DiagnosticCode.RAW_TEX_DROPPED in diagnostic_codes(work)


def test_an_undefined_macro_in_mathematics_is_reported(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path, {"D-UNDEF.md": definition("D-UNDEF", "The sheaf $\\mcF$ is flasque.")})

    assert DiagnosticCode.UNDEFINED_MACRO in diagnostic_codes(work)


def test_preamble_and_mathjax_macros_are_accepted(tmp_path: Path) -> None:
    body = "A \\dfn{group} on $\\RR^n$ with $\\operatorname{Aut}(G) \\cong \\mathbb{Z}/2$ and $\\langle x \\rangle$."
    work = fixture_repo(tmp_path, {"D-KNOWN.md": definition("D-KNOWN", body)})

    assert diagnostic_codes(work) == []


def test_a_defined_term_renders_as_a_dfn_element(tmp_path: Path) -> None:
    body = "A finite group is a \\dfn{$p$-group} if its order is a power of the prime $p$."
    work = fixture_repo(tmp_path, {"D-DFN.md": definition("D-DFN", body)})

    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    page = (work / "build" / "quarto" / "_site" / "tag" / "D-DFN.html").read_text()
    [term] = re.findall(r'<dfn class="qual-dfn">(.*?)</dfn>', page, re.S)
    assert 'class="math inline"' in term
    assert re.sub(r"<[^>]+>", "", term) == "\\(p\\)-group"
    assert "power of the prime" in " ".join(page.split())
