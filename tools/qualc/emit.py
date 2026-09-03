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
from pathlib import Path
from typing import cast
from urllib.parse import urlencode, urlsplit

import panflute as pf
import yaml

from .index import load_areas
from .model import DIV_CLASS_TO_KIND, MARKDOWN, TERMS_IN_YEAR_ORDER, from_ast, to_json
from .pandoc_batch import (
    PandocBatchError,
    PandocFailure,
    PandocResult,
    PandocServer,
)
from .publication import (
    PublicationManifest,
    PublicationSection,
    load_publications,
)
from .static_site import (
    AssetCatalog,
    AuthoredPage,
    Crumb,
    EndReading,
    LevelOnly,
    Listing,
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
    SearchDocument,
    StandardPage,
    StartReading,
    SubjectPage,
    build_asset_catalog,
    write_page,
)
from .wiki import (
    SITE_PAGES,
    WIKI_BATCH_SIZE,
    WikiPage,
    incoming_wiki_links,
    slug,
    wiki_card_mentions,
)
from .wiki import (
    link_targets as wiki_link_targets,
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


_LAMPORT_MARKER = re.compile(r"^<(\d)>((?:\d+\.)*\d+)\.\s*$")
_LAMPORT_DIVS = {"solution", "proof", "hint", "strategy", "blockquote"}


def _marker_level(text: str) -> tuple[int, str] | None:
    match = _LAMPORT_MARKER.match(text)
    if match is None:
        return None
    return (int(match.group(1)), match.group(2))


def _lamport_group(
    segments: list[tuple[int, str, list[pf.Inline]]],
    prefix: tuple[int, ...] = (),
) -> pf.Div:
    children: list[pf.Block] = []
    i = 0
    index = 0
    while i < len(segments):
        level, num, content = segments[i]
        index += 1
        path = prefix + (index,)
        label = ".".join(str(part) for part in path)
        body: list[pf.Block] = [pf.Para(pf.Span(pf.Str(f"{label}."), classes=["pf-number"]), *content)]
        i += 1
        deeper: list[tuple[int, str, list[pf.Inline]]] = []
        while i < len(segments) and segments[i][0] > level:
            deeper.append(segments[i])
            i += 1
        if deeper:
            body.append(_lamport_group(deeper, path))
        children.append(pf.Div(*body, classes=["pf-step", f"pf-level-{level}"]))
    return pf.Div(*children, classes=["pf-group"])


def _lamport_paragraph(paragraph: pf.Para | pf.Plain) -> pf.Block:
    """Split a marker-carrying paragraph into a structured pf-group.

    Authors write `<1>1. claim. <2>1. because …` inside one wrapped paragraph;
    pandoc reads it as flat prose and the Lamport hierarchy vanishes on the
    page. Splitting at each marker restores the authored steps as nested
    groups, each with its number kept on a `pf-number` span so the page can
    render the outline. Cross-references like "step <1>1.4" stay because the
    numbering is a stable reordering of the authored sequence.
    """
    segments: list[tuple[int, str, list[pf.Inline]]] = []
    cur: list[pf.Inline] = []
    cur_level = -1
    cur_num = ""
    for inline in paragraph.content:
        marker = _marker_level(inline.text) if isinstance(inline, pf.Str) else None
        if marker is not None:
            if cur_level >= 0 or cur:
                segments.append((cur_level, cur_num, cur))
            cur_level, cur_num = marker
            cur = []
        elif isinstance(inline, pf.SoftBreak):
            continue
        else:
            cur.append(inline)
    if cur_level >= 0 or cur:
        segments.append((cur_level, cur_num, cur))
    kept = [segment for segment in segments if segment[0] >= 0]
    if not kept:
        return paragraph
    return _lamport_group(kept)


def _lamport_blocks(blocks: list[pf.Block]) -> list[pf.Block]:
    out: list[pf.Block] = []
    for block in blocks:
        if isinstance(block, pf.Para | pf.Plain):
            seen = False
            for inline in block.content:
                if isinstance(inline, pf.Str) and _marker_level(inline.text or "") is not None:
                    seen = True
                    break
            out.append(_lamport_paragraph(block) if seen else block)
        elif isinstance(block, pf.Div):
            block.content = _lamport_blocks(list(block.content))
            out.append(block)
        elif isinstance(block, pf.BulletList | pf.OrderedList):
            for item in block.content:
                item.content = _lamport_blocks(list(item.content))
            out.append(block)
        else:
            block_type = type(block).__name__.lower()
            if block_type in _LAMPORT_DIVS and hasattr(block, "content"):
                block.content = _lamport_blocks(list(block.content))
            out.append(block)
    return out


_LAMPORT_REF = re.compile(r"^<(\d)>((?:\d+\.)*\d+)(\.?)([.,;:)]?)$")


def _lamport_refs(block: pf.Element, document: pf.Doc) -> pf.Element | None:
    """Rewrite in-text step references to the rendered number.

    Inside a structured proof, `step <1>1.4` names the same step the group's
    hierarchical label prints; the `<1>` prefix is the authoring surface, not
    what a reader hunts for on the page. The rendered number is the part after
    the angle-bracket level, which the grouping above assigns verbatim.
    """
    del document
    if not isinstance(block, pf.Str):
        return None
    match = _LAMPORT_REF.match(block.text or "")
    if match is None:
        return None
    block.text = f"{match.group(2)}{match.group(3)}{match.group(4)}"
    return block


def _lamport(element: pf.Element, document: pf.Doc) -> pf.Element | None:
    del document
    if not isinstance(element, pf.Div):
        return None
    if not _LAMPORT_DIVS.intersection(element.classes):
        return None
    element.content = _lamport_blocks(list(element.content))
    element.walk(_lamport_refs, element)
    return element


def _lamport_rewrite_ref(inline: object) -> object:
    """Rewrite a `step <1>1.4` inline Str to its rendered number, raw JSON."""
    if isinstance(inline, dict) and inline.get("t") == "Str":
        match = _LAMPORT_REF.match(inline.get("c", ""))
        if match is not None:
            inline["c"] = f"{match.group(2)}{match.group(3)}{match.group(4)}"
    return inline


def _lamport_json_group(
    segments: list[tuple[int, str, list[object]]],
    prefix: tuple[int, ...] = (),
) -> dict:
    """A nested `pf-group` of `pf-step`s, as raw pandoc JSON."""
    children: list[dict] = []
    i = 0
    index = 0
    while i < len(segments):
        level, _num, content = segments[i]
        index += 1
        path = prefix + (index,)
        label = ".".join(str(part) for part in path)
        number: list[object] = [
            {
                "t": "Span",
                "c": [["", ["pf-number"], []], [{"t": "Str", "c": f"{label}."}]],
            }
        ]
        body: list[object] = [{"t": "Para", "c": [*number, *[_lamport_rewrite_ref(x) for x in content]]}]
        i += 1
        deeper: list[tuple[int, str, list[object]]] = []
        while i < len(segments) and segments[i][0] > level:
            deeper.append(segments[i])
            i += 1
        if deeper:
            body.append(_lamport_json_group(deeper, path))
        children.append({"t": "Div", "c": [["", ["pf-step", f"pf-level-{level}"], []], body]})
    return {"t": "Div", "c": [["", ["pf-group"], []], children]}


def _lamport_json_paragraph(inlines: list[object]) -> dict | None:
    """Split a flat marker-carrying inline list into one nested group, or None.

    `<1>1. claim. <2>1. because …` reads as one flat paragraph; pandoc does
    not know the `<N>` markers, so the authored hierarchy is rebuilt here.
    """
    segments: list[tuple[int, str, list[object]]] = []
    cur: list[object] = []
    cur_level = -1
    cur_num = ""
    for inline in inlines:
        if isinstance(inline, dict) and inline.get("t") == "Str":
            marker = _marker_level(inline.get("c", ""))
            if marker is not None:
                if cur_level >= 0 or cur:
                    segments.append((cur_level, cur_num, cur))
                cur_level, cur_num = marker
                cur = []
                continue
        if isinstance(inline, dict) and inline.get("t") == "SoftBreak":
            continue
        cur.append(inline)
    if cur_level >= 0 or cur:
        segments.append((cur_level, cur_num, cur))
    kept = [segment for segment in segments if segment[0] >= 0]
    if not kept:
        return None
    return _lamport_json_group(kept)


def _lamport_json_blocks(blocks: list[dict]) -> list[dict]:
    """`_lamport_blocks` on raw pandoc JSON plus the ref rewrite.

    The card-page path keeps bodies as raw JSON (see `_rename_json`) rather
    than walking pf objects, so the structured-proof pass has to run on the
    same shape. It walks Divs whose authored class is a proof/solution/hint/
    strategy, recursing into list items and blockquotes, splitting marker
    paragraphs into nested `pf-group`/`pf-step` groups, and rewriting in-text
    `<1>1.4` refs.
    """
    out: list[dict] = []
    for block in blocks:
        t = block.get("t")
        if t in ("Para", "Plain"):
            inlines = block.get("c", [])
            if any(isinstance(x, dict) and x.get("t") == "Str" and _marker_level(x.get("c", "")) is not None for x in inlines):
                grouped = _lamport_json_paragraph(inlines)
                if grouped is not None:
                    out.append(grouped)
                    continue
            block["c"] = [_lamport_rewrite_ref(x) for x in inlines]
            out.append(block)
        elif t == "Div":
            classes = block.get("c", [["", [], []]])[0][1]
            if _LAMPORT_DIVS.intersection(classes):
                block["c"][1] = _lamport_json_blocks(block["c"][1])
            out.append(block)
        elif t in ("BulletList", "OrderedList"):
            for item in block.get("c", []):
                if isinstance(item, dict) and item.get("t") == "ListItem":
                    item["c"] = _lamport_json_blocks(item["c"])
            out.append(block)
        elif t == "BlockQuote":
            quoted: list[object] = []
            for q in block.get("c", []):
                if isinstance(q, list):
                    quoted.append(_lamport_json_blocks(q))
                elif isinstance(q, dict):
                    quoted.append(_lamport_json_blocks([q])[0])
                else:
                    quoted.append(q)
            block["c"] = quoted
            out.append(block)
        else:
            out.append(block)
    return out


def _prepare_html(
    element: pf.Element,
    document: pf.Doc,
) -> pf.Element | list[pf.Block] | list[pf.Inline] | None:
    lamport = _lamport(element, document)
    if lamport is not None:
        return lamport
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
    return AuthoredPage(found) if found else StandardPage(Listing())


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
        "c": [
            "html",
            f'<p class="qual-section-title">{html.escape(card["title"])} {tag}</p>',
        ],
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


def _wiki_blocks(
    page: WikiPage,
    incoming: list[WikiPage],
    cards: dict[str, sqlite3.Row],
    areas: set[str],
) -> list[pf.Block]:
    """An authored wiki page gets the same section labelling a card gets.

    Only the card path ran `_rename`, so every `:::{.remark}`, `:::{.proof}`
    and `:::{.fact}` on the wiki reached the reader as unmarked prose: the
    label rule in `styles.css` keys on the `qual-section` class this adds.
    Transcluded cards are inserted first, so the same walk labels those too.
    Incoming wikilinks are inverted from the resolved graph, not authored.
    """
    blocks = list(pf.Doc(*_transclude_wikilinks(page.blocks, cards)).walk(_rename).content)
    branch = slug(page.source_rel.parts[0]) if len(page.source_rel.parts) > 1 else ""
    is_subject_root = page.source_rel.name == "index.md" and len(page.source_rel.parts) == 2 and branch in areas
    if is_subject_root:
        blocks.append(_problem_browse_link_block(branch, ()))
    elif page.topics:
        blocks.append(_problem_browse_link_block(branch, page.topics))
    html_block = _wiki_incoming_html(incoming)
    if html_block:
        blocks.append(pf.RawBlock(html_block, format="html"))
    return blocks


# --- raw-JSON tag-page path -------------------------------------------------
#
# The 3,200 tag pages are the bulk of the build. Composing them through panflute
# means one pandoc process per card to load and one per page to write -- an hour.
# Their bodies are only a card's own blocks. For a problem, hints and solutions
# are already semantic sections in that body. No `uses` link, no title parsing:
# every piece is already pandoc JSON
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
    dependencies: dict[str, list[sqlite3.Row]]
    backlinks: dict[str, list[sqlite3.Row]]


def load_card_page_data(con: sqlite3.Connection) -> CardPageData:
    terms: dict[tuple[str, str], list[str]] = {}
    for row in _rows(
        con,
        "select card_id, axis, term from classifications order by card_id, axis, term",
    ):
        key = (row["card_id"], row["axis"])
        if key not in terms:
            terms[key] = []
        terms[key].append(row["term"])

    facets: dict[str, list[sqlite3.Row]] = {}
    for row in _rows(
        con,
        """
        select cp.problem_id, cp.collection_id, cp.section_ordinal, cp.section_name, cp.ordinal, cp.comment,
          c.title as collection_title, s.source_kind, s.year as source_year,
          case when s.source_kind='university-exam' then s.year else null end as exam_year,
          e.institution
        from collection_problems cp
        join cards listed on listed.id=cp.problem_id and listed.kind='problem'
        join cards c on c.id=cp.collection_id
        join sources s on s.id=cp.collection_id
        left join exam_sources e on e.id=s.id
        order by cp.problem_id, cp.collection_id, coalesce(cp.section_ordinal, -1), cp.ordinal
        """,
    ):
        card_id = row["problem_id"]
        if card_id not in facets:
            facets[card_id] = []
        facets[card_id].append(row)

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
        dependencies=dependencies,
        backlinks=backlinks,
    )


