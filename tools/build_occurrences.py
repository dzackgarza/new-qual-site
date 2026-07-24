#!/usr/bin/env python3
"""Turn recorded exam terms into occurrence and source cards.

Every problem the corpus imported from a qual carried an `exam_term` string in
its routing ledger -- "Fall 2015", "Spring '09/Spring '07", "January 2011 3a".
Those strings were recorded and never modelled. This builds the two card kinds
that model them:

  source (SRC-*)      one per distinct sitting: institution, area, and a date
                      the schema can represent (academic-term, year, or unknown).
  occurrence (O-*)    one per (problem, sitting): the problem is `instance-of`
                      nothing -- it *occurred* at the sitting, linked by an
                      `instance-of` relation to the problem card and a
                      `payload.source` pointer to the SRC card.

The occurrence body is a remark, not a copy of the statement: the statement
already lives in the problem card and the relation joins them. Duplicating it
would fork one problem's text across every sitting it appeared in.

Three honest limits, encoded rather than smoothed over:

  season      the schema's academic-term is spring or fall only. January maps to
              spring and November to fall (the sitting, not the calendar month),
              but May, June, and Summer have no representable season, so those
              sittings are year-only. This is the same limit the QualBot May 2021
              images hit.
  institution UCSD-labelled files are ucsd; everything else is uga, resource
              collections included -- `Extra_Questions.md` says outright it is
              the UGA analysis qual, so the file a problem was copied into does
              not change which exam it came from. Only a term that names a course
              event (Midterm, Final, HW) rather than a sitting, or one with no
              year at all, becomes a contributed-artifact source; the schema's
              ContributedArtifact exists for exactly that.
  multiplicity a problem tagged "Fall 2009, Fall 2011" occurred twice. Such
              strings split into one occurrence per sitting.

    uv run python tools/build_occurrences.py <triples.json> <out-dir>
"""

from __future__ import annotations

import base64
import hashlib
import json
import re
import sys
from pathlib import Path

AREA_CODE = {"algebra": "ALG", "real-analysis": "RA", "complex-analysis": "CA", "topology": "TOP"}
# The Prelims are the first-year exam and span areas, so their problem cards
# carry no single area (`areas: []`). Their sittings are still real, so they get
# their own area-agnostic source series rather than being dropped.
PRELIM_CODE = "PRELIM"

# The period a sitting names, as written. UGA labels its algebra/topology/complex
# quals by semester (Spring/Fall) and its analysis qual by month (January, May,
# June). The written label is the source's identity, so it is preserved in the
# SRC id; the schema season is derived from it separately and is deliberately
# lossy, because academic-term is spring-or-fall only.
PERIOD_WORD = re.compile(r"\b(spring|fall|autumn|summer|january|february|march|april|may|june|july|august|september|october|november|december)\b", re.I)
# Period label -> schema season, or None when the schema cannot represent it.
# January is the spring-semester sitting, November the fall one; May/June/Summer
# have no spring/fall home and stay year-only.
SCHEMA_SEASON = {
    "SPRING": "spring", "JANUARY": "spring",
    "FALL": "fall", "AUTUMN": "fall", "NOVEMBER": "fall",
}

COURSE_ARTIFACT = re.compile(r"\b(midterm|final|hw|homework|practice ?exam)\b", re.I)
# A trailing problem locator: "#3", ".4", " 6.1", " 3a", ", 4b", "1b,c", "Challenge 1".
LOCATOR = re.compile(
    r"[\s,]*#?\s*(\d+[a-z]?(?:[.,]\s*\d+[a-z]?)*(?:\s*[a-z]|,\s*[a-z])*|challenge\s*\d*|extended)\s*$",
    re.I,
)
YEAR = re.compile(r"\b(19|20)\d{2}\b")
APOS_YEAR = re.compile(r"\b(spring|fall|autumn)\s*'\s*(\d{2})\b", re.I)


def _b32(s: str, n: int) -> str:
    return base64.b32encode(hashlib.sha1(s.encode()).digest()).decode()[:n]


def institution(src_path: str) -> str:
    """Which department the sitting belongs to.

    Only the UCSD topology sets are non-UGA. Everything else in these repos is a
    UGA qual -- including the resource collections: `Extra_Questions.md` states
    outright that it is worked solutions to the UGA analysis qual ("May 2016
    Qual"), so its month-labelled sittings are UGA sittings, not a foreign
    calendar. The file a problem was written down in does not change which exam
    it came from.
    """
    if "UCSD" in src_path:
        return "ucsd"
    # WS9 extraction paths encode the institution: ws9/<inst>/<doc>.
    m = re.search(r"(?:^|/)ws9/(ucla|jhu|tamu|ucsd|uga)/", src_path)
    if m:
        return m.group(1)
    return "uga"


