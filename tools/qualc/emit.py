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
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import cast
from urllib.parse import urlsplit

import panflute as pf
import yaml

from .model import DIV_CLASS_TO_KIND, MARKDOWN, TERMS_IN_YEAR_ORDER, from_ast, to_json
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
    Crumb,
    EndReading,
    LevelOnly,
    MiddleReading,
    NavigationLink,
    NavigationParent,
    NodeParent,
    NotFoundPage,
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
    SITE_PAGES,
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


# A `title=` on a hint or solution is written into the summary by `_reveal`
# rather than into the body, so it does not land below the label inside the
# `<details>`.
TITLED_KINDS = set(DIV_CLASS_TO_KIND.values()) - {"hint", "solution"}


def _title_html(title: str) -> str:
    """The authored `title=` as a qualifier on the block's own label.

    It is not a heading and not the block's name: it says which part or which
    case this block treats, so a reader can open the proof of (b) without
    reading the proof of (a). That makes `Proof 3 (of b)` one heading line; set
    as a bold line under the label it read as the proof's first sentence.

    It goes in the body and not in a CSS `content: attr(...)` because the titles
    carry mathematics -- `$\\implies$`, `$J(R) = \\mathfrak N(R)$` -- and
    `attr()` would print that as its source. In the body MathJax typesets it
    like any other `$...$` on the page.
    """
    return f'<p class="qual-section-qualifier">({html.escape(title)})</p>'


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
    # A card with two solutions showed two disclosures both reading "Solution",
    # and what told them apart -- "Using Morera" beside "Using limit definition"
    # -- was dropped. The authored label names the closed block, which is the
    # only place a reader can act on it: it is the one thing visible before the
    # solution is opened.
    summary = REVEAL_LABELS[reveal_class]
    label = element.attributes.get("title", "").strip()
    if label:
        summary = f"{summary}: {label}"
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


def _figure(
    element: pf.Element,
    document: pf.Doc,
) -> pf.Element | list[pf.Block] | None:
    """A paragraph that is only an image is a figure, so give it the element.

    Pandoc's `implicit_figures` already does this for `![caption](src)`, which
    is why 179 figures reach the page; it cannot for `![](src)`, because there
    is no caption to put in one. Those arrived as a bare `<img>` inside a
    paragraph, with nothing to bound a tall image and nothing for a caption
    under a grid of them to align to.

    The image stays an AST node rather than becoming raw HTML, so `src`
    rewriting and asset linking still see it -- the same shape `_reveal` uses
    for its `<details>`.
    """
    del document
    if isinstance(element, pf.Figure):
        # Pandoc's own figures carry the class too, so the 280 it makes and the
        # 401 made here are one thing to style, captions included.
        if "qual-figure" not in element.classes:
            element.classes.append("qual-figure")
        return element
    if not isinstance(element, pf.Para) or len(element.content) != 1:
        return None
    image = element.content[0]
    if not isinstance(image, pf.Image):
        return None
    return [
        pf.RawBlock('<figure class="qual-figure">', format="html"),
        pf.Plain(image),
        pf.RawBlock("</figure>", format="html"),
    ]


def _sidenote(
    element: pf.Element,
    document: pf.Doc,
) -> pf.Element | list[pf.Inline] | None:
    """A footnote as a sidenote, in the margin beside the line that raises it.

    Every note in the corpus is a technique aside on the sentence it hangs from
    -- "Using the argument principle", "Keyhole contour" -- and a numbered list
    at the foot of the page puts that a scroll away from the step it explains.
    Tufte's arrangement keeps it level with its own line.

    The markdown written beside the HTML keeps real footnotes: this walk runs
    on the way to the page, not on the way to the source.
    """
    del document
    if not isinstance(element, pf.Note):
        return None
    match list(element.content):
        case []:
            # Five footnote definitions in the corpus have nothing after them.
            # A mark pointing at no text is noise on the page, and inventing the
            # note is not this walk's business: the mark goes and #59 records
            # the missing asides.
            return []
        case [pf.Para() as paragraph]:
            note = list(paragraph.content)
        case _:
            raise ValueError("a sidenote is one paragraph; this note is not")
    return [
        pf.RawInline('<span class="sidenote-number"></span>', format="html"),
        pf.Span(*note, classes=["sidenote"]),
    ]


