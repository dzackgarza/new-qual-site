#!/usr/bin/env python3
"""Regenerate vocabularies/macros.json from the shared pandoc-config preamble.

Only the macros the corpus actually uses, plus whatever those expand into.
The result is committed, so a build never reaches outside this repository.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MACRO_SOURCE = Path("/home/dzack/gitclones/pandoc-config/archive/legacy-macros-2025-01-09")

MACRO_RE = re.compile(r"\\newcommand\*?\{?\\([A-Za-z]+)\}?(?:\[(\d)\])?(?:\[[^\]]*\])?\{(.*)\}\s*$")


def definitions() -> dict[str, tuple[str, int]]:
    defs: dict[str, tuple[str, int]] = {}
    for path in sorted(MACRO_SOURCE.glob("latexmacs*.tex")):
        for line in path.read_text().splitlines():
            m = MACRO_RE.match(line.strip())
            if m:
                defs[m.group(1)] = (m.group(3), int(m.group(2) or 0))
    return defs


def main() -> int:
    if not MACRO_SOURCE.exists():
        print(f"macro source not found: {MACRO_SOURCE}", file=sys.stderr)
        return 1
    defs = definitions()
    used = set()
    for path in (ROOT / "corpus").rglob("*.md"):
        used |= set(re.findall(r"\\([A-Za-z]+)", path.read_text()))

    frontier, keep = used & defs.keys(), {}
    while frontier:  # a macro may be defined in terms of another
        name = frontier.pop()
        body, arity = defs[name]
        keep[name] = [body, arity] if arity else body
        frontier |= {n for n in re.findall(r"\\([A-Za-z]+)", body) if n in defs and n not in keep}

    undefined = sorted(n for n in used if n not in defs and n not in keep)
    (ROOT / "vocabularies" / "macros.json").write_text(json.dumps(dict(sorted(keep.items())), indent=1) + "\n")
    print(f"{len(keep)} macros used by the corpus")
    if undefined:
        print(f"not defined in the preamble (assumed standard LaTeX): {' '.join(undefined)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
