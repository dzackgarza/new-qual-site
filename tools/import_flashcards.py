"""Ingest the `math-flashcards` qual decks as theory cards.

The corpus holds 3,348 problems against 3 definitions and 26 theorems: it has no
theory layer at card level. `math-flashcards` is where that layer was authored,
as Anki decks in nested-list markdown, and it appeared in no ledger.

Deck format (README.md of that repo, verified against every file here): a
top-level list item is the front of the card, its indented body is the back, and
an optional trailing `tags:` line carries the author's own classification. The
front becomes the card title and the back becomes the card body, verbatim --
only the list indentation is removed, because it is the file's syntax and not
the author's prose.

    uv run python tools/import_flashcards.py report   # dispositions, mint nothing
    uv run python tools/import_flashcards.py mint     # write corpus/flashcards/

Three dispositions, total over the 496 deck cards:

  migrated   minted as a card under corpus/flashcards/
  dropped    its content is already in the corpus -- names the card it duplicates,
             or the deck file it is a byte-copy of
  queued     its statement depends on one of the 17 missing figures, which are
             tabled for re-authoring as TikZ. Minting it would silently drop the
             figure and store an incomplete statement.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
# The decks are read from the copy inside this repository, not from a clone of the
# source. Pointing at `~/gitclones/math-flashcards` meant the importer and the test
# over it only worked on one machine: CI has no such clone, so `dispositions()`
# returned an empty list and the Pages deploy failed on every push with
# `assert 0 == 496`. It is also what PLAN-QUAL-HANDOFF-CLOSEOUT-001's invariant 4
# forbids -- a permanent target may not depend on a source clone.
DECKS = REPO / "assets/ws9/math-flashcards/native"
OUT = REPO / "corpus/flashcards"

# The 28 `*Qual*` decks. The other decks in that repo (orals, schemes, toric,
# algebraic geometry, lattices, reading notes) are not qual material.
#
# Order decides which copy of a repeated card is the one minted, so a deck filed
# under a `Qual*` directory sorts first: `decks/Analysis/QualClassReview.md` and
# `decks/Qual Real Analysis/QualClassReview.md` are the same 24 cards under two
# deck names, and the qual-filed one is the copy this corpus wants.
QUAL_DECKS = sorted(
    [p for p in (DECKS / "decks").rglob("*.md") if "qual" in p.stem.lower() or "Qual" in p.parent.name],
    key=lambda p: (not p.parent.name.startswith("Qual"), str(p)),
)

# Area comes from the deck the author filed the card under, which is that
# author's own classification of it -- never from guessing at the mathematics.
# Two decks need a hand call and get one here rather than an empty list:
#   Qual Algebra/QualAlgebraicTopology.md -- filed under algebra, but its cards
#     are homology computations, so the area is topology.
#   Qual Basics/ -- not one of the four exam areas. `Basics.md` is polynomial
#     factoring and Descartes' rule, which is algebra; `Special Angles.md` is
#     trig values, which both analysis quals use, so it carries both.
DECK_AREAS = {
    "Qual Algebra": ["algebra"],
    "Qual Real Analysis": ["real-analysis"],
    "Qual Complex Analysis": ["complex-analysis"],
    "Qual Topology": ["topology"],
    "Analysis": ["real-analysis"],
}
FILE_AREAS = {
    "Qual Algebra/QualAlgebraicTopology.md": ["topology"],
    "Qual Basics/Basics.md": ["algebra"],
    "Qual Basics/Special Angles.md": ["real-analysis", "complex-analysis"],
    "Quals/Commutative Algebra.md": ["algebra"],
    "Quals/Complex Analysis.md": ["complex-analysis"],
    "Quals/Real Analysis.md": ["real-analysis"],
    "Quals/Topology.md": ["topology"],
}

# The author's tag -> card kind. Highest-priority tag present wins, so
# `theorem, proof` is a theorem and `definition, example, counterexample` is a
# definition. An untagged card, or one tagged only with a subject word
# (`math`, `complex`, `important`), is a `fact`: a result stated without proof
# is exactly what the kind means, and it is the honest floor rather than a
# promotion to `theorem` the source does not support.
class FlashcardKind(Enum):
    """The deck-tag classification vocabulary: the value is the corpus kind string."""

    DEFINITION = "definition"
    THEOREM = "theorem"
    PROPOSITION = "proposition"
    EXAMPLE = "example"
    PROOF = "proof"
    STRATEGY = "strategy"
    FACT = "fact"


TAG_KIND = [
    (FlashcardKind.DEFINITION, ("definition", "definitions", "notation")),
    (FlashcardKind.THEOREM, ("theorem", "theorems")),
    (FlashcardKind.PROPOSITION, ("proposition",)),
    (FlashcardKind.EXAMPLE, ("example", "examples", "counterexample", "counterexamples")),
    (FlashcardKind.PROOF, ("proof",)),
    (FlashcardKind.STRATEGY, ("technique",)),
    (FlashcardKind.FACT, ("fact", "facts", "formula", "formulas", "identity", "problem")),
]
KIND_PREFIX = {
    FlashcardKind.DEFINITION: "FD",
    FlashcardKind.THEOREM: "FT",
    FlashcardKind.PROPOSITION: "FP",
    FlashcardKind.EXAMPLE: "FE",
    FlashcardKind.PROOF: "FR",
    FlashcardKind.STRATEGY: "FS",
    FlashcardKind.FACT: "FF",
}

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"


@dataclass
class DeckCard:
    deck: str  # repo-relative path of the deck file
    front: str
    back: str
    tags: list[str]

    @property
    def kind(self) -> FlashcardKind:
        for kind, words in TAG_KIND:
            if any(t in words for t in self.tags):
                return kind
        return FlashcardKind.FACT

    @property
    def areas(self) -> list[str]:
        rel = self.deck[len("decks/") :]
        if rel in FILE_AREAS:
            return FILE_AREAS[rel]
        return DECK_AREAS[rel.split("/")[0]]

    @property
    def id(self) -> str:
        digest = int.from_bytes(hashlib.sha1(f"{self.deck}\n{self.front}".encode()).digest()[:5], "big")
        tail = "".join(ALPHABET[(digest >> (5 * i)) & 31] for i in range(5))
        return f"{KIND_PREFIX[self.kind]}-{tail}"


def parse_deck(path: Path) -> list[DeckCard]:
    """Split a deck into cards. A top-level `- ` opens one; every following line
    that is blank or indented belongs to it."""
    rel = str(path.relative_to(DECKS))
    lines = path.read_text().splitlines()
    if lines[0] == "---":  # skip the deck's own front matter
        lines = lines[lines.index("---", 1) + 1 :]

    cards: list[DeckCard] = []
    front: str | None = None
    body: list[str] = []

    def flush() -> None:
        if front is None:
            return
        text = "\n".join(body)
        tags: list[str] = []
        match = re.search(r"^tags:\s*(.+)$", text, re.M)
        if match:
            tags = [t.strip().lower() for t in re.split(r"[,\s]+", match.group(1)) if t.strip()]
            text = text[: match.start()] + text[match.end() :]
        cards.append(DeckCard(rel, front, text.strip("\n"), tags))

    for line in lines:
        if line.startswith("- "):
            flush()
            front, body = line[2:].strip(), []
        elif front is not None:
            # Dedent by the body indent (4 spaces); nested list levels survive.
            body.append(line[4:] if line.startswith("    ") else line)
    flush()
    return cards


# The recovered decks lost their `figures/` directory: 17 figures are missing and
# the migration left this marker where the answer used to be. An `![](...)` is an
# image the back leans on too. Either way the mathematics is not in the text.
IMAGE = re.compile(r"!\[[^\]]*\]\([^)]*\)|\*\(Answer was a figure; image not recovered\.\)\*")


# A back that is a bare `?` is the same loss recorded differently: 19 of the qual
# cards whose figure went missing kept the question mark the author typed where
# the picture used to be, and every one of them is a card MISSING-FIGURES.md
# names. `Proof: ?` is the same thing behind a label.
PLACEHOLDER = re.compile(r"^([A-Za-z ]{0,12}:)?\s*\?$")

# A short single line ending in a colon announces the figure that followed it
# ("The Cathode Ray:") and states nothing itself. The test is deliberately narrow:
# a whole proof that happens to end `The actual source:` is still a proof, and an
# earlier rule that looked only at the last character queued one away.
ANNOUNCEMENT = re.compile(r"^.{0,40}:$")


def figureless_body(back: str) -> str:
    """What of the back survives with the images and placeholders taken out.

    A card is only complete without its figure if prose remains that states the
    mathematics. A bare label such as `The Cathode Ray:` announces the figure
    rather than replacing it, and a bare `?` never said anything at all.
    """
    rest = IMAGE.sub("", back).strip()
    if PLACEHOLDER.match(rest) or ANNOUNCEMENT.match(rest):
        return ""
    return rest


def normalize(text: str) -> str:
    """Fold a title to a comparison key: case, whitespace, and math delimiters
    are not differences in the mathematics.

    Macro *names* are kept. Stripping them collapses `$\\sin(\\pi/4)$`,
    `$\\cos(\\pi/4)$` and `$\\tan(\\pi/4)$` to the single key `4`, which is how a
    first pass reported six Special Angles cards as duplicates of one another.
    """
    text = re.sub(r"\$+", " ", text.lower())
    # A leading minus is part of the number: without this, `Euler Characteristic
    # 2` and `Euler Characteristic -2` fold together, which they are not.
    text = re.sub(r"-(?=\d)", " minus ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


# Comparison is against the corpus's theory cards only. A `problem` sharing a
# title is not the same content: `P-4IWVY` is titled `**Irreducible:**` and holds
# a solution fragment about irreducible modules, and the corpus's three "Class
# Equation" hits are all one exam problem that asks the reader to *use* it. A
# definition of either is new content, not a second copy.
THEORY_KINDS = {
    "definition",
    "theorem",
    "proposition",
    "corollary",
    "lemma",
    "fact",
    "example",
    "concept",
    "remark",
    "slogan",
    "strategy",
}


def corpus_titles() -> dict[str, str]:
    """normalized title -> card id, over the corpus's existing theory cards."""
    out: dict[str, str] = {}
    for path in (REPO / "corpus").rglob("*.md"):
        if path.is_relative_to(OUT):
            continue
        head = path.read_text()[:2000]
        kind = re.search(r"^kind:\s*(\S+)$", head, re.M)
        title = re.search(r"^title:\s*(.+)$", head, re.M)
        if not kind or not title or kind.group(1) not in THEORY_KINDS:
            continue
        key = normalize(title.group(1).strip().strip("'\""))
        if key and key not in out:
            out[key] = path.stem
    return out


