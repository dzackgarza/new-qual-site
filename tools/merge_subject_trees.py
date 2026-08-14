#!/usr/bin/env python3
r"""Merge the two parallel subject trees in `wiki/` into one.

`wiki/` carried each subject twice: the `qual-wiki` numbered layout
(`10_Algebra`, `20_Real_Analysis`, ...) and the `qual-review-and-solutions`
named layout (`Algebra`, `Real Analysis`, ...). The numbered layout is the
user's own reorganization of the named one -- it keeps the filenames and sorts
them into topic sections -- so it is the tree a reader gets, and the named tree
is folded into it.

    uv run python tools/merge_subject_trees.py --dry-run
    uv run python tools/merge_subject_trees.py

Two named pages are the same page only under an *exact* rule, never a
resemblance score:

* equal filename, or
* equal filename after its leading number is dropped, when exactly one page on
  each side carries that stem.

A named page matched that way is merged into its numbered counterpart
additively: every line and every `[[TAG]]` the counterpart does not already
carry is inserted at the position the named page put it, and nothing the
counterpart holds is dropped or reworded. Lines are compared under
`import_mmaq.loose` plus the two rewrites this corpus applied wholesale -- the
`\#` -> `\size` macro rename and the asset-vendoring path rewrite -- so a page
that differs only by those is recognised as the same page.

An unmatched named page is not guessed onto a counterpart. It moves into the
numbered tree whole, keeping its filename, so its number still places it: pages
are ordered by path, and `order:` front matter is inert. Its destination is the
section its already-matched siblings went to, or `HAND_DESTINATIONS` where the
siblings scattered.

`\work`/`\todo`/`\done` survive only in the named tree; every numbered page had
them stripped already. They are dropped from what this pass carries over, per
the user's 2026-07-25 decision that they end at the import boundary.

`sources/g6-page-merge-map.jsonl` records every route change, old -> new.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from collections.abc import Callable
from pathlib import Path

from import_mmaq import loose

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
MERGE_MAP = ROOT / "sources" / "g6-page-merge-map.jsonl"

# The numbered directory that owns each subject, and the named directory it absorbs.
SUBJECT_OF = {
    "00_Prelims": "Prelims",
    "10_Algebra": "Algebra",
    "20_Real_Analysis": "Real Analysis",
    "30_Complex_Analysis": "Complex Analysis",
    "40_Topology": "Topology",
}
NAMED_ROOTS = set(SUBJECT_OF.values())

# Named pages whose already-matched siblings scattered across topic sections, so
# no destination can be derived from them. Each is placed in the numbered section
# that carries its own section's topic.
HAND_DESTINATIONS = {
    "Algebra/README.md": "10_Algebra",
    "Complex Analysis/README.md": "30_Complex_Analysis",
    "Real Analysis/README.md": "20_Real_Analysis",
    "Topology/README.md": "40_Topology",
    "Algebra/Review Doc/sections/11_Groups_Counting_Actions.md": "10_Algebra/020_Groups",
    "Algebra/Review Doc/sections/50_Linear Algebra.md": "10_Algebra/100_Linear_Algebra",
    "Complex Analysis/Review Doc/sections/040_Zeros_and_Poles/015_Zeros and Poles.md": "30_Complex_Analysis/030_Zeros_and_Poles",
    "Complex Analysis/Review Doc/sections/040_Zeros_and_Poles/016_Counting_Zeros_and_Poles_ArgPrinciple_Rouche.md": "30_Complex_Analysis/030_Zeros_and_Poles",
    "Complex Analysis/Review Doc/sections/050_Conformal_Maps/030_Conformal_Mapping.md": "30_Complex_Analysis/050_Conformal_Maps",
    "Real Analysis/Review Doc/sections/00_Preface.md": "20_Real_Analysis/000_Resources",
    # Both named trees hold a `000_Preface.md`; the questions one pairs with the
    # questions section by itself, and this is the review document's.
    "Topology/ReviewDoc/sections/000_Preface.md": "40_Topology/000_Basics",
}

TAG = re.compile(r"\[\[([A-Z]+-[A-Z0-9]+)\]\]")
STATUS = re.compile(r"\s*\\(?:work|todo|done)\b")
IMAGE = re.compile(r"!\[[^\]]*\]\(([^)]*)\)")
DIV_OPEN = re.compile(r"^\s*:{3,}\s*\S")
DIV_CLOSE = re.compile(r"^\s*:{3,}\s*$")
FOOTNOTE = re.compile(r"\[\^([^\]]+)\]")


def strip_status(line: str) -> str:
    """Drop the authoring status markers, which end at the import boundary."""
    return STATUS.sub("", line)


def key_of(line: str) -> str:
    """A line's identity, under the corpus's own equality plus this tree's two
    wholesale rewrites. Empty for a line that carries no content."""
    text = strip_status(line).replace(r"\size", r"\#")
    text = IMAGE.sub(lambda m: "!IMG[" + m.group(1).rsplit("/", 1)[-1].replace("%3A", ":") + "]", text)
    return loose(text)


def is_tag_line(line: str) -> bool:
    return bool(line.strip()) and not TAG.sub("", line).strip()


def stem_of(name: str) -> str:
    text = re.sub(r"^[\d_\s-]+", "", Path(name).stem.lower())
    return re.sub(r"[^a-z0-9]+", "", text)


def inventory() -> tuple[dict[str, list[Path]], dict[str, list[Path]]]:
    numbered: dict[str, list[Path]] = {}
    named: dict[str, list[Path]] = {}
    for path in sorted(WIKI.rglob("*.md")):
        rel = path.relative_to(WIKI)
        top = rel.parts[0]
        if top in SUBJECT_OF:
            subject = SUBJECT_OF[top]
            if subject not in numbered:
                numbered[subject] = []
            numbered[subject].append(rel)
        elif top in NAMED_ROOTS:
            if top not in named:
                named[top] = []
            named[top].append(rel)
    return numbered, named


def _index(pool: list[Path], of_name: Callable[[str], str]) -> dict[str, list[Path]]:
    out: dict[str, list[Path]] = {}
    for rel in pool:
        name = of_name(rel.name)
        if name not in out:
            out[name] = []
        out[name].append(rel)
    return out


def pair_pages() -> tuple[list[tuple[Path, Path, str]], list[Path]]:
    """Split every named page into a merge onto a numbered page, or a move."""
    numbered, named = inventory()
    pairs: list[tuple[Path, Path, str]] = []
    moves: list[Path] = []

    for subject in sorted(named):
        pool = numbered[subject] if subject in numbered else []
        by_base = _index(pool, lambda name: name)
        by_stem = _index(pool, stem_of)
        named_stems = Counter(stem_of(rel.name) for rel in named[subject])
        taken: set[Path] = set()

        # An unambiguous filename match first, then the filename matches that
        # several numbered sections claim, settled by which section the page's
        # own siblings went to.
        deferred: list[Path] = []
        rest: list[Path] = []
        for rel in named[subject]:
            cands = by_base[rel.name] if rel.name in by_base else []
            if len(cands) == 1:
                pairs.append((rel, cands[0], "filename"))
                taken.add(cands[0])
            elif len(cands) > 1:
                deferred.append(rel)
            else:
                rest.append(rel)

        for rel in deferred:
            cands = [c for c in by_base[rel.name] if c not in taken]
            sibling = derive_destination(rel, pairs)
            chosen = next((c for c in cands if sibling is not None and str(c.parent) == sibling), None)
            if chosen is None and len(cands) == 1:
                chosen = cands[0]
            if chosen is None:
                moves.append(rel)
                continue
            pairs.append((rel, chosen, "filename+section"))
            taken.add(chosen)

        for rel in rest:
            stem = stem_of(rel.name)
            cands = [c for c in (by_stem[stem] if stem in by_stem else []) if c not in taken]
            if len(cands) == 1 and named_stems[stem] == 1:
                pairs.append((rel, cands[0], "stem"))
                taken.add(cands[0])
            else:
                moves.append(rel)

    return pairs, moves


def derive_destination(rel: Path, pairs: list[tuple[Path, Path, str]]) -> str | None:
    """The numbered section this page's already-matched siblings went to."""
    counts = Counter(str(target.parent) for source, target, _ in pairs if source.parent == rel.parent)
    if not counts:
        return None
    return counts.most_common(1)[0][0]


