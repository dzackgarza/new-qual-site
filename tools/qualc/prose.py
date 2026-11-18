"""Measure prose-only solutions: a solution section with no numbered step in it.

`queues/C-unsolved-cards.md` counts the problem cards with **no** solution section, and
issue #2 asks for more than that: a Lamport-style structured proof -- hierarchically
numbered steps `<1>1`, `<2>1`, ..., each justification explicit -- and issue #2 says a
correct prose solution is not grandfathered. So the corpus can report zero unsolved cards
and still be far from the requirement, and nothing before this module could name the cards
whose solution is prose.

The rule, in one sentence: a card's solution is **structured** when a `.pf` proof root
holds at least one `.pf-step`, and **prose only** otherwise.

It is read from the parsed card's AST, not from the source text and not from `review` or
`audit`. The reasons are exact:

* `pf-step` is the authored surface, and the step *numbers* are assigned by the filter that
  reads it (`lamport_proof.lua`, run from `tools/qualc/lamport.py`). No card writes a number
  of its own -- the corpus holds no literal `<1>1` -- so the class is the whole evidence.
* The stringified text in `ParsedCard.sections` has already lost the classes, so a card
  whose only step is nested inside a `pf-proof` and one that writes "first, ..." read the
  same there. The AST does not confuse them.
* A step is counted only inside a solution section, and only when a `pf` root encloses it
  (`lamport_proof.lua` numbers a proof root's direct steps, and a step's nested levels live
  in its `pf-proof` body, so every numbered step has a root above it).
* A hand-numbered Markdown list in a solution is prose here. The requirement's numbers
  (`<1>1`, `<2>1`, ...) are the filter's, assigned to `.pf-step` blocks, and a list item
  carries no level: nothing in it can be referenced as a step of its parent.

Nothing here rewrites a card. This is the measurement issue #2 needs before it can dispatch
its work; the queue it renders is `queues/D-prose-only-solutions.md`.
"""

from __future__ import annotations

import json
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path

from .model import ParsedCard

SOLUTION_CLASS = "solution"
PROOF_ROOT_CLASS = "pf"
STEP_CLASS = "pf-step"

#: The file this measurement is published as, relative to the repository root.
QUEUE = Path("queues") / "D-prose-only-solutions.md"


@dataclass(frozen=True)
class Structured:
    """What one card's solution sections hold, counted and not judged.

    `sections` is 0 on a card with no solution at all: that card is Queue C's, not this
    queue's. `steps` counts the steps that a proof root will number.
    """

    sections: int
    steps: int

    @property
    def prose_only(self) -> bool:
        return self.sections > 0 and self.steps == 0


def _div_classes(node: object) -> list[str] | None:
    """The classes of a pandoc `Div` node, or None if this node is not a `Div`."""
    if isinstance(node, dict) and node.get("t") == "Div":
        return list(node["c"][0][1])
    return None


def _children(value: object) -> Iterator[object]:
    """Every value nested in a pandoc AST node, attr strings included.

    Recursing over the node's whole value rather than over `c` keeps this independent of
    any one node's shape: a solution inside a block quote or a list item is reached the
    same way a top-level one is.
    """
    if isinstance(value, dict):
        yield from value.values()
    elif isinstance(value, list):
        yield from value


def structured(ast: str) -> Structured:
    """Count the solution sections and their numbered steps in one card's AST."""
    sections = 0
    steps = 0
    pending = [(json.loads(ast), False, False)]
    while pending:
        node, inside_solution, inside_root = pending.pop()
        classes = _div_classes(node)
        if classes is not None:
            if SOLUTION_CLASS in classes:
                sections += 1
                inside_solution = True
            if PROOF_ROOT_CLASS in classes:
                inside_root = True
            if STEP_CLASS in classes and inside_solution and inside_root:
                steps += 1
        pending.extend((child, inside_solution, inside_root) for child in _children(node))
    return Structured(sections=sections, steps=steps)


@dataclass(frozen=True)
class Measurement:
    """The queue, and the population it was drawn from.

    The population is the problem cards that have a solution section: the cards this
    measurement speaks for. Reporting the draw against it keeps the count from reading as
    "the whole corpus".
    """

    prose_only: tuple[ParsedCard, ...]
    with_solution: int

    def __len__(self) -> int:
        return len(self.prose_only)

    def entries(self) -> list[tuple[str, str]]:
        return [(item.card.id, item.card.title) for item in self.prose_only]


def measure(parsed: list[ParsedCard]) -> Measurement:
    """Partition the corpus's problem cards by whether their solution holds a step."""
    prose_only: list[ParsedCard] = []
    with_solution = 0
    for item in parsed:
        if item.card.kind != "problem":
            continue
        counted = structured(item.ast)
        if counted.sections == 0:
            continue
        with_solution += 1
        if counted.prose_only:
            prose_only.append(item)
    return Measurement(prose_only=tuple(prose_only), with_solution=with_solution)


def render_entries(
    entries: Iterable[tuple[str, str]], with_solution: int
) -> str:
    ordered = sorted(entries)
    lines = [
        "# Document queue D: Prose-only solutions",
        "",
        f"{len(ordered)} of the {with_solution} problem cards that have a solution",
        "section hold no numbered step in it. These are the cards issue #2 targets once",
        "`queues/C-unsolved-cards.md` is empty: issue #2 asks for a Lamport-style",
        "structured proof, and a correct prose solution is not grandfathered.",
        "",
        "Regenerate with `just prose-only` after a solution gains steps. CI publishes",
        "the current measurement with its corpus reports, beside Queue C. The rule is",
        "read from the parsed card, never from `review` or `audit`: the solution is",
        "structured when a `.pf` proof root holds at least one `.pf-step`, and prose",
        "only otherwise. A card with no solution section is Queue C's card, not this",
        "one. The boxes are a measurement and not a ledger -- ticking one by hand does",
        "not survive the next regeneration, and writing the steps removes the line.",
        "",
        "## Count",
        "",
        f"- Problems: {len(ordered)}",
        f"- Problem cards with a solution: {with_solution}",
        "",
        f"## Problems ({len(ordered)})",
        "",
    ]
    lines += [f'- [ ] {card_id} — "{title}"' for card_id, title in ordered]
    lines.append("")
    return "\n".join(lines)


def render(measurement: Measurement) -> str:
    return render_entries(measurement.entries(), measurement.with_solution)
