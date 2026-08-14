"""Corpus projections.

Pages are composed as Pandoc ASTs and batch-written as both QMD and HTML.
Nothing here assembles either projection by hand, so fencing, escaping, and
math remain the writer's problem rather than a source of quoting bugs.

Emitted documents carry only semantics: a card's blocks keep the classes their
author wrote (`.problem`, `.solution`, `.hint`), plus attributes drawn from the
catalog. The direct HTML projection owns the shared shell and presentation;
generated QMD remains available as an inspectable secondary artifact.
"""

from __future__ import annotations

import copy
import html
import json
import re
import shutil
import sqlite3
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import panflute as pf
import yaml

from .model import DIV_CLASS_TO_KIND, MARKDOWN, from_ast, to_json
from .pandoc_batch import (
    PandocBatchError,
    PandocFailure,
    PandocResult,
    PandocServer,
)
from .publication import (
    AnyReview,
    PublicationManifest,
    PublicationQuery,
    PublicationSection,
    QueryItem,
    ReferenceItem,
    SelectedReviews,
    load_publications,
)
from .static_site import (
    AssetCatalog,
    AuthoredPage,
    EndReading,
    LevelOnly,
    MiddleReading,
    NavigationLink,
    NavigationParent,
    NodeParent,
    PageChrome,
    PageTarget,
    PublicationNavigation,
    ReadingLink,
    RootParent,
    StandardPage,
    StartReading,
    SubjectPage,
    build_asset_catalog,
    write_page,
    write_search_index,
)
from .wiki import (
    WIKI_BATCH_SIZE,
    WikiPage,
)
from .wiki import (
    link_targets as wiki_link_targets,
)
from .wiki import (
    search_records as wiki_search_records,
)

KNOWN_PANDOC_WARNINGS = (
    "Could not load translations for en-US",
    "The term Abstract has no translation defined.",
)


def _rows(con: sqlite3.Connection, sql: str, args: tuple = ()) -> list[sqlite3.Row]:
    con.row_factory = sqlite3.Row
    return con.execute(sql, args).fetchall()


def _successful_outputs(
    results: list[PandocResult],
    operation: str,
    ignored: tuple[str, ...] = KNOWN_PANDOC_WARNINGS,
) -> list[str]:
    outputs: list[str] = []
    for index, result in enumerate(results):
        match result:
            case PandocFailure(error=error):
                raise PandocBatchError(f"pandoc {operation} failed for item {index}: {error}")
        warnings = [message.message for message in result.messages if message.verbosity == "WARNING" and not message.message.startswith(ignored)]
        if warnings:
            raise ValueError(f"pandoc {operation} warned for item {index}: {'; '.join(warnings)}")
        outputs.append(result.output)
    return outputs


def _successful_html_outputs(
    results: list[PandocResult],
    operation: str,
) -> list[str]:
    """Accept only PandocPure's two missing-localization notices.

    Fragment HTML does not use either localized value, but Pandoc's HTML writer
    still attempts to load them. Every content warning remains fatal.
    """
    outputs: list[str] = []
    for index, result in enumerate(results):
        match result:
            case PandocFailure(error=error):
                raise PandocBatchError(f"pandoc {operation} failed for item {index}: {error}")
        warnings = [message.message for message in result.messages if message.verbosity == "WARNING" and not message.message.startswith(KNOWN_PANDOC_WARNINGS)]
        if warnings:
            raise ValueError(f"pandoc {operation} warned for item {index}: {'; '.join(warnings)}")
        outputs.append(result.output)
    return outputs


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


def _owned_class(class_name: str) -> str:
    if class_name in OWNED:
        return OWNED[class_name]
    return class_name


# A `title=` on a hint, solution or occurrence would land inside the `<details>`
# those become, below the summary that already names them.
TITLED_KINDS = set(DIV_CLASS_TO_KIND.values()) - {"hint", "solution"}


def _title_html(title: str) -> str:
    """The authored `title=` as body text, so it is read rather than hovered.

    It goes in the body and not in a CSS `content: attr(...)` because the titles
    carry mathematics -- `$p\\dash$-subgroup` and the like -- and `attr()` would
    print that as its source. In the body MathJax typesets it like any other
    `$...$` on the page.
    """
    return f'<p class="qual-section-title">{html.escape(title)}</p>'


def _rename(el: pf.Element, doc: pf.Doc) -> pf.Element:
    if isinstance(el, pf.Div):
        owned = [c for c in el.classes if c in OWNED]
        el.classes = [_owned_class(class_name) for class_name in el.classes]
        if owned:
            kind = DIV_CLASS_TO_KIND[owned[0]]
            el.classes.append(SECTION_CLASS)
            el.attributes["data-label"] = kind.title()
            title = el.attributes["title"].strip() if "title" in el.attributes else ""
            if title and kind in TITLED_KINDS:
                el.content.insert(0, pf.RawBlock(_title_html(title), format="html"))
    return el


REVEAL_LABELS = {
    "qual-hint": "Hint",
    "qual-solution": "Solution",
    "qual-occurrence": "As it appeared",
}

# Authored div classes whose content answers the problem instead of stating it.
# A tag page may hide them behind a disclosure; a printable practice sheet must
# not carry them at all.
ANSWER_CLASSES = {"solution", "hint", "proof", "strategy", "concept", "warnings"}

# The same material also occurs unwrapped, as a paragraph or list item whose
# leading bold run labels it.
ANSWER_LABELS = {"solution", "hint", "answer"}


def _answer_label(block: pf.Element) -> str:
    if not isinstance(block, pf.Para | pf.Plain) or not block.content:
        return ""
    head = block.content[0]
    if not isinstance(head, pf.Strong):
        return ""
    return pf.stringify(head).strip().rstrip(":").lower()


def _statement_only(
    element: pf.Element,
    document: pf.Doc,
) -> pf.Element | list[pf.Block] | None:
    """Drop every block that answers the problem instead of stating it.

    `walk` is bottom-up, so a labelled paragraph inside a list item is removed
    before the item is visited; the emptied item is then removed as well, rather
    than surviving as a stray bullet."""
    del document
    if isinstance(element, pf.Div) and ANSWER_CLASSES.intersection(element.classes):
        return []
    if isinstance(element, pf.ListItem):
        return [] if not element.content else None
    if _answer_label(element) in ANSWER_LABELS:
        return []
    return None


def _reveal(
    element: pf.Element,
    document: pf.Doc,
) -> pf.Element | list[pf.Block] | None:
    del document
    if not isinstance(element, pf.Div):
        return None
    reveal_class = next(
        (class_name for class_name in element.classes if class_name in REVEAL_LABELS),
        None,
    )
    if reveal_class is None:
        return None
    summary = REVEAL_LABELS[reveal_class]
    if reveal_class == "qual-occurrence":
        if "source" in element.attributes:
            summary = element.attributes["source"]
        locator = element.attributes.get("locator")
        if locator:
            summary += f", problem {locator}"
    opening = f'<details class="reveal {reveal_class}"><summary>{html.escape(summary)}</summary>'
    return [
        pf.RawBlock(opening, format="html"),
        *element.content,
        pf.RawBlock("</details>", format="html"),
    ]


