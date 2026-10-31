"""The bibliography mirror requires both authored source trees."""

from __future__ import annotations

from pathlib import Path

import pytest
import sync_bibliography


@pytest.mark.parametrize("missing", ["corpus", "wiki"])
def test_citation_scan_rejects_missing_source_tree(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, missing: str) -> None:
    (tmp_path / ("wiki" if missing == "corpus" else "corpus")).mkdir()
    monkeypatch.setattr(sync_bibliography, "ROOT", tmp_path)

    with pytest.raises(FileNotFoundError, match=missing):
        sync_bibliography.cited_keys()
