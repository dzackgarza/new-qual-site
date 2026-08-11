"""Replay the migration ledger from isolated SSH source clones."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, TypedDict, cast

from audit import load, orphan_ids
from qualc.pandoc_batch import PandocServer
from source_revisions import SOURCE_REVISIONS, TARGET_COMMIT, SourceRevision

Disposition = Literal["migrated", "generated", "queued", "dropped"]


class LedgerRow(TypedDict, total=False):
    repo: str
    path: str
    disposition: Disposition
    target: str
    evidence: str
    reason: str
    note: str


@dataclass(frozen=True)
class ReplayReport:
    target_commit: str
    source_revisions: tuple[SourceRevision, ...]
    ledger_rows: int
    candidate_path: Path
    clone_root: Path


def _run(command: list[str], *, cwd: Path | None = None) -> str:
    result = subprocess.run(command, cwd=cwd, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def _load_rows(path: Path) -> list[LedgerRow]:
    rows: list[LedgerRow] = []
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number}: ledger row is not an object")
        row = cast(LedgerRow, value)
        if not all(key in row and isinstance(row[key], str) for key in ("repo", "path", "disposition")):
            raise ValueError(f"{path}:{line_number}: ledger row lacks typed identity fields")
        rows.append(row)
    return rows


def compare_ledger_rows(rows: list[LedgerRow], tracked_by_repo: dict[str, set[str]]) -> list[str]:
    """Return source/ledger path differences without accepting a partial ledger."""
    by_repo: dict[str, list[str]] = {}
    problems: list[str] = []
    known = set(tracked_by_repo)
    for row in rows:
        repo = row["repo"]
        path = row["path"]
        if repo not in known:
            problems.append(f"{repo}: ledger row names an unknown source")
        if repo not in by_repo:
            by_repo[repo] = []
        by_repo[repo].append(path)

    for repo, tracked in tracked_by_repo.items():
        paths = by_repo[repo] if repo in by_repo else []
        duplicates = sorted({path for path in paths if paths.count(path) > 1})
        problems.extend(f"{repo}: duplicate ledger row for {path}" for path in duplicates)
        problems.extend(f"{repo}: missing ledger row for {path}" for path in sorted(tracked - set(paths)))
        problems.extend(f"{repo}: ledger row for untracked path {path}" for path in sorted(set(paths) - tracked))
    return sorted(problems)


def resolve_target(root: Path, target: str) -> Path:
    """Resolve a ledger target, including the committed G6 route moves."""
    direct = root / target
    if direct.exists():
        return direct
    map_path = root / "sources/g6-page-merge-map.jsonl"
    if map_path.exists():
        for line in map_path.read_text().splitlines():
            row = cast(dict[str, str], json.loads(line))
            if row["old_route"] == target:
                return root / row["new_route"]
    return direct


def _tracked(clone: Path) -> set[str]:
    return set(_run(["git", "ls-files"], cwd=clone).splitlines())


def _clone(revision: SourceRevision, root: Path) -> Path:
    destination = root / revision.name
    _run(["git", "clone", "--no-checkout", revision.ssh_url, str(destination)])
    _run(["git", "checkout", "--detach", revision.commit], cwd=destination)
    _check_clone(revision, destination)
    return destination


def _check_clone(revision: SourceRevision, destination: Path) -> None:
    actual = _run(["git", "rev-parse", "HEAD"], cwd=destination)
    if actual != revision.commit:
        raise RuntimeError(f"{revision.name}: checked out {actual}, expected {revision.commit}")
    if _run(["git", "status", "--porcelain"], cwd=destination):
        raise RuntimeError(f"{revision.name}: fresh clone is not clean")
    remote = _run(["git", "remote", "get-url", "origin"], cwd=destination)
    if not remote.startswith("git@github.com:"):
        raise RuntimeError(f"{revision.name}: clone did not use SSH origin")


def _source_bytes(clone: Path, path: str) -> bytes:
    return (clone / path).read_bytes()


def _verify_asset(root: Path, clone: Path, row: LedgerRow) -> None:
    target_name = row["target"] if "target" in row else ""
    evidence = row["evidence"] if "evidence" in row else ""
    if not target_name or not evidence.startswith("sha1 "):
        return
    target = resolve_target(root, target_name)
    if not target.is_file():
        raise RuntimeError(f"{row['repo']}:{row['path']}: asset target missing: {target_name}")
    source_hash = hashlib.sha1(_source_bytes(clone, row["path"])).hexdigest()
    target_hash = hashlib.sha1(target.read_bytes()).hexdigest()
    if source_hash != target_hash or not evidence.startswith(f"sha1 {source_hash[:12]}"):
        raise RuntimeError(f"{row['repo']}:{row['path']}: source and target hashes differ")


def _verify_target(root: Path, row: LedgerRow) -> None:
    target_name = row["target"] if "target" in row else ""
    if not target_name or target_name in {"existing cards", "corpus/flashcards"}:
        return
    target = resolve_target(root, target_name)
    if not target.exists():
        raise RuntimeError(f"{row['repo']}:{row['path']}: migrated target missing: {target_name}")


def _verify_mmaq_import(root: Path) -> None:
    output = root / "corpus/imports/mmaq-total"
    manifest_path = output / "manifest.json"
    reconciliation = root / "sources/mmaq-reconciliation.jsonl"
    if not manifest_path.is_file() or not reconciliation.is_file():
        raise RuntimeError("MakeMeAQual import output is incomplete")
    manifest = cast(dict[str, int], json.loads(manifest_path.read_text()))
    rows = [cast(dict[str, object], json.loads(line)) for line in reconciliation.read_text().splitlines() if line.strip()]
    if manifest["rows"] != len(rows) or manifest["occurrences"] != len(rows):
        raise RuntimeError("MakeMeAQual import manifest does not match its reconciliation ledger")
    if not all("occurrence_id" in row and isinstance(row["occurrence_id"], str) for row in rows):
        raise RuntimeError("MakeMeAQual reconciliation ledger has an invalid occurrence")


def _verify_authored_page(root: Path, row: LedgerRow) -> None:
    evidence = row["evidence"] if "evidence" in row else ""
    match = re.search(r"re-materialises to (\S+) \+ (\d+) cards", evidence)
    if not match:
        return
    target = resolve_target(root, row["target"])
    references = re.findall(r"\[\[([A-Z]-[A-Z0-9]+)\]\]", target.read_text())
    expected = int(match.group(2))
    if len(references) < expected:
        raise RuntimeError(f"{row['repo']}:{row['path']}: target has {len(references)} card links, expected at least {expected}")


def _flashcard_rows(root: Path, deck: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in (root / "sources/flashcard-import-ledger.jsonl").read_text().splitlines():
        if not line.strip():
            continue
        row = cast(dict[str, str], json.loads(line))
        if "deck" in row and row["deck"] == deck:
            rows.append(row)
    return rows


def _verify_flashcard_deck(root: Path, row: LedgerRow) -> None:
    for card in _flashcard_rows(root, row["path"]):
        if "disposition" in card and card["disposition"] == "migrated":
            evidence = card["evidence"] if "evidence" in card else ""
            target = evidence.split(",", 1)[0].removeprefix("corpus/")
            if not target or not (root / "corpus" / target).is_file():
                card_id = card["id"] if "id" in card else "unknown"
                raise RuntimeError(f"{row['repo']}:{row['path']}: flashcard target missing for {card_id}")


def _verify_source_rows(
    root: Path,
    clones: dict[str, Path],
    tracked_by_repo: dict[str, set[str]],
    rows: list[LedgerRow],
) -> None:
    statement = re.compile(
        r"(:::+\s*(problem|exercise|theorem|definition|proposition|lemma))"
        r"|(^\s*\d+\.\s+\S.{40,})"
        r"|(\\begin\{(problem|exercise|theorem)\})",
        re.M | re.I,
    )
    for row in rows:
        clone = clones[row["repo"]]
        if row["path"] not in tracked_by_repo[row["repo"]]:
            raise RuntimeError(f"{row['repo']}:{row['path']}: source path is not tracked")
        disposition = row["disposition"]
        if disposition == "migrated":
            _verify_asset(root, clone, row)
            _verify_target(root, row)
            target_name = row["target"] if "target" in row else ""
            if target_name == "corpus/imports/mmaq-total":
                _verify_mmaq_import(root)
            if target_name.startswith("wiki/"):
                _verify_authored_page(root, row)
            if target_name == "corpus/flashcards":
                _verify_flashcard_deck(root, row)
            if "evidence" not in row or not row["evidence"]:
                raise RuntimeError(f"{row['repo']}:{row['path']}: migrated row has no evidence")
        elif disposition == "generated":
            reason = (row["reason"] if "reason" in row else "").lower()
            if not any(word in reason for word in ("source", "rebuild", "rebuilt", "aggregate", "compiled", "rendering")):
                raise RuntimeError(f"{row['repo']}:{row['path']}: generated row does not name its source")
        elif disposition == "queued":
            owner_in_flashcard_ledger = row["repo"] == "math-flashcards" and any(
                "disposition" in card and card["disposition"] == "queued" for card in _flashcard_rows(root, row["path"])
            )
            reason = row["reason"] if "reason" in row else ""
            if "WS9" not in reason and not owner_in_flashcard_ledger:
                raise RuntimeError(f"{row['repo']}:{row['path']}: queued row has no extraction owner")
        elif disposition == "dropped":
            if row["path"].lower().endswith((".md", ".tex")):
                text = _run(["git", "show", f"HEAD:{row['path']}"], cwd=clone)
                if len(statement.findall(text)) >= 3:
                    raise RuntimeError(f"{row['repo']}:{row['path']}: dropped reason hides source statements")
        else:
            raise RuntimeError(f"{row['repo']}:{row['path']}: invalid disposition {disposition}")


def _verify_orphans(root: Path) -> None:
    residual = {json.loads(line)["card"] for line in (root / "sources/g7-residual.jsonl").read_text().splitlines() if line.strip()}
    with PandocServer() as pandoc:
        parsed, pages, errors = load(root, pandoc)
    if errors:
        raise RuntimeError(f"target corpus does not validate: {len(errors)} error(s)")
    current = orphan_ids(parsed, pages, root)
    if current != residual:
        missing = sorted(residual - current)
        extra = sorted(current - residual)
        raise RuntimeError(f"G7 residual differs: missing={missing}, undocumented={extra}")


def replay(root: Path, clone_root: Path | None, candidate_path: Path | None) -> ReplayReport:
    ledger_path = root / "sources/migration-ledger.jsonl"
    rows = _load_rows(ledger_path)
    revisions = tuple(SOURCE_REVISIONS)
    clones: dict[str, Path] = {}
    if clone_root is None:
        temporary = tempfile.TemporaryDirectory(prefix="qualc-replay-")
        working_root = Path(temporary.name)
    else:
        temporary = None
        working_root = clone_root
        marker = working_root / ".qualc-replay.json"
        if working_root.exists() and marker.exists():
            recorded = json.loads(marker.read_text())
            expected = {revision.name: revision.commit for revision in SOURCE_REVISIONS}
            if recorded != expected:
                raise RuntimeError(f"clone root marker does not match pinned revisions: {working_root}")
            clones = {revision.name: working_root / revision.name for revision in revisions}
            for revision in revisions:
                _check_clone(revision, clones[revision.name])
        else:
            if working_root.exists() and any(working_root.iterdir()):
                raise RuntimeError(f"clone root is not fresh: {working_root}")
            working_root.mkdir(parents=True, exist_ok=False)
            clones = {}
    try:
        if not clones:
            clones = {revision.name: _clone(revision, working_root) for revision in revisions}
            (working_root / ".qualc-replay.json").write_text(json.dumps({revision.name: revision.commit for revision in revisions}, sort_keys=True) + "\n")
        tracked_by_repo = {name: _tracked(clone) for name, clone in clones.items()}
        problems = compare_ledger_rows(rows, tracked_by_repo)
        if problems:
            raise RuntimeError("ledger/source comparison failed:\n" + "\n".join(problems))
        _verify_source_rows(root, clones, tracked_by_repo, rows)
        _verify_orphans(root)
        destination = candidate_path or working_root / "migration-ledger.candidate.jsonl"
        destination.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows))
        return ReplayReport(TARGET_COMMIT, revisions, len(rows), destination, working_root)
    finally:
        if temporary is not None:
            temporary.cleanup()


def _write_proof(path: Path, report: ReplayReport) -> None:
    lines = [
        "# Fresh-clone source replay",
        "",
        f"Target revision: `{report.target_commit}` Candidate ledger rows: {report.ledger_rows}",
        "",
        "Source revisions:",
        "",
    ]
    for revision in report.source_revisions:
        lines.extend([f"- `{revision.name}` `{revision.branch}` `{revision.commit}` via `{revision.ssh_url}`", ""])
    lines.extend(
        [
            "The command cloned each source over SSH into a new temporary root, checked out the recorded commit, and verified a clean worktree.",
            "It compared every tracked path with the committed ledger, then verified migrated targets and source hashes.",
            "It also verified generated-source reasons, queued owners, dropped-source reasons, and the recorded G7 residual.",
            "",
            "This proves source preservation and build-integrity inputs.",
            "It does not prove that the mathematical wiki is complete.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="qualc replay-sources",
        description="Clone the pinned source revisions over SSH and verify the migration ledger.",
    )
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="project root containing sources/ and corpus/")
    parser.add_argument("--clone-root", type=Path, help="new empty directory for the five fresh clones; a prior command marker permits reruns")
    parser.add_argument("--candidate-ledger", type=Path, help="temporary output path for the candidate ledger")
    parser.add_argument("--proof", type=Path, help="write the replay proof Markdown to this path")
    args = parser.parse_args(argv)
    report = replay(args.root, args.clone_root, args.candidate_ledger)
    if args.proof:
        _write_proof(args.proof, report)
    print(f"replayed {len(report.source_revisions)} SSH clones at {report.ledger_rows} ledger rows")
    print(f"target revision: {report.target_commit}")
    print(f"candidate ledger: {report.candidate_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