def _blocks(card: sqlite3.Row) -> list[pf.Block]:
    """Rename owned classes at every depth, not just the top level.

    `reveal.lua` matches on the renamed `qual-*` classes. Renaming only
    top-level divs meant a `solution` nested inside another section kept its
    authored class, never matched the filter, and rendered fully expanded --
    spoiling the problem it was supposed to hide behind a summary.
    """
    return list(from_ast(card["ast"]).walk(_rename).content)


def _wiki_branch(page: WikiPage) -> str:
    """The subject a page belongs to: its top directory, or the wiki root."""
    parts = page.source_rel.parts
    return parts[0] if len(parts) > 1 else ""


def _wiki_navigation(pages: list[WikiPage]) -> dict[str, PublicationNavigation]:
    """Breadcrumbs and reading order for every authored page, by route.

    A page's trail is the directory path it is filed under, which is the
    hierarchy the author built and the one the subtitle already shows. Reading
    order is filename order within the branch, which is what the tree merge at
    `fd37c3d1` preserved when it sorted the named tree into the numbered one.

    A directory carries a `NavigationLink` with no target: it names a level of
    the trail but has no page of its own to link to.
    """
    navigation: dict[str, PublicationNavigation] = {}
    for branch in sorted({_wiki_branch(page) for page in pages}):
        members = sorted(
            (page for page in pages if _wiki_branch(page) == branch),
            key=lambda page: page.source_rel.as_posix(),
        )
        links: dict[str, NavigationLink] = {}
        for page in members:
            parent: NavigationParent = RootParent()
            for depth in range(1, len(page.source_rel.parts)):
                key = "/".join(page.source_rel.parts[:depth])
                if key not in links:
                    links[key] = NavigationLink(
                        key=key,
                        title=page.source_rel.parts[depth - 1].replace("_", " "),
                        target=LevelOnly(),
                        parent=parent,
                    )
                parent = NodeParent(key)
            links[page.route.as_posix()] = NavigationLink(
                key=page.route.as_posix(),
                title=page.title,
                target=PageTarget(page.route),
                parent=parent,
            )
        ordered = tuple(links.values())
        for index, page in enumerate(members):
            previous = members[index - 1] if index else None
            following = members[index + 1] if index + 1 < len(members) else None
            key = page.route.as_posix()
            position: StartReading | MiddleReading | EndReading
            if previous is None and following is not None:
                position = StartReading(following=ReadingLink.of(links[following.route.as_posix()]))
            elif following is None and previous is not None:
                position = EndReading(previous=ReadingLink.of(links[previous.route.as_posix()]))
            elif previous is not None and following is not None:
                position = MiddleReading(
                    previous=ReadingLink.of(links[previous.route.as_posix()]),
                    following=ReadingLink.of(links[following.route.as_posix()]),
                )
            else:
                # A branch of one page has nowhere to go; it keeps its trail.
                continue
            navigation[key] = PublicationNavigation(
                links=ordered,
                current_key=key,
                position=position,
            )
    return navigation


def _wiki_chrome(
    navigation: dict[str, PublicationNavigation],
    page: WikiPage,
) -> PageChrome:
    found = navigation.get(page.route.as_posix())
    return AuthoredPage(found) if found else StandardPage()


def _wiki_blocks(page: WikiPage) -> list[pf.Block]:
    """An authored wiki page gets the same section labelling a card gets.

    Only the card path ran `_rename`, so every `:::{.remark}`, `:::{.proof}`
    and `:::{.fact}` on the wiki reached the reader as unmarked prose: the
    label rule in `styles.css` keys on the `qual-section` class this adds.
    """
    return list(pf.Doc(*page.blocks).walk(_rename).content)


# --- raw-JSON tag-page path -------------------------------------------------
#
# The 3,200 tag pages are the bulk of the build. Composing them through panflute
# means one pandoc process per card to load and one per page to write -- an hour.
# Their bodies are only a card's own blocks plus, for a problem, its inlined
# occurrences and any solution or hint. No `uses` link, no title parsing: every
# piece is already pandoc JSON in the catalog. These pages are assembled as JSON
# and written in bounded batches through one persistent Pandoc server. The other
# pages use the same writer boundary after Panflute composition.


@dataclass(frozen=True)
class Appearance:
    target_key: str
    title: str
    basis: str


def _card_relation_items(
    rows: list[sqlite3.Row],
) -> str:
    if not rows:
        return '<p class="relation-empty">None.</p>'
    return (
        "<ul>"
        + "".join(
            "<li>"
            f'<a href="{html.escape(row["id"], quote=True)}">'
            f"<code>{html.escape(row['id'])}</code></a>"
            f"<span>{html.escape(row['title'])}</span>"
            f"<small>{html.escape(row['relation_kind'])}</small>"
            "</li>"
            for row in rows
        )
        + "</ul>"
    )


def _appearance_items(appearances: list[Appearance]) -> str:
    if not appearances:
        return '<p class="relation-empty">None.</p>'
    return (
        "<ul>"
        + "".join(
            f'<li><a href="{html.escape(appearance.target_key, quote=True)}">{html.escape(appearance.title)}</a><small>{html.escape(appearance.basis)}</small></li>'
            for appearance in appearances
        )
        + "</ul>"
    )


def _relation_groups_json(
    con: sqlite3.Connection,
    card_id: str,
    appearances: dict[str, list[Appearance]],
) -> dict:
    dependencies = _rows(
        con,
        """
        select c.id, c.title, r.kind as relation_kind
        from relations r join cards c on c.id=r.target_id
        where r.source_id=? and r.kind in ('uses', 'cites', 'extracted-from')
        order by r.kind, c.title, c.id
        """,
        (card_id,),
    )
    backlinks = _rows(
        con,
        """
        select c.id, c.title, r.kind as relation_kind
        from relations r join cards c on c.id=r.source_id
        where r.target_id=? and r.kind != 'instance-of'
        order by r.kind, c.title, c.id
        """,
        (card_id,),
    )
    source = (
        '<div class="relation-groups" aria-label="Card relationships">'
        '<section class="relation-group" data-relation-group="dependencies">'
        "<h2>Authored dependencies</h2>"
        f"{_card_relation_items(dependencies)}"
        "</section>"
        '<section class="relation-group" data-relation-group="appearances">'
        "<h2>Derived appearances</h2>"
        f"{_appearance_items(appearances[card_id])}"
        "</section>"
        '<section class="relation-group" data-relation-group="backlinks">'
        "<h2>Backlinks</h2>"
        f"{_card_relation_items(backlinks)}"
        "</section>"
        "</div>"
    )
    return {"t": "RawBlock", "c": ["html", source]}


