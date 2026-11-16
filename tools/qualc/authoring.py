"""Live card addressing, authored collection traversal, and source context."""

from __future__ import annotations

import argparse
import csv
import random
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from functools import cache, cached_property
from pathlib import Path

import yaml
from pydantic import TypeAdapter

from .emit import _collection_source_links, compile_tikzcd_block
from .model import FRONT_MATTER, MARKDOWN, Card, CollectionCard, CompilationSource, ExamSource, HomeworkSource, Strict, TextbookSource, discover, load_front_matter, parse_card, parse_cards, split_front_matter, unread_math, validate_fenced_divs
from .pandoc_batch import PandocFailure, PandocServer
from .publication import PublicationManifest
from .tex import mark_definienda

CARD_ADAPTER: TypeAdapter[Card] = TypeAdapter(Card)
ID_FIELD = re.compile(r"^(id|'id'|\"id\")\s*:")
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
# Dated records outside the corpus: the root complaints file's entries.
COMPLAINTS = Path("COMPLAINTS.md")
# A dated entry is a heading or a numbered item; the bullets inside a section are its
# evidence, and a day in one of them belongs to the sentence that records it.
ENTRY_DAY = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
HEADING = re.compile(r"^(?P<marks>#{1,6})\s")
NUMBERED = re.compile(r"^\d+\.\s")


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

    A deleted blob is read for the card it held, so its defects are not this gate's to
    report and a header that does not parse has no identity to match.
    """
    match = FRONT_MATTER.match(source)
    if match is None:
        return None
    for line in match["front"].splitlines():
        if ID_FIELD.match(line):
            try:
                value = yaml.load(line, Loader=yaml.CSafeLoader).get("id")
            except (yaml.YAMLError, AttributeError):
                return None
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
    """A card's `audit:` events, in the order authored, read from its front matter."""
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


def rewritten_audit_events(path: Path, before: str, after: str, day: date) -> list[str]:
    """Audit events dated before the commit whose text it changes or removes (QUAL-11).

    An event dated before the commit records what a session found on that day, and the
    events after it refer to that text; a later correction is a new event dated the
    commit's date, so the earlier record keeps meaning what it said. Events dated the
    commit's own day are still in flight and may be edited, and an appended event is
    always accepted.
    """
    kept = Counter(record.text for record in audit_records(after))
    errors: list[str] = []
    for record in audit_records(before):
        if record.day is None or record.day >= day:
            continue
        if kept[record.text]:
            kept[record.text] -= 1
            continue
        kind, by, _, note = record.text
        said = f", whose note begins {excerpt!r}," if (excerpt := " ".join(note.split())[:60]) else ""
        errors.append(f"{path}: the {kind} event by {by} dated {record.day}{said} was changed or deleted; a dated event records what that session found, so a correction is a new event dated {day} (QUAL-11)")
    return errors


def dated_entries(source: str) -> list[tuple[date, str]]:
    """Each COMPLAINTS entry whose heading or first line carries a day, with its text.

    An entry is a heading section or a numbered item, and its day is the first
    `YYYY-MM-DD` on the line that opens it. A day inside the body belongs to the
    sentence that records it, not to the entry.
    """
    lines = source.splitlines()
    starts: list[tuple[int, int | None]] = []
    for index, line in enumerate(lines):
        if heading := HEADING.match(line):
            starts.append((index, len(heading["marks"])))
        elif NUMBERED.match(line):
            starts.append((index, None))
    entries: list[tuple[date, str]] = []
    for position, (start, level) in enumerate(starts):
        found = ENTRY_DAY.search(lines[start])
        if found is None:
            continue
        try:
            day = date.fromisoformat(found[1])
        except ValueError:
            # The shape is a day's, the value is not one; the entry is not dated.
            continue
        end = len(lines)
        for later, later_level in starts[position + 1 :]:
            if level is None or (later_level is not None and later_level <= level):
                end = later
                break
        entries.append((day, "\n".join(lines[start:end]).strip()))
    return entries


def rewritten_complaint_entries(path: Path, before: str, after: str, day: date) -> list[str]:
    """Dated COMPLAINTS entries a commit changes or deletes (QUAL-11).

    An entry dated before the commit is a record, and a paragraph appended after it
    leaves its text intact; editing a word of it or removing the entry does not. An
    entry dated the commit's own day is still in flight.
    """
    errors: list[str] = []
    for entry_day, text in dated_entries(before):
        if entry_day >= day or text in after:
            continue
        said = " ".join(text.split())[:60]
        errors.append(f"{path}: the entry dated {entry_day}, beginning {said!r}, was changed or deleted; a dated entry records what that day found, so a correction is a new entry dated {day} (QUAL-11)")
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


