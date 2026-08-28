"""Shared HTML shell for the site pages."""

from __future__ import annotations

import json
import os
import posixpath
import re
from dataclasses import dataclass
from html import escape
from pathlib import Path
from typing import Literal, assert_never
from urllib.parse import quote, unquote, urlsplit


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
class PageTarget:
    """A node a reader can open: a route to link to."""

    route: Path


@dataclass(frozen=True)
class LevelOnly:
    """A directory in the authored wiki. It names a level of the trail and has
    no page of its own, so it is read in a breadcrumb but never linked to."""


NavigationTarget = PageTarget | LevelOnly


@dataclass(frozen=True)
class NavigationLink:
    key: str
    title: str
    target: NavigationTarget
    parent: NavigationParent


@dataclass(frozen=True)
class ReadingLink:
    """Somewhere reading goes next. Always a page: a directory is not readable.

    Reading runs on past the end of a folder, so the link's place in the tree
    travels with it: that is what lets the previous and next links say which
    section they land in when it is not the one being read.
    """

    title: str
    target: PageTarget
    key: str
    parent: NavigationParent

    @staticmethod
    def of(link: NavigationLink) -> ReadingLink:
        match link.target:
            case LevelOnly():
                raise ValueError(f"reading order points at a directory: {link.key}")
            case PageTarget() as target:
                return ReadingLink(title=link.title, target=target, key=link.key, parent=link.parent)


@dataclass(frozen=True)
class StartReading:
    following: ReadingLink


@dataclass(frozen=True)
class MiddleReading:
    previous: ReadingLink
    following: ReadingLink


@dataclass(frozen=True)
class EndReading:
    previous: ReadingLink


@dataclass(frozen=True)
class OnlyReading:
    pass


ReadingPosition = StartReading | MiddleReading | EndReading | OnlyReading


@dataclass(frozen=True)
class Crumb:
    """One step of where a page is filed, for the breadcrumb."""

    title: str
    route: Path


@dataclass(frozen=True)
class PublicationNavigation:
    links: tuple[NavigationLink, ...]
    current_key: str
    position: ReadingPosition
    # Where this page is filed, from the listing that owns it down to the page
    # itself. Stated by the caller rather than walked out of `parent`, because
    # `parent` means one thing in the wiki (the folder above) and another in a
    # guide (the section this one assumes), and a breadcrumb that means either
    # depending on the page means neither.
    trail: tuple[Crumb, ...]


@dataclass(frozen=True)
class StandardPage:
    pass


@dataclass(frozen=True)
class SubjectPage:
    navigation: PublicationNavigation


@dataclass(frozen=True)
class AuthoredPage:
    """A wiki page with its authored hierarchy and reading order."""

    navigation: PublicationNavigation


@dataclass(frozen=True)
class NotFoundPage:
    """The page a server returns for a URL that names no page.

    Written once at the site root, served for a request at any depth. The
    browser resolves this page's relative links against the URL the reader
    asked for, not against the file, so every other page's `../` arithmetic is
    wrong here. A `<base>` naming the site root repairs all of them at once,
    and only this page needs one.

    The site root is `/<repo>/` on a GitHub Pages project site and `/` under
    any other host, including the local preview server. That is the same rule
    `spa-github-pages` uses for the same reason:
    https://github.com/rafgraph/spa-github-pages
    """


PageChrome = StandardPage | SubjectPage | AuthoredPage | NotFoundPage

SITE_ROOT_BASE = """<script>
    var root = location.hostname.endsWith(".github.io") ? "/" + location.pathname.split("/")[1] + "/" : "/";
    document.head.appendChild(Object.assign(document.createElement("base"), {href: root}));
  </script>"""


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
    """The href, percent-encoded, for a target file whose name may hold spaces.

    `Berkeley Prelims.md` is an authored filename and stays one; a literal space
    in a URL is not. Encoding here rather than at the route covers every href
    and src on the site, because navigation, body links and assets all leave
    through this one function, and it leaves the routes themselves comparable
    as plain paths.
    """
    start = relative_path.parent.as_posix()
    if start == ".":
        start = ""
    return quote(posixpath.relpath(target.as_posix(), start=start or "."), safe="/")


