"""Collection `provenance` lists: empty lists, unresolved hrefs, hrefs listed
on more than one collection, hrefs whose path is a markdown file, hrefs whose
path is an image file, hrefs whose path is under a forbidden source tree, and
collections whose area appears on no problem or exercise card.

Named for exactly what it measured. Empty provenance is the YAML list as written,
not a finding that no source exists. A dead href is the GET status or missing
file, not a decision that the sitting is wrong. A shared href is the same string
on two or more collections' lists, not a decision that the collections should be
one card. A markdown href is a path or URL whose last suffix is `.md` or
`.markdown`, not a decision that the file is an importer wrapper. An image href
is a path or URL whose last suffix is an image extension, not a decision that
no exam paper exists. A collection area without problem cards is that area on
no `problem` or `exercise` card, not a decision that the sitting should be
deleted. It is not wired to `qualc check`, `just test`, or the build: a finding
is a candidate, never an instruction to act.

    just provenance
    uv run python -m qualc.provenance_hrefs
    uv run python -m qualc.provenance_hrefs --json
    uv run python -m qualc.provenance_hrefs --only empty-provenance
    uv run python -m qualc.provenance_hrefs --only dead-provenance-hrefs
    uv run python -m qualc.provenance_hrefs --only shared-provenance-hrefs
    uv run python -m qualc.provenance_hrefs --only markdown-provenance-hrefs
    uv run python -m qualc.provenance_hrefs --only image-provenance-hrefs
    uv run python -m qualc.provenance_hrefs --only forbidden-provenance-hrefs
    uv run python -m qualc.provenance_hrefs --only collection-area-without-problem-cards
"""

from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from http.client import InvalidURL
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml

from qualc.model import discover, split_front_matter

REPO = Path(__file__).resolve().parent.parent
USER_AGENT = "qualc-provenance-hrefs/0.1"
WORKERS = 8
DEFAULT_TIMEOUT = 20.0


@dataclass
class Check:
    name: str
    findings: list[str] = field(default_factory=list)
    measured: int = 0
    unit: str = "hrefs"

    @property
    def ok(self) -> bool:
        return not self.findings


PROBLEM_KINDS = frozenset({"problem", "exercise"})


@dataclass(frozen=True)
class CollectionProvenance:
    card_id: str
    hrefs: list[str]
    areas: tuple[str, ...] = ()


