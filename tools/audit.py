"""Corpus invariant audit: the checks `qualc check` does not own.

`qualc check` validates each card against the schema and the registries. It says
nothing about the corpus *as a corpus* -- whether two cards hold the same body,
whether a card can be reached by a reader, whether every source file has a
disposition. Those are the invariants of PLAN-QUAL-GRUNT-001, and this is the one
instrument that measures them.

    uv run python tools/audit.py            # human report, exit 1 on any violation
    uv run python tools/audit.py --json     # machine report
    uv run python tools/audit.py --only orphans

The ledger checks need the source repos on disk. When a repo is missing the
check reports `skipped` and the run still fails, because an unmeasurable
totality claim is not a satisfied one.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import cast

import yaml
from qualc.cli import load
from qualc.model import AcademicTerm, ParsedCard, TermOnly, YearOnly, split_front_matter
from qualc.pandoc_batch import PandocServer
from qualc.wiki import IMAGE_ELEMENT, WikiPage

REPO = Path(__file__).resolve().parent.parent

# Source repo -> clone on disk. The ledger's own totality claim is over these.
SOURCE_REPOS = {
    "qual-wiki": Path.home() / "gitclones/qual-wiki",
    "qual-review-and-solutions": Path.home() / "gitclones/qual-review-and-solutions",
    "make-me-a-qual": Path.home() / "gitclones/make-me-a-qual",
    "Analysis-Qual-Compendium": Path.home() / "gitclones/Analysis-Qual-Compendium",
    "math-flashcards": Path.home() / "gitclones/math-flashcards",
}


@dataclass
class Check:
    name: str
    violations: list[str] = field(default_factory=list)
    skipped: str | None = None

    @property
    def ok(self) -> bool:
        return not self.violations and self.skipped is None


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
    violations = [f"{len(ids)} cards share one body: {', '.join(sorted(ids)[:6])}" + ("..." if len(ids) > 6 else "") for ids in by_digest.values() if len(ids) > 1]
    return Check("duplicate-bodies", sorted(violations))


def check_empty_areas(parsed: list[ParsedCard]) -> Check:
    return Check(
        "empty-areas",
        sorted(f"{item.card.id}: areas: []" for item in parsed if not item.card.classification.areas),
    )


def check_degenerate_titles(parsed: list[ParsedCard]) -> Check:
    """A title that is a list marker or a bare ordinal names nothing."""
    bad: list[str] = []
    for item in parsed:
        title = item.card.title.strip()
        stripped = title.rstrip(".)").strip()
        if not stripped or (len(stripped) <= 2 and not stripped.isalpha()) or len(stripped) <= 1:
            bad.append(f"{item.card.id}: title {item.card.title!r}")
    return Check("degenerate-titles", sorted(bad))


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
        sorted(f"{key}: {', '.join(sorted(ids))}" for key, ids in seen.items() if len(ids) > 1),
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


def orphan_ids(parsed: list[ParsedCard], wiki_pages: list[WikiPage], root: Path = REPO) -> set[str]:
    """A card is reachable when a page or manifest names it, or when it hangs off
    a card that is. The emitter renders occurrences, hints and solutions on their
    problem's route, so a reader does reach them -- but only through it.

    The same holds one level up, for the same reason: `emit.source_page` renders
    every occurrence of a sitting on that sitting's own route, each linked to its
    problem, "in the order they appeared". Naming a `source` card therefore
    reaches its occurrences and their problems. This edge is here because the
    emitter draws it -- delete `source_page`'s listing and this edge goes too."""
    import panflute as pf

    referenced: set[str] = set(_manifest_ids(root))

    def visit(element: pf.Element) -> None:
        if isinstance(element, pf.Link | IMAGE_ELEMENT):
            # Same two-step as `qualc.wiki`: the Image cast erases the concrete
            # type, so the url comes back through `getattr` with no default.
            head, _, tail = cast(str, getattr(element, "url")).partition("/")
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
            edges[source].update(relation.target for relation in item.card.relations if relation.kind == "instance-of")

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
    return Check("orphans", [f"{len(orphans)} cards reachable from no page or manifest: {head}..."])


