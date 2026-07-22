"""Renderer inputs.

Pages are composed as pandoc ASTs and written by pandoc's own markdown writer.
Nothing here assembles markdown by hand, so fencing, escaping, and math are the
writer's problem rather than a source of quoting bugs.

Emitted documents carry only semantics: a card's blocks keep the classes their
author wrote (`.problem`, `.solution`, `.hint`), plus attributes drawn from the
catalog. Presentation — what collapses, what is labelled how — is a render-time
decision, and lives in `site/filters/reveal.lua`.

Quarto never sees the corpus. Swapping it out replaces this module and nothing
else.
"""

from __future__ import annotations

import json
import shutil
import sqlite3
from collections import Counter
from pathlib import Path

import panflute as pf
import yaml

from .model import DIV_CLASS_TO_KIND, from_ast


def _rows(con: sqlite3.Connection, sql: str, args: tuple = ()) -> list[sqlite3.Row]:
    con.row_factory = sqlite3.Row
    return con.execute(sql, args).fetchall()


def _terms(con: sqlite3.Connection, card_id: str, axis: str) -> list[str]:
    return [
        r["term"]
        for r in _rows(
            con,
            "select term from classifications where card_id=? and axis=? order by term",
            (card_id, axis),
        )
    ]


# Every authored class is renamed and labelled here, driven off the same map the
# indexer uses. Leaving the theorem-like classes to Quarto was measured to be a
# mistake: Quarto only labels a theorem environment it can cross-reference, i.e.
# one carrying a `#thm-…` id, and the corpus has none, so `.theorem`, `.concept`
# and `.warnings` all rendered as unmarked prose -- exactly the semantics WS1
# exists to preserve, lost at the last step.
OWNED = {cls: f"qual-{kind}" for cls, kind in DIV_CLASS_TO_KIND.items()}

# The class carrying the label. `reveal.lua` replaces the hint, solution and
# occurrence divs outright, so those never reach this rule.
SECTION_CLASS = "qual-section"


def _rename(el: pf.Element, doc: pf.Doc) -> pf.Element:
    if isinstance(el, pf.Div):
        owned = [c for c in el.classes if c in OWNED]
        el.classes = [OWNED[c] if c in OWNED else c for c in el.classes]
        if owned:
            el.classes.append(SECTION_CLASS)
            # The label is the kind alone. The authored `title=` often contains
            # mathematics, and a CSS `content: attr(...)` renders it as literal
            # source; showing `$p\dash$subgroup` is worse than showing nothing.
            el.attributes["data-label"] = DIV_CLASS_TO_KIND[owned[0]].title()
    return el


def _blocks(card: sqlite3.Row) -> list[pf.Block]:
    """Rename owned classes at every depth, not just the top level.

    `reveal.lua` matches on the renamed `qual-*` classes. Renaming only
    top-level divs meant a `solution` nested inside another section kept its
    authored class, never matched the filter, and rendered fully expanded --
    spoiling the problem it was supposed to hide behind a summary.
    """
    return list(from_ast(card["ast"]).walk(_rename).content)


def _inlines(markdown: str) -> list[pf.Inline]:
    parsed = pf.convert_text(markdown, output_format="panflute")
    return list(parsed[0].content) if parsed else [pf.Str("")]


def _link(card: sqlite3.Row, prefix: str = "../tag/") -> pf.Plain:
    return pf.Plain(
        pf.Link(*_inlines(card["title"]), url=f"{prefix}{card['id']}.qmd"),
        pf.Space(),
        pf.Code(card["id"]),
    )


Page = tuple[dict, list[pf.Block]]


