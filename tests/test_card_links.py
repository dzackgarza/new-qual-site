"""An unlabelled wikilink to a card shows the card's title; an authored label stays."""

from __future__ import annotations

import pytest
from conftest import fixture_repo, run_qualc

TARGET = """---
schema: qual/card@1
id: T-TARGET
kind: theorem
title: Heine--Borel theorem
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

SOURCE = """---
schema: qual/card@1
id: T-SOURCE
kind: theorem
title: Closed intervals are compact
classification:
  areas: [real-analysis]
  topics: [compactness]
relations: []
review: draft
---

::: theorem
By [[T-TARGET]], and again by [[T-TARGET|the covering argument]], $[0,1]$ is compact.
:::
"""


@pytest.fixture(scope="module")
def page(tmp_path_factory: pytest.TempPathFactory) -> str:
    work = fixture_repo(tmp_path_factory.mktemp("links"), {"T-TARGET.md": TARGET, "T-SOURCE.md": SOURCE})
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr
    return (work / "build" / "quarto" / "_site" / "tag" / "T-SOURCE.html").read_text()


def test_an_unlabelled_card_link_shows_the_title(page: str) -> None:
    assert '<a href="T-TARGET.html" class="wikilink">Heine–Borel theorem</a>' in page
    assert ">T-TARGET</a>" not in page


def test_an_authored_label_is_kept(page: str) -> None:
    assert 'class="wikilink">the covering argument</a>' in " ".join(page.split())
