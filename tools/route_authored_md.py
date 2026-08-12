#!/usr/bin/env python3
r"""Route the authored markdown that was dispositioned `dropped` in error.

`sources/migration-ledger.jsonl` carried 32 rows under
`dropped / "authored .md not routed (index/config/personal)"`. That reason is
false of most of them: they hold qualifying-exam problems, homework compendia
and review-doc exercises in markdown. This routes the statements they hold and
rewrites each of the 32 rows to a disposition that is true of its file.

    uv run python tools/route_authored_md.py

Matching is by exact normalized fingerprint against three already-migrated
surfaces -- the pinned MakeMeAQual YAML rows, every corpus card body, and every
fenced div in `wiki/`. A statement that matches is already in the corpus and is
not minted again. Nothing is merged on similarity.

Two renderings of one statement can differ by TeX spelling alone: these `.md`
files came out of pandoc with `\mathbf{Q}` and `$$\begin{aligned}` where the
YAML rows carry `\mathbb{Q}` and `\begin{align*}`. PLAN-QUAL-GRUNT-001 G3 rules
that macro-spelling and whitespace differences are not variants, so `loose()`
applies exactly that rule -- as equality, never as a similarity threshold.

Bodies are the source text, verbatim, inside a fenced div. The compiler
normalizes; this does not rewrite an author's wording.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import re
import shutil
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path
from typing import TypedDict

from card_titles import title_of

import yaml
from import_mmaq import _source_bytes, loose, normalize

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "corpus/imports/authored-md"
LEDGER = ROOT / "sources/migration-ledger.jsonl"
ROUTING_NOTE = ROOT / "sources/authored-md-routing.jsonl"

MMAQ = Path.home() / "gitclones/make-me-a-qual"
QRS_DEFAULT = Path.home() / "gitclones/qual-review-and-solutions"

MISDROPPED = "authored .md not routed (index/config/personal)"


# --- reading source repos ---------------------------------------------------


def blob(repo: Path, path: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), "show", f"HEAD:{path}"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise FileNotFoundError(f"{repo}:{path} is not readable from HEAD: {result.stderr.strip()}")
    return result.stdout


# --- fingerprints -----------------------------------------------------------

BODYLESS_KINDS = {"source", "occurrence"}


def _front_matter(text: str) -> tuple[dict | None, str]:
    if not text.startswith("---\n"):
        return None, text
    pieces = text.split("---\n", 2)
    if len(pieces) != 3:
        return None, text
    data = yaml.safe_load(pieces[1])
    return (data if isinstance(data, dict) else None), pieces[2]


def _unfence(body: str) -> str:
    body = re.sub(r"^:::+\s*(?:\{\.[^}]*\}|\w+)\s*\n", "", body.strip())
    return re.sub(r"\n:::+\s*$", "", body).strip()


def corpus_index(root: Path, exclude: Path) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Every card body already in the corpus, by exact and by loose fingerprint."""
    exact: dict[str, list[str]] = {}
    lax: dict[str, list[str]] = {}
    for path in sorted((root / "corpus").rglob("*.md")):
        if exclude in path.parents:
            continue
        meta, body = _front_matter(path.read_text())
        if meta is None or meta.get("kind") in BODYLESS_KINDS:
            continue
        text = _unfence(body)
        for table, key in ((exact, normalize(text)), (lax, loose(text))):
            if key not in table:
                table[key] = []
            table[key].append(meta["id"])
    return exact, lax


def wiki_index(root: Path) -> dict[str, str]:
    """Every fenced div still living in a wiki page."""
    found: dict[str, str] = {}
    for path in sorted((root / "wiki").rglob("*.md")):
        for match in re.finditer(r":::+[^\n]*\n(.*?)\n:::+", path.read_text(), re.S):
            found.setdefault(loose(match.group(1)), str(path.relative_to(root)))
    return found