def destination_of(rel: Path, pairs: list[tuple[Path, Path, str]]) -> Path:
    if str(rel) in HAND_DESTINATIONS:
        return Path(HAND_DESTINATIONS[str(rel)]) / rel.name
    derived = derive_destination(rel, pairs)
    if derived is None:
        raise ValueError(f"no destination for {rel}: add it to HAND_DESTINATIONS")
    return Path(derived) / rel.name


def segment(text: str) -> list[list[str]]:
    """Split a page into the units a merge may move: a fenced div whole, and
    every other line on its own.

    A div is atomic because half of one is not markdown: inserting an opener
    without its closer makes Pandoc swallow the rest of the page, and a page
    Pandoc cannot read leaves the index, which dangles every link into it.
    """
    lines = text.splitlines()
    blocks: list[list[str]] = []
    index = 0
    while index < len(lines):
        if not DIV_OPEN.match(lines[index]):
            blocks.append([lines[index]])
            index += 1
            continue
        depth = 0
        end = index
        while end < len(lines):
            if DIV_OPEN.match(lines[end]):
                depth += 1
            elif DIV_CLOSE.match(lines[end]):
                depth -= 1
                if depth == 0:
                    break
            end += 1
        blocks.append(lines[index : end + 1])
        index = end + 1
    return blocks