def card_text(card: DeckCard, variant_of: str | None) -> str:
    title = card.front.replace('"', "'")
    relations = "relations: []\n"
    if variant_of:
        relations = f"relations:\n- kind: variant-of\n  target: {variant_of}\n"
    return (
        "---\n"
        "schema: qual/card@1\n"
        f"id: {card.id}\n"
        f"kind: {card.kind.value}\n"
        f"title: {yaml_scalar(card.front)}\n"
        "classification:\n"
        "  areas:\n" + "".join(f"  - {a}\n" for a in card.areas) + "  topics: []\n" + relations + "review: draft\n"
        "---\n\n"
        f'::: {{.{card.kind.value} title="{title}"}}\n'
        f"{card.back}\n"
        ":::\n"
    )


def yaml_scalar(text: str) -> str:
    return "'" + text.replace("'", "''") + "'"


class QueueReason(Enum):
    """Why a deck card did not migrate: the value is the ledger wire string."""

    SCRATCH = "scratch"
    LOST_FIGURE = "lost-figure"
    DUPLICATE_CORPUS = "duplicate-corpus"
    DUPLICATE_DECK = "duplicate-deck"


def dispositions() -> list[dict]:
    """One row per deck card. Nothing is written.

    The author's decks overlap on purpose -- `QualTopology` restates
    `QualPointSetTopology`, `QualComplexAnalysis` restates `Definitions` -- so the
    same front appears several times. Title alone does not settle what to do with
    the repeat, and PLAN-QUAL-GRUNT-001's G3 rule decides it: an identical body
    collapses onto the first card, a differing body is a `variant-of` and is
    minted, because the two wordings are not the same mathematics.
    """
    titles = corpus_titles()
    seen: dict[str, tuple[str, str]] = {}  # title key -> (first card id, body key)
    rows: list[dict] = []
    for path in QUAL_DECKS:
        for card in parse_deck(path):
            row = {
                "deck": card.deck,
                "front": card.front,
                "kind": card.kind,
                "id": card.id,
            }
            key = normalize(card.front)
            body = normalize(card.back)
            if (card.front, card.back) == ("abcdefg", "asdasdsad"):
                # The author's scratch deck `2021-12-18` holds one keyboard-mash
                # card. It is not mathematics and there is nothing to queue.
                row |= {"disposition": "dropped", "reason_kind": QueueReason.SCRATCH, "reason": "keyboard-mash scratch card, no mathematical content"}
            elif not figureless_body(card.back):
                row |= {
                    "disposition": "queued",
                    "reason_kind": QueueReason.LOST_FIGURE,
                    "reason": "back is a lost figure or a bare `?` with no prose statement; the 17 missing figures are tabled for TikZ re-authoring",
                }
            elif key in titles:
                row |= {
                    "disposition": "dropped",
                    "reason_kind": QueueReason.DUPLICATE_CORPUS,
                    "reason": f"duplicates corpus card {titles[key]} (same normalized title)",
                }
            elif key in seen and seen[key][1] == body:
                row |= {
                    "disposition": "dropped",
                    "reason_kind": QueueReason.DUPLICATE_DECK,
                    "reason": f"duplicates flashcard {seen[key][0]} (same front and same body, an earlier deck)",
                }
            else:
                evidence = f"corpus/flashcards/{card.id}.md"
                if key in seen:
                    row["variant_of"] = seen[key][0]
                    evidence += f", variant-of {seen[key][0]}"
                else:
                    seen[key] = (card.id, body)
                row |= {"disposition": "migrated", "evidence": evidence}
            rows.append(row)
    return rows


