"""Authored wiki-page ingestion and reference resolution.

The corpus cards and the authored wiki are different source domains.  Cards own
stable mathematical identities; wiki pages own prose, source hierarchy, and the
positions where card references occur.  This module keeps those identities
separate while making the page boundary fail loudly on missing or ambiguous
local references.
"""

from __future__ import annotations

import posixpath
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import cast
from urllib.parse import unquote, urlsplit

import panflute as pf
import yaml

from .diagnostics import Diagnostic
from .model import MARKDOWN, drop_path_captions, from_ast
from .pandoc_batch import Citations, PandocFailure, PandocServer
from .static_site import AssetCatalog, _asset_source

WIKI_BATCH_SIZE = 8
IMAGE_ELEMENT = cast(type[pf.Element], vars(pf)["Image"])


def load_citations(root: Path) -> Citations:
    """The BibTeX the authored wiki cites, and the style its references are set in."""
    return Citations(
        bibliography=(root / "references.bib").read_text(),
        style=(root / "citation-style.csl").read_text(),
    )


# citeproc reports a key no entry defines as a warning and renders it as
# `**key?**`, which would reach the page. The message is the only place the key
# is named, so the warning is classified rather than the AST inspected.
CITEPROC_MISSING = "Citeproc: citation "

# Pandoc records the citeproc request in the document's metadata, so a page's
# stringified text ends `references.bibstyle.csl` and every page in the search
# index matches a search for either name. They describe the request, not the page.
CITEPROC_METADATA = ("bibliography", "csl")


def _citation_diagnostic(warning: str, path: Path) -> Diagnostic:
    if warning.startswith(CITEPROC_MISSING):
        return Diagnostic("unknown-citation", str(path), warning)
    return Diagnostic("reader-warning", str(path), warning)


@dataclass
class WikiPage:
    source_path: Path
    source_rel: Path
    route: Path
    title: str
    blocks: list[pf.Block]
    search_text: str


# Obsidian anchors a block by putting `^<id>` on the line after it. Pandoc has
# no such syntax and reads it as an ordinary paragraph, so the marker reached the
# page as literal text and every `...#^<id>` link into it dangled.
BLOCK_MARKER = re.compile(r"\A\^[0-9a-zA-Z]+\Z")


def anchor_block_markers(element: pf.Element, doc: pf.Doc) -> pf.Element | pf.RawBlock:
    """Turn a block-id marker paragraph into the anchor it was standing in for.

    The anchor keeps the marker's own spelling, `^<id>`, so the authored links
    resolve as written instead of every one of them needing a rewrite.
    """
    del doc
    if not isinstance(element, pf.Para) or len(element.content) != 1:
        return element
    head = element.content[0]
    if not isinstance(head, pf.Str) or not BLOCK_MARKER.match(head.text):
        return element
    return pf.RawBlock(f'<span id="{head.text}"></span>', format="html")


# `\cref[label]{text}` is a LaTeX cross-reference. Pandoc reads it as raw TeX
# and the HTML writer drops raw TeX whole, so both the reference and the words
# it was made of left the page -- ten of them as empty list items.
CREF = re.compile(r"\\cref\[([^\]]*)\]\{([^}]*)\}")


def _text_inlines(text: str) -> list[pf.Inline]:
    parts = text.split(" ")
    inlines: list[pf.Inline] = []
    for index, part in enumerate(parts):
        if index:
            inlines.append(pf.Space())
        if part:
            inlines.append(pf.Str(part))
    return inlines


def unpack_cross_references(element: pf.Element, doc: pf.Doc) -> pf.Element | list[pf.Inline]:
    """Replace a `\\cref` with the words it displays.

    It is not turned into a link. The labels these name -- `CauchyTheorem` and
    the like -- are defined nowhere: `\\label{}` does not occur in `wiki/` at
    all, so there is no target to resolve against, and choosing which page each
    one meant is a reading decision rather than a transport one. The text is
    restored and `parse_pages` names every one it restored.
    """
    del doc
    if not isinstance(element, pf.RawInline) or cast(str, getattr(element, "format")) != "tex":
        return element
    match = CREF.fullmatch(cast(str, getattr(element, "text")).strip())
    if match is None:
        return element
    return _text_inlines(match.group(2))


def discover(root: Path) -> list[Path]:
    """Return the complete authored page inventory in deterministic order."""

    if not root.is_dir():
        return []
    return sorted(root.rglob("*.md"))


