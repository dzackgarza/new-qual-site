"""Corpus pages, emitted as QMD and HTML.

Pages are composed as Pandoc ASTs and batch-written as both QMD and HTML.
Nothing here assembles either format by hand, so fencing, escaping, and
math remain the writer's problem rather than a source of quoting bugs.

Emitted documents carry only semantics: a card's blocks keep the classes their
author wrote (`.problem`, `.solution`, `.hint`), plus attributes drawn from the
catalog. The direct HTML output owns the shared shell and presentation;
generated QMD remains available as an inspectable secondary artifact.
"""

from __future__ import annotations

import copy
import html
import json
import os
import re
import shutil
import sqlite3
import subprocess
from collections import Counter
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import cast

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
    MiddleReading,
    NavigationLink,
    NavigationParent,
    NodeParent,
    OnlyReading,
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
    incoming_wiki_links,
    wiki_card_mentions,
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

# The class carrying the label. `reveal.lua` replaces the hint and solution
# divs outright, so those never reach this rule.
SECTION_CLASS = "qual-section"


def _owned_class(class_name: str) -> str:
    if class_name in OWNED:
        return OWNED[class_name]
    return class_name


# A `title=` on a hint or solution would land inside the `<details>`
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
    opening = f'<details class="reveal {reveal_class}"><summary>{html.escape(summary)}</summary>'
    return [
        pf.RawBlock(opening, format="html"),
        *element.content,
        pf.RawBlock("</details>", format="html"),
    ]


_TIKZCD_FILTER = Path.home() / ".pandoc" / "filters" / "tikzcd.lua"
_TIKZCD_START = "\\begin{tikzcd}"


def _compile_tikzcd_block(tex_source: str) -> str:
    """Compile a single tikz/tikzcd block to an inline-SVG HTML fragment.

    Uses the canonical pandoc lua filter at ``~/.pandoc/filters/tikzcd.lua``,
    which compiles via ``pdflatex`` + ``pdf2svg`` and caches by SHA1 of the
    source + template.  On a warm cache the only cost is pandoc startup.
    """
    result = subprocess.run(
        [
            "pandoc",
            "--from",
            "markdown",
            "--to",
            "html",
            "--lua-filter",
            str(_TIKZCD_FILTER),
        ],
        input=tex_source,
        capture_output=True,
        text=True,
        timeout=120,
        env={**os.environ, "HOME": str(Path.home())},
    )
    if result.returncode != 0:
        raise RuntimeError(f"tikzcd compilation failed (exit {result.returncode}): {result.stderr.strip()[:300]}")
    return result.stdout


def _compile_tikzcd(
    element: pf.Element,
    document: pf.Doc,
) -> pf.Element | list[pf.Block] | None:
    """Replace ``RawBlock("tex", tikzcd)`` with ``RawBlock("html", svg)``.

    The pandoc server cannot run lua filters (PandocPure monad), so tikzcd
    blocks are dropped silently during the server's HTML write.  This walk
    pre-compiles them via the CLI filter so the SVG survives as a raw HTML
    block that the server passes through verbatim.
    """
    del document
    if not isinstance(element, pf.RawBlock):
        return None
    # panflute's RawBlock exposes .format and .text at runtime, but the type
    # stubs do not declare them.  Use getattr to satisfy mypy without weakening
    # the runtime check — the isinstance guard ensures the object is a RawBlock.
    fmt = cast(str, getattr(element, "format", ""))
    if fmt not in ("tex", "latex"):
        return None
    text = cast(str, getattr(element, "text", ""))
    if _TIKZCD_START not in text:
        return None
    svg_html = _compile_tikzcd_block(text)
    return pf.RawBlock(svg_html, format="html")


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


def _wiki_node(page: WikiPage) -> tuple[str, NavigationParent]:
    parts = page.source_rel.parts
    if page.source_rel.stem.lower() == "index" and len(parts) > 1:
        parent_parts = parts[:-2]
        parent: NavigationParent = RootParent() if not parent_parts else NodeParent("/".join(parent_parts))
        return "/".join(parts[:-1]), parent
    parent_parts = parts[:-1]
    parent = RootParent() if not parent_parts else NodeParent("/".join(parent_parts))
    return page.route.as_posix(), parent


def _wiki_parent_key(link: NavigationLink) -> str:
    match link.parent:
        case RootParent():
            return ""
        case NodeParent(key=key):
            return key