def mint(rows: list[dict]) -> int:
    by_key = {(r["deck"], r["front"]): r for r in rows}
    OUT.mkdir(parents=True, exist_ok=True)
    for path in OUT.glob("*.md"):
        path.unlink()
    written = 0
    for path in QUAL_DECKS:
        for card in parse_deck(path):
            row = by_key[(card.deck, card.front)]
            if row["disposition"] != "migrated":
                continue
            (OUT / f"{card.id}.md").write_text(card_text(card, row.get("variant_of")))
            written += 1
    return written


SIDECAR = REPO / "sources/flashcard-import-ledger.jsonl"


def main(argv: list[str]) -> int:
    rows = dispositions()
    if argv and argv[0] == "mint":
        print(f"minted {mint(rows)} cards -> {OUT}")
        SIDECAR.write_text("\n".join(json.dumps({k: v.value if isinstance(v, Enum) else v for k, v in r.items()}) for r in rows) + "\n")
        print(f"wrote {len(rows)} card dispositions -> {SIDECAR}")

    from collections import Counter

    print(f"{len(rows)} deck cards across {len(QUAL_DECKS)} decks")
    for disposition, n in Counter(r["disposition"] for r in rows).most_common():
        print(f"  {disposition}: {n}")
    print("\nby deck:")
    for deck in sorted({r["deck"] for r in rows}):
        counts = Counter(r["disposition"] for r in rows if r["deck"] == deck)
        print(f"  {deck}: " + ", ".join(f"{d} {n}" for d, n in sorted(counts.items())))
    print("\nby kind (minted):")
    for kind, n in Counter(r["kind"] for r in rows if r["disposition"] == "migrated").most_common():
        print(f"  {kind}: {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