def load_json(con: sqlite3.Connection) -> tuple[dict, list]:
    """{card id -> its body block list} as raw pandoc JSON, plus the api version."""
    cache, api = {}, [1, 23]
    for r in _rows(con, "select id, ast from cards"):
        doc = json.loads(r["ast"])
        api = doc["pandoc-api-version"]
        cache[r["id"]] = doc["blocks"]
    return cache, api


def _rename_json(node: object) -> None:
    """The `_rename` transform, on raw JSON: rename owned Div classes at any depth."""
    if isinstance(node, list):
        for x in node:
            _rename_json(x)
    elif isinstance(node, dict):
        if node.get("t") == "Div":
            attr = node["c"][0]  # [id, classes, keyvals]
            owned = [c for c in attr[1] if c in OWNED]
            attr[1] = [_owned_class(class_name) for class_name in attr[1]]
            if owned:
                kind = DIV_CLASS_TO_KIND[owned[0]]
                attr[1].append(SECTION_CLASS)
                attr[2].append(["data-label", kind.title()])
                title = next((value.strip() for key, value in attr[2] if key == "title"), "")
                if title and kind in TITLED_KINDS:
                    node["c"][1].insert(0, {"t": "RawBlock", "c": ["html", _title_html(title)]})
        _rename_json(node.get("c"))


def _dup[T](value: T) -> T:
    return copy.deepcopy(value)


def problem_json(
    con: sqlite3.Connection,
    card: sqlite3.Row,
    jcache: dict,
    appearances: dict[str, list[Appearance]],
) -> tuple[dict, list]:
    facets = _rows(
        con,
        "select distinct e.institution, s.year from occurrences o join sources s on s.id=o.source_id join exam_sources e on e.id=s.id where o.problem_id=?",
        (card["id"],),
    )
    institutions = sorted({f["institution"].upper() for f in facets})
    years = sorted({str(f["year"]) for f in facets if f["year"] is not None})
    areas = _terms(con, card["id"], "area")
    topics = _terms(con, card["id"], "topic")

    body = _dup(jcache[card["id"]])
    _rename_json(body)
    for occ in _rows(
        con,
        "select o.*, s.title as source_title from occurrences o join cards s on s.id=o.source_id where o.problem_id=? order by o.id",
        (card["id"],),
    ):
        blocks = _dup(jcache[occ["id"]])
        for b in blocks:
            if b.get("t") == "Div":
                kv = [
                    ["source", occ["source_title"]],
                    ["locator", occ["locator"]],
                    ["occurrence", occ["id"]],
                ]
                b["c"][0] = [b["c"][0][0], ["qual-occurrence"], kv]
        body += blocks
    for kind in ("hints-at", "solves"):
        for rel in _related(con, card["id"], kind):
            rb = _dup(jcache[rel["id"]])
            _rename_json(rb)
            body += rb
    body.append(_relation_groups_json(con, card["id"], appearances))
    meta = {
        "title": card["title"],
        "subtitle": card["id"],
        "area": ", ".join(a.replace("-", " ").title() for a in areas),
        "institutions": ", ".join(institutions) or "—",
        "years": ", ".join(years) or "—",
        "review": card["review"],
        "categories": sorted(set(topics + areas + institutions + years)),
    }
    return meta, body


def plain_json(
    con: sqlite3.Connection,
    card: sqlite3.Row,
    jcache: dict,
    appearances: dict[str, list[Appearance]],
) -> tuple[dict, list]:
    body = _dup(jcache[card["id"]])
    _rename_json(body)
    body.append(_relation_groups_json(con, card["id"], appearances))
    meta = {
        "title": card["title"],
        "subtitle": card["id"],
        "categories": sorted(set(_terms(con, card["id"], "topic") + _terms(con, card["id"], "area"))),
    }
    return meta, body


def write_json_pages(
    pandoc: PandocServer,
    items: list[tuple[Path, dict, list]],
    api: list,
    site_root: Path,
    mathjax: str,
    link_targets: dict[str, Path],
    assets: AssetCatalog,
) -> None:
    """Convert every tag page independently through one persistent server."""
    documents = [
        json.dumps(
            {
                "pandoc-api-version": api,
                "meta": {},
                "blocks": blocks,
            }
        )
        for _, _, blocks in items
    ]
    bodies = _successful_outputs(
        pandoc.write_markdown(documents, MARKDOWN),
        "tag-page write",
    )
    html_bodies = _successful_html_outputs(
        pandoc.write_html([_html_ast(document) for document in documents]),
        "tag-page HTML write",
    )
    for (path, meta, _), body, html_body in zip(
        items,
        bodies,
        html_bodies,
        strict=True,
    ):
        path.write_text(
            "---\n"
            + yaml.safe_dump(
                meta,
                sort_keys=False,
                allow_unicode=True,
            ).strip()
            + "\n---\n\n"
            + body.strip()
            + "\n"
        )
        write_page(
            site_root,
            path.relative_to(site_root.parent).with_suffix(".html"),
            meta,
            html_body,
            mathjax,
            link_targets,
            assets,
            StandardPage(),
        )


def _inline_source(markdown: str) -> str:
    # A title is inline text, but some are lifted verbatim from a statement's
    # first line and still carry a leading list/quote/heading marker, which
    # pandoc parses as a block wrapper whose children are ListItems, not inlines.
    return re.sub(r"^\s*([-*+]|\d+[.)]|>|#{1,6})\s+", "", markdown)


INLINE_SENTINEL = "QUALINLINEBOUNDARY"


def build_inline_cache(
    pandoc: PandocServer,
    markdown_values: list[str],
) -> dict[str, list[pf.Inline]]:
    sources = list(dict.fromkeys(_inline_source(value) for value in markdown_values))
    outputs = _successful_outputs(
        pandoc.read_markdown(
            [INLINE_SENTINEL + source for source in sources],
            MARKDOWN,
        ),
        "inline read",
    )
    cache: dict[str, list[pf.Inline]] = {}
    for source, output in zip(sources, outputs, strict=True):
        document = from_ast(output)
        if len(document.content) != 1 or not isinstance(
            document.content[0],
            (pf.Para, pf.Plain),
        ):
            raise ValueError(f"inline text parsed as block structure: {source!r}")
        inlines = list(document.content[0].content)
        if not inlines or not isinstance(inlines[0], pf.Str):
            raise ValueError(f"inline boundary was not preserved: {source!r}")
        if not inlines[0].text.startswith(INLINE_SENTINEL):
            raise ValueError(f"inline boundary was corrupted: {source!r}")
        inlines[0].text = inlines[0].text.removeprefix(INLINE_SENTINEL)
        if not inlines[0].text:
            inlines.pop(0)
        cache[source] = inlines
    return cache


def _inlines(
    markdown: str,
    cache: dict[str, list[pf.Inline]],
) -> list[pf.Inline]:
    source = _inline_source(markdown)
    if source not in cache:
        raise ValueError(f"inline text was not batched: {source!r}")
    return copy.deepcopy(cache[source])


