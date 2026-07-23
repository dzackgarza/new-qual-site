#!/usr/bin/env python3
"""One-shot importer: make-me-a-qual YAML -> corpus cards.

Run once to seed the proof of concept. It is not part of the build; the cards
it writes are the authored source from that point on.

Two inferences it makes, both recorded here because the source data cannot
support them directly:

  * No `season` field exists. Where a (university, exam, year) run restarts its
    numbering, the records are treated as separate sittings, since a locator
    reset means a new exam document. Terms stay unknown.
  * Records with `year: 0` or `year: Extra` get `date: {kind: unknown}` rather
    than a sentinel year.
"""

from __future__ import annotations

import base64
import hashlib
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

import panflute as pf
import yaml

from qualc.model import MARKDOWN

ROOT = Path(__file__).resolve().parent.parent
MMAQ = Path("/home/dzack/gitclones/make-me-a-qual/Combined_Questions.yaml")

AREA_SLUG = {
    "Algebra": "algebra",
    "Real_Analysis": "real-analysis",
    "Complex_Analysis": "complex-analysis",
    "Topology": "topology",
}
AREA_ABBR = {"algebra": "ALG", "real-analysis": "RA", "complex-analysis": "CA", "topology": "TOP"}

# The slice. Deliberately spans three areas, two institutions, dated and
# undated sources, and one set of records that are exact duplicates.
SLICE = [
    ("UGA", "Algebra", "2018"),
    ("UGA", "Real_Analysis", "2018"),
    ("UW", "Algebra", "2018"),
    ("UGA", "Complex_Analysis", "Extra"),
]
# Only the duplicate groups from the undated complex analysis pile, so the
# import exercises real deduplication rather than a manufactured example.
CA_DUPES_ONLY = True


def opaque(prefix: str, *parts: str) -> str:
    digest = hashlib.sha1("|".join(parts).encode()).digest()
    return prefix + base64.b32encode(digest).decode()[:5]


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.strip().lower()).strip("-")


def normalize(statement: str) -> str:
    return re.sub(r"\s+", " ", statement or "").strip().lower()


def load_records() -> list[dict]:
    records: list[dict] = yaml.safe_load(MMAQ.read_text())
    for i, r in enumerate(records):
        r["_seq"] = i
        r["_uni"] = str(r["university"]).strip()
        r["_exam"] = str(r["exam"]).strip()
        r["_year"] = str(r["year"]).strip()
        r["_norm"] = normalize(r["question"])
    return records


def select(records: list[dict]) -> list[dict]:
    chosen = []
    for uni, exam, year in SLICE:
        group = [r for r in records if (r["_uni"], r["_exam"], r["_year"]) == (uni, exam, year)]
        if exam == "Complex_Analysis" and CA_DUPES_ONLY:
            counts = Counter(r["_norm"] for r in group)
            wanted = [k for k, v in counts.items() if v > 1][:2]
            group = [r for r in group if r["_norm"] in wanted]
        chosen += group
    return chosen


def split_sittings(group: list[dict]) -> list[list[dict]]:
    """A locator that stops increasing means a new exam document."""
    sittings: list[list[dict]] = []
    last = None
    for r in sorted(group, key=lambda r: r["_seq"]):
        n = r.get("number") or 0
        if last is None or n <= last:
            sittings.append([])
        sittings[-1].append(r)
        last = n
    return sittings


def card(meta: dict, body: str) -> str:
    return "---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100).strip() + "\n---\n\n" + body


