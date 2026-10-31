"""Render the queue of parsed problem cards without solution sections."""

from __future__ import annotations

from collections.abc import ItemsView

from .model import ParsedCard


def unsolved(parsed: list[ParsedCard]) -> list[ParsedCard]:
    """The same rule `just sample-unsolved` draws from, over the parsed corpus."""
    return [
        item
        for item in parsed
        if item.card.kind == "problem"
        and not any(kind == "solution" for kind, _text in item.sections)
    ]


def render_entries(entries: list[tuple[str, str]] | ItemsView[str, str]) -> str:
    ordered = sorted(entries)
    lines = [
        "# Document queue C: Unsolved problem cards",
        "",
        f"{len(ordered)} problem cards have no solution section. These are",
        "the cards issue #2 targets: write a Lamport-style structured proof for each.",
        "",
        "Regenerate with `just unsolved` after a card gains a solution. CI publishes",
        "the current measurement with its corpus reports. The boxes are a",
        "measurement and not a ledger -- ticking one by hand does not survive the next",
        "regeneration, and writing the solution removes the line.",
        "",
        "## Count",
        "",
    ]
    lines += [f"- Problems: {len(ordered)}", "", f"## Problems ({len(ordered)})", ""]
    lines += [f'- [ ] {card_id} — "{title}"' for card_id, title in ordered]
    lines.append("")
    return "\n".join(lines)


def render(cards: list[ParsedCard]) -> str:
    return render_entries([(c.card.id, c.card.title) for c in cards])