def yaml_index(root: Path) -> tuple[dict[str, dict], dict[str, dict]]:
    data, source = _source_bytes(root, None)
    rows = yaml.safe_load(data)
    exact: dict[str, dict] = {}
    lax: dict[str, dict] = {}
    for row in rows:
        exact.setdefault(normalize(row["question"]), row)
        lax.setdefault(loose(row["question"]), row)
    return exact, lax


# --- splitting authored files ----------------------------------------------


def _strip_yaml(text: str) -> str:
    if text.startswith("---\n"):
        pieces = text.split("---\n", 2)
        if len(pieces) == 3:
            return pieces[2]
    return text


def by_heading(text: str, pattern: str) -> list[tuple[str, str]]:
    marks = list(re.finditer(pattern, text, re.M))
    out = []
    for index, mark in enumerate(marks):
        end = marks[index + 1].start() if index + 1 < len(marks) else len(text)
        body = text[mark.end() : end].strip()
        # A trailing heading opens the next section; it is not part of this statement.
        while body and re.match(r"^#{1,6}\s", body.splitlines()[-1]):
            body = "\n".join(body.splitlines()[:-1]).strip()
        if body:
            out.append((mark.group(1).strip(), body))
    return out


def _unindent_item(chunk: str) -> str:
    """Drop the `N.` marker and the continuation indent it induces.

    The marker is list structure, not statement text: the YAML rows holding the
    same problems carry the body without it.
    """
    lines = chunk.splitlines()
    head = re.sub(r"^\d+\.\s+", "", lines[0])
    indent = len(lines[0]) - len(head)
    rest = [line[indent:] if line[:indent].strip() == "" else line.lstrip() for line in lines[1:]]
    return "\n".join([head, *rest]).strip()


def by_ordered_list(text: str) -> list[tuple[str, str]]:
    lines = text.splitlines()
    starts = [i for i, line in enumerate(lines) if re.match(r"^\d+\.\s+\S", line)]
    out = []
    for index, start in enumerate(starts):
        end = starts[index + 1] if index + 1 < len(starts) else len(lines)
        chunk = "\n".join(lines[start:end]).rstrip()
        marker = re.match(r"^(\d+)\.", lines[start])
        assert marker is not None  # `starts` only holds lines this matches
        number = marker.group(1)
        if chunk:
            out.append((number, _unindent_item(chunk)))
    return out


def sectioned_ordered_list(text: str, heading: str) -> list[tuple[str, str]]:
    return [(f"{section} {number}", chunk) for section, body in by_heading(text, heading) for number, chunk in by_ordered_list(body)]


def setext_sectioned(text: str) -> list[tuple[str, str]]:
    """`Area\\n====`, then `Subject\\n----`, then ordered lists (Emory's main.md)."""
    lines = text.splitlines()
    area = subject = ""
    out: list[tuple[str, str]] = []
    buffer: list[str] = []

    def flush() -> None:
        if not buffer:
            return
        for number, chunk in by_ordered_list("\n".join(buffer)):
            out.append((f"{area} / {subject} {number}", chunk))
        buffer.clear()

    index = 0
    while index < len(lines):
        following = lines[index + 1] if index + 1 < len(lines) else ""
        if lines[index].strip() and re.fullmatch(r"=+", following.strip() or "x"):
            flush()
            area, subject = lines[index].strip(), ""
            index += 2
            continue
        if lines[index].strip() and re.fullmatch(r"-{2,}", following.strip() or "x"):
            flush()
            subject = lines[index].strip()
            index += 2
            continue
        buffer.append(lines[index])
        index += 1
    flush()
    return out


def by_rule(text: str) -> list[tuple[str, str]]:
    """`# Term Year` sections whose statements are separated by `---`."""
    out = []
    for section, body in by_heading(text, r"^\s*#\s+(\S+ \d{4})\s*$"):
        number = 0
        for piece in re.split(r"^\s*---\s*$", body, flags=re.M):
            piece = piece.strip()
            if piece:
                number += 1
                out.append((f"{section} {number}", piece))
    return out


