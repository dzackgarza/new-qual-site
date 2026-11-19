"""Screen problem cards for a statement of where their argument comes from.

The register's screen of 2026-11-19 read only the ``.solution`` fence, so a
card that states its provenance in a ``::: {.remark title="Published solution"}``
block counted as lacking. This one reads the whole card after the frontmatter,
solution and every remark alike, and reports what it still finds without one.

The test is a phrase match, and its two errors are of unequal size. It cannot
tell a true sentence from a false one, and it misses phrasings outside the list;
every card it reports must be read before it is called absent. It is a screen,
not a gate, and no count from it is a claim about the mathematics.

    python3 tools/provenance_screen.py [--list] [--collection SRC-...]
"""
from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

MARKERS = (
    "transcrib", "published", "solutions", "the argument is", "the proof is",
    "the proof below is", "is that of", "are those of", "outline", "card's own",
    "the card's own", "following the", "follows the", "re-deriv",
    # retained Hartshorne sets and the other solution writers the corpus cites
    "kim", "cais", "sam", "egbert", "yang", "shafarevich", "haiman", "zinger",
    "murayama", "pearse", "xie", "eisenbud", "miyanishi", "stacks project",
    # a citation key is a pointer to a source even without prose
    "[@",
)


def front_matter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end < 0:
        return "", text
    return text[:end], text[end + 4 :]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="corpus")
    parser.add_argument("--collection", default="")
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args()

    total = Counter()
    structured = Counter()
    missing: list[tuple[str, str]] = []
    missing_structured: list[tuple[str, str]] = []
    for path in sorted(Path(args.root).rglob("*.md")):
        if path.name == "index.md":
            continue
        text = path.read_text(encoding="utf-8")
        head, body = front_matter(text)
        if "kind: problem" not in head:
            continue
        start = body.find("::: {.solution}")
        if start < 0:
            continue
        parts = path.relative_to(args.root).parts
        collection = "/".join(parts[:2]) if parts[0] == "collections" and len(parts) > 2 else parts[0]
        cid = re.search(r"^id: (\S+)", head, re.M)
        name = cid.group(1) if cid else path.stem
        total[collection] += 1
        steps = "::: {.pf-step" in body[start:]
        if steps:
            structured[collection] += 1
        tail = body[start:].lower()
        if not any(marker in tail for marker in MARKERS):
            missing.append((collection, name))
            if steps:
                missing_structured.append((collection, name))

    print(f"problem cards with a solution: {sum(total.values())}")
    print(f"without a provenance phrase in the solution or any remark: {len(missing)}")
    print(f"structured cards (with pf-steps): {sum(structured.values())}")
    print(f"  of those, without one: {len(missing_structured)}")
    for collection, count in total.most_common():
        gaps = sum(1 for c, _ in missing if c == collection)
        if gaps:
            print(f"  {collection:40s} {gaps:4d} of {count:4d}")
    if args.list:
        for collection, name in missing:
            print(f"{collection}\t{name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