def _split_front_matter(text: str, path: Path) -> tuple[dict[str, object], str]:
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        raise ValueError(f"{path}: unterminated YAML front matter")
    metadata = yaml.safe_load(parts[1])
    if metadata is None:
        metadata = {}
    if not isinstance(metadata, dict):
        raise TypeError(f"{path}: page front matter must be a mapping")
    return metadata, parts[2]


def _title(document: pf.Doc, metadata: dict[str, object], path: Path) -> str:
    value = metadata.get("title")
    if isinstance(value, str) and value.strip():
        return value.strip()
    for block in document.content:
        if isinstance(block, pf.Header) and block.level == 1:
            return pf.stringify(block).strip()
    return path.stem.replace("_", " ")


def _without_first_title(document: pf.Doc) -> list[pf.Block]:
    blocks = list(document.content)
    for index, block in enumerate(blocks):
        if isinstance(block, pf.Header) and block.level == 1:
            del blocks[index]
            break
    return blocks


def parse_pages(pandoc: PandocServer, root: Path, citations: Citations) -> tuple[list[WikiPage], list[Diagnostic]]:
    """Parse all source pages through the same Pandoc dialect as cards.

    Wiki pages can be much larger than cards, so requests are intentionally kept
    small.  The page inventory remains complete; chunking only changes transport.
    """

    paths = discover(root)
    prepared: list[tuple[Path, Path, dict[str, object], str]] = []
    errors: list[Diagnostic] = []
    for path in paths:
        try:
            metadata, body = _split_front_matter(path.read_text(), path)
            prepared.append((path, path.relative_to(root), metadata, body))
        except (OSError, TypeError, ValueError, yaml.YAMLError) as exc:
            errors.append(Diagnostic("card-unreadable", str(path), str(exc)))

    parsed: list[WikiPage] = []
    restored: list[str] = []
    for offset in range(0, len(prepared), WIKI_BATCH_SIZE):
        batch = prepared[offset : offset + WIKI_BATCH_SIZE]
        results = pandoc.read_markdown([body for _, _, _, body in batch], MARKDOWN, citations)
        for (path, source_rel, metadata, body), result in zip(batch, results, strict=True):
            if isinstance(result, PandocFailure):
                errors.append(Diagnostic("card-unreadable", str(path), result.error))
                continue
            warnings = [message.message for message in result.messages if message.verbosity == "WARNING"]
            if warnings:
                errors.extend(_citation_diagnostic(warning, path) for warning in warnings)
                continue
            restored.extend(f"{source_rel.as_posix()}: \\cref[{label}]" for label, _ in CREF.findall(body))
            document = (
                from_ast(result.output)
                .walk(drop_path_captions)
                .walk(anchor_block_markers)
                .walk(unpack_cross_references)
            )
            for key in CITEPROC_METADATA:
                document.metadata.content.pop(key, None)
            parsed.append(
                WikiPage(
                    source_path=path,
                    source_rel=source_rel,
                    route=Path("wiki") / source_rel.with_suffix(".html"),
                    title=_title(document, metadata, path),
                    blocks=_without_first_title(document),
                    search_text=pf.stringify(document).strip(),
                )
            )
    if restored:
        print(
            f"{len(restored)} cross-reference(s) restored as plain text; no \\label defines their targets:",
            file=sys.stderr,
        )
        for entry in restored:
            print(f"  {entry}", file=sys.stderr)
    return parsed, errors


class MissingPageReference(ValueError):
    def __init__(self, raw: str) -> None:
        self.raw = raw
        super().__init__(f"missing wiki page reference: {raw}")


class AmbiguousPageReference(ValueError):
    def __init__(self, raw: str) -> None:
        self.raw = raw
        super().__init__(f"ambiguous wiki page reference: {raw}")


def _resolved_or_dropped(page: WikiPage, fragment: str, unresolved: list[str]) -> str:
    """The fragment under the id the target page emits, or nothing at all.

    A fragment naming no heading and no anchor is an authored reference to a
    block that is not there. The page half of the link is still right, so the
    link keeps working and loses only its fragment; which block was meant is a
    reading decision, and inventing one here would be a guess. Every one is
    named on stderr instead.
    """
    ids, by_text = _page_anchors(page)
    if fragment in ids:
        return f"#{fragment}"
    slug = by_text.get(_fragment_key(fragment))
    if slug is not None:
        return f"#{slug}"
    unresolved.append(f"{page.source_rel.as_posix()}#{fragment}")
    return ""


