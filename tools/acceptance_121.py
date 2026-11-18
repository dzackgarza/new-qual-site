#!/usr/bin/env python3
"""Check the per-card acceptance of issue #121 against what a card states.

Issue #121 requires, for each Hartshorne card its inventory names, "the published
source and its printed page on the card, with the proof matching it and checked
against the book".  Three of those four parts are decidable from text alone, and
this module decides them:

  R1 PUBLICATION   the card's rendered body names at least one publication, that
                   is a solution set, a textbook, lecture notes or a numbered
                   Stacks tag -- not a Mathematics Stack Exchange or MathOverflow
                   answer, which is a user post.
  R2 PAGE          at least one publication the body names carries a page or a
                   numbered statement within 500 characters of its name
                   ("printed p. 84", "PDF pp. 16--17", "tag 0BYA").  A name that
                   carries no page is reported as a note, not a failure.
  R3 EXERCISE      the exercise the card states is locatable in the checked-in
                   text version of Hartshorne by section heading and number; if
                   it is not, the card must name the book's printed or PDF page
                   for it (the text version being an extraction, its gaps are
                   reported by this module and not charged to the card).

The fourth part -- whether a proof matches its source -- is not decidable from
text, and this module only reports, for each card, how many of its quoted spans
occur in a text version the card names.  That number is advisory: a faithful
quotation is not a proof of agreement.

Usage: python3 tools/acceptance_121.py [--root ROOT] [--json]
Exit 1 if any card fails R1, R2 or R3.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

COLLECTION = Path("corpus/collections/SRC-TEXT-HART77")
BOOK = Path("tmp/sources/hartshorne-1977-algebraic-geometry.md")
INVENTORY_HEAD = "**The cards, sixty-nine.**"
INVENTORY_TAIL = "**What was searched in this pass"

# Publications: a solution set, book, lecture notes or numbered-theorem source.
PUBLICATIONS = (
    "Borcherds", "Troiani", "Egbert", "Cutrone", "Cais", "Lomont", "Park",
    "Saglam", "Stein", "Okamoto", "Shichijo", "National Taiwan University",
    "Kim", "Yang", "Mumford", "Deligne", "Peters", "Sobieska", "Huybrechts", "Kaur", "Dan and",
    "NTU", "Vakil", "Harris", "Reid", "Dolgachev", "Gunning", "Fulton", "Rud",
    "Gruson", "Bourbaki", "Abhyankar", "Haiman", "Bertram", "Garland", "Milne",
    "Stacks Project", "Riebe", "Brieskorn", "Laufer", "Greuel",
)
# A user post is not a publication, whatever else the card says about it.
USER_POSTS = ("Math StackExchange", "Math Stack Exchange", "Mathematics Stack Exchange",
              "MathOverflow", "Stack Exchange answer", "answer to Mathematics Stack")

PAGE_TOKEN = re.compile(r"(printed p+p?\.|PDF p+p?\.|tag [0-9A-Z]{4}|Theorem [0-9IVX]+\.[0-9.]+|Lemma [0-9IVX]+\.[0-9.]+)")
EXERCISE = re.compile(r"`(P-[0-9A-Z-]+)`\s+\(([IV]+)\.(\d+)\.(\d+)")
EXERCISE_FALLBACK = {
    "P-AGH319JACOBIAN": ("I", "3", "19"),
    "P-AGH4110PICOFARITHGENUSONE": ("IV", "1", "10"),
    "P-AGH434RATIONALNORMALCURVE": ("IV", "3", "4"),
}
CHAPTER_PAGES = {"I": (1, 59), "II": (60, 201), "III": (202, 293), "IV": (294, 356), "V": (357, 424)}


def body_of(text: str) -> str:
    """The rendered part of a card: everything after the front matter."""
    if text.startswith("---\n"):
        parts = text.split("\n---\n", 1)
        if len(parts) == 2:
            return parts[1]
    return text


class Book:
    """Locate an exercise in Hartshorne's text version by section and number."""

    def __init__(self, path: Path) -> None:
        self.lines: list[str] = []
        self.printed: list[int | None] = []
        if not path.exists():
            return
        page: int | None = None
        for line in path.read_text().splitlines():
            m = re.match(r"<!-- PDF page (\d+) -->", line)
            if m:
                page = int(m.group(1))
            self.lines.append(line)
            self.printed.append(None if page is None else page - 15)
        self.sections = [
            (i, line) for i, line in enumerate(self.lines) if re.match(r"^## \d+ [A-Z]", line)
        ]

    def find(self, chapter: str, section: str, exercise: str) -> tuple[int, int] | None:
        """(printed page, one-based line) of the exercise, or None."""
        low, high = CHAPTER_PAGES[chapter]
        heads = [
            i
            for i, line in self.sections
            if re.match(rf"^## {section} ", line)
            and self.printed[i] is not None
            and low - 1 <= self.printed[i] <= high
        ]
        if not heads:
            return None
        start = heads[0]
        stop = min([i for i, _ in self.sections if i > start], default=len(self.lines))
        pattern = re.compile(r"^\s*(\\?\*)*" + section + r"\." + exercise + r"\.?\s")
        for i in range(start, stop):
            if pattern.match(self.lines[i]) and self.printed[i] is not None:
                return self.printed[i], i + 1
        return None


