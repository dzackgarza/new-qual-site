"""Corpus invariant audit: the checks `qualc check` does not own.

`qualc check` validates each card against the schema and the registries. It says
nothing about the corpus *as a corpus* -- whether two cards hold the same body,
whether a card can be reached by a reader, whether two source cards claim one
sitting. Those are the invariants this measures.

    uv run python tools/audit.py            # human report, exit 1 on any violation
    uv run python tools/audit.py --json     # machine report
    uv run python tools/audit.py --only orphans
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import cast

import yaml
from qualc.cli import load
from qualc.model import AcademicTerm, ParsedCard, TermOnly, YearOnly, split_front_matter
from qualc.pandoc_batch import PandocServer
from qualc.wiki import IMAGE_ELEMENT, WikiPage

REPO = Path(__file__).resolve().parent.parent


@dataclass
class Check:
    name: str
    violations: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.violations


def _body_digest(path: Path) -> str:
    """Hash the card body only. Two cards holding the same mathematics under
    different ids and titles are the duplicate this looks for; identical front
    matter is not what makes them one."""
    _, body = split_front_matter(path.read_text(), path)
    return hashlib.sha1(body.strip().encode()).hexdigest()


# A source or occurrence card has no mathematics of its own -- its body is a
# provenance remark, and the same remark on two different exam sittings is
# correct, not a duplicate. Duplicate *sittings* are `duplicate-sittings`.
BODYLESS_KINDS = {"source", "occurrence"}


def check_duplicate_bodies(parsed: list[ParsedCard]) -> Check:
    by_digest: dict[str, list[str]] = {}
    for item in parsed:
        if item.card.kind in BODYLESS_KINDS:
            continue
        digest = _body_digest(Path(item.source_path))
        if digest not in by_digest:
            by_digest[digest] = []
        by_digest[digest].append(item.card.id)
    violations = [
        f"{len(ids)} cards share one body: {', '.join(sorted(ids)[:6])}"
        + ("..." if len(ids) > 6 else "")
        for ids in by_digest.values()
        if len(ids) > 1
    ]
    return Check("duplicate-bodies", sorted(violations))


def check_empty_areas(parsed: list[ParsedCard]) -> Check:
    return Check(
        "empty-areas",
        sorted(
            f"{item.card.id}: areas: []"
            for item in parsed
            if not item.card.classification.areas
        ),
    )


def check_one_sitting_one_source(parsed: list[ParsedCard]) -> Check:
    """An exam sitting is institution + area + date. Two source cards for one
    sitting split every per-exam query in half."""
    seen: dict[tuple[str, str, str, int | None, str | None], list[str]] = {}
    for item in parsed:
        card = item.card
        if card.kind != "source" or card.payload.source_kind != "university-exam":
            continue
        date = card.payload.date
        # One branch per date variant, matching the union: a case without a year
        # genuinely has none, and `None` here says which case, never "missing".
        year = date.year if isinstance(date, AcademicTerm | YearOnly) else None
        term = date.term if isinstance(date, AcademicTerm | TermOnly) else None
        key = (card.payload.institution, card.payload.area, date.kind, year, term)
        if key not in seen:
            seen[key] = []
        seen[key].append(card.id)
    return Check(
        "duplicate-sittings",
        sorted(
            f"{key}: {', '.join(sorted(ids))}"
            for key, ids in seen.items()
            if len(ids) > 1
        ),
    )


def _manifest_ids(root: Path = REPO) -> set[str]:
    ids: set[str] = set()
    for path in (root / "publications").glob("*.yaml"):
        text = path.read_text()
        data = yaml.safe_load(text)
        stack = [data]
        while stack:
            node = stack.pop()
            if isinstance(node, dict):
                stack.extend(node.values())
            elif isinstance(node, list):
                stack.extend(node)
            elif isinstance(node, str):
                ids.add(node)
    return ids


def orphan_ids(
    parsed: list[ParsedCard], wiki_pages: list[WikiPage], root: Path = REPO
) -> set[str]:
    """A card is reachable when a page or manifest names it, or when it hangs off
    a card that is. The emitter renders occurrences, hints and solutions on their
    problem's route, so a reader does reach them -- but only through it.

    The same holds one level up, for the same reason: `emit.source_page` renders
    every occurrence of a sitting on that sitting's own route, each linked to its
    problem. Naming a `source` card therefore
    reaches its occurrences and their problems. This edge is here because the
    emitter draws it -- delete `source_page`'s listing and this edge goes too."""
    import panflute as pf

    referenced: set[str] = set(_manifest_ids(root))

    def visit(element: pf.Element) -> None:
        if isinstance(element, pf.Link | IMAGE_ELEMENT):
            head, _, tail = cast(pf.Link, element).url.partition("/")
            if head in {"tag", "exam"}:
                referenced.add(Path(tail).stem)
        # Leaf inlines carry no `content`; everything with children exposes it.
        if hasattr(element, "content"):
            for child in element.content:
                if isinstance(child, pf.Element):
                    visit(child)

    for page in wiki_pages:
        for block in page.blocks:
            visit(block)

    # Close under attachment: an occurrence/solution/hint is read on the route of
    # the card it points at.
    attaches = {"instance-of", "solves", "hints-at", "variant-of"}
    edges: dict[str, set[str]] = {}
    for item in parsed:
        for relation in item.card.relations:
            if relation.kind in attaches:
                if relation.target not in edges:
                    edges[relation.target] = set()
                edges[relation.target].add(item.card.id)
        if item.card.kind == "occurrence":
            source = item.card.payload.source
            if source not in edges:
                edges[source] = set()
            # The sitting's page carries the occurrence and links its problem.
            edges[source].add(item.card.id)
            edges[source].update(
                relation.target
                for relation in item.card.relations
                if relation.kind == "instance-of"
            )

    reachable = {cid for cid in referenced}
    frontier = list(reachable)
    while frontier:
        current = frontier.pop()
        for child in edges[current] if current in edges else ():
            if child not in reachable:
                reachable.add(child)
                frontier.append(child)

    return {item.card.id for item in parsed if item.card.id not in reachable}


