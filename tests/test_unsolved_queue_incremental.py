from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from conftest import fixture_repo

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "tools" / "unsolved_queue.py"


def problem(card_id: str, title: str, *, solved: bool) -> str:
    solution = "\n::: {.solution}\nDone.\n:::\n" if solved else ""
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
{solution}"""


def run_queue(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(repo), *args],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )


def test_incremental_staged_matches_full_rebuild_when_solution_state_changes(tmp_path: Path) -> None:
    repo = fixture_repo(tmp_path)
    collection = repo / "corpus" / "collections" / "SRC-INCR"
    collection.mkdir(parents=True)
    (collection / "P-INCR-GAIN.md").write_text(problem("P-INCR-GAIN", "Gains a solution", solved=False))
    (collection / "P-INCR-LOSE.md").write_text(problem("P-INCR-LOSE", "Loses a solution", solved=True))
    (repo / "queues").mkdir()
    baseline = run_queue(repo)
    assert baseline.returncode == 0, baseline.stdout + baseline.stderr

    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=repo, check=True)
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "commit", "-qm", "baseline"], cwd=repo, check=True)

    gain = repo / "corpus" / "collections" / "SRC-INCR" / "P-INCR-GAIN.md"
    lose = repo / "corpus" / "collections" / "SRC-INCR" / "P-INCR-LOSE.md"
    gain.write_text(problem("P-INCR-GAIN", "Gains a solution", solved=True))
    lose.write_text(problem("P-INCR-LOSE", "Loses a solution", solved=False))
    subprocess.run(["git", "add", str(gain.relative_to(repo)), str(lose.relative_to(repo))], cwd=repo, check=True)

    incremental = run_queue(repo, "--incremental-staged")
    assert incremental.returncode == 0, incremental.stdout + incremental.stderr
    incremental_bytes = (repo / "queues" / "C-unsolved-cards.md").read_bytes()

    full = run_queue(repo)
    assert full.returncode == 0, full.stdout + full.stderr
    assert incremental_bytes == (repo / "queues" / "C-unsolved-cards.md").read_bytes()
    text = incremental_bytes.decode()
    assert "P-INCR-GAIN" not in text
    assert 'P-INCR-LOSE — "Loses a solution"' in text


def test_incremental_range_matches_full_rebuild_over_committed_changes(tmp_path: Path) -> None:
    """At push time Queue C is updated from the commits being pushed, not the index."""
    repo = fixture_repo(tmp_path)
    collection = repo / "corpus" / "collections" / "SRC-INCR"
    collection.mkdir(parents=True)
    (collection / "P-INCR-GAIN.md").write_text(problem("P-INCR-GAIN", "Gains a solution", solved=False))
    (collection / "P-INCR-LOSE.md").write_text(problem("P-INCR-LOSE", "Loses a solution", solved=True))
    (repo / "queues").mkdir()
    assert run_queue(repo).returncode == 0

    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=repo, check=True)
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "commit", "-qm", "baseline"], cwd=repo, check=True)
    base = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, check=True, capture_output=True, text=True).stdout.strip()

    (collection / "P-INCR-GAIN.md").write_text(problem("P-INCR-GAIN", "Gains a solution", solved=True))
    (collection / "P-INCR-LOSE.md").write_text(problem("P-INCR-LOSE", "Loses a solution", solved=False))
    (collection / "P-INCR-NEW.md").write_text(problem("P-INCR-NEW", "Arrives unsolved", solved=False))
    subprocess.run(["git", "add", "corpus"], cwd=repo, check=True)
    subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "commit", "-qm", "content"], cwd=repo, check=True)

    incremental = run_queue(repo, "--incremental-range", base)
    assert incremental.returncode == 0, incremental.stdout + incremental.stderr
    incremental_bytes = (repo / "queues" / "C-unsolved-cards.md").read_bytes()

    full = run_queue(repo)
    assert full.returncode == 0, full.stdout + full.stderr
    assert incremental_bytes == (repo / "queues" / "C-unsolved-cards.md").read_bytes()
    assert 'P-INCR-NEW — "Arrives unsolved"' in incremental_bytes.decode()
