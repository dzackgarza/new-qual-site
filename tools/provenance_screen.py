"""Screen problem cards for a statement of where their argument comes from.

What it checks
--------------
For every card whose frontmatter says ``kind: problem`` and that has a
``::: {.solution}`` block, it looks at the rendered text from the solution
fence to the end of the file — the solution and every remark — and asks for
one of three signals:

``remark``
    a ``::: {.remark title="Published solution"}`` block, which by the corpus's
    own convention carries the set and its printed page;
``source``
    the name of a retained solution set or its author, in a list below;
``own``
    an explicit statement that the argument is the card's own, or that no
    published solution was located.

A card with none of the three says nothing about where its proof comes from.
The audit events in the frontmatter are not read: they are the card's
bookkeeping, not something a reader of the page sees.

What it does not check, and why the count is a bound
----------------------------------------------------
It is a screen, not a proof: a card can name a source and still state it
wrongly, and a phrase outside the lists (an unusual attribution) reads as
absent. So a card it reports must be opened before it is called missing, and a
card it passes has not thereby been verified. Run ``--explain`` on one card to
see exactly which signal it matched.

    python3 tools/provenance_screen.py [--explain CARD] [--list] [--collection SRC-...]
"""
from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

REMARK = 'title="Published solution"'

SOURCES = (
    "dongryul kim", "kim,", "cais", "sam,", "egbert", "yang pi-yeh", "shafarevich",
    "haiman", "zinger", "murayama", "pearse", "xie", "eisenbud", "miyanishi",
    "stacks project", "solutions to hartshorne", "hartshorne solutions",
    "attachments/",
)

OWN = (
    "card's own", "cards own", "no published solution", "no complete published",
    "no retained", "own argument", "own proof", "argument is this card",
    "the argument is the author", "is not published", "derived here",
)


def front_matter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end < 0:
        return "", text
    return text[:end], text[end + 4 :]


def signals(tail: str) -> list[str]:
    low = tail.lower()
    found = []
    if REMARK in tail:
        found.append("remark")
    if any(name in low for name in SOURCES):
        found.append("source")
    if any(phrase in low for phrase in OWN):
        found.append("own")
    return found


def cards(root: Path):
    for path in sorted(root.rglob("*.md")):
        if path.name == "index.md":
            continue
        text = path.read_text(encoding="utf-8")
        head, body = front_matter(text)
        if "kind: problem" not in head:
            continue
        start = body.find("::: {.solution}")
        if start < 0:
            continue
        cid = re.search(r"^id: (\S+)", head, re.M)
        yield path, (cid.group(1) if cid else path.stem), body[start:]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="corpus")
    parser.add_argument("--collection", default="")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--explain", default="")
    args = parser.parse_args()
    root = Path(args.root)

    if args.explain:
        for path, name, tail in cards(root):
            if name == args.explain:
                sig = signals(tail)
                print(f"{name} ({path}): signals {sig or 'none'}")
                return 0 if sig else 1
        print(f"{args.explain}: not a problem card with a solution")
        return 2

    total: Counter[str] = Counter()
    structured: Counter[str] = Counter()
    missing: list[tuple[str, str]] = []
    missing_structured: list[tuple[str, str]] = []
    for path, name, tail in cards(root):
        parts = path.relative_to(root).parts
        collection = "/".join(parts[:2]) if parts[0] == "collections" and len(parts) > 2 else parts[0]
        total[collection] += 1
        has_steps = "::: {.pf-step" in tail
        if has_steps:
            structured[collection] += 1
        if not signals(tail):
            missing.append((collection, name))
            if has_steps:
                missing_structured.append((collection, name))

    print(f"problem cards with a solution: {sum(total.values())}")
    print(f"with no remark, no source name and no own-argument statement: {len(missing)}")
    print(f"structured cards (with pf-steps): {sum(structured.values())}")
    print(f"  of those, without one: {len(missing_structured)}")
    for collection, count in total.most_common():
        gaps = sum(1 for c, _ in missing if c == collection)
        if gaps:
            print(f"  {collection:50s} {gaps:4d} of {count:4d}")
    if args.list:
        for collection, name in missing:
            print(f"{collection}\t{name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