def parse_term(term: str) -> list[dict]:
    """One exam_term string -> a list of sittings, each with an optional locator.

    Each sitting: {season, year, locator, artifact}. artifact is a free string
    when the term names a course event (a midterm, a homework) rather than a
    datable sitting; then season/year are still parsed if present.
    """
    out: list[dict] = []
    # A problem may be tagged with several sittings; the separators seen in the
    # corpus are comma, semicolon and slash. Split, but keep "6b" style locators
    # that use a comma from being torn apart: only split on separators that sit
    # before another season/year-looking piece.
    parts = re.split(r"\s*[;/]\s*|\s*,\s*(?=(?:Spring|Fall|Autumn|January|June|May|November|\d{4}|['’]\d2))", term)
    for raw in parts:
        piece = raw.strip()
        if not piece:
            continue
        artifact = piece if COURSE_ARTIFACT.search(piece) else ""
        # Expand "'09" to a full year first, so it is read as the year and not
        # mistaken for a trailing problem locator.
        piece = APOS_YEAR.sub(lambda x: f"{x.group(1)} 20{x.group(2)}", piece)
        piece = re.sub(r"\b20202\b", "2020", piece)  # a real source typo, 18 times
        pm = PERIOD_WORD.search(piece)
        period = pm.group(1).upper() if pm else ("SUMMER" if "summer" in piece.lower() else None)
        ym = YEAR.search(piece)
        year = int(ym.group()) if ym else None
        # The locator is whatever problem-number trails the year, once course
        # words are removed: "January 2005 3b" -> "3b", "May 2016, 1" -> "1",
        # "Fall 2019 Midterm #7" -> "7", "2010 6.1" -> "6.1".
        rest = piece[ym.end():] if ym else piece
        rest = re.sub(r"\b(midterm|final|hw|homework|practice ?exam|exam|challenge|qual)\b", " ", rest, flags=re.I)
        lm = re.search(r"(\d+[a-z]?(?:[.,]\s*\d+[a-z]?)*)", rest)
        locator = re.sub(r"\s+", "", lm.group(1)) if lm else ""
        out.append({"period": period, "year": year, "locator": locator, "artifact": artifact})
    return out


def date_spec(period: str | None, year: int | None) -> dict:
    season = SCHEMA_SEASON.get(period or "")
    if season and year:
        return {"kind": "academic-term", "term": season, "year": year}
    if year:
        return {"kind": "year", "year": year}
    return {"kind": "unknown"}


def source_card(inst: str, kind: str, area: str | None, period, year, artifact: str) -> tuple[str, dict]:
    ac = AREA_CODE.get(area, PRELIM_CODE)
    areas = [area] if area else []
    if kind == "contributed-artifact":
        # A course event (midterm, homework) rather than a sitting. Its written
        # description is its provenance; a date is attached when one was given.
        slug = _b32(f"{artifact}|{area}|{period}|{year}", 6)
        sid = f"SRC-{ac}-ART-{slug}"
        payload = {"source_kind": "contributed-artifact",
                   "provenance": artifact or "origin unrecorded",
                   "date": date_spec(period, year)}
        title = f"{artifact or 'Contributed problem'} ({area or 'prelim'})"
    else:
        # The id carries the written period (SPRING, MAY, ...) so two sittings in
        # one year -- a January and a May analysis qual -- stay distinct even
        # though the schema date can only say the year for one of them.
        tag = "-".join(x for x in (period, str(year) if year else None) if x) or "UNDATED"
        sid = f"SRC-{inst.upper()}-{ac}-{tag}"
        payload = {"source_kind": "university-exam", "institution": inst,
                   "area": area or "prelim", "date": date_spec(period, year)}
        label = " ".join(x for x in (period.title() if period else None, str(year) if year else None) if x) or "undated"
        title = f"{inst.upper()} {area or 'prelim'} {label}"
    card = {
        "schema": "qual/card@1", "id": sid, "kind": "source", "title": title,
        "classification": {"areas": areas, "topics": []}, "relations": [],
        "review": "draft", "payload": payload,
    }
    body = f"::: remark\n{title}. Recorded from the source corpus' exam-term annotations.\n:::\n"
    return sid, {"card": card, "body": body}


