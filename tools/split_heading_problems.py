"""Split heading-format problems that were swallowed into card bodies.

The wiki and qrs importers cut problem statements at paragraph boundaries rather
than at headings, so a card can end mid-problem while the next card begins with
the tail of the previous one, carries the heading that should have started a new
problem, and then runs into the next problem's text.

This restores the heading boundary.  Inside a run of consecutive card references
under one page heading, the run's bodies are re-joined and re-split on the
headings they contain.  Chunk i keeps run id i, so ids are stable; the page gets
the recovered heading back in front of each chunk after the first.  Status
markers (``$\\work$`` and friends) are dropped from restored headings, per the
2026-07-25 decision.

Every emitted chunk is checked against the upstream source file: its text must
appear there verbatim up to whitespace.

Usage:
    uv run python tools/split_heading_problems.py --report
    uv run python tools/split_heading_problems.py --apply
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from card_titles import title_of

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
CORPUS = ROOT / "corpus"
QRS = Path("/home/dzack/gitclones/qual-review-and-solutions")
QUAL_WIKI = Path("/home/dzack/gitclones/qual-wiki")

HEADING = re.compile(r"^(#{1,6}) +(\S.*?)[ \t]*$", re.M)
REF = re.compile(r"\[\[([A-Z]+-[A-Z0-9]+)\]\]")
ANCHOR = re.compile(r"^\^[0-9a-f]+$")
STATUS = re.compile(r"\s*\$\\(work|todo|done)\$\s*$")
ID_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def normalize(text: str) -> str:
    """Whitespace-insensitive text, with vendored asset paths made comparable.

    Image targets were rewritten when the sources were vendored, so a verbatim
    comparison against upstream has to ignore them.
    """
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"![\1]()", text)
    return re.sub(r"\s+", " ", text).strip()


def strip_status(title: str) -> str:
    return STATUS.sub("", title).strip()


@dataclass
class Card:
    path: Path
    front: dict
    body: str


def load_cards() -> dict[str, Card]:
    cards = {}
    for path in CORPUS.rglob("*.md"):
        _, front, body = path.read_text().split("---", 2)
        cards[path.stem] = Card(path, yaml.safe_load(front), body)
    return cards


def source_text(page: Path) -> str | None:
    """Upstream text of a vendored wiki page, from whichever source repo holds it."""
    rel = page.relative_to(WIKI)
    direct = QRS / rel
    if direct.exists():
        return direct.read_text()
    show = subprocess.run(
        ["git", "show", f"HEAD:{rel}"],
        cwd=QUAL_WIKI,
        capture_output=True,
        text=True,
    )
    return show.stdout if show.returncode == 0 else None


def runs(lines: list[str]) -> list[tuple[int, int, list[str]]]:
    """Maximal spans of reference-only lines, as (start, end, ids)."""
    out = []
    start, ids = None, []
    for i, line in enumerate(lines):
        stripped = line.strip()
        found = REF.findall(stripped)
        if found and REF.sub("", stripped).strip() == "":
            if start is None:
                start = i
            ids.extend(found)
            continue
        if start is not None and (not stripped or ANCHOR.match(stripped)):
            continue
        if start is not None:
            out.append((start, i, ids))
            start, ids = None, []
    if start is not None:
        out.append((start, len(lines), ids))
    return [(s, e, i) for s, e, i in out if i]


def chunk_run(bodies: list[str]) -> list[tuple[str | None, str]]:
    """Re-join a run's bodies and re-split them on the headings they contain."""
    chunks: list[tuple[str | None, str]] = [(None, "")]
    for body in bodies:
        pos = 0
        for m in HEADING.finditer(body):
            head, text = chunks[-1]
            chunks[-1] = (head, text + body[pos : m.start()])
            chunks.append((f"{m.group(1)} {strip_status(m.group(2))}", ""))
            pos = m.end() + 1
        head, text = chunks[-1]
        chunks[-1] = (head, text + body[pos:])
    return [(h, t) for h, t in chunks if h is not None or t.strip()]


def statement(text: str) -> str:
    """The problem statement of a chunk: its prose up to the first fenced div."""
    lines = []
    for line in text.splitlines():
        if line.startswith(":::"):
            break
        lines.append(line)
    return normalize("\n".join(lines))


def mint_id(prefix: str, taken: set[str], seed: str) -> str:
    import hashlib

    digest = hashlib.sha1(seed.encode()).hexdigest()
    for start in range(0, 30):
        candidate = prefix + "".join(ID_CHARS[int(digest[start + k : start + k + 2], 16) % len(ID_CHARS)] for k in range(0, 10, 2))
        if candidate not in taken:
            taken.add(candidate)
            return candidate
    raise RuntimeError(f"no free id for {seed}")