def _link(
    card: sqlite3.Row,
    inline_cache: dict[str, list[pf.Inline]],
    prefix: str = "../tag/",
) -> pf.Plain:
    return pf.Plain(
        pf.Link(
            *_inlines(card["title"], inline_cache),
            url=f"{prefix}{card['id']}.html",
        ),
        pf.Space(),
        pf.Code(card["id"]),
    )


Page = tuple[dict, list[pf.Block]]
PageItem = tuple[Page, Path, PageChrome]


def _page_ast(page: Page) -> str:
    _, blocks = page
    return to_json(pf.Doc(*blocks))


def _html_ast(ast: str) -> str:
    return to_json(from_ast(ast).walk(_reveal))


def _statement_ast(ast: str) -> str:
    return to_json(from_ast(ast).walk(_statement_only))


def write_pages(
    pandoc: PandocServer,
    items: list[PageItem],
    site_root: Path,
    mathjax: str,
    link_targets: dict[str, Path],
    assets: AssetCatalog,
) -> None:
    """Front matter is machine-read data; the body is prose.

    They are written by different tools on purpose. Routing the metadata through
    pandoc's markdown writer would escape it as if it were prose — `tag/P-*.qmd`
    comes back out as `tag/P-\\*.qmd` and the listing silently matches nothing.
    """
    documents = [_page_ast(page) for page, _, _ in items]
    bodies = _successful_outputs(
        pandoc.write_markdown(documents, MARKDOWN),
        "page write",
    )
    html_bodies = _successful_html_outputs(
        pandoc.write_html([_html_ast(document) for document in documents]),
        "page HTML write",
    )
    for ((meta, _), path, navigation), body, html_body in zip(
        items,
        bodies,
        html_bodies,
        strict=True,
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "---\n"
            + yaml.safe_dump(
                meta,
                sort_keys=False,
                allow_unicode=True,
            ).strip()
            + "\n---\n\n"
            + body
            + "\n"
        )
        write_page(
            site_root,
            path.relative_to(site_root.parent).with_suffix(".html"),
            meta,
            html_body,
            mathjax,
            link_targets,
            assets,
            navigation,
        )


def _related(con: sqlite3.Connection, problem_id: str, kind: str) -> list[sqlite3.Row]:
    return _rows(
        con,
        "select c.* from relations r join cards c on c.id = r.source_id where r.target_id=? and r.kind=? order by c.id",
        (problem_id, kind),
    )


# --- publication manifests --------------------------------------------------


def run_query(
    con: sqlite3.Connection,
    query: PublicationQuery,
    area: str,
) -> list[sqlite3.Row]:
    """The only query surface a publication manifest gets. Deliberately small.

    Every key is required. A manifest that omits `limit` is a manifest whose
    author has not decided how long the panel is, and the build should say so
    rather than pick a number.

    `area` is the guide's own subject, not a manifest key: the panel renders
    inside a subject section and reads as scoped to it, so a query is scoped
    whether or not its author thought about scoping.

    `topics` matches a card carrying **any** of them. Topic vocabulary is finer
    than a section: convergence alone splits four ways, and a section about
    convergence wants all of it. One join per topic asked for a card carrying
    every one, which no card does, so the panel a section actually wants was
    unsayable.
    """
    sql = "select distinct c.* from cards c join classifications a on a.card_id=c.id and a.axis='area' and a.term=?"
    args: list = [area]
    if query.topics:
        sql += " join classifications t on t.card_id=c.id and t.axis='topic' and t.term in ({})".format(",".join("?" * len(query.topics)))
        args += list(query.topics)
    sql += " where c.kind=?"
    args.append(query.kind)
    match query.review:
        case AnyReview():
            pass
        case SelectedReviews(values=reviews):
            sql += " and c.review in ({})".format(",".join("?" * len(reviews)))
            args += reviews
    sql += " order by c.title limit ?"
    args.append(query.limit)
    return _rows(con, sql, tuple(args))


# --- pages ------------------------------------------------------------------


def problem_page(
    con: sqlite3.Connection,
    card: sqlite3.Row,
    inline_cache: dict[str, list[pf.Inline]],
) -> Page:
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
        blocks.append(pf.BulletList(*[pf.ListItem(_link(u, inline_cache)) for u in uses]))

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


def source_page(
    con: sqlite3.Connection,
    src: sqlite3.Row,
    inline_cache: dict[str, list[pf.Inline]],
) -> Page:
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
        pf.BulletList(
            *[
                pf.ListItem(
                    pf.Plain(
                        pf.Strong(pf.Str(i["locator"])),
                        pf.Space(),
                        *_link(i, inline_cache).content,
                    )
                )
                for i in items
            ]
        ),
        classes=["qual-exam-listing"],
    )
    return {"title": src["title"], "subtitle": src["id"]}, [
        pf.Para(
            pf.Str(str(len(items))),
            pf.Space(),
            *_inlines(
                "problems, in the order they appeared.",
                inline_cache,
            ),
        ),
        listing,
    ]


def _publication_root_route(
    manifest: PublicationManifest,
) -> Path:
    return Path("guide") / f"{manifest.id}.html"


def _publication_section_route(
    manifest: PublicationManifest,
    section: PublicationSection,
) -> Path:
    return Path("guide") / manifest.id / f"{section.slug}.html"


def _publication_root_target_key(
    manifest: PublicationManifest,
) -> str:
    return manifest.id


def _publication_section_target_key(
    manifest: PublicationManifest,
    section: PublicationSection,
) -> str:
    return f"{manifest.id}/{section.slug}"


def _publication_navigation(
    manifest: PublicationManifest,
    current_key: str,
) -> PublicationNavigation:
    links = (
        NavigationLink(
            key=manifest.id,
            title=manifest.title,
            target=PageTarget(_publication_root_route(manifest)),
            parent=RootParent(),
        ),
        *(
            NavigationLink(
                key=section.slug,
                title=section.title,
                target=PageTarget(_publication_section_route(manifest, section)),
                parent=NodeParent(section.parent),
            )
            for section in manifest.sections
        ),
    )
    ordered = list(links)
    index = next(i for i, link in enumerate(ordered) if link.key == current_key)
    position: StartReading | MiddleReading | EndReading
    if index == 0:
        position = StartReading(following=ReadingLink.of(ordered[1]))
    elif index == len(ordered) - 1:
        position = EndReading(previous=ReadingLink.of(ordered[-2]))
    else:
        position = MiddleReading(
            previous=ReadingLink.of(ordered[index - 1]),
            following=ReadingLink.of(ordered[index + 1]),
        )
    return PublicationNavigation(
        links=links,
        current_key=current_key,
        position=position,
    )


def _manifest_card(
    con: sqlite3.Connection,
    card_id: str,
) -> sqlite3.Row:
    matches = _rows(con, "select * from cards where id=?", (card_id,))
    if not matches:
        raise ValueError(f"publication references unknown card: {card_id}")
    return matches[0]


