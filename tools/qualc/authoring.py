"""Live card addressing, authored collection traversal, and source context."""

from __future__ import annotations

import argparse
import csv
import random
import re
import subprocess
import sys
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from functools import cache, cached_property
from pathlib import Path
from typing import TypeVar

import yaml
from pydantic import TypeAdapter

from . import certificates as certificate
from .emit import _collection_source_links, compile_tikzcd_block
from .model import FRONT_MATTER, MARKDOWN, Card, CollectionCard, CompilationSource, ExamSource, HomeworkSource, Strict, TextbookSource, discover, load_front_matter, parse_card, parse_cards, split_front_matter, unread_math, validate_fenced_divs
from .pandoc_batch import PandocFailure, PandocServer
from .publication import PublicationManifest
from .tex import mark_definienda

CARD_ADAPTER: TypeAdapter[Card] = TypeAdapter(Card)
ID_FIELD = re.compile(r"^(id|'id'|\"id\")\s*:")
# A card's dated events, whose text QUAL-11 makes a record rather than authored prose.
AUDIT_BLOCK = re.compile(r"^(?P<indent>[ \t]*)audit:[ \t]*$", re.MULTILINE)
TIKZCD = re.compile(r"\\begin\{tikzcd\}.*?\\end\{tikzcd\}", re.DOTALL)
# STYLE-03: every blackboard-bold object has a semantic macro in vocabularies/macros.json,
# so the display choice for each meaning is made once in the preamble.
RAW_BLACKBOARD = re.compile(r"\\(?:mathbb|Bbb)(?![A-Za-z])")
# STYLE-02: math is delimited with dollars; `\\[` (a line break with spacing) is not a delimiter.
BACKSLASH_DELIMITER = re.compile(r"(?<!\\)\\[\[\]()]")
# STYLE-04: a definitional equality is `\coloneqq`; `\definedas` is its alias.
DEFINEDAS = re.compile(r"\\definedas(?![A-Za-z])")
# STYLE-04: a bar in mathematics has one semantic macro per meaning (`\abs`, `\norm`,
# `\cardinality`, `\st`, `\divides`, ...), so a raw bar glyph is never authored.
BAR_GLYPHS = frozenset({"|", "\\|", "\\vert", "\\Vert", "\\lvert", "\\rvert", "\\lVert", "\\rVert"})
BAR_SIZES = frozenset({"\\left", "\\right", "\\middle"} | {f"\\{size}{side}" for size in ("big", "Big", "bigg", "Bigg") for side in ("", "l", "r", "m")})
# Pandoc's tex_math_dollars: `$$` displays, and `$` spans whose opener is not followed and
# whose closer is not preceded by whitespace, and whose closer is not followed by a digit.
MATH_SPAN = re.compile(r"\$\$(?P<display>.+?)\$\$|\$(?![\s$])(?P<inline>(?:[^$\\]|\\.)+?)(?<!\s)\$(?!\d)", re.DOTALL)
CODE = re.compile(r"^(?P<fence>```+|~~~+).*?^(?P=fence)[ \t]*$|(?P<ticks>`+)(?!`).+?(?<!`)(?P=ticks)(?!`)", re.DOTALL | re.MULTILINE)
TEX_TOKEN = re.compile(r"\\(?:[A-Za-z]+|.)|.", re.DOTALL)
# A link target the wiki resolver reads as a card id: a bare name, no directory, in the
# uppercase-prefix shape every corpus id has (`P-QJ7MD`, `E-SS1.EX-19`, `SRC-UCLA-RA-FALL-2010`).
LINK_TARGET = re.compile(r"\[\[(?P<wiki>[^\]|#]+)|\]\((?P<markdown>[^)\s#]+)")
CARD_ID_SHAPE = re.compile(r"^[A-Z][A-Z0-9]*-[A-Za-z0-9._-]+$")


@dataclass(frozen=True)
class BarToken:
    """One bar glyph in a math span, with any `\\left`/`\\big`-style size prefix, as offsets into the span."""

    start: int
    end: int
    text: str


def math_spans(text: str) -> list[tuple[int, int]]:
    """Offsets of the contents of each dollar-delimited math span outside code."""
    spans: list[tuple[int, int]] = []
    position = 0
    while (match := MATH_SPAN.search(text, position)) is not None:
        code = CODE.search(text, position)
        if code is not None and code.start() < match.start():
            position = code.end()
            continue
        if match.start() > 0 and text[match.start() - 1] == "\\":
            position = match.start() + 1
            continue
        group = "display" if match["display"] is not None else "inline"
        if group == "inline" and re.search(r"\n[ \t]*\n", match[group]):
            position = match.start() + 1
            continue
        spans.append((match.start(group), match.end(group)))
        position = match.end()
    return spans


def bar_tokens(math: str) -> list[BarToken]:
    """Raw bar glyphs in one math span, outside tikzcd diagrams and array column specifications.

    Tokenizes as TeX does: a control word, a control symbol, or one character, so `\\\\|`
    is a line break followed by a bar and `\\|` is the double-bar control symbol.
    """
    tokens = [(match.start(), match.end(), match.group()) for match in TEX_TOKEN.finditer(math)]
    bars: list[BarToken] = []
    skip_until = -1
    index = 0
    while index < len(tokens):
        start, end, text = tokens[index]
        if start < skip_until:
            index += 1
            continue
        if text == "\\begin":
            environment = re.match(r"\s*\{(\w+\*?)\}", math[end:])
            if environment and environment[1] == "tikzcd":
                close = math.find("\\end{tikzcd}", end)
                skip_until = len(math) if close < 0 else close
            elif environment and environment[1] in ("array", "tabular"):
                spec = re.match(r"\s*\{\w+\*?\}\s*(?:\[[^\]]*\]\s*)?\{(?:[^{}]|\{[^{}]*\})*\}", math[end:])
                if spec:
                    skip_until = end + spec.end()
        elif text in BAR_SIZES:
            glyph = index + 1
            while glyph < len(tokens) and tokens[glyph][2].isspace():
                glyph += 1
            if glyph < len(tokens) and tokens[glyph][2] in BAR_GLYPHS:
                bars.append(BarToken(start, tokens[glyph][1], math[start : tokens[glyph][1]]))
                index = glyph + 1
                continue
        elif text in BAR_GLYPHS:
            bars.append(BarToken(start, end, text))
        index += 1
    return bars


def raw_notation(source: str) -> str | None:
    """The first STYLE-04 raw form in a card or page source, or None."""
    if raw := DEFINEDAS.search(source):
        return f"{raw.group()} is written \\coloneqq (STYLE-04)"
    for start, end in math_spans(source):
        if bars := bar_tokens(source[start:end]):
            return f"raw bar {bars[0].text!r} in ${source[start:end]}$ is written with the semantic macro for its meaning (STYLE-04)"
    return None


def card_header(text: str, path: Path) -> Card:
    """Validate one authored header and its fence balance without Pandoc or other cards."""
    try:
        meta, body = split_front_matter(text, path)
        validate_fenced_divs(body, text[: len(text) - len(body)].count("\n") + 1)
        return CARD_ADAPTER.validate_python(meta)
    except (ValueError, TypeError, yaml.YAMLError) as exc:
        raise ValueError(f"{path}: {exc}") from exc


