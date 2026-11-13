"""Which cards a file under `proofs/` certifies, and the status that follows.

A card's proof status is derived and stored nowhere. It is one of three, and
two authored sources decide it:

- **certified** — `proofs/README.md` lists a certificate row for the card, in
  one of the two sections that hold them (Lean lemmas, exact finite
  computations), and that row says it covers the card's **whole statement**. A
  Lean certificate is a link to a file at a named commit of this repository or
  to a declaration on lean-categories main. The Sage and GAP certificates are
  files that remain. What is named on the page decides the tool: `.lean` is
  Lean, `.sage` exact Sage, `.g` exact GAP.
- **reviewed** — no certificate covering the whole statement, and the card's
  `review:` field says a review has happened (`reviewed`, or the reserved
  `verified`).
- **draft** — neither.

A certificate that proves one claim of a card whose statement has several does
not make the card certified. `E-HAT-3.A-6` asks that `Tor(A,B)` be a torsion
group and that it have an element of order `n` when both arguments do; its rows
compute `Tor` of a presented stage, of a cyclic stage and of a two-term free
resolution, and they say in their own text that the passage to an arbitrary
abelian group is not proved. `E-HAT-3.A-2` has the same shape. Which of the two
things a row proves is authored on the row, not guessed here: see `COVERS`
below.

`proofs/README.md` is the registry because it is where the certificates are
described and where an author already writes the certificate-to-card mapping
when they add one. A second `certificate:` field on the card would be a copy
that drifts, and each certificate is either a file in this repository whose
own table row says what it proves or a link whose target the check follows.

Only sections 1 and 2 are read. Section 1 is "Group lemmas proved in Lean" and
section 2 is "Exact finite computations", and their tables map files to cards.
The later tables do not: section 6 lists repairs with *no* machine certificate
while its backing column mentions certificate files in passing, and section 7c
lists what discharges a node rather than what certifies a card. Reading those
would certify cards on the strength of a sentence that says the opposite.

Within a certificate table a row's file is the cell that is nothing but one
backticked `cards/...` path, or one `<https://github.com/dzackgarza/...>` link
naming a file at a commit of this repository or a declaration on
lean-categories main. The two section-2 tables differ: one carries its
file in a third column, the other carries it in the paragraph above the table,
so a row with no file cell inherits the last path or link named before it.
`bary_regression.py` is not a certificate -- its own row says so -- so only the
three machine-checked extensions are read, and a row naming no certificate of
its own inherits the one named above it.

The last cell of every certificate row is its `Covers` entry, and a row without
one is a corpus error rather than a certification: a certificate that proves
part of a statement has to say so on the page the reader is looking at.
"""

from __future__ import annotations

import re
import subprocess
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

# The three states a reader is told about, in the order they are reported.
STATUSES = ("certified", "reviewed", "draft")

CERTIFICATE_SECTIONS = (1, 2)

# What a row's last cell says it proves. `THE_STATEMENT` is the card's whole
# statement, and it is the only thing that makes a card certified; `PART` is
# one claim of a statement that has several, which the row's `What it proves`
# cell names. Nothing here decides which a row is -- the author of the table
# does, having read the certificate.
THE_STATEMENT = "the statement"
PART = "part"
COVERS = (THE_STATEMENT, PART)

# What a certificate file is. The extension is the whole claim: a `.lean` file
# is elaborated, a `.sage` file is an exact finite computation in Sage.
TOOLS = {".lean": "Lean", ".sage": "exact Sage", ".g": "exact GAP"}

# A Lean certificate is a link to a file at a named commit of this
# repository, or a declaration on lean-categories main. Both are GitHub
# blob URLs.
GITHUB = "https://github.com/dzackgarza/"
THIS_REPOSITORY = GITHUB + "new-qual-site/blob/"
LEAN_CATEGORIES = GITHUB + "lean-categories/blob/"

_SECTION = re.compile(r"^## (\d+)\.")
_SUBSECTION = re.compile(r"^## ")
_INLINE = re.compile(r"`([^`]+)`")
_CARD_ID = re.compile(r"[PE]-[A-Z0-9]+(?:[.\-][A-Z0-9]+)*")
_CARD_REF = re.compile(r"-[A-Z0-9]+(?:\.[A-Z0-9]+)*")
_FILE = re.compile(
    rf"(?:{re.escape(THIS_REPOSITORY)}|{re.escape(LEAN_CATEGORIES)})"
    rf"[^\s<>`]+|cards/[^`\s]+\.(?:lean|sage|g)"
)