def _ledger_rows() -> list[dict]:
    path = REPO / "sources" / "migration-ledger.jsonl"
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def _tracked(repo: Path) -> list[str] | None:
    if not (repo / ".git").exists():
        return None
    result = subprocess.run(
        ["git", "-C", str(repo), "ls-files"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout.splitlines()


def check_ledger_totality() -> Check:
    """Every tracked file of every source repo has exactly one disposition,
    recomputed against the repo -- never against a summary of it."""
    rows = _ledger_rows()
    by_repo: dict[str, list[str]] = {}
    for row in rows:
        if row["repo"] not in by_repo:
            by_repo[row["repo"]] = []
        by_repo[row["repo"]].append(row["path"])

    violations: list[str] = []
    missing_repos: list[str] = []
    for name, path in SOURCE_REPOS.items():
        tracked = _tracked(path)
        if tracked is None:
            missing_repos.append(name)
            continue
        ledgered = by_repo[name] if name in by_repo else []
        duplicates = {p for p in ledgered if ledgered.count(p) > 1}
        unclassified = sorted(set(tracked) - set(ledgered))
        phantom = sorted(set(ledgered) - set(tracked))
        if duplicates:
            violations.append(f"{name}: {len(duplicates)} paths with more than one disposition")
        if unclassified:
            violations.append(f"{name}: {len(unclassified)} tracked files with no disposition, e.g. {unclassified[0]!r}")
        if phantom:
            violations.append(f"{name}: {len(phantom)} ledger rows for untracked paths, e.g. {phantom[0]!r}")
    check = Check("ledger-totality", violations)
    if missing_repos:
        check.skipped = f"no clone on disk: {', '.join(missing_repos)}"
    return check


def check_reason_truth() -> Check:
    """A disposition reason must be true of the file. The realized failure was
    `dropped / authored .md not routed (index/config/personal)` on files full of
    numbered problem statements, so every dropped markdown row is re-read."""
    import re

    statement = re.compile(
        r"(:::+\s*(problem|exercise|theorem|definition|proposition|lemma))"
        r"|(^\s*\d+\.\s+\S.{40,})"
        r"|(\\begin\{(problem|exercise|theorem)\})",
        re.M | re.I,
    )
    violations: list[str] = []
    missing: list[str] = []
    for row in _ledger_rows():
        if row["disposition"] != "dropped" or not row["path"].lower().endswith((".md", ".tex")):
            continue
        if row["repo"] not in SOURCE_REPOS:
            continue
        repo = SOURCE_REPOS[row["repo"]]
        blob = subprocess.run(
            ["git", "-C", str(repo), "show", f"HEAD:{row['path']}"],
            capture_output=True,
            text=True,
        )
        if blob.returncode != 0:
            missing.append(f"{row['repo']}:{row['path']}")
            continue
        hits = statement.findall(blob.stdout)
        if len(hits) >= 3:
            violations.append(f"{row['repo']}:{row['path']}: {len(hits)} statement-shaped items under {row['reason']!r}")
    check = Check("reason-truth", sorted(violations))
    if missing:
        check.skipped = f"{len(missing)} dropped rows unreadable from HEAD"
    return check


def check_queued_not_claimed() -> Check:
    """A row may not move `queued` -> `migrated` without evidence naming what
    carries its content."""
    violations = [
        f"{row['repo']}:{row['path']}: migrated with no evidence"
        for row in _ledger_rows()
        if row["disposition"] == "migrated" and not any(key in row for key in ("evidence", "cards", "sha1"))
    ]
    return Check("migrated-evidence", sorted(violations))


CORPUS_CHECKS = {
    "duplicate-bodies": check_duplicate_bodies,
    "empty-areas": check_empty_areas,
    "degenerate-titles": check_degenerate_titles,
    "duplicate-sittings": check_one_sitting_one_source,
}
LEDGER_CHECKS = {
    "ledger-totality": check_ledger_totality,
    "reason-truth": check_reason_truth,
    "migrated-evidence": check_queued_not_claimed,
}
ALL = list(CORPUS_CHECKS) + ["orphans"] + list(LEDGER_CHECKS)


def run(names: list[str]) -> list[Check]:
    checks: list[Check] = []
    wanted = set(names)
    needs_corpus = wanted & (set(CORPUS_CHECKS) | {"orphans"})
    if needs_corpus:
        with PandocServer() as pandoc:
            parsed, wiki_pages, errors = load(REPO, pandoc)
        if errors:
            return [Check("qualc-check", [f"corpus does not validate: {len(errors)} error(s); first: {errors[0]}"])]
        for name in names:
            if name in CORPUS_CHECKS:
                checks.append(CORPUS_CHECKS[name](parsed))
            elif name == "orphans":
                checks.append(check_orphans(parsed, wiki_pages))
    for name in names:
        if name in LEDGER_CHECKS:
            checks.append(LEDGER_CHECKS[name]())
    return checks


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="audit")
    ap.add_argument("--only", action="append", choices=ALL, help="run one check (repeatable)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--full", action="store_true", help="print every violation, not the first 20")
    args = ap.parse_args(argv)

    checks = run(args.only or ALL)
    if args.json:
        print(
            json.dumps(
                [{"check": c.name, "ok": c.ok, "skipped": c.skipped, "violations": c.violations} for c in checks],
                indent=2,
            )
        )
    else:
        for check in checks:
            status = "ok" if check.ok else f"{len(check.violations)} violation(s)"
            print(f"{check.name}: {status}" + (f" [skipped: {check.skipped}]" if check.skipped else ""))
            for line in check.violations if args.full else check.violations[:20]:
                print(f"    {line}")
            if not args.full and len(check.violations) > 20:
                print(f"    ... {len(check.violations) - 20} more")
    return 0 if all(c.ok for c in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
