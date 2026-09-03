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
import sqlite3
from pathlib import Path

from conftest import fixture_repo, run_qualc


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


def test_the_index_holds_exactly_the_problems_the_catalog_has(tmp_path: Path) -> None:
    """The canonical problem browser asks the shared index, so it offers exactly what the catalog holds.

    Each used to carry its own copy of the problem set -- the browser as rows,
    a former generator as a script literal -- and a problem in one and not the other
    was the defect this guarded against. There is one query surface now, and what makes
    it right is that every problem's page is a document filed under `problem`
    and no other page is.
    """
    site, con = built(tmp_path)
    catalog = {r["id"] for r in con.execute("select id from cards where kind='problem'")}
    assert catalog, "the fixture must carry problems for this to mean anything"

    indexed = set()
    for page in sorted(site.rglob("*.html")):
        text = page.read_text()
        if 'data-pagefind-filter="kind:problem"' not in text:
            continue
        assert "data-pagefind-body" in text, f"{page} is filed as a problem but is not a document"
        indexed.add(page.stem)
    assert indexed == catalog, f"the index and the catalog differ by {sorted(indexed ^ catalog)}"

    # The canonical problem browser is the only query/listing implementation.
    markup = (site / "problems.html").read_text()
    assert "data-pagefind-body" not in markup, "problems.html is a listing, not a result"
    assert "app.js" in markup, "the problem browser must read the shared index"
    legacy = (site / "generate.html").read_text()
    assert "location.replace(target.href)" in legacy
    assert 'new URL("problems.html",document.baseURI)' in legacy


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


def test_every_collection_problem_is_exposed_by_the_central_source_order_index(tmp_path: Path) -> None:
    """Collection pages delegate problem rows, but no listed problem becomes unreachable."""
    site, con = built(tmp_path)
    listed = {
        row[0]
        for row in con.execute(
            """
            select cp.problem_id
            from collection_problems cp join cards c on c.id=cp.problem_id
            where c.kind='problem'
            """
        )
    }
    assert listed, "the fixture must have a collection listing problems"

    index = json.loads((site / "collection-problems.json").read_text())
    indexed = {item["id"] for source in index.values() for item in source["items"]}
    assert listed <= indexed, f"{sorted(listed - indexed)} are missing from the central source-order index"

    for collection_id, source in index.items():
        route = con.execute("select route from cards where id=?", (collection_id,)).fetchone()[0]
        page = (site / route / f"{collection_id}.html").read_text()
        assert f"problems.html?collection={collection_id}" in html.unescape(page)
        for item in source["items"]:
            assert f"tag/{item['id']}.html" not in page, "source pages must not duplicate problem rows"


def test_the_filters_offer_every_value_problem_appearances_carry(tmp_path: Path) -> None:
    """A facet value a problem appearance carries and the browser omits hides that problem."""
    site, con = built(tmp_path)
    payload = json.loads((site / "problems.json").read_text())
    rows = payload["rows"]

    problem_ids = {row["id"] for row in rows}
    assert problem_ids == {r[0] for r in con.execute("select id from cards where kind='problem'")}

    carried_areas = {r[0] for r in con.execute("select distinct cl.term from classifications cl join cards c on c.id=cl.card_id where c.kind='problem' and cl.axis='area'")}
    carried_topics = {r[0] for r in con.execute("select distinct cl.term from classifications cl join cards c on c.id=cl.card_id where c.kind='problem' and cl.axis='topic'")}
    carried_source_kinds = {
        r[0]
        for r in con.execute(
            "select distinct s.source_kind from sources s join collection_problems cp on cp.collection_id=s.id join cards c on c.id=cp.problem_id where c.kind='problem'"
        )
    }
    carried_collections = {r[0] for r in con.execute("select distinct cp.collection_id from collection_problems cp join cards c on c.id=cp.problem_id where c.kind='problem'")}
    carried_institutions = {
        r[0].upper()
        for r in con.execute(
            "select distinct e.institution from exam_sources e join collection_problems cp on cp.collection_id=e.id join cards c on c.id=cp.problem_id where c.kind='problem'"
        )
    }
    carried_years = {
        str(r[0])
        for r in con.execute(
            """
            select distinct s.year
            from sources s
            join collection_problems cp on cp.collection_id=s.id
            join cards c on c.id=cp.problem_id
            where c.kind='problem' and s.year is not null
            """
        )
    }

    assert carried_areas <= set(payload["areaNames"])
    assert carried_source_kinds <= set(payload["sourceKindNames"])
    assert carried_collections <= set(payload["collectionNames"])
    assert carried_topics <= {topic for row in rows for topic in row["topics"]}
    assert carried_institutions <= {institution for row in rows for institution in row["institutions"]}
    assert carried_years <= {year for row in rows for year in row["years"]}

    table_script = (site / "assets" / "scripts" / "catalog-tables.js").read_text()
    assert "searchPanes" in table_script
    assert "preSelect" in table_script
    assert "collection-problems.json" in table_script
