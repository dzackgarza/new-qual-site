"""Validation + the derived index.

The SQLite catalog is never authoritative. It is a disposable projection of the
corpus at one commit, rebuilt from scratch every time.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import yaml

from .model import (
    AcademicTerm,
    ContributedArtifact,
    ExamSource,
    OccurrenceCard,
    ParsedCard,
    SourceCard,
    TermOnly,
    TextbookSource,
    YearOnly,
)

SCHEMA = """
create table cards (
  id text primary key,
  kind text not null,
  title text not null,
  review text not null,
  source_path text not null,   -- diagnostics and edit links only, never identity
  ast text not null            -- pandoc JSON of the card body
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
  date_kind text not null, year integer, term text
);
create table exam_sources (id text primary key, institution text not null, area text not null);
create table textbook_sources (id text primary key, textbook text not null);
create table artifact_sources (id text primary key, provenance text not null);
create table occurrences (
  id text primary key, problem_id text not null, source_id text not null, locator text not null
);
create table sections (
  card_id text not null, section_kind text not null, ordinal integer not null, text text not null
);
create virtual table search using fts5(card_id unindexed, section_kind unindexed, text);
"""


def load_vocabularies(root: Path) -> dict[str, set[str]]:
    vocab = {}
    for name in ("areas", "topics", "institutions"):
        data = yaml.safe_load((root / f"{name}.yaml").read_text())
        vocab[name] = {entry["id"] for entry in data}
    return vocab


def validate(parsed: list[ParsedCard], vocab: dict[str, set[str]]) -> list[str]:
    errors: list[str] = []
    by_id: dict[str, ParsedCard] = {}
    for p in parsed:
        if p.card.id in by_id:
            errors.append(f"duplicate id {p.card.id}: {by_id[p.card.id].source_path} and {p.source_path}")
        by_id[p.card.id] = p

    for p in parsed:
        where = f"{p.source_path} ({p.card.id})"
        for area in p.card.classification.areas:
            if area not in vocab["areas"]:
                errors.append(f"{where}: unknown area {area!r}")
        for topic in p.card.classification.topics:
            if topic not in vocab["topics"]:
                errors.append(f"{where}: unknown topic {topic!r}")
        for rel in p.card.relations:
            if rel.target not in by_id:
                errors.append(f"{where}: dangling relation target {rel.target!r}")
        if isinstance(p.card, SourceCard):
            # Only an exam sitting has an institution to check. A textbook has a
            # publisher, not a university; an artifact has a provenance note.
            if isinstance(p.card.payload, ExamSource) and p.card.payload.institution not in vocab["institutions"]:
                errors.append(f"{where}: unknown institution {p.card.payload.institution!r}")
        if isinstance(p.card, OccurrenceCard):
            src = by_id.get(p.card.payload.source)
            if src is None:
                errors.append(f"{where}: occurrence names missing source {p.card.payload.source!r}")
            elif not isinstance(src.card, SourceCard):
                errors.append(f"{where}: {p.card.payload.source} is not a source card")
            targets = [r.target for r in p.card.relations if r.kind == "instance-of"]
            if len(targets) != 1:
                errors.append(f"{where}: occurrence needs exactly one instance-of relation")
            elif by_id.get(targets[0]) and by_id[targets[0]].card.kind != "problem":
                errors.append(f"{where}: instance-of must target a problem")
    return errors


def build(parsed: list[ParsedCard], db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    db_path.unlink(missing_ok=True)
    con = sqlite3.connect(db_path)
    con.executescript(SCHEMA)

    for p in parsed:
        c = p.card
        con.execute(
            "insert into cards values (?,?,?,?,?,?)",
            (c.id, c.kind, c.title, c.review, p.source_path, p.ast),
        )
        for axis, terms in (("area", c.classification.areas), ("topic", c.classification.topics)):
            con.executemany("insert into classifications values (?,?,?)", [(c.id, axis, t) for t in terms])
        con.executemany("insert into relations values (?,?,?)", [(c.id, r.kind, r.target) for r in c.relations])
        for ordinal, (kind, text) in enumerate(p.sections):
            con.execute("insert into sections values (?,?,?,?)", (c.id, kind, ordinal, text))
            con.execute("insert into search values (?,?,?)", (c.id, kind, text))

        if isinstance(c, SourceCard):
            d = c.payload.date
            con.execute(
                "insert into sources values (?,?,?,?,?)",
                (
                    c.id,
                    c.payload.source_kind,
                    d.kind,
                    d.year if isinstance(d, AcademicTerm | YearOnly) else None,
                    d.term if isinstance(d, AcademicTerm | TermOnly) else None,
                ),
            )
            # One branch per variant, no fallback: a new source kind added to the
            # union without a projection here is a mypy error, not a silent skip.
            match c.payload:
                case ExamSource():
                    con.execute(
                        "insert into exam_sources values (?,?,?)",
                        (c.id, c.payload.institution, c.payload.area),
                    )
                case TextbookSource():
                    con.execute("insert into textbook_sources values (?,?)", (c.id, c.payload.textbook))
                case ContributedArtifact():
                    con.execute("insert into artifact_sources values (?,?)", (c.id, c.payload.provenance))
        if isinstance(c, OccurrenceCard):
            problem = next(r.target for r in c.relations if r.kind == "instance-of")
            con.execute(
                "insert into occurrences values (?,?,?,?)",
                (c.id, problem, c.payload.source, c.payload.locator),
            )

    con.commit()
    con.close()