@dataclass(frozen=True)
class Certificate:
    """One machine-checked artifact, the tool that checks it, and what it proves."""

    # Either a link to the artifact — the file at a named commit of this
    # repository (`https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/
    # proofs/cards/BarySign.lean`) or a declaration on lean-categories main —
    # or a repository-relative path with the `proofs/` prefix, for the Sage
    # and GAP certificates that still live here.
    file: str
    # `Lean`, `exact Sage` or `exact GAP`.
    tool: str
    # Which claim of the card this artifact proves: `the statement` for the
    # card's whole statement, `part` for one claim of a statement that has
    # several. The row's `What it proves` cell names the part.
    covers: str


def tool_of(file: str) -> str | None:
    return TOOLS.get(Path(urlsplit(file).path).suffix)


def status(review: str, certificates: tuple[Certificate, ...]) -> str:
    """The three-way status a page states, from the card's own two sources.

    A row proving part of the card's statement does not make the card
    certified: certification is a claim about the whole statement, and a card
    whose proof is split across rows that each prove a part stays `draft` (or
    `reviewed`) until one row records the whole statement. That is the
    conservative direction, and the tables are authored, so the author is who
    supplies the missing row.

    `review: verified` is reserved and currently unpopulated; it is a level of
    review above draft, so it reads as `reviewed` rather than disappearing.
    """
    if any(entry.covers == THE_STATEMENT for entry in certificates):
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
    for card_id, file, covers in _rows(readme.read_text().splitlines()):
        tool = tool_of(file)
        if tool is None:
            continue
        # A link names its own home; a path is repository-relative.
        where = file if file.startswith("https://") else f"proofs/{file}"
        certificate = Certificate(file=where, tool=tool, covers=covers)
        entries = rows.setdefault(card_id, [])
        if certificate not in entries:
            entries.append(certificate)
    return {card_id: tuple(entries) for card_id, entries in rows.items()}


def exists(root: Path, file: str) -> bool:
    """Whether the link's target exists.

    A section 1 row links a file at a named commit of this repository or a
    declaration on lean-categories main: the file is looked up in this clone's
    own history, and the declaration over HTTP against its main. A section 2
    row names a file of the working tree.
    """
    if file.startswith(THIS_REPOSITORY):
        ref, _, path = file[len(THIS_REPOSITORY) :].partition("/")
        return _commit_has(root, ref, urlsplit(path).path)
    if file.startswith(LEAN_CATEGORIES):
        return _reachable(file)
    return (root / file).is_file()


def _commit_has(root: Path, ref: str, path: str) -> bool:
    """The path exists at `ref` in this clone's own history, which is
    authoritative for it; no other source is consulted when it is absent."""
    result = subprocess.run(
        ["git", "-C", str(root), "cat-file", "-e", f"{ref}:{path}"],
        capture_output=True,
    )
    return result.returncode == 0


def _reachable(url: str) -> bool:
    """The URL answers 200, so the link's target exists on its main."""
    request = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return response.status == 200
    except urllib.error.HTTPError:
        return False
    except (urllib.error.URLError, TimeoutError):
        return False


def _rows(lines: list[str]) -> list[tuple[str, str, str]]:
    """Every (card id, `cards/...` path, coverage) triple the certificate tables state.

    The coverage is the row's `Covers` cell, normalised to one of `COVERS`, or
    the empty string when the row carries no such cell. It is the last cell of
    the row in all three table shapes, which is why the file cell is looked for
    over the whole row rather than in a fixed column.
    """
    out: list[tuple[str, str, str]] = []
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
        exact = [cell for cell in cells if _FILE.fullmatch(cell.strip("`<>"))]
        file = exact[0].strip("`<>") if exact else standing
        if file is None:
            continue
        covers = _covers(cells)
        out.extend((card_id, file, covers) for card_id in card_ids)
    return out


def _covers(cells: list[str]) -> str:
    """The row's `Covers` cell, as one of `COVERS`, or `""` when it has none."""
    if not cells:
        return ""
    last = cells[-1].strip("`*_ ~").lower()
    return last if last in COVERS else ""


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
