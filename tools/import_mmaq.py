#!/usr/bin/env python3
"""Reproducibly reconcile every MakeMeAQual row with the corpus.

The upstream file is an input, not an authored corpus subtree.  The default
invocation downloads the exact revision named by ``sources/mmaq-source.yaml``
and verifies its hash before doing any work.  ``--input`` is an explicit local
source override for tests or an already downloaded copy; it never acts as a
silent fallback.

The importer is deliberately additive.  It owns only ``corpus/imports/mmaq-total``
and its reconciliation ledger.  Existing cards are matched by an exact
normalized statement fingerprint; no fuzzy or similarity merge is performed.
Legacy generated directories are retired separately, after the ledger has been
checked by the caller.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import re
import shutil
import sys
import urllib.request
from pathlib import Path
from typing import Any

import yaml
from card_titles import title_of
from qualc.model import MARKDOWN
from qualc.pandoc_batch import PandocFailure, PandocServer

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_NAME = Path("sources/mmaq-source.yaml")
OUTPUT_NAME = Path("corpus/imports/mmaq-total")
LEDGER_NAME = Path("sources/mmaq-reconciliation.jsonl")

AREA_SLUG = {
    "Algebra": "algebra",
    "Real_Analysis": "real-analysis",
    "Complex_Analysis": "complex-analysis",
    "Topology": "topology",
}
AREA_ABBR = {
    "algebra": "ALG",
    "real-analysis": "RA",
    "complex-analysis": "CA",
    "topology": "TOP",
}
VALID_TERMS = {"spring", "fall"}
REQUIRED_ROW_KEYS = {"year", "number", "university", "exam", "tags", "question"}


def opaque(prefix: str, statement: str) -> str:
    """Return a stable, human-safe identifier for a statement."""

    digest = hashlib.sha1(statement.encode("utf-8")).digest()
    return prefix + base64.b32encode(digest).decode("ascii").rstrip("=")[:10]


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.strip().lower()).strip("-")


def normalize(statement: str) -> str:
    return re.sub(r"\s+", " ", statement).strip().lower()


_BB = re.compile(r"\\math(?:bf|bb|cal|rm)\{([a-zA-Z])\}")
_ALIGN = re.compile(r"\$\$\s*\\begin\{aligned\}|\\begin\{align\*?\}|\\begin\{aligned\}")
_ALIGN_END = re.compile(r"\\end\{aligned\}\s*\$\$|\\end\{align\*?\}|\\end\{aligned\}")


def loose(text: str) -> str:
    r"""One import's text, after every difference that re-minting would invent.

    Two renderings of one record differ by TeX spelling alone -- `\mathbf{Q}`
    against `\mathbb{Q}`, `\begin{aligned}` against `\begin{align*}`, a spacing
    macro, a `.` inside display math. Equal here means the importer recognises a
    record it already minted, instead of minting it again on the next run.

    It does not decide whether two cards state the same mathematics. Nothing in
    the text decides that: an unwritten card normalises to the same string as
    every other unwritten card, and two sittings of one problem normalise to the
    same string as each other. Deciding it means reading both statements.
    """
    t = text.lower()
    # Pandoc spells a TeX environment it will not touch as a raw-tex span, and
    # re-emits a blockquote with its `>` markers. Neither is part of the
    # statement. `>` is dropped only where it opens a line, so a `>` inside
    # mathematics survives.
    t = re.sub(r"^\s*>+\s?", "", t, flags=re.M)
    t = t.replace("`{=tex}", "").replace("`", "")
    t = t.replace(r"\[", "$$").replace(r"\]", "$$")
    t = _BB.sub(lambda m: r"\bb{" + m.group(1) + "}", t)
    t = _ALIGN.sub(lambda _: r"\begin{ALIGN}", t)
    t = _ALIGN_END.sub(lambda _: r"\end{ALIGN}", t)
    t = re.sub(r"\\[,;:!]", "", t)
    t = re.sub(r"\s+", "", t)
    t = re.sub(r"\.(?=\\end\{ALIGN\}|\$\$)", "", t)
    return t.rstrip(".,;$ \t")


def card(meta: dict[str, Any], body: str) -> str:
    frontmatter = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100).strip()
    return f"---\n{frontmatter}\n---\n\n{body.rstrip()}\n"


def converted_bodies(pandoc: PandocServer, statements: list[str], section: str) -> list[str]:
    """Convert a bounded batch through the repository's persistent Pandoc boundary."""

    documents = [f":::{{.{section}}}\n{statement}\n:::" for statement in statements]
    parsed = pandoc.read_markdown(documents, MARKDOWN)
    json_documents: list[str] = []
    for index, result in enumerate(parsed):
        if isinstance(result, PandocFailure):
            raise RuntimeError(f"pandoc failed while reading imported row {index + 1}: {result.error}")
        warnings = [message.message for message in result.messages if message.verbosity == "WARNING"]
        if warnings:
            raise RuntimeError(f"pandoc warned while reading imported row {index + 1}: {'; '.join(warnings)}")
        json_documents.append(result.output)
    written = pandoc.write_markdown(json_documents, MARKDOWN)
    outputs: list[str] = []
    for index, result in enumerate(written):
        if isinstance(result, PandocFailure):
            raise RuntimeError(f"pandoc failed while writing imported row {index + 1}: {result.error}")
        warnings = [message.message for message in result.messages if message.verbosity == "WARNING"]
        if warnings:
            raise RuntimeError(f"pandoc warned while writing imported row {index + 1}: {'; '.join(warnings)}")
        outputs.append(result.output.rstrip() + "\n")
    return outputs