def check_orphans(parsed: list[ParsedCard], wiki_pages: list[WikiPage]) -> Check:
    orphans = sorted(orphan_ids(parsed, wiki_pages))
    if not orphans:
        return Check("orphans")
    head = ", ".join(orphans[:10])
    return Check(
        "orphans",
        [f"{len(orphans)} cards reachable from no page or manifest: {head}..."],
    )


CHECKS = {
    "duplicate-bodies": check_duplicate_bodies,
    "empty-areas": check_empty_areas,
    "duplicate-sittings": check_one_sitting_one_source,
}
ALL = list(CHECKS) + ["orphans"]


def run(names: list[str]) -> list[Check]:
    with PandocServer() as pandoc:
        parsed, wiki_pages, errors = load(REPO, pandoc)
    if errors:
        return [
            Check(
                "qualc-check",
                [
                    f"corpus does not validate: {len(errors)} error(s); first: {errors[0]}"
                ],
            )
        ]
    checks: list[Check] = []
    for name in names:
        if name in CHECKS:
            checks.append(CHECKS[name](parsed))
        elif name == "orphans":
            checks.append(check_orphans(parsed, wiki_pages))
    return checks


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="audit")
    ap.add_argument(
        "--only", action="append", choices=ALL, help="run one check (repeatable)"
    )
    ap.add_argument("--json", action="store_true")
    ap.add_argument(
        "--full", action="store_true", help="print every violation, not the first 20"
    )
    args = ap.parse_args(argv)

    checks = run(args.only or ALL)
    if args.json:
        print(
            json.dumps(
                [
                    {
                        "check": c.name,
                        "ok": c.ok,
                        "violations": c.violations,
                    }
                    for c in checks
                ],
                indent=2,
            )
        )
    else:
        for check in checks:
            status = "ok" if check.ok else f"{len(check.violations)} violation(s)"
            print(f"{check.name}: {status}")
            for line in check.violations if args.full else check.violations[:20]:
                print(f"    {line}")
            if not args.full and len(check.violations) > 20:
                print(f"    ... {len(check.violations) - 20} more")
    return 0 if all(c.ok for c in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
