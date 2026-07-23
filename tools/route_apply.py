#!/usr/bin/env python3
"""Materialise routing ledgers into problem-bundle cards and wiki pages.

A ledger says where every line of a source file goes. This performs that edit:

  card span  ->  one card under <out>/corpus/, body verbatim, and the span is
                 replaced in the wiki page by a `[[TAG]]` reference
  wiki span  ->  stays in the page, byte for byte

The point of doing this before routing the rest of the corpus is that a ledger
is not an artifact anyone can use. Until a card validates against the schema and
a wiki page renders with its references resolving, a clean ledger proves only
that the lines were classified -- not that the classification can be executed.

Writes to a fresh output root; never edits `corpus/` or the source repo.

    uv run python tools/route_apply.py <ledger-dir> <out-root>

Deferred, deliberately, and reported rather than guessed:

  occurrences   `exam_term` carries the sitting a problem appeared in. Turning
                that into occurrence + source cards needs the institution and
                term parsed and a source registry; the ledger records the raw
                string and this prints what it saw.
  topics        the topic registry is a closed vocabulary and nothing in the
                ledger names a topic. Cards land with `topics: []` rather than
                inventing entries.
  tag stability the id is content-derived, matching the existing corpus scheme.
                That means editing a bundle changes its tag, which is wrong for
                a permanent reference and is a pre-existing question in this
                repo, not one introduced here.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import re
import shutil
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import quote, unquote

AREA_BY_PREFIX = {
    "10_Algebra": "algebra",
    "20_Real_Analysis": "real-analysis",
    "30_Complex_Analysis": "complex-analysis",
    "40_Topology": "topology",
}
KIND_PREFIX = {"problem": "P", "exercise": "E"}


def tag(kind: str, body: str) -> str:
    digest = hashlib.sha1(body.encode()).digest()
    prefix = KIND_PREFIX[kind] if kind in KIND_PREFIX else "X"
    return f"{prefix}-" + base64.b32encode(digest).decode()[:5]


unresolved: list[tuple[str, str]] = []
rewrites: list[dict[str, str]] = []
# The vault is not the only authoritative copy. 173 authored assets exist solely
# on the deployment host -- 172 of them with a colon in the filename, which is
# how they were lost: an earlier copy of this vault ran through a filesystem
# that could not represent the name. Both trees are the corpus.
ASSET_ROOTS: list[Path] = []
_by_name: dict[str, list[tuple[Path, Path]]] = {}


def resolve_asset(ref: str, src: Path) -> tuple[Path, Path] | None:
    """Where an asset actually lives: (tree, path-relative-to-that-tree).

    Obsidian resolves three ways and this corpus uses all of them: relative to
    the note, relative to the vault root, and -- for 92 of 679 references --
    neither, because the written path is wrong and Obsidian falls back to
    searching by filename. Those render today and would break anywhere that took
    the path literally.

    Each asset tree is searched the same way, with the note's own position
    mirrored into it: a bare `figures/x.png` from a note in `40_Topology/` means
    `40_Topology/figures/x.png` in every tree, not the unrelated top-level
    `figures/` that also exists.
    """
    root = corpus_root(src)
    here = src.parent.resolve().relative_to(root.resolve())
    if not _by_name:
        for tree in [root, *ASSET_ROOTS]:
            for p in tree.rglob("*"):
                if p.is_file():
                    if p.name not in _by_name:
                        _by_name[p.name] = []
                    _by_name[p.name].append((tree, p))
    for tree in [root, *ASSET_ROOTS]:
        for cand in (tree / here / ref, tree / ref):
            if cand.exists() and cand.is_file():
                return tree, Path(os.path.normpath(cand.relative_to(tree)))
    for tree, hit in _by_name[Path(ref).name] if Path(ref).name in _by_name else []:
        return tree, hit.resolve().relative_to(tree.resolve())
    return None


def vendor_assets(root: Path, out: Path) -> int:
    """Copy every asset tree, paths preserved, so wiki pages need no rewrite."""
    n = 0
    for tree in [root, *ASSET_ROOTS]:
        n += _vendor_one(tree, out)
    return n


def _vendor_one(root: Path, out: Path) -> int:
    n = 0
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".pdf", ".webp"}:
            continue
        dest = out / "assets" / p.relative_to(root)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            shutil.copy(p, dest)
            n += 1
    return n


def corpus_root(src: Path) -> Path:
    """The vault root, which is where Obsidian resolves non-local asset paths."""
    parts = src.parts
    for marker in ("qual-wiki", "qual-review-and-solutions"):
        if marker in parts:
            return Path(*parts[: parts.index(marker) + 1])
    return src.parent


def rel_path(src: Path) -> Path:
    """The source's path relative to its corpus root, so the wiki keeps its tree."""
    parts = src.parts
    for marker in ("qual-wiki", "qual-review-and-solutions"):
        if marker in parts:
            return Path(*parts[parts.index(marker) + 1 :])
    return Path(src.name)


