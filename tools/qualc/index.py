"""Validation + the derived catalog.

The SQLite catalog is never authoritative. It is a disposable snapshot of the
corpus at one commit, rebuilt from scratch every time.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import yaml

from .diagnostics import Diagnostic, DiagnosticCode
from .model import (
    AcademicTerm,
    CollectionCard,
    CompilationSource,
    ExamSource,
    HomeworkSource,
    ParsedCard,
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
  problem_id text not null
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


def load_vocabularies(root: Path) -> dict[str, set[str]]:
    vocab = {}
    for name in ("areas", "institutions", "textbooks"):
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
                errors.append(
                    Diagnostic(
                        DiagnosticCode.UNKNOWN_AREA, where, f"unknown area {area!r}"
                    )
                )
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
            if (
                isinstance(source, ExamSource)
                and source.institution not in vocab["institutions"]
            ):
                errors.append(
                    Diagnostic(
                        DiagnosticCode.UNKNOWN_INSTITUTION,
                        where,
                        f"unknown institution {source.institution!r}",
                    )
                )
            if (
                isinstance(source, (ExamSource, HomeworkSource, CompilationSource))
                and source.area not in vocab["areas"]
            ):
                errors.append(
                    Diagnostic(
                        DiagnosticCode.UNKNOWN_AREA,
                        where,
                        f"unknown source area {source.area!r}",
                    )
                )
            if (
                isinstance(source, TextbookSource)
                and source.textbook not in vocab["textbooks"]
            ):
                errors.append(
                    Diagnostic(
                        DiagnosticCode.UNKNOWN_TEXTBOOK,
                        where,
                        f"unknown textbook {source.textbook!r}",
                    )
                )
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
            con.execute(
                "insert into sections values (?,?,?,?)", (c.id, kind, ordinal, text)
            )
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
                    for ordinal, pid in enumerate(c.source.problems):
                        con.execute(
                            "insert into collection_problems values (?,?,?,?,?)",
                            (c.id, None, None, ordinal, pid),
                        )
                case TextbookSource():
                    con.execute(
                        "insert into textbook_sources values (?,?)",
                        (c.id, c.source.textbook),
                    )
                    for section_ordinal, section in enumerate(c.source.sections):
                        for ordinal, pid in enumerate(section.problems):
                            con.execute(
                                "insert into collection_problems values (?,?,?,?,?)",
                                (c.id, section_ordinal, section.name, ordinal, pid),
                            )
                case HomeworkSource():
                    con.execute(
                        "insert into homework_sources values (?,?)",
                        (c.id, c.source.area),
                    )
                    for ordinal, pid in enumerate(c.source.problems):
                        con.execute(
                            "insert into collection_problems values (?,?,?,?,?)",
                            (c.id, None, None, ordinal, pid),
                        )
                case CompilationSource():
                    con.execute(
                        "insert into compilation_sources values (?,?)",
                        (c.id, c.source.area),
                    )
                    if c.source.sections:
                        for section_ordinal, section in enumerate(c.source.sections):
                            for ordinal, pid in enumerate(section.problems):
                                con.execute(
                                    "insert into collection_problems values (?,?,?,?,?)",
                                    (c.id, section_ordinal, section.name, ordinal, pid),
                                )
                    else:
                        for ordinal, pid in enumerate(c.source.problems):
                            con.execute(
                                "insert into collection_problems values (?,?,?,?,?)",
                                (c.id, None, None, ordinal, pid),
                            )

    con.commit()
    con.close()
