from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from conftest import fixture_repo

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "tools" / "unsolved_queue.py"


def unsolved_problem(card_id: str, title: str) -> str:
    return f"""---
schema: qual/card@1
id: {card_id}
kind: problem
title: {title}
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
---

::: {{.problem}}
Prove the claim.
:::
"""


def solved_problem(card_id: str, title: str, *, solution_fence: str = ":::") -> str:
    return unsolved_problem(card_id, title) + f"\n{solution_fence} {{.solution}}\nDone.\n{solution_fence}\n"


def run_queue(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(repo), *args],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )


def test_incremental_range_matches_full_rebuild_over_committed_changes(tmp_path: Path) -> None:
    """At push time Queue C is updated from the commits being pushed, not the index."""
    repo = fixture_repo(tmp_path)
    collection = repo / "corpus" / "collections" / "SRC-INCR"
    collection.mkdir(parents=True)
    (collection / "P-INCR-GAIN.md").write_text(unsolved_problem("P-INCR-GAIN", "Gains a solution"))
    (collection / "P-INCR-LOSE.md").write_text(solved_problem("P-INCR-LOSE", "Loses a solution"))
    (repo / "queues").mkdir()
    assert run_queue(repo).returncode == 0

    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=repo, check=True)
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "commit", "-qm", "baseline"], cwd=repo, check=True)
    base = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, check=True, capture_output=True, text=True).stdout.strip()

    (collection / "P-INCR-GAIN.md").write_text(solved_problem("P-INCR-GAIN", "Gains a solution"))
    (collection / "P-INCR-LOSE.md").write_text(unsolved_problem("P-INCR-LOSE", "Loses a solution"))
    (collection / "P-INCR-NEW.md").write_text(unsolved_problem("P-INCR-NEW", "Arrives unsolved"))
    subprocess.run(["git", "add", "corpus"], cwd=repo, check=True)
    subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "commit", "-qm", "content"], cwd=repo, check=True)

    incremental = run_queue(repo, "--incremental-range", base)
    assert incremental.returncode == 0, incremental.stdout + incremental.stderr
    incremental_bytes = (repo / "queues" / "C-unsolved-cards.md").read_bytes()

    full = run_queue(repo)
    assert full.returncode == 0, full.stdout + full.stderr
    assert incremental_bytes == (repo / "queues" / "C-unsolved-cards.md").read_bytes()
    assert 'P-INCR-NEW — "Arrives unsolved"' in incremental_bytes.decode()


def test_incremental_range_recognizes_nested_solution_fences(tmp_path: Path) -> None:
    repo = fixture_repo(tmp_path)
    collection = repo / "corpus" / "collections" / "SRC-INCR"
    collection.mkdir(parents=True)
    (collection / "P-INCR.md").write_text(unsolved_problem("P-INCR", "Nested solution"))
    (repo / "queues").mkdir()
    assert run_queue(repo).returncode == 0

    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=repo, check=True)
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "commit", "-qm", "baseline"], cwd=repo, check=True)
    base = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, check=True, capture_output=True, text=True).stdout.strip()

    (collection / "P-INCR.md").write_text(solved_problem("P-INCR", "Nested solution", solution_fence=":::::"))
    subprocess.run(["git", "add", "corpus"], cwd=repo, check=True)
    subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "commit", "-qm", "solution"], cwd=repo, check=True)

    incremental = run_queue(repo, "--incremental-range", base)
    assert incremental.returncode == 0, incremental.stdout + incremental.stderr
    incremental_bytes = (repo / "queues" / "C-unsolved-cards.md").read_bytes()

    full = run_queue(repo)
    assert full.returncode == 0, full.stdout + full.stderr
    assert incremental_bytes == (repo / "queues" / "C-unsolved-cards.md").read_bytes()
    assert "P-INCR" not in incremental_bytes.decode()


