"""Which cards a file under `proofs/` certifies, and the status that follows.

A card's proof status is derived and stored nowhere. It is one of three, and
two authored sources decide it:

- **certified** — `proofs/README.md` lists a certificate file for the card, in
  one of the two sections that hold them (Lean lemmas, exact finite
  computations). The file name decides what is named on the page: `.lean` is
  Lean, `.sage` exact Sage, `.g` exact GAP.
- **reviewed** — no certificate, and the card's `review:` field says a review
  has happened (`reviewed`, or the reserved `verified`).
- **draft** — neither.

`proofs/README.md` is the registry because it is where the certificates are
described and where an author already writes the file-to-card mapping when they
add one. A second `certificate:` field on the card would be a copy that drifts,
and the certificate is a file in this repository whose own table row says what
it proves.

Only sections 1 and 2 are read. Section 1 is "Group lemmas proved in Lean" and
section 2 is "Exact finite computations", and their tables map files to cards.
The later tables do not: section 6 lists repairs with *no* machine certificate
while its backing column mentions certificate files in passing, and section 7c
lists what discharges a node rather than what certifies a card. Reading those
would certify cards on the strength of a sentence that says the opposite.

Within a certificate table a row's file is the cell that is nothing but one
backticked `cards/...` path. The two section-2 tables differ: one carries its
file in a third column, the other carries it in the paragraph above the table,
so a row with no file cell inherits the last `cards/...` path named before it.
`bary_regression.py` is not a certificate -- its own row says so -- so only the
three machine-checked extensions are read, and a row naming no certificate of
its own inherits the one named above it.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

# The three states a reader is told about, in the order they are reported.
STATUSES = ("certified", "reviewed", "draft")

CERTIFICATE_SECTIONS = (1, 2)

# What a certificate file is. The extension is the whole claim: a `.lean` file
# is elaborated, a `.sage` file is an exact finite computation in Sage.
TOOLS = {".lean": "Lean", ".sage": "exact Sage", ".g": "exact GAP"}

_SECTION = re.compile(r"^## (\d+)\.")
_SUBSECTION = re.compile(r"^## ")
_INLINE = re.compile(r"`([^`]+)`")
_CARD_ID = re.compile(r"[PE]-[A-Z0-9]+(?:[.\-][A-Z0-9]+)*")
_CARD_REF = re.compile(r"-[A-Z0-9]+(?:\.[A-Z0-9]+)*")
_FILE = re.compile(r"cards/[^`\s]+\.(?:lean|sage|g)")


@dataclass(frozen=True)
class Certificate:
    """One machine-checked artifact and the tool that checks it."""

    # Repository-relative, with the `proofs/` prefix: `proofs/cards/BarySign.lean`.
    file: str
    # `Lean`, `exact Sage` or `exact GAP`.
    tool: str


def tool_of(file: str) -> str | None:
    return TOOLS.get(Path(file).suffix)


def status(review: str, certificates: tuple[Certificate, ...]) -> str:
    """The three-way status a page states, from the card's own two sources.

    `review: verified` is reserved and currently unpopulated; it is a level of
    review above draft, so it reads as `reviewed` rather than disappearing.
    """
    if certificates:
        return "certified"
    return "draft" if review == "draft" else "reviewed"


def load(proofs: Path) -> dict[str, tuple[Certificate, ...]]:
    """Card id to its certificates, from the tables of `proofs/README.md`.

    A repository with no `proofs/README.md` certifies nothing, which is what a
    fixture corpus is.
    """
    readme = proofs / "README.md"
    if not readme.is_file():
        return {}
    rows: dict[str, list[Certificate]] = {}
    for card_id, file in _rows(readme.read_text().splitlines()):
        tool = tool_of(file)
        if tool is None:
            continue
        certificate = Certificate(file=f"proofs/{file}", tool=tool)
        entries = rows.setdefault(card_id, [])
        if certificate not in entries:
            entries.append(certificate)
    return {card_id: tuple(entries) for card_id, entries in rows.items()}


def _rows(lines: list[str]) -> list[tuple[str, str]]:
    """Every (card id, `cards/...` path) pair the certificate tables state."""
    out: list[tuple[str, str]] = []
    section: int | None = None
    # The artifact a file-less table is about, named in the prose above it.
    standing: str | None = None
    for line in lines:
        heading = _SECTION.match(line)
        if heading:
            section = int(heading.group(1))
            continue
        # A subheading keeps its section: the all-`n` sign discussion sits
        # between two blocks of section 1's certificate rows.
        if _SUBSECTION.match(line):
            section = None
            continue
        if section not in CERTIFICATE_SECTIONS:
            continue
        named = _FILE.findall(line)
        if named and not _table_row(line):
            standing = named[0]
        if not _table_row(line) or _is_separator(line):
            continue
        card_ids = _card_ids(line)
        if not card_ids:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        exact = [cell for cell in cells if _FILE.fullmatch(cell.strip("`"))]
        file = exact[0].strip("`") if exact else standing
        if file is None:
            continue
        out.extend((card_id, file) for card_id in card_ids)
    return out


def _table_row(line: str) -> bool:
    return line.startswith("|")


def _is_separator(line: str) -> bool:
    return set(line.replace("|", "").strip()) <= set("-: ")


def _card_ids(line: str) -> list[str]:
    """The cards a row names, expanding the `-3` shorthand for a repeated id.

    `| P-CH8-1`, `-3`, `-4` |` is how the table writes three cards of one
    source, and the shorthand means the prefix of the last full id written.
    """
    ids: list[str] = []
    previous: str | None = None
    for token in _INLINE.findall(line):
        if _CARD_ID.fullmatch(token):
            ids.append(token)
            previous = token
        elif previous is not None and _CARD_REF.fullmatch(token):
            previous = previous[: previous.rfind("-")] + token
            ids.append(previous)
    return ids
