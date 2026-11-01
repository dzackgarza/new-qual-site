#!/usr/bin/env python3
"""Check the control words in named card files against the known macro set.

The full `qualc check` renders every card through pandoc, which takes minutes.
Almost all of that cost is unrelated to a prose edit: what a per-card edit can
break, and `qualc.authoring check` cannot see, is an undefined or glued control
word (the `\\mapstov_1` class of defect, and `\\q` for an undefined `\\q`).

This script extracts every `\\word` from the given files and reports the ones that
are neither in `vocabularies/macros.json` nor in the MathJax command set that
`qualc` itself uses. It is a fast pre-check, not a replacement for the full gate.

    python3 tools/check_macros.py corpus/collections/.../CARD.md
    python3 tools/check_macros.py $(git diff --name-only HEAD | grep '\\.md$')
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

CONTROL_WORD = re.compile(r"\\([A-Za-z]+)")


def known_words(root: Path) -> frozenset[str]:
    sys.path.insert(0, str(root / "tools"))
    from qualc.tex import mathjax_commands

    preamble = root / "vocabularies" / "macros.json"
    macros = json.loads(preamble.read_text(encoding="utf-8")) if preamble.exists() else {}
    names = {name.removeprefix("\\") for name in macros}
    names |= set(mathjax_commands())
    return frozenset(names)


def main(argv: list[str]) -> int:
    root = Path(__file__).resolve().parent.parent
    known = known_words(root)
    failed = False
    for argument in argv:
        path = Path(argument)
        text = path.read_text(encoding="utf-8")
        unknown = sorted({word for word in CONTROL_WORD.findall(text) if word not in known})
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