def test_committed_projection_ignores_malformed_history_and_dirty_cards(tmp_path: Path) -> None:
    """The pushed snapshot determines membership even when its history cannot parse."""
    repo = fixture_repo(tmp_path)
    collection = repo / "corpus" / "collections" / "SRC-INCR"
    collection.mkdir(parents=True)
    changed = collection / "unrelated-filename.md"
    removed = collection / "removed.md"
    renamed = collection / "before.md"
    changed.write_text(unsolved_problem("P-INCR-OLD", "Old identity"))
    removed.write_text(unsolved_problem("P-INCR-REMOVE", "Deleted card"))
    renamed.write_text(unsolved_problem("P-INCR-RENAME", "Renamed card $Format:%H$"))
    (repo / ".gitattributes").write_text("corpus/collections/SRC-INCR/unrelated-filename.md export-ignore\ncorpus/collections/SRC-INCR/after.md export-subst\n")
    (repo / "queues").mkdir()
    assert run_queue(repo).returncode == 0
    changed.write_text(changed.read_text().replace("review: draft", "review: draft\naudit:\n- note: Source states: the complete claim"))
    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=repo, check=True)
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "commit", "-qm", "malformed historical audit"], cwd=repo, check=True)
    base = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, check=True, capture_output=True, text=True).stdout.strip()

    changed.write_text(unsolved_problem("P-INCR-NEW-ID", "Current identity"))
    removed.unlink()
    renamed.rename(collection / "after.md")
    subprocess.run(["git", "add", "corpus"], cwd=repo, check=True)
    subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "commit", "-qm", "repair and rename cards"], cwd=repo, check=True)
    full = run_queue(repo)
    assert full.returncode == 0, full.stdout + full.stderr
    expected = (repo / "queues" / "C-unsolved-cards.md").read_bytes()

    changed.write_text(unsolved_problem("P-STAGED", "Staged identity"))
    subprocess.run(["git", "add", str(changed.relative_to(repo))], cwd=repo, check=True)
    changed.write_text(solved_problem("P-DIRTY", "Uncommitted identity"))
    (collection / "after.md").write_text("---\nmalformed: audit: text\n---\n")
    (collection / "untracked.md").write_text(unsolved_problem("P-UNTRACKED", "Untracked card"))
    result = run_queue(repo, "--incremental-range", base)
    assert result.returncode == 0, result.stdout + result.stderr
    actual = (repo / "queues" / "C-unsolved-cards.md").read_bytes()
    assert actual == expected
    assert 'P-INCR-NEW-ID — "Current identity"'.encode() in actual
    assert 'P-INCR-RENAME — "Renamed card $Format:%H$"'.encode() in actual
    assert b"P-INCR-OLD" not in actual
    assert b"P-INCR-REMOVE" not in actual
    assert b"P-DIRTY" not in actual
    assert b"P-UNTRACKED" not in actual

    assert b"P-STAGED" not in actual

    # A malformed current committed card still rejects queue generation, even
    # though historical malformed YAML no longer participates in the projection.
    changed.write_text(changed.read_text().replace("review: draft", "review: draft\naudit:\n- note: Current states: an invalid mapping"))
    subprocess.run(["git", "add", str(changed.relative_to(repo))], cwd=repo, check=True)
    subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "commit", "-qm", "malformed current audit"], cwd=repo, check=True)
    rejected = run_queue(repo, "--incremental-range", base)
    assert rejected.returncode != 0
    assert (repo / "queues" / "C-unsolved-cards.md").read_bytes() == expected

    changed.write_text(solved_problem("P-INCR-RENAME", "Duplicate solved identity"))
    subprocess.run(["git", "add", str(changed.relative_to(repo))], cwd=repo, check=True)
    subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "commit", "-qm", "duplicate current identity"], cwd=repo, check=True)
    duplicate = run_queue(repo, "--incremental-range", base)
    assert duplicate.returncode != 0
    assert (repo / "queues" / "C-unsolved-cards.md").read_bytes() == expected
