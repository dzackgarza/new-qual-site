"""`just check-staged` is the local command that validates the cards staged for commit."""

from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARD = (ROOT / "tests/fixtures/kinds/PRB-INDEXP.md").read_text()


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True).stdout


def test_just_check_staged_rejects_an_invalid_staged_card(tmp_path: Path) -> None:
    git(tmp_path, "init", "-q")
    git(tmp_path, "config", "user.name", "Card validation test")
    git(tmp_path, "config", "user.email", "card-validation@example.invalid")
    git(tmp_path, "config", "commit.gpgsign", "false")
    card = tmp_path / "corpus/card.md"
    card.parent.mkdir()
    card.write_text(CARD)
    git(tmp_path, "add", "corpus")
    git(tmp_path, "commit", "-qm", "initial card")

    def check_staged() -> subprocess.CompletedProcess[str]:
        command = ["just", "--justfile", str(ROOT / "justfile"), "--working-directory", str(tmp_path), "check-staged"]
        return subprocess.run(command, capture_output=True, text=True)

    card.write_text(CARD + "\nAn authored remark.\n")
    git(tmp_path, "add", "corpus")
    assert check_staged().returncode == 0

    card.write_text(CARD.replace("title:", "title: Series: ", 1))
    git(tmp_path, "add", "corpus")
    result = check_staged()

    assert result.returncode == 1
    assert "corpus/card.md" in result.stderr
    assert "mapping values are not allowed" in result.stderr
