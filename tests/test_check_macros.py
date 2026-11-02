"""The fast macro checker reads the corpus dialect, not the raw card text.

Two false-rejection classes, both taken from real cards when this was written:
`P-AGH210CONE` carries `\\dfn{affine cone}`, the one supported prose command,
which `qualc.tex.mark_definienda` rewrites before Pandoc reads the card; and
`T-SKJB2` carries a tikzcd environment, which the emitter compiles to SVG
(`emit._compile_tikzcd`). Neither control word ever reaches MathJax, so neither
is undefined, but the checker scanned authored text directly and rejected both --
699 `\\dfn` cards and every diagram card in the corpus at the time.

The regressions pin the checker to `qualc.tex.checkable_tex`, the
markdown-level image of `unrenderable_tex`'s exclusions, while keeping the true
detections: a glued `\\mapstov_1` and an undefined macro. The known set is
deliberately tiny and does not contain `dfn` or `arrow`, so a pass here cannot
come from an allowlist entry.
"""

from __future__ import annotations

from pathlib import Path

import check_macros

KNOWN = frozenset({"ZZ"})


def test_a_defined_term_is_not_an_undefined_macro() -> None:
    body = "The \\dfn{affine cone} over $Y$ is the closure of $\\ZZ$."

    assert check_macros.unknown_control_words(body, KNOWN) == []


def test_an_unbalanced_dfn_is_still_reported() -> None:
    # mark_definienda leaves an unbalanced \dfn{ as written, and the full gate
    # reports it as dropped raw TeX, so the fast check must still see it.
    body = "The \\dfn{unbalanced term is broken."

    assert check_macros.unknown_control_words(body, KNOWN) == ["dfn"]


def test_a_tikzcd_environment_is_not_scanned() -> None:
    body = "A pullback square, as in T-SKJB2:\n\n\\begin{tikzcd}\n\t{Y} && {\\tilde X} \\\\\n\t\\arrow[\"{p}\", from=1-3, to=3-3]\n\\end{tikzcd}\n"

    assert check_macros.unknown_control_words(body, KNOWN) == []


def test_code_is_not_tex() -> None:
    body = "Run `\\notdefined` in the shell, and\n\n```\n\\alsoundefined\n```\n\nbut $\\ZZ$ is a macro."

    assert check_macros.unknown_control_words(body, KNOWN) == []


def test_a_glued_control_word_is_reported() -> None:
    body = "The map $x \\mapstov_1 y$ glues a command to a variable."

    assert check_macros.unknown_control_words(body, KNOWN) == ["mapstov"]


def test_an_undefined_macro_is_reported() -> None:
    body = "The quotient $\\ZZ / \\q$ uses an undefined macro."

    assert check_macros.unknown_control_words(body, KNOWN) == ["q"]


def _card(title: str, prompt: str, note: str = "Nothing to see.") -> str:
    return f"""---
id: P-TEST
kind: problem
title: {title}
prompts:
- {prompt}
audit:
- event: solution-written
  by: claude
  date: 2026-11-02
  note: >-
    {note}
---

::: {{.problem}}
Show that $\\ZZ$ is cyclic.
:::
"""


def test_non_rendered_metadata_is_not_mathematics() -> None:
    # An audit note's X\C is prose about mathematics and "Rouch\xE9" in a
    # non-rendered field is a YAML escape: neither reaches a reader, so neither
    # is scanned.
    body = _card(
        title="A valid title about $\\ZZ$",
        prompt="'Why is $\\ZZ$ cyclic?'",
        note="For the shrinking step, A=C\\O2 and B=C\\O1, as Rouch\\xE9 noted.",
    )

    assert check_macros.unknown_control_words(body, KNOWN) == []


def test_an_undefined_macro_in_a_title_is_reported() -> None:
    # Titles are rendered page text whose $...$ spans typeset_dashes preserves,
    # so an undefined macro there is red source exactly as in the body.
    body = _card(
        title="A valid title about $\\undefinedword$",
        prompt="'Why is $\\ZZ$ cyclic?'",
    )

    assert check_macros.unknown_control_words(body, KNOWN) == ["undefinedword"]


def test_an_undefined_macro_in_a_prompt_is_reported() -> None:
    body = _card(
        title="A valid title about $\\ZZ$",
        prompt="'Why is $\\undefinedword$ cyclic?'",
    )

    assert check_macros.unknown_control_words(body, KNOWN) == ["undefinedword"]


def test_a_slogan_with_an_undefined_macro_is_reported() -> None:
    body = _card(
        title="A valid title about $\\ZZ$",
        prompt="'Why is $\\ZZ$ cyclic?'",
    ).replace("prompts:\n", "slogan: Every $\\undefinedword$-module is free\nprompts:\n")

    assert check_macros.unknown_control_words(body, KNOWN) == ["undefinedword"]


def test_a_yaml_escape_in_a_rendered_field_decodes() -> None:
    # The front matter is read through the YAML loader, so \xE9 decodes to é
    # before the scan instead of surfacing as a control word. (A double-quoted
    # scalar cannot also hold $\ZZ$: \Z is not a YAML escape, which is the
    # next test's point.)
    body = _card(
        title='"Rouch\xE9 counts the zeros"',
        prompt="'Why is $\ZZ$ cyclic?'",
    )

    assert check_macros.unknown_control_words(body, KNOWN) == []


def test_an_unparseable_card_is_scanned_whole() -> None:
    # \Z is not a YAML escape, so the double-quoted title makes the front
    # matter unparseable. The fallback then scans the raw text, including the
    # audit note the rendered-field pass would ignore -- which can only add
    # flags, never lose one.
    body = _card(
        title='"$\ZZ$"',
        prompt="'Why is $\ZZ$ cyclic?'",
        note="The note may mention $\q$ when the card does not parse.",
    )

    assert check_macros.unknown_control_words(body, KNOWN) == ["q"]

def test_the_cli_checks_a_file(tmp_path: Path, capsys) -> None:
    good = tmp_path / "good.md"
    good.write_text("The \\dfn{cone} over $\\ZZ$ is a scheme.\n", encoding="utf-8")
    bad = tmp_path / "bad.md"
    bad.write_text("The glued $\\mapstov_1$ map.\n", encoding="utf-8")

    assert check_macros.main([str(good)]) == 0
    assert check_macros.main([str(bad)]) == 1
    reported = capsys.readouterr().out
    assert "bad.md: undefined control word(s): \\mapstov" in reported