def _prepare_html(
    element: pf.Element,
    document: pf.Doc,
) -> pf.Element | list[pf.Block] | list[pf.Inline] | None:
    compiled = _compile_tikzcd(element, document)
    if compiled is not None:
        return compiled
    figure = _figure(element, document)
    if figure is not None:
        return figure
    sidenote = _sidenote(element, document)
    if sidenote is not None:
        return sidenote
    return _reveal(element, document)


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
    # The wiki's own index is the root of every trail. It is filed beside the
    # subjects rather than above them, so walking `parent` never reaches it and
    # a subject landing page's breadcrumb was one crumb repeating its heading.
    wiki_root = Crumb(title="Wiki", route=Path("wiki/index.html"))

    def trail_of(key: str) -> tuple[Crumb, ...]:
        steps: list[Crumb] = []
        cursor = links[key]
        while True:
            match cursor.target:
                case LevelOnly():
                    raise ValueError(f"a wiki page is a level, not a page: {cursor.key}")
                case PageTarget(route=route):
                    steps.append(Crumb(title=cursor.title, route=route))
            match cursor.parent:
                case RootParent():
                    break
                case NodeParent(key=parent_key):
                    cursor = links[parent_key]
        steps.reverse()
        if steps[0].route == wiki_root.route:
            return tuple(steps)
        return (wiki_root, *steps)

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
                trail=trail_of(page_keys[route_key]),
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


# A wikilink standing on its own -- in a paragraph that is nothing but card
# links and the whitespace between them -- names the statement the author wanted
# read there, not a place to go and read it. It is transcluded: the card's own
# blocks render in its position under the id that cites them, the way the Stacks
# Project prints a result under its tag. A wikilink inside a sentence is a
# reference to somewhere else and stays a link.
#
# The transcluded card goes through `_rename`, the walk `_blocks` already runs
# for a tag page, so a transcluded definition is the same `div.qual-section`
# markup a locally authored `:::{.definition}` produces.
CARD_ROUTE = "tag/"

# Sorts a sitting within its year. A sitting with no recorded term sorts after
# the ones that have one rather than ahead of spring.
TERM_RANK = "case s.term " + " ".join(f"when '{term}' then {rank}" for rank, term in enumerate(TERMS_IN_YEAR_ORDER)) + f" else {len(TERMS_IN_YEAR_ORDER)} end"
WIKILINK_CLASS = "wikilink"


def _transcluded_ids(block: pf.Element) -> list[str]:
    """The card ids a paragraph transcludes, or nothing if it is prose.

    Consecutive authored links share one paragraph -- pandoc joins adjacent
    lines, and several are written on one line besides -- so the paragraph is
    the unit and every link in it transcludes. That is also why the run of
    merged underlined links these rendered as needs no separate fix: it is not
    a paragraph of links any more.
    """
    if not isinstance(block, pf.Para | pf.Plain):
        return []
    ids: list[str] = []
    for inline in block.content:
        if isinstance(inline, pf.Space | pf.SoftBreak | pf.LineBreak):
            continue
        if not isinstance(inline, pf.Link) or WIKILINK_CLASS not in inline.classes:
            return []
        path = urlsplit(inline.url).path
        if not path.startswith(CARD_ROUTE) or not path.endswith(".html"):
            return []
        ids.append(Path(path).stem)
    return ids


def _transclusion_head(card: sqlite3.Row) -> dict:
    """The heading line: the card's name, then the tag that permalinks it.

    The name is the YAML `title` and nothing else. A body-level `title=` on the
    card's outermost block is import residue, not a second name -- 85 cards
    carry junk there ("part 1", "of claim") over a real YAML title -- so that
    block is unwrapped and its attribute never reaches the heading. Nested
    `title=` blocks keep theirs: those label which part or case they treat.
    """
    href = html.escape(f"{CARD_ROUTE}{card['id']}.html", quote=True)
    # The brackets are inside the anchor so the whole `(Tag …)` wraps as one
    # piece; outside it, a long name left the closing bracket alone on the
    # next line.
    tag = f'<a class="qual-section-tag" href="{href}">(Tag {html.escape(card["id"])})</a>'
    return {
        "t": "RawBlock",
        "c": ["html", f'<p class="qual-section-title">{html.escape(card["title"])} {tag}</p>'],
    }