def area_of(src: Path) -> str | None:
    for part in src.parts:
        if part in AREA_BY_PREFIX:
            return AREA_BY_PREFIX[part]
    return None


AUTHORED_TITLE = re.compile(r'^:{3,}[^\n]*?\btitle="([^"]*)"')
# Lines that are page furniture rather than statement: layout macros, Obsidian
# block anchors, bare tag lines.
NOT_A_TITLE = re.compile(r"^(\\\w+\s*$|\^[0-9a-f]{6}\s*$|#[\w/-]+\s*$|!\[[^\]]*\]\([^)]*\)\s*$)")
# A figure reference relative to the source file's own directory. Cards are
# extracted out of that directory, so every one of these breaks on the way out.
IMAGE = re.compile(r"(!\[[^\]]*\]\()((?!https?:|/)[^)]+)(\))")


def title_of(span: dict, body: str) -> str:
    r"""The authored title if there is one, else the first sentence of the statement.

    The title is read out of the source body, never from the ledger. Asked to
    copy `title="Complement of the disc to $\\mathbb{H}$"`, routing agents
    returned `"Complement of the disc to H"` -- LaTeX silently rendered to
    Unicode, `\mathbb{H}` collapsed to a letter -- and four titles came back
    empty. Byte-exact reconstruction cannot see it, because the card *body*
    still holds the authored div verbatim; only the front-matter title was
    paraphrased. Parsing it here makes transcription impossible to get wrong.

    The corpus titles most expository divs but leaves problems bare -- 240 carry
    an explicit `?`. A generated title is a display handle, not an identity; the
    tag is the identity.
    """
    for line in body.splitlines()[:4]:
        m = AUTHORED_TITLE.match(line)
        if m and m.group(1).strip() not in ("", "?"):
            return str(m.group(1)).strip()
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith((":::", "#", "---", ">")):
            continue
        # `\envlist` is a layout macro and `^043381` an Obsidian block anchor;
        # both are the first line of a statement often enough to have produced
        # 95 cards titled after them. Neither says anything about the problem.
        if NOT_A_TITLE.match(line):
            continue
        line = re.sub(r"\s+", " ", line)
        title = (line[:70].rstrip() + "…") if len(line) > 70 else line
        # A title is one line of text. Anything that survives to here and still
        # spans lines or embeds an image is furniture the filters missed, and
        # emitting it produces front matter that will not parse.
        return title.replace("\n", " ").strip() or "Untitled"
    return "Untitled"


