#!/usr/bin/env python3
"""Remove the author's personal study-tracking pages from a materialised wiki.

`route_apply` regenerates the wiki from source every run, and the source carried
the author's private study dashboards. Those are personal tracking, not the
public study guide, so this strips them back out. Idempotent: safe to re-run
after every materialisation.

Three pages are pure personal tracking and are deleted:

  qual_progress.md            a chart of the author's own completed/to-work
                              counts, timestamped across his exam prep.
  000_My Active Problems.md   a dashboard whose only content was an Obsidian
                              query for problems he had tagged "to work".
  999_Typsetting_Progress.md  a table of which sittings he had personally
                              typeset and imported; the sittings themselves are
                              now modelled as SRC-* source cards.

Two pages mix personal tracking with real reference material -- links to the
official UGA qual PDFs and a human-readable map of which problem appeared at
which sitting -- so those are trimmed, not deleted: the query blocks, the
`[x]`/`[ ]` completion checkboxes, and the "(stuck)"/"(unsure)" notes go; the
PDF links, problem maps, and course material stay.

    uv run python tools/depersonalize_wiki.py <wiki-dir>
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DELETE = ["qual_progress.md", "000_My Active Problems.md", "999_Typsetting_Progress.md"]

TRIM = {
    "30_Complex_Analysis/Complex Qual Progress.md":
        "> Index of UGA Complex Analysis qual sittings, with links to the official exam "
        "PDFs and to the problems in this wiki. (Structured occurrence data lives in the "
        "`O-*` / `SRC-*` cards.)\n\n",
    "20_Real_Analysis/Real Analysis Qual Progress.md":
        "> UGA Real Analysis qual review material and an index of sittings, with links to "
        "official exam PDFs and to the problems in this wiki.\n\n",
}


def trim(text: str) -> str:
    text = re.sub(r"```query.*?```\n?", "", text, flags=re.S)     # Obsidian query blocks
    text = re.sub(r"^See #\S+.*$\n?", "", text, flags=re.M)       # personal tag-reference line
    text = re.sub(r"^(\s*)-\s*\[[ xX]\]\s*", r"\1- ", text, flags=re.M)  # checkboxes -> bullets
    text = re.sub(r"\s*\((stuck|unsure|unsure\?)\)", "", text, flags=re.I)
    text = re.sub(r"\n{3,}", "\n\n", text).lstrip("\n")
    return text


def drop_empty_headings(text: str) -> str:
    lines = text.splitlines()
    keep = []
    for i, line in enumerate(lines):
        if re.match(r"^#+\s+\S", line) and "Exams by Year" not in line and "Review Material" not in line:
            has = False
            for nxt in lines[i + 1:]:
                if re.match(r"^#+\s", nxt):
                    break
                if nxt.strip() and not nxt.strip().startswith(">"):
                    has = True
                    break
            if not has:
                continue
        keep.append(line)
    return "\n".join(keep).replace("\n\n\n", "\n\n") + "\n"


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    wiki = Path(argv[0])
    n_del = n_trim = 0
    for name in DELETE:
        p = wiki / name
        if p.exists():
            p.unlink()
            n_del += 1
    for rel, intro in TRIM.items():
        p = wiki / rel
        if p.exists():
            p.write_text(intro + drop_empty_headings(trim(p.read_text())))
            n_trim += 1
    # index.md: drop the now-dead status-query blocks
    idx = wiki / "index.md"
    if idx.exists():
        idx.write_text(re.sub(r"```query\s*\n\s*tag:(work|completed|problems|solutions)\s*\n```\n?", "", idx.read_text()))
    print(f"depersonalised {wiki}: {n_del} pages deleted, {n_trim} trimmed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