def _transclude(card: sqlite3.Row, counts: Counter[str]) -> pf.Div:
    """The card as one labelled section: kind and number, name, tag, body.

    The card's own outermost section div is unwrapped and this one takes its
    kind, so the reader sees one labelled box rather than a tagged box nested
    inside an untagged one. A card that opens on prose instead of a fenced div
    is labelled by its catalog kind, which is the same word.

    The number counts that kind on the page, not the transclusions before it.
    One sequence across every kind produced "Warning 14" on a page carrying one
    warning: the label asserts what it counts, so it has to count warnings.
    """
    document = json.loads(card["ast"])
    blocks = document["blocks"]
    kind = _owned_kind(blocks[0]) if blocks else ""
    if kind:
        body = blocks[0]["c"][1] + blocks[1:]
    else:
        kind, body = card["kind"], blocks
    counts[kind] += 1
    _rename_json(body)
    document["blocks"] = [
        {
            "t": "Div",
            "c": [
                [
                    card["id"],
                    [f"qual-{kind}", SECTION_CLASS, "qual-transclusion"],
                    [["data-label", f"{kind.title()} {counts[kind]}"]],
                ],
                [_transclusion_head(card), *body, *_prompts_json(card)],
            ],
        }
    ]
    return cast(pf.Div, from_ast(json.dumps(document)).content[0])


def _transclude_wikilinks(blocks: list[pf.Block], cards: dict[str, sqlite3.Row]) -> list[pf.Block]:
    """Replace every standalone-wikilink paragraph with the cards it names.

    A card already transcluded on the page is dropped rather than repeated: the
    first rendering is the one its tag cites. A paragraph whose links were all
    repeats leaves nothing behind. A card id `resolve_links` did not resolve
    never reaches here -- it is a build error there.
    """
    seen: set[str] = set()
    counts: Counter[str] = Counter()

    def visit(element: pf.Element, doc: pf.Doc) -> pf.Element | list[pf.Block] | None:
        del doc
        ids = _transcluded_ids(element)
        if not ids:
            return None
        rendered: list[pf.Block] = []
        for card_id in ids:
            if card_id in seen:
                continue
            seen.add(card_id)
            rendered.append(_transclude(cards[card_id], counts))
        return rendered

    return list(pf.Doc(*blocks).walk(visit).content)


def _wiki_blocks(page: WikiPage, incoming: list[WikiPage], cards: dict[str, sqlite3.Row]) -> list[pf.Block]:
    """An authored wiki page gets the same section labelling a card gets.

    Only the card path ran `_rename`, so every `:::{.remark}`, `:::{.proof}`
    and `:::{.fact}` on the wiki reached the reader as unmarked prose: the
    label rule in `styles.css` keys on the `qual-section` class this adds.
    Transcluded cards are inserted first, so the same walk labels those too.
    Incoming wikilinks are inverted from the resolved graph, not authored.
    """
    blocks = list(pf.Doc(*_transclude_wikilinks(page.blocks, cards)).walk(_rename).content)
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


@dataclass(frozen=True)
class CardPageData:
    terms: dict[tuple[str, str], list[str]]
    facets: dict[str, list[sqlite3.Row]]
    related: dict[tuple[str, str], list[sqlite3.Row]]
    dependencies: dict[str, list[sqlite3.Row]]
    backlinks: dict[str, list[sqlite3.Row]]


def load_card_page_data(con: sqlite3.Connection) -> CardPageData:
    terms: dict[tuple[str, str], list[str]] = {}
    for row in _rows(con, "select card_id, axis, term from classifications order by card_id, axis, term"):
        key = (row["card_id"], row["axis"])
        if key not in terms:
            terms[key] = []
        terms[key].append(row["term"])

    facets: dict[str, list[sqlite3.Row]] = {}
    for row in _rows(
        con,
        """
        select cp.problem_id, e.institution, s.year
        from collection_problems cp
        join sources s on s.id=cp.collection_id
        left join exam_sources e on e.id=s.id
        order by cp.problem_id, e.institution, s.year
        """,
    ):
        card_id = row["problem_id"]
        if card_id not in facets:
            facets[card_id] = []
        facets[card_id].append(row)

    related: dict[tuple[str, str], list[sqlite3.Row]] = {}
    for row in _rows(
        con,
        """
        select r.target_id, r.kind as relation_kind, c.*
        from relations r join cards c on c.id=r.source_id
        where r.kind in ('hints-at', 'solves')
        order by r.target_id, r.kind, c.id
        """,
    ):
        key = (row["target_id"], row["relation_kind"])
        if key not in related:
            related[key] = []
        related[key].append(row)

    dependencies: dict[str, list[sqlite3.Row]] = {}
    for row in _rows(
        con,
        """
        select r.source_id, c.id, c.title, r.kind as relation_kind
        from relations r join cards c on c.id=r.target_id
        where r.kind in ('uses', 'cites', 'extracted-from')
        order by r.source_id, r.kind, c.title, c.id
        """,
    ):
        card_id = row["source_id"]
        if card_id not in dependencies:
            dependencies[card_id] = []
        dependencies[card_id].append(row)

    backlinks: dict[str, list[sqlite3.Row]] = {}
    for row in _rows(
        con,
        """
        select r.target_id, c.id, c.title, r.kind as relation_kind
        from relations r join cards c on c.id=r.source_id
        order by r.target_id, r.kind, c.title, c.id
        """,
    ):
        card_id = row["target_id"]
        if card_id not in backlinks:
            backlinks[card_id] = []
        backlinks[card_id].append(row)

    return CardPageData(
        terms=terms,
        facets=facets,
        related=related,
        dependencies=dependencies,
        backlinks=backlinks,
    )


