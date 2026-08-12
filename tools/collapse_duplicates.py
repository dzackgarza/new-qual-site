#!/usr/bin/env python3
r"""Collapse duplicate card bodies onto one card and repoint everything at it.

`tools/audit.py --only duplicate-bodies` reports the groups; this retires all but
one card of each group and rewrites every pointer at a retired id -- card
relations, `[[TAG]]` refs in `wiki/`, publication manifests -- so no reference
dangles and no occurrence is lost.

    uv run python tools/collapse_duplicates.py --dry-run
    uv run python tools/collapse_duplicates.py
    uv run python tools/collapse_duplicates.py --repoint-only

`--repoint-only` collapses nothing and repairs references alone; run it after
`tools/import_mmaq.py`, whose regenerated lane can change the id that carries a
statement.

Grouping is by `import_mmaq.loose()`, the fingerprint G2 already uses:
exact text after whitespace, case, TeX macro spelling (`\mathbf{Q}` vs
`\mathbb{Q}`), align-environment spelling and display-math punctuation are
normalized away. PLAN-QUAL-GRUNT-001 rules those are not variants. Nothing is
merged on similarity: two cards group only when that normal form is *equal*.

The survivor is chosen by lane, then by card kind, then by title length: the
`qual-wiki` lane is canonical per the user's 2026-07-22 decision, and among
equals the more specific kind and the more descriptive title carry more of what
a reader needs.

`sources/g3-collapse-map.jsonl` is the retirement record, and it is re-derived
from `HEAD` on every run rather than accumulated: it names every card id `HEAD`
held that the tree no longer does, against the card that now carries its body.
This run's own plan names the survivor for the cards it retires, because the
`HEAD` body of a card a pass edited before collapsing matches nothing on disk.

The run exits non-zero, naming the ids and the files, if any retired id has no
survivor or is still referenced when it finishes. A retired id with no surviving
body is a loss, not a collapse, and an unrepointed reference is what the
pre-push gate would find later, after it has blocked every other workstream.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

import yaml
from import_mmaq import loose
from route_authored_md import BODYLESS_KINDS, _front_matter, _unfence

ROOT = Path(__file__).resolve().parent.parent
COLLAPSE_MAP = ROOT / "sources" / "g3-collapse-map.jsonl"

# `qual-wiki` is canonical. After it, the lane that authored the text outranks
# the lane that copied it, and the two generated lanes rank last because their
# importer re-derives them from whatever the rest of the corpus holds.
LANE_RANK = ["canonical", "wiki", "qrs", "ws9", "authored-md", "flashcards", "hand-authored", "qualbot", "mmaq-total"]
# Among cards in one lane, the kind that names the mathematics most precisely.
KIND_RANK = ["theorem", "definition", "example", "problem", "exercise", "fact", "strategy", "lemma", "hint", "solution"]

# Pointers that predate this pass and already dangle. `P-L72DL` was a
# `corpus/qrs` card until commit 9189f8c stripped the author's status hashtags
# from its body; the strip changed the body, so the card was re-minted under the
# content-derived id `P-JP74P`, whose body is byte-identical to what `P-L72DL`
# held. The compendium sidecar was never updated.
SEED_ALIASES = {"P-L72DL": "P-JP74P"}


def _rank(values: list[str], value: str) -> int:
    return values.index(value) if value in values else len(values)


def read_cards() -> dict[str, tuple[Path, dict, str]]:
    cards: dict[str, tuple[Path, dict, str]] = {}
    for path in sorted((ROOT / "corpus").rglob("*.md")):
        meta, body = _front_matter(path.read_text())
        if meta is None:
            continue
        cards[meta["id"]] = (path, meta, _unfence(body))
    return cards


def plan_collapse(cards: dict[str, tuple[Path, dict, str]]) -> dict[str, str]:
    """Retired id -> survivor id, for every group of loose-equal bodies.

    `BODYLESS_KINDS` is load-bearing here, not a tidy-up. An occurrence card
    carries the body of the problem it instantiates -- that is what the
    occurrence layer is -- so an `O-*` card and its `P-*` card are loose-equal
    by design and are not duplicates. Collapsing on shared body alone would
    retire the whole occurrence layer.
    """
    groups: dict[str, list[str]] = {}
    for card_id, (_, meta, text) in cards.items():
        if meta["kind"] in BODYLESS_KINDS:
            continue
        key = loose(text)
        if key not in groups:
            groups[key] = []
        groups[key].append(card_id)

    retire: dict[str, str] = {}
    for members in groups.values():
        if len(members) < 2:
            continue
        ordered = sorted(
            members,
            key=lambda cid: (
                _rank(LANE_RANK, cards[cid][0].parent.name),
                _rank(KIND_RANK, cards[cid][1]["kind"]),
                -len(cards[cid][1]["title"]),
                cid,
            ),
        )
        survivor = ordered[0]
        for loser in ordered[1:]:
            retire[loser] = survivor
    return retire


def rewrite_relations(cards: dict[str, tuple[Path, dict, str]], alias: dict[str, str]) -> int:
    """Repoint every relation at a retired card, dropping self- and duplicate edges."""
    changed = 0
    for card_id, (path, meta, _) in cards.items():
        if card_id in alias:
            continue
        relations = meta["relations"]
        rewritten: list[dict] = []
        for relation in relations:
            target = relation["target"]
            resolved = alias[target] if target in alias else target
            if resolved == card_id:
                continue
            edge = dict(relation, target=resolved)
            if edge not in rewritten:
                rewritten.append(edge)
        if rewritten == relations:
            continue
        text = path.read_text()
        head, _, tail = text.partition("---\n")
        front, _, body = tail.partition("\n---\n")
        data = yaml.safe_load(front)
        data["relations"] = rewritten
        path.write_text(head + "---\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100).strip() + "\n---\n" + body)
        changed += 1
    return changed


def rewrite_payload_sources(cards: dict[str, tuple[Path, dict, str]], alias: dict[str, str]) -> int:
    """Repoint `payload.source` on occurrence cards whose sitting was retired."""
    changed = 0
    for card_id, (path, meta, _) in cards.items():
        if card_id in alias or "payload" not in meta:
            continue
        source = meta["payload"]["source"] if "source" in meta["payload"] else None
        if source is None or source not in alias:
            continue
        text = path.read_text()
        head, _, tail = text.partition("---\n")
        front, _, body = tail.partition("\n---\n")
        data = yaml.safe_load(front)
        data["payload"]["source"] = alias[source]
        path.write_text(head + "---\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100).strip() + "\n---\n" + body)
        changed += 1
    return changed


def _id_pattern(ids: set[str] | dict[str, str]) -> re.Pattern[str]:
    return re.compile(r"\b(" + "|".join(sorted(map(re.escape, ids), key=len, reverse=True)) + r")\b")


def _resolved_targets() -> list[Path]:
    """The pages and manifests whose card ids `qualc check` resolves.

    Nothing under `sources/` is here, and no name is exempted from that: every
    sidecar is a record of what a pass found, not an index into the tree. Each
    row states its ids together with the columns that describe them at the
    moment it was written -- the file the card was at, its title and kind, the
    sha of the source block, the disposition and the evidence -- so an id
    rewritten to a survivor makes the rest of its own row false. That is what
    happened to `sources/g7-residual.jsonl`: rows reading "this card duplicates
    that survivor" became "the survivor duplicates itself", at a `path` naming
    the file the collapse had just deleted.

    No reader needs the rewrite. `tools/replay_sources.py` compares these rows
    against the tree (`_verify_orphans` requires the residual set to equal the
    orphans the corpus now has) and `tools/attach_pages.py` drops any ledger id
    the corpus no longer holds. A record that has fallen out of step with the
    tree must say so and fail, which a rewritten id would hide.
    """
    return [*sorted((ROOT / "wiki").rglob("*.md")), *sorted((ROOT / "publications").glob("*.yaml"))]


def rewrite_text_references(alias: dict[str, str]) -> dict[str, int]:
    """Rewrite every retired id named in a page or a publication manifest."""
    if not alias:
        return {}
    pattern = _id_pattern(alias)
    counts: dict[str, int] = {}
    for path in _resolved_targets():
        text = path.read_text()
        rewritten = pattern.sub(lambda m: alias[m.group(1)], text)
        if rewritten == text:
            continue
        path.write_text(rewritten)
        counts[str(path.relative_to(ROOT))] = len(pattern.findall(text))
    return counts


def promote_kinds(cards: dict[str, tuple[Path, dict, str]]) -> list[str]:
    r"""Give each survivor the strongest kind its group held.

    One text can be an `exercise` in `qual-wiki` and a `problem` in
    `qual-review-and-solutions`. The lane rule picks the `qual-wiki` card as the
    survivor, but the classification is not the lane's to weaken: an occurrence
    card says the text was set on a qualifying exam, and the schema refuses an
    `instance-of` that does not target a problem. So the survivor keeps the
    canonical body and takes the group's most specific kind.
    """
    if not COLLAPSE_MAP.exists():
        return []
    strongest: dict[str, str] = {}
    for line in COLLAPSE_MAP.read_text().splitlines():
        row = json.loads(line)
        survivor, kind = row["survivor"], row["retired_kind"]
        if survivor not in cards:
            continue
        best = strongest[survivor] if survivor in strongest else cards[survivor][1]["kind"]
        strongest[survivor] = kind if _rank(KIND_RANK, kind) < _rank(KIND_RANK, best) else best

    promoted: list[str] = []
    for survivor, kind in sorted(strongest.items()):
        path, meta, _ = cards[survivor]
        if meta["kind"] == kind:
            continue
        text = path.read_text()
        head, _, tail = text.partition("---\n")
        front, _, body = tail.partition("\n---\n")
        data = yaml.safe_load(front)
        data["kind"] = kind
        path.write_text(head + "---\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100).strip() + "\n---\n" + body)
        promoted.append(f"{survivor}: {meta['kind']} -> {kind}")
    return promoted


def rebuild_map(cards: dict[str, tuple[Path, dict, str]], retire: dict[str, str]) -> list[dict]:
    """Rebuild the retirement map from git: every card id `HEAD` held and the
    tree no longer does, against the card that now carries its body.

    Derived rather than accumulated, so a map is never a partial record of
    however many passes happened to run. A retired card whose body no card now
    holds is reported with `survivor: null` -- that would be a loss, not a
    collapse.

    `retire` is this run's own plan and outranks the fingerprint lookup. The
    lookup asks which working-tree card carries the `HEAD` body, so it answers
    `None` for any card whose body a pass edited before the collapse -- the id
    was then retired with no survivor and every reference to it dangled
    silently. The plan was computed from the working tree and does not have that
    blind spot.
    """
    listing = subprocess.run(
        ["git", "-C", str(ROOT), "ls-tree", "-r", "--name-only", "HEAD", "corpus/"],
        capture_output=True,
        text=True,
        check=True,
    )
    by_fingerprint = {loose(text): card_id for card_id, (_, meta, text) in cards.items() if meta["kind"] not in BODYLESS_KINDS}

    rows: list[dict] = []
    for relative in listing.stdout.splitlines():
        if not relative.endswith(".md"):
            continue
        blob = subprocess.run(["git", "-C", str(ROOT), "show", f"HEAD:{relative}"], capture_output=True, text=True, check=True)
        meta, body = _front_matter(blob.stdout)
        if meta is None or meta["id"] in cards or meta["kind"] in BODYLESS_KINDS:
            continue
        text = _unfence(body)
        planned = meta["id"] in retire
        survivor = retire[meta["id"]] if planned else (by_fingerprint[loose(text)] if loose(text) in by_fingerprint else None)
        if planned:
            reason = "collapsed by this run; the working-tree body was loose-equal to the survivor's"
        elif survivor and cards[survivor][2].strip() == text.strip():
            reason = "exact body"
        else:
            reason = "body differs only in whitespace, blockquote or display-math and TeX macro spelling"
        rows.append(
            {
                "retired": meta["id"],
                "retired_path": relative,
                "retired_kind": meta["kind"],
                "retired_title": meta["title"],
                "survivor": survivor,
                "survivor_path": str(cards[survivor][0].relative_to(ROOT)) if survivor else None,
                "survivor_kind": cards[survivor][1]["kind"] if survivor else None,
                "reason": reason,
            }
        )
    for loser, survivor in sorted(SEED_ALIASES.items()):
        rows.append(
            {
                "retired": loser,
                "retired_path": "corpus/qrs/P-L72DL.md (removed in 9189f8c)",
                "retired_kind": "problem",
                "retired_title": "Let $f: \\RR \\to \\CC$ be continuous with period 1.",
                "survivor": survivor,
                "survivor_path": str(cards[survivor][0].relative_to(ROOT)),
                "survivor_kind": cards[survivor][1]["kind"],
                "reason": "stale pointer; body of the removed card is byte-identical to the survivor's",
            }
        )
    return sorted(rows, key=lambda row: row["retired"])


def dangling_references(cards: dict[str, tuple[Path, dict, str]], retired: set[str]) -> dict[str, list[str]]:
    """File -> the retired ids it still names, after repointing.

    The map and the rewriters can only repoint an id they can name a survivor
    for. This asks the question `qualc check` asks -- does anything the compiler
    resolves still point at a card that is gone -- so the answer arrives here
    rather than as a pre-push failure that blocks every other workstream.
    """
    found: dict[str, list[str]] = {}
    for path, meta, _ in cards.values():
        named = {relation["target"] for relation in meta["relations"]} & retired
        if "payload" in meta and "source" in meta["payload"] and meta["payload"]["source"] in retired:
            named.add(meta["payload"]["source"])
        if named:
            found[str(path.relative_to(ROOT))] = sorted(named)
    if retired:
        pattern = _id_pattern(retired)
        for path in _resolved_targets():
            named = set(pattern.findall(path.read_text()))
            if named:
                found[str(path.relative_to(ROOT))] = sorted(named)
    return found


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="collapse_duplicates")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--promote-kinds-only", action="store_true", help="re-apply kind promotion from an existing collapse map")
    ap.add_argument("--repoint-only", action="store_true", help="re-derive the map from HEAD and repoint references; collapse nothing")
    args = ap.parse_args(argv)

    cards = read_cards()
    if args.promote_kinds_only:
        for line in promote_kinds(cards):
            print(f"    {line}")
        return 0

    retire = plan_collapse(cards)
    print(f"{len(retire)} cards retired into {len(set(retire.values()))} survivors")
    if args.dry_run:
        for loser, survivor in sorted(retire.items()):
            print(f"    {loser} [{cards[loser][0].parent.name}] -> {survivor} [{cards[survivor][0].parent.name}]")
        return 0

    if not args.repoint_only:
        rewrite_relations(cards, {**SEED_ALIASES, **retire})
        rewrite_payload_sources(cards, {**SEED_ALIASES, **retire})
        for loser in retire:
            cards[loser][0].unlink()

    # The map is re-derived from `HEAD`, so it names every id the tree has ever
    # dropped, not only this run's. Repointing from the whole map is what makes
    # a second run finish the job rather than leave the first run's references
    # half-rewritten.
    cards = read_cards()
    rows = rebuild_map(cards, retire)
    lost = [row["retired"] for row in rows if row["survivor"] is None]
    alias = {row["retired"]: row["survivor"] for row in rows if row["survivor"] is not None}
    relations = rewrite_relations(cards, alias)
    payloads = rewrite_payload_sources(cards, alias)
    references = rewrite_text_references(alias)

    COLLAPSE_MAP.write_text("".join(json.dumps(row) + "\n" for row in rows))
    for line in promote_kinds(read_cards()):
        print(f"    promoted {line}")
    print(f"relations rewritten on {relations} cards; payload.source rewritten on {payloads} cards")
    print(f"text references rewritten in {len(references)} files: {sum(references.values())} ids")
    print(f"{len(rows)} retired ids mapped; {len(lost)} with no surviving body: {lost}")

    dangling = dangling_references(read_cards(), {row["retired"] for row in rows})
    if not lost and not dangling:
        return 0
    for path, ids in sorted(dangling.items()):
        print(f"    {path} still names {', '.join(ids)}")
    print(f"tree is inconsistent: {len(lost)} retired ids with no survivor, {len(dangling)} files still naming a retired id")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