# Pandoc's smart punctuation turns the apostrophe in a heading into `’`, and the
# link into that heading is still typed with `'`. The two spell one heading.
SMART_PUNCTUATION = str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"', "–": "-", "—": "-"})


def _fragment_key(value: str) -> str:
    return value.translate(SMART_PUNCTUATION).strip().casefold()


def _page_anchors(page: WikiPage) -> tuple[set[str], dict[str, str]]:
    """The ids the page emits, and its heading text under the id Pandoc gave it.

    Obsidian addresses a heading by its text, `[[Page#Green's Theorem]]`, and
    Pandoc addresses it by a slug, `greens-theorem`. Reading the id off the
    parsed header is exact; re-deriving the slug from the text would be a guess
    at Pandoc's algorithm.
    """
    ids: set[str] = set()
    by_text: dict[str, str] = {}

    def collect(element: pf.Element, doc: pf.Doc) -> pf.Element:
        del doc
        if isinstance(element, pf.Header) and element.identifier:
            ids.add(element.identifier)
            by_text[_fragment_key(pf.stringify(element))] = element.identifier
        elif isinstance(element, pf.RawBlock):
            found = re.search(r'id="([^"]+)"', cast(str, getattr(element, "text")))
            if found:
                ids.add(found.group(1))
        return element

    pf.Doc(*page.blocks).walk(collect)
    return ids, by_text


def _normal_key(value: str) -> str:
    key = unquote(value).replace("\\", "/")
    if key.startswith("wiki/"):
        key = key.removeprefix("wiki/")
    return posixpath.normpath(key)


def _normalized_path(value: str) -> str:
    return "/".join(re.sub(r"[ _]+", "_", part).casefold() for part in value.split("/"))


def _page_indexes(
    pages: list[WikiPage],
) -> tuple[dict[str, WikiPage], dict[str, list[WikiPage]], dict[str, list[WikiPage]]]:
    by_key: dict[str, WikiPage] = {}
    by_normalized: dict[str, list[WikiPage]] = {}
    by_stem: dict[str, list[WikiPage]] = {}

    def add(mapping: dict[str, list[WikiPage]], key: str, page: WikiPage) -> None:
        if key not in mapping:
            mapping[key] = []
        mapping[key].append(page)

    for page in pages:
        relative = page.source_rel.as_posix()
        without_suffix = page.source_rel.with_suffix("").as_posix()
        by_key[relative] = page
        by_key[without_suffix] = page
        by_key[relative.lower()] = page
        by_key[without_suffix.lower()] = page
        add(by_normalized, _normalized_path(relative), page)
        add(by_normalized, _normalized_path(without_suffix), page)
        add(by_stem, page.source_rel.stem, page)
        add(by_stem, page.source_rel.stem.lower(), page)
    return by_key, by_normalized, by_stem


def _page_target(
    page: WikiPage,
    raw: str,
    by_key: dict[str, WikiPage],
    by_normalized: dict[str, list[WikiPage]],
    by_stem: dict[str, list[WikiPage]],
) -> WikiPage:
    key = _normal_key(urlsplit(raw).path)
    if key.endswith(".html"):
        key = key.removesuffix(".html")
    exact_candidates = [key]
    if not key.endswith(".md"):
        exact_candidates.append(f"{key}.md")
    relative = page.source_rel.parent.as_posix()
    if relative != ".":
        exact_candidates.extend(
            [
                posixpath.normpath(posixpath.join(relative, key)),
                posixpath.normpath(posixpath.join(relative, f"{key}.md")),
            ]
        )
    matches = []
    for candidate in exact_candidates:
        target = by_key.get(candidate) or by_key.get(candidate.lower())
        if target is not None and target not in matches:
            matches.append(target)
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        raise AmbiguousPageReference(raw)
    normalized_matches: list[WikiPage] = []
    for candidate in exact_candidates:
        key = _normalized_path(candidate)
        targets = by_normalized[key] if key in by_normalized else []
        for target in targets:
            if target not in normalized_matches:
                normalized_matches.append(target)
    if len(normalized_matches) == 1:
        return normalized_matches[0]
    if len(normalized_matches) > 1:
        raise AmbiguousPageReference(raw)
    stem = Path(key).stem
    candidates: list[WikiPage] = []
    for stem_key in (stem, stem.lower()):
        if stem_key in by_stem:
            candidates.extend(by_stem[stem_key])
    unique: list[WikiPage] = []
    for candidate_page in candidates:
        if candidate_page not in unique:
            unique.append(candidate_page)
    if len(unique) == 1:
        return unique[0]
    if len(unique) > 1:
        raise AmbiguousPageReference(raw)
    raise MissingPageReference(raw)


