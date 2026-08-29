"""Nothing the corpus holds is missing from the site that is supposed to show it.

Each claim here was a line in TODO.md's publication section, checked by hand
against one build. A hand check answers for the corpus that existed that
afternoon; these answer for any corpus, which is what the claims were reaching
for. They are set equalities rather than counts: a count matches by accident,
a set does not.
"""

from __future__ import annotations

import html
import json
import re
import sqlite3
from pathlib import Path

from conftest import fixture_repo, run_qualc

CARD_LINK = re.compile(r'href="(?:\.\./)?tag/([A-Z]+-[A-Z0-9.-]+)\.html"')


def built(tmp_path: Path) -> tuple[Path, sqlite3.Connection]:
    work = fixture_repo(tmp_path, {"P-EXTRA.md": PROBLEM, "SRC-SHEET.md": COLLECTION})
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr
    con = sqlite3.connect(work / "build" / "catalog.sqlite")
    con.row_factory = sqlite3.Row
    return work / "build" / "quarto" / "_site", con


PROBLEM = """---
schema: qual/card@1
id: P-EXTRA
kind: problem
title: A second problem, so the sets have something to differ by
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
relations: []
review: draft
---

::: problem
Let $G$ have order $p^2q$. Show $G$ has a normal Sylow subgroup.
:::
"""

COLLECTION = """---
schema: qual/card@1
id: SRC-SHEET
kind: collection
title: A homework sheet that lists one problem
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
source:
  source_kind: homework
  area: algebra
  date:
    kind: academic-term
    year: 2020
    term: spring
  problems:
  - P-EXTRA
---

::: remark
A sheet exists to list the problems it set.
:::
"""


def test_the_browser_and_the_generator_offer_the_same_problems(tmp_path: Path) -> None:
    """Both read the catalog, and a problem in one but not the other is a defect.

    The generator used to derive its own area list from whatever the problem
    data happened to carry, which is the shape this guards against.
    """
    site, con = built(tmp_path)
    catalog = {r["id"] for r in con.execute("select id from cards where kind='problem'")}
    assert catalog, "the fixture must carry problems for this to mean anything"

    browser = set(CARD_LINK.findall((site / "problems.html").read_text()))
    embedded = re.search(r"const QDATA=(\[.*?\]);", (site / "generate.html").read_text(), re.S)
    assert embedded is not None, "the generator must embed its problems"
    generator = {q["id"] for q in json.loads(embedded.group(1))}

    assert browser >= catalog, f"the browser drops {sorted(catalog - browser)}"
    assert generator == catalog, f"the generator and the catalog differ by {sorted(generator ^ catalog)}"


def test_every_authored_page_is_emitted_once(tmp_path: Path) -> None:
    """A page the wiki holds and the site does not is a page a reader cannot reach."""
    work = fixture_repo(tmp_path)
    result = run_qualc("build", work)
    assert result.returncode == 0, result.stderr

    authored = {p.relative_to(work / "wiki").with_suffix(".html").as_posix() for p in (work / "wiki").rglob("*.md")}
    emitted = {p.relative_to(work / "build" / "quarto" / "_site" / "wiki").as_posix() for p in (work / "build" / "quarto" / "_site" / "wiki").rglob("*.html")}
    manifest = json.loads((work / "build" / "quarto" / "wiki-manifest.json").read_text())

    assert len(emitted) == len(authored), f"{len(authored)} pages, {len(emitted)} routes"
    assert len(manifest) == len(authored), f"{len(authored)} pages, {len(manifest)} in the manifest"


def test_a_collection_page_links_every_problem_the_collection_lists(tmp_path: Path) -> None:
    """A listed problem the page does not link is a problem a reader cannot reach.

    Whether every problem belongs to a collection at all is a fact about the
    corpus rather than the emitter, and `just backlog`'s `orphans` check owns
    it. This owns the step after: given that a collection claims a problem, its
    page carries the link.
    """
    site, con = built(tmp_path)
    listed = {r["problem_id"] for r in con.execute("select problem_id from collection_problems")}
    assert listed, "the fixture must have a collection listing problems"

    linked: set[str] = set()
    for directory in ("exam", "source"):
        for page in (site / directory).glob("*.html"):
            linked |= set(CARD_LINK.findall(page.read_text()))
    assert listed <= linked, f"{sorted(listed - linked)} are listed by a collection whose page does not link them"


def test_the_filters_offer_every_value_the_corpus_carries(tmp_path: Path) -> None:
    """A facet value a card carries and the filter omits hides that card."""
    site, con = built(tmp_path)
    page = (site / "problems.html").read_text()
    for axis in ("area", "topic"):
        carried = {r[0] for r in con.execute("select distinct term from classifications where axis=?", (axis,))}
        control = re.search(rf'<select id="listing-{axis}".*?</select>', page, re.S)
        assert control is not None, f"the browser must offer a {axis} filter"
        offered = {html.unescape(v) for v in re.findall(r'<option value="([^"]*)"', control.group(0))}
        assert carried <= offered, f"{axis}: {sorted(carried - offered)} carried but not offered"
