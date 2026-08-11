"""Emit the wiki pages that make every card reachable, from recorded order only.

G7 of PLAN-QUAL-GRUNT-001. Three bodies of cards were reachable from no page:

  * every `source` card -- the sittings, contributed artifacts and workshop days.
    The order is the archive's own: institution, then date. The order *inside* a
    sitting is not repeated here; `emit.source_page` already prints it from the
    occurrence locators, "in the order they appeared".
  * the `math-flashcards` decks. The order is each deck file's own card order,
    recorded line by line in `sources/flashcard-import-ledger.jsonl`.
  * the `Extra Problems` chapter of `AlgebraQualNotes.md`. The order is the
    chapter's own, recorded with its heading path in
    `sources/authored-md-routing.jsonl`.

Nothing here composes a reading order. Every page transcribes an order that
already exists in a ledger or in a card's own date field, and every page records
what supplied it in `sources/g7-page-attachment.jsonl`.

    uv run python tools/attach_pages.py
"""

from __future__ import annotations

import json
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent

AREA_DIR = {
    "prelim": "00_Prelims",
    "algebra": "10_Algebra",
    "real-analysis": "20_Real_Analysis",
    "complex-analysis": "30_Complex_Analysis",
    "topology": "40_Topology",
}

SUBJECT_TITLE = {
    "prelim": "Prelims",
    "algebra": "Algebra",
    "real-analysis": "Real Analysis",
    "complex-analysis": "Complex Analysis",
    "topology": "Topology",
}

# The deck tree is the author's own filing. A deck goes to the subject its own
# folder names, and `decks/Quals/` names the subject in the file instead.
DECK_FOLDER_AREA = {
    "Qual Algebra": "algebra",
    "Qual Real Analysis": "real-analysis",
    "Qual Complex Analysis": "complex-analysis",
    "Qual Topology": "topology",
    "Qual Basics": "prelim",
}
DECK_FILE_AREA = {
    "Real Analysis": "real-analysis",
    "Complex Analysis": "complex-analysis",
    "Topology": "topology",
    "Commutative Algebra": "algebra",
}

TERM_ORDER = {"spring": 0, "fall": 1}

# Every page here lists ids, the convention of the authored pages they sit beside.
# What a reader does not get from them is recorded once, not per page.
ID_LIST_NOTE = (
    "the page lists card ids, the convention of the authored pages it sits beside; a reader"
    " sees no statement or title until the link is followed. Titled link text and connective"
    " prose are tabled prose work."
)


def _front_matter(path: Path) -> dict:
    text = path.read_text()
    meta = yaml.safe_load(text.split("---\n")[1])
    if not isinstance(meta, dict):
        raise TypeError(f"{path}: front matter must be a mapping")
    return meta


def _cards() -> dict[str, dict]:
    cards: dict[str, dict] = {}
    for path in sorted((REPO / "corpus").rglob("*.md")):
        meta = _front_matter(path)
        cards[meta["id"]] = meta
    return cards


def _rows(name: str) -> list[dict]:
    path = REPO / "sources" / name
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def _date_key(date: dict) -> tuple[int, int]:
    """Sort key over the date union. A case without a year sorts last, because
    "we do not know when" is not "year zero"."""
    year = date["year"] if "year" in date else 10_000
    term = TERM_ORDER[date["term"]] if "term" in date else 0
    return year, term


def _write(route: str, title: str, lede: str, blocks: list[str]) -> None:
    path = REPO / route
    path.parent.mkdir(parents=True, exist_ok=True)
    head = f"---\ntitle: {json.dumps(title)}\n---\n\n# {title}\n\n{lede}\n"
    path.write_text(head + "".join(blocks))


def _ref(card_id: str) -> str:
    return f"[[{card_id}]]\n\n"


# --- source archive ---------------------------------------------------------


def _institution_heading(card: dict) -> str:
    payload = card["payload"]
    if payload["source_kind"] == "university-exam":
        institution: str = payload["institution"]
        return institution.upper()
    return "Contributed artifacts"