def occurrence_card(problem_tag: str, area: str | None, src_id: str, locator: str, sitting_label: str) -> tuple[str, dict]:
    oid = "O-" + _b32(f"{problem_tag}|{src_id}|{locator}", 10)
    card = {
        "schema": "qual/card@1", "id": oid, "kind": "occurrence",
        "title": f"{problem_tag} at {sitting_label}",
        "classification": {"areas": [area] if area else [], "topics": []},
        "relations": [{"kind": "instance-of", "target": problem_tag}],
        "review": "draft",
        "payload": {"source": src_id, "locator": locator or "?"},
    }
    loc = f", problem {locator}" if locator else ""
    body = f"::: remark\n[[{problem_tag}]] appeared at {sitting_label}{loc}.\n:::\n"
    return oid, {"card": card, "body": body}


def render(card: dict, body: str) -> str:
    import io
    # Deterministic YAML by hand: the schema is small and fixed, and this avoids
    # a yaml dependency reordering keys between runs.
    def block(d, indent=0):
        pad = "  " * indent
        s = ""
        for k, v in d.items():
            if isinstance(v, dict):
                s += f"{pad}{k}:\n" + block(v, indent + 1)
            elif isinstance(v, list):
                if not v:
                    s += f"{pad}{k}: []\n"
                else:
                    s += f"{pad}{k}:\n"
                    for item in v:
                        if isinstance(item, dict):
                            first = True
                            for ik, iv in item.items():
                                lead = "- " if first else "  "
                                s += f"{pad}{lead}{ik}: {yaml_scalar(iv)}\n"
                                first = False
                        else:
                            s += f"{pad}- {yaml_scalar(item)}\n"
            else:
                s += f"{pad}{k}: {yaml_scalar(v)}\n"
        return s
    def yaml_scalar(v):
        if isinstance(v, bool):
            return "true" if v else "false"
        if isinstance(v, int):
            return str(v)
        if v is None:
            return "null"
        sv = str(v)
        # Quote when the value would be mis-parsed unquoted: a YAML indicator at
        # the start (`?`, `-`, `:` ...), embedded `: `, edge whitespace, a bare
        # keyword, or anything that reads as a number or bool. Occurrence
        # locators like "?", "10.1", "3a" all fall here and must stay strings.
        needs_quote = (
            not sv
            or sv[0] in "!&*[]{}#|>@`\"'%,?-:"
            or ":" in sv          # any colon can start a nested mapping in YAML
            or sv.strip() != sv
            or sv.lower() in ("null", "true", "false", "yes", "no", "~")
            or re.fullmatch(r"-?\d+(\.\d+)?", sv) is not None
        )
        if needs_quote:
            return '"' + sv.replace("\\", "\\\\").replace('"', '\\"') + '"'
        return sv
    return "---\n" + block(card) + "---\n\n" + body


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    triples = json.loads(Path(argv[0]).read_text())
    out = Path(argv[1])
    (out / "corpus").mkdir(parents=True, exist_ok=True)

    sources: dict[str, dict] = {}
    occurrences: dict[str, dict] = {}
    dropped: list[dict] = []

    for t in triples:
        area = t["area"]  # None for Prelims, which span areas; handled downstream
        inst = institution(t["src"])
        for sit in parse_term(t["exam_term"]):
            period, year = sit["period"], sit["year"]
            # A course event (midterm/HW) or an undatable string is a
            # contributed-artifact; a datable sitting is a university exam.
            if sit["artifact"]:
                k, art = "contributed-artifact", sit["artifact"]
            elif year is None:
                k, art = "contributed-artifact", t["exam_term"]
            else:
                k, art = "university-exam", ""
            sid, sc = source_card(inst, k, area, period, year, art)
            sources.setdefault(sid, sc)
            label = sc["card"]["title"]
            oid, oc = occurrence_card(t["card"], area, sid, sit["locator"], label)
            occurrences.setdefault(oid, oc)

    for sid, sc in sources.items():
        (out / "corpus" / f"{sid}.md").write_text(render(sc["card"], sc["body"]))
    for oid, oc in occurrences.items():
        (out / "corpus" / f"{oid}.md").write_text(render(oc["card"], oc["body"]))

    print(f"{len(sources)} source cards, {len(occurrences)} occurrence cards -> {out}")
    if dropped:
        print(f"{len(dropped)} triples dropped (no area)")
    # audit summary of date kinds
    from collections import Counter
    kinds = Counter(sc["card"]["payload"].get("source_kind") for sc in sources.values())
    dates = Counter(sc["card"]["payload"]["date"]["kind"] for sc in sources.values())
    print("source kinds:", dict(kinds))
    print("date kinds:  ", dict(dates))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