IMAGE_SUFFIXES = frozenset({".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".tif", ".tiff"})

FORBIDDEN_PROVENANCE_MARKERS: tuple[tuple[str, str], ...] = (
    ("make-me-a-qual", "dzackgarza repo copy"),
    ("qual-review-and-solutions", "compiled notes"),
    ("qual-wiki", "wiki copy"),
    ("qualbot-question-images", "note screenshot"),
    ("Combined_Questions.yaml", "importer wrapper"),
    ("Combined_Questions.pdf", "importer wrapper"),
)


def _normalized_href(href: str) -> str:
    path = urlparse(href).path if _is_http_href(href) else href
    return unquote(path).lower()


def _forbidden_provenance_reason(href: str) -> str | None:
    text = _normalized_href(href)
    if text.startswith("wiki/") or "/wiki/" in text:
        return "wiki"
    if "dzackgarza" in href.lower():
        return "dzackgarza repository"
    for marker, reason in FORBIDDEN_PROVENANCE_MARKERS:
        if marker.lower() in text:
            return reason
    return None


def _is_http_href(href: str) -> bool:
    return href.startswith(("http://", "https://"))


def _is_markdown_href(href: str) -> bool:
    path = urlparse(href).path if _is_http_href(href) else href
    return Path(unquote(path)).suffix.lower() in {".md", ".markdown"}


def _is_image_href(href: str) -> bool:
    path = urlparse(href).path if _is_http_href(href) else href
    return Path(unquote(path)).suffix.lower() in IMAGE_SUFFIXES


def _card_id(meta: dict[object, object], path: Path) -> str:
    card_id = meta.get("id")
    if isinstance(card_id, str) and card_id:
        return card_id
    return path.stem


def _hrefs(raw: object) -> list[str] | None:
    if raw is None:
        return []
    if not isinstance(raw, list):
        return None
    return [item.strip() for item in raw if isinstance(item, str) and item.strip()]


def _areas(meta: dict[object, object]) -> tuple[str, ...]:
    found: list[str] = []
    classification = meta.get("classification")
    if isinstance(classification, dict):
        areas = classification.get("areas")
        if isinstance(areas, list):
            found.extend(area for area in areas if isinstance(area, str) and area)
    source = meta.get("source")
    if isinstance(source, dict):
        area = source.get("area")
        if isinstance(area, str) and area:
            found.append(area)
    return tuple(dict.fromkeys(found))


def load_corpus_provenance(
    root: Path,
) -> tuple[list[CollectionProvenance], set[str]]:
    """Collection provenance lists and areas that appear on problem cards.

    Origin notes belong in `::: remark` blocks, not in frontmatter. A non-list
    collection `provenance` value is skipped; `qualc check` already rejects that
    shape. Problem areas are `classification.areas` and `source.area` on exam,
    homework, and compilation cards.
    """
    collections: list[CollectionProvenance] = []
    problem_areas: set[str] = set()
    corpus = root / "corpus"
    if not corpus.is_dir():
        return collections, problem_areas
    for path in discover(corpus):
        try:
            meta, _body = split_front_matter(path.read_text(), path)
        except (OSError, TypeError, ValueError, yaml.YAMLError) as exc:
            raise ValueError(f"{path}: {exc}") from exc
        kind = meta.get("kind")
        if kind in PROBLEM_KINDS:
            problem_areas.update(_areas(meta))
            continue
        if kind != "collection":
            continue
        hrefs = _hrefs(meta.get("provenance"))
        if hrefs is None:
            continue
        collections.append(CollectionProvenance(_card_id(meta, path), hrefs, _areas(meta)))
    return collections, problem_areas


def load_collection_provenance(root: Path) -> list[CollectionProvenance]:
    collections, _problem_areas = load_corpus_provenance(root)
    return collections


def collection_provenance_hrefs(root: Path) -> list[tuple[str, str]]:
    return [(collection.card_id, href) for collection in load_collection_provenance(root) for href in collection.hrefs]


def http_get_status(url: str, *, timeout: float) -> int | str:
    base_headers = {
        "User-Agent": USER_AGENT,
        "Accept": "*/*",
    }
    # A 416 under `Range: bytes=0-0` means the server rejected the ranged
    # probe itself; retry once without the header to get the real status.
    status = _http_get_status(url, timeout=timeout, headers={**base_headers, "Range": "bytes=0-0"})
    if status == 416:
        return _http_get_status(url, timeout=timeout, headers=base_headers)
    return status


def _http_get_status(url: str, *, timeout: float, headers: dict[str, str]) -> int | str:
    request = urllib.request.Request(url, method="GET", headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            status: int = response.status
            return status
    except urllib.error.HTTPError as exc:
        return exc.code
    except urllib.error.URLError as exc:
        return f"error: {exc.reason}"
    except TimeoutError:
        return "error: timeout"
    except InvalidURL as exc:
        return f"error: {exc}"


def _http_live(status: int | str) -> bool:
    return isinstance(status, int) and 200 <= status < 300


def check_empty_provenance(collections: list[CollectionProvenance]) -> Check:
    findings = [collection.card_id for collection in collections if not collection.hrefs]
    return Check(
        "empty-provenance",
        sorted(findings),
        measured=len(collections),
        unit="collections",
    )


def check_dead_provenance_hrefs(collections: list[CollectionProvenance], *, root: Path, timeout: float) -> Check:
    targets = [(collection.card_id, href) for collection in collections for href in collection.hrefs]
    http_targets = [(card_id, href) for card_id, href in targets if _is_http_href(href)]
    path_targets = [(card_id, href) for card_id, href in targets if not _is_http_href(href)]
    unique_urls = list(dict.fromkeys(href for _card_id, href in http_targets))
    statuses: dict[str, int | str] = {}
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        pending = {pool.submit(http_get_status, url, timeout=timeout): url for url in unique_urls}
        for future in as_completed(pending):
            url = pending[future]
            statuses[url] = future.result()
    findings = [f"{card_id}: {href} -> {statuses[href]}" for card_id, href in http_targets if not _http_live(statuses[href])]
    findings.extend(f"{card_id}: {href} -> not a file" for card_id, href in path_targets if not (root / href).is_file())
    return Check("dead-provenance-hrefs", sorted(findings), measured=len(targets))


def check_shared_provenance_hrefs(collections: list[CollectionProvenance]) -> Check:
    owners: dict[str, set[str]] = defaultdict(set)
    for collection in collections:
        for href in collection.hrefs:
            owners[href].add(collection.card_id)
    findings = [f"{href}: {', '.join(sorted(card_ids))}" for href, card_ids in owners.items() if len(card_ids) > 1]
    return Check(
        "shared-provenance-hrefs",
        sorted(findings),
        measured=len(owners),
        unit="hrefs",
    )


def check_markdown_provenance_hrefs(collections: list[CollectionProvenance]) -> Check:
    findings = [f"{collection.card_id}: {href}" for collection in collections for href in collection.hrefs if _is_markdown_href(href)]
    return Check(
        "markdown-provenance-hrefs",
        sorted(findings),
        measured=sum(len(collection.hrefs) for collection in collections),
    )


def check_image_provenance_hrefs(collections: list[CollectionProvenance]) -> Check:
    findings = [f"{collection.card_id}: {href}" for collection in collections for href in collection.hrefs if _is_image_href(href)]
    return Check(
        "image-provenance-hrefs",
        sorted(findings),
        measured=sum(len(collection.hrefs) for collection in collections),
    )


def check_forbidden_provenance_hrefs(
    collections: list[CollectionProvenance],
) -> Check:
    findings = [f"{collection.card_id}: {href} ({reason})" for collection in collections for href in collection.hrefs if (reason := _forbidden_provenance_reason(href))]
    return Check(
        "forbidden-provenance-hrefs",
        sorted(findings),
        measured=sum(len(collection.hrefs) for collection in collections),
    )


def check_collection_area_without_problem_cards(collections: list[CollectionProvenance], problem_areas: set[str]) -> Check:
    findings = [f"{collection.card_id}: {area}" for collection in collections for area in collection.areas if area not in problem_areas]
    return Check(
        "collection-area-without-problem-cards",
        sorted(findings),
        measured=len(collections),
        unit="collections",
    )


ALL = [
    "empty-provenance",
    "dead-provenance-hrefs",
    "shared-provenance-hrefs",
    "markdown-provenance-hrefs",
    "image-provenance-hrefs",
    "forbidden-provenance-hrefs",
    "collection-area-without-problem-cards",
]


def run(names: list[str], *, root: Path = REPO, timeout: float = DEFAULT_TIMEOUT) -> list[Check]:
    collections, problem_areas = load_corpus_provenance(root)
    checks: list[Check] = []
    for name in names:
        if name == "empty-provenance":
            checks.append(check_empty_provenance(collections))
        elif name == "dead-provenance-hrefs":
            checks.append(check_dead_provenance_hrefs(collections, root=root, timeout=timeout))
        elif name == "shared-provenance-hrefs":
            checks.append(check_shared_provenance_hrefs(collections))
        elif name == "markdown-provenance-hrefs":
            checks.append(check_markdown_provenance_hrefs(collections))
        elif name == "image-provenance-hrefs":
            checks.append(check_image_provenance_hrefs(collections))
        elif name == "forbidden-provenance-hrefs":
            checks.append(check_forbidden_provenance_hrefs(collections))
        elif name == "collection-area-without-problem-cards":
            checks.append(check_collection_area_without_problem_cards(collections, problem_areas))
    return checks


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="provenance_hrefs")
    ap.add_argument("--root", type=Path, default=REPO)
    ap.add_argument("--only", action="append", choices=ALL, help="run one check (repeatable)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument(
        "--timeout",
        type=float,
        default=DEFAULT_TIMEOUT,
        help=f"HTTP GET timeout in seconds (default {DEFAULT_TIMEOUT:g})",
    )
    args = ap.parse_args(argv)

    checks = run(args.only or ALL, root=args.root, timeout=args.timeout)
    if args.json:
        print(
            json.dumps(
                [
                    {
                        "check": check.name,
                        "ok": check.ok,
                        "findings": check.findings,
                        "measured": check.measured,
                    }
                    for check in checks
                ],
                indent=2,
            )
        )
    else:
        for check in checks:
            status = "ok" if check.ok else f"{len(check.findings)} finding(s)"
            print(f"{check.name}: {status} ({check.measured} {check.unit})")
            for line in check.findings:
                print(f"    {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