def comparison_revision(version: str) -> str:
    """The revision a changed blob is compared with when its caller names no base.

    The index becomes a commit whose parent is HEAD. A committed candidate is compared
    with the merge-base of its commit and the branch's upstream, so a card changed in two
    commits of one push is compared with its content before the push; where no upstream is
    recorded the comparison is the commit's parent, and a card changed twice in such a
    push is compared with the version after its earlier change.
    """
    if version == "index":
        return "HEAD"
    merged = subprocess.run(["git", "merge-base", version, "@{upstream}"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    base = merged.stdout.strip()
    if merged.returncode == 0 and base and base != version:
        return base
    return f"{version}^"


def revision_exists(revision: str) -> bool:
    """Whether Git resolves `revision` to a commit in this repository."""
    return subprocess.run(["git", "rev-parse", "--verify", "--quiet", f"{revision}^{{commit}}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


def previous_source(path: Path, revision: str) -> str:
    """The text at `path` in `revision`, or the empty text when there is none.

    A card added in this commit has no earlier blob, and a repository's first commit has
    no earlier revision; both are empty sources, established by asking Git for the
    revision and for the path. Any other `git show` failure is raised, never read as
    absence.
    """
    if not revision_exists(revision):
        return ""
    if subprocess.run(["git", "cat-file", "-e", f"{revision}:{path.as_posix()}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode:
        return ""
    return subprocess.run(["git", "show", f"{revision}:{path.as_posix()}"], check=True, stdout=subprocess.PIPE, text=True).stdout


def changed_paths(version: str, base: str) -> tuple[dict[Path, Path], list[Path]]:
    """Git's rename records and deletions for one version's diff against `base`.

    A rename is one change at its new path, so the earlier text of a moved card is read
    from the path Git names as its source. The deleted paths let a move whose content
    changed below Git's similarity threshold keep the earlier text through the card's
    own id.
    """
    if not revision_exists(base):
        return {}, []
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
            errors.extend(rewritten_audit_events(change.path, previous_source(earlier, base), source, day))
    return errors


def check_git_changes(changes: list[GitChange], base: str) -> int:
    """Validate card, wiki and complaint blobs selected by the shared hook or a range check.

    Diagrams are compiled here because the site build is the only other place
    that compiles them, and a malformed one otherwise first fails the deploy.

    `base` is the revision every changed blob is compared with: the parent of the staged
    index, or the base of an outgoing range. The caller names it, because the two
    selections have different ancestors.
    """
    cards = [change for change in changes if change.path.parts[0] in ("corpus", "wiki") and change.path.suffix == ".md"]
    complaints = [change for change in changes if change.path == COMPLAINTS]
    errors: list[str] = []
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
            if raw := RAW_BLACKBOARD.search(source):
                errors.append(f"{change.path}: {raw.group()} is written with its semantic macro (STYLE-03)")
            if raw := BACKSLASH_DELIMITER.search(source):
                errors.append(f"{change.path}: {raw.group()} delimits math; use $...$ or $$...$$ (STYLE-02)")
            if raw := raw_notation(source):
                errors.append(f"{change.path}: {raw}")
            bodies.append((change.path, mark_definienda(split_front_matter(source, change.path)[1])))
        except ValueError as exc:
            errors.append(str(exc))
        except RuntimeError as exc:
            errors.append(f"{change.path}: {exc}")
    errors.extend(changed_audit_events(selected, base))
    for change in complaints:
        revision = "" if change.version == "index" else change.version
        source = subprocess.run(["git", "show", f"{revision}:{COMPLAINTS.as_posix()}"], check=True, stdout=subprocess.PIPE, text=True).stdout
        errors.extend(rewritten_complaint_entries(COMPLAINTS, previous_source(COMPLAINTS, base), source, commit_day(change.version)))
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
        ["git", "diff", "--name-only", "--no-renames", "--diff-filter=ACM", "-z", *diff_args, "--", "corpus/", "wiki/", COMPLAINTS.as_posix()],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout
    return check_git_changes([GitChange(path=Path(name), version=version) for name in names.split("\0") if name], base)


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
            return check_git_cards("index", ("--cached",), "HEAD")
        if args.command == "check-range":
            return check_git_cards("HEAD", (args.base, "HEAD"), args.base) or check_references(["HEAD"])
        if args.command == "check-changes":
            if args.mode == "staged":
                _refuse_secondary_worktrees()
            changes = [GitChange.model_validate_json(line) for line in sys.stdin]
            if any((change.version == "index") != (args.mode == "staged") for change in changes):
                raise ValueError("Git blob versions must match the requested validation mode")
            if args.mode == "staged":
                return check_git_changes(changes, "HEAD")
            # The shared hook's payload omits deletions, and the pushed tip is HEAD on main (QUAL-09).
            versions = list(dict.fromkeys(change.version for change in changes))
            failed = 0
            for version in versions:
                failed |= check_git_changes([change for change in changes if change.version == version], comparison_revision(version))
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
            rewritten = rewritten_audit_events(Path(relative), previous_source(Path(relative), "HEAD"), path.read_text(), commit_day("index"))
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
