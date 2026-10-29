"""Local card validation reads the Git content that will be committed or pushed."""

from __future__ import annotations

import json
import shlex
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
CARD = (ROOT / "tests/fixtures/kinds/PRB-INDEXP.md").read_text()


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True).stdout


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    git(tmp_path, "init", "-q")
    git(tmp_path, "config", "user.name", "Card validation test")
    git(tmp_path, "config", "user.email", "card-validation@example.invalid")
    git(tmp_path, "config", "commit.gpgsign", "false")
    hooks = tmp_path / ".git" / "hooks"
    git(tmp_path, "config", "core.hooksPath", str(hooks))
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    (corpus / "one card.md").write_text(CARD)
    # Unchanged historical defects are outside the local diff's scope.
    (corpus / "unrelated.md").write_text("---\ntitle: Series: invalid\n---\n")
    git(tmp_path, "add", "corpus")
    git(tmp_path, "commit", "-qm", "initial cards")
    return tmp_path


def check(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, "-m", "qualc.authoring", *args], cwd=root, capture_output=True, text=True)


@pytest.mark.parametrize(
    ("source", "diagnostic"),
    [
        (CARD.replace("title:", "title: Series: ", 1), "mapping values are not allowed"),
        (CARD.replace("review: draft", "review: draft\nreview: verified"), "duplicate key"),
        (CARD.replace("kind: problem", "kind: problem\nunrecognised: value"), "extra_forbidden"),
        (CARD.replace("kind: problem", "kind: unrelated"), "union_tag_invalid"),
        (CARD.replace("review: draft", "review: [draft]"), "literal_error"),
        (CARD.replace("id: PRB-INDEXP\n", ""), "Field required"),
        (CARD.replace(":::\n", "", 1), "unclosed fenced div"),
        (CARD.replace("\n\n::: {.hint}", "\n::: {.hint}", 1), "follows text"),
    ],
)
def test_staged_header_errors_cannot_be_hidden_by_a_valid_worktree(repo: Path, source: str, diagnostic: str) -> None:
    card = repo / "corpus/one card.md"
    card.write_text(source)
    git(repo, "add", "corpus/one card.md")
    card.write_text(CARD)

    result = check(repo, "check-staged")

    assert result.returncode == 1, result.stdout
    assert "corpus/one card.md" in result.stderr
    assert diagnostic in result.stderr
    assert git(repo, "show", ":corpus/one card.md") == source
    assert card.read_text() == CARD


def test_staged_validation_ignores_unstaged_edits_and_unrelated_cards(repo: Path) -> None:
    card = repo / "corpus/one card.md"
    staged = CARD + "\nAn authored remark.\n"
    card.write_text(staged)
    git(repo, "add", "corpus/one card.md")
    card.write_text(CARD.replace("title:", "title: Series: ", 1))

    result = check(repo, "check-staged")

    assert result.returncode == 0, result.stderr
    assert "1 changed file(s) checked" in result.stdout
    assert git(repo, "show", ":corpus/one card.md") == staged


def test_outgoing_validation_reads_committed_cards_and_accepts_repairs(repo: Path) -> None:
    base = git(repo, "rev-parse", "HEAD").strip()
    card = repo / "corpus/one card.md"
    card.write_text(CARD.replace("title:", "title: Series: ", 1))
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "hook-free content")
    card.write_text(CARD)
    git(repo, "add", "corpus/one card.md")

    result = check(repo, "check-range", base)

    assert result.returncode == 1
    assert "corpus/one card.md" in result.stderr
    assert "mapping values are not allowed" in result.stderr
    git(repo, "commit", "-qm", "repair title")
    accepted = check(repo, "check-range", base)
    assert accepted.returncode == 0, accepted.stderr


def test_added_renamed_and_deleted_cards_follow_the_outgoing_tree(repo: Path) -> None:
    base = git(repo, "rev-parse", "HEAD").strip()
    renamed = repo / "corpus/renamed card.md"
    (repo / "corpus/one card.md").rename(renamed)
    added = repo / "corpus/added card.md"
    added.write_text(CARD.replace("PRB-INDEXP", "P-ADDED"))
    # Git records deletion without interpreting the deleted malformed card.
    (repo / "corpus/unrelated.md").rename(repo / "retired.txt")
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "update card paths")
    result = check(repo, "check-range", base)
    assert result.returncode == 0, result.stderr
    assert "2 changed file(s) checked" in result.stdout
    renamed.write_text(CARD.replace("title:", "title: Series: ", 1))
    git(repo, "add", "corpus/renamed card.md")
    git(repo, "commit", "-qm", "invalid renamed card")
    rejected = check(repo, "check-range", base)
    assert rejected.returncode == 1
    assert "corpus/renamed card.md" in rejected.stderr


def test_pathspec_commit_validates_its_temporary_index(repo: Path) -> None:
    hook = repo / ".git/hooks/pre-commit"
    hook.write_text(f"#!/bin/sh\nexec {shlex.quote(sys.executable)} -m qualc.authoring check-staged\n")
    hook.chmod(0o755)
    other = repo / "corpus/other.md"
    other.write_text(CARD.replace("title:", "title: Series: ", 1))
    git(repo, "add", "corpus/other.md")
    staged_before = git(repo, "diff", "--cached")
    target = repo / "corpus/one card.md"
    target.write_text(CARD + "\nA reviewed remark.\n")

    git(repo, "commit", "--only", "-qm", "review card", "--", "corpus/one card.md")

    assert git(repo, "show", "HEAD:corpus/one card.md") == target.read_text()
    assert git(repo, "diff", "--cached") == staged_before
    head = git(repo, "rev-parse", "HEAD")
    target.write_text(CARD.replace("title:", "title: Series: ", 1))
    result = subprocess.run(["git", "commit", "--only", "-qm", "invalid card", "--", "corpus/one card.md"], cwd=repo, capture_output=True, text=True)
    assert result.returncode != 0
    assert "corpus/one card.md" in result.stderr
    assert git(repo, "rev-parse", "HEAD") == head
    assert git(repo, "diff", "--cached") == staged_before


def test_shared_push_payload_validates_each_exact_candidate_commit(repo: Path) -> None:
    valid = git(repo, "rev-parse", "HEAD").strip()
    card = repo / "corpus/one card.md"
    card.write_text(CARD.replace("title:", "title: Series: ", 1))
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "invalid candidate")
    invalid = git(repo, "rev-parse", "HEAD").strip()
    card.write_text(CARD)
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "valid HEAD")
    payload = "\n".join(json.dumps({"path": "corpus/one card.md", "version": commit}) for commit in (valid, invalid))

    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts/local-validate.py"), "--mode", "push"],
        cwd=repo,
        input=payload,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert "corpus/one card.md" in result.stderr
    assert "mapping values are not allowed" in result.stderr
