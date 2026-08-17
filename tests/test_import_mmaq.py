"""The MakeMeAQual importer proves a total, stable source-to-corpus join."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
IMPORTER = ROOT / "tools/import_mmaq.py"


def _fixture(path: Path) -> None:
    rows = [
        {
            "year": 2018,
            "number": 1,
            "university": "UGA",
            "exam": "Algebra",
            "season": "Spring",
            "tags": ["Groups"],
            "question": "Let $G$ be a finite group. Prove that the identity is unique.",
        },
        {
            "year": 2018,
            "number": 2,
            "university": "UGA",
            "exam": "Algebra",
            "season": "Spring",
            "tags": ["Groups"],
            "question": "  Let $G$ be a finite group. Prove that the identity is unique.  ",
        },
        {
            "year": 1970,
            "number": 1,
            "university": "NUS",
            "exam": "Real_Analysis",
            "season": "spring",
            "tags": ["Sequences"],
            "question": "Show that every convergent sequence is bounded.",
        },
        {
            "year": 0,
            "number": 0,
            "university": "UGA",
            "exam": "Topology",
            "season": "NA",
            "tags": ["Point Set"],
            "question": "Prove that a one-point space is compact.",
        },
        {
            "year": "Extra",
            "number": 0,
            "university": "UGA",
            "exam": "Complex_Analysis",
            "tags": ["Residues"],
            "question": "Compute the residue of $1/z$ at zero.",
        },
    ]
    path.write_text(yaml.safe_dump(rows, sort_keys=False, allow_unicode=True))


def _meta(path: Path) -> dict[str, Any]:
    pieces = path.read_text().split("---\n", 2)
    raw = yaml.safe_load(pieces[1])
    assert isinstance(raw, dict)
    return raw


def _snapshot(root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted((root / "corpus/imports/mmaq-total").rglob("*")):
        if path.is_file():
            result[str(path.relative_to(root))] = hashlib.sha256(path.read_bytes()).hexdigest()
    ledger = root / "sources/mmaq-reconciliation.jsonl"
    result[str(ledger.relative_to(root))] = hashlib.sha256(ledger.read_bytes()).hexdigest()
    return result


def _vocabulary(root: Path, topics: list[str], aliases: list[dict[str, str]] | None = None) -> None:
    """Seed the curated topic vocabulary the importer reads and never writes."""
    directory = root / "vocabularies"
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "topics.yaml").write_text(yaml.safe_dump([{"id": t, "name": t} for t in topics]))
    (directory / "topic-aliases.yaml").write_text(yaml.safe_dump(aliases or []))


def _run(root: Path, source: Path) -> None:
    subprocess.run(
        [sys.executable, str(IMPORTER), "--root", str(root), "--input", str(source)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )


def test_importer_reconciles_rows_dates_and_idempotently_preserves_unrelated_files(
    tmp_path: Path,
) -> None:
    """The real CLI owns row identity, date interpretation, and additive writes."""

    source = tmp_path / "Combined_Questions.yaml"
    _fixture(source)
    _vocabulary(tmp_path, ["groups", "sequences", "point-set", "residues"])
    (tmp_path / "corpus/imports").mkdir(parents=True)
    keep = tmp_path / "corpus/imports/keep.txt"
    keep.write_text("user-owned marker\n")
    legacy = tmp_path / "corpus/imports/mmaq-full"
    legacy.mkdir()
    legacy_meta = {
        "schema": "qual/card@1",
        "id": "P-OLD",
        "kind": "problem",
        "title": "Legacy exact problem",
        "classification": {"areas": ["algebra"], "topics": ["groups"]},
        "relations": [],
        "review": "draft",
        "solved": False,
    }
    (legacy / "P-OLD.md").write_text(
        "---\n" + yaml.safe_dump(legacy_meta, sort_keys=False) + "---\n\n::: problem\nLet $G$ be a finite group. Prove that the identity is unique.\n:::\n"
    )

    _run(tmp_path, source)
    manifest = json.loads((tmp_path / "corpus/imports/mmaq-total/manifest.json").read_text())
    assert manifest["rows"] == 5
    assert manifest["unique_statements"] == 4
    assert manifest["occurrences"] == 5
    assert manifest["source_groups"] == 4
    assert len(list((tmp_path / "corpus/imports/mmaq-total").glob("O-*.md"))) == 5
    assert len(list((tmp_path / "corpus/imports/mmaq-total").glob("P-*.md"))) == 4
    assert len(list((tmp_path / "corpus/imports/mmaq-total").glob("SRC-*.md"))) == 4
    assert (tmp_path / "corpus/imports/mmaq-total/P-OLD.md").read_text() == (legacy / "P-OLD.md").read_text()
    assert keep.read_text() == "user-owned marker\n"

    ledger = [json.loads(line) for line in (tmp_path / "sources/mmaq-reconciliation.jsonl").read_text().splitlines()]
    assert [item["row"] for item in ledger] == [1, 2, 3, 4, 5]
    assert ledger[0]["problem_id"] == ledger[1]["problem_id"]
    assert ledger[0]["locator"] == "1"
    assert ledger[3]["locator"] == "row-0004"

    sources = {path.stem: _meta(path)["payload"]["date"] for path in (tmp_path / "corpus/imports/mmaq-total").glob("SRC-*.md")}
    assert sources["SRC-MMAQ-UGA-ALG-2018-SPRING"] == {
        "kind": "academic-term",
        "year": 2018,
        "term": "spring",
    }
    assert sources["SRC-MMAQ-NUS-RA-1970-SPRING"] == {"kind": "term", "term": "spring"}
    assert sources["SRC-MMAQ-UGA-TOP-UNKNOWN-NA"] == {"kind": "unknown"}
    assert sources["SRC-MMAQ-UGA-CA-EXTRA-NA"] == {"kind": "unknown"}

    first = _snapshot(tmp_path)
    _run(tmp_path, source)
    assert _snapshot(tmp_path) == first


def test_a_retired_topic_resolves_to_its_survivor_and_an_unregistered_one_stops_the_import(
    tmp_path: Path,
) -> None:
    """Registry merges are curation: the importer honours them and never writes them."""

    source = tmp_path / "Combined_Questions.yaml"
    _fixture(source)
    (tmp_path / "corpus/imports").mkdir(parents=True)
    # "Point Set" slugs to point-set, which this registry retired in favour of point-set-topology.
    _vocabulary(
        tmp_path,
        ["groups", "sequences", "point-set-topology", "residues"],
        [{"retired": "point-set", "survivor": "point-set-topology"}],
    )
    registry_before = (tmp_path / "vocabularies/topics.yaml").read_text()

    _run(tmp_path, source)
    topics = {topic for path in (tmp_path / "corpus/imports/mmaq-total").glob("O-*.md") for topic in _meta(path)["classification"]["topics"]}
    assert "point-set-topology" in topics
    assert "point-set" not in topics
    assert (tmp_path / "vocabularies/topics.yaml").read_text() == registry_before

    # Drop the alias: the tag is now neither registered nor mapped, and the import stops.
    _vocabulary(tmp_path, ["groups", "sequences", "point-set-topology", "residues"])
    with pytest.raises(subprocess.CalledProcessError):
        _run(tmp_path, source)
    sys.path.insert(0, str(ROOT / "tools"))
    from import_mmaq import UnregisteredTopic, load_records

    with pytest.raises(UnregisteredTopic):
        load_records(tmp_path, source)


def test_loose_equates_rendering_spellings_and_separates_different_mathematics() -> None:
    """The corpus's statement identity: same mathematics, whatever the spelling."""

    from import_mmaq import loose

    assert loose(r"Let $\mathbf{Q}$ act.") == loose(r"Let $\mathbb{Q}$ act.")
    assert loose(r"$$\begin{aligned} x &= 1 \end{aligned}$$") == loose(r"\begin{align*} x &= 1 \end{align*}")
    assert loose(r"Evaluate \[ \int f \,dx \]") == loose(r"Evaluate $$\int f \, dx$$")
    assert loose("> Hint: use compactness.") == loose("Hint: use compactness.")
    assert loose(r"`\begin{align*} x = 1 \end{align*}`{=tex}") == loose(r"\begin{align*} x = 1 \end{align*}")

    # Equality, not resemblance: one changed symbol is a different statement.
    assert loose("Show that $f$ is continuous.") != loose("Show that $f$ is differentiable.")
    assert loose("Let $n \\geq 2$.") != loose("Let $n \\geq 3$.")
    assert loose("$x > 0$") != loose("$x 0$")