def write(page: Page, path: Path) -> None:
    """Front matter is machine-read data; the body is prose.

    They are written by different tools on purpose. Routing the metadata through
    pandoc's markdown writer would escape it as if it were prose — `tag/P-*.qmd`
    comes back out as `tag/P-\\*.qmd` and the listing silently matches nothing.
    """
    meta, blocks = page
    body = (
        pf.convert_text(
            pf.Doc(*blocks),
            input_format="panflute",
            output_format="markdown",
            extra_args=["--wrap=preserve"],
        )
        if blocks
        else ""
    )
    path.write_text("---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).strip() + "\n---\n\n" + body + "\n")


def _related(con: sqlite3.Connection, problem_id: str, kind: str) -> list[sqlite3.Row]:
    return _rows(
        con,
        "select c.* from relations r join cards c on c.id = r.source_id where r.target_id=? and r.kind=? order by c.id",
        (problem_id, kind),
    )


# --- publication manifests --------------------------------------------------


def run_query(con: sqlite3.Connection, q: dict) -> list[sqlite3.Row]:
    """The only query surface a publication manifest gets. Deliberately small.

    Every key is required. A manifest that omits `limit` is a manifest whose
    author has not decided how long the panel is, and the build should say so
    rather than pick a number.
    """
    sql = "select distinct c.* from cards c"
    args: list = []
    for i, topic in enumerate(q["topics"]):
        sql += f" join classifications t{i} on t{i}.card_id=c.id and t{i}.axis='topic' and t{i}.term=?"
        args.append(topic)
    sql += " where c.kind=?"
    args.append(q["kind"])
    if "review" in q:
        sql += " and c.review in ({})".format(",".join("?" * len(q["review"])))
        args += q["review"]
    sql += " order by c.title limit ?"
    args.append(q["limit"])
    return _rows(con, sql, tuple(args))


# --- pages ------------------------------------------------------------------


def problem_page(con: sqlite3.Connection, card: sqlite3.Row) -> Page:
    occurrences = _rows(
        con,
        "select o.*, c.ast, s.title as source_title from occurrences o join cards c on c.id=o.id join cards s on s.id=o.source_id where o.problem_id=? order by o.id",
        (card["id"],),
    )
    # Institution facets come from exam_sources: only a sitting has one. A
    # problem cited from a textbook contributes a year but no institution.
    facets = _rows(
        con,
        "select distinct e.institution, s.year from occurrences o join sources s on s.id=o.source_id join exam_sources e on e.id=s.id where o.problem_id=?",
        (card["id"],),
    )
    institutions = sorted({f["institution"].upper() for f in facets})
    years = sorted({str(f["year"]) for f in facets if f["year"] is not None})
    areas = _terms(con, card["id"], "area")
    topics = _terms(con, card["id"], "topic")

    blocks = _blocks(card)

    for occ in occurrences:
        for block in from_ast(occ["ast"]).content:
            if isinstance(block, pf.Div):
                block.classes = ["qual-occurrence"]
                block.attributes = {
                    "source": occ["source_title"],
                    "locator": occ["locator"],
                    "occurrence": occ["id"],
                }
            blocks.append(block)

    for kind in ("hints-at", "solves"):
        for rel in _related(con, card["id"], kind):
            blocks += _blocks(rel)

    uses = _rows(
        con,
        "select c.* from relations r join cards c on c.id=r.target_id where r.source_id=? and r.kind='uses'",
        (card["id"],),
    )
    if uses:
        blocks.append(pf.Header(pf.Str("Uses"), level=2))
        blocks.append(pf.BulletList(*[pf.ListItem(_link(u)) for u in uses]))

    return {
        "title": card["title"],
        "subtitle": card["id"],
        "area": ", ".join(a.replace("-", " ").title() for a in areas),
        "institutions": ", ".join(institutions) or "—",
        "years": ", ".join(years) or "—",
        "review": card["review"],
        "categories": sorted(set(topics + areas + institutions + years)),
    }, blocks


def plain_page(con: sqlite3.Connection, card: sqlite3.Row) -> Page:
    return {
        "title": card["title"],
        "subtitle": card["id"],
        "categories": sorted(set(_terms(con, card["id"], "topic") + _terms(con, card["id"], "area"))),
    }, _blocks(card)


def source_page(con: sqlite3.Connection, src: sqlite3.Row) -> Page:
    items = _rows(
        con,
        "select o.locator, c.* from occurrences o join cards c on c.id=o.problem_id where o.source_id=? order by cast(o.locator as integer), o.locator",
        (src["id"],),
    )
    # The locator is printed, not encoded in list numbering. A locator is a
    # free-text label on the original sheet -- `3a`, `II.4`, `Problem 3` are all
    # real -- so numbering the list by it either crashes or, worse, renumbers
    # the sheet silently. A bullet carrying the label says what was actually
    # printed on the exam.
    listing = pf.Div(
        pf.BulletList(*[pf.ListItem(pf.Plain(pf.Strong(pf.Str(i["locator"])), pf.Space(), *_link(i).content)) for i in items]),
        classes=["qual-exam-listing"],
    )
    return {"title": src["title"], "subtitle": src["id"]}, [
        pf.Para(pf.Str(str(len(items))), pf.Space(), *_inlines("problems, in the order they appeared.")),
        listing,
    ]


def guide_page(con: sqlite3.Connection, manifest: dict) -> Page:
    blocks: list[pf.Block] = [
        pf.Para(*_inlines("Assembled from a publication manifest: an ordered list of stable IDs and queries. Reordering it touches no card and no catalog row."))
    ]
    for section in manifest["sections"]:
        blocks.append(pf.Header(*_inlines(section["title"]), level=2))
        for item in section["items"]:
            if "ref" in item:
                blocks += _blocks(_rows(con, "select * from cards where id=?", (item["ref"],))[0])
            else:
                hits = run_query(con, item["query"])
                blocks.append(
                    pf.Div(
                        pf.BulletList(*[pf.ListItem(_link(h)) for h in hits]) if hits else pf.Para(pf.Emph(pf.Str("No"), pf.Space(), pf.Str("matches."))),
                        classes=["panel"],
                        attributes={"query-kind": item["query"]["kind"], "count": str(len(hits))},
                    )
                )
    return {"title": manifest["title"]}, blocks


def index_page(con: sqlite3.Connection) -> Page:
    # Counted off what is actually in the catalog, not off a list of kinds kept
    # here. A hand-written list silently omits every kind added after it, and
    # the omission looks exactly like a count of zero.
    counts = Counter(r["kind"] for r in _rows(con, "select kind from cards"))
    labels = {
        "problem": "Problems (canonical)",
        "occurrence": "Occurrences (as they appeared)",
        "source": "Sources",
    }

    def plural(kind: str) -> str:
        stem = kind.title()
        return labels.get(kind) or (f"{stem[:-1]}ies" if stem.endswith("y") else f"{stem}s")

    body = "\n".join(f"| {plural(kind)} | {n} |" for kind, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))
    blocks = pf.convert_text(
        "A proof of concept: markdown cards in git compile to a semantic index, and\n"
        "the site is one projection of that index.\n\n"
        "| Cards | Count |\n|---|---|\n" + body + "\n\n"
        "Start with [the problem browser](problems.qmd), a "
        "[historical exam](exams.qmd), or a [study guide](guides.qmd) — the same "
        "records, arranged three different ways.\n",
        output_format="panflute",
    )
    return {"title": "Qual Corpus"}, list(blocks)


