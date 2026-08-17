"""Batched Pandoc reads preserve each card's independent document semantics."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from qualc import emit, model
from qualc.pandoc_batch import PandocServer


def _card(path: Path, card_id: str, footnote: str) -> Path:
    path.write_text(
        f"""---
schema: qual/card@1
id: {card_id}
kind: problem
title: Problem {card_id}
classification:
  areas: [algebra]
  topics: [groups]
relations: []
review: draft
solved: false
---

# Shared heading {{#shared}}

::: problem
Dr. Example states {card_id}.[^local]

[^local]: {footnote}
:::
"""
    )
    return path


def _isolated_ast(path: Path) -> dict:
    _, body = model.split_front_matter(path.read_text(), path)
    result = subprocess.run(
        [
            "pandoc",
            "--from",
            model.MARKDOWN,
            "--to",
            "json",
            "--standalone",
            "--fail-if-warnings",
        ],
        input=body,
        capture_output=True,
        text=True,
        check=True,
    )
    payload: object = json.loads(result.stdout)
    assert isinstance(payload, dict)
    return payload


def test_batch_parse_matches_isolated_pandoc(tmp_path: Path) -> None:
    paths = [
        _card(tmp_path / "P-FIRST.md", "P-FIRST", "First local footnote."),
        _card(tmp_path / "P-SECOND.md", "P-SECOND", "Second local footnote."),
    ]

    parsed, errors = model.parse_cards(paths)

    assert errors == []
    assert [json.loads(item.ast) for item in parsed] == [_isolated_ast(path) for path in paths]


def test_batch_inline_parse_keeps_titles_inline() -> None:
    """A title is inline text. The batch cache must return inlines, not a
    block wrapper, and must not leak the boundary sentinel into the page."""
    title = "Uniform limits of continuous functions are continuous"
    with PandocServer() as pandoc:
        cache = emit.build_inline_cache(pandoc, [title])
    inlines = cache[title]
    assert type(inlines[0]).__name__ == "Str"
    assert all(emit.INLINE_SENTINEL not in str(inline) for inline in inlines)