def _page_terms(data: CardPageData, card_id: str, axis: str) -> list[str]:
    key = (card_id, axis)
    return data.terms[key] if key in data.terms else []


def _page_rows(rows: dict[str, list[sqlite3.Row]], card_id: str) -> list[sqlite3.Row]:
    return rows[card_id] if card_id in rows else []


def _related_rows(data: CardPageData, card_id: str, kind: str) -> list[sqlite3.Row]:
    key = (card_id, kind)
    return data.related[key] if key in data.related else []


def _card_relation_items(
    rows: list[sqlite3.Row],
) -> str:
    if not rows:
        return ""
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
        return ""
    return "<ul>" + "".join(f'<li><a href="{html.escape(appearance.target_key, quote=True)}">{html.escape(appearance.title)}</a></li>' for appearance in appearances) + "</ul>"


def _relation_group(key: str, heading: str, items: str) -> str:
    """One panel, or nothing when the card has no relations of that sort.

    A heading whose body reads "None." tells the reader nothing and cost two of
    the three panels on a typical card. An empty panel is dropped, and a card
    with no relations at all loses the band rather than showing an empty frame.
    """
    if not items:
        return ""
    return f'<section class="relation-group" data-relation-group="{key}"><h2>{heading}</h2>{items}</section>'


def _relation_groups_json(
    data: CardPageData,
    card_id: str,
    appearances: dict[str, list[Appearance]],
    wiki_mentions: list[WikiPage],
) -> list[dict]:
    dependencies = _page_rows(data.dependencies, card_id)
    backlinks = _page_rows(data.backlinks, card_id)
    panels = [
        _relation_group("dependencies", "Dependencies", _card_relation_items(dependencies)),
        _relation_group("appearances", "Appearances", _appearance_items(appearances[card_id])),
        _relation_group("backlinks", "Backlinks", _card_relation_items(backlinks)),
        _wiki_incoming_html(wiki_mentions),
    ]
    filled = [panel for panel in panels if panel]
    if not filled:
        return []
    source = f'<div class="relation-groups" aria-label="Card relationships">{"".join(filled)}</div>'
    return [{"t": "RawBlock", "c": ["html", source]}]


def load_json(con: sqlite3.Connection) -> tuple[dict, list]:
    """{card id -> its body block list} as raw pandoc JSON, plus the api version."""
    cache, api = {}, [1, 23]
    for r in _rows(con, "select id, ast from cards"):
        doc = json.loads(r["ast"])
        api = doc["pandoc-api-version"]
        cache[r["id"]] = doc["blocks"]
    return cache, api


def _owned_kind(node: object) -> str:
    """The card kind an owned Div carries, before renaming; "" for anything else."""
    if not isinstance(node, dict) or node.get("t") != "Div":
        return ""
    owned = next((c for c in node["c"][0][1] if c in OWNED), "")
    return DIV_CLASS_TO_KIND[owned] if owned else ""