def publications_named(body: str) -> list[str]:
    return [name for name in PUBLICATIONS if re.search(rf"(?<![\w-]){re.escape(name)}", body)]


def page_cited_for(body: str, name: str) -> bool:
    for m in re.finditer(re.escape(name), body):
        window = body[m.start(): m.start() + 500]
        if PAGE_TOKEN.search(window):
            return True
    return False


def exercise_of(card_id: str, inventory: str) -> tuple[str, str, str] | None:
    for cid, chapter, section, exercise in EXERCISE.findall(inventory):
        if cid == card_id:
            return chapter, section, exercise
    return EXERCISE_FALLBACK.get(card_id)


def quoted_spans(body: str) -> list[str]:
    return [q for q in re.findall(r'"([^"]{60,400})"', body) if len(re.findall(r"[A-Za-z]{4,}", q)) >= 6]


def words(text: str) -> set[str]:
    return {w.lower() for w in re.findall(r"[A-Za-z]{4,}", text)}


def quote_fidelity(body: str, root: Path) -> tuple[int, int]:
    """(spans examined, spans found in a text version the card names)."""
    named = set(re.findall(r"tmp/sources/[A-Za-z0-9._\-/]+\.md", body))
    named.add(str(BOOK))
    pools = []
    for rel in named:
        path = root / rel
        if path.exists():
            pools.append(words(path.read_text()))
    spans = quoted_spans(body)
    found = 0
    for span in spans:
        bag = words(span)
        if any(len(bag & pool) / len(bag) >= 0.85 for pool in pools):
            found += 1
    return len(spans), found


def check(root: Path) -> list[dict]:
    complaints = root / "COMPLAINTS.md"
    inventory = ""
    if complaints.exists():
        text = complaints.read_text()
        if INVENTORY_HEAD in text and INVENTORY_TAIL in text:
            inventory = text.split(INVENTORY_HEAD, 1)[1].split(INVENTORY_TAIL, 1)[0]
    if not inventory:
        return [{"card": "-", "fail": "R0 inventory", "evidence": "COMPLAINTS.md: no sixty-nine-card inventory block"}]

    seen: list[str] = []
    for cid, *_ in EXERCISE.findall(inventory):
        if cid not in seen:
            seen.append(cid)
    for cid in EXERCISE_FALLBACK:
        if cid not in seen and (root / COLLECTION / f"{cid}.md").exists():
            seen.append(cid)

    book = Book(root / BOOK)
    rows = []
    for cid in seen:
        path = root / COLLECTION / f"{cid}.md"
        if not path.exists():
            rows.append({"card": cid, "fail": "R1 publication", "evidence": f"{path}: missing card"})
            continue
        text = path.read_text()
        body = body_of(text)
        names = publications_named(body)
        row = {"card": cid}
        if not names:
            row["fail"] = "R1 publication"
            row["evidence"] = f"{COLLECTION}/{cid}.md: no publication named; user post named: {[u for u in USER_POSTS if u in body][:1]}"
            rows.append(row)
            continue
        cited = [n for n in names if page_cited_for(body, n)]
        if not cited:
            line = next((i + 1 for i, l in enumerate(text.splitlines()) if names[0] in l), 0)
            row["fail"] = "R2 page"
            row["evidence"] = f"{COLLECTION}/{cid}.md:{line}: no page or numbered statement for any of {names}"
            rows.append(row)
            continue
        uncited = [n for n in names if n not in cited]
        exercise = exercise_of(cid, inventory)
        if exercise:
            chapter, section, number = exercise
            hit = book.find(chapter, section, number)
            if hit is None:
                token = f"{chapter}.{section}.{number}"
                if not re.search(re.escape(token) + r"[^\n]{0,200}(PDF|printed) p+\.", text):
                    row["fail"] = "R3 exercise"
                    row["evidence"] = f"{COLLECTION}/{cid}.md: {token} not in {BOOK} and no printed or PDF page given for it"
                    rows.append(row)
                    continue
                row["note"] = f"{token} absent from the text version; its book page is on the card"
        spans, found = quote_fidelity(body, root)
        row.setdefault("quotes", f"{found}/{spans}")
        if uncited:
            row["note"] = "; ".join(filter(None, [row.get("note", ""), "names without a page: " + ", ".join(uncited)]))
        rows.append(row)
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=".", type=Path)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    rows = check(args.root.resolve())
    if args.json:
        print(json.dumps(rows, indent=1))
    else:
        for row in rows:
            if "fail" in row:
                print(f"FAIL {row['card']:44s} {row['fail']:16s} {row['evidence']}")
            else:
                print(f"ok   {row['card']:44s} quotes {row.get('quotes','0/0'):>6s} {row.get('note','')}")
    failed = [r for r in rows if "fail" in r]
    print(f"\n{len(rows) - len(failed)} of {len(rows)} cards pass R1--R3; {len(failed)} fail", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
