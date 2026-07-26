"""Shared HTML shell for the compiler's direct static-site projection."""

from __future__ import annotations

import json
import os
import posixpath
import re
from dataclasses import dataclass
from html import escape
from pathlib import Path
from typing import Literal
from urllib.parse import unquote, urlsplit


@dataclass(frozen=True)
class AssetCatalog:
    root: Path
    by_name: dict[str, tuple[Path, ...]]


@dataclass(frozen=True)
class RootParent:
    pass


@dataclass(frozen=True)
class NodeParent:
    key: str


NavigationParent = RootParent | NodeParent


@dataclass(frozen=True)
class NavigationLink:
    key: str
    title: str
    target: Path
    parent: NavigationParent


@dataclass(frozen=True)
class StartReading:
    following: NavigationLink


@dataclass(frozen=True)
class MiddleReading:
    previous: NavigationLink
    following: NavigationLink


@dataclass(frozen=True)
class EndReading:
    previous: NavigationLink


ReadingPosition = StartReading | MiddleReading | EndReading


@dataclass(frozen=True)
class PublicationNavigation:
    links: tuple[NavigationLink, ...]
    current_key: str
    position: ReadingPosition


@dataclass(frozen=True)
class StandardPage:
    pass


@dataclass(frozen=True)
class SubjectPage:
    navigation: PublicationNavigation


PageChrome = StandardPage | SubjectPage


def build_asset_catalog(root: Path) -> AssetCatalog:
    by_name: dict[str, list[Path]] = {}
    for path in root.rglob("*"):
        if path.is_file():
            if path.name not in by_name:
                by_name[path.name] = []
            by_name[path.name].append(path)
    return AssetCatalog(
        root=root,
        by_name={name: tuple(paths) for name, paths in by_name.items()},
    )


def _prefix(relative_path: Path) -> str:
    if relative_path.parent == Path("."):
        return ""
    return "../" * len(relative_path.parent.parts)


def _metadata(meta: dict[str, object]) -> str:
    labels = {
        "area": "Area",
        "institutions": "Seen at",
        "years": "Years",
        "review": "Status",
    }
    rows = []
    for key, label in labels.items():
        value = meta.get(key)
        if isinstance(value, str) and value:
            rows.append(f'<div class="page-fact"><dt>{escape(label)}</dt><dd>{escape(value)}</dd></div>')
    if not rows:
        return ""
    return '<dl class="page-facts">' + "".join(rows) + "</dl>"


def _relative_url(relative_path: Path, target: Path) -> str:
    start = relative_path.parent.as_posix()
    if start == ".":
        start = ""
    return posixpath.relpath(target.as_posix(), start=start or ".")


def _navigation_link(
    relative_path: Path,
    link: NavigationLink,
) -> str:
    target = escape(_relative_url(relative_path, link.target))
    return f'<a href="{target}">{escape(link.title)}</a>'


def _current_navigation_link(
    relative_path: Path,
    link: NavigationLink,
) -> str:
    target = escape(_relative_url(relative_path, link.target))
    return f'<a href="{target}" aria-current="page">{escape(link.title)}</a>'


def _reading_navigation_link(
    relative_path: Path,
    link: NavigationLink,
    relation: Literal["prev", "next"],
) -> str:
    target = escape(_relative_url(relative_path, link.target))
    return f'<a href="{target}" rel="{relation}">{escape(link.title)}</a>'


def _subject_tree(
    relative_path: Path,
    navigation: PublicationNavigation,
) -> str:
    roots: list[NavigationLink] = []
    children: dict[str, list[NavigationLink]] = {link.key: [] for link in navigation.links}
    for link in navigation.links:
        match link.parent:
            case RootParent():
                roots.append(link)
            case NodeParent(key=parent_key):
                children[parent_key].append(link)

    def branch(links: list[NavigationLink]) -> str:
        items = []
        for link in links:
            nested = branch(children[link.key])
            anchor = _current_navigation_link(relative_path, link) if link.key == navigation.current_key else _navigation_link(relative_path, link)
            items.append("<li>" + anchor + nested + "</li>")
        return f"<ol>{''.join(items)}</ol>" if items else ""

    return f'<aside class="subject-sidebar"><nav aria-label="Subject"><strong class="subject-label">Study path</strong>{branch(roots)}</nav></aside>'


