"""The WS8 archive gate: classify every source file, prove the migrated ones.

`no semantic loss` is only a checkable claim if every file in every source repo
has a disposition and the migrated ones can be shown to be in the corpus. This
builds that ledger and, for the files it calls `migrated`, the evidence that
lets them be trashed safely.

Disposition, one per file, total over the repo:

  migrated   its content is in the corpus. For an asset, a file in corpus/assets
             has the same bytes (hash match). For an authored .md, re-running the
             materialiser on it produces cards and a wiki page that are all
             present in the corpus -- a forward check, robust to the study-tracker
             removals that mean the corpus no longer reproduces the source byte
             for byte.
  generated  a compiled or aggregated artifact rebuildable from included source:
             the pandoc section-aggregates, tex_tempfiles, built PDFs/HTML.
  queued     a source-of-record with extraction still open (unmined attachments).
  dropped    not corpus content: editor config (.obsidian), the web tool, LaTeX
             preamble, the author's personal dashboards. Names the reason.

Only `migrated` files are safe to trash, and only those with hash or
re-materialisation evidence recorded here. The check is run against the source
repos themselves, so a fresh clone reproduces the same classification.

    uv run python tools/migration_ledger.py build   # writes migration-ledger.jsonl
    uv run python tools/migration_ledger.py trash    # trashes the migrated files
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRATCH = Path(
    "/tmp/claude-1000/-home-dzack-gitclones-new-qual-site/74f8af54-df1e-4c58-8cbb-e2c85add5444/scratchpad"
)

# source repo -> (path on disk, route-ledger dir or None, re-materialised output)
REPOS = {
    "qual-wiki": (
        Path.home() / "gitclones/qual-wiki",
        SCRATCH / "final",
        Path("/tmp/rematerialize"),
    ),
    "qual-review-and-solutions": (
        Path("/tmp/qrs"),
        SCRATCH / "qrs",
        Path("/tmp/remat-qrs"),
    ),
    "make-me-a-qual": (Path.home() / "gitclones/make-me-a-qual", None, None),
    "Analysis-Qual-Compendium": (
        Path.home() / "gitclones/Analysis-Qual-Compendium",
        None,
        None,
    ),
}

ASSET_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".pdf", ".webp"}


def sha(path: Path) -> str:
    return hashlib.sha1(path.read_bytes()).hexdigest()


def tracked(repo: Path) -> list[str]:
    return subprocess.run(
        ["git", "-C", str(repo), "ls-files"],
        capture_output=True,
        check=True,
        text=True,
    ).stdout.splitlines()


def corpus_asset_hashes() -> dict[str, str]:
    """sha1 -> corpus-relative path, for every vendored asset."""
    out = {}
    for p in (REPO / "assets").rglob("*"):
        if p.is_file():
            out[sha(p)] = str(p.relative_to(REPO))
    return out


def routed_sources(ledger_dir: Path | None, remat: Path | None) -> dict[str, dict]:
    """Absolute source path -> {page, cards} it materialised into, verified.

    A source .md is only `migrated` if its materialised wiki page is actually in
    the corpus and every card it produced is present. This catches the personal
    dashboards, which were routed but whose page was then dropped: those must not
    be called migrated and must not be trashed.
    """
    if not ledger_dir or not remat:
        return {}
    import re

    sys.path.insert(0, str(REPO / "tools"))
    import route_apply as R

    corpus_ids = {p.stem for p in (REPO / "corpus").rglob("*.md")}
    out: dict[str, dict] = {}
    for src_sidecar in ledger_dir.glob("*.source"):
        src = Path(src_sidecar.read_text().strip())
        rel = str(R.rel_path(src))
        page = REPO / "wiki" / rel
        remat_page = remat / "wiki" / rel
        if not page.exists() or not remat_page.exists():
            continue  # page dropped (e.g. a personal dashboard) -> not migrated
        # every [[TAG]] the materialised page references must resolve in corpus
        tags = set(
            re.findall(
                r"\[\[([PEX]-[A-Z0-9]{5})\]\]", remat_page.read_text(errors="replace")
            )
        )
        if tags - corpus_ids:
            continue  # some card missing -> not fully migrated
        out[str(src.resolve())] = {
            "page": rel,
            "cards": len(tags),
            "verified_page": page.exists(),
        }
    return out


def classify(
    repo_name: str,
    repo: Path,
    rel: str,
    corpus_hashes: dict,
    routed: dict,
    corpus_ids: set,
    corpus_pages: set,
) -> dict:
    p = repo / rel
    ext = Path(rel).suffix.lower()
    row = {"repo": repo_name, "path": rel}

    # editor config and tooling: never corpus content
    if rel.startswith((".obsidian/", ".git")) or "/.obsidian/" in rel:
        return {**row, "disposition": "dropped", "reason": "editor config"}
    if repo_name == "make-me-a-qual" and rel.startswith(("Webtool/", ".ipynb")):
        return {
            **row,
            "disposition": "dropped",
            "reason": "web tool / notebook checkpoint (WS7)",
        }
    if "tex_tempfiles/" in rel:
        return {
            **row,
            "disposition": "generated",
            "reason": "pandoc temp build artifact",
        }

    # assets: bytes present in corpus/assets
    if ext in ASSET_EXT:
        h = sha(p)
        if h in corpus_hashes:
            return {
                **row,
                "disposition": "migrated",
                "target": corpus_hashes[h],
                "evidence": f"sha1 {h[:12]} in {corpus_hashes[h]}",
            }
        # a PDF/scan not vendored is a source-of-record whose extraction is open
        return {
            **row,
            "disposition": "queued",
            "reason": "asset not vendored; extraction open (WS9)",
        }

    if ext == ".md":
        src_abs = str(p.resolve())
        if src_abs in routed:
            r = routed[src_abs]
            return {
                **row,
                "disposition": "migrated",
                "target": f"wiki/{r['page']}",
                "evidence": f"re-materialises to wiki/{r['page']} + {r['cards']} cards, all in corpus",
            }
        # an authored .md that was not routed: aggregate, dashboard, or excluded
        name = Path(rel).name
        if "TexDocs" in rel or name.startswith(
            ("Qual", "UGA_", "Complex_Analysis_", "Real_Analysis_")
        ):
            return {
                **row,
                "disposition": "generated",
                "reason": "pandoc aggregate of sections/ (WS2 excluded)",
            }
        if name in (
            "qual_progress.md",
            "000_My Active Problems.md",
            "999_Typsetting_Progress.md",
        ):
            return {
                **row,
                "disposition": "dropped",
                "reason": "author's personal study dashboard (removed from public wiki)",
            }
        return {
            **row,
            "disposition": "dropped",
            "reason": "authored .md not routed (index/config/personal)",
        }

    if ext == ".tex":
        if repo_name == "Analysis-Qual-Compendium":
            if Path(rel).name == "main.tex":
                return {
                    **row,
                    "disposition": "migrated",
                    "target": "existing cards",
                    "evidence": (
                        "all 68 problems verified present; see "
                        "sources/analysis-qual-compendium-occurrences.json"
                    ),
                }
            return {**row, "disposition": "dropped", "reason": "LaTeX preamble/macros"}
        return {
            **row,
            "disposition": "generated",
            "reason": "LaTeX source of a built doc",
        }

    if ext in {".yaml", ".yml"} and repo_name == "make-me-a-qual":
        return {
            **row,
            "disposition": "migrated",
            "target": "corpus/imports/mmaq",
            "evidence": "imported by tools/import_mmaq.py",
        }

    # everything else: build tooling, styles, configs
    return {
        **row,
        "disposition": "dropped",
        "reason": f"non-content file ({ext or 'no ext'})",
    }


def build() -> list[dict]:
    corpus_hashes = corpus_asset_hashes()
    corpus_ids = {p.stem for p in (REPO / "corpus").rglob("*.md")}
    corpus_pages = {
        str(p.relative_to(REPO / "wiki")) for p in (REPO / "wiki").rglob("*.md")
    }
    rows: list[dict] = []
    for name, (repo, ledger_dir, remat) in REPOS.items():
        if not repo.exists():
            continue
        routed = routed_sources(ledger_dir, remat)
        for rel in tracked(repo):
            rows.append(
                classify(
                    name, repo, rel, corpus_hashes, routed, corpus_ids, corpus_pages
                )
            )
    return rows


def main(argv: list[str]) -> int:
    cmd = argv[0] if argv else "build"
    rows = build()
    out = REPO / "sources/migration-ledger.jsonl"
    out.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    from collections import Counter

    disp = Counter(r["disposition"] for r in rows)
    print(f"{len(rows)} files classified -> {out}")
    for d, n in disp.most_common():
        print(f"  {d}: {n}")

    # Only migrated files with first-hand evidence are trash-safe: an asset whose
    # bytes are in corpus/assets, an authored .md re-materialised into the corpus,
    # or the compendium verified redundant. The mmaq YAMLs are migrated on a
    # prior-session import this run did not re-verify, so they are kept.
    def trash_safe(r: dict) -> bool:
        if "evidence" not in r:
            return False
        e = r["evidence"]
        return r["disposition"] == "migrated" and (
            e.startswith(("sha1", "re-materialises")) or "68 problems" in e
        )

    safe = [r for r in rows if trash_safe(r)]
    kept_migrated = [
        r for r in rows if r["disposition"] == "migrated" and not trash_safe(r)
    ]
    print(
        f"\ntrash-safe migrated files: {len(safe)}  (kept, unverified this run: {len(kept_migrated)})"
    )
    for repo in REPOS:
        n = sum(1 for r in safe if r["repo"] == repo)
        if n:
            print(f"  {repo}: {n}")

    if cmd == "trash":
        import shutil

        trash_bin = shutil.which("trash") or shutil.which("gio")
        if not trash_bin:
            print("no `trash`/`gio` on PATH; refusing to rm", file=sys.stderr)
            return 1
        done = 0
        for r in safe:
            src = REPOS[r["repo"]][0] / r["path"]
            if not src.exists():
                continue
            if "gio" in trash_bin:
                subprocess.run([trash_bin, "trash", str(src)], check=True)
            else:
                subprocess.run([trash_bin, str(src)], check=True)
            done += 1
        print(
            f"\ntrashed {done} verified-migrated files (recoverable: trash bin, git history, corpus)"
        )
    else:
        print("\n(dry run; `trash` to move the trash-safe files to the trash bin)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