def unread_math_errors(bodies: list[tuple[Path, str]]) -> list[str]:
    """Read the changed bodies in one Pandoc batch and report each dollar the reader left as text."""
    if not bodies:
        return []
    with PandocServer() as pandoc:
        results = pandoc.read_markdown([body for _, body in bodies], MARKDOWN)
    errors: list[str] = []
    for (path, _), result in zip(bodies, results, strict=True):
        if isinstance(result, PandocFailure):
            errors.append(f"{path}: {result.error}")
        elif diagnostic := unread_math(result.output, path):
            errors.append(f"{path}: {diagnostic.detail}")
    return errors


class GitChange(Strict):
    path: Path
    version: str


# `model.AuditEvent`'s fields, in the order a refusal names them.
AUDIT_FIELDS = ("event", "by", "date", "note")
# Dated records outside the corpus: the root complaints file's sections and paragraphs.
COMPLAINTS = Path("COMPLAINTS.md")
# The paths whose blobs the card gate validates and whose deletions it reads.
CHECKED_PATHS = ("corpus/", "wiki/", COMPLAINTS.as_posix())
DAY = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
HEADING = re.compile(r"^(?P<marks>#{1,6})\s")
# A section record begins with its own day; a paragraph or numbered item states it
# first in the bold or italic lead that opens it.
SECTION_DAY = re.compile(r"^#{1,6}\s+(\d{4}-\d{2}-\d{2}):")
NUMBERED = re.compile(r"^(?P<indent>[ \t]*)\d+\.\s")
# The three restored section headings carry their own day mid-title. No other heading
# is read this way: every other section record states its day first.
RESTORED_SECTIONS: dict[str, date] = {
    "## `SRC-TEXT-HART77`: the #121 pass of 2026-11-15, the cards listed, and what the sources outside the retained sets proved": date(2026, 11, 15),
    "## `SRC-TEXT-HART77` #121: the remaining cards against the MinerU text versions, second pass (2026-11-15)": date(2026, 11, 15),
    "## `SRC-TEXT-HART77` #121: the third pass of 2026-11-15, four repairs and the next two cards": date(2026, 11, 15),
}


@dataclass(frozen=True)
class AuditRecord:
    """One `audit:` event as the text it records, with the day it carries.

    Comparing these rather than the YAML lets a re-serialised header pass: what may not
    change is what an event says, not how its block is laid out.
    """

    day: date | None
    text: tuple[str, ...]


def source_identity(source: str) -> str | None:
    """The scalar id in a card's front matter, read without validating the rest of it.

    A deleted blob is read for the card it held, so its other defects are not this
    gate's to report; a header whose id line does not parse raises, and only a header
    with no id line, or with an id that is not a nonempty scalar, has no identity.
    """
    match = FRONT_MATTER.match(source)
    if match is None:
        return None
    for line in match["front"].splitlines():
        if ID_FIELD.match(line):
            parsed = yaml.load(line, Loader=yaml.CSafeLoader)
            value = parsed.get("id") if isinstance(parsed, dict) else None
            return value if isinstance(value, str) and value else None
    return None


def _audit_day(event: object) -> date | None:
    value = event.get("date") if isinstance(event, dict) else None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            return None
    return None


def _audit_text(event: object) -> tuple[str, ...]:
    """An event's four fields as text. A field that is gone keeps its own spelling, so
    deleting it from an event is a change and not a silent match."""
    values: list[str] = []
    for field in AUDIT_FIELDS:
        if not isinstance(event, dict) or field not in event:
            values.append(f"<no {field}>")
        elif event[field] is None:
            values.append("")
        elif isinstance(event[field], datetime):
            values.append(event[field].isoformat()[:10])
        elif isinstance(event[field], date):
            values.append(event[field].isoformat())
        else:
            values.append(str(event[field]))
    return tuple(values)


def audit_records(source: str) -> list[AuditRecord]:
    """A card's `audit:` events, in the order authored, read from its front matter.

    A card the gate accepted carries a `date` its schema parsed, so an event with no
    readable day can only come from a commit made outside the gate: it has no day to
    compare, and the commit that touches that card reports the header defect instead.
    """
    match = FRONT_MATTER.match(source)
    if match is None:
        return []
    try:
        front = load_front_matter(match["front"])
    except yaml.YAMLError:
        # A header that is not YAML is `card_header`'s to report; nothing is compared here.
        return []
    events = front.get("audit") if isinstance(front, dict) else None
    if not isinstance(events, list):
        return []
    return [AuditRecord(day=_audit_day(event), text=_audit_text(event)) for event in events]


def authored_prose(source: str) -> str:
    """A card's source without its `audit:` block.

    STYLE-02 to STYLE-04 govern what a session writes now, and a dated event is text no
    session may rewrite (QUAL-11): the rule applied to it would demand the rewrite the
    other rule forbids. So the checks read the header's other fields and the body, and
    leave the events as the sessions of their day wrote them.
    """
    match = AUDIT_BLOCK.search(source)
    if match is None:
        return source
    lines = source[match.end() :].splitlines(keepends=True)
    end = len(lines)
    for index, line in enumerate(lines):
        if line.strip() and not line.startswith((" ", "\t", "- ")):
            end = index
            break
    return source[: match.start()] + "".join(lines[end:])


def earlier_versions(path: Path, revision: str) -> list[str]:
    """The text of `path` at each earlier revision of it, newest first."""
    revisions = subprocess.run(["git", "log", "--format=%H", revision, "--", path.as_posix()], check=True, stdout=subprocess.PIPE, text=True).stdout.split()
    return [previous_source(path, earlier) for earlier in revisions]


def _folded(text: str) -> str:
    """A record's text with its whitespace folded, so a wrapped note is the same note."""
    return " ".join(text.split())


RecordIdentity = TypeVar("RecordIdentity")


def introduced_record_texts(
    path: Path,
    revision: str,
    identity: RecordIdentity,
    records: Callable[[str], list[tuple[RecordIdentity, str]]],
) -> Counter[str]:
    """The texts introduced under one identity in `path`'s history, as a multiset.

    A pure rewrite is not an introduction: texts enter this multiset only at a revision
    where the identity has more records than at the path's previous revision. Within such
    a revision, exact text matches are consumed first, as they are in the gate. Remaining
    old records then match remaining new records one-to-one in file order, representing
    rewrites of the base records; only new records left unpaired are introductions. Thus
    [A] -> [A', B] introduces B rather than A'. Texts are folded to ignore source wrapping.
    """
    introduced: Counter[str] = Counter()
    previous: list[str] = []
    for standing in reversed(earlier_versions(path, revision)):
        current = [_folded(text) for other, text in records(standing) if other == identity]
        if len(current) > len(previous):
            unused = set(range(len(current)))
            rewritten = 0
            for before_text in previous:
                match = next((index for index in sorted(unused) if current[index] == before_text), None)
                if match is None:
                    rewritten += 1
                else:
                    unused.remove(match)
            # The remaining old records pair one-to-one with replacement texts. Count growth
            # leaves at least this many new records, and exactly those left over are introduced.
            for index in sorted(unused)[:rewritten]:
                unused.remove(index)
            introduced += Counter(current[index] for index in sorted(unused))
        previous = current
    return introduced


def introduced_event_notes(path: Path, revision: str, identity: tuple[date, str, str]) -> Counter[str]:
    """The audit notes introduced under this day, kind and author in the path's history."""
    return introduced_record_texts(
        path,
        revision,
        identity,
        lambda source: [((record.day, record.text[0], record.text[1]), record.text[3]) for record in audit_records(source)],
    )