def review_doc_items(text: str) -> list[tuple[str, str, str]]:
    """Fenced divs and top-level bullets of a review doc, with their heading path."""
    out: list[tuple[str, str, str]] = []
    lines = text.splitlines()
    index = 0
    section: list[str] = []
    while index < len(lines):
        line = lines[index]
        heading = re.match(r"^(#{1,6})\s+(.*)", line)
        if heading:
            level = len(heading.group(1))
            section = section[: level - 1] + [heading.group(2).strip()]
            index += 1
            continue
        opened = re.match(r"^:::+\s*\{?\.?(\w+)", line)
        if opened:
            cursor = index + 1
            depth = 1
            buffer = []
            while cursor < len(lines):
                if re.match(r"^:::+\s*\{?\.?\w", lines[cursor]):
                    depth += 1
                elif re.match(r"^:::+\s*$", lines[cursor]):
                    depth -= 1
                    if depth == 0:
                        break
                buffer.append(lines[cursor])
                cursor += 1
            out.append((" / ".join(section), opened.group(1), "\n".join(buffer).strip()))
            index = cursor + 1
            continue
        if re.match(r"^-\s+\S", line):
            cursor = index + 1
            buffer = [line]
            while cursor < len(lines) and not re.match(r"^-\s+\S|^#|^:::", lines[cursor]) and (not lines[cursor].strip() or lines[cursor].startswith(("  ", "\t"))):
                if not lines[cursor].strip() and (cursor + 1 >= len(lines) or not lines[cursor + 1].startswith(("  ", "\t"))):
                    break
                buffer.append(lines[cursor])
                cursor += 1
            body = re.sub(r"^-\s+", "", "\n".join(buffer).rstrip())
            out.append((" / ".join(section), "bullet", re.sub(r"^  ", "", body, flags=re.M).strip()))
            index = cursor
            continue
        index += 1
    return [item for item in out if item[2].strip()]


# --- the files ---------------------------------------------------------------

# Justin's file names three figures by their bare filename; all three are already
# vendored under `assets/`, so the reference is repointed rather than dropped.
JUSTIN_ASSETS = "../../../assets/40_Topology/650_UCSD_Qual_Questions/Quals/assets"

Splitter = Callable[[str], list[tuple[str, str]]]

SITTING_FILES: dict[str, tuple[str, Splitter]] = {
    "Questions/Complex_Analysis/UGA/AllQuestions.md": ("complex-analysis", by_rule),
    "Questions/Topology/UGA/MikeProblems.md": (
        "topology",
        lambda text: by_heading(text, r"^##\s+(\d+\s*\([^)]*\)\.?)\s*$"),
    ),
    "Questions/Topology/UCSD/Fall 2017 Final.md": (
        "topology",
        lambda text: by_heading(text, r"^#\s+(\d+)\s*$"),
    ),
}
for _year in range(2014, 2020):
    for _term in ("Spring", "Fall"):
        SITTING_FILES[f"Questions/Real_Analysis/UGA/sections/{_year} {_term}.md"] = (
            "real-analysis",
            lambda text: by_heading(text, r"^##\s+(\d+)\.?\s*$"),
        )


# Files with no exam sitting: each mints one contributed-artifact source card,
# whose required `provenance` is where the file's authorship attribution lives.
class Collection(TypedDict):
    area: str
    splitter: Splitter
    id: str
    title: str
    provenance: str


