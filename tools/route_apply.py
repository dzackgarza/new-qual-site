#!/usr/bin/env python3
"""Materialise routing ledgers into problem-bundle cards and wiki pages.

A ledger says where every line of a source file goes. This performs that edit:

  card span  ->  one card under <out>/corpus/, body verbatim, and the span is
                 replaced in the wiki page by a `[[TAG]]` reference
  wiki span  ->  stays in the page, byte for byte

The point of doing this before routing the rest of the corpus is that a ledger
is not an artifact anyone can use. Until a card validates against the schema and
a wiki page renders with its references resolving, a clean ledger proves only
that the lines were classified -- not that the classification can be executed.

Writes to a fresh output root; never edits `corpus/` or the source repo.

    uv run python tools/route_apply.py <ledger-dir> <out-root>

Deferred, deliberately, and reported rather than guessed:

  occurrences   `exam_term` carries the sitting a problem appeared in. Turning
                that into occurrence + source cards needs the institution and
                term parsed and a source registry; the ledger records the raw
                string and this prints what it saw.
  topics        the topic registry is a closed vocabulary and nothing in the
                ledger names a topic. Cards land with `topics: []` rather than
                inventing entries.
  tag stability the id is content-derived, matching the existing corpus scheme.
                That means editing a bundle changes its tag, which is wrong for
                a permanent reference and is a pre-existing question in this
                repo, not one introduced here.
"""

from __future__ import annotations

import base64
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

AREA_BY_PREFIX = {
    "10_Algebra": "algebra",
    "20_Real_Analysis": "real-analysis",
    "30_Complex_Analysis": "complex-analysis",
    "40_Topology": "topology",
}
KIND_PREFIX = {"problem": "P", "exercise": "E"}


def tag(kind: str, body: str) -> str:
    digest = hashlib.sha1(body.encode()).digest()
    return f"{KIND_PREFIX.get(kind, 'X')}-" + base64.b32encode(digest).decode()[:5]


def rel_path(src: Path) -> Path:
    """The source's path relative to its corpus root, so the wiki keeps its tree."""
    parts = src.parts
    for marker in ("qual-wiki", "qual-review-and-solutions"):
        if marker in parts:
            return Path(*parts[parts.index(marker) + 1 :])
    return Path(src.name)


def area_of(src: Path) -> str | None:
    for part in src.parts:
        if part in AREA_BY_PREFIX:
            return AREA_BY_PREFIX[part]
    return None


def title_of(span: dict, body: str) -> str:
    """The authored title if there is one, else the first sentence of the statement.

    The corpus titles most expository divs but leaves problems bare -- 240 carry
    an explicit `?`. A generated title is a display handle, not an identity; the
    tag is the identity.
    """
    authored = str(span.get("title") or "").strip()
    if authored not in ("", "?"):
        return authored
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith((":::", "#", "---", ">")):
            continue
        line = re.sub(r"\s+", " ", line)
        return (line[:70].rstrip() + "…") if len(line) > 70 else line
    return "Untitled"


def apply_ledger(ledger: Path, out: Path) -> dict:
    spans = json.loads(ledger.read_text())
    src = Path((ledger.with_suffix(".source")).read_text().strip())
    lines = src.read_text(errors="replace").splitlines(keepends=True)
    area = area_of(src)

    page: list[str] = []
    cards: list[tuple[str, str]] = []
    terms: list[str] = []
    for span in spans:
        body = "".join(lines[span["start_line"] - 1 : span["end_line"]])
        if span["destination"] != "card":
            page.append(body)
            continue
        kind = span.get("kind", "problem")
        t = tag(kind, body)
        if span.get("exam_term"):
            terms.append(span["exam_term"])
        meta = [
            "---",
            "schema: qual/card@1",
            f"id: {t}",
            f"kind: {kind}",
            f"title: {json.dumps(title_of(span, body))}",
            "classification:",
            f"  areas:\n  - {area}" if area else "  areas: []",
            "  topics: []",
            "relations: []",
            "review: draft",
            "---",
            "",
        ]
        cards.append((t, "\n".join(meta) + body))
        page.append(f"[[{t}]]\n")

    (out / "corpus" / "wiki").mkdir(parents=True, exist_ok=True)
    for t, text in cards:
        (out / "corpus" / "wiki" / f"{t}.md").write_text(text)

    # The wiki page keeps its place in the tree. Writing by basename alone
    # collides -- qual-wiki has three `00_Resources.md`, three `000_Preface.md`
    # -- and silently overwrites, which is indistinguishable from a routing
    # failure when the reconstruction check runs. The directory structure is
    # also the wiki's navigation, so flattening would discard it regardless.
    wiki_page = out / "wiki" / rel_path(src)
    wiki_page.parent.mkdir(parents=True, exist_ok=True)
    wiki_page.write_text("".join(page))

    return {"source": src.name, "cards": len(cards), "page": wiki_page, "terms": terms, "area": area}


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    ledgers, out = Path(argv[0]), Path(argv[1])
    reports = [apply_ledger(p, out) for p in sorted(ledgers.glob("*.json"))]
    total = sum(r["cards"] for r in reports)
    for r in reports:
        print(f"{r['cards']:4d} bundles  area={r['area'] or '—':16s} {r['source']}")
    print(f"\n{total} bundle cards, {len(reports)} wiki pages -> {out}")

    seen = Counter(t for r in reports for t in r["terms"])
    if seen:
        print(f"\n{sum(seen.values())} exam terms recorded but NOT yet made into occurrences:")
        for term, n in seen.most_common(8):
            print(f"   {n:3d}  {term}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