def introduced_complaint_records(path: Path, revision: str, day: date) -> Counter[str]:
    """The COMPLAINTS texts introduced under this day in the path's history."""
    return introduced_record_texts(path, revision, day, dated_records)


def unmatched_record_indices(
    before: list[tuple[RecordIdentity, str]],
    after: list[tuple[RecordIdentity, str]],
    introduced: Callable[[RecordIdentity], Counter[str]],
) -> tuple[list[int], list[RecordIdentity]]:
    """Old records not preserved or restored, and repeated identities among them.

    For each identity, the new records accept the base records when they contain them as
    a multiset, including an unchanged reorder. Otherwise they are a restoration only
    when they contain every text ever introduced under that identity. A group meeting
    neither condition loses every old record without an exact match. Repeated identities
    receive the existing additional diagnostic, but repetition alone no longer refuses
    the comparison: the whole introduction multiset is what distinguishes a restoration
    from [A, B] -> [B, A] -> [B, B], where A is missing.
    """
    unused = set(range(len(after)))
    lost: list[int] = []
    for index, (identity, text) in enumerate(before):
        match = next((other for other in unused if after[other][0] == identity and _folded(after[other][1]) == _folded(text)), None)
        if match is None:
            lost.append(index)
        else:
            unused.remove(match)

    before_counts = Counter(identity for identity, _ in before)
    after_counts = Counter(identity for identity, _ in after)
    after_texts: dict[RecordIdentity, Counter[str]] = {}
    for identity, text in after:
        after_texts.setdefault(identity, Counter())[_folded(text)] += 1
    lost_identities = dict.fromkeys(before[old][0] for old in lost)
    restored: set[RecordIdentity] = set()
    for identity in lost_identities:
        introduced_texts = introduced(identity)
        # No earlier introduction is no evidence that replacement text is a restoration.
        if introduced_texts and introduced_texts <= after_texts.get(identity, Counter()):
            restored.add(identity)
    ambiguous = [identity for identity in lost_identities if identity not in restored and (before_counts[identity] > 1 or after_counts[identity] > 1)]
    return [index for index in lost if before[index][0] not in restored], ambiguous


def rewritten_audit_events(path: Path, before: str, after: str, day: date, introduced: Callable[[tuple[date, str, str]], Counter[str]]) -> list[str]:
    """Audit events dated before the commit whose text it changes or removes (QUAL-11).

    An event dated before the commit records what a session found on that day, and the
    events after it refer to that text; a later correction is a new event dated the
    commit's date, so the earlier record keeps meaning what it said. Events dated the
    commit's own day are still in flight and may be edited, an appended event is always
    accepted, and an event restored to a note that stood for that event in an earlier
    revision of the path is the repair QUAL-11 asks for rather than a rewrite of it —
    which is why an edit made in place earlier in the branch can still be undone.

    A day, a kind and an author do not identify an event when a card states two of them.
    The comparison therefore judges each identity's whole multiset against the base or
    the texts introduced in the path's history, rather than assigning occurrences by order.
    """
    before_records = [
        ((record.day, record.text[0], record.text[1]), record.text[3])
        for record in audit_records(before)
        if record.day is not None and record.day < day
    ]
    after_records = [
        ((record.day, record.text[0], record.text[1]), record.text[3])
        for record in audit_records(after)
        if record.day is not None
    ]
    errors: list[str] = []
    unmatched, ambiguous = unmatched_record_indices(before_records, after_records, introduced)
    for record_day, kind, by in ambiguous:
        errors.append(f"{path}: multiple dated audit events share one identity ({kind}, {by}, {record_day}); their earlier texts cannot be distinguished, so the comparison is refused (QUAL-11)")
    for index in unmatched:
        (record_day, kind, by), note = before_records[index]
        said = f", whose note begins {excerpt!r}," if (excerpt := " ".join(note.split())[:60]) else ""
        errors.append(f"{path}: the {kind} event by {by} dated {record_day}{said} was changed or deleted; a dated event records what that session found, so a correction is a new event dated {day} (QUAL-11)")
    return errors


def opening_lead(block: str) -> str:
    """The bold or italic run that opens a paragraph or numbered item, with its markers."""
    text = block.lstrip()
    if item := NUMBERED.match(text):
        text = text[item.end() :]
    for marker in ("**", "*"):
        if text.startswith(marker):
            end = text.find(marker, len(marker))
            if end != -1:
                return text[: end + len(marker)]
    return ""


def _record_day(found: re.Match[str] | None) -> date | None:
    """The day a match carries, or None when the shape is a day's and the value is not."""
    if found is None:
        return None
    try:
        return date.fromisoformat(found[1])
    except ValueError:
        return None


def _blocks(lines: list[str]) -> list[tuple[int, int]]:
    """The line ranges of the blank-line-separated blocks of a Markdown file."""
    blocks: list[tuple[int, int]] = []
    start: int | None = None
    for index, line in enumerate(lines):
        if line.strip():
            if start is None:
                start = index
        elif start is not None:
            blocks.append((start, index))
            start = None
    if start is not None:
        blocks.append((start, len(lines)))
    return blocks


def _item_end(lines: list[str], start: int, indent: int) -> int:
    """The line after the last line a numbered item holds.

    A continuation paragraph and every bullet under the item are indented past the
    item's own marker, and they are the evidence the item records; a heading, the next
    item at that indentation, and a block outside it end the item instead. A line that
    follows the item's text without a blank line is a lazy continuation, which Markdown
    keeps in the item.
    """
    end = start + 1
    blank = False
    for index in range(start + 1, len(lines)):
        line = lines[index]
        if HEADING.match(line):
            break
        if not line.strip():
            blank = True
            continue
        inner = NUMBERED.match(line)
        if (inner is not None and len(inner["indent"]) <= indent) or (blank and len(line) - len(line.lstrip()) <= indent):
            break
        blank = False
        end = index + 1
    return end


def dated_records(source: str) -> list[tuple[date, str]]:
    """Each dated COMPLAINTS record, with its own day and its text.

    A section record begins with its day (`## 2026-11-16: ...`) and runs to the next
    heading of the same or a higher rank. A paragraph states its day first in the bold
    or italic lead that opens it, and a numbered item is one record with everything the
    item holds: its continuation paragraphs and the bullets indented under it are the
    evidence it records, so they are part of it and not free text beside it, and the
    items of a list are records one by one even where no blank line separates them. A
    day the record merely mentions follows its own, and a lead that carries no day
    records none, so the bullets of an entry are not records in their own right. A
    heading states its day first or is not a record, so no day is read out of the middle
    of a title except through the three exact headings named by `RESTORED_SECTIONS`.
    """
    lines = source.splitlines()
    headings = [(index, len(match["marks"])) for index, line in enumerate(lines) if (match := HEADING.match(line))]
    records: list[tuple[date, str]] = []
    for position, (start, level) in enumerate(headings):
        day = _record_day(SECTION_DAY.match(lines[start])) or RESTORED_SECTIONS.get(lines[start])
        if day is None:
            continue
        end = len(lines)
        for later, later_level in headings[position + 1 :]:
            if later_level <= level:
                end = later
                break
        records.append((day, "\n".join(lines[start:end]).strip()))
    for start, line in enumerate(lines):
        item = NUMBERED.match(line)
        if item is None:
            continue
        day = _record_day(DAY.search(opening_lead(line)))
        if day is not None:
            records.append((day, "\n".join(lines[start : _item_end(lines, start, len(item["indent"]))]).strip()))
    for start, end in _blocks(lines):
        if NUMBERED.match(lines[start]):
            continue
        day = _record_day(DAY.search(opening_lead("\n".join(lines[start:end]))))
        if day is not None:
            records.append((day, "\n".join(lines[start:end]).strip()))
    return records


