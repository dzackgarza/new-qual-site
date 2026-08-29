#!/usr/bin/env python3
r"""Regenerate vocabularies/macros.json from the author's pandoc preamble.

Only the macros the authored text actually uses, plus whatever those expand into.
`_macros.html` is included in every document the build emits, so the used set is read
from `wiki/` as well as `corpus/`; narrowing it to `corpus/` left every macro a wiki page
uses undefined, and an undefined macro renders as red literal text without raising a
MathJax error.

The result is committed, so a build never reaches outside this repository.

`PREAMBLE` is the file the author's own pipeline loads, and it is read the way
LaTeX reads it, because every shortcut here has already cost the site a macro:

  * `\input` is expanded in place, so `preamble_common.tex`, `latexmacs.tex`
    and the rest are all seen, and in the order LaTeX sees them. Reading only
    `latexmacs*.tex` missed `\qty` and `\one`.
  * a later definition replaces an earlier one, `\renewcommand` included.
    `latexmacs.tex` defines `\too` with one argument and then renews it with
    none; keeping the first put `\xrightarrow` under a `\too` that the corpus
    writes 57 times without an argument.
  * `\DeclareMathOperator{\Aut}{Aut}` is a definition, and reads as
    `\operatorname{Aut}`. 63 of the preamble's operators are declared that way.
  * a `%` starts a comment, and nothing after it is a definition. `\exp` and
    `\perp` are only ever defined in commented-out lines, in terms of `\oldexp`
    and `\oldperp` that nothing defines; taking those definitions broke 82
    corpus sites that mean MathJax's own `\exp` and `\perp`.
  * the preamble targets LaTeX, and MathJax is the smaller language. A body may
    use a primitive MathJax has no equivalent for, and MathJax fails the whole
    expression rather than the primitive. `TEX_ONLY` drops those; the preamble
    stays correct for the LaTeX pipeline that also reads it.

Keys carry the leading backslash, which is the name `qualc build` wants:
`mathjax_header` rejects anything else. Arity is not written; it is read back
off the `#1..#9` the body uses.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PREAMBLE = Path("/home/dzack/Dropbox/pandoc/custom/preamble.tex")

COMMENT_RE = re.compile(r"(?<!\\)%.*")
INPUT_RE = re.compile(r"\\input\{([^}]+)\}")
# The optional groups are LaTeX's argument count and default first argument.
COMMAND_RE = re.compile(r"\\(?:re|provide)?newcommand\*?\s*\{?\\([A-Za-z]+)\}?\s*(?:\[\d+\])?(?:\[[^\]]*\])?\s*\{")
OPERATOR_RE = re.compile(r"\\DeclareMathOperator\*?\s*\{?\\([A-Za-z]+)\}?\s*\{")
# `\def` is a definition too. The preamble writes three macros with it, and the
# corpus uses two of them, so `\rising{n}{k}` and `\falling{2n}{n}` reached the
# page as red source. The parameter markers sit between the name and the body.
DEF_RE = re.compile(r"\\def\s*\\([A-Za-z]+)\s*(?:#[1-9])*\s*\{")
# A card's front-matter title is stored cut short at an ellipsis, and the cut
# lands mid-name often enough to matter: `$\sq…` is `\sqrt` and `\I…` is `\Im`.
# The committed vocabulary carried `\sq` and `\I` because of it. `[A-Za-z]` is
# in the lookahead so a failed test cannot be satisfied by a shorter name.
MACRO_USE_RE = re.compile(r"\\([A-Za-z]+)(?![A-Za-z\u2026])")
# Paragraph-mode glue. MathJax has no `\hfill`, and `\qed` is written with one.
TEX_ONLY = re.compile(r"\\hfill\b")

# Preamble definitions MathJax cannot render, under the definition to use
# instead. A body reaching MathJax with a construct it does not implement
# renders as a red error box, not as a fallback, so the substitution has to
# happen here rather than at the page.
#
# `\notdivides` is built from `\ooalign`, `\hidewidth` and `\cr`, which are
# plain-TeX alignment primitives MathJax has no equivalent for. `\nmid` is the
# same relation from the standard tables, which MathJax does implement.
# `\Lightning` is a marvosym symbol, so `\contradiction` reached the page as
# red literal text. U+21AF DOWNWARDS ZIGZAG ARROW is the same sign.
#
# `\one` and `\indic` are built on `\mathbbm`, declared from `bbm.sty`; the
# blackboard-bold digit is U+1D7D9. `\mapsfrom` reflects `\mapsto` with
# `graphicx`, and draws U+21A4. `\varinjlim` and `\varprojlim` are renewed over
# the amsmath originals in terms of `\varlim@` and `\nmlimits@`, which are
# amsmath's own internals: MathJax already provides both, so its versions
# stand. `\fps` is written with stmaryrd's `\llbracket` and `\rrbracket`, which
# are U+27E6 and U+27E7. `\envlist` is vertical glue with no mathematics in it.
UNRENDERABLE = {
    "notdivides": "\\mathrel{\\nmid}",
    "contradiction": "\\mathord{\\unicode{x21AF}}",
    "one": "{\\unicode{x1D7D9}}",
    "indic": "{\\unicode{x1D7D9}}\\left[#1\\right]",
    "mapsfrom": "\\mathrel{\\unicode{x21A4}}",
    "fps": "{\\unicode{x27E6} #1 \\unicode{x27E7}}",
    "envlist": "",
}

# Preamble macros that renew an amsmath original in terms of amsmath's own
# internals. MathJax carries the originals, so its definitions are left to
# stand: naming them here would define each macro as itself.
NATIVE = frozenset({"varinjlim", "varprojlim"})

USED_IN = ("corpus", "wiki")


def preamble_text(path: Path, seen: frozenset[Path] = frozenset()) -> str:
    """The preamble with its comments dropped and its `\\input` files spliced in."""
    text = "\n".join(COMMENT_RE.sub("", line) for line in path.read_text().splitlines())
    out, cut = [], 0
    for match in INPUT_RE.finditer(text):
        name = match.group(1)
        child = path.parent / (name if name.endswith(".tex") else name + ".tex")
        out.append(text[cut : match.start()])
        if child.is_file() and child not in seen:
            out.append(preamble_text(child, seen | {path}))
        cut = match.end()
    out.append(text[cut:])
    return "".join(out)


def group_at(text: str, start: int) -> str:
    """The body of the brace group whose opening brace sits just before `start`."""
    depth, at = 1, start
    while at < len(text) and depth:
        if text[at] == "\\":
            at += 2
            continue
        depth += (text[at] == "{") - (text[at] == "}")
        at += 1
    return text[start : at - 1]


def definitions(text: str) -> dict[str, str]:
    """Every macro the preamble defines, under the definition that survives."""
    found: list[tuple[int, str, str]] = []
    for match in COMMAND_RE.finditer(text):
        found.append((match.start(), match.group(1), group_at(text, match.end())))
    for match in OPERATOR_RE.finditer(text):
        found.append((match.start(), match.group(1), f"\\operatorname{{{group_at(text, match.end())}}}"))
    for match in DEF_RE.finditer(text):
        found.append((match.start(), match.group(1), group_at(text, match.end())))
    return {name: body for _, name, body in sorted(found)}


def main() -> int:
    if not PREAMBLE.is_file():
        print(f"preamble not found: {PREAMBLE}", file=sys.stderr)
        return 1
    defined = definitions(preamble_text(PREAMBLE))

    used: set[str] = set()
    for where in USED_IN:
        for path in (ROOT / where).rglob("*.md"):
            used |= set(MACRO_USE_RE.findall(path.read_text()))

    frontier, keep = used & defined.keys(), {}
    while frontier:  # a macro may be defined in terms of another
        name = frontier.pop()
        keep[name] = defined[name]
        frontier |= {n for n in MACRO_USE_RE.findall(defined[name]) if n in defined and n not in keep}

    macros = {"\\" + name: UNRENDERABLE[name] if name in UNRENDERABLE else TEX_ONLY.sub("", body).strip() for name, body in sorted(keep.items()) if name not in NATIVE}
    (ROOT / "vocabularies" / "macros.json").write_text(json.dumps(macros, indent=2, ensure_ascii=False) + "\n")
    print(f"{len(macros)} macros used by {' and '.join(USED_IN)}, from {PREAMBLE}")
    undefined = sorted(n for n in used if n not in defined)
    if undefined:
        print(f"not defined in the preamble (assumed standard LaTeX): {' '.join(undefined)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