def source_archive(cards: dict[str, dict], theory: dict[str, list[str]]) -> list[dict]:
    """One page per subject listing every source card of that subject.

    Grouping and order are the archive's own: institution, then date. Nothing
    about which sitting to read first is asserted -- this is a catalogue.
    """
    by_area: dict[str, list[dict]] = {}
    for card in cards.values():
        if card["kind"] != "source":
            continue
        area = card["classification"]["areas"][0]
        if area not in by_area:
            by_area[area] = []
        by_area[area].append(card)

    emitted: list[dict] = []
    for area, items in sorted(by_area.items()):
        groups: dict[str, list[dict]] = {}
        for card in items:
            heading = _institution_heading(card)
            if heading not in groups:
                groups[heading] = []
            groups[heading].append(card)

        blocks: list[str] = []
        listed: list[str] = []
        # Institutions first, alphabetically; the artifacts that name no
        # institution last, because they are not a sitting of anything.
        headings = sorted(k for k in groups if k != "Contributed artifacts")
        if "Contributed artifacts" in groups:
            headings.append("Contributed artifacts")
        for heading in headings:
            blocks.append(f"\n## {heading}\n\n")
            for card in sorted(groups[heading], key=lambda c: (_date_key(c["payload"]["date"]), c["id"])):
                blocks.append(_ref(card["id"]))
                listed.append(card["id"])
                for theory_id in theory[card["id"]] if card["id"] in theory else []:
                    blocks.append(_ref(theory_id))
                    listed.append(theory_id)

        route = f"wiki/{AREA_DIR[area]}/700_Source_Archive.md"
        _write(
            route,
            f"{SUBJECT_TITLE[area]} Source Archive",
            "Every recorded sitting and contributed artifact in this subject, by institution and\n"
            "then by date. Each entry links to that source's own page, which lists its problems\n"
            "in the order they appeared.\n",
            blocks,
        )
        emitted.append(
            {
                "route": route,
                "disposition": "created",
                "standalone_note": ID_LIST_NOTE,
                "cards": listed,
                "order_source": "source card institution and date fields; within a source, emit.source_page prints the occurrence locators",
            }
        )
    return emitted


def workshop_theory(cards: dict[str, dict]) -> dict[str, list[str]]:
    """Workshop theory cards carry their day in their id and their number in
    their own title (`Proposition 3.1`), so both the owning document and the
    position inside it are recorded. They attach under their day's source card."""
    # A workshop problem is already listed on its day's own page, through its
    # occurrence. Only the theory statements, which have no occurrence, need a
    # position here.
    with_occurrence = {
        relation["target"]
        for card in cards.values()
        if card["kind"] == "occurrence"
        for relation in card["relations"]
        if relation["kind"] == "instance-of"
    }
    days: dict[str, list[tuple[tuple[int, ...], str]]] = {}
    for card_id, card in cards.items():
        parts = card_id.split("-")
        if "WORKSHOP" not in parts or card["kind"] in {"source", "occurrence"} or card_id in with_occurrence:
            continue
        day = next((p for p in parts if p.startswith("D") and p[1:].isdigit()), None)
        if day is None:
            continue
        subject = parts[1]
        label = card["title"].split(":")[0].split()[-1]
        number = tuple(int(n) for n in label.split(".")) if all(n.isdigit() for n in label.split(".")) else (10_000,)
        key = f"{subject}-{day}"
        if key not in days:
            days[key] = []
        days[key].append((number, card_id))

    attached: dict[str, list[str]] = {}
    for card_id, card in cards.items():
        if card["kind"] != "source":
            continue
        parts = card_id.split("-")
        if "WORKSHOP" not in parts:
            continue
        day = next((p for p in parts if p.startswith("D") and p[1:].isdigit()), None)
        key = f"{parts[1]}-{day}"
        if key in days:
            attached[card_id] = [cid for _, cid in sorted(days[key])]
    return attached


# --- flashcard decks --------------------------------------------------------


def deck_pages(cards: dict[str, dict]) -> list[dict]:
    order: dict[str, list[str]] = {}
    for row in _rows("flashcard-import-ledger.jsonl"):
        if row["disposition"] != "migrated" or row["id"] not in cards:
            continue
        if row["deck"] not in order:
            order[row["deck"]] = []
        if row["id"] not in order[row["deck"]]:
            order[row["deck"]].append(row["id"])

    emitted: list[dict] = []
    for deck, ids in sorted(order.items()):
        folder = Path(deck).parent.name
        stem = Path(deck).stem
        area = DECK_FOLDER_AREA[folder] if folder in DECK_FOLDER_AREA else DECK_FILE_AREA[stem]
        route = f"wiki/{AREA_DIR[area]}/900_Flashcards/{folder} - {stem}.md"
        _write(
            route,
            f"{folder}: {stem}",
            f"The `{deck}` deck of `math-flashcards`, in the deck's own card order.\n",
            ["\n"] + [_ref(card_id) for card_id in ids],
        )
        emitted.append(
            {
                "route": route,
                "disposition": "created",
                "standalone_note": ID_LIST_NOTE,
                "cards": ids,
                "order_source": f"math-flashcards {deck}, card order as recorded in sources/flashcard-import-ledger.jsonl",
            }
        )
    return emitted