def rewritten_complaint_records(path: Path, before: str, after: str, day: date, introduced: Callable[[date], Counter[str]]) -> list[str]:
    """Dated COMPLAINTS records a commit changes or deletes (QUAL-11).

    A record dated before the commit is kept as it stands; text appended after it leaves
    it intact, and editing a word of it or removing it does not. A record dated the
    commit's own day is still in flight, and a record restored to the text it carried on
    its day — text that stands in an earlier revision of this file — is that repair.

    Records that share a day use the same multiset comparison as audit events: the day
    is the whole of what identifies them, and a partial restoration cannot excuse a loss.
    """
    before_records = [(record_day, text) for record_day, text in dated_records(before) if record_day < day]
    after_records = dated_records(after)
    errors: list[str] = []
    unmatched, ambiguous = unmatched_record_indices(before_records, after_records, introduced)
    for record_day in ambiguous:
        errors.append(f"{path}: multiple dated COMPLAINTS records share one identity ({record_day}); their earlier texts cannot be distinguished, so the comparison is refused (QUAL-11)")
    for index in unmatched:
        record_day, text = before_records[index]
        said = " ".join(text.split())[:60]
        errors.append(f"{path}: the record dated {record_day}, beginning {said!r}, was changed or deleted; a dated record states what that day found, so a correction is a new record dated {day} (QUAL-11)")
    return errors


def commit_day(version: str) -> date:
    """The calendar day Git records for the commit being validated.

    The staged index holds no commit yet, so this is the day Git is about to write.
    `git var GIT_COMMITTER_IDENT` is Git's own parse of `GIT_COMMITTER_DATE` — the raw
    `<epoch> <zone>`, ISO 8601 and RFC 2822 forms alike — and prints the timestamp with
    the zone the commit records, so the day is that zone's. A committed candidate
    carries its own committer date.
    """
    if version != "index":
        stamp = subprocess.run(["git", "log", "-1", "--format=%cI", version], check=True, stdout=subprocess.PIPE, text=True).stdout.strip()
        return datetime.fromisoformat(stamp).date()
    ident = subprocess.run(["git", "var", "GIT_COMMITTER_IDENT"], check=True, stdout=subprocess.PIPE, text=True).stdout
    stamp, zone = ident.split()[-2:]
    offset = timedelta(hours=int(zone[1:3]), minutes=int(zone[3:5]))
    if zone[0] == "-":
        offset = -offset
    return (datetime.fromtimestamp(int(stamp), timezone.utc) + offset).date()


def empty_tree() -> str:
    """The empty tree's object id: the base of a root commit and of an unborn branch."""
    return subprocess.run(["git", "hash-object", "-w", "-t", "tree", "/dev/null"], check=True, stdout=subprocess.PIPE, text=True).stdout.strip()


