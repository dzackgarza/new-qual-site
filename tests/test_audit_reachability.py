"""Guide prose does not make a card reachable; an authored reference does."""

from __future__ import annotations

from pathlib import Path

import yaml

from qualc.audit import orphan_ids
from qualc.model import ParsedCard, ProblemCard


def test_only_guide_references_make_cards_reachable(tmp_path: Path) -> None:
    publications = tmp_path / "publications"
    publications.mkdir()
    guide = publications / "guide.yaml"
    data = {
        "schema": "qual/publication@2",
        "id": "GUIDE-ALGEBRA",
        "kind": "study-guide",
        "title": "P-TEST",
        "lede": "A guide.",
        "sections": [
            {
                "slug": "first",
                "title": "First",
                "parent": "GUIDE-ALGEBRA",
                "lede": "Read this section.",
                "items": [],
            }
        ],
    }
    card = ParsedCard(
        card=ProblemCard.model_validate(
            {
                "schema": "qual/card@1",
                "id": "P-TEST",
                "kind": "problem",
                "title": "A problem",
                "classification": {"areas": ["algebra"], "topics": ["Groups"]},
                "relations": [],
                "review": "draft",
            }
        ),
        ast="[]",
        source_path="test",
        sections=[],
    )
    guide.write_text(yaml.safe_dump(data))
    assert orphan_ids([card], [], root=tmp_path) == {"P-TEST"}

    data["sections"][0]["items"] = [{"ref": "P-TEST"}]
    guide.write_text(yaml.safe_dump(data))
    assert orphan_ids([card], [], root=tmp_path) == set()
