"""Exercise the authoring recipes against real files, Pandoc, and Git."""

from __future__ import annotations

import csv
import io
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KINDS = ROOT / "tests" / "fixtures" / "kinds"


def workspace(tmp_path: Path) -> Path:
    collection = tmp_path / "corpus" / "one exam"
    collection.mkdir(parents=True)
    shutil.copy(KINDS / "EXE-CENTER.md", collection / "open card.md")
    shutil.copy(KINDS / "PRB-INDEXP.md", collection / "solved card.md")
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
    assert [(row["id"], row["path"]) for row in rows(result.stdout)] == [("EXE-CENTER", "corpus/one exam/open card.md")]
    card = collection / "open card.md"
    source = card.read_text()
    assert run(tmp_path, "just", "read-card", str(card)).stdout == source
    solution = (KINDS / "PRB-INDEXP.md").read_text().split("::: solution\n", 1)[1]
    card.write_text(source + "\n::: solution\n" + solution)
    assert rows(run(tmp_path, "just", "unsolved-in", str(collection)).stdout) == []


def test_sampling_reads_current_scope_without_catalog_or_rebuild(tmp_path: Path) -> None:
    collection = workspace(tmp_path)
    (tmp_path / "corpus" / "unrelated-invalid.md").write_text("not a card")
    before = {path: path.read_bytes() for path in collection.glob("*.md")}
    result = run(tmp_path, "just", "sample-unsolved", str(collection), "5")
    assert [row["id"] for row in rows(result.stdout)] == ["EXE-CENTER"]
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
    run(tmp_path, "just", "commit-card", str(target), message)
    assert run(tmp_path, "git", "log", "-1", "--format=%s").stdout.strip() == message
    assert run(tmp_path, "git", "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").stdout.splitlines() == ["corpus/one exam/open card.md"]
    assert run(tmp_path, "git", "show", "HEAD:corpus/one exam/open card.md").stdout == target.read_text()
    assert run(tmp_path, "git", "diff", "--cached").stdout == index_before
    assert not (tmp_path / "hook-invoked").exists()
