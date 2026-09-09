"""Exercise the authoring recipes against real files, Pandoc, and Git."""

from __future__ import annotations

import csv
import io
import shutil
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
KINDS = ROOT / "tests" / "fixtures" / "kinds"


def workspace(tmp_path: Path) -> Path:
    collection = tmp_path / "corpus" / "one exam"
    collection.mkdir(parents=True)
    shutil.copy(KINDS / "EXE-CENTER.md", collection / "open card.md")
    shutil.copy(KINDS / "PRB-INDEXP.md", collection / "solved card.md")
    for path in collection.glob("*.md"):
        path.write_text(path.read_text().replace("id: EXE-CENTER", "id: E-CENTER").replace("id: PRB-INDEXP", "id: P-INDEXP"))
    source = yaml.safe_load((KINDS / "SRC-UGA-FIX.md").read_text().split("---\n")[1])
    source["source"]["problems"] = ["E-CENTER", "P-INDEXP"]
    (collection / "index.md").write_text("---\n" + yaml.safe_dump(source, sort_keys=False) + "---\n")
    return collection


def run(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    command = ("just", "--justfile", str(ROOT / "justfile"), "--working-directory", str(root), *args[1:]) if args[0] == "just" else args
    result = subprocess.run(command, cwd=root, text=True, capture_output=True)
    assert result.returncode == 0, result.stdout + result.stderr
    return result


def rows(output: str) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO(output), delimiter="\t"))


def test_live_scope_ignores_other_collections_and_tracks_new_solution(tmp_path: Path) -> None:
    collection = workspace(tmp_path)
    (tmp_path / "corpus" / "unrelated-invalid.md").write_text("not a card")
    result = run(tmp_path, "just", "unsolved-in", str(collection))
    assert [(row["id"], row["path"]) for row in rows(result.stdout)] == [("E-CENTER", "corpus/one exam/open card.md")]
    card = collection / "open card.md"
    source = card.read_text()
    assert run(tmp_path, "just", "read-card", str(card)).stdout.endswith(source)
    solution = (KINDS / "PRB-INDEXP.md").read_text().split("::: solution\n", 1)[1]
    card.write_text(source + "\n::: solution\n" + solution)
    assert rows(run(tmp_path, "just", "unsolved-in", str(collection)).stdout) == []


def test_sampling_reads_current_scope_without_catalog_or_rebuild(tmp_path: Path) -> None:
    collection = workspace(tmp_path)
    (tmp_path / "corpus" / "unrelated-invalid.md").write_text("not a card")
    before = {path: path.read_bytes() for path in collection.glob("*.md")}
    result = run(tmp_path, "just", "sample-unsolved", str(collection), "5")
    assert [row["id"] for row in rows(result.stdout)] == ["E-CENTER"]
    assert {path: path.read_bytes() for path in collection.glob("*.md")} == before
    assert not (tmp_path / "build").exists()


def test_card_commit_preserves_other_staged_work_and_skips_hook(tmp_path: Path) -> None:
    collection = workspace(tmp_path)
    run(tmp_path, "git", "init", "-q")
    run(tmp_path, "git", "config", "user.name", "Authoring recipe test")
    run(tmp_path, "git", "config", "user.email", "authoring@example.invalid")
    run(tmp_path, "git", "config", "commit.gpgsign", "false")
    hooks = tmp_path / "hooks"
    hooks.mkdir()
    run(tmp_path, "git", "config", "core.hooksPath", str(hooks))
    run(tmp_path, "git", "add", "corpus")
    run(tmp_path, "git", "commit", "-qm", "initial cards")
    hook = hooks / "pre-commit"
    hook.write_text("#!/bin/sh\necho invoked > hook-invoked\nexit 1\n")
    hook.chmod(0o755)
    target = collection / "open card.md"
    other = collection / "solved card.md"
    target.write_text(target.read_text() + "\nAn authored remark.\n")
    other.write_text(other.read_text() + "\nConcurrent authored work.\n")
    run(tmp_path, "git", "add", str(other))
    index_before = run(tmp_path, "git", "diff", "--cached").stdout
    message = "docs: review one card's statement; $(literal)"
    assert run(tmp_path, "just", "path-card", "E-CENTER").stdout.strip() == "corpus/one exam/open card.md"
    assert "An authored remark." in run(tmp_path, "just", "diff-card", "E-CENTER").stdout
    run(tmp_path, "just", "commit-card", "E-CENTER", message)
    assert run(tmp_path, "git", "log", "-1", "--format=%s").stdout.strip() == message
    assert run(tmp_path, "git", "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").stdout.splitlines() == ["corpus/one exam/open card.md"]
    assert run(tmp_path, "git", "show", "HEAD:corpus/one exam/open card.md").stdout == target.read_text()
    assert run(tmp_path, "git", "diff", "--cached").stdout == index_before
    assert not (tmp_path / "hook-invoked").exists()


