"""The compiler requires the authored corpus tree."""

from __future__ import annotations

from pathlib import Path

from conftest import fixture_repo, run_qualc


def test_check_rejects_missing_corpus(tmp_path: Path) -> None:
    root = fixture_repo(tmp_path)
    (root / "corpus").rename(root / "corpus-hidden")

    result = run_qualc("check", root)

    assert result.returncode != 0
    assert "corpus" in result.stderr
