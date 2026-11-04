#!/usr/bin/env python3
"""Check the control words in named card files against the known macro set.

The full `qualc check` renders every card through pandoc, which takes minutes.
Almost all of that cost is unrelated to a prose edit: what a per-card edit can
break, and `qualc.authoring check` cannot see, is an undefined or glued control
word (the `\\mapstov_1` class of defect, and `\\q` for an undefined `\\q`).

This script extracts every `\\word` from the given files and reports the ones that
are neither in `vocabularies/macros.json` nor in the MathJax command set that
`qualc` itself uses. It is a fast pre-check, not a replacement for the full gate.

It scans the same text the reader sees: the body read through
`qualc.tex.checkable_tex` (`\\dfn{term}` is rewritten out, for it is the one
supported prose command; code spans are not TeX; tikzcd environments are
compiled to SVG rather than rendered by MathJax), together with the rendered
metadata -- `title`, `slogan`, `prompts`, which `model.typeset_dashes` documents
as Markdown and passes to the page with its `$...$` spans intact. Non-rendered
metadata such as audit notes is never scanned, and the front matter is read
through the YAML loader, so escapes decode before the scan. Without that pass
the checker rejected every card carrying a defined term or a diagram, while
letting an undefined word in a title through.

    python3 tools/check_macros.py corpus/collections/.../CARD.md
    python3 tools/check_macros.py $(git diff --name-only HEAD | grep '\\.md$')
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

from qualc.model import split_front_matter
from qualc.tex import checkable_tex, mathjax_commands

# Metadata the site renders on the page. `model.typeset_dashes` documents that
# titles and prompts are written in Markdown and preserves their `$...$` spans,
# and the slogan badge goes through the same function, so mathematics in these
# three fields reaches the reader and an undefined macro there is red source.
# Every other front-matter field -- audit notes, ids, classifications,
# provenance -- never reaches a reader.
RENDERED_FIELDS = ("title", "slogan", "prompts")

CONTROL_WORD = re.compile(r"(?<!\\)\\([A-Za-z]+)")


def known_words(root: Path) -> frozenset[str]:
    preamble = root / "vocabularies" / "macros.json"
    macros = json.loads(preamble.read_text(encoding="utf-8")) if preamble.exists() else {}
    names = {name.removeprefix("\\") for name in macros}
    names |= set(mathjax_commands())
    return frozenset(names)


def rendered_metadata(meta: dict) -> list[str]:
    """The rendered fields' values, read the way the site reads them.

    The front matter is parsed with the pipeline's own YAML loader, so escapes
    decode before the scan: `"Rouch\xE9"` is `Rouch\u00e9` by the time it is
    checked, not a control word.
    """
    rendered: list[str] = []
    for field in RENDERED_FIELDS:
        value = meta.get(field)
        if isinstance(value, str):
            rendered.append(value)
        elif isinstance(value, list):
            rendered.extend(item for item in value if isinstance(item, str))
    return rendered


def unknown_control_words(markdown: str, known: frozenset[str]) -> list[str]:
    r"""The undefined or glued control words in one card's authored markdown.

    The body is scanned together with the rendered metadata (`title`, `slogan`,
    `prompts`), which reaches the reader as page text with its `$...$` spans
    preserved, so an undefined macro in a title is as much red source as one
    in the body. Non-rendered metadata is not scanned: an audit note's `X\C`
    is prose about mathematics, never mathematics, and YAML escapes decode
    before the scan. A card whose front matter does not parse is scanned
    whole, so the failure mode is a false rejection, never a missed defect.
    """
    try:
        meta, body = split_front_matter(markdown, Path("card"))
    except (TypeError, ValueError, yaml.YAMLError):
        meta, body = {}, markdown
    scannable = checkable_tex("\n\n".join([body, *rendered_metadata(meta)]))
    return sorted({word for word in CONTROL_WORD.findall(scannable) if word not in known})


def main(argv: list[str]) -> int:
    root = Path(__file__).resolve().parent.parent
    known = known_words(root)
    failed = False
    for argument in argv:
        path = Path(argument)
        text = path.read_text(encoding="utf-8")
        unknown = unknown_control_words(text, known)
        if unknown:
            failed = True
            print(f"{path}: undefined control word(s): {', '.join('\\' + w for w in unknown)}")
        else:
            print(f"{path}: OK")
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1:]))
