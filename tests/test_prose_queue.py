"""Queue D names the cards whose solution is prose, and only those.

The rule under test is the one `tools/qualc/prose.py` documents: a solution is structured
when a `.pf` proof root holds at least one `.pf-step`, and prose only otherwise.

The fixture corpus has problem cards of its own, so each case is measured against the bare
fixture rather than against a hard-coded total: the claim is what the injected card does to
the measurement, not what the fixture happens to hold today.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

from conftest import fixture_repo

ROOT = Path(__file__).resolve().parent.parent
PROSE_QUEUE = ROOT / "tools" / "prose_queue.py"
UNSOLVED_QUEUE = ROOT / "tools" / "unsolved_queue.py"
#: The queue's two counts, read structurally rather than out of its wrapped prose.
COUNT = re.compile(r"^- Problems: (\d+)$", re.M)
POPULATION = re.compile(r"^- Problem cards with a solution: (\d+)$", re.M)


def card(card_id: str, body: str) -> str:
    return (
        f"---\nschema: qual/card@1\nid: {card_id}\nkind: problem\n"
        f'title: Card {card_id}\nclassification:\n  areas: [algebra]\n  topics: []\n'
        f"relations: []\nreview: draft\n---\n\n{body}"
    )


PROSE = "::: {.solution}\nEvery odd integer is $2a+1$ for some integer $a$, so the sum is even.\n:::\n"

STEPS = """::: {.solution}

::: {.pf}

::: {.pf-step}
Every odd integer is $2a+1$ for some integer $a$.
:::

:::

:::
"""

# A numbered step that is not inside any solution section: the card holds a proof, but the
# solution the reader is shown is prose, so the card belongs to the queue.
STEPS_OUTSIDE_SOLUTION = """::: {.solution}
Every odd integer is $2a+1$, so the sum is even.
:::

::: {.pf}

::: {.pf-step}
Every odd integer is $2a+1$ for some integer $a$.
:::

:::
"""

NO_SOLUTION = "::: {.problem}\nProve the claim.\n:::\n"


def run(script: Path, root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script), "--root", str(root)],
        text=True,
        capture_output=True,
        check=False,
    )


def measured(tmp: Path, cards: dict[str, str] | None = None) -> tuple[int, int, str]:
    """The queue for a fixture corpus holding `cards`: (prose only, with a solution, text)."""
    root = fixture_repo(tmp, cards)
    result = run(PROSE_QUEUE, root)
    assert result.returncode == 0, result.stdout + result.stderr
    text = (root / "queues" / "D-prose-only-solutions.md").read_text()
    count, population = COUNT.search(text), POPULATION.search(text)
    assert count is not None and population is not None, text
    prose, with_solution = int(count[1]), int(population[1])
    # The header sentence says the same numbers; a queue whose prose and counts disagreed
    # would be two measurements in one file. Compared with its wrapping flattened, so a
    # re-wrapped sentence is not a test failure.
    flat = " ".join(text.split())
    assert f"{prose} of the {with_solution} problem cards that have a solution section" in flat
    return prose, with_solution, text


def test_prose_solution_is_queued_and_numbered_steps_are_not(tmp_path: Path) -> None:
    base, base_with_solution, _text = measured(tmp_path / "base")
    prose, with_solution, text = measured(
        tmp_path / "case",
        {
            "P-PROSECARD.md": card("P-PROSECARD", PROSE),
            "P-STEPCARD.md": card("P-STEPCARD", STEPS),
        },
    )
    assert 'P-PROSECARD — "Card P-PROSECARD"' in text
    assert "P-STEPCARD" not in text
    assert (prose, with_solution) == (base + 1, base_with_solution + 2)
    assert text.count("- [ ]") == prose
    assert f"## Problems ({prose})" in text


def test_a_step_outside_the_solution_does_not_count(tmp_path: Path) -> None:
    base, base_with_solution, _text = measured(tmp_path / "base")
    prose, with_solution, text = measured(
        tmp_path / "case", {"P-OUTSIDE.md": card("P-OUTSIDE", STEPS_OUTSIDE_SOLUTION)}
    )
    assert 'P-OUTSIDE — "Card P-OUTSIDE"' in text
    assert (prose, with_solution) == (base + 1, base_with_solution + 1)


def test_a_card_without_a_solution_belongs_to_queue_c(tmp_path: Path) -> None:
    base, base_with_solution, _text = measured(tmp_path / "base")
    prose, with_solution, text = measured(
        tmp_path / "case", {"P-NOSOLUTION.md": card("P-NOSOLUTION", NO_SOLUTION)}
    )
    assert "P-NOSOLUTION" not in text
    assert (prose, with_solution) == (base, base_with_solution)
    root = tmp_path / "case" / "repo"
    result = run(UNSOLVED_QUEUE, root)
    assert result.returncode == 0, result.stderr
    assert "P-NOSOLUTION" in (root / "queues" / "C-unsolved-cards.md").read_text()


def test_the_backlog_report_publishes_the_count_the_queue_was_drawn_from(
    tmp_path: Path,
) -> None:
    """One measurement, two spellings: the drawn count, and the report's last line."""
    prose, with_solution, _text = measured(
        tmp_path / "case",
        {
            "P-PROSECARD.md": card("P-PROSECARD", PROSE),
            "P-STEPCARD.md": card("P-STEPCARD", STEPS),
        },
    )
    root = tmp_path / "case" / "repo"
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "backlog.py"), "--root", str(root)],
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    report = (root / "BACKLOG.md").read_text()
    assert (
        f"{prose} of the {with_solution} problem cards with a solution hold no numbered step"
        in report
    )
    assert "queues/D-prose-only-solutions.md" in report