def _rename_json(node: object, number: str = "") -> None:
    """The `_rename` transform, on raw JSON: rename owned Div classes at any depth.

    Siblings of one kind are numbered. A card with five `.solution` blocks read
    as five boxes all labelled "Solution" with nothing to cite one by, which is
    what the authored `title="Part 1"` labels were standing in for. A kind
    occurring once is not numbered: "Definition 1" alone names nothing.
    """
    if isinstance(node, list):
        counts = Counter(kind for kind in map(_owned_kind, node) if kind)
        seen: Counter[str] = Counter()
        for x in node:
            kind = _owned_kind(x)
            if kind and counts[kind] > 1:
                seen[kind] += 1
                _rename_json(x, f" {seen[kind]}")
            else:
                _rename_json(x)
    elif isinstance(node, dict):
        if node.get("t") == "Div":
            attr = node["c"][0]  # [id, classes, keyvals]
            owned = [c for c in attr[1] if c in OWNED]
            attr[1] = [_owned_class(class_name) for class_name in attr[1]]
            if owned:
                kind = DIV_CLASS_TO_KIND[owned[0]]
                attr[1].append(SECTION_CLASS)
                attr[2].append(["data-label", f"{kind.title()}{number}"])
                title = next((value.strip() for key, value in attr[2] if key == "title"), "")
                if title and kind in TITLED_KINDS:
                    node["c"][1].insert(0, {"t": "RawBlock", "c": ["html", _title_html(title)]})
        _rename_json(node.get("c"))


def _prompts_json(card: sqlite3.Row) -> list[dict]:
    """The card's review questions, one block each, after the statement.

    They sit below rather than above because the card is the answer and it is
    already on the page: a question printed over the statement it gives away is
    a heading, not a review. On a wiki page of transcluded definitions, leading
    each one with a question would also read as a quiz rather than a reference.

    One block per prompt, which is the shape the author writes -- several
    questions are several questions, not one list with a heading over it. A
    card with no prompts emits nothing at all.
    """
    return [{"t": "RawBlock", "c": ["html", f'<div class="review-question">{html.escape(prompt)}</div>']} for prompt in cast(list[str], json.loads(card["prompts"]))]


def _dup[T](value: T) -> T:
    return copy.deepcopy(value)