def _breadcrumbs(
    relative_path: Path,
    navigation: PublicationNavigation,
) -> str:
    by_key = {link.key: link for link in navigation.links}
    trail = []
    cursor = by_key[navigation.current_key]
    while True:
        trail.append(cursor)
        match cursor.parent:
            case RootParent():
                break
            case NodeParent(key=parent_key):
                cursor = by_key[parent_key]
    trail.reverse()
    return (
        '<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>'
        + "".join(
            "<li>" + (_current_navigation_link(relative_path, link) if link.key == navigation.current_key else _navigation_link(relative_path, link)) + "</li>"
            for link in trail
        )
        + "</ol></nav>"
    )


def _reading_order(
    relative_path: Path,
    navigation: PublicationNavigation,
) -> str:
    match navigation.position:
        case StartReading(following=following):
            links = [
                '<span class="reading-following"><small>Next</small>'
                + _reading_navigation_link(
                    relative_path,
                    following,
                    "next",
                )
                + "</span>"
            ]
        case MiddleReading(previous=previous, following=following):
            links = [
                '<span class="reading-previous"><small>Previous</small>'
                + _reading_navigation_link(
                    relative_path,
                    previous,
                    "prev",
                )
                + "</span>",
                '<span class="reading-following"><small>Next</small>'
                + _reading_navigation_link(
                    relative_path,
                    following,
                    "next",
                )
                + "</span>",
            ]
        case EndReading(previous=previous):
            links = [
                '<span class="reading-previous"><small>Previous</small>'
                + _reading_navigation_link(
                    relative_path,
                    previous,
                    "prev",
                )
                + "</span>"
            ]
    return '<nav class="reading-order" aria-label="Reading order">' + "".join(links) + "</nav>"


def _asset_source(raw_url: str, catalog: AssetCatalog) -> Path:
    decoded = unquote(urlsplit(raw_url).path)
    parts = Path(decoded).parts
    if "assets" in parts:
        suffix = parts[parts.index("assets") + 1 :]
        exact = catalog.root.joinpath(*suffix)
        if exact.is_file():
            return exact
    direct = catalog.root / decoded.lstrip("./")
    if direct.is_file():
        return direct
    name = Path(decoded).name
    canonical = catalog.root / "figures" / name
    if canonical.is_file():
        return canonical
    if name not in catalog.by_name:
        raise ValueError(f"referenced asset does not exist: {raw_url}")
    matches = catalog.by_name[name]
    if len(matches) == 1:
        return matches[0]
    raise ValueError(f"referenced asset is ambiguous: {raw_url} matches " + ", ".join(str(path) for path in matches))


def _rewrite_body(
    site_root: Path,
    relative_path: Path,
    body: str,
    link_targets: dict[str, Path],
    assets: AssetCatalog,
) -> str:
    pattern = re.compile(r'(?P<attribute>href|src)="(?P<url>[^"]+)"')

    def replace(match: re.Match[str]) -> str:
        attribute = match.group("attribute")
        raw_url = match.group("url")
        parsed = urlsplit(raw_url)
        if parsed.scheme or parsed.netloc or raw_url.startswith(("#", "data:", "mailto:")):
            return match.group(0)
        if attribute == "href" and parsed.path in link_targets:
            target = link_targets[parsed.path]
            rewritten = _relative_url(relative_path, target)
            if parsed.fragment:
                rewritten += f"#{parsed.fragment}"
            return f'href="{escape(rewritten, quote=True)}"'
        if attribute == "src":
            source = _asset_source(raw_url, assets)
            target = Path("assets") / source.relative_to(assets.root)
            destination = site_root / target
            destination.parent.mkdir(parents=True, exist_ok=True)
            if not destination.exists():
                os.link(source, destination)
            rewritten = _relative_url(relative_path, target)
            return f'src="{escape(rewritten, quote=True)}"'
        return match.group(0)

    return pattern.sub(replace, body)