def listing_page(title: str, listing: dict, lede: str) -> Page:
    return {"title": title, "listing": listing}, [pf.Para(*_inlines(lede))]


def link_list_page(con: sqlite3.Connection, title: str, lede: str, rows: list[sqlite3.Row], prefix: str) -> Page:
    return {"title": title}, [
        pf.Para(*_inlines(lede)),
        pf.BulletList(*[pf.ListItem(_link(r, prefix)) for r in rows]),
    ]


# --- project ----------------------------------------------------------------

QUARTO_YML = {
    "project": {"type": "website", "output-dir": "_site"},
    "website": {
        "title": "Qual Corpus",
        "navbar": {
            "left": [
                {"href": "index.qmd", "text": "Home"},
                {"href": "problems.qmd", "text": "Problems"},
                {"href": "exams.qmd", "text": "Exams"},
                {"href": "guides.qmd", "text": "Guides"},
            ]
        },
        "search": {"location": "navbar", "type": "overlay"},
    },
    "filters": ["reveal.lua"],
    "format": {
        "html": {
            "theme": "cosmo",
            "toc": True,
            "include-in-header": "_macros.html",
            "css": "styles.css",
        }
    },
}

PROBLEMS_LISTING = {
    "id": "problems",
    "contents": "tag/P-*.qmd",
    "type": "table",
    "fields": ["title", "area", "institutions", "years", "review"],
    "field-display-names": {
        "title": "Problem",
        "area": "Area",
        "institutions": "Seen at",
        "years": "Years",
        "review": "Status",
    },
    "sort": ["title"],
    "sort-ui": ["title", "area", "years", "review"],
    "filter-ui": True,
    "categories": "cloud",
    "page-size": 100,
}