def collection_workspace(root: Path) -> Path:
    collection = workspace(root)
    source = yaml.safe_load((KINDS / "SRC-NEILNOTES.md").read_text().split("---\n")[1])
    source["source"]["sections"] = [
        {"name": "Exam B (p. 9)", "problems": [{"id": "E-CENTER", "comment": "Problem 7"}, "P-INDEXP"]},
        {"name": "Exam A (p. 2)", "problems": ["E-CENTER"]},
    ]
    source["provenance"] = ["assets/attachments/Exam packet.pdf", "https://example.invalid/exam"]
    index = collection / "index.md"
    index.write_text("---\n" + yaml.safe_dump(source, sort_keys=False) + "---\n")
    elsewhere = root / "corpus" / "another directory"
    elsewhere.mkdir()
    (collection / "open card.md").rename(elsewhere / "arbitrary filename.md")
    extraction = root / "assets" / "attachments" / "extracted" / "Exam packet.md"
    extraction.parent.mkdir(parents=True)
    extraction.write_text("Preserved exam extraction\n")
    return index


def test_collection_listing_follows_membership_order_and_live_solutions(tmp_path: Path) -> None:
    index = collection_workspace(tmp_path)
    listing = rows(run(tmp_path, "just", "list-cards", "SRC-NEILNOTES").stdout)
    assert [(row["id"], row["section"], row["position"], row["comment"]) for row in listing] == [
        ("E-CENTER", "Exam B (p. 9)", "1", "Problem 7"),
        ("P-INDEXP", "Exam B (p. 9)", "2", ""),
        ("E-CENTER", "Exam A (p. 2)", "1", ""),
    ]
    assert listing[0]["path"] == "corpus/another directory/arbitrary filename.md"
    sampled = rows(run(tmp_path, "just", "sample-unsolved", "SRC-NEILNOTES", "1").stdout)
    assert [(row["id"], row["section"]) for row in sampled] == [("E-CENTER", "Exam B (p. 9)"), ("E-CENTER", "Exam A (p. 2)")]
    assert [row["id"] for row in rows(run(tmp_path, "just", "unsolved-in", str(index.parent), "Exam B (p. 9)").stdout)] == ["E-CENTER"]
    card = tmp_path / listing[0]["path"]
    solution = (KINDS / "PRB-INDEXP.md").read_text().split("::: solution\n", 1)[1]
    card.write_text(card.read_text() + "\n::: solution\n" + solution)
    assert rows(run(tmp_path, "just", "unsolved-in", "SRC-NEILNOTES").stdout) == []
    assert not (tmp_path / "build").exists()


def test_read_by_id_includes_all_appearances_sources_and_exact_card(tmp_path: Path) -> None:
    collection_workspace(tmp_path)
    card = tmp_path / "corpus" / "another directory" / "arbitrary filename.md"
    result = run(tmp_path, "just", "read-card", "E-CENTER").stdout
    assert result.endswith(card.read_text())
    for recorded in (
        "SRC-NEILNOTES",
        "Exam B (p. 9)",
        "Exam A (p. 2)",
        "Problem 7",
        "assets/attachments/Exam packet.pdf",
        "assets/attachments/extracted/Exam packet.md",
        "https://example.invalid/exam",
    ):
        assert recorded in result
    assert "E-CENTER: schema and Markdown parsing OK" in run(tmp_path, "just", "check-card", "E-CENTER").stdout


