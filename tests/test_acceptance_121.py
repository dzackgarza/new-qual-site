"""Tests for tools/acceptance_121.py, the #121 per-card acceptance checker."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "tools" / "acceptance_121.py"

BOOK = """<!-- PDF page 16 -->
## 1 Affine Varieties

text
<!-- PDF page 27 -->
## 2 Projective Varieties

 2.9. Projective Closure of an Affine Variety. Let $Y$ be an affine variety.
<!-- PDF page 46 -->
## 5 Nonsingular Varieties

 5.5. For every degree $d>0$ give the equation of a nonsingular curve.
<!-- PDF page 52 -->
## 6 Nonsingular Curves
"""

INVENTORY = """
**The cards, sixty-nine.** Grouped by chapter.

- Chapter I, three. `P-TEST-OK` (I.2.9(b), generators), `P-TEST-POST` (I.2.9(a)),
  `P-TEST-SHORT` (I.5.5, the equation).
- Chapter I, one. `P-TEST-GAP` (I.5.6, blowing up).

**What was searched in this pass, and its text version.** Nothing.
"""

CARD_OK = """---
id: P-TEST-OK
---
::: {.problem}
Exercise.
:::

::: {.solution}
See Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994),
Exercise 2.9, printed p. 2, text version `tmp/sources/set.md`.
:::
"""

CARD_POST = """---
id: P-TEST-POST
---
::: {.problem}
Exercise.
:::

::: {.solution}
A Mathematics Stack Exchange answer 161648 proves it; a user post is not a
publication and no printed page is cited.
:::
"""

CARD_SHORT = """---
id: P-TEST-SHORT
---
::: {.problem}
Exercise.
:::

::: {.solution}
A. Shichijo, *Solutions*, Exercise 5.5, for the curve.
:::
"""

CARD_GAP = """---
id: P-TEST-GAP
---
::: {.problem}
Exercise.
:::

::: {.solution}
A. Shichijo, *Solutions*, Exercise 5.6, printed p. 4, for the blowup.
:::
"""


def build(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    coll = root / "corpus" / "collections" / "SRC-TEXT-HART77"
    coll.mkdir(parents=True)
    (root / "tmp" / "sources").mkdir(parents=True)
    (root / "COMPLAINTS.md").write_text("# Complaints\n" + INVENTORY)
    (root / "tmp" / "sources" / "hartshorne-1977-algebraic-geometry.md").write_text(BOOK)
    (root / "tmp" / "sources" / "set.md").write_text("2.9 Projective closure. The twisted cubic.")
    for name, text in {
        "P-TEST-OK": CARD_OK,
        "P-TEST-POST": CARD_POST,
        "P-TEST-SHORT": CARD_SHORT,
        "P-TEST-GAP": CARD_GAP,
    }.items():
        (coll / f"{name}.md").write_text(text)
    return root


def run(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(root)],
        capture_output=True,
        text=True,
        check=False,
    )


def test_a_card_with_a_publication_and_a_page_and_its_exercise_passes(tmp_path: Path) -> None:
    result = run(build(tmp_path))
    assert "ok   P-TEST-OK" in result.stdout, result.stdout + result.stderr


def test_a_card_whose_only_source_is_a_user_post_fails_item_one(tmp_path: Path) -> None:
    result = run(build(tmp_path))
    assert "FAIL P-TEST-POST" in result.stdout
    assert "R1 publication" in result.stdout


def test_a_publication_named_without_a_page_fails_item_two(tmp_path: Path) -> None:
    result = run(build(tmp_path))
    assert "FAIL P-TEST-SHORT" in result.stdout
    assert "R2 page" in result.stdout


def test_an_exercise_absent_from_the_text_version_needs_a_book_page(tmp_path: Path) -> None:
    result = run(build(tmp_path))
    # I.5.6 is not in the fixture book, and the card cites only the solution set.
    assert "FAIL P-TEST-GAP" in result.stdout
    assert "R3 exercise" in result.stdout


def test_an_absent_exercise_whose_book_page_is_given_is_not_charged_to_the_card(tmp_path: Path) -> None:
    root = build(tmp_path)
    card = root / "corpus" / "collections" / "SRC-TEXT-HART77" / "P-TEST-GAP.md"
    card.write_text(
        CARD_GAP.replace(
            "printed p. 4, for the blowup.",
            "printed p. 4, for the blowup; the exercise is Hartshorne I.5.6, printed p. 38.",
        )
    )
    result = run(root)
    assert "ok   P-TEST-GAP" in result.stdout, result.stdout
    assert "absent from the text version" in result.stdout


def test_the_run_fails_when_any_card_fails(tmp_path: Path) -> None:
    assert run(build(tmp_path)).returncode == 1


def test_the_checker_reports_a_missing_inventory(tmp_path: Path) -> None:
    root = build(tmp_path)
    (root / "COMPLAINTS.md").write_text("# Complaints\n\nNo inventory here.\n")
    result = run(root)
    assert result.returncode == 1
    assert "R0 inventory" in result.stdout