def mathjax_header(macros: dict) -> str:
    return "<script>\nwindow.MathJax = { tex: { macros: " + json.dumps(macros) + ", inlineMath: [['$','$'],['\\\\(','\\\\)']] } };\n</script>\n"


def project(db: Path, out: Path, publications: Path, site: Path, macros: dict) -> None:
    if out.exists():
        shutil.rmtree(out)
    (out / "tag").mkdir(parents=True)
    (out / "exam").mkdir()
    (out / "guide").mkdir()
    con = sqlite3.connect(db)

    (out / "_quarto.yml").write_text(yaml.safe_dump(QUARTO_YML, sort_keys=False))
    (out / "_macros.html").write_text(mathjax_header(macros))
    for asset in ("styles.css", "filters/reveal.lua"):
        shutil.copy(site / asset, out / Path(asset).name)

    for card in _rows(con, "select * from cards where kind='problem'"):
        write(problem_page(con, card), out / "tag" / f"{card['id']}.qmd")
    # Everything that is not a problem, a source, or an occurrence is envelope
    # plus prose, and gets a plain page. Stated as an exclusion rather than a
    # list of kinds so that adding a kind to the union publishes it, instead of
    # leaving it indexed but unreachable with nothing saying so. Occurrences are
    # deliberately absent: they render inline on the problem they instantiate.
    for card in _rows(con, "select * from cards where kind not in ('problem','source','occurrence')"):
        write(plain_page(con, card), out / "tag" / f"{card['id']}.qmd")
    for src in _rows(con, "select * from cards where kind='source'"):
        write(source_page(con, src), out / "exam" / f"{src['id']}.qmd")

    guides = []
    for path in sorted(publications.glob("*.yaml")):
        manifest = yaml.safe_load(path.read_text())
        write(guide_page(con, manifest), out / "guide" / f"{manifest['id']}.qmd")
        guides.append(manifest)

    write(
        listing_page(
            "Problems",
            PROBLEMS_LISTING,
            "Every problem in the corpus. Filter by any facet; the URL is the query.",
        ),
        out / "problems.qmd",
    )
    write(
        link_list_page(
            con,
            "Exams",
            "Historical sittings, each a fixed ordered list of occurrences.",
            _rows(
                con,
                "select c.* from cards c join sources s on s.id=c.id join exam_sources e on e.id=s.id order by e.institution, s.year, c.id",
            ),
            "exam/",
        ),
        out / "exams.qmd",
    )
    write(
        (
            {"title": "Guides"},
            [pf.BulletList(*[pf.ListItem(pf.Plain(pf.Link(pf.Str(g["title"]), url=f"guide/{g['id']}.qmd"))) for g in guides])],
        ),
        out / "guides.qmd",
    )
    write(index_page(con), out / "index.qmd")
    con.close()
