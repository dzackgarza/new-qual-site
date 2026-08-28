"""Validation + the derived catalog.

The SQLite catalog is never authoritative. It is a disposable snapshot of the
corpus at one commit, rebuilt from scratch every time.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

import yaml

from .diagnostics import Diagnostic, DiagnosticCode
from .model import (
    AcademicTerm,
    Card,
    CollectionCard,
    CompilationSource,
    ExamSource,
    HomeworkSource,
    ParsedCard,
    ProblemEntry,
    TermOnly,
    TextbookSource,
    YearOnly,
)
from .wiki import slug

SCHEMA = """
create table cards (
  id text primary key,
  kind text not null,
  title text not null,
  prompts text not null,         -- JSON list of review questions; '[]' when the card has none
  review text not null,
  source_path text not null,   -- diagnostics and edit links only, never identity
  ast text not null,           -- pandoc JSON of the card body
  route text not null          -- the directory the card's page is written under
);
create table classifications (card_id text not null, axis text not null, term text not null);
create table relations (source_id text not null, kind text not null, target_id text not null);
-- `sources` holds what every source kind has. The kind-specific columns live in
-- their own tables, mirroring the discriminated union rather than flattening it
-- into one row with columns that are null for two kinds out of three.
-- `year` and `term` stay nullable here because the date union genuinely has
-- cases that lack them; `date_kind` says which case, so null is never ambiguous.
create table sources (
  id text primary key, source_kind text not null,
  date_kind text not null, year integer, term text,
  completion text not null
);
create table exam_sources (id text primary key, institution text not null, area text not null);
create table textbook_sources (id text primary key, textbook text not null);
create table homework_sources (id text primary key, area text not null);
create table compilation_sources (id text primary key, area text not null);
create table collection_problems (
  collection_id text not null,
  section_ordinal integer,
  section_name text,
  ordinal integer not null,
  problem_id text not null,
  comment text                 -- where the problem sits in THIS source ("Problem 6"); null when it needs no comment
);
create table collection_provenance (
  collection_id text not null,
  ordinal integer not null,
  href text not null
);
create table sections (
  card_id text not null, section_kind text not null, ordinal integer not null, text text not null
);
create virtual table search using fts5(card_id unindexed, section_kind unindexed, text);
"""


def load_areas(wiki_root: Path) -> dict[str, str]:
    """Every subject the corpus has, as id to display name.

    The subjects are the wiki's top-level folders. That is already what a
    reader navigates and what a card's `area` names, so a registry listing them
    again was a second copy with nothing to keep it honest -- and it had
    drifted: it said `Prelim` where the wiki had said `Prelims` all along, and
    the display name it carried was never read at all.

    A folder is a subject unless its index says `subject: false`. Archives is
    the one that says so: it holds source dumps, not a subject.

    Adding a subject is `mkdir wiki/<name>` and an `index.md` with a title,
    which is the landing page that subject needs regardless.
    """
    areas: dict[str, str] = {}
    if not wiki_root.is_dir():
        return areas
    for directory in sorted(p for p in wiki_root.iterdir() if p.is_dir()):
        index = directory / "index.md"
        if not index.exists():
            continue
        text = index.read_text()
        metadata = yaml.safe_load(text.split("---\n", 2)[1]) or {} if text.startswith("---\n") and len(text.split("---\n", 2)) == 3 else {}
        if metadata.get("subject") is False:
            continue
        title = metadata.get("title")
        areas[slug(directory.name)] = title if isinstance(title, str) and title.strip() else directory.name
    return areas


def load_vocabularies(root: Path, wiki_root: Path) -> dict[str, set[str]]:
    """Institutions and textbooks stay registries; areas are the wiki's folders.

    An institution or a textbook has no counterpart in the tree -- they are
    provenance, not subjects -- so those remain authored lists.
    """
    vocab = {"areas": set(load_areas(wiki_root))}
    for name in ("institutions", "textbooks"):
        data = yaml.safe_load((root / f"{name}.yaml").read_text())
        vocab[name] = {entry["id"] for entry in data}
    return vocab


def validate(parsed: list[ParsedCard], vocab: dict[str, set[str]]) -> list[Diagnostic]:
    errors: list[Diagnostic] = []
    by_id: dict[str, ParsedCard] = {}
    for p in parsed:
        if p.card.id in by_id:
            errors.append(
                Diagnostic(
                    DiagnosticCode.DUPLICATE_ID,
                    p.source_path,
                    f"duplicate id {p.card.id}: also at {by_id[p.card.id].source_path}",
                )
            )
        by_id[p.card.id] = p

    for p in parsed:
        where = f"{p.source_path} ({p.card.id})"
        for area in p.card.classification.areas:
            if area not in vocab["areas"]:
                errors.append(Diagnostic(DiagnosticCode.UNKNOWN_AREA, where, f"unknown area {area!r}"))
        for rel in p.card.relations:
            if rel.target not in by_id:
                errors.append(
                    Diagnostic(
                        DiagnosticCode.DANGLING_RELATION,
                        where,
                        f"dangling relation target {rel.target!r}",
                    )
                )
        if isinstance(p.card, CollectionCard):
            # One registry check per variant, matching the union.
            source = p.card.source
            if isinstance(source, ExamSource) and source.institution not in vocab["institutions"]:
                errors.append(
                    Diagnostic(
                        DiagnosticCode.UNKNOWN_INSTITUTION,
                        where,
                        f"unknown institution {source.institution!r}",
                    )
                )
            if isinstance(source, (ExamSource, HomeworkSource, CompilationSource)) and source.area not in vocab["areas"]:
                errors.append(
                    Diagnostic(
                        DiagnosticCode.UNKNOWN_AREA,
                        where,
                        f"unknown source area {source.area!r}",
                    )
                )
            if isinstance(source, TextbookSource) and source.textbook not in vocab["textbooks"]:
                errors.append(
                    Diagnostic(
                        DiagnosticCode.UNKNOWN_TEXTBOOK,
                        where,
                        f"unknown textbook {source.textbook!r}",
                    )
                )
    return errors


def _insert_problems(
    con: sqlite3.Connection,
    collection_id: str,
    section_ordinal: int | None,
    section_name: str | None,
    entries: list[ProblemEntry],
) -> None:
    con.executemany(
        "insert into collection_problems values (?,?,?,?,?,?)",
        [(collection_id, section_ordinal, section_name, ordinal, e.id, e.comment) for ordinal, e in enumerate(entries)],
    )


def card_route(card: Card) -> str:
    """The directory a card's page is written under.

    A sitting is under `exam/` and reads as one. The other 43 collections are
    textbooks, homework sets and compiled scans, and calling a textbook page an
    exam is the defect this splits. Every other card is under `tag/`.

    Decided here, where the card's kind and its source kind are both in hand,
    and carried on the row: the emitter used to recompute it from `kind` alone
    in three places, which is three chances to disagree.
    """
    if not isinstance(card, CollectionCard):
        return "tag"
    return "exam" if isinstance(card.source, ExamSource) else "source"


def build(parsed: list[ParsedCard], db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    db_path.unlink(missing_ok=True)
    con = sqlite3.connect(db_path)
    con.executescript(SCHEMA)

    for p in parsed:
        c = p.card
        con.execute(
            "insert into cards values (?,?,?,?,?,?,?,?)",
            # ponytail: JSON in one column, not a side table like `classifications`.
            # Prompts are only ever read back whole and in order, and the side
            # tables carry no position column -- ordering them would mean adding
            # one, which is more invention than a `json.loads` on the way out.
            (c.id, c.kind, c.title, json.dumps(c.prompts), c.review, p.source_path, p.ast, card_route(c)),
        )
        for axis, terms in (
            ("area", c.classification.areas),
            ("topic", c.classification.topics),
        ):
            con.executemany(
                "insert into classifications values (?,?,?)",
                [(c.id, axis, t) for t in terms],
            )
        con.executemany(
            "insert into relations values (?,?,?)",
            [(c.id, r.kind, r.target) for r in c.relations],
        )
        for ordinal, (kind, text) in enumerate(p.sections):
            con.execute("insert into sections values (?,?,?,?)", (c.id, kind, ordinal, text))
            con.execute("insert into search values (?,?,?)", (c.id, kind, text))

        if isinstance(c, CollectionCard):
            d = c.source.date
            con.execute(
                "insert into sources values (?,?,?,?,?,?)",
                (
                    c.id,
                    c.source.source_kind,
                    d.kind,
                    d.year if isinstance(d, AcademicTerm | YearOnly) else None,
                    d.term if isinstance(d, AcademicTerm | TermOnly) else None,
                    c.completion,
                ),
            )
            for ordinal, href in enumerate(c.provenance):
                con.execute(
                    "insert into collection_provenance values (?,?,?)",
                    (c.id, ordinal, href),
                )
            match c.source:
                case ExamSource():
                    con.execute(
                        "insert into exam_sources values (?,?,?)",
                        (c.id, c.source.institution, c.source.area),
                    )
                    _insert_problems(con, c.id, None, None, c.source.problems)
                case TextbookSource():
                    con.execute(
                        "insert into textbook_sources values (?,?)",
                        (c.id, c.source.textbook),
                    )
                    for section_ordinal, section in enumerate(c.source.sections):
                        _insert_problems(con, c.id, section_ordinal, section.name, section.problems)
                case HomeworkSource():
                    con.execute(
                        "insert into homework_sources values (?,?)",
                        (c.id, c.source.area),
                    )
                    _insert_problems(con, c.id, None, None, c.source.problems)
                case CompilationSource():
                    con.execute(
                        "insert into compilation_sources values (?,?)",
                        (c.id, c.source.area),
                    )
                    if c.source.sections:
                        for section_ordinal, section in enumerate(c.source.sections):
                            _insert_problems(con, c.id, section_ordinal, section.name, section.problems)
                    else:
                        _insert_problems(con, c.id, None, None, c.source.problems)

    con.commit()
    con.close()