def apply_ledger(ledger: Path, out: Path) -> dict:
    spans = json.loads(ledger.read_text())
    src = Path((ledger.with_suffix(".source")).read_text().strip())
    lines = src.read_text(errors="replace").splitlines(keepends=True)
    area = area_of(src)

    page: list[str] = []
    cards: list[tuple[str, str]] = []
    terms: list[str] = []
    for span in spans:
        body = "".join(lines[span["start_line"] - 1 : span["end_line"]])
        if span["destination"] != "card":
            page.append(body)
            continue
        # A bundle span that opens with the section heading swallows page
        # structure into the card: the heading is the wiki's navigation and the
        # exam provenance, not part of the problem statement. Split it back out
        # -- the page keeps it, so reconstruction is unaffected.
        head: list[str] = []
        rest = lines[span["start_line"] - 1 : span["end_line"]]
        while rest and (rest[0].startswith("#") or NOT_A_TITLE.match(rest[0].strip()) or not rest[0].strip()):
            head.append(rest.pop(0))
        if not rest:                       # nothing but furniture; leave it be
            page.append(body)
            continue
        page.extend(head)
        body = "".join(rest)

        kind = str(span["kind"]) if span.get("kind") else "problem"
        t = tag(kind, body)
        if span.get("exam_term"):
            terms.append(span["exam_term"])
        meta = [
            "---",
            "schema: qual/card@1",
            f"id: {t}",
            f"kind: {kind}",
            f"title: {json.dumps(title_of(span, body))}",
            "classification:",
            f"  areas:\n  - {area}" if area else "  areas: []",
            "  topics: []",
            "relations: []",
            "review: draft",
            "---",
            "",
        ]
        cards.append((t, "\n".join(meta) + body))
        page.append(f"[[{t}]]\n")

    # Assets are vendored as a whole tree by `vendor_assets`, preserving their
    # vault-relative paths, so a wiki page's references keep working untouched.
    # A card has left the tree, so its references are rewritten to reach the
    # vendored copy -- with the original path preserved inside the rewrite, so
    # the transformation stays reversible and the reconstruction check can tell
    # a move from an edit.
    (out / "corpus" / "wiki").mkdir(parents=True, exist_ok=True)
    for t, text in cards:
        def move(m: re.Match) -> str:
            found = resolve_asset(unquote(m.group(2)), src)
            if found is None:
                unresolved.append((src.name, m.group(2)))
                return str(m.group(0))
            new = f"../../assets/{quote(str(found[1]))}"
            # Every rewrite is recorded. A card is otherwise byte-identical to
            # its source region, so reconstruction stays provable: reverse these
            # and the original must come back exactly. Without the record the
            # guarantee would quietly weaken from "nothing changed" to "nothing
            # changed except things I decided were fine", which is not a
            # guarantee at all.
            rewrites.append({"card": t, "from": m.group(2), "to": new})
            return f"{m.group(1)}{new}{m.group(3)}"

        # Rewrite only the body: the front matter is machine-read metadata and
        # an image path has no business being in it.
        cut = text.index("\n---\n", 3) + len("\n---\n")
        (out / "corpus" / "wiki" / f"{t}.md").write_text(text[:cut] + IMAGE.sub(move, text[cut:]))

    # The wiki page keeps its place in the tree. Writing by basename alone
    # collides -- qual-wiki has three `00_Resources.md`, three `000_Preface.md`
    # -- and silently overwrites, which is indistinguishable from a routing
    # failure when the reconstruction check runs. The directory structure is
    # also the wiki's navigation, so flattening would discard it regardless.
    # Pages keep their place in the tree, so a correctly-written relative
    # reference still resolves untouched. The wrong ones do not: 92 references
    # in this corpus name a path the asset is not at, and Obsidian only renders
    # them because it falls back to searching by filename. Correct them here so
    # the migrated wiki does not depend on that behaviour, recording each change
    # in the same manifest as the cards'.
    page_text = "".join(page)
    here = rel_path(src).parent

    def move_page(m: re.Match) -> str:
        ref = unquote(m.group(2))
        if (out / "assets" / here / ref).exists():
            return str(m.group(0))
        found = resolve_asset(ref, src)
        if found is None:
            unresolved.append((src.name, m.group(2)))
            return str(m.group(0))
        depth = len(here.parts)
        new = ("../" * depth) + f"../assets/{quote(str(found[1]))}"
        rewrites.append({"card": f"wiki:{rel_path(src)}", "from": m.group(2), "to": new})
        return f"{m.group(1)}{new}{m.group(3)}"

    wiki_page = out / "wiki" / rel_path(src)
    wiki_page.parent.mkdir(parents=True, exist_ok=True)
    wiki_page.write_text(IMAGE.sub(move_page, page_text))

    return {"source": src.name, "cards": len(cards), "page": wiki_page, "terms": terms, "area": area}


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    if "--assets" in argv:
        i = argv.index("--assets")
        ASSET_ROOTS.append(Path(argv[i + 1]))
        argv = argv[:i] + argv[i + 2 :]
    ledgers, out = Path(argv[0]), Path(argv[1])
    first = next(iter(sorted(ledgers.glob("*.source"))), None)
    vault = corpus_root(Path(first.read_text().strip())) if first else None
    n_assets = vendor_assets(vault, out) if vault else 0
    reports = [apply_ledger(p, out) for p in sorted(ledgers.glob("*.json"))]
    total = sum(r["cards"] for r in reports)
    for r in reports:
        print(f"{r['cards']:4d} bundles  area={r['area'] or '—':16s} {r['source']}")
    print(f"\n{total} bundle cards, {len(reports)} wiki pages, {n_assets} assets vendored -> {out}")
    (out / "asset-rewrites.json").write_text(json.dumps(rewrites, indent=1))
    print(f"{len(rewrites)} asset references rewritten; manifest at {out}/asset-rewrites.json")
    if unresolved:
        print(f"\n{len(unresolved)} asset references could not be resolved anywhere in the vault:")
        for where, ref in unresolved[:10]:
            print(f"   {ref[:58]:58s} <- {where[:40]}")

    seen = Counter(t for r in reports for t in r["terms"])
    if seen:
        print(f"\n{sum(seen.values())} exam terms recorded but NOT yet made into occurrences:")
        for term, n in seen.most_common(8):
            print(f"   {n:3d}  {term}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