def block_key(block: list[str]) -> str:
    return "".join(key_of(line) for line in block)


def div_depth(text: str) -> int:
    depth = 0
    for line in text.splitlines():
        if DIV_OPEN.match(line):
            depth += 1
        elif DIV_CLOSE.match(line):
            depth -= 1
    return depth


def merge_text(base_text: str, incoming_text: str) -> tuple[str, list[str], list[str]]:
    """Insert everything `incoming` carries that `base` does not, in place.

    Walking `incoming` block by block, a block `base` already holds becomes the
    anchor; a block it does not is buffered and flushed just after that anchor.
    Base text is never reordered, reworded or dropped.
    """
    base_blocks = segment(base_text)
    base_keys = {block_key(block) for block in base_blocks if block_key(block)}
    base_tags = set(TAG.findall(base_text))

    # A footnote label is page-global. When both pages word one statement their
    # own way, both wordings survive the merge and would claim the same label,
    # so the arriving copy gets its own -- reference and definition together.
    taken_labels = set(FOOTNOTE.findall(base_text))
    relabel = {label: f"{label}-qrs" for label in set(FOOTNOTE.findall(incoming_text)) & taken_labels}

    def rename(line: str) -> str:
        return FOOTNOTE.sub(lambda m: f"[^{relabel[m.group(1)]}]" if m.group(1) in relabel else m.group(0), line)

    # Where each key last appears in base, so an insert lands after its anchor.
    anchor_at: dict[str, int] = {}
    for index, block in enumerate(base_blocks):
        key = block_key(block)
        if key:
            anchor_at[key] = index

    inserts: dict[int, list[str]] = {}
    tail: list[str] = []
    pending: list[str] = []
    cursor = len(base_blocks) - 1
    added_lines: list[str] = []
    added_tags: list[str] = []

    def flush(at: int) -> None:
        if not pending:
            return
        if at < 0:
            tail.extend(pending)
        else:
            if at not in inserts:
                inserts[at] = []
            inserts[at].extend(pending)
        pending.clear()

    for block in segment(incoming_text):
        if len(block) == 1 and is_tag_line(block[0]):
            fresh = [tag for tag in TAG.findall(block[0]) if tag not in base_tags]
            if fresh:
                base_tags.update(fresh)
                added_tags.extend(fresh)
                pending.append(" ".join(f"[[{tag}]]" for tag in fresh))
            continue
        key = block_key(block)
        if not key:
            continue
        if key in base_keys:
            flush(cursor)
            cursor = anchor_at[key]
            continue
        clean = [rename(strip_status(line)).rstrip() for line in block]
        pending.extend(clean)
        added_lines.extend(clean)
    flush(cursor)

    out: list[str] = []
    for index, block in enumerate(base_blocks):
        out.extend(block)
        if index in inserts:
            out.append("")
            out.extend(inserts[index])
    if tail:
        out.append("")
        out.extend(tail)
    merged = "\n".join(out).rstrip() + "\n"
    # A merge that splits a div makes Pandoc swallow the rest of the page and
    # drop it from the index, which dangles every link into it. Fail here
    # instead of emitting a page that reads as half its own length.
    if div_depth(merged) != div_depth(base_text):
        raise ValueError("merge changed fenced-div nesting")
    return merged, added_lines, added_tags


