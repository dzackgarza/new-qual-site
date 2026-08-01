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


def card(meta: dict[str, Any], body: str) -> str:
    frontmatter = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100).strip()
    return f"---\n{frontmatter}\n---\n\n{body.rstrip()}\n"


def title_of(statement: str) -> str:
    """Take a stable, recognizable title without spawning one Pandoc per row."""

    first = next((line.strip() for line in statement.splitlines() if line.strip()), "")
    first = re.sub(r"^(?:[-*+]\s+|\d+[.)]\s+)", "", first)
    first = re.sub(r"\s+", " ", first).strip()
    if len(first) > 72:
        first = first[:69].rsplit(" ", 1)[0].rstrip() + "…"
    return first or "Imported qualifying-exam problem"


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
        records.append(
            {
                "sequence": sequence,
                "year": year,
                "number": raw["number"],
                "university": university,
                "exam": exam,
                "season": season,
                "tags": [tag.strip() for tag in tags],
                "question": question.strip(),
                "normalized": normalize(question),
            }
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
    return normalize(text)


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


def topic_registry(root: Path, records: list[dict[str, Any]]) -> None:
    path = root / "vocabularies/topics.yaml"
    existing_raw: Any = []
    if path.exists():
        existing_raw = yaml.safe_load(path.read_text())
    if not isinstance(existing_raw, list):
        raise ValueError(f"{path} must contain a YAML list")
    names: dict[str, str] = {}
    for item in existing_raw:
        if not isinstance(item, dict) or "id" not in item or "name" not in item:
            raise ValueError(f"{path} contains a malformed topic entry")
        topic_id = item["id"]
        topic_name = item["name"]
        if not isinstance(topic_id, str) or not isinstance(topic_name, str):
            raise ValueError(f"{path} contains a non-string topic entry")
        names[topic_id] = topic_name
    for record in records:
        for topic_name in record["tags"]:
            topic_id = slug(topic_name)
            if not topic_id:
                raise ValueError(f"empty topic slug for {topic_name!r}")
            if topic_id in names and names[topic_id] != topic_name:
                if names[topic_id].casefold() != topic_name.casefold():
                    raise ValueError(f"topic slug collision: {topic_id!r} names {names[topic_id]!r} and {topic_name!r}")
                continue
            names[topic_id] = topic_name
    entries = [{"id": topic_id, "name": names[topic_id]} for topic_id in sorted(names)]
    path.write_text("# Topics. A registry, not a schema enum: a new topic is a new entry here.\n" + yaml.safe_dump(entries, sort_keys=False, allow_unicode=True))


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
) -> None:
    area = AREA_SLUG[record["exam"]]
    topics = list(dict.fromkeys(slug(tag) for tag in record["tags"]))
    number = str(record["number"])
    locator = number if number not in {"", "0"} else f"row-{record['sequence']:04d}"
    metadata = {
        "schema": "qual/card@1",
        "id": occurrence_id,
        "kind": "occurrence",
        "title": f"{source_title(source_key(record))}, problem {locator}",
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
            prior_ids = {prior_id} if prior_id is not None else set()
            preserved_ids = prior_ids | {candidate_id for candidate_id, _ in current_candidates}
            while problem_id in used_ids and problem_id not in preserved_ids and not (len(candidates) == 1 and problem_id == candidates[0][0]):
                problem_id = opaque("P-MMAQ-", fingerprint + problem_id)
            used_ids.add(problem_id)
            problem_ids[fingerprint] = problem_id
            problem_operations[fingerprint] = operation
            if prior_entry is not None and problem_id == prior_id:
                problem_matches[fingerprint] = prior_entry["match"]
                problem_history[fingerprint] = list(
                    zip(prior_entry["legacy_problem_ids"], prior_entry["legacy_problem_paths"], strict=True)
                )
            else:
                problem_matches[fingerprint] = operation
                problem_history[fingerprint] = legacy
            problem_legacy[fingerprint] = legacy
            area = AREA_SLUG[record["exam"]]
            topics = list(dict.fromkeys(slug(tag) for tag in record["tags"]))
            problem_details[fingerprint] = (area, topics)

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

    for key, group in groups.items():
        write_source(output / f"{source_id(key)}.md", key, len(group), source, source_bodies[key])

    ledger: list[dict[str, Any]] = []
    for record in records:
        fingerprint = record["normalized"]
        problem_id = problem_ids[fingerprint]
        occurrence_id = f"O-MMAQ-{record['sequence']:06d}"
        write_occurrence(
            output / f"{occurrence_id}.md",
            record,
            source_id(source_key(record)),
            problem_id,
            occurrence_id,
            occurrence_bodies[record["sequence"] - 1],
        )
        legacy = problem_history[fingerprint]
        ledger.append(
            {
                "row": record["sequence"],
                "source_key": list(source_key(record)),
                "source_id": source_id(source_key(record)),
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
    topic_registry(root, records)

    summary = {
        "source": source,
        "rows": len(records),
        "source_groups": len(groups),
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
