"""Report metadata completeness for problem cards.

A card is *complete* when every metadata field that a reader or generator
needs is populated.  The recipe is a measurement, not a gate: incomplete
cards are candidates for authoring, not build failures.

Completeness criteria (problem cards):
  1. title is present and non-empty
  2. classification.areas is non-empty
  3. classification.topics is non-empty
  4. body contains content

Collection cards are excluded — their completeness is provenance, measured
elsewhere.
"""

from __future__ import annotations

import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml


def check_card(path: Path) -> list[str]:
    """Return a list of missing fields for one card file."""
    text = path.read_text()
    if not text.startswith("---\n"):
        return ["no-frontmatter"]
    _, fm_body = text.split("---\n", 1)
    fm_text, _, body = fm_body.partition("---\n")
    meta = yaml.safe_load(fm_text)
    if not isinstance(meta, dict):
        return ["bad-frontmatter"]

    issues: list[str] = []
    kind = meta.get("kind", "")

    if kind != "problem":
        return []

    title = meta.get("title", "")
    if not title or not title.strip():
        issues.append("no-title")

    classification = meta.get("classification", {})
    areas = classification.get("areas", []) if isinstance(classification, dict) else []
    if not areas:
        issues.append("no-areas")

    topics = classification.get("topics", []) if isinstance(classification, dict) else []
    if not topics:
        issues.append("no-topics")

    if not body or not body.strip():
        issues.append("no-body")

    return issues


def get_area(path: Path) -> str:
    """Extract the first area from a card's frontmatter."""
    text = path.read_text()
    if not text.startswith("---\n"):
        return "unknown"
    _, fm_body = text.split("---\n", 1)
    fm_text, _, _ = fm_body.partition("---\n")
    meta = yaml.safe_load(fm_text)
    if not isinstance(meta, dict):
        return "unknown"
    classification = meta.get("classification", {})
    areas = classification.get("areas", []) if isinstance(classification, dict) else []
    return areas[0] if areas else "unclassified"


def main() -> None:
    corpus = Path("corpus")
    if not corpus.exists():
        print("corpus/ not found", file=sys.stderr)
        sys.exit(1)

    complete: list[str] = []
    incomplete: list[tuple[str, list[str], str]] = []  # (id, issues, area)

    for path in sorted(corpus.rglob("*.md")):
        issues = check_card(path)
        if not issues:
            continue
        card_id = path.stem
        if not issues:
            complete.append(card_id)
        else:
            area = get_area(path)
            incomplete.append((card_id, issues, area))

    print(f"complete:   {len(complete)}")
    print(f"incomplete: {len(incomplete)}")
    print()

    if incomplete:
        issue_counts: Counter[str] = Counter()
        for _, issues, _ in incomplete:
            for issue in issues:
                issue_counts[issue] += 1

        print("by issue:")
        for issue, count in issue_counts.most_common():
            print(f"  {issue}: {count}")
        print()

        by_area: dict[str, list[tuple[str, list[str]]]] = defaultdict(list)
        for card_id, issues, area in incomplete:
            by_area[area].append((card_id, issues))

        for area in sorted(by_area):
            cards = by_area[area]
            print(f"[{area}] ({len(cards)} cards):")
            for card_id, issues in cards:
                print(f"  {card_id}: {', '.join(issues)}")
            print()


if __name__ == "__main__":
    main()
