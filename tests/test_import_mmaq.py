"""The MakeMeAQual importer proves a total, stable source-to-corpus join."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

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


def _run(root: Path, source: Path) -> None:
    subprocess.run(
        [sys.executable, str(IMPORTER), "--root", str(root), "--input", str(source)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )


def test_importer_reconciles_rows_dates_and_idempotently_preserves_unrelated_files(tmp_path: Path) -> None:
    """The real CLI owns row identity, date interpretation, and additive writes."""

    source = tmp_path / "Combined_Questions.yaml"
    _fixture(source)
    (tmp_path / "corpus/imports").mkdir(parents=True)
    (tmp_path / "vocabularies").mkdir()
    (tmp_path / "vocabularies/topics.yaml").write_text("[]\n")
    keep = tmp_path / "corpus/imports/keep.txt"
    keep.write_text("user-owned marker\n")

    _run(tmp_path, source)
    manifest = json.loads((tmp_path / "corpus/imports/mmaq-total/manifest.json").read_text())
    assert manifest["rows"] == 5
    assert manifest["unique_statements"] == 4
    assert manifest["occurrences"] == 5
    assert manifest["source_groups"] == 4
    assert len(list((tmp_path / "corpus/imports/mmaq-total").glob("O-*.md"))) == 5
    assert len(list((tmp_path / "corpus/imports/mmaq-total").glob("P-*.md"))) == 4
    assert len(list((tmp_path / "corpus/imports/mmaq-total").glob("SRC-*.md"))) == 4
    assert keep.read_text() == "user-owned marker\n"

    ledger = [json.loads(line) for line in (tmp_path / "sources/mmaq-reconciliation.jsonl").read_text().splitlines()]
    assert [item["row"] for item in ledger] == [1, 2, 3, 4, 5]
    assert ledger[0]["problem_id"] == ledger[1]["problem_id"]
    assert ledger[0]["locator"] == "1"
    assert ledger[3]["locator"] == "row-0004"

    sources = {path.stem: _meta(path)["payload"]["date"] for path in (tmp_path / "corpus/imports/mmaq-total").glob("SRC-*.md")}
    assert sources["SRC-MMAQ-UGA-ALG-2018-SPRING"] == {"kind": "academic-term", "year": 2018, "term": "spring"}
    assert sources["SRC-MMAQ-NUS-RA-1970-SPRING"] == {"kind": "term", "term": "spring"}
    assert sources["SRC-MMAQ-UGA-TOP-UNKNOWN-NA"] == {"kind": "unknown"}
    assert sources["SRC-MMAQ-UGA-CA-EXTRA-NA"] == {"kind": "unknown"}

    first = _snapshot(tmp_path)
    _run(tmp_path, source)
    assert _snapshot(tmp_path) == first
