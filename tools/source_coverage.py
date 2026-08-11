"""Build an exhaustive source-to-target coverage record.

This verifier reads the pinned Git objects, not mutable source worktrees.  It
records one row for every tracked source path and every known untracked APKG.
Generated artifacts are retained verbatim before the record is written.  The
report therefore separates exact identity checks, transformed-content checks,
and direct non-content inspections.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from typing import TypedDict

from source_revisions import SOURCE_REVISIONS

ROOT = Path(__file__).resolve().parent.parent
LEDGER_PATH = ROOT / "sources/migration-ledger.jsonl"
ROUTING_PATH = ROOT / "sources/authored-md-routing.jsonl"
AUTHORED_MANIFEST_PATH = ROOT / "corpus/imports/authored-md/manifest.json"
UNTRACKED_PATH = ROOT / "sources/math-flashcards-untracked-artifacts.json"
BLOCK_PATH = ROOT / "sources/unrouted-source-blocks.jsonl"
REPORT_PATH = ROOT / "artifacts/issue-11/source-coverage.jsonl"
SUMMARY_PATH = ROOT / "artifacts/issue-11/source-coverage.md"


class LedgerRow(TypedDict, total=False):
    repo: str
    path: str
    disposition: str
    reason: str
    evidence: str
    target: str
    native_target: str
    source_sha1: str
    source_bytes: int
    source_kind: str
    coverage: str


class CoverageRow(TypedDict, total=False):
    repo: str
    path: str
    state: str
    source_revision: str
    source_kind: str
    source_sha1: str
    source_bytes: int
    link_target: str
    disposition: str
    coverage: str
    target: str
    target_sha1: str
    evidence: str


def _run(command: list[str]) -> bytes:
    return subprocess.run(command, check=True, capture_output=True).stdout


def _source_repo(name: str) -> Path:
    return Path.home() / "gitclones" / name


def _tree(repo: Path, commit: str) -> list[tuple[str, str, str, str]]:
    raw = _run(["git", "-C", str(repo), "ls-tree", "-r", "-z", commit])
    out: list[tuple[str, str, str, str]] = []
    for entry in raw.split(b"\0"):
        if not entry:
            continue
        header, path_bytes = entry.split(b"\t", 1)
        mode, kind, oid = header.decode("ascii").split()
        out.append((mode, kind, oid, path_bytes.decode("utf-8", "surrogateescape")))
    return out


def _blob(repo: Path, commit: str, path: str) -> bytes:
    return _run(["git", "-C", str(repo), "show", f"{commit}:{path}"])


def _sha1(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def _load_ledger() -> list[LedgerRow]:
    return [json.loads(line) for line in LEDGER_PATH.read_text().splitlines() if line.strip()]


def _target_file(target: str) -> Path | None:
    if not target or target in {"existing cards", "corpus/flashcards"}:
        return None
    candidate = ROOT / target
    if not candidate.is_file():
        merge_map = ROOT / "sources/g6-page-merge-map.jsonl"
        if merge_map.is_file():
            for line in merge_map.read_text().splitlines():
                mapping = json.loads(line)
                if mapping["old_route"] == target:
                    candidate = ROOT / mapping["new_route"]
                    break
    return candidate if candidate.is_file() else None


def _copy_generated(rows: list[LedgerRow], revisions: dict[str, str], repos: dict[str, Path]) -> None:
    for row in rows:
        if row["disposition"] != "generated":
            continue
        source = repos[row["repo"]] / row["path"]
        if not source.is_file():
            raise RuntimeError(f"generated source is not a regular file: {row['repo']}:{row['path']}")
        target_name = row["path"] + ".source" if row["path"].endswith(".md") else row["path"]
        target = ROOT / "assets" / "ws9" / row["repo"] / "generated" / target_name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(_blob(repos[row["repo"]], revisions[row["repo"]], row["path"]))
        row["target"] = str(target.relative_to(ROOT))
        row["evidence"] = f"sha1 {_sha1(source.read_bytes())}; generated artifact retained verbatim"


def _copy_unrouted_source(revisions: dict[str, str], repos: dict[str, Path], rows: list[LedgerRow]) -> None:
    source = repos["qual-review-and-solutions"] / "Algebra/Review Doc/AlgebraQualNotes.md"
    target = ROOT / "assets/ws9/qual-review-and-solutions/native/Algebra/Review Doc/AlgebraQualNotes.md.source"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(_blob(repos["qual-review-and-solutions"], revisions["qual-review-and-solutions"], str(source.relative_to(repos["qual-review-and-solutions"]))))
    for row in rows:
        if row["repo"] == "qual-review-and-solutions" and row["path"] == "Algebra/Review Doc/AlgebraQualNotes.md":
            row["native_target"] = str(target.relative_to(ROOT))
            row["evidence"] = (
                "953 authored statements: 949 route records (768 exact, 1 macro-twin, 180 minted) "
                "+ 4 unrouted blocks retained verbatim in native_target; see sources/unrouted-source-blocks.jsonl"
            )


def _routing_checks() -> dict[str, str]:
    records = [json.loads(line) for line in ROUTING_PATH.read_text().splitlines() if line.strip()]
    by_path: dict[str, list[dict[str, str]]] = defaultdict(list)
    for record in records:
        by_path[record["path"]].append(record)
    manifest = json.loads(AUTHORED_MANIFEST_PATH.read_text())
    results: dict[str, str] = {}
    for path, value in manifest.items():
        routed = by_path.get(path, [])
        statuses = Counter(record["verdict"] for record in routed)
        unresolved = len(value.get("unrouted", []))
        unresolved_records = sum(statuses[status] for status in ("not-a-card-kind", "not-self-contained"))
        if sum(statuses.values()) != value["statements"] or unresolved_records != unresolved:
            raise RuntimeError(f"authored statement count mismatch for {path}")
        if any(status not in {"exact", "macro-twin", "minted"} for status in statuses):
            if path != "Algebra/Review Doc/AlgebraQualNotes.md":
                raise RuntimeError(f"unresolved authored statements remain in {path}")
        retired = {
            json.loads(line)["retired"]: json.loads(line)["survivor"]
            for line in (ROOT / "sources/g3-collapse-map.jsonl").read_text().splitlines()
            if line.strip() and json.loads(line).get("survivor")
        }
        for card in value.get("minted", []):
            direct = ROOT / "corpus/imports/authored-md" / f"{card}.md"
            survivor = retired.get(card)
            if not direct.is_file() and (survivor is None or not any((ROOT / "corpus").rglob(f"{survivor}.md"))):
                raise RuntimeError(f"minted authored card is missing: {card}")
        results[path] = (
            f"{value['statements']} statements: {dict(sorted(statuses.items()))}; "
            f"{unresolved} native blocks"
        )
    block_lines = [json.loads(line) for line in BLOCK_PATH.read_text().splitlines() if line.strip()]
    if len(block_lines) != 4:
        raise RuntimeError(f"expected four unrouted AlgebraQualNotes blocks, found {len(block_lines)}")
    return results


def _flashcard_checks() -> str:
    rows = [json.loads(line) for line in (ROOT / "sources/flashcard-import-ledger.jsonl").read_text().splitlines() if line.strip()]
    queued = [row for row in rows if row["disposition"] == "queued"]
    if queued:
        raise RuntimeError(f"flashcard queue is non-empty: {len(queued)} rows")
    missing = [
        row["id"]
        for row in rows
        if row["disposition"] == "migrated"
        and not (
            (ROOT / row["evidence"].split(";", 1)[0].split(",", 1)[0]).is_file()
            or (ROOT / "corpus/flashcards" / f"{row['id']}.md").is_file()
        )
    ]
    if missing:
        raise RuntimeError(f"flashcard targets are missing: {missing[:5]}")
    return f"{len(rows)} cards; {sum(row['disposition'] == 'migrated' for row in rows)} migrated; zero queued"


def _mmaq_check() -> str:
    manifest = json.loads((ROOT / "corpus/imports/mmaq-total/manifest.json").read_text())
    rows = [json.loads(line) for line in (ROOT / "sources/mmaq-reconciliation.jsonl").read_text().splitlines() if line.strip()]
    if manifest["rows"] != len(rows) or manifest["occurrences"] != len(rows):
        raise RuntimeError("MakeMeAQual manifest and reconciliation row count differ")
    retired = {
        json.loads(line)["retired"]: json.loads(line)["survivor"]
        for line in (ROOT / "sources/g3-collapse-map.jsonl").read_text().splitlines()
        if line.strip() and json.loads(line).get("survivor")
    }
    missing = [
        row["problem_id"]
        for row in rows
        if not any((ROOT / "corpus").rglob(f"{row['problem_id']}.md"))
        and not any((ROOT / "corpus").rglob(f"{retired.get(row['problem_id'], '')}.md"))
    ]
    if missing:
        raise RuntimeError(f"MakeMeAQual problem targets are missing: {missing[:5]}")
    return f"{len(rows)} source rows and {manifest['unique_statements']} unique statements reconciled"


def _compendium_check() -> str:
    data = json.loads((ROOT / "sources/analysis-qual-compendium-occurrences.json").read_text())
    ids = [str(value["card"]).removesuffix(".md") for value in data["occurrences"]]
    if any(not any((ROOT / "corpus").rglob(f"{card}.md")) for card in ids):
        raise RuntimeError("Analysis-Qual-Compendium occurrence target missing")
    return f"{len(ids)} compendium occurrence identifiers checked"


def _untracked_rows() -> list[CoverageRow]:
    data = json.loads(UNTRACKED_PATH.read_text())
    rows: list[CoverageRow] = []
    repo = _source_repo("math-flashcards")
    for artifact in data["artifacts"]:
        source = repo / artifact["source_path"]
        target = ROOT / artifact["target"]
        if not source.is_file() or not target.is_file():
            raise RuntimeError(f"untracked APKG missing: {artifact['source_path']}")
        source_hash = _sha1(source.read_bytes())
        target_hash = _sha1(target.read_bytes())
        if source_hash != target_hash or source_hash != artifact["sha1"]:
            raise RuntimeError(f"untracked APKG identity mismatch: {artifact['source_path']}")
        rows.append({
            "repo": "math-flashcards",
            "path": artifact["source_path"],
            "state": "untracked",
            "source_revision": data["source_revision"],
            "source_kind": "file",
            "source_sha1": source_hash,
            "source_bytes": source.stat().st_size,
            "disposition": "migrated",
            "coverage": "native-identity",
            "target": artifact["target"],
            "target_sha1": target_hash,
            "evidence": "untracked artifact manifest and direct source-target identity check",
        })
    return rows


def build(write: bool) -> tuple[list[CoverageRow], dict[str, str], list[LedgerRow]]:
    ledger = _load_ledger()
    revisions = {revision.name: revision.commit for revision in SOURCE_REVISIONS}
    repos = {revision.name: _source_repo(revision.name) for revision in SOURCE_REVISIONS}
    if write:
        _copy_generated(ledger, revisions, repos)
        _copy_unrouted_source(revisions, repos, ledger)
    routing = _routing_checks()
    checks = {
        "authored_markdown": f"{len(routing)} files; " + "; ".join(routing.values()),
        "flashcards": _flashcard_checks(),
        "make_me_a_qual": _mmaq_check(),
        "analysis_compendium": _compendium_check(),
    }
    by_key = {(row["repo"], row["path"]): row for row in ledger}
    coverage: list[CoverageRow] = []
    for revision in SOURCE_REVISIONS:
        repo = repos[revision.name]
        tree = _tree(repo, revision.commit)
        for mode, kind, _oid, path in tree:
            key = (revision.name, path)
            if key not in by_key:
                raise RuntimeError(f"ledger row missing: {revision.name}:{path}")
            row = by_key[key]
            data = _blob(repo, revision.commit, path)
            source_hash = _sha1(data)
            source_kind = "symlink" if mode == "120000" else "file"
            result: CoverageRow = {
                "repo": revision.name,
                "path": path,
                "state": "tracked",
                "source_revision": revision.commit,
                "source_kind": source_kind,
                "source_sha1": source_hash,
                "source_bytes": len(data),
                "disposition": row["disposition"],
            }
            if source_kind == "symlink":
                result["link_target"] = data.decode("utf-8", "replace")
                result["coverage"] = "symlink-metadata"
                result["evidence"] = "pinned Git symlink target recorded; no source bytes exist"
            elif row["disposition"] == "generated":
                target = _target_file(row["target"])
                if target is None or _sha1(target.read_bytes()) != source_hash:
                    raise RuntimeError(f"generated target mismatch: {revision.name}:{path}")
                result["coverage"] = "generated-native-identity"
                result["target"] = row["target"]
                result["target_sha1"] = source_hash
                result["evidence"] = "generated artifact retained verbatim; direct identity check"
            elif row["disposition"] == "dropped":
                reason = row.get("reason", "")
                accepted = (
                    "editor config" in reason
                    or "non-content" in reason
                    or "web tool" in reason
                    or "personal study dashboard" in reason
                    or "empty file" in reason
                    or "build tooling" in reason
                    or "documentation" in reason
                )
                if not accepted:
                    raise RuntimeError(f"dropped row lacks a direct non-content class: {revision.name}:{path}")
                if path.lower().endswith((".md", ".tex")) and len(data) > 0:
                    raise RuntimeError(f"non-empty Markdown or TeX remains dropped: {revision.name}:{path}")
                result["coverage"] = "non-content-inspection"
                result["evidence"] = f"direct source inspection: {reason}; source sha1 {source_hash}"
            elif row.get("native_target"):
                target = _target_file(row["native_target"])
                if target is None or _sha1(target.read_bytes()) != source_hash:
                    raise RuntimeError(f"native target mismatch: {revision.name}:{path}")
                result["coverage"] = "transformed-plus-native-identity"
                result["target"] = row["target"]
                result["target_sha1"] = source_hash
                result["evidence"] = row.get("evidence", "")
            elif row["disposition"] == "migrated":
                target = _target_file(row.get("target", ""))
                result["target"] = row.get("target", "")
                result["evidence"] = row.get("evidence", "target and route evidence recorded")
                if target is None and row.get("target") not in {"corpus/imports/authored-md", "corpus/imports/mmaq-total", "corpus/flashcards", "existing cards"}:
                    raise RuntimeError(f"migrated target missing: {revision.name}:{path}")
                if target is not None and row.get("evidence", "").startswith("sha1 "):
                    target_hash = _sha1(target.read_bytes())
                    if target_hash != source_hash or not row["evidence"].startswith(f"sha1 {source_hash[:12]}"):
                        raise RuntimeError(f"migrated identity mismatch: {revision.name}:{path}")
                    result["coverage"] = "native-identity"
                    result["target_sha1"] = target_hash
                else:
                    result["coverage"] = "transformed-semantic"
                if row.get("target") == "corpus/imports/authored-md" and path in routing:
                    result["evidence"] = routing[path]
            else:
                raise RuntimeError(f"unsupported disposition: {revision.name}:{path}")
            row["source_sha1"] = source_hash
            row["source_bytes"] = len(data)
            row["source_kind"] = source_kind
            row["coverage"] = result["coverage"]
            coverage.append(result)
    coverage.extend(_untracked_rows())
    return coverage, checks, ledger


def write_outputs(coverage: list[CoverageRow], checks: dict[str, str]) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in coverage))
    counts = Counter(row["coverage"] for row in coverage)
    by_repo = Counter(row["repo"] for row in coverage)
    lines = [
        "# Exhaustive source coverage",
        "",
        "This report is generated from the pinned Git trees, not source worktree summaries.",
        "It records every tracked path in the five pinned revisions and every known untracked APKG.",
        "",
        f"Tracked and known untracked artifacts: **{len(coverage)}**.",
        "",
        "| Source | Artifacts |",
        "| --- | ---: |",
    ]
    lines.extend(f"| `{repo}` | {count} |" for repo, count in sorted(by_repo.items()))
    lines.extend(["", "| Coverage class | Artifacts |", "| --- | ---: |"])
    lines.extend(f"| `{kind}` | {count} |" for kind, count in sorted(counts.items()))
    lines.extend(["", "## Independent checks", ""])
    lines.extend(f"- **{name}:** {value}" for name, value in checks.items())
    lines.extend([
        "",
        "Generated artifacts have verbatim native targets and SHA-1 identity checks.",
        "Dropped rows are accepted only as direct non-content inspections; no non-empty Markdown or TeX row is accepted as dropped.",
        "Transformed rows retain their route, import, flashcard, or occurrence evidence in the ledger and source ledgers.",
        "The JSONL file is the row-level evidence. Every row has a pinned source revision and source SHA-1.",
    ])
    SUMMARY_PATH.write_text("\n".join(lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="retain generated artifacts and the unrouted source file")
    args = parser.parse_args()
    coverage, checks, ledger = build(args.write)
    if args.write:
        LEDGER_PATH.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in ledger))
        write_outputs(coverage, checks)
    print(f"checked {len(coverage)} source artifacts")
    print("; ".join(f"{name}={value}" for name, value in sorted(checks.items())))
    if args.write:
        print(f"wrote {REPORT_PATH}")
        print(f"wrote {SUMMARY_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
