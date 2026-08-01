"""The authored wiki is a first-class source projection, not a sidecar."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "kinds"


def fixture_repo(tmp_path: Path) -> Path:
    work = tmp_path / "repo"
    for sub in ("vocabularies", "site"):
        shutil.copytree(ROOT / sub, work / sub)
    shutil.copytree(FIXTURES, work / "corpus")
    (work / "publications").mkdir()
    assets = work / "assets" / "figures"
    assets.mkdir(parents=True)
    (assets / "diagram.png").write_bytes(b"fixture image")
    wiki = work / "wiki"
    wiki.mkdir()
    (wiki / "index.md").write_text("# Fixture index\n\nSee [[PRB-INDEXP|the index problem]] and [the details](details.md).\n\n![diagram](figures/diagram.png)\n")
    (wiki / "details.md").write_text("# Fixture details\n\nThe page reference survived.\n")
    return work


def run(command: str, root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "qualc", command, "--root", str(root)],
        capture_output=True,
        text=True,
        check=False,
    )


def test_build_emits_every_authored_page_and_resolves_real_links(tmp_path: Path) -> None:
    work = fixture_repo(tmp_path)
    result = run("build", work)
    assert result.returncode == 0, result.stderr

    output = work / "build" / "quarto"
    site = output / "_site"
    manifest = json.loads((output / "wiki-manifest.json").read_text())
    assert {entry["source"] for entry in manifest} == {"index.md", "details.md"}
    assert {entry["route"] for entry in manifest} == {"wiki/index.html", "wiki/details.html"}

    index = (site / "wiki" / "index.html").read_text()
    assert "../tag/PRB-INDEXP.html" in index
    assert 'href="details.html"' in index
    assert 'src="../assets/figures/diagram.png"' in index
    assert (site / "assets" / "figures" / "diagram.png").read_bytes() == b"fixture image"

    records = json.loads((site / "search.json").read_text())
    page = next(record for record in records if record["url"] == "wiki/index.html")
    assert page["kind"] == "Page"
    assert "fixture index" in page["search"]


@pytest.mark.parametrize(
    ("pages", "needle"),
    [
        ({"index.md": "# Root\n\n[[does-not-exist]]\n"}, "missing wiki page reference"),
        (
            {
                "index.md": "# Root\n\n[[same]]\n",
                "a/same.md": "# A\n",
                "b/same.md": "# B\n",
            },
            "ambiguous wiki page reference",
        ),
    ],
)
def test_check_rejects_missing_or_ambiguous_page_references(
    tmp_path: Path,
    pages: dict[str, str],
    needle: str,
) -> None:
    work = fixture_repo(tmp_path)
    wiki = work / "wiki"
    for path in wiki.rglob("*.md"):
        path.unlink()
    for relative, text in pages.items():
        path = wiki / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    result = run("check", work)
    assert result.returncode != 0
    assert "wiki/" in result.stderr
    assert needle in result.stderr