def _publication_card(
    card: sqlite3.Row,
    inline_cache: dict[str, list[pf.Inline]],
) -> list[pf.Block]:
    card_id = html.escape(card["id"], quote=True)
    return [
        pf.RawBlock(
            f'<section class="publication-card" data-card-id="{card_id}">',
            format="html",
        ),
        pf.Header(
            pf.Link(
                *_inlines(card["title"], inline_cache),
                url=card["id"],
            ),
            pf.Space(),
            pf.Code(card["id"]),
            level=2,
        ),
        *_blocks(card),
        pf.RawBlock("</section>", format="html"),
    ]


def publication_root_page(
    manifest: PublicationManifest,
    inline_cache: dict[str, list[pf.Inline]],
) -> Page:
    return {"title": manifest.title}, [
        pf.Para(
            *_inlines(manifest.lede, inline_cache),
        ),
        pf.OrderedList(
            *[
                pf.ListItem(
                    pf.Plain(
                        pf.Link(
                            *_inlines(section.title, inline_cache),
                            url=_publication_section_target_key(manifest, section),
                        )
                    )
                )
                for section in manifest.sections
            ]
        ),
    ]


def publication_section_page(
    con: sqlite3.Connection,
    manifest: PublicationManifest,
    section: PublicationSection,
    inline_cache: dict[str, list[pf.Inline]],
) -> Page:
    blocks: list[pf.Block] = [
        pf.Para(*_inlines(section.lede, inline_cache)),
    ]
    for item in section.items:
        match item:
            case ReferenceItem(ref=card_id):
                blocks += _publication_card(
                    _manifest_card(con, card_id),
                    inline_cache,
                )
            case QueryItem(query=query):
                hits = run_query(con, query, manifest.area)
                if not hits:
                    raise ValueError(f"publication query has no matches in area {manifest.area}: {manifest.id}/{section.slug}")
                blocks.append(
                    pf.Div(
                        pf.Header(
                            *_inlines("More from the catalog", inline_cache),
                            level=2,
                        ),
                        pf.BulletList(
                            *[
                                pf.ListItem(
                                    pf.Plain(
                                        pf.Link(
                                            *_inlines(hit["title"], inline_cache),
                                            url=hit["id"],
                                        ),
                                        pf.Space(),
                                        pf.Code(hit["id"]),
                                    )
                                )
                                for hit in hits
                            ]
                        ),
                        classes=["panel", "publication-query"],
                        attributes={
                            "query-kind": query.kind,
                            "count": str(len(hits)),
                        },
                    )
                )
    return {"title": section.title}, blocks


def card_appearances(
    con: sqlite3.Connection,
    manifests: list[PublicationManifest],
) -> dict[str, list[Appearance]]:
    """Where each card shows up: guide sections, and for a problem, its sittings.

    The sitting edge is the reverse of the 2,798 links an exam page already
    carries. Without it a problem page names the sitting it came from in the
    occurrence disclosure but offers no way to reach it."""
    appearances: dict[str, list[Appearance]] = {row["id"]: [] for row in _rows(con, "select id from cards order by id")}
    seen: set[tuple[str, str]] = set()
    for occurrence in _rows(
        con,
        """
        select o.problem_id, o.source_id, o.locator, c.title
        from occurrences o join cards c on c.id=o.source_id
        order by c.title, o.locator = '?', o.locator, o.id
        """,
    ):
        # One link per sitting. A problem recorded twice at the same sitting is
        # usually one occurrence with a locator and one without; ordering puts
        # the located one first, so that is the row that survives.
        key = (occurrence["problem_id"], occurrence["source_id"])
        if key in seen:
            continue
        seen.add(key)
        locator = occurrence["locator"]
        title = occurrence["title"]
        if locator and locator != "?":
            title += f", problem {locator}"
        appearances[occurrence["problem_id"]].append(
            Appearance(
                target_key=occurrence["source_id"],
                title=title,
                basis="Exam sitting",
            )
        )
    for manifest in manifests:
        for section in manifest.sections:
            target_key = _publication_section_target_key(manifest, section)
            for item in section.items:
                match item:
                    case ReferenceItem(ref=card_id):
                        _manifest_card(con, card_id)
                        appearances[card_id].append(
                            Appearance(
                                target_key=target_key,
                                title=section.title,
                                basis="Authored reference",
                            )
                        )
                    case QueryItem(query=query):
                        hits = run_query(con, query, manifest.area)
                        if not hits:
                            raise ValueError(f"publication query has no matches in area {manifest.area}: {manifest.id}/{section.slug}")
                        for hit in hits:
                            appearances[hit["id"]].append(
                                Appearance(
                                    target_key=target_key,
                                    title=section.title,
                                    basis=f"Catalog query: {query.kind}",
                                )
                            )
    return appearances


def index_page(
    pandoc: PandocServer,
    con: sqlite3.Connection,
) -> Page:
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
    output = _successful_outputs(
        pandoc.read_markdown(
            [
                "A proof of concept: markdown cards in git compile to a semantic index, and\n"
                "the site is one projection of that index.\n\n"
                "| Cards | Count |\n|---|---|\n" + body + "\n\n"
                "Start with [the problem browser](problems.html), a "
                "[historical exam](exams.html), or a [study guide](guides.html) — the same "
                "records, arranged three different ways.\n"
            ],
            MARKDOWN,
        ),
        "index-page read",
    )
    return {"title": "Qual Corpus"}, list(from_ast(output[0]).content)


def listing_page(
    title: str,
    listing: dict,
    lede: str,
    inline_cache: dict[str, list[pf.Inline]],
) -> Page:
    return {"title": title, "listing": listing}, [pf.Para(*_inlines(lede, inline_cache))]


def problem_browser_page(
    con: sqlite3.Connection,
    inline_cache: dict[str, list[pf.Inline]],
) -> Page:
    problems = _rows(
        con,
        """
        select c.*,
          (select group_concat(term, ' ') from classifications
           where card_id=c.id and axis='area') as areas,
          (select group_concat(term, ' ') from classifications
           where card_id=c.id and axis='topic') as topics,
          (select group_concat(distinct upper(e.institution))
           from occurrences o join exam_sources e on e.id=o.source_id
           where o.problem_id=c.id) as institutions,
          (select group_concat(distinct s.year)
           from occurrences o join sources s on s.id=o.source_id
           where o.problem_id=c.id and s.year is not null) as years
        from cards c
        where c.kind='problem'
        order by c.title, c.id
        """,
    )
    rows: list[pf.Block] = []
    for problem in problems:
        facets = " · ".join(
            value.replace("-", " ").title()
            for value in (
                problem["areas"] or "",
                problem["institutions"] or "",
                problem["years"] or "",
            )
            if value
        )
        search = " ".join(
            str(value)
            for value in (
                problem["title"],
                problem["id"],
                problem["areas"],
                problem["topics"],
                problem["institutions"],
                problem["years"],
            )
            if value
        ).lower()
        rows.append(
            pf.Div(
                _link(problem, inline_cache, prefix="tag/"),
                pf.Plain(pf.Str(facets or "Unclassified")),
                classes=["problem-row"],
                attributes={"data-search": search},
            )
        )
    return {"title": "Problems"}, [
        pf.Para(
            *_inlines(
                "Every problem in the corpus. Filter by any facet; the URL is the query.",
                inline_cache,
            )
        ),
        pf.RawBlock(
            '<label for="problem-filter">Filter problems</label><input id="problem-filter" type="search" placeholder="Group theory, UGA, 2019…">',
            format="html",
        ),
        pf.Div(*rows, classes=["problem-browser"]),
    ]


