#!/usr/bin/env python3
"""Repair ledger span boundaries that cut through a fenced div.

A routing agent occasionally places a boundary one or two lines off: the card
span starts just after the `:::{.problem}` that opens it, or stops just before
the `:::` that closes its solution. The classification is right and only the
edges are wrong, so re-running the agent is the expensive way to fix it.

Moving an edge is not a local edit. Spans tile the file exactly, so every line
this takes into a card has to come out of its neighbour, and a neighbour that
gives up all its lines has to go. That bookkeeping is what this does.

Two shapes are repaired, both of which `route_audit` reports as SPLIT_DIV:

  span opens unbalanced   the div opened before the span did -- pull `start`
                          back to the opener
  span closes unbalanced  the div closes after the span did -- push `end`
                          forward to the closer

Also fixes spans that run past the end of the file, and single-line gaps left
between two spans.

    uv run python tools/route_repair.py <ledger-dir> [--write]

Without `--write` it reports what it would change and touches nothing.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

FENCE = ":::"


def opens(line: str) -> bool:
    """A fence that opens a div: `:::{.problem}` or `::: {.solution}`."""
    s = line.strip()
    return s.startswith(FENCE) and "{" in s


def closes(line: str) -> bool:
    """A bare `:::`, which closes whatever is open."""
    s = line.strip()
    return s.startswith(FENCE) and "{" not in s


def is_filler(line: str) -> str | bool:
    """Blank lines, headings and block anchors -- never prose or mathematics."""
    s = line.strip()
    return not s or s.startswith("#") or (s.startswith("^") and len(s) < 12)


def balance(lines: list[str], a: int, b: int) -> tuple[int, int]:
    """(unmatched openers, unmatched closers) over the 1-indexed range [a, b]."""
    op = cl = 0
    for line in lines[a - 1 : b]:
        if opens(line):
            op += 1
        elif closes(line):
            if op:
                op -= 1
            else:
                cl += 1
    return op, cl


def repair(spans: list[dict], lines: list[str]) -> tuple[list[dict], list[str]]:
    n = len(lines)
    notes: list[str] = []

    # A span that claims lines the file does not have. Clamp before anything
    # else looks at the boundaries.
    for s in spans:
        if s["end_line"] > n:
            notes.append(f"clamped end {s['end_line']} -> {n} (file is {n} lines)")
            s["end_line"] = n

    for i, s in enumerate(spans):
        if s.get("destination") != "card":
            continue
        op, cl = balance(lines, s["start_line"], s["end_line"])

        # Unmatched closer: the opening fence should sit just above the span,
        # separated at most by blank lines and the section heading.
        #
        # The walk back must not cross prose. In `050 Group Theory General.md`
        # the nearest opener above the span is the *previous problem's*
        # `:::{.solution}`, 35 lines up, because the real cause is a stray `:::`
        # inside this span that closes nothing. Pulling back to that opener
        # would silently swallow the previous problem's whole solution. An
        # unmatched closer with no opener in the filler above it is a defect in
        # the source, not a misplaced edge, and is left for a human.
        while cl and i > 0:
            prev = spans[i - 1]
            j = s["start_line"] - 1
            while j >= prev["start_line"] and not opens(lines[j - 1]) and is_filler(lines[j - 1]):
                j -= 1
            if j < prev["start_line"] or not opens(lines[j - 1]):
                notes.append(f"UNFIXABLE: span {s['start_line']}-{s['end_line']} has an unmatched closer and no opener in the filler above it; the source is wrong")
                break
            notes.append(f"start {s['start_line']} -> {j} (pulled back to its opener)")
            s["start_line"] = j
            prev["end_line"] = j - 1
            op, cl = balance(lines, s["start_line"], s["end_line"])

        # Unmatched opener: the closing fence sits below the span.
        while op and i + 1 < len(spans):
            nxt = spans[i + 1]
            j = s["end_line"] + 1
            while j <= nxt["end_line"] and not closes(lines[j - 1]):
                j += 1
            if j > nxt["end_line"]:
                break
            notes.append(f"end {s['end_line']} -> {j} (pushed out to its closer)")
            s["end_line"] = j
            nxt["start_line"] = j + 1
            op, cl = balance(lines, s["start_line"], s["end_line"])

    # A neighbour that gave up all of its lines is no longer a span.
    kept = [s for s in spans if s["start_line"] <= s["end_line"]]
    if len(kept) != len(spans):
        notes.append(f"dropped {len(spans) - len(kept)} span(s) emptied by the above")

    # Close single-line gaps by extending the span above them.
    for a, b in zip(kept, kept[1:]):
        if b["start_line"] > a["end_line"] + 1:
            notes.append(f"gap {a['end_line'] + 1}-{b['start_line'] - 1} folded into the span above")
            a["end_line"] = b["start_line"] - 1

    return kept, notes


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    write = "--write" in argv
    ledgers = Path([a for a in argv if not a.startswith("--")][0])

    changed = 0
    for led in sorted(ledgers.glob("*.json")):
        src = Path(led.with_suffix(".source").read_text().strip())
        lines = src.read_text(errors="replace").splitlines()
        spans = json.loads(led.read_text())
        fixed, notes = repair([dict(s) for s in spans], lines)
        if not notes:
            continue
        changed += 1
        print(f"\n{src.name}")
        for note in notes:
            print(f"    {note}")
        if write:
            led.write_text(json.dumps(fixed, indent=1))

    print(f"\n{changed} ledger(s) {'repaired' if write else 'would be repaired'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
