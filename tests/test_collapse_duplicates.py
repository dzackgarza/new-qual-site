"""What the collapse must never leave behind: a reference to a card it removed.

`tools/collapse_duplicates.py` deletes from the working tree but rebuilt its
retired -> survivor map from `HEAD`, matching each removed card's `HEAD` body
against the bodies the tree now holds. A pass that edits card bodies before
collapsing breaks that match, so the id was retired with no survivor and every
`[[TAG]]` naming it was left pointing at nothing -- silently, exit 0. It
happened twice for real (46 cards in G5, 312 references in G3), and each time
the inconsistent tree failed the pre-push gate and blocked every other
workstream's push.

These drive the real CLI against a small git repo, because the defect is in what
the tool reads from git versus from disk; nothing below can be proved from
in-process state alone.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ORDER_12 = "Let $G$ be a group of order 12. Classify $G$ up to isomorphism."


def card(card_id: str, kind: str, title: str, body: str, *, extra: str = "") -> str:
    return f"""---
schema: qual/card@1
id: {card_id}
kind: {kind}
title: "{title}"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
{extra}---
{body}
"""


def fixture_corpus(root: Path, cards: dict[str, str], page: str) -> None:
    """A corpus the tool can run against: cards, a wiki page, and a `HEAD`.

    `tools/` is copied because the tool locates the corpus relative to its own
    file. `P-JP74P` is the survivor of the tool's committed seed alias, so any
    tree it runs against holds it.
    """
    (root / "wiki").mkdir(parents=True)
    (root / "sources").mkdir()
    (root / "publications").mkdir()
    shutil.copytree(ROOT / "tools", root / "tools")
    for relative, text in cards.items():
        path = root / "corpus" / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    (root / "corpus/qrs").mkdir(parents=True, exist_ok=True)
    (root / "corpus/qrs/P-JP74P.md").write_text(card("P-JP74P", "problem", "Seed", "Let $f$ be continuous with period 1."))
    (root / "wiki/page.md").write_text(page)
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    subprocess.run(["git", "-C", str(root), "add", "-A"], check=True)
    subprocess.run(
        ["git", "-C", str(root), "-c", "core.hooksPath=", "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "corpus"],
        check=True,
    )


def collapse(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(root / "tools/collapse_duplicates.py")], capture_output=True, text=True)


def test_a_body_edited_before_the_collapse_still_repoints_its_references(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    fixture_corpus(
        root,
        {
            "wiki/P-AAAAA.md": card("P-AAAAA", "problem", "Order 12", ORDER_12),
            "qrs/P-BBBBB.md": card("P-BBBBB", "problem", "Order 12, as posed", "A statement about Lebesgue measure."),
        },
        "# Page\n\n[[P-AAAAA]] and [[P-BBBBB]]\n",
    )
    # The editing pass: `P-BBBBB` is rewritten in the working tree to the text
    # `P-AAAAA` already carries, so the two are duplicates on disk but not in
    # `HEAD`. This is G5's heading-boundary split in miniature.
    (root / "corpus/qrs/P-BBBBB.md").write_text(card("P-BBBBB", "problem", "Order 12, as posed", ORDER_12))

    result = collapse(root)

    assert not (root / "corpus/qrs/P-BBBBB.md").exists()
    assert (root / "wiki/page.md").read_text() == "# Page\n\n[[P-AAAAA]] and [[P-AAAAA]]\n"
    assert result.returncode == 0


def test_an_id_the_tree_dropped_with_no_survivor_fails_instead_of_dangling(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    fixture_corpus(
        root,
        {
            "wiki/P-AAAAA.md": card("P-AAAAA", "problem", "Order 12", ORDER_12),
            "qrs/P-CCCCC.md": card("P-CCCCC", "problem", "Uniform convergence", "Show that the convergence is uniform on compact sets."),
        },
        "# Page\n\n[[P-AAAAA]] and [[P-CCCCC]]\n",
    )
    # A card removed with no card carrying its text is a loss, not a collapse.
    (root / "corpus/qrs/P-CCCCC.md").unlink()

    result = collapse(root)

    assert result.returncode == 1
    assert "P-CCCCC" in result.stdout
    assert "wiki/page.md" in result.stdout


def test_an_occurrence_is_not_a_duplicate_of_the_problem_it_instantiates(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    occurrence = card(
        "O-AAAAA",
        "occurrence",
        "Order 12 at UGA algebra Spring 2020",
        ORDER_12,
        extra="payload:\n  source: SRC-UGA\n  locator: Problem 3\n",
    ).replace("relations: []", "relations:\n- kind: instance-of\n  target: P-AAAAA")
    fixture_corpus(
        root,
        {
            "wiki/P-AAAAA.md": card("P-AAAAA", "problem", "Order 12", ORDER_12),
            "occurrences/O-AAAAA.md": occurrence,
        },
        "# Page\n\n[[P-AAAAA]] and [[O-AAAAA]]\n",
    )

    result = collapse(root)

    # An occurrence carries the body of the problem it instantiates by design.
    # Collapsing on shared body alone would retire the whole occurrence layer.
    assert (root / "corpus/occurrences/O-AAAAA.md").exists()
    assert (root / "corpus/wiki/P-AAAAA.md").exists()
    assert (root / "wiki/page.md").read_text() == "# Page\n\n[[P-AAAAA]] and [[O-AAAAA]]\n"
    assert result.returncode == 0