def page_document(
    relative_path: Path,
    meta: dict[str, object],
    body: str,
    mathjax_header: str,
    chrome: PageChrome,
) -> str:
    prefix = _prefix(relative_path)
    try:
        raw_title = meta["title"]
    except KeyError:
        raw_title = "Qual Corpus"
    title = raw_title if isinstance(raw_title, str) else "Qual Corpus"
    raw_subtitle = meta.get("subtitle")
    subtitle = raw_subtitle if isinstance(raw_subtitle, str) else ""
    subtitle_html = f'<p class="page-subtitle">{escape(subtitle)}</p>' if subtitle else ""
    match chrome:
        case StandardPage():
            subject_html = ""
            breadcrumb_html = ""
            reading_order_html = ""
            layout_class = "page-layout"
        case SubjectPage(navigation=navigation):
            subject_html = _subject_tree(relative_path, navigation)
            breadcrumb_html = _breadcrumbs(relative_path, navigation)
            reading_order_html = _reading_order(relative_path, navigation)
            layout_class = "page-layout subject-layout"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="generator" content="qualc">
  <title>{escape(title)} · Qual Corpus</title>
  <link rel="icon" href="data:,">
  <link rel="stylesheet" href="{prefix}styles.css">
  {mathjax_header}
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js"></script>
  <script defer src="{prefix}app.js"></script>
</head>
<body data-search-index="{prefix}search.json">
  <header class="site-header">
    <nav class="site-nav" aria-label="Primary">
      <a class="site-brand" href="{prefix}index.html">Qual Corpus</a>
      <div class="site-links">
        <a href="{prefix}problems.html">Browse</a>
        <a href="{prefix}generate.html">Generate</a>
        <a href="{prefix}exams.html">Exams</a>
        <a href="{prefix}guides.html">Guides</a>
      </div>
      <button id="search-open" class="search-open" type="button" aria-haspopup="dialog">
        Search <kbd>/</kbd>
      </button>
    </nav>
  </header>
  <dialog id="site-search" class="search-dialog" aria-labelledby="search-title">
    <div class="search-heading">
      <h2 id="search-title">Search the corpus</h2>
      <button id="search-close" type="button" aria-label="Close search">×</button>
    </div>
    <input id="site-search-input" type="search" autocomplete="off"
           placeholder="Titles, statements, proofs, topics…">
    <ol id="site-search-results"></ol>
  </dialog>
  <div class="{layout_class}">
    {subject_html}
    <main id="main-content">
      <header class="page-heading">
        {breadcrumb_html}
        <h1>{escape(title)}</h1>
        {subtitle_html}
        {_metadata(meta)}
      </header>
      <article class="page-body">
        {body}
      </article>
      {reading_order_html}
    </main>
    <aside id="page-toc" class="page-toc" aria-label="On this page"></aside>
  </div>
</body>
</html>
"""


def write_page(
    site_root: Path,
    relative_path: Path,
    meta: dict[str, object],
    body: str,
    mathjax_header: str,
    link_targets: dict[str, Path],
    assets: AssetCatalog,
    chrome: PageChrome,
) -> None:
    path = site_root / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    rewritten = _rewrite_body(
        site_root,
        relative_path,
        body,
        link_targets,
        assets,
    )
    path.write_text(
        page_document(
            relative_path,
            meta,
            rewritten,
            mathjax_header,
            chrome,
        )
    )


def write_search_index(site_root: Path, records: list[dict[str, object]]) -> None:
    (site_root / "search.json").write_text(json.dumps(records, ensure_ascii=False, separators=(",", ":")))