COLLECTION_FILES: dict[str, Collection] = {
    "Questions/Algebra/Extra/UCSD Algebra HW Questions.md": {
        "area": "algebra",
        "splitter": lambda text: sectioned_ordered_list(_strip_yaml(text), r"^#\s+(\w+)\s*$"),
        "id": "SRC-UCSD-ALG-200A-HOMEWORK",
        "title": "UCSD Math 200A Homework Question Compendium",
        "provenance": ('make-me-a-qual `Questions/Algebra/Extra/UCSD Algebra HW Questions.md`, titled "Math 200A Homework Question Compendium". The file names no author.'),
    },
    "Questions/Topology/UCSD/Justin's Problems.md": {
        "area": "topology",
        "splitter": lambda text: sectioned_ordered_list(_strip_yaml(text), r"^##\s+(.+?)\s*$"),
        "id": "SRC-UCSD-TOP-JUSTIN",
        "title": "UCSD Topology Qual Problems (Justin)",
        "provenance": (
            "make-me-a-qual `Questions/Topology/UCSD/Justin's Problems.md`, titled "
            '"Topology Qual Problems"; attributed to Justin by the filename, which is '
            "the only attribution the file carries."
        ),
    },
    "Questions/Archive/Emory/main.md": {
        "area": "complex-analysis",
        "splitter": lambda text: setext_sectioned(_strip_yaml(text)),
        "id": "SRC-EMORY-CA-ARANGO",
        "title": "Emory Quals, collected by Santiago Arango (complex analysis)",
        "provenance": ("make-me-a-qual `Questions/Archive/Emory/main.md`, whose front matter reads `title: Emory Quals` / `author: Santiago Arango`."),
    },
}

AREA_ABBR = {"algebra": "ALG", "real-analysis": "RA", "complex-analysis": "CA", "topology": "TOP"}
TERM_WORD = {"spring": "SPRING", "fall": "FALL"}


def sitting_id(path: str, locator: str) -> str:
    """The existing `source` card for the sitting this statement's file names."""
    if path.startswith("Questions/Real_Analysis/UGA/sections/"):
        year, term = Path(path).stem.split()
        return f"SRC-UGA-RA-{term.upper()}-{year}"
    if path == "Questions/Topology/UCSD/Fall 2017 Final.md":
        return "SRC-UCSD-TOP-FALL-2017"
    if path == "Questions/Complex_Analysis/UGA/AllQuestions.md":
        term, year, _ = locator.split()
        return f"SRC-UGA-CA-{term.upper()}-{year}"
    if path == "Questions/Topology/UGA/MikeProblems.md":
        match = re.search(r"\((\w+) '(\d\d)", locator)
        if match is None:
            raise ValueError(f"MikeProblems locator names no term: {locator!r}")
        term = match.group(1).lower()
        return f"SRC-UGA-TOP-{TERM_WORD[term]}-{2000 + int(match.group(2))}"
    raise ValueError(f"no sitting rule for {path}")


# The Algebra review doc is not only an aggregate of its `sections/`: it carries
# an `# Extra Problems` chapter that exists nowhere else in either repo.
ALGEBRA_REVIEW_DOC = "Algebra/Review Doc/AlgebraQualNotes.md"
CARD_KINDS = {
    "problem",
    "exercise",
    "solution",
    "hint",
    "definition",
    "theorem",
    "proposition",
    "corollary",
    "lemma",
    "proof",
    "example",
}


# --- writing cards -----------------------------------------------------------


def opaque(prefix: str, statement: str) -> str:
    digest = hashlib.sha1(statement.encode("utf-8")).digest()
    return prefix + base64.b32encode(digest).decode("ascii").rstrip("=")[:8]


def card(meta: dict, kind: str, body: str) -> str:
    front = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100).strip()
    return f"---\n{front}\n---\n\n:::{{.{kind}}}\n{body.rstrip()}\n:::\n"


def envelope(card_id: str, kind: str, title: str, area: str) -> dict:
    return {
        "schema": "qual/card@1",
        "id": card_id,
        "kind": kind,
        "title": title,
        "classification": {"areas": [area], "topics": []},
        "relations": [],
        "review": "draft",
    }


# --- the run -----------------------------------------------------------------


Indexes = tuple[dict[str, dict], dict[str, dict], dict[str, list[str]], dict[str, list[str]], dict[str, str]]