def _navigation_link(
    relative_path: Path,
    link: NavigationLink,
) -> str:
    match link.target:
        case LevelOnly():
            return f"<span>{escape(link.title)}</span>"
        case PageTarget(route=route):
            target = escape(_relative_url(relative_path, route))
            return f'<a href="{target}">{escape(link.title)}</a>'


def _current_navigation_link(
    relative_path: Path,
    link: NavigationLink,
) -> str:
    match link.target:
        case LevelOnly():
            return f'<span aria-current="page">{escape(link.title)}</span>'
        case PageTarget(route=route):
            target = escape(_relative_url(relative_path, route))
            return f'<a href="{target}" aria-current="page">{escape(link.title)}</a>'


def _reading_navigation_link(
    relative_path: Path,
    link: ReadingLink,
    relation: Literal["prev", "next"],
    navigation: PublicationNavigation,
) -> str:
    target = escape(_relative_url(relative_path, link.target.route))
    anchor = f'<a href="{target}" rel="{relation}">{escape(link.title)}</a>'
    return anchor + _crossing(link, navigation)


def _crossing(link: ReadingLink, navigation: PublicationNavigation) -> str:
    """Names the section a reading link lands in, when it leaves this one.

    Reading order runs on past the end of a folder. From Algebra > Quals the
    previous page was `Final Exam`, three folders away under Exercises, and the
    link said only `Final Exam`.

    Silent between a page and its own siblings, its own folder, and the pages
    inside it. None of those is a crossing.
    """
    by_key = {node.key: node for node in navigation.links}
    here = by_key[navigation.current_key].parent
    if link.parent in (here, NodeParent(navigation.current_key)) or NodeParent(link.key) == here:
        return ""
    trail: list[str] = []
    cursor = link.parent
    while True:
        match cursor:
            case RootParent():
                break
            case NodeParent(key=parent_key):
                trail.append(by_key[parent_key].title)
                cursor = by_key[parent_key].parent
            case _ as unreachable:
                assert_never(unreachable)
    if not trail:
        return ""
    return f'<span class="reading-section">in {escape(" / ".join(reversed(trail)))}</span>'


def _subject_tree(
    relative_path: Path,
    navigation: PublicationNavigation,
) -> str:
    roots, children = _navigation_structure(navigation)

    def branch(links: list[NavigationLink]) -> str:
        items: list[str] = []
        for link in links:
            nested = branch(children[link.key])
            anchor = _current_navigation_link(relative_path, link) if link.key == navigation.current_key else _navigation_link(relative_path, link)
            items.append("<li>" + anchor + nested + "</li>")
        return f"<ol>{''.join(items)}</ol>" if items else ""

    tree = branch(roots)
    return (
        '<aside class="subject-sidebar">'
        '<nav class="sidebar-wide" aria-label="Subject">'
        f'<strong class="subject-label">Study path</strong>{tree}</nav>'
        '<details class="sidebar-narrow"><summary>Study path</summary>'
        f'<nav aria-label="Subject navigation">{tree}</nav></details></aside>'
    )


def _navigation_structure(
    navigation: PublicationNavigation,
) -> tuple[list[NavigationLink], dict[str, list[NavigationLink]]]:
    roots: list[NavigationLink] = []
    children: dict[str, list[NavigationLink]] = {link.key: [] for link in navigation.links}
    for link in navigation.links:
        match link.parent:
            case RootParent():
                roots.append(link)
            case NodeParent(key=parent_key):
                children[parent_key].append(link)
            case _ as unreachable:
                assert_never(unreachable)
    return roots, children