def _page_terms(data: CardPageData, card_id: str, axis: str) -> list[str]:
    key = (card_id, axis)
    return data.terms[key] if key in data.terms else []


def _page_rows(rows: dict[str, list[sqlite3.Row]], card_id: str) -> list[sqlite3.Row]:
    return rows[card_id] if card_id in rows else []


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
    source_collections: dict[str, list[Appearance]],
    guide_appearances: dict[str, list[Appearance]],
    wiki_mentions: list[WikiPage],
) -> list[dict]:
    dependencies = _page_rows(data.dependencies, card_id)
    backlinks = _page_rows(data.backlinks, card_id)
    panels = [
        _relation_group(
            "source-collections",
            "Source Collections",
            _appearance_items(source_collections.get(card_id, [])),
        ),
        _relation_group(
            "guide-appearances",
            "Guide Appearances",
            _appearance_items(guide_appearances.get(card_id, [])),
        ),
        _relation_group("dependencies", "Dependencies", _card_relation_items(dependencies)),
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
    return [
        {
            "t": "RawBlock",
            "c": ["html", f'<div class="review-question">{html.escape(prompt)}</div>'],
        }
        for prompt in cast(list[str], json.loads(card["prompts"]))
    ]


def _dup[T](value: T) -> T:
    return copy.deepcopy(value)


def _statement_first(blocks: list[dict]) -> list[dict]:
    """The card's own blocks, with the question marked off from the answers.

    A practice sheet needs the question and must not carry the answer, and the
    browser's sampled practice view asks the card's page for it rather than being handed every
    statement on the site. Which blocks are the question is something the
    emitter knows and a reader of the HTML would have to guess: taking blocks
    up to the first answer truncates the 11 problems that write more of the
    question after one.
    """
    statement = [block for block in blocks if not (block.get("t") == "Div" and set(block["c"][0][1]) & ANSWER_CLASSES)]
    answers = [block for block in blocks if block.get("t") == "Div" and set(block["c"][0][1]) & ANSWER_CLASSES]
    if not statement:
        return answers
    return [{"t": "Div", "c": [["", ["card-statement"], []], statement]}, *answers]


def _asked_meta(data: CardPageData, card: sqlite3.Row) -> dict[str, object]:
    facets = _page_rows(data.facets, card["id"])
    institutions = sorted({f["institution"].upper() for f in facets if f["institution"]})
    years = sorted({str(f["exam_year"]) for f in facets if f["exam_year"] is not None})
    areas = _page_terms(data, card["id"], "area")
    topics = _page_terms(data, card["id"], "topic")
    meta: dict[str, object] = {
        "title": card["title"],
        "subtitle": card["id"],
        "area": ", ".join(a.replace("-", " ").title() for a in areas),
        "review": card["review"],
        "categories": sorted(set(topics + areas + institutions + years)),
    }
    if institutions:
        meta["institutions"] = ", ".join(institutions)
    if years:
        meta["years"] = ", ".join(years)
    return meta


def asked_json(
    data: CardPageData,
    card: sqlite3.Row,
    jcache: dict,
    source_collections: dict[str, list[Appearance]],
    guide_appearances: dict[str, list[Appearance]],
    wiki_mentions: dict[str, list[WikiPage]],
) -> tuple[dict, list]:
    body = _statement_first(_dup(jcache[card["id"]]))
    body = _lamport_json_blocks(body)
    _rename_json(body)
    body.extend(_prompts_json(card))
    body.extend(
        _relation_groups_json(
            data,
            card["id"],
            source_collections,
            guide_appearances,
            wiki_mentions.get(card["id"], []),
        )
    )
    return _asked_meta(data, card), body


def plain_json(
    data: CardPageData,
    card: sqlite3.Row,
    jcache: dict,
    source_collections: dict[str, list[Appearance]],
    guide_appearances: dict[str, list[Appearance]],
    wiki_mentions: dict[str, list[WikiPage]],
) -> tuple[dict, list]:
    body = _dup(jcache[card["id"]])
    body = _lamport_json_blocks(body)
    _rename_json(body)
    body.extend(_prompts_json(card))
    body.extend(
        _relation_groups_json(
            data,
            card["id"],
            source_collections,
            guide_appearances,
            wiki_mentions.get(card["id"], []),
        )
    )
    meta = {
        "title": card["title"],
        "subtitle": card["id"],
        "categories": sorted(set(_page_terms(data, card["id"], "topic") + _page_terms(data, card["id"], "area"))),
    }
    return meta, body


def _card_filters(
    data: CardPageData,
    card: sqlite3.Row,
    also: tuple[tuple[str, str], ...] = (),
) -> tuple[tuple[str, str], ...]:
    """The values a card's page answers under, in the spelling the rows carry.

    These are ids and acronyms, not display names: a filter value is matched,
    and what a reader is shown is the registry's business. `also` carries what
    a particular kind of card knows and the `cards` row does not -- a
    collection's source kind lives in `sources`.
    """
    facets = _page_rows(data.facets, card["id"])
    return (
        ("kind", card["kind"]),
        *also,
        *(("area", term) for term in _page_terms(data, card["id"], "area")),
        *(("topic", term) for term in _page_terms(data, card["id"], "topic")),
        *sorted({("source_kind", row["source_kind"]) for row in facets}),
        *sorted({("collection", row["collection_id"]) for row in facets}),
        *sorted({("institution", row["institution"].upper()) for row in facets if row["institution"]}),
        *sorted({("year", str(row["source_year"])) for row in facets if row["source_year"] is not None}),
        # Compatibility for old saved generator URLs. The canonical browser now
        # exposes source kind directly, but this Boolean still answers whether a
        # problem has ever appeared on a university exam.
        ("sourced", "yes" if any(row["source_kind"] == "university-exam" for row in facets) else "no"),
    )


def _listing_sort(data: CardPageData, card: sqlite3.Row) -> str:
    """Where a card falls in its listing when nothing has been searched for.

    Browsing and searching want different orders, and a listing that has only
    relevance has no order at all until a reader types. This is the order the
    problem browser used to emit its rows in: by area, and within an area the
    titles that begin with prose before the ones that begin with mathematics,
    because `$` sorts ahead of every letter and the page opened on 483 formulas.
    """
    areas = " ".join(_page_terms(data, card["id"], "area"))
    return f"{areas}|{1 if card['title'].startswith('$') else 0}|{card['title']}"


def write_json_pages(
    pandoc: PandocServer,
    items: list[tuple[Path, dict, list, SearchDocument]],
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
        for _, _, blocks, _ in items
    ]
    bodies = _successful_outputs(
        pandoc.write_markdown(documents, MARKDOWN),
        "tag-page write",
    )
    html_bodies = _successful_html_outputs(
        pandoc.write_html(_html_asts(documents)),
        "tag-page HTML write",
    )
    for (path, meta, _, role), body, html_body in zip(
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
            StandardPage(role),
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


def _link_inline(
    card: sqlite3.Row,
    inline_cache: dict[str, list[pf.Inline]],
    base: str = "../",
) -> pf.Link:
    return pf.Link(
        *_inlines(card["title"], inline_cache),
        url=f"{base}{card['route']}/{card['id']}.html",
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
        select distinct e.institution, case when s.source_kind='exam' then s.year else null end as year
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

    uses = _rows(
        con,
        "select c.* from relations r join cards c on c.id=r.target_id where r.source_id=? and r.kind='uses'",
        (card["id"],),
    )
    if uses:
        blocks.append(pf.Header(pf.Str("Uses"), level=2))
        blocks.append(pf.BulletList(*[pf.ListItem(_link(u, inline_cache)) for u in uses]))

    meta: dict[str, object] = {
        "title": card["title"],
        "subtitle": card["id"],
        "area": ", ".join(a.replace("-", " ").title() for a in areas),
        "review": card["review"],
        "categories": sorted(set(topics + areas + institutions + years)),
    }
    if institutions:
        meta["institutions"] = ", ".join(institutions)
    if years:
        meta["years"] = ", ".join(years)
    return meta, blocks


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
    repo_root: Path,
) -> Page:
    listed = _rows(
        con,
        """
        select cp.section_ordinal, cp.section_name, cp.ordinal, cp.problem_id, cp.comment,
          listed.kind, listed.title, listed.route
        from collection_problems cp
        join cards listed on listed.id=cp.problem_id
        where cp.collection_id=?
        order by coalesce(cp.section_ordinal, -1), cp.ordinal
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
    return {"title": src["title"], "subtitle": src["id"]}, _collection_listing(
        src["id"],
        listed,
        inline_cache,
        completion,
        provenance,
        repo_root,
    )


def _pdf_extraction_href(repo_root: Path, href: str) -> str | None:
    """The checked-in Markdown extraction for one local provenance PDF.

    This is a filesystem fact, not a semantic inference. External URLs have no
    repository sibling. Local PDFs use one of the two established extraction
    spellings: `extracted/<stem>.md` or `<stem>_extracted.md`.
    """
    if href.startswith(("http://", "https://")):
        return None
    source = repo_root / href
    if source.suffix.lower() != ".pdf":
        return None
    candidates = (
        source.parent / "extracted" / f"{source.stem}.md",
        source.with_name(f"{source.stem}_extracted.md"),
    )
    for candidate in candidates:
        if candidate.is_file() and candidate.stat().st_size:
            return candidate.relative_to(repo_root).as_posix()
    return None


def _collection_listing(
    collection_id: str,
    listed: list[sqlite3.Row],
    inline_cache: dict[str, list[pf.Inline]],
    completion: str = "complete",
    provenance: list[str] | None = None,
    repo_root: Path | None = None,
) -> list[pf.Block]:
    """Render the collection's authored source-order contents.

    `source.problems` / `source.sections` is intrinsic collection data, not a
    metadata query. The collection page therefore materializes it directly.
    The central problem browser remains available as a supplementary searchable
    and printable view of the direct problem appearances.
    """

    def card_item(row: sqlite3.Row) -> pf.ListItem:
        inlines: list[pf.Inline] = [
            pf.Link(
                *_inlines(row["title"], inline_cache),
                url=f"../{row['route']}/{row['problem_id']}.html",
            )
        ]
        if row["comment"]:
            inlines.extend((pf.Space(), pf.Str("—"), pf.Space(), pf.Str(row["comment"])))
        return pf.ListItem(pf.Plain(*inlines))

    blocks: list[pf.Block] = []
    if completion == "incomplete":
        blocks.append(pf.Para(pf.Str("This collection is incomplete; listed items are a prefix of the source, and further extraction is pending.")))
    if provenance:
        blocks.append(pf.Header(pf.Str("Provenance"), level=2))
        provenance_items: list[pf.ListItem] = []
        for href in provenance:
            inlines: list[pf.Inline] = [pf.Link(pf.Str(href), url=href)]
            extraction = _pdf_extraction_href(repo_root, href) if repo_root is not None else None
            if extraction is not None:
                inlines.extend(
                    (
                        pf.Space(),
                        pf.Str("—"),
                        pf.Space(),
                        pf.Link(pf.Str("Markdown extraction"), url=extraction),
                    )
                )
            provenance_items.append(pf.ListItem(pf.Plain(*inlines)))
        blocks.append(pf.BulletList(*provenance_items))
    problem_count = sum(row["kind"] == "problem" for row in listed)
    blocks.append(
        pf.Para(
            pf.Str(str(problem_count)),
            pf.Space(),
            *_inlines("problems.", inline_cache),
        )
    )
    if listed:
        by_section: list[tuple[str | None, list[sqlite3.Row]]] = []
        for row in listed:
            name = row["section_name"]
            if not by_section or by_section[-1][0] != name:
                by_section.append((name, []))
            by_section[-1][1].append(row)

        for name, entries in by_section:
            if name:
                blocks.append(pf.Header(*_inlines(name, inline_cache), level=2))
            blocks.append(
                pf.Div(
                    pf.OrderedList(
                        *[card_item(row) for row in entries],
                        start=1,
                        style="Decimal",
                        delimiter="Period",
                    ),
                    classes=["qual-exam-listing"],
                )
            )
    if problem_count:
        blocks.append(
            pf.Div(
                pf.Para(
                    pf.Link(
                        pf.Str("Browse these problems in source order"),
                        url=_problem_browser_deep_link(collection=collection_id),
                    )
                ),
                classes=["panel", "problem-browse-link"],
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
                parent=NodeParent(manifest.id),
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
        trail = (
            *trail,
            Crumb(title=section.title, route=_publication_section_route(manifest, section)),
        )
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


def _problem_browser_deep_link(
    area: str = "",
    topics: tuple[str, ...] | list[str] = (),
    collection: str = "",
) -> str:
    """A site-root link into the one problem browser.

    Area/topics come from authored page classification; collection comes from
    a source page. Repeated topic parameters preserve the OR-family exactly.
    """
    params: list[tuple[str, str]] = []
    if area:
        params.append(("area", area))
    params.extend(("topic", topic) for topic in topics)
    if collection:
        params.append(("collection", collection))
    suffix = f"?{urlencode(params)}" if params else ""
    return f"problems.html{suffix}"


def _problem_browse_link_block(
    area: str,
    topics: tuple[str, ...] | list[str],
) -> pf.Block:
    """One derived problem-discovery link shared by guides and wiki pages.

    This does not execute the query or compute a count. The central browser owns
    the live result set and lets the reader refine, sample, and print it there.
    """
    if len(topics) == 1:
        focus = f" on {topics[0]}"
    elif topics:
        focus = " matching these topics"
    else:
        focus = ""
    return pf.Div(
        pf.Para(
            pf.Link(
                pf.Str(f"Browse the problems{focus}"),
                url=_problem_browser_deep_link(area=area, topics=topics),
            ),
        ),
        classes=["panel", "problem-browse-link"],
    )


def publication_section_page(
    con: sqlite3.Connection,
    manifest: PublicationManifest,
    section: PublicationSection,
    inline_cache: dict[str, list[pf.Inline]],
) -> Page:
    blocks: list[pf.Block] = [
        pf.Para(*_inlines(section.lede, inline_cache)),
    ]
    counts: Counter[str] = Counter()
    for item in section.items:
        blocks.append(_transclude(_manifest_card(con, item.ref), counts))
    if section.topics:
        blocks.append(_problem_browse_link_block(manifest.area, section.topics))
    return {"title": section.title}, blocks


def card_source_collections(
    con: sqlite3.Connection,
) -> dict[str, list[Appearance]]:
    """Collections that list this problem."""
    sources: dict[str, list[Appearance]] = {row["id"]: [] for row in _rows(con, "select id from cards order by id")}
    for row in _rows(
        con,
        """
        select cp.problem_id, cp.collection_id, cp.ordinal, cp.comment, c.title
        from collection_problems cp
        join cards c on c.id=cp.collection_id
        order by c.title, coalesce(cp.section_ordinal, -1), cp.ordinal
        """,
    ):
        locator = row["comment"] or f"problem {row['ordinal'] + 1}"
        sources[row["problem_id"]].append(
            Appearance(
                target_key=row["collection_id"],
                title=f"{row['title']}, {locator}",
            )
        )
    return sources


def card_guide_appearances(
    con: sqlite3.Connection,
    manifests: list[PublicationManifest],
) -> dict[str, list[Appearance]]:
    """Guide sections that explicitly reference this card."""
    guide_appearances: dict[str, list[Appearance]] = {row["id"]: [] for row in _rows(con, "select id from cards order by id")}
    for manifest in manifests:
        for section in manifest.sections:
            target_key = _publication_section_target_key(manifest, section)
            surfaced = [item.ref for item in section.items]
            for card_id in surfaced:
                _manifest_card(con, card_id)
            for card_id in dict.fromkeys(surfaced):
                guide_appearances[card_id].append(
                    Appearance(
                        target_key=target_key,
                        title=section.title,
                    )
                )
    return guide_appearances


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
          (select count(*) from cards where kind='problem') as asked,
          (select count(*) from exam_sources) as sittings,
          (select count(distinct institution) from exam_sources) as institutions,
          (select count(*) from cards where kind='problem'
             and id in (select card_id from sections where section_kind = 'solution')) as solved
        """,
    )[0]
    intro = (
        f"Past qualifying-exam problems, with the sources and notes to work them. "
        f"{scale['asked']:,} problems, from {scale['sittings']:,} exam sittings "
        f"at {scale['institutions']} institutions and from textbooks, homework sets and compiled scans. "
        f"{scale['solved']:,} carry a written solution.\n\n"
    )
    links = (
        "## Where to start\n\n"
        "[Problems](problems.html)\n"
        ": Every problem, with live topic/source filters plus random sampling and print/PDF.\n\n"
        "[Exams](exams.html)\n"
        ": Each sitting as it was sat, problem by problem.\n\n"
        "[Guides](guides.html)\n"
        ": One ordered path per subject, built from the same problems. Read front to back:\n"
        "  a section assumes only the sections above it.\n\n"
        "[Wiki](wiki/index.html)\n"
        ": Written notes filed by subject. Look one topic up rather than read a path.\n"
    )
    output = _successful_outputs(
        pandoc.read_markdown(
            [intro + links],
            MARKDOWN,
        ),
        "index-page read",
    )
    return {"title": "Qual Corpus"}, list(from_ast(output[0]).content)


# Separates multi-valued facet terms in HTML data attributes. Topics are free
# strings and may contain spaces, so space is not a usable delimiter.
DATATABLES_ASSETS = """
<link rel="stylesheet" href="https://cdn.datatables.net/2.3.8/css/dataTables.dataTables.min.css">
<link rel="stylesheet" href="https://cdn.datatables.net/searchpanes/2.3.5/css/searchPanes.dataTables.min.css">
<link rel="stylesheet" href="https://cdn.datatables.net/select/3.1.3/css/select.dataTables.min.css">
<link rel="stylesheet" href="https://cdn.datatables.net/rowgroup/1.6.0/css/rowGroup.dataTables.min.css">
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script src="https://cdn.datatables.net/2.3.8/js/dataTables.min.js"></script>
<script src="https://cdn.datatables.net/select/3.1.3/js/dataTables.select.min.js"></script>
<script src="https://cdn.datatables.net/searchpanes/2.3.5/js/dataTables.searchPanes.min.js"></script>
<script src="https://cdn.datatables.net/rowgroup/1.6.0/js/dataTables.rowGroup.min.js"></script>
"""


def _data_table(table_id: str, headings: tuple[str, ...]) -> pf.RawBlock:
    """One standard DataTables shell; rows and controls are library-owned."""
    header = "".join(f"<th>{html.escape(heading)}</th>" for heading in headings)
    return pf.RawBlock(
        DATATABLES_ASSETS
        + f'<table id="{html.escape(table_id, quote=True)}" class="display catalog-table" style="width:100%">'
        + f"<thead><tr>{header}</tr></thead></table>"
        + '<script src="assets/scripts/catalog-tables.js"></script>',
        format="html",
    )


def _practice_controls() -> pf.RawBlock:
    return pf.RawBlock(
        '<div class="practice-actions">'
        '<label for="practice-count">Random sample'
        '<input id="practice-count" type="number" min="1" max="100" value="8"></label>'
        '<button id="practice-sample" type="button">Sample from filtered rows</button>'
        '<button id="practice-print" type="button" disabled>Print / PDF sample</button>'
        "</div>"
        '<section id="practice-sheet" class="practice-sheet" hidden></section>',
        format="html",
    )


def problem_browser_page(
    con: sqlite3.Connection,
    area_names: dict[str, str],
) -> Page:
    """The one problem browser, rendered by DataTables + SearchPanes."""
    del con, area_names
    return {"title": "Problems"}, [
        pf.Para(pf.Str("Every problem in the corpus. Filter with the facet panes, search or paginate the table, or draw a printable random sample from the filtered rows.")),
        _practice_controls(),
        _data_table(
            "problem-table",
            ("Problem", "Source", "Topics", "Area", "Source type", "Institution", "Year", "Collection", "Section", "Order"),
        ),
    ]


def collection_problem_index(
    con: sqlite3.Connection,
    data: CardPageData,
) -> dict[str, dict[str, object]]:
    """Ordered source appearances used lazily by the central problem browser."""
    collections: dict[str, dict[str, object]] = {}
    rows = _rows(
        con,
        """
        select cp.collection_id, cp.section_ordinal, cp.section_name, cp.ordinal, cp.problem_id, cp.comment,
          source.title as collection_title, problem.title as problem_title, s.source_kind, s.year, e.institution
        from collection_problems cp
        join cards source on source.id=cp.collection_id
        join cards problem on problem.id=cp.problem_id and problem.kind='problem'
        join sources s on s.id=cp.collection_id
        left join exam_sources e on e.id=s.id
        order by cp.collection_id, coalesce(cp.section_ordinal, -1), cp.ordinal
        """,
    )
    for row in rows:
        collection_id = row["collection_id"]
        if collection_id not in collections:
            collections[collection_id] = {
                "title": row["collection_title"],
                "items": [],
            }
        filters: dict[str, list[str]] = {
            "area": _page_terms(data, row["problem_id"], "area"),
            "topic": _page_terms(data, row["problem_id"], "topic"),
            "source_kind": [row["source_kind"]],
            "collection": [collection_id],
        }
        if row["institution"]:
            filters["institution"] = [row["institution"].upper()]
        if row["year"] is not None:
            filters["year"] = [str(row["year"])]
        locator = row["comment"] or f"Problem {row['ordinal'] + 1}"
        items = collections[collection_id]["items"]
        assert isinstance(items, list)
        items.append(
            {
                "id": row["problem_id"],
                "url": f"tag/{row['problem_id']}.html",
                "meta": {
                    "title": row["problem_title"],
                    "collection_title": row["collection_title"],
                    "collection_section": row["section_name"] or "",
                    "collection_locator": locator,
                },
                "filters": filters,
            }
        )
    return collections


def problem_table_data(
    con: sqlite3.Connection,
    data: CardPageData,
    area_names: dict[str, str],
) -> dict[str, object]:
    """Problem rows for DataTables; all interactive behavior stays in the library."""
    collection_names = {row["id"]: row["title"] for row in _rows(con, "select id, title from cards where kind='collection'")}
    rows: list[dict[str, object]] = []
    for card in _rows(con, "select * from cards where kind='problem' order by id"):
        facets = _page_rows(data.facets, card["id"])
        area_ids = _page_terms(data, card["id"], "area")
        topics = _page_terms(data, card["id"], "topic")
        source_kinds = sorted({row["source_kind"] for row in facets})
        institutions = sorted({row["institution"].upper() for row in facets if row["institution"]})
        years = sorted({str(row["source_year"]) for row in facets if row["source_year"] is not None})
        collections = sorted({collection_names[row["collection_id"]] for row in facets})
        source_bits = institutions or [SOURCE_KIND_HEADINGS[kind] for kind in source_kinds]
        if years:
            source_bits = [*source_bits, ", ".join(years)]
        rows.append(
            {
                "id": card["id"],
                "title": card["title"],
                "url": f"tag/{card['id']}.html",
                "source": " · ".join(source_bits) if source_bits else "Unclassified",
                "topics": topics,
                "areas": [area_names[area] for area in area_ids],
                "sourceKinds": [SOURCE_KIND_HEADINGS[kind] for kind in source_kinds],
                "institutions": institutions,
                "years": years,
                "collections": collections,
                "section": "",
                "order": _listing_sort(data, card),
            }
        )
    return {
        "areaNames": area_names,
        "sourceKindNames": SOURCE_KIND_HEADINGS,
        "collectionNames": collection_names,
        "rows": rows,
    }


def source_table_data(
    con: sqlite3.Connection,
    data: CardPageData,
    area_names: dict[str, str],
) -> dict[str, object]:
    """Source rows for the standard source catalog table."""
    rows: list[dict[str, object]] = []
    sources = _rows(
        con,
        f"""
        select c.id, c.title, c.route, s.source_kind, s.year, s.term,
          coalesce(e.institution, '') as institution,
          coalesce(e.area, '') as exam_area,
          {TERM_RANK} as term_rank,
          (select count(*) from collection_problems cp where cp.collection_id=c.id) as problems,
          (select count(*) from collection_problems cp
             where cp.collection_id=c.id
               and cp.problem_id in (select card_id from sections where section_kind='solution')) as solved
        from cards c join sources s on s.id=c.id
        left join exam_sources e on e.id=s.id
        order by c.id
        """,
    )
    for row in sources:
        area_ids = _page_terms(data, row["id"], "area")
        rows.append(
            {
                "id": row["id"],
                "title": row["title"],
                "url": f"{row['route']}/{row['id']}.html",
                "sourceKind": SOURCE_KIND_HEADINGS[row["source_kind"]],
                "areas": [area_names[area] for area in area_ids],
                "institution": row["institution"].upper() if row["institution"] else "",
                "year": str(row["year"]) if row["year"] is not None else "",
                "worked": f"{row['solved']} / {row['problems']} solved" if row["problems"] else "No problems listed",
                "order": f"{list(SOURCE_KIND_HEADINGS).index(row['source_kind']):02d}|{row['institution']}|{row['year'] or 0:04d}|{row['term_rank']}|{row['exam_area']}",
            }
        )
    return {"areaNames": area_names, "sourceKindNames": SOURCE_KIND_HEADINGS, "rows": rows}


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


ACROSS_SUBJECTS_LEDE = (
    "Not a subject. These read the same problems the subject guides do, in a different order, "
    "so a subject appears in both and neither is a copy of the other. "
    "The wiki files each of these pages under the subject it belongs to."
)


def _guide_sections(
    guides: list[PublicationManifest],
    area_names: dict[str, str],
    inline_cache: dict[str, list[pf.Inline]],
) -> list[pf.Block]:
    """The subject guides, then the guides that cross subjects rather than being one.

    A guide's id names its subject -- that is how its problem-browser deep links are
    scoped -- so whether it is a subject is already recorded and does not
    become a field an author can forget.
    """

    def listing(chosen: list[PublicationManifest]) -> pf.BulletList:
        return pf.BulletList(
            *[
                pf.ListItem(
                    pf.Plain(pf.Link(pf.Str(guide.title), url=f"guide/{guide.id}.html")),
                    pf.Para(*_inlines(guide.lede, inline_cache)),
                )
                for guide in chosen
            ]
        )

    subjects = [guide for guide in guides if guide.area in area_names]
    crossing = [guide for guide in guides if guide.area not in area_names]
    blocks: list[pf.Block] = [listing(subjects)]
    if crossing:
        blocks.append(pf.Header(pf.Str("Across the subjects"), level=2))
        blocks.append(pf.Para(*_inlines(ACROSS_SUBJECTS_LEDE, inline_cache)))
        blocks.append(listing(crossing))
    return blocks


def source_index_page(
    con: sqlite3.Connection,
    area_names: dict[str, str],
) -> Page:
    """Every collection the corpus draws from, under the kind of thing it is.

    The page listed only the 338 sittings. The other 43 -- 20 compiled scans, 17
    homework sets, 6 textbooks -- had no listing anywhere, and the largest
    collection on the site, Munkres with 586 problems, was among them: a reader
    reached it only from a problem card.
    """
    collections = _rows(
        con,
        """
        select s.source_kind, s.year,
          coalesce(e.institution, '') as institution,
          coalesce(e.area, '') as area
        from cards c join sources s on s.id=c.id
        left join exam_sources e on e.id=s.id
        """,
    )
    unlisted = {row["source_kind"] for row in collections} - set(SOURCE_KIND_HEADINGS)
    if unlisted:
        raise ValueError(f"source kinds with no heading on the source index: {sorted(unlisted)}")

    del area_names
    blocks: list[pf.Block] = [
        pf.Para(pf.Str(f"Every collection the corpus draws problems from: {len(collections)} in all.")),
        _data_table("source-table", ("Source", "Type", "Area", "Institution", "Year", "Worked", "Order")),
    ]
    return {"title": "Sources"}, blocks


# --- project ----------------------------------------------------------------

QUARTO_YML = {
    "project": {"type": "website", "output-dir": "_site"},
    "website": {
        "title": "Qual Corpus",
        "navbar": {
            "left": [
                {"href": "index.qmd", "text": "Home"},
                {"href": "problems.qmd", "text": "Problems"},
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
    # rewrites the DOM that exists when the page opens, so the central problem
    # browser's sampled practice sheet, injected on demand, never got the wrapper and its
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
        "    chtml: { scale: 0.95, matchFontHeight: true },\n"
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
    for card in _rows(con, "select id, route from cards"):
        add(card["id"], Path(card["route"]) / f"{card['id']}.html")
    for guide in guides:
        add(_publication_root_target_key(guide), _publication_root_route(guide))
        for section in guide.sections:
            add(
                _publication_section_target_key(guide, section),
                _publication_section_route(guide, section),
            )
    return targets


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
    (out / "source").mkdir()
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
    # ETBook font files for Tufte-style typography.
    fonts_src = site / "fonts"
    if fonts_src.is_dir():
        fonts_dst = site_root / "fonts"
        fonts_dst.mkdir(exist_ok=True)
        for f in fonts_src.iterdir():
            if f.suffix == ".woff":
                shutil.copy(f, fonts_dst / f.name)

    guides = load_publications(publications)
    link_targets = _link_targets(con, guides)
    link_targets.update(wiki_link_targets(wiki_pages or []))
    (out / "wiki-manifest.json").write_text(json.dumps(_wiki_manifest(wiki_pages or []), ensure_ascii=False, indent=2) + "\n")
    source_collections = card_source_collections(con)
    guide_appearances = card_guide_appearances(con, guides)
    mentions = wiki_card_mentions(wiki_pages or [])
    incoming_pages = incoming_wiki_links(wiki_pages or [])
    assets = build_asset_catalog(site.parent / "assets")
    area_names = load_areas(site.parent / "wiki")
    inline_values = [row["title"] for row in _rows(con, "select distinct title from cards")]
    inline_values.extend(
        [
            "problems.",
            ("Assembled from a publication manifest: an ordered list of stable IDs and queries. Reordering it touches no card and no catalog row."),
            "Every problem in the corpus.",
            f"Every collection the corpus draws problems from: {len(_rows(con, 'select id from sources'))} in all.",
            GUIDES_LEDE,
            ACROSS_SUBJECTS_LEDE,
        ]
    )
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
    (site_root / "collection-problems.json").write_text(json.dumps(collection_problem_index(con, card_page_data), ensure_ascii=False, separators=(",", ":")) + "\n")
    (site_root / "problems.json").write_text(json.dumps(problem_table_data(con, card_page_data, area_names), ensure_ascii=False, separators=(",", ":")) + "\n")
    (site_root / "sources.json").write_text(json.dumps(source_table_data(con, card_page_data, area_names), ensure_ascii=False, separators=(",", ":")) + "\n")
    tag_pages: list[tuple[Path, dict, list, SearchDocument]] = []
    for card in _rows(con, "select * from cards where kind='problem'"):
        meta, body = asked_json(
            card_page_data,
            card,
            jcache,
            source_collections,
            guide_appearances,
            mentions,
        )
        document = SearchDocument(
            _card_filters(card_page_data, card),
            sort=(("listing", _listing_sort(card_page_data, card)),),
        )
        tag_pages.append((out / "tag" / f"{card['id']}.qmd", meta, body, document))
    for card in _rows(con, "select * from cards where kind not in ('problem','collection')"):
        meta, body = plain_json(
            card_page_data,
            card,
            jcache,
            source_collections,
            guide_appearances,
            mentions,
        )
        document = SearchDocument(
            _card_filters(card_page_data, card),
            sort=(("listing", _listing_sort(card_page_data, card)),),
        )
        tag_pages.append((out / "tag" / f"{card['id']}.qmd", meta, body, document))
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
    # How much of a collection is worked is what a reader picking one is after,
    # and the index cannot count it: it is carried as page metadata.
    collection_facts = {
        row["id"]: (
            row["source_kind"],
            f"{row['problems']} problems, {row['solved']} solved" if row["problems"] else "no problems listed",
            f"{list(SOURCE_KIND_HEADINGS).index(row['source_kind']):02d}|{row['institution']}|{row['year'] or 0:04d}|{row['term_rank']}|{row['area']}",
        )
        for row in _rows(
            con,
            f"""
            select s.id, s.source_kind,
              coalesce(e.institution, '') as institution, coalesce(e.area, '') as area, s.year,
              {TERM_RANK} as term_rank,
              (select count(*) from collection_problems where collection_id=s.id) as problems,
              (select count(*) from collection_problems cp
               where cp.collection_id=s.id
                 and cp.problem_id in (select card_id from sections where section_kind='solution')) as solved
            from sources s left join exam_sources e on e.id=s.id
            """,
        )
    }
    for src in _rows(con, "select * from cards where kind='collection'"):
        kind, worked, order = collection_facts.get(src["id"], ("", "", ""))
        pages.append(
            (
                collection_page(con, src, inline_cache, site.parent),
                out / src["route"] / f"{src['id']}.qmd",
                StandardPage(
                    SearchDocument(
                        _card_filters(
                            card_page_data,
                            src,
                            (("source_kind", kind),) if kind else (),
                        ),
                        (("worked", worked),) if worked else (),
                        (("listing", order),),
                    )
                ),
            )
        )

    # `generate.html` was the old second query implementation. Keep the route so
    # saved links do not break, but immediately forward its filters into the one
    # canonical problem browser and request the old default eight-item sample.
    generate_qmd = """---
title: Practice problems
---

Practice generation now lives in the [problem browser](problems.html).
"""
    (out / "generate.qmd").write_text(generate_qmd)
    generate_html = (
        '<p>Practice generation now lives in the <a href="problems.html">problem browser</a>.</p>'
        '<script>(function(){const target=new URL("problems.html",document.baseURI);'
        "const source=new URLSearchParams(location.search);for(const [key,value] of source)target.searchParams.append(key,value);"
        'if(!target.searchParams.has("sample"))target.searchParams.set("sample","8");location.replace(target.href);})();</script>'
    )
    write_page(
        site_root,
        Path("generate.html"),
        {"title": "Practice problems"},
        generate_html,
        mathjax,
        link_targets,
        assets,
        StandardPage(Listing()),
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
            problem_browser_page(con, area_names),
            out / "problems.qmd",
            StandardPage(Listing()),
        ),
    )
    pages.append(
        (
            source_index_page(con, area_names),
            out / "exams.qmd",
            StandardPage(Listing()),
        ),
    )
    pages.append(
        (
            (
                {"title": "Guides"},
                [
                    pf.Para(*_inlines(GUIDES_LEDE, inline_cache)),
                    # Each guide states what it is in its manifest and the list
                    # showed none of it: bare subject names, the same ones the
                    # wiki offers, with nothing to choose between them.
                    #
                    # A guide whose id names an area is a subject. Workshops is
                    # not one, and listing it beside the six read as a seventh
                    # subject -- which is why Guides and the wiki appeared to
                    # disagree about what the subjects are. The wiki files each
                    # workshop week under the subject it belongs to, correctly;
                    # the guide crosses them on purpose, and says so here.
                    *_guide_sections(guides, area_names, inline_cache),
                ],
            ),
            out / "guides.qmd",
            StandardPage(Listing()),
        ),
    )
    pages.append((index_page(pandoc, con), out / "index.qmd", StandardPage(Listing())))
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
                    _wiki_blocks(
                        page,
                        incoming_pages[page.route.as_posix()],
                        cards,
                        set(area_names),
                    ),
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
    con.close()