# --- the review doc's Extra Problems chapter --------------------------------

EXTRA_PROBLEMS_ROUTE = "wiki/10_Algebra/500_Exercises/9970 Extra Problems.md"


def extra_problems(cards: dict[str, dict]) -> list[dict]:
    rows = [
        row
        for row in _rows("authored-md-routing.jsonl")
        if row["path"] == "Algebra/Review Doc/AlgebraQualNotes.md" and row["verdict"] == "minted" and row["card"] in cards
    ]
    blocks: list[str] = []
    listed: list[str] = []
    current: list[str] = []
    for row in rows:
        # The locator is the chapter's own heading path: `Extra Problems / Group
        # Theory / p-Groups`. Transcribe it back into headings, dropping the
        # chapter name because it is the page.
        headings = [part.strip() for part in row["locator"].split("/")][1:]
        if headings != current:
            for depth, heading in enumerate(headings):
                if depth >= len(current) or current[depth] != heading:
                    blocks.append(f"\n{'#' * (depth + 2)} {heading}\n\n")
            current = headings
        blocks.append(_ref(row["card"]))
        listed.append(row["card"])

    _write(
        EXTRA_PROBLEMS_ROUTE,
        "Extra Problems",
        "The `Extra Problems` chapter of `Algebra/Review Doc/AlgebraQualNotes.md`, in the\n"
        "chapter's own order and under its own headings.\n",
        blocks,
    )
    return [
        {
            "route": EXTRA_PROBLEMS_ROUTE,
            "disposition": "created",
            "standalone_note": ID_LIST_NOTE,
            "cards": listed,
            "order_source": "Algebra/Review Doc/AlgebraQualNotes.md chapter order and heading path, as recorded in sources/authored-md-routing.jsonl",
        }
    ]


def hub(emitted: list[dict]) -> list[dict]:
    """A reader reaches a page through a link, and the authored index links only
    what its author put there. One hub page collects the routes this tool emits,
    and `wiki/index.md` carries a single line pointing at it."""
    # Ordered by the subject directory numbering, which is the tree order the
    # author already gave the wiki.
    ordered = sorted(emitted, key=lambda row: row["route"])
    archives = [row for row in ordered if row["route"].endswith("700_Source_Archive.md")]
    decks = [row for row in ordered if "900_Flashcards" in row["route"]]
    others = [row for row in ordered if row not in archives and row not in decks]

    blocks = ["\n## Source archives\n\n"]
    blocks.extend(f"- [[{Path(row['route']).relative_to('wiki').with_suffix('').as_posix()}]]\n" for row in archives)
    blocks.append("\n## Flashcard decks\n\n")
    blocks.extend(f"- [[{Path(row['route']).relative_to('wiki').with_suffix('').as_posix()}]]\n" for row in decks)
    blocks.append("\n## Problem chapters\n\n")
    blocks.extend(f"- [[{Path(row['route']).relative_to('wiki').with_suffix('').as_posix()}]]\n" for row in others)

    route = "wiki/000_Card_Archives.md"
    _write(
        route,
        "Card Archives",
        "The pages that list the corpus by its source: the sittings and artifacts of each\n"
        "subject, the flashcard decks, and the review doc's problem chapter.\n",
        blocks,
    )
    return [
        {
            "route": route,
            "disposition": "created",
            "standalone_note": "a route index over the pages below it; it states no mathematics.",
            "cards": [],
            "order_source": "the routes this tool emits, grouped by the body they transcribe",
        }
    ]


def main() -> int:
    cards = _cards()
    emitted = source_archive(cards, workshop_theory(cards)) + deck_pages(cards) + extra_problems(cards)
    emitted += hub(emitted)
    ledger = REPO / "sources" / "g7-page-attachment.jsonl"
    ledger.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in emitted))
    print(f"wrote {len(emitted)} pages attaching {sum(len(row['cards']) for row in emitted)} cards; ledger {ledger.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
