"""A card's title and prompts reach the reader typeset, wherever they are shown.

Titles are written in Markdown, `Heine--Borel`, and several sinks show them
as text rather than through the Markdown reader: the page heading, the tab
title, review prompts. The tab title cannot typeset TeX at all.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
from conftest import fixture_repo, run_qualc

CARD = """---
schema: qual/card@1
id: T-DASHED
kind: theorem
title: Heine--Borel theorem in $\\RR^n$
prompts:
- State the Heine--Borel theorem.
classification:
  areas: [real-analysis]
  topics: [compactness]
relations: []
review: draft
---

::: theorem
A subset of $\\RR^n$ is compact if and only if it is closed and bounded.
:::
"""


@pytest.fixture(scope="module")
def page(tmp_path_factory: pytest.TempPathFactory) -> str:
    work = fixture_repo(tmp_path_factory.mktemp("titles"), {"T-DASHED.md": CARD})
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr
    return (work / "build" / "quarto" / "_site" / "tag" / "T-DASHED.html").read_text()


def test_the_heading_and_prompt_typeset_their_dashes(page: str) -> None:
    assert "<h1>Heine–Borel theorem in $\\RR^n$</h1>" in page
    assert "State the Heine–Borel theorem." in page
    assert "--" not in re.sub(r"<!--.*?-->|<script.*?</script>|<style.*?</style>", "", page, flags=re.S).split("<main", 1)[1]


def test_the_tab_title_is_plain_text(page: str) -> None:
    title = page.split("<title>", 1)[1].split("</title>", 1)[0]
    assert title.startswith("Heine–Borel theorem in ")
    assert title.endswith(" · Qual Corpus")
    assert "$" not in title
    assert "\\" not in title


def test_the_home_page_title_is_the_site_name(tmp_path_factory: pytest.TempPathFactory) -> None:
    work = fixture_repo(tmp_path_factory.mktemp("home"))
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr
    home = (work / "build" / "quarto" / "_site" / "index.html").read_text()
    assert "<title>Qual Corpus</title>" in home