def test_import_joins_a_sitting_the_corpus_already_records(tmp_path: Path) -> None:
    """One sitting, one source card: a second importer attaches to the first's."""

    source = tmp_path / "Combined_Questions.yaml"
    _fixture(source)
    _vocabulary(tmp_path, ["groups", "sequences", "point-set", "residues"])
    (tmp_path / "corpus/imports").mkdir(parents=True)
    (tmp_path / "corpus/occurrences").mkdir()
    native = {
        "schema": "qual/card@1",
        "id": "SRC-UGA-ALG-SPRING-2018",
        "kind": "source",
        "title": "UGA algebra Spring 2018",
        "classification": {"areas": ["algebra"], "topics": []},
        "relations": [],
        "review": "draft",
        "payload": {
            "source_kind": "university-exam",
            "institution": "uga",
            "area": "algebra",
            "date": {"kind": "academic-term", "year": 2018, "term": "spring"},
        },
    }
    (tmp_path / "corpus/occurrences/SRC-UGA-ALG-SPRING-2018.md").write_text(
        "---\n" + yaml.safe_dump(native, sort_keys=False) + "---\n\n::: remark\nUGA algebra Spring 2018.\n:::\n"
    )

    _run(tmp_path, source)
    output = tmp_path / "corpus/imports/mmaq-total"
    manifest = json.loads((output / "manifest.json").read_text())
    assert manifest["joined_existing_sittings"] == 1
    assert not (output / "SRC-MMAQ-UGA-ALG-2018-SPRING.md").exists()

    ledger = [json.loads(line) for line in (tmp_path / "sources/mmaq-reconciliation.jsonl").read_text().splitlines()]
    assert ledger[0]["source_id"] == "SRC-UGA-ALG-SPRING-2018"
    occurrence = _meta(output / f"{ledger[0]['occurrence_id']}.md")
    assert occurrence["payload"]["source"] == "SRC-UGA-ALG-SPRING-2018"
    assert occurrence["title"].startswith("UGA algebra Spring 2018,")