def link_list_page(
    con: sqlite3.Connection,
    title: str,
    lede: str,
    rows: list[sqlite3.Row],
    prefix: str,
    inline_cache: dict[str, list[pf.Inline]],
) -> Page:
    return {"title": title}, [
        pf.Para(*_inlines(lede, inline_cache)),
        pf.BulletList(*[pf.ListItem(_link(row, inline_cache, prefix)) for row in rows]),
    ]


# --- project ----------------------------------------------------------------

QUARTO_YML = {
    "project": {"type": "website", "output-dir": "_site"},
    "website": {
        "title": "Qual Corpus",
        "navbar": {
            "left": [
                {"href": "index.qmd", "text": "Home"},
                {"href": "problems.qmd", "text": "Browse"},
                {"href": "generate.qmd", "text": "Generate"},
                {"href": "exams.qmd", "text": "Exams"},
                {"href": "guides.qmd", "text": "Guides"},
                {"href": "wiki/index.qmd", "text": "Wiki"},
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
    mathjax_macros: dict[str, object] = {}
    for tex_name, definition in macros.items():
        if not isinstance(tex_name, str):
            raise TypeError(f"invalid TeX macro name type: {type(tex_name).__name__}")
        if not tex_name.startswith("\\") or tex_name == "\\":
            raise ValueError(f"invalid TeX macro name: {tex_name!r}")
        if not isinstance(definition, str):
            raise TypeError(f"invalid definition for TeX macro {tex_name}: {definition!r}")
        name = tex_name[1:]
        if name in mathjax_macros:
            raise ValueError(f"duplicate MathJax macro name: {name}")
        parameters = {int(match.group(1)) for match in re.finditer(r"(?<!\\)#([1-9])", definition)}
        if parameters:
            argument_count = max(parameters)
            expected = set(range(1, argument_count + 1))
            if parameters != expected:
                raise ValueError(f"non-contiguous parameters for TeX macro {tex_name}: {sorted(parameters)}")
            mathjax_macros[name] = [definition, argument_count]
        else:
            mathjax_macros[name] = definition
    # The corpus writes multi-line display maths as `\[ a &= b \\ &= c \]`, with bare
    # alignment characters and no environment: 831 blocks across 458 cards. The author's
    # own LaTeX pipeline treats `\[...\]` as aligned, but MathJax's is plain display
    # maths, where `&` is illegal -- so those blocks render as "Misplaced &" instead of
    # the mathematics. Wrapping them in `aligned` before typesetting is what the source
    # means, and is done here rather than by editing 458 cards.
    #
    # A block is left alone only when every `&` in it already sits inside an alignment
    # environment, so ENV deletes whole `\begin{env}...\end{env}` spans before the test:
    # a block that says `a &= \begin{cases}...\end{cases} \\ &= b` needs the wrapper for
    # its own alignment characters even though it contains an environment.
    # It runs as a render action rather than once at page load. A `pageReady` hook
    # rewrites the DOM that exists when the page opens, so `generate.html`, which
    # injects a sheet and typesets it on demand, never got the wrapper and its
    # mathematics failed on exactly the blocks that render correctly on their own
    # page. A render action runs on every typeset pass, and at priority 15 it sees
    # the TeX after `find` (10) and before `compile` (20) -- so it edits the source
    # string, with the delimiters already stripped, instead of the rendered element.
    return (
        "<script>\n(function () {\n"
        "  var ENV = /\\\\begin\\{(align|aligned|array|cases|matrix|gather|split|"
        "smallmatrix|pmatrix|bmatrix|vmatrix)(\\*?)\\}[\\s\\S]*?\\\\end\\{\\1\\2\\}/g;\n"
        "  function wrap(math) {\n"
        "    if (!math.display) return;\n"
        "    var t = math.math;\n"
        "    if (t.indexOf('&') < 0 || t.replace(ENV, '').indexOf('&') < 0) return;\n"
        "    math.math = '\\\\begin{aligned}' + t + '\\\\end{aligned}';\n"
        "  }\n"
        "  window.MathJax = {\n"
        "    tex: { macros: " + json.dumps(mathjax_macros) + ", "
        "inlineMath: [['$','$'],['\\\\(','\\\\)']] },\n"
        "    options: { renderActions: { wrapAligned: [15,\n"
        "      function (doc) { for (var m of doc.math) { wrap(m); } },\n"
        "      function (math) { wrap(math); }\n"
        "    ] } }\n"
        "  };\n})();\n</script>\n"
    )


def _link_targets(
    con: sqlite3.Connection,
    guides: list[PublicationManifest],
) -> dict[str, Path]:
    targets: dict[str, Path] = {}

    def add(key: str, target: Path) -> None:
        targets[key] = target
        targets[target.as_posix()] = target

    for card in _rows(con, "select id, kind from cards where kind != 'occurrence'"):
        directory = "exam" if card["kind"] == "source" else "tag"
        add(card["id"], Path(directory) / f"{card['id']}.html")
    for occurrence in _rows(con, "select id, problem_id from occurrences"):
        add(occurrence["id"], Path("tag") / f"{occurrence['problem_id']}.html")
    for guide in guides:
        add(_publication_root_target_key(guide), _publication_root_route(guide))
        for section in guide.sections:
            add(
                _publication_section_target_key(guide, section),
                _publication_section_route(guide, section),
            )
    return targets


def _search_records(
    con: sqlite3.Connection,
    guides: list[PublicationManifest],
    wiki_pages: list[WikiPage] | None = None,
) -> list[dict[str, object]]:
    card_records: list[dict[str, object]] = []
    cards = _rows(
        con,
        """
        select c.id, c.kind, c.title,
          coalesce((select group_concat(term, ' ') from classifications
                    where card_id=c.id), '') as facets,
          coalesce((select group_concat(text, ' ') from sections
                    where card_id=c.id), '') as body
        from cards c
        where c.kind != 'occurrence'
        order by c.id
        """,
    )
    for card in cards:
        directory = "exam" if card["kind"] == "source" else "tag"
        search = " ".join(
            (
                card["id"],
                card["kind"],
                card["title"],
                card["facets"],
                card["body"],
            )
        ).lower()
        card_records.append(
            {
                "title": card["title"],
                "kind": "Problem" if card["kind"] == "problem" else "Card",
                "detail": f"{card['kind']} · {card['id']}",
                "url": f"{directory}/{card['id']}.html",
                "search": search,
            }
        )
    page_records: list[dict[str, object]] = []
    for guide in guides:
        page_records.append(
            {
                "title": guide.title,
                "kind": "Page",
                "detail": "study guide",
                "url": _publication_root_route(guide).as_posix(),
                "search": " ".join([guide.title, guide.lede] + [section.title for section in guide.sections]).lower(),
            }
        )
        page_records.extend(
            {
                "title": section.title,
                "kind": "Page",
                "detail": guide.title,
                "url": _publication_section_route(guide, section).as_posix(),
                "search": (f"{guide.title} {section.title} {section.lede}").lower(),
            }
            for section in guide.sections
        )
    return wiki_search_records(wiki_pages or []) + page_records + card_records


def _wiki_manifest(pages: list[WikiPage]) -> list[dict[str, str]]:
    manifest = [
        {
            "source": page.source_rel.as_posix(),
            "route": page.route.as_posix(),
            "title": page.title,
        }
        for page in pages
    ]
    routes = [entry["route"] for entry in manifest]
    if len(routes) != len(set(routes)):
        raise ValueError("wiki page route collision")
    return manifest


def _generate_data(
    pandoc: PandocServer,
    con: sqlite3.Connection,
) -> list[dict]:
    """Every problem as a selectable exam question: statement HTML + facets.

    The statement is recovered from the card AST (never the flattened section
    text, which loses the math) with a single batched pandoc call rather than one
    per problem, and each problem carries the areas and institutions it is filed
    under so the generator can select the way make-me-a-qual did -- by area.

    The sheet is statements only, so the AST goes through `_statement_only`
    first. `_html_ast` is the tag-page extraction and is wrong here: it hides
    answers behind a disclosure the reader can open, which on a printed practice
    sheet means printing them."""
    problems = _rows(con, "select id, title, ast from cards where kind='problem' order by id")
    areas: dict[str, list[str]] = {problem["id"]: [] for problem in problems}
    for r in _rows(con, "select card_id, term from classifications where axis='area'"):
        if r["card_id"] in areas:
            areas[r["card_id"]].append(r["term"])
    insts: dict[str, set[str]] = {problem["id"]: set() for problem in problems}
    for r in _rows(
        con,
        "select o.problem_id pid, e.institution inst from occurrences o join exam_sources e on e.id=o.source_id",
    ):
        if r["pid"] in insts:
            insts[r["pid"]].add(r["inst"])
    bodies = _successful_html_outputs(
        pandoc.write_html([_statement_ast(problem["ast"]) for problem in problems]),
        "generator statement HTML write",
    )
    out = []
    for r, body in zip(problems, bodies, strict=True):
        stmt = body.strip()
        out.append(
            {
                "id": r["id"],
                "areas": areas[r["id"]],
                "insts": sorted(insts[r["id"]]),
                "q": stmt,
            }
        )
    return out


GENERATE_QMD = """---
title: Generate a practice set
---

```{=html}
<style>
/* Every track and flex item is min-width:0. A grid or flex item defaults to a
   min-content floor, so one wide equation in one problem widened the sheet
   track and pushed the whole page sideways; `mjx-container{max-width:100%}` in
   the site stylesheet then resolved against the widened column and never bit.
   The remaining irreducibly wide block scrolls inside .qb, not on <body>. */
.gen-panel{display:grid;grid-template-columns:minmax(0,260px) minmax(0,1fr);gap:32px;align-items:start;margin-top:8px}
.gen-controls .grp{margin-bottom:18px}
.gen-controls label.h{display:block;font-weight:600;font-size:13px;text-transform:uppercase;letter-spacing:.05em;color:#6c757d;margin-bottom:8px}
.gen-controls .opt{display:block;margin:4px 0}
#gen-n{width:90px;padding:6px 8px}
#gen-go{margin-top:6px;padding:10px 18px;font-weight:600;border:0;border-radius:6px;background:#2780e3;color:#fff;cursor:pointer}
#gen-sheet{min-width:0}
#gen-sheet .q{display:flex;gap:14px;margin:22px 0;page-break-inside:avoid}
#gen-sheet .qn{font-weight:700;color:#2780e3;min-width:26px;flex:0 0 auto}
#gen-sheet .qb{min-width:0;flex:1 1 auto;overflow-x:auto}
#gen-sheet .src{font-size:.85em;color:#6c757d;font-style:italic;margin-top:6px}
#gen-sheet h2{text-align:center;border-bottom:2px solid #333;padding-bottom:10px}
@media (max-width:56rem){.gen-panel{grid-template-columns:minmax(0,1fr)}}
@media print{.gen-controls,.navbar,#quarto-header,.quarto-title-block{display:none!important}.gen-panel{display:block}}
</style>
<div class="gen-panel">
  <form class="gen-controls" onsubmit="return false">
    <div class="grp"><label class="h">Areas</label><div id="gen-areas"></div></div>
    <div class="grp"><label class="h">Institution</label><select id="gen-inst" class="form-select"></select></div>
    <div class="grp"><label class="h">Number of problems</label><input type="number" id="gen-n" value="8" min="1" max="40"></div>
    <div class="grp"><label class="opt"><input type="checkbox" id="gen-src"> Only from a recorded sitting</label></div>
    <button id="gen-go">Generate set</button>
    <button id="gen-print" style="margin-top:6px;background:none;border:1px solid #ccc;border-radius:6px;padding:9px 16px;cursor:pointer">Print / PDF</button>
  </form>
  <div id="gen-sheet">
    <p class="text-muted">Pick criteria and press <b>Generate set</b>.
      A modern take on make-me-a-qual — problems are sampled from the corpus
      and typeset here.</p>
  </div>
</div>
<script>
const AREAS={"algebra":"Algebra","real-analysis":"Real Analysis","complex-analysis":"Complex Analysis","topology":"Topology"};
const QDATA=__GENDATA__;
const insts=[...new Set(QDATA.flatMap(q=>q.insts))].filter(Boolean).sort();
document.getElementById("gen-areas").innerHTML=Object.entries(AREAS)
  .map(([k,v])=>`<label class="opt"><input type="checkbox" class="ga"
    value="${k}"> ${v}</label>`)
  .join("");
document.getElementById("gen-inst").innerHTML='<option value="">Any</option>'+insts.map(i=>`<option value="${i}">${i.toUpperCase()}</option>`).join("");
function sample(a,n){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a.slice(0,n);}
document.getElementById("gen-go").onclick=()=>{
  const areas=[...document.querySelectorAll(".ga:checked")].map(c=>c.value);
  const inst=document.getElementById("gen-inst").value;
  const n=Math.max(1,Math.min(40,+document.getElementById("gen-n").value||8));
  const needSrc=document.getElementById("gen-src").checked;
  let pool=QDATA.filter(q=>q.q.length>10
    &&(!areas.length||q.areas.some(a=>areas.includes(a)))
    &&(!inst||q.insts.includes(inst))
    &&(!needSrc||q.insts.length));
  const pick=sample(pool,n);
  const sheet=document.getElementById("gen-sheet");
  if(!pick.length){sheet.innerHTML='<p class="text-muted">No problems match. Loosen the criteria.</p>';return;}
  const title=(areas.length?areas.map(a=>AREAS[a]).join(", "):"All areas")+(inst?" · "+inst.toUpperCase():"");
  sheet.innerHTML=`<h2>Practice Set</h2><p style="text-align:center" class="text-muted">${pick.length} problems · ${title}</p>`+
    pick.map((q,i)=>`<div class="q">
      <div class="qn">${i+1}.</div>
      <div class="qb">${q.q}
        <div class="src">${q.insts.map(x=>x.toUpperCase()).join(", ")} ·
          <a href="tag/${q.id}.html">${q.id}</a>
        </div>
      </div>
    </div>`).join("");
  if(window.MathJax&&MathJax.typesetPromise)MathJax.typesetPromise([sheet]);
};
document.getElementById("gen-print").onclick=()=>window.print();
</script>
```
"""


def project(
    pandoc: PandocServer,
    db: Path,
    out: Path,
    publications: Path,
    site: Path,
    macros: dict,
    wiki_pages: list[WikiPage] | None = None,
) -> None:
    if out.exists():
        shutil.rmtree(out)
    (out / "tag").mkdir(parents=True)
    (out / "exam").mkdir()
    (out / "guide").mkdir()
    if wiki_pages:
        (out / "wiki").mkdir()
    site_root = out / "_site"
    site_root.mkdir()
    con = sqlite3.connect(db)
    mathjax = mathjax_header(macros)

    (out / "_quarto.yml").write_text(yaml.safe_dump(QUARTO_YML, sort_keys=False))
    (out / "_macros.html").write_text(mathjax)
    for asset in ("styles.css", "app.js", "filters/reveal.lua"):
        shutil.copy(site / asset, out / Path(asset).name)
    for asset in ("styles.css", "app.js"):
        shutil.copy(site / asset, site_root / asset)

    guides = load_publications(publications)
    link_targets = _link_targets(con, guides)
    link_targets.update(wiki_link_targets(wiki_pages or []))
    (out / "wiki-manifest.json").write_text(json.dumps(_wiki_manifest(wiki_pages or []), ensure_ascii=False, indent=2) + "\n")
    appearances = card_appearances(con, guides)
    assets = build_asset_catalog(site.parent / "assets")
    inline_values = [row["title"] for row in _rows(con, "select distinct title from cards")]
    inline_values.extend(
        [
            "problems, in the order they appeared.",
            ("Assembled from a publication manifest: an ordered list of stable IDs and queries. Reordering it touches no card and no catalog row."),
            "Every problem in the corpus. Filter by any facet; the URL is the query.",
            "Historical sittings, each a fixed ordered list of occurrences.",
            "More from the catalog",
        ]
    )
    inline_values.extend(guide.title for guide in guides)
    inline_values.extend(guide.lede for guide in guides)
    inline_values.extend(value for guide in guides for section in guide.sections for value in (section.title, section.lede))
    inline_cache = build_inline_cache(pandoc, inline_values)

    jcache, api = load_json(con)
    tag_pages: list[tuple[Path, dict, list]] = []
    for card in _rows(con, "select * from cards where kind='problem'"):
        meta, body = problem_json(con, card, jcache, appearances)
        tag_pages.append((out / "tag" / f"{card['id']}.qmd", meta, body))
    for card in _rows(con, "select * from cards where kind not in ('problem','source','occurrence')"):
        meta, body = plain_json(con, card, jcache, appearances)
        tag_pages.append((out / "tag" / f"{card['id']}.qmd", meta, body))
    write_json_pages(
        pandoc,
        tag_pages,
        api,
        site_root,
        mathjax,
        link_targets,
        assets,
    )

    pages: list[PageItem] = []
    for src in _rows(con, "select * from cards where kind='source'"):
        pages.append(
            (
                source_page(con, src, inline_cache),
                out / "exam" / f"{src['id']}.qmd",
                StandardPage(),
            )
        )

    generator_data = json.dumps(
        _generate_data(pandoc, con),
        separators=(",", ":"),
    )
    for unsafe, escaped in (("&", "\\u0026"), ("<", "\\u003c"), (">", "\\u003e")):
        generator_data = generator_data.replace(unsafe, escaped)
    generate_qmd = GENERATE_QMD.replace("__GENDATA__", generator_data)
    (out / "generate.qmd").write_text(generate_qmd)
    generate_html = generate_qmd.split("```{=html}\n", 1)[1].rsplit("\n```", 1)[0]
    write_page(
        site_root,
        Path("generate.html"),
        {"title": "Generate a practice set"},
        generate_html,
        mathjax,
        link_targets,
        assets,
        StandardPage(),
    )

    for guide in guides:
        pages.append(
            (
                publication_root_page(guide, inline_cache),
                out / "guide" / f"{guide.id}.qmd",
                SubjectPage(_publication_navigation(guide, guide.id)),
            )
        )
        pages.extend(
            (
                publication_section_page(
                    con,
                    guide,
                    section,
                    inline_cache,
                ),
                out / "guide" / guide.id / f"{section.slug}.qmd",
                SubjectPage(_publication_navigation(guide, section.slug)),
            )
            for section in guide.sections
        )

    pages.append(
        (
            problem_browser_page(con, inline_cache),
            out / "problems.qmd",
            StandardPage(),
        ),
    )
    pages.append(
        (
            link_list_page(
                con,
                "Exams",
                "Historical sittings, each a fixed ordered list of occurrences.",
                _rows(
                    con,
                    "select c.* from cards c join sources s on s.id=c.id join exam_sources e on e.id=s.id order by e.institution, s.year, c.id",
                ),
                "exam/",
                inline_cache,
            ),
            out / "exams.qmd",
            StandardPage(),
        ),
    )
    pages.append(
        (
            (
                {"title": "Guides"},
                [
                    pf.BulletList(
                        *[
                            pf.ListItem(
                                pf.Plain(
                                    pf.Link(
                                        pf.Str(guide.title),
                                        url=f"guide/{guide.id}.html",
                                    )
                                )
                            )
                            for guide in guides
                        ]
                    )
                ],
            ),
            out / "guides.qmd",
            StandardPage(),
        ),
    )
    pages.append((index_page(pandoc, con), out / "index.qmd", StandardPage()))
    write_pages(
        pandoc,
        pages,
        site_root,
        mathjax,
        link_targets,
        assets,
    )
    if wiki_pages:
        wiki_navigation = _wiki_navigation(wiki_pages)
        wiki_items: list[PageItem] = [
            (
                (
                    {"title": page.title, "subtitle": page.source_rel.as_posix()},
                    _wiki_blocks(page),
                ),
                out / "wiki" / page.source_rel.with_suffix(".qmd"),
                _wiki_chrome(wiki_navigation, page),
            )
            for page in wiki_pages
        ]
        for offset in range(0, len(wiki_items), WIKI_BATCH_SIZE):
            write_pages(
                pandoc,
                wiki_items[offset : offset + WIKI_BATCH_SIZE],
                site_root,
                mathjax,
                link_targets,
                assets,
            )
    write_search_index(site_root, _search_records(con, guides, wiki_pages))
    con.close()
