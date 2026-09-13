from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "tools" / "extraction_detector.py"


def card(body: str, card_id: str = "P-TEST") -> str:
    return f"""---
id: {card_id}
kind: problem
---

::: {{.problem}}
{body}
:::
"""


def run_detector(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(root), *args],
        text=True,
        capture_output=True,
        check=False,
    )


def git(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=repo, text=True, capture_output=True, check=True)


def write_card(root: Path, body: str, card_id: str = "P-TEST") -> Path:
    path = root / "corpus" / "collections" / "SRC-TEST" / f"{card_id}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(card(body, card_id))
    return path


def init_repo(tmp_path: Path, body: str) -> tuple[Path, Path]:
    repo = tmp_path / "repo"
    path = write_card(repo, body)
    git(repo, "init", "-q")
    git(repo, "config", "user.name", "Test")
    git(repo, "config", "user.email", "test@example.invalid")
    git(repo, "add", ".")
    git(repo, "-c", "core.hooksPath=/dev/null", "commit", "-q", "-m", "base")
    return repo, path


def test_report_ignores_unicode_math_inside_dollar_spans(tmp_path: Path) -> None:
    write_card(tmp_path, r"Let $H\cap K$ be a subgroup and $A\subseteq B$.")
    result = run_detector(tmp_path)
    assert result.returncode == 0
    assert "Extraction detector: 0 problem card(s)" in result.stdout


def test_report_lists_unicode_math_outside_dollar_spans(tmp_path: Path) -> None:
    write_card(tmp_path, "Let H∩K be a subgroup of G.")
    result = run_detector(tmp_path)
    assert result.returncode == 0
    assert "Extraction detector: 1 problem card(s)" in result.stdout
    assert "P-TEST: ∩ (1)" in result.stdout


def test_report_recognizes_exercise_and_compact_problem_fences(tmp_path: Path) -> None:
    exercise = write_card(tmp_path, "Let x∈A.", "P-EXERCISE")
    exercise.write_text(card("Let x∈A.", "P-EXERCISE").replace("::: {.problem}", "::: exercise"))
    compact = write_card(tmp_path, "Let y∉B.", "P-COMPACT")
    compact.write_text(card("Let y∉B.", "P-COMPACT").replace("::: {.problem}", ":::{.problem}"))

    result = run_detector(tmp_path)

    assert result.returncode == 0
    assert "Extraction detector: 2 problem card(s)" in result.stdout
    assert "P-EXERCISE: ∈ (1)" in result.stdout
    assert "P-COMPACT: ∉ (1)" in result.stdout


def test_report_ignores_non_math_unicode_prose(tmp_path: Path) -> None:
    write_card(tmp_path, "Prove the author’s claim about Café spaces.")
    result = run_detector(tmp_path)
    assert result.returncode == 0
    assert "Extraction detector: 0 problem card(s)" in result.stdout


def test_staged_gate_rejects_new_finding(tmp_path: Path) -> None:
    repo, path = init_repo(tmp_path, r"Let $x\in A$.")
    path.write_text(card("Let x∈A."))
    git(repo, "add", str(path.relative_to(repo)))
    result = run_detector(repo, "--staged-gate")
    assert result.returncode == 1
    assert "extraction findings 0 -> 1" in result.stderr


def test_staged_gate_allows_legacy_finding_to_decrease(tmp_path: Path) -> None:
    repo, path = init_repo(tmp_path, "Let x∈A and A⊆B.")
    path.write_text(card(r"Let x∈A and $A\subseteq B$."))
    git(repo, "add", str(path.relative_to(repo)))
    result = run_detector(repo, "--staged-gate")
    assert result.returncode == 0


def test_staged_gate_allows_unrelated_edit_with_same_legacy_count(tmp_path: Path) -> None:
    repo, path = init_repo(tmp_path, "Let x∈A.")
    path.write_text(card("Let x∈A. Prove the claim."))
    git(repo, "add", str(path.relative_to(repo)))
    result = run_detector(repo, "--staged-gate")
    assert result.returncode == 0