def head_commit() -> str:
    """The commit HEAD names, or the empty tree while the branch has no commit."""
    listed = subprocess.run(["git", "rev-list", "--max-count=1", "HEAD"], capture_output=True, text=True)
    if listed.returncode == 0 and listed.stdout.strip():
        return listed.stdout.strip()
    if subprocess.run(["git", "symbolic-ref", "-q", "HEAD"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
        return empty_tree()
    raise ValueError("HEAD names no commit and is not an unborn branch")


def commit_parents(commit: str) -> list[str]:
    """A commit's parents in order; a root commit has none."""
    return subprocess.run(["git", "rev-list", "--parents", "--max-count=1", commit], check=True, stdout=subprocess.PIPE, text=True).stdout.split()[1:]


def merge_authored_paths(commit: str, parents: list[str]) -> list[str]:
    """The checked paths a merge commit authored, rather than carried from a parent.

    A path whose merged blob equals one parent's is that parent's change, judged by that
    parent's own commit: upstream when it was published, or earlier in the same replay.
    `git diff-tree -c` lists the paths that differ from every parent (git-diff-tree,
    "combined diff format"). Of those, a path that Git's own automatic merge of the two
    parents (`git merge-tree --write-tree`, git-merge-tree) resolves to the same blob was
    merged textually, each hunk taken from one side, so it is carried too. What is left
    is a conflict resolution or an edit made in the merge, and that is the merge's own.
    """
    combined = subprocess.run(["git", "diff-tree", "-c", "-r", "--no-commit-id", "--name-only", "-z", commit, "--", *CHECKED_PATHS], check=True, stdout=subprocess.PIPE, text=True).stdout
    paths = [name for name in combined.split("\0") if name]
    if len(parents) != 2 or not paths:
        return paths
    # Exit status 1 is a conflicted automatic merge; its tree, with markers, is still written.
    automatic = subprocess.run(["git", "merge-tree", "--write-tree", *parents], stdout=subprocess.PIPE, text=True)
    if automatic.returncode not in (0, 1):
        raise ValueError(f"git merge-tree could not merge the parents of {commit}")
    merged = tree_blobs(commit, paths)
    resolved = tree_blobs(automatic.stdout.split("\n", 1)[0], paths)
    return [path for path in paths if merged.get(path) != resolved.get(path)]


def tree_blobs(revision: str, paths: list[str]) -> dict[str, str]:
    """The blob id at each of `paths` that `revision`'s tree holds."""
    listing = subprocess.run(["git", "ls-tree", "-r", "-z", revision, "--", *paths], check=True, stdout=subprocess.PIPE, text=True).stdout
    return {name: fields.split()[2] for fields, name in (record.split("\t", 1) for record in listing.split("\0") if record)}


def upstream_commit() -> str:
    """The commit `@{upstream}` names; the push gate publishes above it."""
    result = subprocess.run(["git", "rev-parse", "--verify", "--quiet", "@{upstream}"], capture_output=True, text=True)
    if result.returncode != 0:
        raise ValueError("the push gate needs the branch's upstream to know which commits the push publishes; set branch.<name>.remote and branch.<name>.merge")
    return result.stdout.strip()


def pushed_commits(tip: str) -> list[str]:
    """The commits a push publishes, oldest first."""
    merged = subprocess.run(["git", "merge-base", tip, upstream_commit()], check=True, stdout=subprocess.PIPE, text=True).stdout.strip()
    return subprocess.run(["git", "rev-list", "--reverse", f"{merged}..{tip}"], check=True, stdout=subprocess.PIPE, text=True).stdout.split()


def previous_source(path: Path, revision: str) -> str:
    """The text at `path` in `revision`, or the empty text when that tree has no such path.

    Absence is `ls-tree`'s empty listing. A revision that does not resolve, and any
    other Git failure, raises: only a readable tree with no such path is an empty
    source.
    """
    listed = subprocess.run(["git", "ls-tree", "-z", revision, "--", path.as_posix()], check=True, stdout=subprocess.PIPE, text=True).stdout
    if not listed:
        return ""
    return subprocess.run(["git", "show", f"{revision}:{path.as_posix()}"], check=True, stdout=subprocess.PIPE, text=True).stdout


def version_source(path: Path, version: str) -> str:
    """The text at `path` in this version's tree, read from the index for a staged commit."""
    revision = "" if version == "index" else version
    return subprocess.run(["git", "show", f"{revision}:{path.as_posix()}"], check=True, stdout=subprocess.PIPE, text=True).stdout


def changed_card_sources(version: str, base: str, scope: tuple[str, ...] = ("corpus/", "wiki/")) -> dict[Path, str]:
    """Surviving Markdown card blobs changed in the candidate, including moves."""
    command = ["git", "diff", "--no-renames", "--name-only", "--diff-filter=ACM", "-z"]
    command.extend(["--cached", base] if version == "index" else [base, version])
    names = subprocess.run([*command, "--", *scope], check=True, stdout=subprocess.PIPE, text=True).stdout
    cards: dict[Path, str] = {}
    for name in names.split("\0"):
        if not name:
            continue
        path = Path(name)
        if path.suffix == ".md" and path.parts[0] in ("corpus", "wiki"):
            source = version_source(path, version)
            if source_identity(source) is not None:
                cards[path] = source
    return cards


AuditKey = tuple[date, str, str, str]


def dated_audit_counts(source: str, day: date) -> Counter[AuditKey]:
    """Protected events, counting repeated identical records separately."""
    return Counter(
        (record.day, record.text[0], record.text[1], _folded(record.text[3]))
        for record in audit_records(source)
        if record.day is not None and record.day < day
    )


def added_audit_counts(path: Path, before: str, after: str, base: str, day: date) -> Counter[AuditKey]:
    """The surviving card's newly carried records, after reserving its own history."""
    old = dated_audit_counts(before, day)
    new = dated_audit_counts(after, day)
    # A restored event belongs to this card already. Do not credit the same
    # occurrence both as a restoration and as a transfer from a retired card.
    changed = {key[:3] for key in old - new}
    for identity in changed:
        record_day, kind, by = identity
        previous = introduced_event_notes(path, base, (record_day, kind, by))
        reserved = Counter({(record_day, kind, by, note): count for note, count in previous.items()})
        if reserved and reserved <= new:
            for key in list(old):
                if key[:3] == identity:
                    del old[key]
            old.update(reserved)
        else:
            # No transfer can excuse loss of the surviving card's own history.
            # This also covers a move whose Git similarity pairing names a
            # different retired card rather than the surviving id's old path.
            return Counter()
    return new - old


def transfers_fit(requirements: list[Counter[AuditKey]], available: list[Counter[AuditKey]]) -> bool:
    """Assign each retired card's entire history to one survivor, without double use."""
    # Most merges have one destination. If several are possible, try them all:
    # choosing the first greedily can reject a valid simultaneous pair of merges.
    pending = [(0, available)]
    while pending:
        position, capacities = pending.pop()
        if position == len(requirements):
            return True
        required = requirements[position]
        for index, capacity in enumerate(capacities):
            if required <= capacity:
                residual = capacities.copy()
                residual[index] = capacity - required
                pending.append((position + 1, residual))
    return False


def removal_errors(version: str, base: str, scope: tuple[str, ...]) -> list[str]:
    """Dated records a commit deletes, with the path that held them (QUAL-11).

    Git's diff supplies the deleted paths even when the hook has no surviving
    path to check. A moved card retains its id and is checked at the new path.
    A CARD-04 merge retires an id but must carry its protected events into one
    surviving card; neither a pre-existing copy nor one occurrence shared by
    two retired cards constitutes a transfer. COMPLAINTS is not a card.
    """
    command = ["git", "diff", "--no-renames", "--name-only", "--diff-filter=D", "-z"]
    command.extend(["--cached", base] if version == "index" else [base, version])
    listing = subprocess.run([*command, "--", *scope], check=True, stdout=subprocess.PIPE, text=True).stdout
    if not listing:
        return []
    day = commit_day(version)
    survivors = changed_card_sources(version, base)
    surviving_ids = {source_identity(source) for source in survivors.values()}
    deleted = {Path(name): previous_source(Path(name), base) for name in listing.split("\0") if name}
    moved = {source_identity(source): path for path, source in deleted.items() if path.suffix == ".md" and source_identity(source) is not None}
    available: list[Counter[AuditKey]] = []
    for path, after in changed_card_sources(version, base, scope).items():
        if path.parts[0] != "corpus":
            continue
        card_id = source_identity(after)
        earlier = path
        before = previous_source(path, base)
        if source_identity(before) != card_id and card_id in moved:
            earlier = moved[card_id]
            before = deleted[earlier]
        # CARD-04 keeps an existing card and id, rather than creating a new card.
        if source_identity(before) == card_id:
            available.append(added_audit_counts(earlier, before, after, base, day))
    errors: list[str] = []
    pending: dict[Path, Counter[AuditKey]] = {}
    for path, before in deleted.items():
        card_id = source_identity(before)
        if card_id is not None and card_id in surviving_ids:
            continue
        if path == COMPLAINTS:
            errors.extend(rewritten_complaint_records(path, before, "", day, lambda record_day, path=path: introduced_complaint_records(path, base, record_day)))
        elif path.suffix == ".md":
            required = dated_audit_counts(before, day)
            if path.parts[0] == "corpus" and card_id is not None and required and any(required <= capacity for capacity in available):
                pending[path] = required
            else:
                errors.extend(rewritten_audit_events(path, before, "", day, lambda identity, path=path: introduced_event_notes(path, base, identity)))
    if not transfers_fit(list(pending.values()), available):
        errors.append(f"{', '.join(str(path) for path in pending)}: retired cards' dated events cannot all be transferred to surviving cards without reusing an occurrence (QUAL-11)")
    return errors


def changed_paths(version: str, base: str) -> tuple[dict[Path, Path], list[Path]]:
    """Git's rename records and deletions for one version's diff against `base`.

    A rename is one change at its new path, so the earlier text of a moved card is read
    from the path Git names as its source. The deleted paths let a move whose content
    changed below Git's similarity threshold keep the earlier text through the card's
    own id.
    """
    command = ["git", "diff", "--find-renames", "--name-status", "-z"]
    command.extend(["--cached", base] if version == "index" else [base, version])
    listing = subprocess.run([*command, "--", "corpus/", "wiki/"], check=True, stdout=subprocess.PIPE, text=True).stdout
    fields = listing.split("\0")
    moves: dict[Path, Path] = {}
    deleted: list[Path] = []
    index = 0
    while index < len(fields) and fields[index]:
        status = fields[index]
        if status[0] in "RC":
            if status[0] == "R":
                moves[Path(fields[index + 2])] = Path(fields[index + 1])
            index += 3
        else:
            if status[0] == "D":
                deleted.append(Path(fields[index + 1]))
            index += 2
    return moves, deleted


def changed_audit_events(selected: list[tuple[GitChange, str]], base: str) -> list[str]:
    """Refuse a commit that rewrites an audit event dated before it (QUAL-11)."""
    errors: list[str] = []
    for version in dict.fromkeys(change.version for change, _ in selected):
        day = commit_day(version)
        moves, deleted = changed_paths(version, base)
        retired = {card_id: path for path in deleted if (card_id := source_identity(previous_source(path, base))) is not None}
        for change, source in selected:
            if change.version != version:
                continue
            earlier = moves.get(change.path, change.path)
            if earlier == change.path and not previous_source(earlier, base) and (card_id := source_identity(source)) is not None:
                earlier = retired.get(card_id, change.path)
            errors.extend(rewritten_audit_events(change.path, previous_source(earlier, base), source, day, lambda identity, path=change.path: introduced_event_notes(path, base, identity)))
    return errors


# The audit event that records a correction of a card's mathematics (issue #111). It is
# the machine-readable marker the acceptance criterion needs: a corrected claim is
# settled only by a certificate of it, so the refusal belongs where the correction is
# recorded rather than in a reviewer's recollection, and a change that records one on a
# card no row covers for its whole statement does not commit.
SOLUTION_CORRECTED = "solution-corrected"
REGISTRY = Path("proofs/README.md")


def audit_event_kinds(source: str, path: Path) -> tuple[str, ...]:
    """The `event` of every audit entry in one card text, in authored order.

    The front matter is read, not validated: a header this reader cannot parse has no
    events to compare, and the schema check is what reports the header itself.
    """
    try:
        meta, _ = split_front_matter(source, path)
    except (TypeError, ValueError):
        return ()
    audit = meta.get("audit")
    if not isinstance(audit, list):
        return ()
    return tuple(
        entry["event"]
        for entry in audit
        if isinstance(entry, dict) and isinstance(entry.get("event"), str)
    )


def registry_at(revision: str) -> list[str]:
    """`proofs/README.md` in one revision's tree; a tree without one certifies nothing."""
    read = subprocess.run(
        ["git", "show", f"{revision}:{REGISTRY.as_posix()}"],
        capture_output=True,
        text=True,
    )
    return read.stdout.splitlines() if read.returncode == 0 else []


def corrections_without_certificates(selected: list[tuple[GitChange, str]], base: str) -> list[str]:
    """Refuse a change that records a correction and leaves the card uncertified (#111).

    The event kind is what makes this decidable: a change about mathematics says so, and
    a change about a citation or a layout does not, so the rule fires on the corrections
    the criterion names and on nothing else. What it checks is the row's presence, not
    its adequacy — the row says what it proves, and reading whether that is the corrected
    claim stays the review it always was.
    """
    errors: list[str] = []
    certified: dict[str, set[str]] = {}
    for change, source in selected:
        if change.version not in certified:
            revision = "" if change.version == "index" else change.version
            certified[change.version] = certificate.certified_statements(registry_at(revision))
        before = audit_event_kinds(previous_source(change.path, base), change.path)
        after = audit_event_kinds(source, change.path)
        if after.count(SOLUTION_CORRECTED) <= before.count(SOLUTION_CORRECTED):
            continue
        card_id = source_identity(source)
        if card_id is not None and card_id in certified[change.version]:
            continue
        errors.append(
            f"{change.path}: records a `{SOLUTION_CORRECTED}` event, and `{REGISTRY.as_posix()}` "
            f"certifies no statement for {card_id or 'this card'}: a corrected claim is settled "
            f"only by a certificate of it (#111)"
        )
    return errors


def check_git_changes(changes: list[GitChange], base: str, versions: tuple[str, ...], scope: tuple[str, ...] = CHECKED_PATHS) -> int:
    """Validate card, wiki and complaint blobs selected by the shared hook or a range check.

    Diagrams are compiled here because the site build is the only other place
    that compiles them, and a malformed one otherwise first fails the deploy.

    `base` is the revision every changed blob is compared with: the parent of the staged
    index, or the base of an outgoing range. The caller names it, because the two
    selections have different ancestors. `versions` names the trees whose deletions are
    compared with `base`; every caller names them, because the paths such a caller hands
    over are the ones that survive the change, so a commit that only deletes has none.
    `scope` limits where those deletions are read: a merge names only the paths it authored.
    """
    cards = [change for change in changes if change.path.parts[0] in ("corpus", "wiki") and change.path.suffix == ".md"]
    complaints = [change for change in changes if change.path == COMPLAINTS]
    errors: list[str] = []
    for version in versions:
        errors.extend(removal_errors(version, base, scope))
    bodies: list[tuple[Path, str]] = []
    selected: list[tuple[GitChange, str]] = []
    for change in cards:
        revision = "" if change.version == "index" else change.version
        source = subprocess.run(["git", "show", f"{revision}:{change.path.as_posix()}"], check=True, stdout=subprocess.PIPE, text=True).stdout
        try:
            if change.path.parts[0] == "corpus":
                card_header(source, change.path)
                # A header that parses is the one holding the events this commit may not rewrite.
                selected.append((change, source))
            for diagram in TIKZCD.findall(source):
                compile_tikzcd_block(diagram)
            prose = authored_prose(source)
            if raw := RAW_BLACKBOARD.search(prose):
                errors.append(f"{change.path}: {raw.group()} is written with its semantic macro (STYLE-03)")
            if raw := BACKSLASH_DELIMITER.search(prose):
                errors.append(f"{change.path}: {raw.group()} delimits math; use $...$ or $$...$$ (STYLE-02)")
            if raw := raw_notation(prose):
                errors.append(f"{change.path}: {raw}")
            bodies.append((change.path, mark_definienda(split_front_matter(source, change.path)[1])))
        except ValueError as exc:
            errors.append(str(exc))
        except RuntimeError as exc:
            errors.append(f"{change.path}: {exc}")
    errors.extend(changed_audit_events(selected, base))
    errors.extend(corrections_without_certificates(selected, base))
    for change in complaints:
        revision = "" if change.version == "index" else change.version
        source = subprocess.run(["git", "show", f"{revision}:{COMPLAINTS.as_posix()}"], check=True, stdout=subprocess.PIPE, text=True).stdout
        errors.extend(rewritten_complaint_records(COMPLAINTS, previous_source(COMPLAINTS, base), source, commit_day(change.version), lambda record_day: introduced_complaint_records(COMPLAINTS, base, record_day)))
    errors.extend(unread_math_errors(bodies))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Card YAML and schema: {len(cards) + len(complaints)} changed file(s) checked")
    return 0


def tree_sources(revision: str) -> dict[Path, str]:
    """Every corpus, wiki and publication blob at one commit, read through one `git cat-file --batch`."""
    listing = subprocess.run(["git", "ls-tree", "-r", "-z", revision, "--", "corpus/", "wiki/", "publications/"], check=True, stdout=subprocess.PIPE, text=True).stdout
    entries = [(fields.split()[2], Path(name)) for fields, name in (record.split("\t", 1) for record in listing.split("\0") if record) if name.endswith((".md", ".yaml"))]
    batch = subprocess.run(["git", "cat-file", "--batch"], input="".join(f"{oid}\n" for oid, _ in entries).encode(), check=True, stdout=subprocess.PIPE).stdout
    sources: dict[Path, str] = {}
    offset = 0
    for _, path in entries:
        header_end = batch.index(b"\n", offset)
        size = int(batch[offset:header_end].split()[2])
        sources[path] = batch[header_end + 1 : header_end + 1 + size].decode()
        offset = header_end + 2 + size
    return sources


def dangling_references(revision: str) -> list[str]:
    """References at one commit to a card id that no card at that commit carries.

    The full build reports the same references (index.validate: relations and collection
    members; emit._manifest_card: guide items; wiki.resolve_links: page links) after Pandoc
    has read every card. Here only front matter is parsed, so a card deleted by a merge
    is caught before the push instead of in the deploy.
    """
    sources = tree_sources(revision)
    ids: set[str] = set()
    referring: list[Path] = []
    for path, text in sources.items():
        if path.parts[0] != "corpus" or (match := FRONT_MATTER.match(text)) is None:
            continue
        # Only the id line is read from most headers, as `identity` does; a header that
        # names other cards is validated whole. Other header defects are the diff check's.
        lines = match["front"].splitlines()
        ids.update(yaml.load(line, Loader=yaml.CSafeLoader)["id"] for line in lines if ID_FIELD.match(line))
        if "kind: collection" in lines or any(line.startswith("relations:") and line != "relations: []" for line in lines):
            referring.append(path)
    page_stems = {path.stem.lower() for path in sources if path.parts[0] == "wiki"}
    errors: list[str] = []
    for path in referring:
        try:
            card = card_header(sources[path], path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        errors.extend(f"{path}: relation target {relation.target!r} has no card" for relation in card.relations if relation.target not in ids)
        if isinstance(card, CollectionCard):
            source = card.source
            problems = source.problems if isinstance(source, (ExamSource, HomeworkSource, CompilationSource)) else []
            sections = source.sections if isinstance(source, (TextbookSource, CompilationSource)) else []
            errors.extend(f"{path}: lists {entry.id!r}, which has no card" for entry in [*problems, *(entry for section in sections for entry in section.problems)] if entry.id not in ids)
    for path, text in sources.items():
        if path.parts[0] == "publications":
            manifest = PublicationManifest.model_validate(yaml.load(text, Loader=yaml.CSafeLoader))
            errors.extend(f"{path}: {section.slug} names {item.ref!r}, which has no card" for section in manifest.sections for item in section.items if item.ref not in ids)
        elif path.suffix == ".md":
            for match in LINK_TARGET.finditer(text):
                target = (match["wiki"] or match["markdown"]).strip()
                if CARD_ID_SHAPE.match(target) and target not in ids and target.lower() not in page_stems:
                    errors.append(f"{path}: links {target!r}, which has no card")
    return errors


def check_references(revisions: list[str]) -> int:
    """Run `dangling_references` at each selected commit that no other selected commit descends from."""
    tips = subprocess.run(["git", "merge-base", "--independent", *revisions], check=True, stdout=subprocess.PIPE, text=True).stdout.split()
    errors = [f"{tip[:12]} {error}" for tip in tips for error in dangling_references(tip)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Card references: {len(tips)} outgoing tip(s) resolve")
    return 0


def check_git_cards(version: str, diff_args: tuple[str, ...], base: str) -> int:
    """Validate Git blobs selected by diff, including Git's temporary commit index.

    Git's diff --name-only -z and show :path / revision:path interfaces own
    selection and blob transport (git-diff and gitrevisions manuals).
    """
    names = subprocess.run(
        ["git", "diff", "--name-only", "--no-renames", "--diff-filter=ACM", "-z", *diff_args, "--", *CHECKED_PATHS],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout
    return check_git_changes([GitChange(path=Path(name), version=version) for name in names.split("\0") if name], base, (version,))


def check_pushed_commits(tip: str) -> int:
    """Validate each published commit against its own parent and its own day (QUAL-11).

    The shared hook names only the tip of each pushed ref, so the commits between the
    upstream and the tip are replayed one at a time: a rewrite made by an earlier commit
    is refused even when a later commit restores the text, and an edit is judged by the
    day of the commit that made it.

    A merge is judged only on the paths it authored (`merge_authored_paths`), against
    each parent in turn: replayed against its first parent alone, a merge of the
    upstream presents every published change as its own, on the merge's day.
    """
    failed = 0
    for commit in pushed_commits(tip):
        parents = commit_parents(commit)
        if len(parents) < 2:
            base = parents[0] if parents else empty_tree()
            names = subprocess.run(
                ["git", "diff", "--name-only", "--no-renames", "--diff-filter=ACM", "-z", base, commit, "--", *CHECKED_PATHS],
                check=True,
                stdout=subprocess.PIPE,
                text=True,
            ).stdout
            failed |= check_git_changes([GitChange(path=Path(name), version=commit) for name in names.split("\0") if name], base, (commit,))
            continue
        authored = merge_authored_paths(commit, parents)
        if not authored:
            continue
        present = subprocess.run(["git", "ls-tree", "-r", "-z", "--name-only", commit, "--", *authored], check=True, stdout=subprocess.PIPE, text=True).stdout
        changes = [GitChange(path=Path(name), version=commit) for name in present.split("\0") if name]
        for parent in parents:
            failed |= check_git_changes(changes, parent, (commit,), tuple(authored))
    return failed


@dataclass(frozen=True)
class Location:
    collection: CollectionCard
    section: str
    position: int
    comment: str | None

    def label(self) -> str:
        parts = [self.collection.id, self.section, f"entry {self.position}"]
        if self.comment is not None:
            parts.append(self.comment)
        return " / ".join(part for part in parts if part)


@dataclass(frozen=True)
class Appearance:
    card_id: str
    locations: tuple[Location, ...]


def identity(path: Path) -> str | None:
    """Read only the authored scalar id field, even during edits to other fields.

    Corpus IDs occupy one top-level YAML line. No body parsing or filename-based
    identity inference is needed to address a card that is being edited.
    """
    with path.open() as stream:
        if stream.readline() != "---\n":
            return None
        for line in stream:
            if line.rstrip() == "---":
                break
            if ID_FIELD.match(line):
                value = yaml.load(line, Loader=yaml.CSafeLoader)["id"]
                if not isinstance(value, str) or not value:
                    raise ValueError(f"{path}: id must be a nonempty scalar on one YAML line")
                return value
    return None


class Corpus:
    def __init__(self, root: Path):
        self.root = root.resolve()

    @cached_property
    def addresses(self) -> dict[str, list[Path]]:
        addresses: dict[str, list[Path]] = {}
        for path in discover(self.root / "corpus"):
            card_id = identity(path)
            if card_id is not None:
                if card_id not in addresses:
                    addresses[card_id] = []
                addresses[card_id].append(path)
        return addresses

    def resolve(self, reference: str) -> Path:
        path = self.root / reference
        if path.is_dir():
            path = path / "index.md"
        if not path.is_file():
            if reference not in self.addresses:
                raise ValueError(f"Cannot resolve card ID or corpus path: {reference}")
            matches = self.addresses[reference]
            if len(matches) != 1:
                raise ValueError(f"Ambiguous card ID {reference}: {', '.join(map(str, matches))}")
            path = matches[0]
        path = path.resolve()
        if not path.is_relative_to(self.root / "corpus") or path.suffix != ".md":
            raise ValueError(f"Card must be a Markdown file under corpus/: {path}")
        return path

    @cache
    def header(self, path: Path) -> Card:
        return card_header(path.read_text(), path)

    def collection(self, reference: str) -> CollectionCard:
        card = self.header(self.resolve(reference))
        if not isinstance(card, CollectionCard):
            raise ValueError(f"Expected a collection: {reference}")
        return card

    def appearances(self, reference: str, section: str = "", trail: tuple[Location, ...] = ()) -> list[Appearance]:
        collection = self.collection(reference)
        if collection.id in [location.collection.id for location in trail]:
            raise ValueError(f"Collection cycle: {' -> '.join([location.collection.id for location in trail] + [collection.id])}")
        source = collection.source
        if isinstance(source, TextbookSource) or isinstance(source, CompilationSource) and source.sections:
            groups = [(group.name, group.problems) for group in source.sections]
        else:
            groups = [("", source.problems)]
        if section:
            selected = [(name, entries) for name, entries in groups if name == section]
            if len(selected) != 1:
                raise ValueError(f"Section must match exactly one authored name in {collection.id}: {section!r}")
            groups = selected
        appearances = []
        for name, entries in groups:
            for position, entry in enumerate(entries, 1):
                locations = (*trail, Location(collection, name, position, entry.comment))
                if entry.id.startswith("SRC-"):
                    appearances.extend(self.appearances(entry.id, trail=locations))
                else:
                    appearances.append(Appearance(entry.id, locations))
        return appearances

    def context(self, path: Path) -> str:
        card_id = identity(path)
        if card_id is None:
            raise ValueError(f"{path}: no scalar id field in front matter")
        lines = [f"Card: {card_id}", f"Path: {path.relative_to(self.root)}", "", "Recorded source context:"]
        if card_id.startswith("SRC-"):
            collections = [self.collection(card_id)]
        else:
            collections = []
            for collection_id in self.addresses:
                if not collection_id.startswith("SRC-"):
                    continue
                for appearance in self.appearances(collection_id):
                    if appearance.card_id == card_id:
                        lines.append("- " + " > ".join(location.label() for location in appearance.locations))
                        for location in appearance.locations:
                            if location.collection not in collections:
                                collections.append(location.collection)
        for collection in collections:
            lines.append(f"\n{collection.id}: {collection.title}")
            lines.append(f"Collection card: {self.resolve(collection.id).relative_to(self.root)}")
            links = _collection_source_links(self.root, collection.provenance)
            lines.extend(f"{link['label']}: {link['href']}" for link in links)
            if not links:
                lines.append("Provenance list is empty.")
        if not collections:
            lines.append("No authored collection membership references this card.")
        return "\n".join(lines)


def _refuse_secondary_worktrees() -> None:
    """QUAL-09: one checkout, one branch. A card commit is where a stream that opened a
    worktree finds out, because card authoring is the population that built them."""
    listing = subprocess.run(["git", "worktree", "list", "--porcelain"], check=True, capture_output=True, text=True).stdout
    extra = sum(line.startswith("worktree ") for line in listing.splitlines()) - 1
    if extra > 0:
        raise ValueError(f"QUAL-09: {extra} worktree(s) exist. Streams work directly on main in this clone; land the work on main, then remove the worktree.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check-staged", help="validate changed card YAML and schema from the Git index")
    range_check = commands.add_parser("check-range", help="validate changed card YAML and schema from committed HEAD")
    range_check.add_argument("base", help="base commit of the outgoing range")
    selected_check = commands.add_parser("check-changes", help="validate exact Git blobs selected by the shared local hook")
    selected_check.add_argument("--mode", choices=("staged", "push"), required=True)
    for name in ("path", "read", "diff", "check", "commit"):
        command = commands.add_parser(name)
        command.add_argument("card", help="card ID or corpus Markdown path")
        if name == "commit":
            command.add_argument("message")
    for name in ("list", "unsolved", "sample"):
        command = commands.add_parser(name)
        command.add_argument("collection", help="collection ID, index path, or directory containing index.md")
        if name == "sample":
            command.add_argument("count", type=int)
        command.add_argument("section", nargs="?", default="", help="exact authored section name; omitted means all")
    args = parser.parse_args(argv)
    corpus = Corpus(Path.cwd())
    try:
        if args.command == "check-staged":
            return check_git_cards("index", ("--cached",), head_commit())
        if args.command == "check-range":
            return check_git_cards("HEAD", (args.base, "HEAD"), args.base) or check_references(["HEAD"])
        if args.command == "check-changes":
            if args.mode == "staged":
                _refuse_secondary_worktrees()
            changes = [GitChange.model_validate_json(line) for line in sys.stdin]
            if any((change.version == "index") != (args.mode == "staged") for change in changes):
                raise ValueError("Git blob versions must match the requested validation mode")
            if args.mode == "staged":
                return check_git_changes(changes, head_commit(), ("index",))
            # The shared hook's payload omits deletions, and the pushed tip is HEAD on main (QUAL-09),
            # so the tip is replayed even when the payload holds no path at all.
            versions = list(dict.fromkeys([*[change.version for change in changes], "HEAD"]))
            failed = 0
            for version in versions:
                failed |= check_pushed_commits(version)
            return failed or check_references(["HEAD", *versions])
        if args.command in ("list", "unsolved", "sample"):
            if args.command == "sample" and args.count <= 0:
                raise ValueError("sample count must be positive")
            appearances = corpus.appearances(args.collection, args.section)
            paths = {item.card_id: corpus.resolve(item.card_id) for item in appearances}
            headers = {card_id: corpus.header(path) for card_id, path in paths.items()}
            if args.command != "list":
                parsed, errors = parse_cards(list(paths.values()))
                if errors:
                    raise ValueError("\n".join(map(str, errors)))
                unsolved = {item.card.id for item in parsed if item.card.kind == "problem" and not any(kind == "solution" for kind, _ in item.sections)}
                appearances = [item for item in appearances if item.card_id in unsolved]
            if args.command == "sample":
                selected_ids = random.sample(list(dict.fromkeys(item.card_id for item in appearances)), min(args.count, len({item.card_id for item in appearances})))
                appearances = [item for item in appearances if item.card_id in selected_ids]
            writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
            writer.writerow(("id", "path", "title", "collection", "section", "position", "comment", "via"))
            for item in appearances:
                location = item.locations[-1]
                writer.writerow(
                    (
                        item.card_id,
                        paths[item.card_id].relative_to(corpus.root),
                        headers[item.card_id].title,
                        location.collection.id,
                        location.section,
                        location.position,
                        location.comment,
                        " > ".join(step.label() for step in item.locations[:-1]),
                    )
                )
            return 0
        path = corpus.resolve(args.card)
        relative = str(path.relative_to(corpus.root))
        if args.command == "path":
            print(relative)
        elif args.command == "read":
            print(corpus.context(path) + "\n\n--- Authored card ---\n")
            print(path.read_text(), end="")
        elif args.command == "check":
            card = parse_card(path)
            print(f"{card.card.id}: schema and Markdown parsing OK (single card)")
        elif args.command == "diff":
            subprocess.run(["git", "--literal-pathspecs", "diff", "HEAD", "--", relative], check=True)
        elif args.command == "commit":
            _refuse_secondary_worktrees()
            subprocess.run(["git", "--literal-pathspecs", "ls-files", "--error-unmatch", "--", relative], check=True, stdout=subprocess.DEVNULL)
            # --only commits this working-tree path, preserving other staged work.
            # Validate that same source before taking the content-only commit route; the
            # comparison reads the base blob by its repository-relative path.
            corpus.header(path)
            rewritten = rewritten_audit_events(
                Path(relative),
                previous_source(Path(relative), "HEAD"),
                path.read_text(),
                commit_day("index"),
                lambda identity: introduced_event_notes(Path(relative), "HEAD", identity),
            )
            if rewritten:
                raise ValueError("\n".join(rewritten))
            subprocess.run(["git", "--literal-pathspecs", "commit", "--only", "--no-verify", "-m", args.message, "--", relative], check=True)
    except (ValueError, TypeError, OSError, yaml.YAMLError) as exc:
        parser.exit(1, f"{exc}\n")
    except subprocess.CalledProcessError as exc:
        return exc.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
