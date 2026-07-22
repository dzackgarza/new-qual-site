"""The architecture's load-bearing claim, as a runnable check.

Source layout, semantic structure, and publication structure are independent.
If moving a card between contributor subtrees changed the catalog, the corpus
tree would secretly be part of the data model.
"""

from __future__ import annotations

import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def catalog_rows(root: Path) -> dict[str, list[tuple]]:
    subprocess.run(
        [sys.executable, "-m", "qualc", "build", "--root", str(root)],
        check=True,
        capture_output=True,
    )
    con = sqlite3.connect(root / "build" / "catalog.sqlite")
    return {
        # source_path is excluded: it is a diagnostic, not identity
        "cards": con.execute("select id, kind, title, review, ast from cards order by id").fetchall(),
        "classifications": con.execute("select * from classifications order by 1,2,3").fetchall(),
        "relations": con.execute("select * from relations order by 1,2,3").fetchall(),
        "occurrences": con.execute("select * from occurrences order by id").fetchall(),
        "sources": con.execute("select * from sources order by id").fetchall(),
        "sections": con.execute("select * from sections order by 1,3").fetchall(),
    }


def test_corpus_layout_is_semantically_inert(tmp_path: Path) -> None:
    work = tmp_path / "repo"
    for sub in ("corpus", "vocabularies", "publications", "site"):
        shutil.copytree(ROOT / sub, work / sub)
    before = catalog_rows(work)

    # Reorganize the corpus the way a contributor might: flatten every card into
    # one flat pile with unrecognizable filenames.
    flat = work / "flat"
    flat.mkdir()
    for i, card in enumerate(sorted((work / "corpus").rglob("*.md"))):
        card.rename(flat / f"{i:04d}.md")
    shutil.rmtree(work / "corpus")
    flat.rename(work / "corpus")

    assert catalog_rows(work) == before


def test_unknown_metadata_field_is_rejected(tmp_path: Path) -> None:
    work = tmp_path / "repo"
    for sub in ("corpus", "vocabularies", "publications", "site"):
        shutil.copytree(ROOT / sub, work / sub)
    card = next((work / "corpus").rglob("P-*.md"))
    card.write_text(card.read_text().replace("review: draft", "review: draft\nunivrsity: uga"))

    result = subprocess.run(
        [sys.executable, "-m", "qualc", "check", "--root", str(work)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "univrsity" in result.stderr