def main() -> int:
    records = select(load_records())
    corpus = ROOT / "corpus"
    for sub in ("imports", "canonical"):
        shutil.rmtree(corpus / sub, ignore_errors=True)

    topics: dict[str, str] = {}
    problems: dict[str, dict] = {}  # normalized statement -> problem card meta
    problem_bodies: dict[str, str] = {}
    written_occurrences = 0

    for uni, exam, year in SLICE:
        area = AREA_SLUG[exam]
        group = [r for r in records if (r["_uni"], r["_exam"], r["_year"]) == (uni, exam, year)]
        if not group:
            continue
        sittings = split_sittings(group) if year.isdigit() else [group]
        for si, sitting in enumerate(sittings):
            suffix = f"{uni.upper()}-{AREA_ABBR[area]}-{year if year.isdigit() else 'UNDATED'}"
            if len(sittings) > 1:
                suffix += f"-{chr(ord('A') + si)}"
            source_id = f"SRC-{suffix}"
            date = {"kind": "year", "year": int(year)} if year.isdigit() else {"kind": "unknown"}
            src_dir = corpus / "imports" / "mmaq" / source_id.lower()
            src_dir.mkdir(parents=True, exist_ok=True)
            (src_dir / f"{source_id}.md").write_text(
                card(
                    {
                        "schema": "qual/card@1",
                        "id": source_id,
                        "kind": "source",
                        "title": f"{uni} {exam.replace('_', ' ')}"
                        + (f" {year}" if year.isdigit() else ", undated collection")
                        + (f" (sitting {chr(ord('A') + si)})" if len(sittings) > 1 else ""),
                        "classification": {"areas": [area], "topics": []},
                        "relations": [],
                        "review": "draft",
                        "payload": {
                            "source_kind": "university-exam",
                            "institution": uni.lower(),
                            "area": area,
                            "date": date,
                        },
                    },
                    body_of(
                        "Imported from `make-me-a-qual` `Combined_Questions.yaml`. The exam term is not recorded in that source.",
                        "remark",
                    ),
                )
            )

            seen_here: set[str] = set()
            for i, rec in enumerate(sitting, start=1):
                if rec["_norm"] in seen_here:
                    continue  # duplicate transcription of the same exam item
                seen_here.add(rec["_norm"])
                statement = (rec.get("question") or "").strip()
                tags = [t.strip() for t in (rec.get("tags") or []) if t and t.strip()]
                for t in tags:
                    topics[slug(t)] = t
                topic_ids = [slug(t) for t in tags]

                known = problems.get(rec["_norm"])
                pid = known["id"] if known else opaque("P-", rec["_norm"])
                if known is None:
                    problems[rec["_norm"]] = {
                        "schema": "qual/card@1",
                        "id": pid,
                        "kind": "problem",
                        "title": title_of(statement),
                        "classification": {"areas": [area], "topics": topic_ids},
                        "relations": [],
                        "review": "draft",
                    }
                    problem_bodies[pid] = body_of(statement, "problem")

                locator = str(rec.get("number") or i)
                occ_id = f"O-{suffix}-{int(locator):02d}"
                (src_dir / f"{occ_id}.md").write_text(
                    card(
                        {
                            "schema": "qual/card@1",
                            "id": occ_id,
                            "kind": "occurrence",
                            "title": f"{uni} {exam.replace('_', ' ')}" + (f" {year}" if year.isdigit() else "") + f", problem {locator}",
                            "classification": {"areas": [area], "topics": topic_ids},
                            "relations": [{"kind": "instance-of", "target": pid}],
                            "review": "draft",
                            "payload": {"source": source_id, "locator": locator},
                        },
                        body_of(statement, "problem"),
                    )
                )
                written_occurrences += 1

    canon = corpus / "canonical"
    canon.mkdir(parents=True, exist_ok=True)
    for meta in problems.values():
        (canon / f"{meta['id']}.md").write_text(card(meta, problem_bodies[meta["id"]]))

    write_topics(topics)
    print(f"{len(records)} selected records -> {len(problems)} problems, {written_occurrences} occurrences, {len(topics)} topics")
    return 0


def _text_inlines(blocks: list, include_display: bool) -> list[pf.Inline]:
    """Inlines from the first prose in a statement, descending into lists."""
    out: list[pf.Inline] = []
    for block in blocks:
        if isinstance(block, (pf.Para, pf.Plain)):
            text = [
                pf.Math(i.text, format="InlineMath") if isinstance(i, pf.Math) and i.format == "DisplayMath" else i
                for i in block.content
                if include_display or not (isinstance(i, pf.Math) and i.format == "DisplayMath")
            ]
            if any(pf.stringify(i).strip() for i in text):
                out += ([pf.Space()] if out else []) + text
        elif hasattr(block, "content"):
            nested = _text_inlines(list(block.content), include_display)
            if nested:
                out += ([pf.Space()] if out else []) + nested
        if len(pf.stringify(pf.Plain(*out))) > 72:
            break
    return out


def title_of(statement: str) -> str:
    """A first-pass display title, taken off the AST so math stays math.

    Editorial titles are a curation task; this only has to be recognizable.
    """
    doc = pf.convert_text(statement, input_format=MARKDOWN, output_format="panflute", standalone=True)
    inlines = _text_inlines(list(doc.content), include_display=False)
    if len(pf.stringify(pf.Plain(*inlines)).strip()) < 20:
        # A statement that is mostly displayed formulas has to show one.
        inlines = _text_inlines(list(doc.content), include_display=True)

    kept: list[pf.Inline] = []
    length, cut = 0, None
    for inline in inlines:
        if isinstance(inline, pf.Space):
            cut = len(kept)  # last safe place to stop
        length += len(pf.stringify(inline))
        if length > 72 and cut:
            kept = kept[:cut] + [pf.Str("…")]
            break
        kept.append(inline)

    title: str = pf.convert_text(
        pf.Plain(*kept),
        input_format="panflute",
        output_format="markdown",
        extra_args=["--wrap=none"],
    )
    return title.strip()


def body_of(statement: str, section: str) -> str:
    """Wrap a statement in its semantic div. Written by pandoc, not by hand."""
    blocks = pf.convert_text(statement, input_format=MARKDOWN, output_format="panflute")
    body: str = pf.convert_text(
        pf.Doc(pf.Div(*blocks, classes=[section])),
        input_format="panflute",
        output_format="markdown",
        extra_args=["--wrap=preserve"],
    )
    return body + "\n"


def write_topics(topics: dict[str, str]) -> None:
    path = ROOT / "vocabularies" / "topics.yaml"
    entries = [{"id": k, "name": v} for k, v in sorted(topics.items())]
    path.write_text("# Topics. A registry, not a schema enum: a new topic is a new entry here.\n" + yaml.safe_dump(entries, sort_keys=False, allow_unicode=True))


if __name__ == "__main__":
    sys.exit(main())
