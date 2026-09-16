"""Authored TeX: the one supported prose command, and what the site cannot show.

The corpus dialect reads a TeX command written in prose as raw TeX, and Pandoc's
HTML writer drops raw TeX it cannot typeset as mathematics. `\\dfn{term}` (DEF-26)
is the one prose command the corpus is written with; it is rewritten before the
reader sees it into a bracketed span of class `dfn`, which the HTML writer emits
as a `<dfn>` element, with the term's own mathematics still read as mathematics.

Everything else that would reach a reader as nothing is a check failure:

* raw TeX the HTML writer does not render (`RAW_TEX_DROPPED`). Which raw TeX
  Pandoc renders -- math environments such as `\\begin{align*}` and `\\ref` go to
  MathJax, anything else is dropped -- is Pandoc's decision, so the writer is
  asked rather than its rule copied here.
* a TeX command in mathematics that neither the author's preamble
  (`vocabularies/macros.json`) nor the MathJax build the site loads defines
  (`UNDEFINED_MACRO`, issue #87). MathJax renders one as red source.

`mathjax_commands.json` is the command set of that MathJax build (3.2.2,
`tex-chtml-full`: the `require` package and `AllPackages`, including the text-mode
macros); `just mathjax-commands` regenerates it from MathJax's own parse maps.
"""

from __future__ import annotations

import json
import re
from collections.abc import Iterator
from pathlib import Path

from .diagnostics import Diagnostic, DiagnosticCode
from .pandoc_batch import PandocFailure, PandocServer

DFN_COMMAND = re.compile(r"\\dfn\{")
DFN_CLASSES = "{.dfn .qual-dfn}"
FENCED_CODE = re.compile(r"(?ms)^[ \t]*(`{3,}|~{3,}).*?^[ \t]*\1[`~]*[ \t]*$")
INLINE_CODE = re.compile(r"(`+)(?:(?!\1).)+?\1", re.S)
# A control word, or a control symbol such as the row separator `\\\\`, which is consumed
# whole so that `\\\\c` is a row break before `c` and not a command `\\c`.
TEX_CONTROL = re.compile(r"\\(?:([A-Za-z]+)|.)", re.S)
RAW_TEX_FORMATS = ("tex", "latex")
# Compiled to SVG by the emitter (`emit._compile_tikzcd`), not by the HTML writer.
TIKZCD_START = "\\begin{tikzcd}"
NOT_RENDERED = "Not rendering "

MATHJAX_COMMANDS = Path(__file__).with_name("mathjax_commands.json")


def _code_spans(markdown: str) -> list[tuple[int, int]]:
    spans = [match.span() for match in FENCED_CODE.finditer(markdown)]
    spans.extend(match.span() for match in INLINE_CODE.finditer(markdown) if not any(start <= match.start() < end for start, end in spans))
    return spans


def _group_end(text: str, start: int) -> int | None:
    """Index just past the brace group opening at `start`, or None if unbalanced."""
    depth = 0
    index = start
    while index < len(text):
        char = text[index]
        if char == "\\":
            index += 2
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index + 1
        index += 1
    return None


def mark_definienda(markdown: str) -> str:
    """Rewrite each `\\dfn{term}` outside code as `[term]{.dfn .qual-dfn}`.

    An unbalanced `\\dfn{` is left as written, so the reader keeps it as raw TeX
    and the check reports it as dropped.
    """
    code = _code_spans(markdown)
    out: list[str] = []
    cursor = 0
    for match in DFN_COMMAND.finditer(markdown):
        if match.start() < cursor or any(start <= match.start() < end for start, end in code):
            continue
        end = _group_end(markdown, match.end() - 1)
        if end is None:
            continue
        out.append(markdown[cursor : match.start()])
        out.append("[" + mark_definienda(markdown[match.end() : end - 1]) + "]" + DFN_CLASSES)
        cursor = end
    out.append(markdown[cursor:])
    return "".join(out)


def mathjax_commands() -> frozenset[str]:
    names = json.loads(MATHJAX_COMMANDS.read_text())
    if not isinstance(names, list) or not all(isinstance(name, str) for name in names):
        raise TypeError(f"{MATHJAX_COMMANDS}: expected a list of command names")
    return frozenset(names)


def _tex_nodes(node: object) -> Iterator[tuple[str, str, str]]:
    """Yield `(element type, format or math kind, text)` for raw TeX and math, in order."""
    if isinstance(node, dict):
        kind = node.get("t")
        content = node.get("c")
        if kind in ("RawInline", "RawBlock") and isinstance(content, list) and content[0] in RAW_TEX_FORMATS:
            yield kind, content[0], content[1]
            return
        if kind == "Math" and isinstance(content, list):
            yield kind, content[0]["t"], content[1]
            return
        for value in node.values():
            yield from _tex_nodes(value)
    elif isinstance(node, list):
        for value in node:
            yield from _tex_nodes(value)


def _probe(kind: str, fmt: str, text: str, api: object) -> str:
    element = {"t": kind, "c": [fmt, text]}
    blocks = [element] if kind == "RawBlock" else [{"t": "Plain", "c": [element]}]
    return json.dumps({"pandoc-api-version": api, "meta": {}, "blocks": blocks})


def unrenderable_tex(
    pandoc: PandocServer,
    documents: list[tuple[str, str]],
    preamble: dict[str, str],
) -> list[Diagnostic]:
    """Report raw TeX the HTML writer drops and macros nothing defines.

    `documents` pairs where a document came from with its Pandoc JSON, and
    `preamble` is `vocabularies/macros.json`. A preamble macro that expands to
    nothing (`\\envlist`, vertical glue) loses nothing when the writer drops it.
    """
    known = frozenset(name.removeprefix("\\") for name in preamble) | mathjax_commands()
    invisible = frozenset(name for name, body in preamble.items() if not body.strip())
    found: list[tuple[str, list[tuple[str, str, str]]]] = []
    raw: set[tuple[str, str, str]] = set()
    api: object = None
    for where, ast in documents:
        document = json.loads(ast)
        api = document["pandoc-api-version"]
        nodes = list(_tex_nodes(document["blocks"]))
        found.append((where, nodes))
        raw.update(node for node in nodes if node[0] != "Math" and TIKZCD_START not in node[2] and node[2].strip() not in invisible)

    ordered = sorted(raw)
    dropped: set[tuple[str, str, str]] = set()
    if ordered:
        for node, result in zip(ordered, pandoc.write_html([_probe(*node, api) for node in ordered]), strict=True):
            if isinstance(result, PandocFailure):
                raise ValueError(f"pandoc could not write raw TeX {node[2]!r}: {result.error}")
            if any(message.message.startswith(NOT_RENDERED) for message in result.messages):
                dropped.add(node)

    errors: list[Diagnostic] = []
    for where, nodes in found:
        for node in nodes:
            kind, _, text = node
            if node in dropped:
                errors.append(Diagnostic(DiagnosticCode.RAW_TEX_DROPPED, where, f"raw TeX the page cannot show: {text[:80]!r}"))
                continue
            if TIKZCD_START in text:
                continue
            undefined = sorted({name for name in TEX_CONTROL.findall(text) if name and name not in known})
            if undefined:
                names = " ".join("\\" + name for name in undefined)
                errors.append(Diagnostic(DiagnosticCode.UNDEFINED_MACRO, where, f"not defined by the preamble or MathJax: {names} in {text[:80]!r}"))
    return errors