def _wiki_tree(
    relative_path: Path,
    navigation: PublicationNavigation,
) -> str:
    roots, children = _navigation_structure(navigation)
    by_key = {link.key: link for link in navigation.links}
    open_directories: set[str] = set()
    cursor = by_key[navigation.current_key]
    while True:
        match cursor.parent:
            case RootParent():
                break
            case NodeParent(key=parent_key):
                open_directories.add(parent_key)
                cursor = by_key[parent_key]
            case _ as unreachable:
                assert_never(unreachable)

    def branch(links: list[NavigationLink]) -> str:
        items: list[str] = []
        for link in links:
            match link.target:
                case LevelOnly():
                    nested = branch(children[link.key])
                    assert nested, f"wiki directory has no pages: {link.key}"
                    open_attribute = " open" if link.key in open_directories else ""
                    items.append(f"<li><details{open_attribute}><summary>{escape(link.title)}</summary>{nested}</details></li>")
                case PageTarget():
                    anchor = _current_navigation_link(relative_path, link) if link.key == navigation.current_key else _navigation_link(relative_path, link)
                    if children[link.key]:
                        # The folder's own page is the summary. Writing the
                        # title in the summary and again as the first child put
                        # the same word on two lines, one to expand and one to
                        # navigate, with nothing to tell them apart. A link is
                        # interactive content, so clicking it follows it and
                        # leaves the disclosure alone; the marker still toggles.
                        open_attribute = " open" if link.key in open_directories or link.key == navigation.current_key else ""
                        nested = branch(children[link.key])
                        items.append(f"<li><details{open_attribute}><summary>{anchor}</summary>{nested}</details></li>")
                    else:
                        items.append("<li>" + anchor + "</li>")
                case _ as unreachable:
                    assert_never(unreachable)
        return f"<ol>{''.join(items)}</ol>" if items else ""

    tree = branch(roots)
    return (
        '<aside class="subject-sidebar wiki-sidebar">'
        '<nav class="sidebar-wide" aria-label="Wiki">'
        f'<strong class="subject-label">Wiki</strong>{tree}</nav>'
        '<details class="sidebar-narrow"><summary>Wiki navigation</summary>'
        f'<nav aria-label="Wiki navigation">{tree}</nav></details></aside>'
    )


def _breadcrumbs(
    relative_path: Path,
    navigation: PublicationNavigation,
) -> str:
    def crumb(step: Crumb, last: bool) -> str:
        target = escape(_relative_url(relative_path, step.route))
        current = ' aria-current="page"' if last else ""
        return f'<li><a href="{target}"{current}>{escape(step.title)}</a></li>'

    steps = navigation.trail
    # A page that is its own root has nowhere to go up to, and a one-item
    # breadcrumb only repeats the heading under it.
    if len(steps) < 2:
        return ""
    return '<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>' + "".join(crumb(step, index == len(steps) - 1) for index, step in enumerate(steps)) + "</ol></nav>"


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
                    navigation,
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
                    navigation,
                )
                + "</span>",
                '<span class="reading-following"><small>Next</small>'
                + _reading_navigation_link(
                    relative_path,
                    following,
                    "next",
                    navigation,
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
                    navigation,
                )
                + "</span>"
            ]
        case OnlyReading():
            return ""
        case _ as unreachable:
            assert_never(unreachable)
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

    def asset_url(raw_url: str) -> tuple[Path, str]:
        source = _asset_source(raw_url, assets)
        target = Path("assets") / source.relative_to(assets.root)
        destination = site_root / target
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists():
            os.link(source, destination)
        return target, _relative_url(relative_path, target)

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
        if attribute == "href" and parsed.path.startswith("assets/"):
            _, rewritten = asset_url(raw_url)
            if parsed.fragment:
                rewritten += f"#{parsed.fragment}"
            return f'href="{escape(rewritten, quote=True)}"'
        if attribute == "src":
            _, rewritten = asset_url(raw_url)
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
            base_html = ""
            subject_html = ""
            breadcrumb_html = ""
            reading_order_html = ""
            layout_class = "page-layout"
        case NotFoundPage():
            base_html = SITE_ROOT_BASE
            subject_html = ""
            breadcrumb_html = ""
            reading_order_html = ""
            layout_class = "page-layout"
        case SubjectPage(navigation=navigation):
            base_html = ""
            subject_html = _subject_tree(relative_path, navigation)
            breadcrumb_html = _breadcrumbs(relative_path, navigation)
            reading_order_html = _reading_order(relative_path, navigation)
            layout_class = "page-layout subject-layout"
        case AuthoredPage(navigation=navigation):
            base_html = ""
            subject_html = _wiki_tree(relative_path, navigation)
            breadcrumb_html = _breadcrumbs(relative_path, navigation)
            reading_order_html = _reading_order(relative_path, navigation)
            layout_class = "page-layout subject-layout"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="generator" content="qualc">
  {base_html}
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
        <a href="{prefix}exams.html">Sources</a>
        <a href="{prefix}guides.html">Guides</a>
        <a href="{prefix}wiki/index.html">Wiki</a>
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
