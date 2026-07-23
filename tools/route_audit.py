#!/usr/bin/env python3
"""Audit routing ledgers against their source files.

A routing ledger is one agent's decision about where every line of a source
file goes: `wiki` (stays as prose in the study guide) or `card` (factored out
into the problem bank). The routing is judgment. This is not -- everything here
is mechanical, and every check exists because it caught a real failure.

Failure modes observed, in the order they were found:

  TRUNCATED     the ledger starts partway into the file. Seen once, at 51%: a
                1598-line file returned a ledger beginning at line 819, valid
                JSON, perfectly contiguous, ending exactly at 1598. It fails
                one check and one only -- does the first span start at line 1.
  GAP           a line belongs to no span. Seen once, line 460 of a 734-line
                file, between spans ending 459 and starting 461.
  REASSEMBLY    the spans, concatenated in order, are not the source.
  LUMPED        far fewer spans than the file has fenced divs. A ledger reading
                "lines 4-1040 are definitions, all wiki" passes every byte-level
                check and resolves nothing.
  UNROUTED      a source file with no ledger at all. Reported against the source
                tree, not the ledger set, because a missing ledger produces no
                row to inspect: three files went unrouted in a 263-file run that
                reported 263/263 success, and nothing in a per-ledger audit could
                have seen it. Completeness is a property of the pair.
  REGRESSION    fewer bundles than a previous run of the same file produced.
                Invisible to every single-run check: a ledger that finds no
                problems is indistinguishable from a file that has none. Found
                34 dropped problems in one file on its first use, which is the
                argument for keeping a baseline at all.
  EMPTY         the ledger is an empty array. Every line unaccounted for, and
                it reads as success to anything that only checks for errors.
  MALFORMED     the ledger is not valid JSON. Usually an unescaped backslash in
                a LaTeX title. One file's failure, never the batch's.
  DETACHED      a solution/hint/concept/strategy emitted as its own card. The
                unit of the problem bank is a *problem bundle*: one card holding
                the statement (which may be multi-part), any hints, strategies,
                and concepts, links to other items, and every solution of it.

                A detached solution is one of two things and both need a human:
                a routing error, or a solution whose problem is missing from the
                source. The second is data loss -- a solution is of something,
                so if no statement precedes it the statement was dropped
                upstream. There is no such thing as a solution to nothing, and
                the schema must not grow a kind to hold one.
  DANGLING      `attaches_to` naming a span that is not a problem or exercise.
  BARREN        a file full of numbered problem headings that produced no cards.
                Not proof of error -- a link list of PDFs legitimately yields
                none -- but it is never uninteresting.

Nothing here decides whether a routing is *right*. It decides whether it is
answerable, and it shouts when it is not.

    uv run python tools/route_audit.py <ledger-dir> [--json]
                                        [--baseline prev-audit.json]
                                        [--sources qual-wiki-root]

Each ledger is `<name>.json`, an array of spans, and carries the source path in
a sibling `<name>.source` file or a `_source` key on its first span.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

FENCE = re.compile(r"^:{3,}\s*\{?\s*\.?[\w-]")
# Bundled into the problem card, never emitted alongside it. The bank's unit is
# a *problem bundle*: statement (possibly multi-part), hints, strategies,
# concepts, links to other items, and any number of solutions -- all one card.
# Multiple solutions are multiple divs in one body, which is what
# `site/filters/reveal.lua` already renders, each collapsed behind a summary.
BUNDLED = {"solution", "hint", "concept", "strategy"}
ANCHORS = {"problem", "exercise"}
LUMP_RATIO = 0.5  # spans/divs below this is a lump, not a resolution
# A problem card legitimately runs long: statement plus every worked solution.
# Only non-card spans are suspicious at this size -- a 555-line "definition" is
# a lump, a 217-line problem is a problem.
HUGE_SPAN = 150  # lines


def source_of(ledger: Path, spans: list[dict]) -> Path:
    sidecar = ledger.with_suffix(".source")
    if sidecar.exists():
        return Path(sidecar.read_text().strip())
    if spans and "_source" in spans[0]:
        return Path(spans[0]["_source"])
    raise SystemExit(f"{ledger}: no source recorded (need a .source sidecar or a _source key)")


def audit(ledger: Path) -> dict:
    # A malformed ledger must be one file's failure, not the run's. An agent
    # writing a LaTeX title without escaping the backslash produces invalid
    # JSON, and crashing here hides every other result in the batch.
    try:
        spans = json.loads(ledger.read_text())
    except json.JSONDecodeError as exc:
        return {"file": ledger.name, "lines": 0, "spans": 0, "cards": 0, "divs": 0,
                "fatal": [f"MALFORMED: {exc}"], "loud": [], "kinds": {}}
    src = source_of(ledger, spans)
    lines = src.read_text(errors="replace").splitlines(keepends=True)
    n = len(lines)
    fatal: list[str] = []
    loud: list[str] = []

    if not spans:
        return {"file": src.name, "lines": n, "spans": 0, "cards": 0, "divs": 0,
                "fatal": [f"EMPTY: ledger has no spans; {n} lines unaccounted for"],
                "loud": [], "kinds": {}}

    # --- did we get the whole ledger, and does it cover the whole file --------
    if spans[0]["start_line"] != 1:
        fatal.append(f"TRUNCATED: first span starts at line {spans[0]['start_line']}, not 1 — missing {spans[0]['start_line'] - 1} lines ({100 * (spans[0]['start_line'] - 1) // n}% of the file)")
    if spans[-1]["end_line"] != n:
        fatal.append(f"first/last: last span ends at {spans[-1]['end_line']}, file has {n} lines")
    for a, b in zip(spans, spans[1:]):
        if b["start_line"] != a["end_line"] + 1:
            fatal.append(f"GAP: span ends {a['end_line']}, next starts {b['start_line']}")
    for s in spans:
        if s["start_line"] > s["end_line"]:
            fatal.append(f"inverted span {s['start_line']}-{s['end_line']}")

    if not fatal:
        rebuilt = "".join("".join(lines[s["start_line"] - 1 : s["end_line"]]) for s in spans)
        if rebuilt != "".join(lines):
            fatal.append("REASSEMBLY: spans concatenated do not reproduce the source")

    # --- did it actually resolve anything ------------------------------------
    divs = sum(1 for line in lines if FENCE.match(line))
    if divs and len(spans) < divs * LUMP_RATIO:
        loud.append(f"LUMPED: {len(spans)} spans for {divs} fenced divs")
    prose = [s for s in spans if s.get("kind") not in ANCHORS]
    if prose:
        biggest = max(s["end_line"] - s["start_line"] + 1 for s in prose)
        if biggest > HUGE_SPAN:
            big = next(s for s in prose if s["end_line"] - s["start_line"] + 1 == biggest)
            loud.append(f"span of {biggest} lines at {big['start_line']}-{big['end_line']} ({big.get('kind')})")

    # --- are the cards reachable ---------------------------------------------
    starts = {s["start_line"]: s for s in spans}
    for s in spans:
        if s["destination"] != "card":
            continue
        if s.get("kind") in BUNDLED:
            loud.append(f"DETACHED: {s['kind']} at {s['start_line']}-{s['end_line']} emitted as its own card; it belongs inside the problem span")
            continue
        at = s.get("attaches_to")
        if at not in (None, "", "null"):
            if int(at) not in starts:
                loud.append(f"DANGLING: span {s['start_line']} attaches to {at}, not a span start")
            elif starts[int(at)].get("kind") not in ANCHORS:
                loud.append(f"DANGLING: span {s['start_line']} attaches to a {starts[int(at)].get('kind')!r}")

    # --- did a file of problems produce no problems --------------------------
    cards = [s for s in spans if s["destination"] == "card"]
    numbered = sum(1 for line in lines if re.match(r"^#{1,6}\s+(\d+|\w+\s+\d{4})", line))
    if not cards and numbered >= 3:
        loud.append(f"BARREN: {numbered} numbered/dated headings produced 0 cards")

    kinds = Counter((s["destination"], s.get("kind")) for s in spans)
    return {
        "file": src.name,
        "lines": n,
        "spans": len(spans),
        "cards": len(cards),
        "divs": divs,
        "fatal": fatal,
        "loud": loud,
        "kinds": {f"{d}/{k}": c for (d, k), c in kinds.most_common()},
    }


def line_count(path: Path) -> int:
    """The one definition of how long a file is.

    `wc -l` counts newlines, so it is short by one on any file whose last line
    lacks a trailing newline -- 27 of qual-wiki's 263 authored files. Feeding a
    routing agent a `wc -l` count and auditing it with this one makes every such
    file fail for a reason that is entirely ours. The batch launcher and the
    auditor must read the count from here.
    """
    return len(path.read_text(errors="replace").splitlines(keepends=True))


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    source_root: Path | None = None
    if "--sources" in argv:
        i = argv.index("--sources")
        source_root = Path(argv[i + 1])
        argv = argv[:i] + argv[i + 2 :]
    baseline: dict[str, int] = {}
    if "--baseline" in argv:
        i = argv.index("--baseline")
        baseline = {x["file"]: x["cards"] for x in json.loads(Path(argv[i + 1]).read_text())}
        argv = argv[:i] + argv[i + 2 :]
    if argv[0] == "--lines":
        for arg in argv[1:]:
            print(f"{line_count(Path(arg))}\t{arg}")
        return 0
    as_json = "--json" in argv
    root = Path([a for a in argv if not a.startswith("--")][0])
    reports = [audit(p) for p in sorted(root.glob("*.json"))]

    if as_json:
        print(json.dumps(reports, indent=2))
        return 1 if any(r["fatal"] for r in reports) else 0

    # A file that yielded bundles before and none now is a regression no
    # single-run check can see -- nothing in this ledger looks wrong.
    for r in reports:
        was = baseline.get(r["file"])
        if was is not None and r["cards"] < was:
            r["loud"].insert(0, f"REGRESSION: {was} bundles previously, {r['cards']} now")

    bad = 0
    for r in reports:
        mark = "FAIL" if r["fatal"] else ("warn" if r["loud"] else "  ok")
        print(f"{mark}  {r['file'][:44]:44s} {r['lines']:5d}L {r['spans']:4d}sp {r['cards']:4d}cards")
        for f in r["fatal"]:
            print(f"        !! {f}")
        for w in r["loud"]:
            print(f"         ? {w}")
        if r["fatal"]:
            bad += 1

    # Destination consistency is a cross-file property, so it is reported here
    # rather than per file: the same semantic role landing in two places is how
    # a corpus becomes unqueryable.
    roles: dict[str, Counter] = {}
    for r in reports:
        for key, count in r["kinds"].items():
            dest, kind = key.split("/", 1)
            roles.setdefault(kind, Counter())[dest] += count
    split = {k: v for k, v in roles.items() if len(v) > 1 and k in BUNDLED | ANCHORS}
    if split:
        print("\n ?  SPLIT DESTINATION — the same role routed two ways across this batch:")
        for kind, dests in sorted(split.items()):
            print(f"        {kind}: " + ", ".join(f"{d}={c}" for d, c in dests.most_common()))

    if source_root is not None:
        def authored(p: Path) -> bool:
            return "attachments" not in p.parts and "TexDocs" not in p.parts and not p.name.endswith("_stripped.md")

        want = {p for p in source_root.rglob("*.md") if authored(p)}
        have = {source_of(p, []) for p in sorted(root.glob("*.json")) if p.with_suffix(".source").exists()}
        missing = sorted(want - have)
        if missing:
            bad += len(missing)
            print(f"\n !! UNROUTED — {len(missing)} source files have no ledger:")
            for m in missing:
                print(f"        {m}")
        else:
            print(f"\n ok  completeness: all {len(want)} source files have a ledger")

    print(f"\n{len(reports)} ledgers, {bad} fatal, {sum(1 for r in reports if r['loud'] and not r['fatal'])} flagged")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
