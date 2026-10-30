"""Batched Pandoc reads preserve each card's independent document semantics."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from qualc import emit, model
from qualc.pandoc_batch import PandocServer, pandoc_executable, write_html_parallel, write_markdown_parallel


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
            str(pandoc_executable()),
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


def test_parallel_writers_preserve_serial_result_order() -> None:
    documents = [
        json.dumps(
            {
                "pandoc-api-version": [1, 23],
                "meta": {},
                "blocks": [{"t": "Para", "c": [{"t": "Str", "c": f"item-{index}"}]}],
            }
        )
        for index in range(24)
    ]
    with PandocServer() as pandoc:
        serial_markdown = pandoc.write_markdown(documents, model.MARKDOWN)
        serial_html = pandoc.write_html(documents)

    parallel_markdown = write_markdown_parallel(documents, model.MARKDOWN)
    parallel_html = write_html_parallel(documents)

    assert parallel_markdown == serial_markdown
    assert parallel_html == serial_html


def test_wikilink_text_typesets_dashes(tmp_path: Path) -> None:
    path = tmp_path / "P-LINK.md"
    path.write_text(_card(tmp_path / "P-LINK.md", "P-LINK", "Note.").read_text().replace("Dr. Example states", "See [[FF-CSABG|Artin--Rees lemma]];"))

    parsed, errors = model.parse_cards([path])

    assert errors == []
    assert "Artin–Rees" in parsed[0].ast
    assert "Artin--Rees" not in parsed[0].ast


def test_citation_keeps_its_locator() -> None:
    source = "A [@DF04, Section 10.1, Exercise 8]. B [@DF04, p. 5].\n"
    vocabularies = Path(__file__).resolve().parent.parent / "vocabularies"
    result = subprocess.run(
        [
            str(pandoc_executable()),
            "--citeproc",
            "--bibliography",
            str(vocabularies / "references.yaml"),
            "--csl",
            str(vocabularies / "citation-style.csl"),
            "--to",
            "plain",
            "--wrap",
            "none",
        ],
        input=source,
        capture_output=True,
        text=True,
        check=True,
    )
    assert "[DuFo04, Section 10.1, Exercise 8]" in result.stdout
    assert "[DuFo04, p. 5]" in result.stdout


def test_corporate_author_citation_renders_its_label() -> None:
    """A corporate author has no family name to build a label from, so the
    bibliography gives `Har07` an explicit `citation-label`, and the server's
    citeproc read of the committed bibliography renders it."""
    with PandocServer() as pandoc:
        (result,) = pandoc.read_markdown(["See [@Har07].\n"], model.MARKDOWN, model.load_citations(model.VOCABULARIES))
    text = json.dumps(json.loads(result.output)["blocks"][0])
    assert '"Har07"' in text