def _required(mapping: dict[str, Any], key: str, context: str) -> Any:
    if key not in mapping:
        raise ValueError(f"{context} is missing required key {key!r}")
    return mapping[key]


def _manifest(root: Path) -> dict[str, str]:
    path = root / MANIFEST_NAME
    if not path.is_file():
        raise FileNotFoundError(f"pinned MakeMeAQual manifest is missing: {path}")
    raw = yaml.safe_load(path.read_text())
    if not isinstance(raw, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    values: dict[str, str] = {}
    for key in ("source", "url", "revision", "sha256", "path"):
        value = _required(raw, key, str(path))
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{path}: {key} must be a non-empty string")
        values[key] = value.strip()
    if len(values["sha256"]) != 64 or not re.fullmatch(r"[0-9a-f]{64}", values["sha256"]):
        raise ValueError(f"{path}: sha256 must be 64 lowercase hexadecimal characters")
    return values


def _source_bytes(root: Path, input_path: Path | None) -> tuple[bytes, dict[str, str]]:
    if input_path is not None:
        path = input_path.expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(f"explicit MakeMeAQual input is missing: {path}")
        data = path.read_bytes()
        return data, {
            "source": "explicit local input",
            "url": str(path),
            "revision": "local-input",
            "sha256": hashlib.sha256(data).hexdigest(),
            "path": str(path),
        }

    manifest = _manifest(root)
    request = urllib.request.Request(
        manifest["url"],
        headers={"User-Agent": "new-qual-site-mmaq-import/1"},
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        data = response.read()
    actual = hashlib.sha256(data).hexdigest()
    if actual != manifest["sha256"]:
        raise ValueError(f"MakeMeAQual source hash mismatch: expected {manifest['sha256']}, received {actual}")
    return data, manifest


def load_records(root: Path, input_path: Path | None) -> tuple[list[dict[str, Any]], dict[str, str]]:
    data, source = _source_bytes(root, input_path)
    parsed = yaml.safe_load(data)
    if not isinstance(parsed, list) or not parsed:
        raise ValueError("MakeMeAQual source must be a non-empty YAML list")
    registered, aliases = topic_vocabulary(root)
    unregistered: dict[str, int] = {}
    records: list[dict[str, Any]] = []
    for sequence, raw in enumerate(parsed, start=1):
        if not isinstance(raw, dict):
            raise ValueError(f"MakeMeAQual row {sequence} must be a mapping")
        missing = sorted(REQUIRED_ROW_KEYS - set(raw))
        if missing:
            raise ValueError(f"MakeMeAQual row {sequence} is missing keys: {', '.join(missing)}")
        question = raw["question"]
        tags = raw["tags"]
        if not isinstance(question, str) or not question.strip():
            raise ValueError(f"MakeMeAQual row {sequence} has an empty question")
        if not isinstance(tags, list) or any(not isinstance(tag, str) or not tag.strip() for tag in tags):
            raise ValueError(f"MakeMeAQual row {sequence} has invalid tags")
        exam = str(raw["exam"]).strip()
        if exam not in AREA_SLUG:
            raise ValueError(f"MakeMeAQual row {sequence} has unknown exam area {exam!r}")
        university = str(raw["university"]).strip()
        year = str(raw["year"]).strip()
        season = ""
        if "season" in raw and raw["season"] is not None:
            season = str(raw["season"]).strip().lower()
        if season == "na":
            season = ""
        if season and season not in VALID_TERMS:
            raise ValueError(f"MakeMeAQual row {sequence} has unknown season {season!r}")
        topics: list[str] = []
        for tag in tags:
            topic = slug(tag)
            if not topic:
                raise ValueError(f"MakeMeAQual row {sequence} has an empty topic slug for {tag!r}")
            topic = aliases.get(topic, topic)
            if topic not in registered:
                unregistered.setdefault(topic, sequence)
            if topic not in topics:
                topics.append(topic)
        records.append(
            {
                "sequence": sequence,
                "topics": topics,
                "year": year,
                "number": raw["number"],
                "university": university,
                "exam": exam,
                "season": season,
                "tags": [tag.strip() for tag in tags],
                "question": question.strip(),
                "normalized": loose(question),
            }
        )
    if unregistered:
        listed = ", ".join(f"{topic!r} (row {row})" for topic, row in sorted(unregistered.items()))
        raise ValueError(
            f"unregistered-topic: {len(unregistered)} tag(s) are neither in vocabularies/topics.yaml nor "
            f"aliased in vocabularies/topic-aliases.yaml: {listed}. Registering a topic or recording a "
            f"merge is a curation act; this importer will not do it."
        )
    return records, source


def _frontmatter(path: Path) -> dict[str, Any] | None:
    text = path.read_text()
    if not text.startswith("---\n"):
        return None
    pieces = text.split("---\n", 2)
    if len(pieces) != 3:
        return None
    raw = yaml.safe_load(pieces[1])
    return raw if isinstance(raw, dict) else None


def _problem_fingerprint(path: Path) -> str | None:
    metadata = _frontmatter(path)
    if metadata is None or metadata.get("kind") != "problem":
        return None
    text = path.read_text().split("---\n", 2)[2].strip()
    text = re.sub(r"^:::\s*(?:\{\.problem[^}]*\}|problem)\s*\n", "", text)
    text = re.sub(r"\n:::\s*$", "", text)
    return loose(text)


def existing_problems(
    root: Path,
    scan_root: Path | None = None,
    excluded_roots: tuple[Path, ...] = (),
) -> dict[str, list[tuple[str, str]]]:
    by_fingerprint: dict[str, list[tuple[str, str]]] = {}
    search_root = scan_root if scan_root is not None else root / "corpus"
    for path in sorted(search_root.rglob("*.md")):
        if any(path == excluded or excluded in path.parents for excluded in excluded_roots):
            continue
        fingerprint = _problem_fingerprint(path)
        if fingerprint is None:
            continue
        metadata = _frontmatter(path)
        if metadata is None:
            continue
        card_id = metadata["id"]
        if not isinstance(card_id, str) or not card_id:
            raise ValueError(f"problem card has invalid id: {path}")
        if fingerprint not in by_fingerprint:
            by_fingerprint[fingerprint] = []
        by_fingerprint[fingerprint].append((card_id, str(path.relative_to(root))))
    return dict(by_fingerprint)


def prior_reconciliation(root: Path, records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Read prior row reconciliation so IDs and classifications survive retirement."""

    ledger_path = root / LEDGER_NAME
    if not ledger_path.exists():
        return {}
    wanted = {hashlib.sha256(record["question"].encode("utf-8")).hexdigest() for record in records}
    recovered: dict[str, dict[str, Any]] = {}
    for line_number, line in enumerate(ledger_path.read_text().splitlines(), start=1):
        item = json.loads(line)
        context = f"{ledger_path} line {line_number}"
        if not isinstance(item, dict):
            raise ValueError(f"{context} is not a JSON object")
        statement_hash = _required(item, "statement_sha256", context)
        problem_id = _required(item, "problem_id", context)
        match = _required(item, "match", context)
        legacy_ids = _required(item, "legacy_problem_ids", context)
        legacy_paths = _required(item, "legacy_problem_paths", context)
        if (
            not isinstance(statement_hash, str)
            or not isinstance(problem_id, str)
            or not isinstance(match, str)
            or not isinstance(legacy_ids, list)
            or not isinstance(legacy_paths, list)
            or any(not isinstance(value, str) for value in legacy_ids)
            or any(not isinstance(value, str) for value in legacy_paths)
            or len(legacy_ids) != len(legacy_paths)
        ):
            raise ValueError(f"{context} has invalid reconciliation fields")
        if statement_hash not in wanted:
            continue
        entry = {
            "problem_id": problem_id,
            "match": match,
            "legacy_problem_ids": legacy_ids,
            "legacy_problem_paths": legacy_paths,
        }
        previous = recovered.get(statement_hash)
        if previous is not None and previous != entry:
            raise ValueError(f"{context} disagrees with an earlier row for {statement_hash}")
        recovered[statement_hash] = entry
    return recovered


def is_legacy_generated(path: str) -> bool:
    parts = Path(path).parts
    return "imports" in parts and any(name in parts for name in ("mmaq", "mmaq-full"))


def is_owned_output(path: str) -> bool:
    parts = Path(path).parts
    return "imports" in parts and "mmaq-total" in parts


def date_spec(year: str, season: str) -> dict[str, Any]:
    if year == "1970" and season in VALID_TERMS:
        return {"kind": "term", "term": season}
    if year.isdigit() and int(year) > 0:
        if season in VALID_TERMS:
            return {"kind": "academic-term", "year": int(year), "term": season}
        return {"kind": "year", "year": int(year)}
    if season in VALID_TERMS:
        return {"kind": "term", "term": season}
    return {"kind": "unknown"}


def source_key(record: dict[str, Any]) -> tuple[str, str, str, str]:
    season = record["season"] if record["season"] else ""
    return (record["university"].upper(), record["exam"], record["year"], season)


def source_id(key: tuple[str, str, str, str]) -> str:
    university, exam, year, season = key
    year_token = slug(year).upper() or "UNKNOWN"
    if year_token == "0":
        year_token = "UNKNOWN"
    if year_token == "EXTRA":
        year_token = "EXTRA"
    season_token = season.upper() if season else "NA"
    return f"SRC-MMAQ-{slug(university).upper()}-{AREA_ABBR[AREA_SLUG[exam]]}-{year_token}-{season_token}"


def native_sittings(root: Path, excluded_roots: tuple[Path, ...] = ()) -> dict[tuple[str, str, str], list[tuple[str, str]]]:
    """Exam sittings the corpus already records, keyed by institution, area and date.

    One sitting has one `source` card. When a sitting this import names already
    has a card minted from another source, the import joins onto it rather than
    minting a parallel `SRC-MMAQ-*`, which would split every per-exam query.

    A key can hold more than one card, because the schema's `academic-term` is
    spring-or-fall only and the corpus labels UGA analysis sittings by month:
    "January 2014" and "Spring 2014" both derive spring 2014. Which of those a
    row belongs to is decided by its own season word, in `join_sitting`.
    """
    found: dict[tuple[str, str, str], list[tuple[str, str]]] = {}
    for path in sorted((root / "corpus").rglob("*.md")):
        if any(path == excluded or excluded in path.parents for excluded in excluded_roots):
            continue
        metadata = _frontmatter(path)
        if metadata is None or metadata["kind"] != "source":
            continue
        payload = metadata["payload"]
        if payload["source_kind"] != "university-exam":
            continue
        key = (payload["institution"], payload["area"], json.dumps(payload["date"], sort_keys=True))
        if key not in found:
            found[key] = []
        found[key].append((metadata["id"], metadata["title"]))
    return found


def join_sitting(
    native: dict[tuple[str, str, str], list[tuple[str, str]]],
    key: tuple[str, str, str, str],
) -> tuple[str, str] | None:
    """The existing card for this sitting, or None when the corpus is unclear.

    A row states its own season. When several existing cards derive the same
    schema season, only the one whose written label is that season is the same
    sitting; joining onto a differently-labelled one would assert an identity
    the source does not support.
    """
    candidates = native[sitting_key(key)] if sitting_key(key) in native else []
    if len(candidates) == 1:
        return candidates[0]
    season = key[3].lower()
    labelled = [item for item in candidates if season and season in item[1].lower()]
    return labelled[0] if len(labelled) == 1 else None


def corpus_ids(root: Path, excluded_roots: tuple[Path, ...] = ()) -> set[str]:
    """Every card id the corpus holds outside this import's own output."""
    found: set[str] = set()
    for path in sorted((root / "corpus").rglob("*.md")):
        if any(path == excluded or excluded in path.parents for excluded in excluded_roots):
            continue
        metadata = _frontmatter(path)
        if metadata is not None:
            found.add(metadata["id"])
    return found


def sitting_key(key: tuple[str, str, str, str]) -> tuple[str, str, str]:
    university, exam, year, season = key
    return (university.lower(), AREA_SLUG[exam], json.dumps(date_spec(year, season), sort_keys=True))


def source_title(key: tuple[str, str, str, str]) -> str:
    university, exam, year, season = key
    area = exam.replace("_", " ")
    if year.isdigit() and int(year) > 0:
        date = f"{year} {season.title()}" if season else year
    elif season:
        date = f"undated year ({season.title()})"
    else:
        date = "undated collection"
    return f"{university} {area} {date}"


def topic_vocabulary(root: Path) -> tuple[set[str], dict[str, str]]:
    """Read the curated topic registry and its retirement aliases.

    Both files belong to the classification side. This importer consumes them
    and never writes them: a registry merge is a reading decision, so writing
    the registry here would undo one on every re-import.
    """
    registry_path = root / "vocabularies/topics.yaml"
    entries = yaml.safe_load(registry_path.read_text())
    if not isinstance(entries, list):
        raise ValueError(f"{registry_path} must contain a YAML list")
    registered = set()
    for item in entries:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            raise ValueError(f"{registry_path} contains a malformed topic entry")
        registered.add(item["id"])

    alias_path = root / "vocabularies/topic-aliases.yaml"
    aliases: dict[str, str] = {}
    for item in yaml.safe_load(alias_path.read_text()) or []:
        if not isinstance(item, dict) or not isinstance(item.get("retired"), str) or not isinstance(item.get("survivor"), str):
            raise ValueError(f"{alias_path} contains a malformed alias entry")
        if item["survivor"] not in registered:
            raise ValueError(f"{alias_path}: alias {item['retired']!r} names unregistered survivor {item['survivor']!r}")
        aliases[item["retired"]] = item["survivor"]
    return registered, aliases


def write_source(
    path: Path,
    key: tuple[str, str, str, str],
    count: int,
    source: dict[str, str],
    body: str,
) -> None:
    university, exam, year, season = key
    area = AREA_SLUG[exam]
    metadata = {
        "schema": "qual/card@1",
        "id": source_id(key),
        "kind": "source",
        "title": source_title(key),
        "classification": {"areas": [area], "topics": []},
        "relations": [],
        "review": "draft",
        "payload": {
            "source_kind": "university-exam",
            "institution": university.lower(),
            "area": area,
            "date": date_spec(year, season),
        },
    }
    path.write_text(card(metadata, body))


def write_problem(
    path: Path,
    statement: str,
    area: str,
    topics: list[str],
    problem_id: str,
    body: str,
) -> None:
    metadata = {
        "schema": "qual/card@1",
        "id": problem_id,
        "kind": "problem",
        "title": title_of(statement),
        "classification": {"areas": [area], "topics": topics},
        "relations": [],
        "review": "draft",
    }
    path.write_text(card(metadata, body))


def write_occurrence(
    path: Path,
    record: dict[str, Any],
    source: str,
    problem_id: str,
    occurrence_id: str,
    body: str,
    sitting_title: str,
) -> None:
    area = AREA_SLUG[record["exam"]]
    topics = record["topics"]
    number = str(record["number"])
    locator = number if number not in {"", "0"} else f"row-{record['sequence']:04d}"
    metadata = {
        "schema": "qual/card@1",
        "id": occurrence_id,
        "kind": "occurrence",
        "title": f"{sitting_title}, problem {locator}",
        "classification": {"areas": [area], "topics": topics},
        "relations": [{"kind": "instance-of", "target": problem_id}],
        "review": "draft",
        "payload": {"source": source, "locator": locator},
    }
    path.write_text(card(metadata, body))


def reconcile(
    root: Path,
    records: list[dict[str, Any]],
    source: dict[str, str],
    pandoc: PandocServer,
) -> dict[str, int]:
    output = root / OUTPUT_NAME
    native = native_sittings(root, excluded_roots=(output,))
    foreign_ids = corpus_ids(root, excluded_roots=(output,))
    old = existing_problems(root, excluded_roots=(output,))
    current = existing_problems(root, scan_root=output) if output.exists() else {}
    current_text: dict[str, str] = {}
    for candidates in current.values():
        for _, relative_path in candidates:
            current_text[relative_path] = (root / relative_path).read_text()
    current_text_by_id: dict[str, str] = {}
    if output.exists():
        for path in sorted(output.glob("P-*.md")):
            metadata = _frontmatter(path)
            if metadata is not None and isinstance(metadata.get("id"), str):
                current_text_by_id[metadata["id"]] = path.read_text()
    prior = prior_reconciliation(root, records)
    if output.exists():
        if not output.is_dir():
            raise ValueError(f"import output is not a directory: {output}")
        for child in output.iterdir():
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    output.mkdir(parents=True, exist_ok=True)

    used_ids = {card_id for candidates in old.values() for card_id, _ in candidates}
    used_ids.update(card_id for candidates in current.values() for card_id, _ in candidates)
    problem_ids: dict[str, str] = {}
    problem_matches: dict[str, str] = {}
    problem_operations: dict[str, str] = {}
    problem_legacy: dict[str, list[tuple[str, str]]] = {}
    problem_history: dict[str, list[tuple[str, str]]] = {}
    problem_details: dict[str, tuple[str, list[str]]] = {}

    groups: dict[tuple[str, str, str, str], list[dict[str, Any]]] = {}
    for record in records:
        key = source_key(record)
        if key not in groups:
            groups[key] = []
        groups[key].append(record)

    for record in records:
        fingerprint = record["normalized"]
        if fingerprint not in problem_ids:
            candidates = old[fingerprint] if fingerprint in old else []
            current_candidates = current[fingerprint] if fingerprint in current else []
            statement_hash = hashlib.sha256(record["question"].encode("utf-8")).hexdigest()
            prior_entry = prior[statement_hash] if statement_hash in prior else None
            prior_id = prior_entry["problem_id"] if prior_entry is not None else None
            if len(current_candidates) == 1:
                problem_id, _ = current_candidates[0]
                operation = "current-output"
                legacy = current_candidates
            elif len(candidates) == 1:
                problem_id, _ = candidates[0]
                operation = "existing-exact"
                legacy = candidates
            elif len(candidates) > 1:
                problem_id = opaque("P-MMAQ-", fingerprint)
                operation = "ambiguous-exact"
                legacy = candidates
            elif prior_id is not None:
                problem_id = prior_id
                operation = "ledger-recovered"
                relative_path = f"corpus/imports/mmaq-total/{problem_id}.md"
                legacy = [(problem_id, relative_path)] if problem_id in current_text_by_id else [(problem_id, "")]
            else:
                problem_id = opaque("P-MMAQ-", fingerprint)
                operation = "new"
                legacy = []
            # A prior id is preserved so a row keeps its identity across runs --
            # but only while it is still this statement's id. Once another card
            # in the corpus owns it, recovering it mints a duplicate id, so the
            # row takes a fresh one instead.
            prior_ids = {prior_id} if prior_id is not None and prior_id not in foreign_ids else set()
            preserved_ids = prior_ids | {candidate_id for candidate_id, _ in current_candidates}
            while problem_id in used_ids and problem_id not in preserved_ids and not (len(candidates) == 1 and problem_id == candidates[0][0]):
                problem_id = opaque("P-MMAQ-", fingerprint + problem_id)
            used_ids.add(problem_id)
            problem_ids[fingerprint] = problem_id
            problem_operations[fingerprint] = operation
            if prior_entry is not None and problem_id == prior_id:
                problem_matches[fingerprint] = prior_entry["match"]
                problem_history[fingerprint] = list(zip(prior_entry["legacy_problem_ids"], prior_entry["legacy_problem_paths"], strict=True))
            else:
                problem_matches[fingerprint] = operation
                problem_history[fingerprint] = legacy
            problem_legacy[fingerprint] = legacy
            area = AREA_SLUG[record["exam"]]
            problem_details[fingerprint] = (area, record["topics"])

    unique_fingerprints = list(problem_ids)
    unique_statements = [next(record["question"] for record in records if record["normalized"] == fingerprint) for fingerprint in unique_fingerprints]
    problem_bodies = dict(zip(unique_fingerprints, converted_bodies(pandoc, unique_statements, "problem"), strict=True))
    # Occurrence cards carry the source appearance in their envelope; the
    # statement itself remains a problem section, matching the existing corpus
    # convention and the renderer's occurrence reveal handling.
    occurrence_bodies = converted_bodies(pandoc, [record["question"] for record in records], "problem")

    source_body_texts: list[str] = []
    source_keys = list(groups)
    for key in source_keys:
        source_body_texts.append(
            f"Imported from [`{source['source']}`]({source['url']}) at revision "
            f"`{source['revision']}`. The verified source SHA-256 is `{source['sha256']}`. "
            f"This source group contains {len(groups[key])} rows; no exam-term inference was made beyond "
            "the explicit `season` value."
        )
    source_bodies = dict(zip(source_keys, converted_bodies(pandoc, source_body_texts, "remark"), strict=True))

    for fingerprint, problem_id in problem_ids.items():
        operation = problem_operations[fingerprint]
        if operation == "existing-exact":
            legacy_path = problem_legacy[fingerprint][0][1]
            if is_legacy_generated(legacy_path):
                if legacy_path in current_text:
                    (output / f"{problem_id}.md").write_text(current_text[legacy_path])
                elif (root / legacy_path).is_file():
                    (output / f"{problem_id}.md").write_text((root / legacy_path).read_text())
            continue
        if operation in {"current-output", "ledger-recovered"}:
            for card_id, legacy_path in problem_legacy[fingerprint]:
                if legacy_path in current_text:
                    (output / f"{problem_id}.md").write_text(current_text[legacy_path])
                    break
                if is_owned_output(legacy_path) and card_id in current_text_by_id:
                    (output / f"{problem_id}.md").write_text(current_text_by_id[card_id])
                    break
                if is_legacy_generated(legacy_path) and (root / legacy_path).is_file():
                    (output / f"{problem_id}.md").write_text((root / legacy_path).read_text())
                    break
            else:
                operation = "regenerate"
        if operation in {"ambiguous-exact", "new", "regenerate"}:
            area, topics = problem_details[fingerprint]
            statement = next(record["question"] for record in records if record["normalized"] == fingerprint)
            write_problem(output / f"{problem_id}.md", statement, area, topics, problem_id, problem_bodies[fingerprint])

    # A sitting the corpus already records keeps its own `source` card; this
    # import contributes its occurrences to it. Only a sitting no other source
    # has recorded gets an `SRC-MMAQ-*` card of its own.
    sitting_ids: dict[tuple[str, str, str, str], str] = {}
    sitting_titles: dict[tuple[str, str, str, str], str] = {}
    joined = 0
    for key in groups:
        existing = join_sitting(native, key)
        if existing is None:
            sitting_ids[key], sitting_titles[key] = source_id(key), source_title(key)
            continue
        sitting_ids[key], sitting_titles[key] = existing
        joined += 1

    for key, group in groups.items():
        if sitting_ids[key] != source_id(key):
            continue
        write_source(output / f"{source_id(key)}.md", key, len(group), source, source_bodies[key])

    ledger: list[dict[str, Any]] = []
    for record in records:
        fingerprint = record["normalized"]
        problem_id = problem_ids[fingerprint]
        occurrence_id = f"O-MMAQ-{record['sequence']:06d}"
        write_occurrence(
            output / f"{occurrence_id}.md",
            record,
            sitting_ids[source_key(record)],
            problem_id,
            occurrence_id,
            occurrence_bodies[record["sequence"] - 1],
            sitting_titles[source_key(record)],
        )
        legacy = problem_history[fingerprint]
        ledger.append(
            {
                "row": record["sequence"],
                "source_key": list(source_key(record)),
                "source_id": sitting_ids[source_key(record)],
                "problem_id": problem_id,
                "occurrence_id": occurrence_id,
                "locator": str(record["number"]) if str(record["number"]) not in {"", "0"} else f"row-{record['sequence']:04d}",
                "statement_sha256": hashlib.sha256(record["question"].encode("utf-8")).hexdigest(),
                "match": problem_matches[fingerprint],
                "legacy_problem_ids": [card_id for card_id, _ in legacy],
                "legacy_problem_paths": [path for _, path in legacy],
                "source_revision": source["revision"],
                "source_sha256": source["sha256"],
            }
        )

    ledger_path = root / LEDGER_NAME
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    ledger_path.write_text("".join(json.dumps(item, sort_keys=True) + "\n" for item in ledger))

    summary = {
        "source": source,
        "rows": len(records),
        "source_groups": len(groups),
        "joined_existing_sittings": joined,
        "unique_statements": len(problem_ids),
        "existing_exact": sum(1 for value in problem_matches.values() if value == "existing-exact"),
        "ambiguous_exact": sum(1 for value in problem_matches.values() if value == "ambiguous-exact"),
        "new_problems": sum(1 for value in problem_matches.values() if value == "new"),
        "occurrences": len(records),
    }
    (output / "manifest.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    return {key: value for key, value in summary.items() if isinstance(value, int)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="import_mmaq")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    records, source = load_records(root, args.input)
    with PandocServer() as pandoc:
        counts = reconcile(root, records, source, pandoc)
    print(
        f"{counts['rows']} source rows -> {counts['unique_statements']} unique problems, "
        f"{counts['occurrences']} occurrences across {counts['source_groups']} source groups "
        f"({counts['existing_exact']} exact existing, {counts['new_problems']} new, "
        f"{counts['ambiguous_exact']} ambiguous)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