def problem_json(
    data: CardPageData,
    card: sqlite3.Row,
    jcache: dict,
    appearances: dict[str, list[Appearance]],
    wiki_mentions: dict[str, list[WikiPage]],
) -> tuple[dict, list]:
    facets = _page_rows(data.facets, card["id"])
    institutions = sorted({f["institution"].upper() for f in facets if f["institution"]})
    years = sorted({str(f["year"]) for f in facets if f["year"] is not None})
    areas = _page_terms(data, card["id"], "area")
    topics = _page_terms(data, card["id"], "topic")

    body = _dup(jcache[card["id"]])
    _rename_json(body)
    for kind in ("hints-at", "solves"):
        for rel in _related_rows(data, card["id"], kind):
            rb = _dup(jcache[rel["id"]])
            _rename_json(rb)
            body += rb
    body.extend(_prompts_json(card))
    body.extend(_relation_groups_json(data, card["id"], appearances, wiki_mentions.get(card["id"], [])))
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
    data: CardPageData,
    card: sqlite3.Row,
    jcache: dict,
    appearances: dict[str, list[Appearance]],
    wiki_mentions: dict[str, list[WikiPage]],
) -> tuple[dict, list]:
    body = _dup(jcache[card["id"]])
    _rename_json(body)
    body.extend(_prompts_json(card))
    body.extend(_relation_groups_json(data, card["id"], appearances, wiki_mentions.get(card["id"], [])))
    meta = {
        "title": card["title"],
        "subtitle": card["id"],
        "categories": sorted(set(_page_terms(data, card["id"], "topic") + _page_terms(data, card["id"], "area"))),
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
        pandoc.write_html(_html_asts(documents)),
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


def _card_route(card: sqlite3.Row) -> str:
    """A collection's page is written under `exam/`, every other card under `tag/`.

    The caller supplies only the path back to the site root, so a link to a card
    cannot disagree with where that card was written. A collection may list a
    sibling collection among its contents, and then the target is not a problem.
    """
    return "exam" if card["kind"] == "collection" else "tag"


def _link_inline(
    card: sqlite3.Row,
    inline_cache: dict[str, list[pf.Inline]],
    base: str = "../",
) -> pf.Link:
    return pf.Link(
        *_inlines(card["title"], inline_cache),
        url=f"{base}{_card_route(card)}/{card['id']}.html",
    )


def _link(
    card: sqlite3.Row,
    inline_cache: dict[str, list[pf.Inline]],
    base: str = "../",
) -> pf.Plain:
    return pf.Plain(_link_inline(card, inline_cache, base))


Page = tuple[dict, list[pf.Block]]
PageItem = tuple[Page, Path, PageChrome]


def _page_ast(page: Page) -> str:
    _, blocks = page
    return to_json(pf.Doc(*blocks))


def _html_ast(ast: str) -> str:
    return to_json(from_ast(ast).walk(_prepare_html))


def _html_asts(documents: list[str]) -> list[str]:
    if len(documents) < 1_000:
        return [_html_ast(document) for document in documents]
    with ProcessPoolExecutor(max_workers=4) as executor:
        return list(executor.map(_html_ast, documents, chunksize=64))


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
        pandoc.write_html(_html_asts(documents)),
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
    # A guide section's `parent` is the section it assumes, not the place it is
    # filed: the whole guide is one flat list under the guide. The breadcrumb
    # says where the page is, and the sidebar says what it depends on.
    trail: tuple[Crumb, ...] = (
        Crumb(title="Guides", route=Path("guides.html")),
        Crumb(title=manifest.title, route=_publication_root_route(manifest)),
    )
    if current_key != manifest.id:
        section = next(item for item in manifest.sections if item.slug == current_key)
        trail = (*trail, Crumb(title=section.title, route=_publication_section_route(manifest, section)))
    return PublicationNavigation(
        links=links,
        current_key=current_key,
        position=position,
        trail=trail,
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
        select cp.problem_id, cp.collection_id, cp.ordinal, cp.comment, c.title
        from collection_problems cp
        join cards c on c.id=cp.collection_id
        order by c.title, coalesce(cp.section_ordinal, -1), cp.ordinal
        """,
    ):
        # The listing's own comment is the locator the source uses -- "Fall 2011",
        # "Munkres §28". Where an entry has none, the position in the list is all
        # the collection knows about where the problem sat.
        locator = row["comment"] or f"problem {row['ordinal'] + 1}"
        appearances[row["problem_id"]].append(
            Appearance(
                target_key=row["collection_id"],
                title=f"{row['title']}, {locator}",
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
    # Every number is counted off the catalog. A figure written into the copy
    # is true on the day it is written and silently false afterwards.
    scale = _rows(
        con,
        """
        select
          (select count(*) from cards where kind in ('problem', 'exercise')) as asked,
          (select count(*) from exam_sources) as sittings,
          (select count(distinct institution) from exam_sources) as institutions,
          (select count(*) from cards where kind in ('problem', 'exercise')
             and (id in (select card_id from sections where section_kind = 'solution')
                  or id in (select target_id from relations where kind = 'solves'))) as solved
        """,
    )[0]
    output = _successful_outputs(
        pandoc.read_markdown(
            [
                f"Past qualifying-exam problems, with the sources and notes to work them. "
                f"{scale['asked']:,} problems and exercises, from {scale['sittings']:,} exam sittings "
                f"at {scale['institutions']} institutions and from textbooks, homework sets and compiled scans. "
                f"{scale['solved']:,} carry a written solution.\n\n"
                "## Where to start\n\n"
                "[Browse](problems.html)\n"
                ": Every problem, filtered by area, topic, institution and year.\n\n"
                "[Generate](generate.html)\n"
                ": A practice set drawn to those same filters.\n\n"
                "[Exams](exams.html)\n"
                ": Each sitting as it was sat, problem by problem.\n\n"
                "[Guides](guides.html)\n"
                ": One ordered path per subject, built from the same problems. Read front to back:\n"
                "  a section assumes only the sections above it.\n\n"
                "[Wiki](wiki/index.html)\n"
                ": Written notes filed by subject. Look one topic up rather than read a path.\n"
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


def _listing_filters(
    noun: str,
    placeholder: str,
    facet_values: dict[str, list[str]],
) -> pf.RawBlock:
    """The search box and one select per facet, above a filtered listing.

    `app.js` reads the axes off the `data-facet` attributes rather than being
    told which page it is on, so a page adds an axis by emitting a control for
    it. `noun` is what the running count calls the rows.
    """
    return pf.RawBlock(
        '<div class="listing-filters">'
        '<label for="listing-search">Search'
        f'<input id="listing-search" type="search" data-noun="{html.escape(noun, quote=True)}"'
        f' placeholder="{html.escape(placeholder, quote=True)}">'
        "</label>"
        + "".join(
            f'<label for="listing-{axis}">{axis.title()}'
            f'<select id="listing-{axis}" multiple size="5" data-facet="{axis}">'
            + "".join(f'<option value="{html.escape(value, quote=True)}">{html.escape(_facet_option_label(axis, value))}</option>' for value in values)
            + "</select></label>"
            for axis, values in facet_values.items()
        )
        + '<output id="listing-count" aria-live="polite"></output></div>',
        format="html",
    )


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
        -- Grouped by area, and within an area the titles that begin with prose
        -- come before the ones that begin with mathematics. Ordering by the raw
        -- title alone opened the page on 483 formulas, because `$` sorts ahead
        -- of every letter.
        order by areas, case when c.title like '$%' then 1 else 0 end, c.title, c.id
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
    heading_area = ""
    for problem in problems:
        area_terms = _facet_terms(problem["areas"])
        topic_terms = _facet_terms(problem["topics"])
        # One heading per area, carrying the area's own name so the filter can
        # hide a heading whose problems are all hidden.
        if problem["areas"] != heading_area:
            heading_area = problem["areas"]
            label = ", ".join(_facet_option_label("area", a) for a in area_terms) or "Unclassified"
            rows.append(
                pf.Div(
                    pf.Header(pf.Str(label), level=2),
                    classes=["listing-group"],
                    attributes={"data-area": FACET_SEP.join(area_terms), "data-label": label},
                )
            )
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
                # Para, not Plain: Plain writes the text with no element around
                # it, and three of those in a row are one anonymous grid item,
                # not three. The row's columns had nothing to lay out.
                pf.Para(_link_inline(problem, inline_cache, base="")),
                pf.Para(pf.Str(facet_text or "Unclassified")),
                pf.Para(pf.Str("Sources: "), *source_links) if source_links else pf.Para(pf.Str("Sources: none")),
                # 4161 of the 4921 titles are mathematics. Typesetting all of
                # them on load cost ten seconds before a reader could touch the
                # filter. `mathjax_ignore` is MathJax's own opt-out class, so
                # the initial pass skips every row; `app.js` removes it from a
                # row and typesets that row when it scrolls into view.
                classes=["listing-row", "mathjax_ignore"],
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
        _listing_filters("problem", "Group theory, UGA, 2019…", facet_values),
        pf.Div(*rows, classes=["listing"]),
    ]


# Every source kind a collection can declare, in the order a reader meets them,
# with the heading each one is listed under. A kind absent here would go
# unlisted, so the page checks the set against the catalog and fails the build.
SOURCE_KIND_HEADINGS = {
    "university-exam": "University exams",
    "compilation": "Compiled scans",
    "homework": "Homework sets",
    "textbook": "Textbooks",
}


GUIDES_LEDE = (
    "One ordered path per subject, built from the corpus. "
    "A guide is read front to back: each section assumes only the sections above it, and the study path in the margin is that order. "
    "The [wiki](wiki/index.html) covers the same subjects as written notes, filed to be looked up rather than read through."
)


def source_index_page(
    con: sqlite3.Connection,
    inline_cache: dict[str, list[pf.Inline]],
) -> Page:
    """Every collection the corpus draws from, under the kind of thing it is.

    The page listed only the 338 sittings. The other 43 -- 20 compiled scans, 17
    homework sets, 6 textbooks -- had no listing anywhere, and the largest
    collection on the site, Munkres with 586 problems, was among them: a reader
    reached it only from a problem card.
    """
    collections = _rows(
        con,
        f"""
        select c.*, s.source_kind, s.year,
          coalesce(e.institution, '') as institution,
          coalesce(e.area, '') as area,
          (select count(*) from collection_problems where collection_id=c.id) as problems,
          (select count(*) from collection_problems cp
           where cp.collection_id=c.id
             and (cp.problem_id in (select card_id from sections where section_kind='solution')
                  or cp.problem_id in (select target_id from relations where kind='solves'))) as solved
        from cards c join sources s on s.id=c.id
        left join exam_sources e on e.id=s.id
        order by e.institution, s.year, {TERM_RANK}, e.area, c.title, c.id
        """,
    )
    unlisted = {row["source_kind"] for row in collections} - set(SOURCE_KIND_HEADINGS)
    if unlisted:
        raise ValueError(f"source kinds with no heading on the source index: {sorted(unlisted)}")

    facet_values = {
        "area": sorted({row["area"] for row in collections if row["area"]}),
        "institution": sorted({row["institution"].upper() for row in collections if row["institution"]}),
        "year": sorted({str(row["year"]) for row in collections if row["year"] is not None}),
    }
    blocks: list[pf.Block] = [
        pf.Para(*_inlines(f"Every collection the corpus draws problems from: {len(collections)} in all.", inline_cache)),
        _listing_filters("source", "UGA, topology, 2019…", facet_values),
    ]
    rows: list[pf.Block] = []
    for kind, heading in SOURCE_KIND_HEADINGS.items():
        listed = [row for row in collections if row["source_kind"] == kind]
        rows.append(
            pf.Div(
                pf.Header(pf.Str(f"{heading} ({len(listed)})"), level=2),
                classes=["listing-group"],
                # The filter rewrites the count to what it is showing, so the
                # heading has to say what the label alone is.
                attributes={"data-label": heading},
            )
        )
        for row in listed:
            institution = row["institution"].upper()
            year = "" if row["year"] is None else str(row["year"])
            # How much of a collection is worked is the fact a reader picking one
            # to sit is after, and no listing carried it.
            solutions = f"{row['problems']} problems, {row['solved']} solved" if row["problems"] else "no problems listed"
            rows.append(
                pf.Div(
                    pf.Para(_link_inline(row, inline_cache, "")),
                    pf.Para(pf.Str(" · ".join(part for part in (institution, row["area"].replace("-", " ").title(), year) if part) or "—")),
                    pf.Para(pf.Str(solutions)),
                    classes=["listing-row"],
                    attributes={
                        "data-search": " ".join(str(part) for part in (row["title"], row["id"], institution, row["area"], year) if part).lower(),
                        "data-area": row["area"],
                        "data-institution": institution,
                        "data-year": year,
                    },
                )
            )
    blocks.append(pf.Div(*rows, classes=["listing"]))
    return {"title": "Sources"}, blocks


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
                {"href": "exams.qmd", "text": "Sources"},
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

    # A wiki page may point at the rest of the site, and a page three folders
    # deep cannot spell the way back itself. `SITE_PAGES` is the set the wiki
    # resolver lets through; here is where each one lands.
    for name in SITE_PAGES:
        add(name, Path(name))
    for card in _rows(con, "select id, kind from cards"):
        add(card["id"], Path(_card_route(card)) / f"{card['id']}.html")
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
        directory = _card_route(card)
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
            f"Every collection the corpus draws problems from: {len(_rows(con, 'select id from sources'))} in all.",
            GUIDES_LEDE,
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
    card_page_data = load_card_page_data(con)
    tag_pages: list[tuple[Path, dict, list]] = []
    for card in _rows(con, "select * from cards where kind='problem'"):
        meta, body = problem_json(card_page_data, card, jcache, appearances, mentions)
        tag_pages.append((out / "tag" / f"{card['id']}.qmd", meta, body))
    for card in _rows(con, "select * from cards where kind not in ('problem','collection')"):
        meta, body = plain_json(card_page_data, card, jcache, appearances, mentions)
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

    write_page(
        site_root,
        Path("404.html"),
        {"title": "No such page"},
        "<p>This address names no page. It may name a card that was renamed, or a page that was never written.</p>"
        '<p>Start again from <a href="index.html">the home page</a>, '
        '<a href="problems.html">the problem browser</a>, '
        '<a href="exams.html">the exams</a>, '
        '<a href="guides.html">the guides</a>, or '
        '<a href="wiki/index.html">the wiki</a>. '
        "The search box in the header reads the whole corpus.</p>",
        mathjax,
        link_targets,
        assets,
        NotFoundPage(),
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
            source_index_page(con, inline_cache),
            out / "exams.qmd",
            StandardPage(),
        ),
    )
    pages.append(
        (
            (
                {"title": "Guides"},
                [
                    pf.Para(*_inlines(GUIDES_LEDE, inline_cache)),
                    # Each guide states what it is in its manifest and the list
                    # showed none of it: six bare subject names, the same six
                    # the wiki offers, with nothing to choose between them.
                    pf.BulletList(
                        *[
                            pf.ListItem(
                                pf.Plain(pf.Link(pf.Str(guide.title), url=f"guide/{guide.id}.html")),
                                pf.Para(*_inlines(guide.lede, inline_cache)),
                            )
                            for guide in guides
                        ]
                    ),
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
        cards = {row["id"]: row for row in _rows(con, "select * from cards")}
        wiki_navigation = _wiki_navigation(wiki_pages)
        wiki_items: list[PageItem] = [
            (
                (
                    {"title": page.title},
                    _wiki_blocks(page, incoming_pages[page.route.as_posix()], cards),
                ),
                out / page.route.with_suffix(".qmd"),
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