def test_nested_collection_keeps_source_ownership_and_rejects_cycles(tmp_path: Path) -> None:
    index = collection_workspace(tmp_path)
    parent = yaml.safe_load(index.read_text().split("---\n")[1])
    parent["source"]["sections"] = [{"name": "Workshop day 2", "problems": [{"id": "SRC-UGA-FIX", "comment": "Exam sheet"}]}]
    index.write_text("---\n" + yaml.safe_dump(parent, sort_keys=False) + "---\n")
    child = yaml.safe_load((KINDS / "SRC-UGA-FIX.md").read_text().split("---\n")[1])
    child["source"]["problems"] = [{"id": "E-CENTER", "comment": "Question III"}]
    child["provenance"] = ["https://example.invalid/child-exam.pdf"]
    child_path = tmp_path / "corpus" / "child.md"
    child_path.write_text("---\n" + yaml.safe_dump(child, sort_keys=False) + "---\n")
    listing = rows(run(tmp_path, "just", "list-cards", "SRC-NEILNOTES").stdout)
    assert [(row["id"], row["collection"], row["comment"], row["via"]) for row in listing] == [
        ("E-CENTER", "SRC-UGA-FIX", "Question III", "SRC-NEILNOTES / Workshop day 2 / entry 1 / Exam sheet")
    ]
    context = run(tmp_path, "just", "read-card", "E-CENTER").stdout
    assert "SRC-NEILNOTES / Workshop day 2 / entry 1 / Exam sheet > SRC-UGA-FIX / entry 1 / Question III" in context
    child_context = context.split("SRC-UGA-FIX: UGA Algebra qualifying exam, Spring 2019", 1)[1]
    assert "PDF source: https://example.invalid/child-exam.pdf" in child_context.split("--- Authored card ---", 1)[0]
    parent["source"]["sections"][0]["problems"] = ["SRC-NEILNOTES"]
    index.write_text("---\n" + yaml.safe_dump(parent, sort_keys=False) + "---\n")
    result = subprocess.run(("just", "--justfile", str(ROOT / "justfile"), "--working-directory", str(tmp_path), "list-cards", "SRC-NEILNOTES"), text=True, capture_output=True)
    assert result.returncode != 0
    assert "Collection cycle: SRC-NEILNOTES -> SRC-NEILNOTES" in result.stderr
    assert result.stdout == ""


def test_ambiguous_id_and_unresolved_membership_fail_before_output(tmp_path: Path) -> None:
    index = collection_workspace(tmp_path)
    card = tmp_path / "corpus" / "another directory" / "arbitrary filename.md"
    duplicate = tmp_path / "corpus" / "duplicate.md"
    duplicate.write_text(card.read_text())
    result = subprocess.run(
        ("just", "--justfile", str(ROOT / "justfile"), "--working-directory", str(tmp_path), "commit-card", "E-CENTER", "must not commit"),
        text=True,
        capture_output=True,
    )
    assert result.returncode != 0
    assert "Ambiguous card ID E-CENTER" in result.stderr
    assert str(card) in result.stderr and str(duplicate) in result.stderr
    source = yaml.safe_load(index.read_text().split("---\n")[1])
    source["source"]["sections"][0]["problems"] = ["P-MISSING"]
    index.write_text("---\n" + yaml.safe_dump(source, sort_keys=False) + "---\n")
    result = subprocess.run(
        ("just", "--justfile", str(ROOT / "justfile"), "--working-directory", str(tmp_path), "list-cards", "SRC-NEILNOTES", "Exam B (p. 9)"),
        text=True,
        capture_output=True,
    )
    assert result.returncode != 0
    assert "Cannot resolve card ID or corpus path: P-MISSING" in result.stderr
    assert result.stdout == ""