def moved_text(text: str) -> str:
    """A moved page keeps its prose verbatim; only the status markers go."""
    return "\n".join(strip_status(line).rstrip() for line in text.splitlines()).rstrip() + "\n"


def status_markers(text: str) -> int:
    return len(STATUS.findall(text))


def run(dry_run: bool) -> int:
    pairs, moves = pair_pages()
    rows: list[dict[str, object]] = []
    tally: Counter[str] = Counter()

    for source, target, how in pairs:
        incoming = (WIKI / source).read_text()
        base = (WIKI / target).read_text()
        merged, added_lines, added_tags = merge_text(base, incoming)
        rows.append(
            {
                "old_route": f"wiki/{source}",
                "new_route": f"wiki/{target}",
                "disposition": "merged",
                "matched_by": how,
                "prose_lines_added": len(added_lines),
                "tags_added": added_tags,
                "status_markers_dropped": status_markers(incoming),
            }
        )
        tally.update(merged=1, lines=len(added_lines), tags=len(added_tags), markers=status_markers(incoming))
        if not dry_run:
            (WIKI / target).write_text(merged)
            (WIKI / source).unlink()

    for source in moves:
        target = destination_of(source, pairs)
        incoming = (WIKI / source).read_text()
        if (WIKI / target).exists():
            # The destination already holds a page of this name, so this is the
            # same page reached by hand rather than by filename: merge, never
            # overwrite.
            merged, added_lines, added_tags = merge_text((WIKI / target).read_text(), incoming)
            rows.append(
                {
                    "old_route": f"wiki/{source}",
                    "new_route": f"wiki/{target}",
                    "disposition": "merged",
                    "matched_by": "hand",
                    "prose_lines_added": len(added_lines),
                    "tags_added": added_tags,
                    "status_markers_dropped": status_markers(incoming),
                }
            )
            tally.update(merged=1, lines=len(added_lines), tags=len(added_tags), markers=status_markers(incoming))
            if not dry_run:
                (WIKI / target).write_text(merged)
                (WIKI / source).unlink()
            continue
        rows.append(
            {
                "old_route": f"wiki/{source}",
                "new_route": f"wiki/{target}",
                "disposition": "moved",
                "matched_by": None,
                "prose_lines_added": None,
                "tags_added": sorted(set(TAG.findall(incoming))),
                "status_markers_dropped": status_markers(incoming),
            }
        )
        tally.update(moved=1, markers=status_markers(incoming))
        if not dry_run:
            (WIKI / target).parent.mkdir(parents=True, exist_ok=True)
            (WIKI / target).write_text(moved_text(incoming))
            (WIKI / source).unlink()

    if not dry_run:
        MERGE_MAP.write_text("".join(json.dumps(row) + "\n" for row in rows))
        for named_root in sorted(NAMED_ROOTS):
            prune(WIKI / named_root)

    print(f"merged {tally['merged']} pages, moved {tally['moved']} pages")
    print(f"prose lines carried over: {tally['lines']}")
    print(f"tags carried over: {tally['tags']}")
    print(f"status markers dropped: {tally['markers']}")
    return 0


def prune(directory: Path) -> None:
    """Remove the emptied named tree, deepest first."""
    if not directory.is_dir():
        return
    for child in sorted(directory.rglob("*"), key=lambda p: len(p.parts), reverse=True):
        if child.is_dir() and not any(child.iterdir()):
            child.rmdir()
    if not any(directory.iterdir()):
        directory.rmdir()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="merge_subject_trees")
    ap.add_argument("--dry-run", action="store_true", help="report the plan without touching the tree")
    args = ap.parse_args(argv)
    return run(args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
