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
from dataclasses import dataclass
from pathlib import Path
from typing import cast
from urllib.parse import unquote, urlsplit

import panflute as pf
import yaml

from .diagnostics import Diagnostic
from .model import MARKDOWN, drop_path_captions, from_ast
from .pandoc_batch import PandocFailure, PandocServer
from .static_site import AssetCatalog, _asset_source

WIKI_BATCH_SIZE = 8
IMAGE_ELEMENT = cast(type[pf.Element], vars(pf)["Image"])



@dataclass
class WikiPage:
    source_path: Path
    source_rel: Path
    route: Path
    title: str
    blocks: list[pf.Block]
    search_text: str


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


def parse_pages(pandoc: PandocServer, root: Path) -> tuple[list[WikiPage], list[Diagnostic]]:
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
    for offset in range(0, len(prepared), WIKI_BATCH_SIZE):
        batch = prepared[offset : offset + WIKI_BATCH_SIZE]
        results = pandoc.read_markdown([body for _, _, _, body in batch], MARKDOWN)
        for (path, source_rel, metadata, _), result in zip(batch, results, strict=True):
            if isinstance(result, PandocFailure):
                errors.append(Diagnostic("card-unreadable", str(path), result.error))
                continue
            warnings = [message.message for message in result.messages if message.verbosity == "WARNING"]
            if warnings:
                errors.append(Diagnostic("reader-warning", str(path), "; ".join(warnings)))
                continue
            document = from_ast(result.output).walk(drop_path_captions)
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
    return parsed, errors


class MissingPageReference(ValueError):
    def __init__(self, raw: str) -> None:
        self.raw = raw
        super().__init__(f"missing wiki page reference: {raw}")


class AmbiguousPageReference(ValueError):
    def __init__(self, raw: str) -> None:
        self.raw = raw
        super().__init__(f"ambiguous wiki page reference: {raw}")


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
            target = _page_target(page, path, by_key, by_normalized, by_stem).route.as_posix()
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