def _asset_target(raw: str, assets: AssetCatalog) -> Path:
    source = _asset_source(raw, assets)
    return Path("assets") / source.relative_to(assets.root)


def _canonical_target(
    page: WikiPage,
    raw: str,
    card_routes: dict[str, Path],
    by_key: dict[str, WikiPage],
    by_normalized: dict[str, list[WikiPage]],
    by_stem: dict[str, list[WikiPage]],
    assets: AssetCatalog,
    unresolved: list[str],
) -> str:
    parsed = urlsplit(raw)
    if parsed.scheme or parsed.netloc or raw.startswith(("#", "data:", "mailto:")):
        return raw
    path = parsed.path
    card_key = Path(_normal_key(path)).stem
    if path.startswith("tag/"):
        card_key = Path(path).stem
    if card_key in card_routes:
        target = card_routes[card_key].as_posix()
    else:
        suffix = Path(_normal_key(path)).suffix.lower()
        if suffix and suffix not in {".md", ".html"}:
            target = _asset_target(path, assets).as_posix()
        else:
            destination = _page_target(page, path, by_key, by_normalized, by_stem)
            target = destination.route.as_posix()
            if parsed.fragment:
                return target + _resolved_or_dropped(destination, unquote(parsed.fragment), unresolved)
    if parsed.fragment:
        target += f"#{parsed.fragment}"
    return target


def resolve_links(
    pages: list[WikiPage],
    card_routes: dict[str, Path],
    assets: AssetCatalog,
) -> list[Diagnostic]:
    """Resolve every local page/card/asset link in-place; return failures."""

    by_key, by_normalized, by_stem = _page_indexes(pages)
    errors: list[Diagnostic] = []
    unresolved: list[str] = []

    def visit(page: WikiPage, element: pf.Element) -> pf.Element:
        if isinstance(element, pf.Link) or isinstance(element, IMAGE_ELEMENT):
            raw = cast(str, getattr(element, "url"))
            try:
                target = _canonical_target(
                    page,
                    raw,
                    card_routes,
                    by_key,
                    by_normalized,
                    by_stem,
                    assets,
                    unresolved,
                )
                if isinstance(element, IMAGE_ELEMENT) and target.startswith(("wiki/", "tag/", "exam/", "guide/")):
                    element = pf.Link(
                        *cast(list[pf.Inline], element.content),
                        url=target,
                        title=cast(str, getattr(element, "title")),
                    )
                else:
                    setattr(element, "url", target)
            except MissingPageReference as exc:
                errors.append(Diagnostic("page-reference-missing", str(page.source_path), str(exc)))
            except AmbiguousPageReference as exc:
                errors.append(Diagnostic("page-reference-ambiguous", str(page.source_path), str(exc)))
            except (OSError, ValueError) as exc:
                errors.append(Diagnostic("asset-unresolved", str(page.source_path), str(exc)))
        if hasattr(element, "content"):
            element.content = [visit(page, child) if isinstance(child, pf.Element) else child for child in element.content]
        return element

    for page in pages:
        page.blocks = [cast(pf.Block, visit(page, block)) for block in page.blocks]
    if unresolved:
        print(
            f"{len(unresolved)} reference(s) kept their page and dropped a fragment naming no block:",
            file=sys.stderr,
        )
        for entry in sorted(set(unresolved)):
            print(f"  {entry}", file=sys.stderr)
    return errors


def link_targets(pages: list[WikiPage]) -> dict[str, Path]:
    return {page.route.as_posix(): page.route for page in pages}


def search_records(pages: list[WikiPage]) -> list[dict[str, object]]:
    return [
        {
            "title": page.title,
            "kind": "Page",
            "detail": "authored wiki page",
            "url": page.route.as_posix(),
            "search": f"{page.title} {page.source_rel} {page.search_text}".lower(),
        }
        for page in pages
    ]