def classify(statement: str, indexes: Indexes) -> tuple[str, str]:
    """`new`, or the surface that already carries this statement."""
    yaml_exact, yaml_loose, card_exact, card_loose, wiki = indexes
    key, lax = normalize(statement), loose(statement)
    if key in yaml_exact:
        row = yaml_exact[key]
        return "exact", f"make-me-a-qual YAML row {row['university']} {row['exam']} {row['year']} n={row['number']}"
    if key in card_exact:
        return "exact", f"card {card_exact[key][0]}"
    if lax in yaml_loose:
        row = yaml_loose[lax]
        return "macro-twin", f"make-me-a-qual YAML row {row['university']} {row['exam']} {row['year']} n={row['number']}"
    if lax in card_loose:
        return "macro-twin", f"card {card_loose[lax][0]}"
    if lax in wiki:
        return "macro-twin", f"wiki page {wiki[lax]}"
    return "new", ""


def run(root: Path, qrs: Path) -> dict:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    yaml_exact, yaml_loose = yaml_index(root)
    card_exact, card_loose = corpus_index(root, OUTPUT)
    wiki = wiki_index(root)
    indexes = (yaml_exact, yaml_loose, card_exact, card_loose, wiki)

    used = {card_id for ids in card_exact.values() for card_id in ids}
    notes: list[dict] = []
    report: dict[str, dict] = {}
    occurrence = 0

    def mint(kind: str, area: str, body: str) -> str:
        card_id = opaque("P-AMD-" if kind == "problem" else "E-AMD-", loose(body))
        while card_id in used:
            card_id = opaque("P-AMD-" if kind == "problem" else "E-AMD-", loose(body) + card_id)
        used.add(card_id)
        (OUTPUT / f"{card_id}.md").write_text(card(envelope(card_id, kind, title_of(body), area), kind, body))
        return card_id

    def account(path: str, locator: str, verdict: str, evidence: str, minted: str = "") -> None:
        notes.append(
            {
                "path": path,
                "locator": locator,
                "verdict": verdict,
                "evidence": evidence,
                "card": minted,
                "sha1": hashlib.sha1(locator.encode()).hexdigest()[:12],
            }
        )

    def tally(path: str) -> dict:
        if path not in report:
            report[path] = {"statements": 0, "exact": 0, "macro-twin": 0, "minted": []}
        return report[path]

    # --- make-me-a-qual: files that name their exam sitting
    for path, (area, splitter) in SITTING_FILES.items():
        counts = tally(path)
        for locator, statement in splitter(blob(MMAQ, path)):
            counts["statements"] += 1
            verdict, evidence = classify(statement, indexes)
            if verdict != "new":
                counts[verdict] += 1
                account(path, locator, verdict, evidence)
                continue
            problem = mint("problem", area, statement)
            occurrence += 1
            occurrence_id = f"O-AMD-{occurrence:05d}"
            meta = envelope(occurrence_id, "occurrence", f"{title_of(statement)} ({locator})", area)
            meta["relations"] = [{"kind": "instance-of", "target": problem}]
            meta["payload"] = {"source": sitting_id(path, locator), "locator": locator}
            (OUTPUT / f"{occurrence_id}.md").write_text(card(meta, "problem", statement))
            counts["minted"] += [problem, occurrence_id]
            account(path, locator, "minted", f"sitting {meta['payload']['source']}", problem)

    # --- make-me-a-qual: collections with no sitting
    for path, spec in COLLECTION_FILES.items():
        counts = tally(path)
        minted_here = []
        for locator, statement in spec["splitter"](blob(MMAQ, path)):
            counts["statements"] += 1
            verdict, evidence = classify(statement, indexes)
            if verdict != "new":
                counts[verdict] += 1
                account(path, locator, verdict, evidence)
                continue
            if path.endswith("Justin's Problems.md"):
                statement = re.sub(
                    r"!\[([^\]]*)\]\(([^)/]+\.png)\)",
                    lambda m: f"![{m.group(1)}]({JUSTIN_ASSETS}/{m.group(2).replace(' ', '%20')})",
                    statement,
                )
            problem = mint("problem", spec["area"], statement)
            occurrence += 1
            occurrence_id = f"O-AMD-{occurrence:05d}"
            meta = envelope(occurrence_id, "occurrence", f"{title_of(statement)} ({locator})", spec["area"])
            meta["relations"] = [{"kind": "instance-of", "target": problem}]
            meta["payload"] = {"source": spec["id"], "locator": locator}
            (OUTPUT / f"{occurrence_id}.md").write_text(card(meta, "problem", statement))
            counts["minted"] += [problem, occurrence_id]
            minted_here.append(problem)
            account(path, locator, "minted", f"collection {spec['id']}", problem)
        if minted_here:
            source_meta = envelope(spec["id"], "source", spec["title"], spec["area"])
            source_meta["payload"] = {
                "source_kind": "contributed-artifact",
                "provenance": spec["provenance"],
                "date": {"kind": "unknown"},
            }
            (OUTPUT / f"{spec['id']}.md").write_text(card(source_meta, "remark", f"Collected statements routed from {path}; {len(minted_here)} cards."))
            counts["minted"].append(spec["id"])

    # --- qual-review-and-solutions: the Algebra review doc's Extra Problems
    counts = tally(ALGEBRA_REVIEW_DOC)
    sections = loose(
        " ".join(
            blob(qrs, name)
            for name in subprocess.run(
                ["git", "-C", str(qrs), "ls-files", "Algebra/Review Doc/sections"],
                capture_output=True,
                text=True,
                check=True,
            ).stdout.splitlines()
            if name.endswith(".md")
        )
    )
    unrouted: list[str] = []
    for section, kind, body in review_doc_items(blob(qrs, ALGEBRA_REVIEW_DOC)):
        counts["statements"] += 1
        if loose(body) in sections:
            counts["exact"] += 1
            account(ALGEBRA_REVIEW_DOC, section, "exact", "already migrated with Algebra/Review Doc/sections")
            continue
        verdict, evidence = classify(body, indexes)
        if verdict != "new":
            counts[verdict] += 1
            account(ALGEBRA_REVIEW_DOC, section, verdict, evidence)
            continue
        target = "exercise" if kind == "bullet" else kind
        if re.search(r"^\[\^[^\]]+\]:", body, re.M):
            # A block whose text defines a document footnote does not stand alone
            # as a card: the reference resolves against the page, not the card.
            # (It also crashes flowmark, which cannot format a footnote inside a
            # fenced div -- worth an upstream issue, but not the reason here.)
            unrouted.append(f"{section} [{kind}, defines a footnote]")
            account(ALGEBRA_REVIEW_DOC, section, "not-self-contained", f"{kind} block defining a document footnote")
            continue
        if target not in CARD_KINDS:
            # `remark`/`fact` are wiki prose, not card kinds. Left for the tree
            # merge rather than forced into a card shape that does not fit.
            unrouted.append(f"{section} [{kind}]")
            account(ALGEBRA_REVIEW_DOC, section, "not-a-card-kind", f"{kind} block; belongs to a wiki page")
            continue
        card_id = mint(target, "algebra", body)
        counts["minted"].append(card_id)
        account(ALGEBRA_REVIEW_DOC, section, "minted", f"{target} from the review doc", card_id)
    report[ALGEBRA_REVIEW_DOC]["unrouted"] = unrouted

    ROUTING_NOTE.write_text("".join(json.dumps(note, sort_keys=True) + "\n" for note in notes))
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="route_authored_md")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--qrs", type=Path, default=QRS_DEFAULT, help="clone of qual-review-and-solutions")
    args = parser.parse_args(argv)
    report = run(args.root.resolve(), args.qrs.resolve())
    total = 0
    for path, counts in report.items():
        total += len(counts["minted"])
        print(f"{counts['statements']:4d} statements  {counts['exact']:4d} exact  {counts['macro-twin']:3d} macro-twin  {len(counts['minted']):4d} cards  {path}")
    print(f"{total} cards written to {OUTPUT.relative_to(ROOT)}")
    (OUTPUT / "manifest.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