def _wiki_reading_members(
    ordered: tuple[NavigationLink, ...],
    pages_by_key: dict[str, WikiPage],
) -> dict[str, list[WikiPage]]:
    children: dict[str, list[NavigationLink]] = {link.key: [] for link in ordered}
    roots: list[NavigationLink] = []
    for link in ordered:
        match link.parent:
            case RootParent():
                roots.append(link)
            case NodeParent(key=parent_key):
                children[parent_key].append(link)
    members: dict[str, list[WikiPage]] = {}

    def walk(nodes: list[NavigationLink]) -> None:
        for link in nodes:
            page = pages_by_key[link.key]
            members.setdefault(_wiki_branch(page), []).append(page)
            walk(children[link.key])

    walk(roots)
    return members


def _wiki_navigation(pages: list[WikiPage]) -> dict[str, PublicationNavigation]:
    """The full wiki tree, breadcrumbs, and branch reading order, by route.

    A page's trail is the directory path it is filed under. Labels and sibling
    order come from that page's `title` and `order`. A directory is in the tree
    only through its `index.md`, which is that directory: the folder title,
    order, and route come from the page, and the page is not listed again among
    the children. Reading order is depth-first over that same ordered tree,
    within the top-level branch.
    """
    links: dict[str, NavigationLink] = {}
    page_keys: dict[str, str] = {}
    pages_by_key: dict[str, WikiPage] = {}
    for page in pages:
        key, parent = _wiki_node(page)
        links[key] = NavigationLink(
            key=key,
            title=page.title,
            target=PageTarget(page.route),
            parent=parent,
        )
        page_keys[page.route.as_posix()] = key
        pages_by_key[key] = page

    ordered = tuple(
        sorted(
            links.values(),
            key=lambda link: (
                _wiki_parent_key(link),
                pages_by_key[link.key].order,
                link.title,
                link.key,
            ),
        )
    )
    navigation: dict[str, PublicationNavigation] = {}
    for members in _wiki_reading_members(ordered, pages_by_key).values():
        for index, page in enumerate(members):
            previous = members[index - 1] if index else None
            following = members[index + 1] if index + 1 < len(members) else None
            position: StartReading | MiddleReading | EndReading | OnlyReading
            if previous is None and following is not None:
                position = StartReading(following=ReadingLink.of(links[page_keys[following.route.as_posix()]]))
            elif following is None and previous is not None:
                position = EndReading(previous=ReadingLink.of(links[page_keys[previous.route.as_posix()]]))
            elif previous is not None and following is not None:
                position = MiddleReading(
                    previous=ReadingLink.of(links[page_keys[previous.route.as_posix()]]),
                    following=ReadingLink.of(links[page_keys[following.route.as_posix()]]),
                )
            else:
                position = OnlyReading()
            route_key = page.route.as_posix()
            navigation[route_key] = PublicationNavigation(
                links=ordered,
                current_key=page_keys[route_key],
                position=position,
            )
    return navigation


def _wiki_chrome(
    navigation: dict[str, PublicationNavigation],
    page: WikiPage,
) -> PageChrome:
    found = navigation.get(page.route.as_posix())
    return AuthoredPage(found) if found else StandardPage()


def _wiki_incoming_html(sources: list[WikiPage]) -> str:
    if not sources:
        return ""
    items = "".join(f'<li><a href="{html.escape(page.route.as_posix(), quote=True)}">{html.escape(page.title)}</a></li>' for page in sources)
    return f'<section class="relation-group" data-relation-group="wiki-backlinks"><h2>What links to this</h2><ul>{items}</ul></section>'


def _wiki_blocks(page: WikiPage, incoming: list[WikiPage]) -> list[pf.Block]:
    """An authored wiki page gets the same section labelling a card gets.

    Only the card path ran `_rename`, so every `:::{.remark}`, `:::{.proof}`
    and `:::{.fact}` on the wiki reached the reader as unmarked prose: the
    label rule in `styles.css` keys on the `qual-section` class this adds.
    Incoming wikilinks are inverted from the resolved graph, not authored.
    """
    blocks = list(pf.Doc(*page.blocks).walk(_rename).content)
    html_block = _wiki_incoming_html(incoming)
    if html_block:
        blocks.append(pf.RawBlock(html_block, format="html"))
    return blocks


