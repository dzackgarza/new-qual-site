r"""Reading the author's preamble the way LaTeX reads it.

Every line of the fixture below is copied from
`/home/dzack/Dropbox/pandoc/custom`, and each one stands for a macro the
previous sync got wrong: `\too` was frozen at its first definition and took an
argument the corpus never gives it, `\qty` and `\one` were invisible because
they live in a file `latexmacs*.tex` does not glob, `\Aut` and the 62 other
declared operators were not recognised as definitions at all, and `\exp` was
read out of a commented-out line, in terms of an `\oldexp` nothing defines. The
preamble is not in this repository, so the fixture carries the lines rather
than the path.
"""

from __future__ import annotations

from pathlib import Path

from sync_macros import definitions, preamble_text

LATEXMACS = r"""
\newcommand{\too}[1]{{\xrightarrow{#1}}}
\DeclareMathOperator{\Aut}{Aut}
%\newcommand{\exp}[1]{\oldexp\qty{#1}}
\newcommand{\RM}[1]{%
  \MakeUppercase{\romannumeral #1}%
}
\renewcommand{\too}[0]{\longrightarrow}
\def\falling#1#2{ \qty{#1}_{ (#2) }}
"""

PREAMBLE_COMMON = r"""
\newcommand{\one}[0]{\mathbbm{1}}
\newcommand{\qty}[1]{\left( {#1} \right)}
\input{latexmacs}
"""

PREAMBLE = r"""
\input{preamble_common}
\newcommand{\divides}{\bigm|}
"""


def fixture(tmp_path: Path) -> Path:
    (tmp_path / "latexmacs.tex").write_text(LATEXMACS)
    (tmp_path / "preamble_common.tex").write_text(PREAMBLE_COMMON)
    (tmp_path / "preamble.tex").write_text(PREAMBLE)
    return tmp_path / "preamble.tex"


def test_the_preamble_is_read_as_latex_reads_it(tmp_path: Path) -> None:
    defined = definitions(preamble_text(fixture(tmp_path)))

    # `\renewcommand` is a definition and it comes last, so it is the one that
    # survives -- with no argument, which is how all 57 corpus sites write it.
    assert defined["too"] == r"\longrightarrow"
    # Reached only by following `\input` from the entry file, twice over.
    assert defined["qty"] == r"\left( {#1} \right)"
    assert defined["one"] == r"\mathbbm{1}"
    # A declared operator is a definition, and this is what it means.
    assert defined["Aut"] == r"\operatorname{Aut}"
    # A body that runs past its line, held together by the `%` line joiners.
    assert defined["RM"] == "\n  \\MakeUppercase{\\romannumeral #1}\n"
    # Commented out upstream: taking it would define `\exp` as `\oldexp`, which
    # nothing defines, over the top of the `\exp` MathJax already has.
    assert "exp" not in defined
    assert defined["divides"] == r"\bigm|"
    # `\def` defines too. The preamble writes three macros that way and the
    # corpus uses two of them, so reading only `\newcommand` left them undefined
    # and MathJax printed `\falling{2n}{n}` as its own source.
    assert defined["falling"] == r" \qty{#1}_{ (#2) }"