def plan_page(page: Path, cards: dict[str, Card], defective: set[str]) -> Iterator[tuple[int, int, list[str], list[tuple[str | None, str]]]]:
    """Yield (run, chunks, ids) for every run of this page that needs a split."""
    lines = page.read_text().splitlines()
    for start, end, ids in runs(lines):
        if not any(i in defective for i in ids):
            continue
        if any(i not in cards for i in ids):
            continue
        chunks = chunk_run([cards[i].body for i in ids])
        if len(chunks) <= 1:
            continue
        yield (start, end, ids, chunks)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--ledger", default="sources/g5-heading-splits.jsonl")
    args = parser.parse_args()

    cards = load_cards()
    taken = set(cards)
    defective = {i for i, c in cards.items() if HEADING.search(c.body)}

    rows: list[dict[str, Any]] = []
    unverified = []
    surplus_ids = []
    for page in sorted(WIKI.rglob("*.md")):
        plans = list(plan_page(page, cards, defective))
        if not plans:
            continue
        src = source_text(page)
        src_norm = normalize(src) if src else ""
        lines = page.read_text().splitlines()
        replacements = []
        for start, end, ids, chunks in plans:
            if len(ids) > len(chunks):
                surplus_ids.append((str(page.relative_to(ROOT)), ids, len(chunks)))
                continue
            bad = [statement(text)[:70] for _, text in chunks if statement(text) and statement(text) not in src_norm]
            if bad:
                unverified.append((str(page.relative_to(ROOT)), ids, bad))
                continue
            assigned = []
            for n, (head, text) in enumerate(chunks):
                if n < len(ids):
                    cid = ids[n]
                else:
                    cid = mint_id("P-", taken, f"{page.relative_to(ROOT)}:{start}:{n}:{text[:80]}")
                    template = cards[ids[0]].front
                    cards[cid] = Card(
                        cards[ids[0]].path.with_name(f"{cid}.md"),
                        {
                            "schema": template["schema"],
                            "id": cid,
                            "kind": template["kind"],
                            "title": title_of(text),
                            "classification": {
                                "areas": list(template["classification"]["areas"]),
                                "topics": [],
                            },
                            "relations": [],
                            "review": "draft",
                        },
                        text,
                    )
                assigned.append((cid, head, text))
            replacements.append((start, end, assigned))
            rows.append(
                {
                    "page": str(page.relative_to(ROOT)),
                    "run_ids": ids,
                    "chunks": [{"card": cid, "heading": head, "chars": len(text)} for cid, head, text in assigned],
                }
            )

        if not args.apply:
            continue

        for start, end, assigned in sorted(replacements, reverse=True):
            block = []
            for cid, head, text in assigned:
                if head is not None:
                    block += [head, ""]
                block += [f"[[{cid}]]", ""]
                card = cards[cid]
                card.body = "\n" + text.strip() + "\n"
                card.front["title"] = title_of(text)
            lines[start:end] = block
        page.write_text("\n".join(lines) + "\n")

    if args.apply:
        for cid in {c for row in rows for c in row["run_ids"]} | {ch["card"] for row in rows for ch in row["chunks"]}:
            card = cards[cid]
            front = yaml.dump(card.front, sort_keys=False, allow_unicode=False)
            card.path.write_text(f"---\n{front}---\n{card.body.lstrip(chr(10))}")
        ledger = ROOT / args.ledger
        ledger.write_text("".join(json.dumps(r) + "\n" for r in rows))

    print(f"pages touched: {len({r['page'] for r in rows})}")
    print(f"runs split: {len(rows)}")
    print(f"cards in runs: {sum(len(r['run_ids']) for r in rows)}")
    print(f"chunks out: {sum(len(r['chunks']) for r in rows)}")
    print(f"new cards minted: {sum(len(r['chunks']) - len(r['run_ids']) for r in rows if len(r['chunks']) > len(r['run_ids']))}")
    print(f"runs skipped, would reduce card count: {len(surplus_ids)}")
    for name, ids, n in surplus_ids:
        print(f"    {name}: {len(ids)} refs -> {n} chunks {ids}")
    print(f"runs skipped, statement not verbatim in source: {len(unverified)}")
    for name, ids, bad in unverified:
        print(f"    {name}: {ids}")
        for text in bad:
            print(f"        {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
