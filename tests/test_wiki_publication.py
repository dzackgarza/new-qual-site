"""The authored wiki is a first-class source projection, not a sidecar."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
from conftest import diagnostic_codes

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
    ("pages", "code"),
    [
        ({"index.md": "# Root\n\n[[does-not-exist]]\n"}, "page-reference-missing"),
        (
            {
                "index.md": "# Root\n\n[[same]]\n",
                "a/same.md": "# A\n",
                "b/same.md": "# B\n",
            },
            "page-reference-ambiguous",
        ),
    ],
)
def test_check_rejects_missing_or_ambiguous_page_references(
    tmp_path: Path,
    pages: dict[str, str],
    code: str,
) -> None:
    """A reference that resolves to nothing, and one that resolves to two pages,
    are different failures and must stay distinguishable. Asserting the code
    rather than the wording is what keeps them apart -- both messages contain
    "wiki page reference"."""
    work = fixture_repo(tmp_path)
    wiki = work / "wiki"
    for path in wiki.rglob("*.md"):
        path.unlink()
    for relative, text in pages.items():
        path = wiki / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    assert diagnostic_codes(work) == [code]


def test_a_citation_names_the_book_rather_than_its_key(tmp_path: Path) -> None:
    """Pandoc reads `[@key]` as a citation and leaves the key as the element's
    own text, so with no CSL step the reader is shown `[@dummit_foote_2004]`.
    The registry knows what that key cites; the page says so."""
    work = fixture_repo(tmp_path)
    (work / "wiki" / "index.md").write_text("# Fixture index\n\nReferences: [@dummit_foote_2004], [@smith].\n")

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    # Pandoc's HTML writer wraps its output, so a name can straddle two lines.
    page = re.sub(r"\s+", " ", (work / "build" / "quarto" / "_site" / "wiki" / "index.html").read_text())
    assert "Dummit and Foote, Abstract Algebra" in page
    assert "Smith, Algebra Course Notes" in page
    assert "@dummit_foote_2004" not in page

    records = json.loads((work / "build" / "quarto" / "_site" / "search.json").read_text())
    index = next(record for record in records if record["url"] == "wiki/index.html")
    assert "dummit and foote" in index["search"]


def test_check_rejects_a_citation_no_textbook_claims(tmp_path: Path) -> None:
    """A key the registry does not know would reach the page as itself."""
    work = fixture_repo(tmp_path)
    (work / "wiki" / "index.md").write_text("# Fixture index\n\nSee [@bourbaki_1970].\n")
    for path in (work / "wiki").rglob("*.md"):
        if path.name != "index.md":
            path.unlink()

    assert diagnostic_codes(work) == ["unknown-citation"]


def test_a_figure_captioned_with_its_own_filename_loses_the_caption(tmp_path: Path) -> None:
    """Pandoc's implicit-figure syntax makes the caption out of the alt text, and
    the authored vault wrote the attachment path there. A written caption is a
    caption and stays; a path is the file's name and is not one."""
    work = fixture_repo(tmp_path)
    (work / "wiki" / "index.md").write_text("# Fixture index\n\n![figures/diagram.png](figures/diagram.png)\n\n![The Tube Lemma](figures/diagram.png)\n")

    result = run("build", work)
    assert result.returncode == 0, result.stderr

    page = (work / "build" / "quarto" / "_site" / "wiki" / "index.html").read_text()
    assert page.count("<figcaption") == 1
    assert "The Tube Lemma</figcaption>" in page
    assert 'alt="figures/diagram.png"' in page