# --- raw-JSON tag-page path -------------------------------------------------
#
# The 3,200 tag pages are the bulk of the build. Composing them through panflute
# means one pandoc process per card to load and one per page to write -- an hour.
# Their bodies are only a card's own blocks plus, for a problem, any solution
# or hint. No `uses` link, no title parsing: every piece is already pandoc JSON
# in the catalog. These pages are assembled as JSON and written in bounded
# batches through one persistent Pandoc server. The other pages use the same
# writer boundary after Panflute composition.


@dataclass(frozen=True)
class Appearance:
    target_key: str
    title: str


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
    return "<ul>" + "".join(f'<li><a href="{html.escape(appearance.target_key, quote=True)}">{html.escape(appearance.title)}</a></li>' for appearance in appearances) + "</ul>"


def _relation_groups_json(
    con: sqlite3.Connection,
    card_id: str,
    appearances: dict[str, list[Appearance]],
    wiki_mentions: list[WikiPage],
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
        where r.target_id=?
        order by r.kind, c.title, c.id
        """,
        (card_id,),
    )
    source = (
        '<div class="relation-groups" aria-label="Card relationships">'
        '<section class="relation-group" data-relation-group="dependencies">'
        "<h2>Dependencies</h2>"
        f"{_card_relation_items(dependencies)}"
        "</section>"
        '<section class="relation-group" data-relation-group="appearances">'
        "<h2>Appearances</h2>"
        f"{_appearance_items(appearances[card_id])}"
        "</section>"
        '<section class="relation-group" data-relation-group="backlinks">'
        "<h2>Backlinks</h2>"
        f"{_card_relation_items(backlinks)}"
        "</section>"
        f"{_wiki_incoming_html(wiki_mentions)}"
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
    wiki_mentions: dict[str, list[WikiPage]],
) -> tuple[dict, list]:
    facets = _rows(
        con,
        """
        select distinct e.institution, s.year
        from collection_problems cp
        join sources s on s.id=cp.collection_id
        left join exam_sources e on e.id=s.id
        where cp.problem_id=?
        """,
        (card["id"],),
    )
    institutions = sorted({f["institution"].upper() for f in facets if f["institution"]})
    years = sorted({str(f["year"]) for f in facets if f["year"] is not None})
    areas = _terms(con, card["id"], "area")
    topics = _terms(con, card["id"], "topic")

    body = _dup(jcache[card["id"]])
    _rename_json(body)
    for kind in ("hints-at", "solves"):
        for rel in _related(con, card["id"], kind):
            rb = _dup(jcache[rel["id"]])
            _rename_json(rb)
            body += rb
    body.append(_relation_groups_json(con, card["id"], appearances, wiki_mentions.get(card["id"], [])))
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
    wiki_mentions: dict[str, list[WikiPage]],
) -> tuple[dict, list]:
    body = _dup(jcache[card["id"]])
    _rename_json(body)
    body.append(_relation_groups_json(con, card["id"], appearances, wiki_mentions.get(card["id"], [])))
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


INLINE_SENTINEL = "QUALINLINEBOUNDARY"


def build_inline_cache(
    pandoc: PandocServer,
    markdown_values: list[str],
) -> dict[str, list[pf.Inline]]:
    sources = list(dict.fromkeys(markdown_values))
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
    source = markdown
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
    doc = from_ast(ast)
    doc = doc.walk(_compile_tikzcd)
    doc = doc.walk(_reveal)
    return to_json(doc)


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
    # Institution facets come from exam collections that list this problem. A
    # problem cited from a textbook contributes a year but no institution.
    facets = _rows(
        con,
        """
        select distinct e.institution, s.year
        from collection_problems cp
        join sources s on s.id=cp.collection_id
        left join exam_sources e on e.id=s.id
        where cp.problem_id=?
        """,
        (card["id"],),
    )
    institutions = sorted({f["institution"].upper() for f in facets if f["institution"]})
    years = sorted({str(f["year"]) for f in facets if f["year"] is not None})
    areas = _terms(con, card["id"], "area")
    topics = _terms(con, card["id"], "topic")

    blocks = _blocks(card)

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


def collection_page(
    con: sqlite3.Connection,
    src: sqlite3.Row,
    inline_cache: dict[str, list[pf.Inline]],
) -> Page:
    listed = _rows(
        con,
        """
        select section_ordinal, section_name, ordinal, problem_id
        from collection_problems
        where collection_id=?
        order by coalesce(section_ordinal, -1), ordinal
        """,
        (src["id"],),
    )
    completion_rows = _rows(con, "select completion from sources where id=?", (src["id"],))
    completion = completion_rows[0]["completion"] if completion_rows else "complete"
    provenance = [
        row["href"]
        for row in _rows(
            con,
            "select href from collection_provenance where collection_id=? order by ordinal",
            (src["id"],),
        )
    ]
    return {"title": src["title"], "subtitle": src["id"]}, _collection_listing(con, listed, inline_cache, completion, provenance)


def _collection_listing(
    con: sqlite3.Connection,
    listed: list[sqlite3.Row],
    inline_cache: dict[str, list[pf.Inline]],
    completion: str = "complete",
    provenance: list[str] | None = None,
) -> list[pf.Block]:
    """The collection card's `problems:` / `sections:` list is the page body.

    Position is the list index. An empty list is an unfilled collection, not a
    cue to invent contents from somewhere else.
    """

    def card_item(problem_id: str) -> pf.ListItem:
        matches = _rows(con, "select * from cards where id=?", (problem_id,))
        if matches:
            return pf.ListItem(_link(matches[0], inline_cache))
        return pf.ListItem(pf.Plain(pf.Code(problem_id)))

    blocks: list[pf.Block] = []
    if completion == "incomplete":
        blocks.append(pf.Para(pf.Str("This collection is incomplete; listed items are a prefix of the source, and further extraction is pending.")))
    if provenance:
        blocks.append(pf.Header(pf.Str("Provenance"), level=2))
        blocks.append(pf.BulletList(*[pf.ListItem(pf.Plain(pf.Link(pf.Str(href), url=href))) for href in provenance]))
    blocks.append(
        pf.Para(
            pf.Str(str(len(listed))),
            pf.Space(),
            *_inlines("problems.", inline_cache),
        )
    )
    if not listed:
        return blocks

    by_section: list[tuple[str | None, list[str]]] = []
    for row in listed:
        name = row["section_name"]
        if not by_section or by_section[-1][0] != name:
            by_section.append((name, []))
        by_section[-1][1].append(row["problem_id"])

    for name, pids in by_section:
        if name:
            blocks.append(pf.Header(*_inlines(name, inline_cache), level=2))
        blocks.append(
            pf.Div(
                pf.OrderedList(
                    *[card_item(pid) for pid in pids],
                    start=1,
                    style="Decimal",
                    delimiter="Period",
                ),
                classes=["qual-exam-listing"],
            )
        )
    return blocks


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


def _plural(kind: str) -> str:
    return f"{kind[:-1]}ies" if kind.endswith("y") else f"{kind}s"


def _query_heading(query: PublicationQuery) -> str:
    """What a query panel holds, said in the author's own words.

    Every panel used to be headed `More from the catalog`, so a section with
    ten of them offered ten indistinguishable headings and nothing under them
    was addressable. The kind and the topics are already written in the
    manifest, so the heading restates the query rather than inventing a title.
    """
    topics = ", ".join(query.topics)
    return f"{_plural(query.kind).title()}: {topics}" if topics else _plural(query.kind).title()


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
                            *_inlines(_query_heading(query), inline_cache),
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
    """Where each card shows up: guide sections, and for a problem, the
    collections that list it.

    The listing edge is the reverse of the collection page: a problem is on an
    exam exactly when that exam's `problems:` (or a textbook section) names it.
    Position is the list index."""
    appearances: dict[str, list[Appearance]] = {row["id"]: [] for row in _rows(con, "select id from cards order by id")}
    for row in _rows(
        con,
        """
        select cp.problem_id, cp.collection_id, cp.ordinal, c.title
        from collection_problems cp
        join cards c on c.id=cp.collection_id
        order by c.title, coalesce(cp.section_ordinal, -1), cp.ordinal
        """,
    ):
        appearances[row["problem_id"]].append(
            Appearance(
                target_key=row["collection_id"],
                title=f"{row['title']}, problem {row['ordinal'] + 1}",
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
        "problem": "Problems",
        "collection": "Collections",
    }

    def plural(kind: str) -> str:
        stem = kind.title()
        return labels.get(kind) or (f"{stem[:-1]}ies" if stem.endswith("y") else f"{stem}s")

    body = "\n".join(f"| {plural(kind)} | {n} |" for kind, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))
    output = _successful_outputs(
        pandoc.read_markdown(
            ["| Cards | Count |\n|---|---|\n" + body + "\n\nStart with [the problem browser](problems.html), a [past exam](exams.html), or a [study guide](guides.html).\n"],
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


# Separates multi-valued facet terms in HTML data attributes. Topics are free
# strings and may contain spaces, so space is not a usable delimiter.
FACET_SEP = "|"


def _facet_terms(joined: str | None) -> list[str]:
    return [term for term in (joined or "").split(FACET_SEP) if term]


def _facet_option_label(axis: str, value: str) -> str:
    # Topics are authored display strings. Areas/institutions remain registry ids.
    if axis in {"topic", "year"}:
        return value
    return value.replace("-", " ").title()


def problem_browser_page(
    con: sqlite3.Connection,
    inline_cache: dict[str, list[pf.Inline]],
) -> Page:
    facet_values = {
        "area": sorted({row["term"] for row in _rows(con, "select term from classifications where axis='area'")}),
        "topic": sorted({row["term"] for row in _rows(con, "select term from classifications where axis='topic'")}),
        "institution": sorted({row["institution"].upper() for row in _rows(con, "select institution from exam_sources")}),
        "year": sorted({str(row["year"]) for row in _rows(con, "select year from sources where year is not null")}),
    }
    problems = _rows(
        con,
        f"""
        select c.*,
          (select group_concat(term, '{FACET_SEP}') from classifications
           where card_id=c.id and axis='area') as areas,
          (select group_concat(term, '{FACET_SEP}') from classifications
           where card_id=c.id and axis='topic') as topics,
          (select group_concat(institution, '{FACET_SEP}') from (
             select distinct upper(e.institution) as institution
             from collection_problems cp join exam_sources e on e.id=cp.collection_id
             where cp.problem_id=c.id
           )) as institutions,
          (select group_concat(year, '{FACET_SEP}') from (
             select distinct s.year as year
             from collection_problems cp join sources s on s.id=cp.collection_id
             where cp.problem_id=c.id and s.year is not null
           )) as years
        from cards c
        where c.kind='problem'
        order by c.title, c.id
        """,
    )
    sources_by_problem: dict[str, list[sqlite3.Row]] = {}
    for source in _rows(
        con,
        """
        select distinct cp.problem_id, cp.collection_id as source_id, s.title
        from collection_problems cp join cards s on s.id=cp.collection_id
        order by s.title
        """,
    ):
        sources_by_problem.setdefault(source["problem_id"], []).append(source)
    rows: list[pf.Block] = []
    for problem in problems:
        area_terms = _facet_terms(problem["areas"])
        topic_terms = _facet_terms(problem["topics"])
        institution_terms = _facet_terms(problem["institutions"])
        year_terms = _facet_terms(problem["years"])
        facet_text = " · ".join(
            part
            for part in (
                ", ".join(_facet_option_label("area", a) for a in area_terms),
                ", ".join(institution_terms),
                ", ".join(year_terms),
            )
            if part
        )
        source_rows = sources_by_problem.get(problem["id"], [])
        source_links: list[pf.Inline] = []
        for index, source in enumerate(source_rows):
            if index:
                source_links.append(pf.Str(","))
                source_links.append(pf.Space())
            source_links.append(
                pf.Link(
                    *_inlines(source["title"], inline_cache),
                    url=f"exam/{source['source_id']}.html",
                )
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
                pf.Plain(pf.Str(facet_text or "Unclassified")),
                pf.Plain(pf.Str("Sources: "), *source_links) if source_links else pf.Plain(pf.Str("Sources: none")),
                classes=["problem-row"],
                attributes={
                    "data-search": search,
                    "data-area": FACET_SEP.join(area_terms),
                    "data-topic": FACET_SEP.join(topic_terms),
                    "data-institution": FACET_SEP.join(institution_terms),
                    "data-year": FACET_SEP.join(year_terms),
                },
            )
        )
    return {"title": "Problems"}, [
        pf.Para(
            *_inlines(
                "Every problem in the corpus.",
                inline_cache,
            )
        ),
        pf.RawBlock(
            '<div class="problem-filters">'
            '<label for="problem-filter">Search</label>'
            '<input id="problem-filter" type="search" placeholder="Group theory, UGA, 2019…">'
            + "".join(
                f'<label for="problem-{axis}">{axis.title()}</label>'
                f'<select id="problem-{axis}" multiple size="5" data-problem-facet="{axis}">'
                + "".join(f'<option value="{html.escape(value, quote=True)}">{html.escape(_facet_option_label(axis, value))}</option>' for value in values)
                + "</select>"
                for axis, values in facet_values.items()
            )
            + '<output id="problem-count" aria-live="polite"></output></div>',
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


class SearchRecordKind(Enum):
    """The search index's record vocabulary: the value is the JSON wire string."""

    CARD = "Card"
    PAGE = "Page"
    PROBLEM = "Problem"


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

    for card in _rows(con, "select id, kind from cards"):
        directory = "exam" if card["kind"] == "collection" else "tag"
        add(card["id"], Path(directory) / f"{card['id']}.html")
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
        order by c.id
        """,
    )
    for card in cards:
        directory = "exam" if card["kind"] == "collection" else "tag"
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
                "kind": (SearchRecordKind.PROBLEM if card["kind"] == "problem" else SearchRecordKind.CARD).value,
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
                "kind": SearchRecordKind.PAGE.value,
                "detail": "study guide",
                "url": _publication_root_route(guide).as_posix(),
                "search": " ".join([guide.title, guide.lede] + [section.title for section in guide.sections]).lower(),
            }
        )
        page_records.extend(
            {
                "title": section.title,
                "kind": SearchRecordKind.PAGE.value,
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
    topics: dict[str, list[str]] = {problem["id"]: [] for problem in problems}
    for r in _rows(con, "select card_id, term from classifications where axis='topic'"):
        if r["card_id"] in topics:
            topics[r["card_id"]].append(r["term"])
    insts: dict[str, set[str]] = {problem["id"]: set() for problem in problems}
    years: dict[str, set[str]] = {problem["id"]: set() for problem in problems}
    sources: dict[str, dict[str, str]] = {problem["id"]: {} for problem in problems}
    for r in _rows(
        con,
        """
        select cp.problem_id pid, e.institution inst, s.year, cp.collection_id as source_id, c.title source_title
        from collection_problems cp
        join sources s on s.id=cp.collection_id
        join cards c on c.id=cp.collection_id
        left join exam_sources e on e.id=cp.collection_id
        """,
    ):
        if r["pid"] in insts:
            if r["inst"]:
                insts[r["pid"]].add(r["inst"])
            if r["year"] is not None:
                years[r["pid"]].add(str(r["year"]))
            sources[r["pid"]][r["source_id"]] = r["source_title"]
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
                "topics": topics[r["id"]],
                "insts": sorted(insts[r["id"]]),
                "years": sorted(years[r["id"]]),
                "sources": [{"id": source_id, "title": title} for source_id, title in sorted(sources[r["id"]].items())],
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
    <div class="grp"><label class="h">Topic</label><select id="gen-topic" class="form-select"></select></div>
    <div class="grp"><label class="h">Year</label><select id="gen-year" class="form-select"></select></div>
    <div class="grp"><label class="h">Number of problems</label><input type="number" id="gen-n" value="8" min="1" max="40"></div>
    <div class="grp"><label class="opt"><input type="checkbox" id="gen-src"> Only from a recorded exam</label></div>
    <button id="gen-go">Generate set</button>
    <button id="gen-print" style="margin-top:6px;background:none;border:1px solid #ccc;border-radius:6px;padding:9px 16px;cursor:pointer">Print / PDF</button>
  </form>
  <div id="gen-sheet">
    <p class="text-muted">Pick criteria and press <b>Generate set</b>.
      Problems are sampled from the corpus
      and typeset here.</p>
  </div>
</div>
<script>
const QDATA=__GENDATA__;
const insts=[...new Set(QDATA.flatMap(q=>q.insts))].filter(Boolean).sort();
const escapeHtml=(value)=>String(value).replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll(">","&gt;").replaceAll('"',"&quot;");
const label=(value)=>value.replaceAll("-"," ").replace(/\\b\\w/g,(letter)=>letter.toUpperCase());
const AREAS=Object.fromEntries([...new Set(QDATA.flatMap(q=>q.areas))].map((area)=>[area,label(area)]));
const topics=[...new Set(QDATA.flatMap(q=>q.topics))].filter(Boolean).sort();
const years=[...new Set(QDATA.flatMap(q=>q.years))].filter(Boolean).sort((a,b)=>Number(b)-Number(a));
document.getElementById("gen-areas").innerHTML=Object.entries(AREAS)
  .map(([k,v])=>`<label class="opt"><input type="checkbox" class="ga"
    value="${escapeHtml(k)}"> ${escapeHtml(v)}</label>`)
  .join("");
document.getElementById("gen-inst").innerHTML='<option value="">Any</option>'+insts.map(i=>`<option value="${escapeHtml(i)}">${escapeHtml(i.toUpperCase())}</option>`).join("");
document.getElementById("gen-topic").innerHTML='<option value="">Any</option>'+topics.map(t=>`<option value="${escapeHtml(t)}">${escapeHtml(t)}</option>`).join("");
document.getElementById("gen-year").innerHTML='<option value="">Any</option>'+years.map(y=>`<option value="${escapeHtml(y)}">${escapeHtml(y)}</option>`).join("");
function sample(a,n){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a.slice(0,n);}
document.getElementById("gen-go").onclick=()=>{
  const areas=[...document.querySelectorAll(".ga:checked")].map(c=>c.value);
  const inst=document.getElementById("gen-inst").value;
  const topic=document.getElementById("gen-topic").value;
  const year=document.getElementById("gen-year").value;
  const n=Math.max(1,Math.min(40,+document.getElementById("gen-n").value||8));
  const needSrc=document.getElementById("gen-src").checked;
  let pool=QDATA.filter(q=>q.q.length>10
    &&(!areas.length||q.areas.some(a=>areas.includes(a)))
    &&(!inst||q.insts.includes(inst))
    &&(!topic||q.topics.includes(topic))
    &&(!year||q.years.includes(year))
    &&(!needSrc||q.sources.length));
  const pick=sample(pool,n);
  const sheet=document.getElementById("gen-sheet");
  if(!pick.length){sheet.innerHTML='<p class="text-muted">No problems match. Loosen the criteria.</p>';return;}
  const title=(areas.length?areas.map(a=>AREAS[a]).join(", "):"All areas")+(inst?" · "+inst.toUpperCase():"")+(topic?" · "+topic:"")+(year?" · "+year:"");
  sheet.innerHTML=`<h2>Practice Set</h2><p style="text-align:center" class="text-muted">${pick.length} problems · ${title}</p>`+
    pick.map((q,i)=>`<div class="q">
      <div class="qn">${i+1}.</div>
      <div class="qb">${q.q}
        <div class="src">${q.sources.length?q.sources.map(s=>`<a href="exam/${s.id}.html">${s.title}</a>`).join(", "):"No recorded exam"} ·
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
    mentions = wiki_card_mentions(wiki_pages or [])
    incoming_pages = incoming_wiki_links(wiki_pages or [])
    assets = build_asset_catalog(site.parent / "assets")
    inline_values = [row["title"] for row in _rows(con, "select distinct title from cards")]
    inline_values.extend(
        [
            "problems.",
            ("Assembled from a publication manifest: an ordered list of stable IDs and queries. Reordering it touches no card and no catalog row."),
            "Every problem in the corpus.",
            "Past exams.",
        ]
    )
    inline_values.extend(_query_heading(item.query) for guide in guides for section in guide.sections for item in section.items if isinstance(item, QueryItem))
    inline_values.extend(guide.title for guide in guides)
    inline_values.extend(guide.lede for guide in guides)
    inline_values.extend(value for guide in guides for section in guide.sections for value in (section.title, section.lede))
    inline_values.extend(
        row["section_name"]
        for row in _rows(
            con,
            "select distinct section_name from collection_problems where section_name is not null",
        )
    )
    inline_cache = build_inline_cache(pandoc, inline_values)

    jcache, api = load_json(con)
    tag_pages: list[tuple[Path, dict, list]] = []
    for card in _rows(con, "select * from cards where kind='problem'"):
        meta, body = problem_json(con, card, jcache, appearances, mentions)
        tag_pages.append((out / "tag" / f"{card['id']}.qmd", meta, body))
    for card in _rows(con, "select * from cards where kind not in ('problem','collection')"):
        meta, body = plain_json(con, card, jcache, appearances, mentions)
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
    for src in _rows(con, "select * from cards where kind='collection'"):
        pages.append(
            (
                collection_page(con, src, inline_cache),
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
                "Past exams.",
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
                    _wiki_blocks(page, incoming_pages[page.route.as_posix()]),
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
