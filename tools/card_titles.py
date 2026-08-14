"""One derivation of a card title, and one measure of when a title fails a reader.

Four importers each grew their own `title_of`, and all four took the first
non-empty *line* of the statement. A qualifying-exam problem opens by naming its
objects and then displays them, so that first line is `Let`, `Show that`, or
`Prove that` far more often than it is a sentence: 29 cards were titled exactly
`Let`. `/problems.html` sorts its rows by title, so those fragments occupied the
opening screen of the problem browser.

A title here is never written for the card. It is the opening of the statement,
in the statement's own words, and it is cut only where the cut leaves something a
reader can read:

* display math is inlined rather than dropped -- a statement whose subject is an
  integral has nothing else to be titled by;
* units accumulate until the title carries `FLOOR` characters of prose *and*
  closes a sentence or a formula, so `Show that` never stands alone;
* the cut never falls inside a math span, so the title still typesets;
* two cards that would collide keep taking more of their own statement until
  they differ.

`degenerate` is the reader-facing measure and the audit check's predicate. It
deliberately does not treat a `$` as a defect: `/problems.html` typesets its row
titles, so `Let $R$ be a commutative ring with 1.` reads correctly, and stripping
the mathematics out of 1,873 titles would destroy the statement to work around a
search dialog that does not typeset.
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent

# A title carries at least FLOOR and at most BUDGET characters of prose. Both are
# measured outside the mathematics: a formula is one glyph to a reader, and
# counting its source would cut every title at the first integral.
FLOOR = 12
BUDGET = 60
# Raw ceiling, applied only where a whole unit can be dropped. A single formula
# longer than this is still emitted whole: half a formula does not typeset.
CAP = 220

AUTHORED_TITLE = re.compile(r'^:{3,}[^\n]*?\btitle="([^"]*)"')
# Page furniture: fences, headings, tag lines, quotes, bare images, Obsidian
# block anchors, layout macros, table rows.
FURNITURE = re.compile(r"^(:{3,}|#|>|!\[[^\]]*\]\([^)]*\)\s*$|\^[0-9a-f]{4,}\s*$|\\\w+\s*$|---\s*$|\|)")
DISPLAY = re.compile(r"\$\$(.*?)\$\$|\\\[(.*?)\\\]", re.S)
# A math span is one glyph to a reader and one token to the cut. A LaTeX
# environment is math too: MathJax typesets `\begin{align*}...\end{align*}`
# with no delimiters around it, and counting its source as prose cut titles in
# the middle of an `\begin`.
MATH = re.compile(r"\$[^$]*\$|\\\(.*?\\\)|\\begin\{[a-zA-Z*]+\}.*?\\end\{[a-zA-Z*]+\}", re.S)
IMAGE = re.compile(r"!\[[^\]]*\]\([^)]*\)|!\[\[[^\]]*\]\]")
EMPHASIS = re.compile(r"\*{1,3}(?=\S)|(?<=\S)\*{1,3}|`")
# A footnote reference is a pointer to a note the title does not carry.
FOOTNOTE = re.compile(r"\[\^[^\]]+\]")
LEADIN = re.compile(r"^\s*(?:[-*+](?:\s+|$)|\(?(?:[a-zA-Z]|\d{1,2}|[ivx]{1,4})[.)](?:\s+|$))+")
# `i.e.` and `Fig.` end a word, not a sentence.
ABBREV = re.compile(r"(?:\b(?:i\.e|e\.g|cf|etc|resp|vs|Ex|no|Thm|Def|Prop|Lem|Cor|Fig|Ch|pp)\.|\b[A-Z]\.)$")
CLOSES = ".?!$"


def readable(text: str) -> int:
    """Characters a reader reads: everything outside a math span."""
    return len(re.sub(r"\s+", " ", MATH.sub("", text)).strip())


def _inline_display(body: str) -> str:
    def one(match: re.Match[str]) -> str:
        inner = re.sub(r"\s+", " ", match.group(1) or match.group(2) or "").strip()
        # The corpus writes the sentence's full stop inside the delimiters, as
        # `.\]`. Drop it -- but never the one in `\right.`, which is a brace.
        inner = re.sub(r"(?<!\\right)(?<!\\left)[.,]$", "", inner).strip()
        # The corpus writes aligned display blocks with bare `&`, which is
        # "Misplaced &" once the block is inlined. `_macros.html` wraps such a
        # block in `aligned` before typesetting it; do the same here, so the
        # title keeps the formula instead of losing it.
        if "&" in re.sub(r"\\begin\{([a-zA-Z*]+)\}.*?\\end\{\1\}", "", inner, flags=re.S):
            inner = rf"\begin{{aligned}}{inner}\end{{aligned}}"
        return f" ${inner}$ " if inner else " "

    return DISPLAY.sub(one, body)


def _sentences(line: str) -> list[str]:
    """Split a line at sentence ends, ignoring any that fall inside mathematics."""
    masked = MATH.sub(lambda m: "\x00" * len(m.group(0)), line)
    out: list[str] = []
    start = 0
    for match in re.finditer(r"[.?!]\s+", masked):
        following = line[match.end() : match.end() + 1]
        if ABBREV.search(masked[start : match.start() + 1].rstrip()):
            continue
        if following and not (following.isupper() or following in "$\\("):
            continue
        out.append(line[start : match.end()].strip())
        start = match.end()
    tail = line[start:].strip()
    if tail:
        out.append(tail)
    return [unit for unit in out if unit]


def units(body: str) -> list[str]:
    """The statement in reading order, one entry per sentence, math inlined.

    Markdown markup is dropped rather than carried: a title is displayed as
    text, so `**Main Idea**` reaches the reader as four asterisks, and an image
    reaches it as a vault path.
    """
    out: list[str] = []
    paragraph = ""
    for line in [*_inline_display(body).splitlines(), ""]:
        line = EMPHASIS.sub("", FOOTNOTE.sub("", IMAGE.sub("", line))).strip()
        # A line holding nothing but a marker or an image is not a unit of the
        # statement; appending one leaves a title ending `... ring. 1.`
        spent = not any(character.isalnum() for character in line) or not LEADIN.sub("", line).strip()
        # A paragraph is wrapped prose -- the corpus wraps at 72 columns, and a
        # `$...$` straddling two of those lines is one math span, not two. A
        # list marker opens a new paragraph, so parts (a) and (b) stay apart.
        if spent or FURNITURE.match(line) or LEADIN.match(line):
            out.extend(_sentences(re.sub(r"\s+", " ", paragraph)) if paragraph.strip() else [])
            paragraph = "" if spent or FURNITURE.match(line) else line
            continue
        paragraph = f"{paragraph} {line}"
    # The label of a part is not part of the sentence it labels. Leaving them in
    # puts `(a)` and `1.` in the middle of a title as often as at its front.
    return [LEADIN.sub("", unit).strip() for unit in out]


def _tokens(text: str) -> list[re.Match[str]]:
    """Words and whole math spans, as spans of `text`. Math is never split, and
    the cut lands between tokens so the statement's own spacing survives."""
    return list(re.finditer(rf"{MATH.pattern}|\S+", text, re.S))


def _clip(text: str) -> str:
    text = LEADIN.sub("", text).strip()
    if readable(text) <= BUDGET and len(text) <= CAP:
        return _backed_off(text)
    seen = 0
    cut = 0
    carried = False
    for token in _tokens(text):
        over = seen + readable(token.group(0)) > BUDGET or token.end() > CAP
        # A cut that leaves nothing is not a cut: `We have $...$` must keep the
        # formula even when the formula is longer than the whole ceiling.
        if cut and carried and over:
            return _backed_off(text[:cut].rstrip(" ,;:") + "…")
        seen += readable(token.group(0)) + 1
        cut = token.end()
        carried = seen >= FLOOR or bool(MATH.fullmatch(token.group(0)))
    return _backed_off(text)


def _backed_off(title: str) -> str:
    """Drop trailing tokens until the title typesets.

    A handful of source statements open a `$` on one line and close it on the
    next, so cutting at a line boundary can leave the delimiter unmatched.
    """
    while title and not _typesets(title):
        text = title.removesuffix("…").rstrip(" ,;:")
        tokens = _tokens(text)
        if len(tokens) < 2:
            return ""
        title = text[: tokens[-1].start()].rstrip(" ,;:") + "…"
    return title


def authored_title(body: str) -> str:
    """The `title="..."` the author wrote on the div, if it says anything."""
    for line in body.splitlines()[:4]:
        match = AUTHORED_TITLE.match(line)
        if match and match.group(1).strip() not in ("", "?"):
            return EMPHASIS.sub("", match.group(1)).strip()
    return ""


def title_of(body: str, sentences: int = 1) -> str:
    """The opening of the statement, cut where a reader can still read it.

    `sentences` is how many closed units the title must carry; the collision
    pass raises it for cards that would otherwise share a title.
    """
    authored = authored_title(body)
    if authored and readable(authored) >= FLOOR:
        return authored
    accumulated = ""
    remaining = sentences
    for unit in units(body):
        accumulated = f"{accumulated} {unit}".strip()
        clipped = _clip(accumulated)
        remaining -= 1
        # `Let $A \in M_3(\CC)$` closes a clause but asks nothing; the title
        # goes on to the question. A statement that never offers that much
        # prose ends at the cut instead, and one that ends first ends there.
        if clipped.endswith(tuple(CLOSES)) and readable(clipped) >= FLOOR and remaining <= 0:
            break
        if clipped.endswith("…"):
            break
    candidate = _clip(accumulated)
    if authored and candidate:
        return f"{authored}: {candidate}"
    # A card whose statement is a scan carries no words at all. `Untitled` is
    # the corpus's own admission of that, and it is the one thing that can be
    # written here without writing mathematics the card does not contain; the
    # audit reports every one of them, because the repair is authoring.
    return authored or candidate or "Untitled"


def retitle(bodies: dict[str, str], pinned: dict[str, str] | None = None) -> dict[str, str]:
    """Titles for a whole corpus, extended until no two cards share one.

    A pinned title stands: a card whose title already reads is left as its
    author wrote it, and only the cards that fail a reader are derived again.
    """
    pinned = pinned or {}
    # A pin protects a readable title from being replaced. It does not protect a
    # collision: two cards both called `Dense` are one row twice to a reader, so
    # a pinned title that is not unique goes back to its own statement.
    depth = {card_id: 0 if card_id in pinned else 1 for card_id in bodies}
    titles = {card_id: pinned[card_id] if card_id in pinned else title_of(body) for card_id, body in bodies.items()}
    reach = {card_id: len(units(body)) for card_id, body in bodies.items()}
    for _ in range(12):
        counts = collections.Counter(titles.values())
        extended = False
        for card_id, body in bodies.items():
            if counts[titles[card_id]] < 2 or depth[card_id] >= reach[card_id]:
                continue
            depth[card_id] += 1
            titles[card_id] = title_of(body, depth[card_id])
            extended = True
        if not extended:
            break
    return titles


def _typesets(title: str) -> bool:
    """Whether MathJax can render the title, rather than print its source.

    Escaped braces are dropped before counting: `\\left\\{ x \\right.` is
    balanced LaTeX with one brace character in it.

    A title's mathematics is inline, and an alignment character outside an
    alignment environment is "Misplaced &" there. The corpus writes aligned
    display blocks with bare `&`, which `_inline_display` would otherwise carry
    into a title verbatim; `_macros.html` wraps such a block in `aligned`
    before typesetting it, and a title has nowhere to put that.
    """
    braces = re.sub(r"\\.", "", title, flags=re.S)
    inline = "".join(match.group(0) for match in MATH.finditer(title))
    aligned = re.sub(r"\\begin\{([a-zA-Z*]+)\}.*?\\end\{\1\}", "", inline, flags=re.S)
    return title.count("$") % 2 == 0 and braces.count("{") == braces.count("}") and title.count(r"\begin{") == title.count(r"\end{") and "&" not in aligned


def degenerate(title: str, authored: str = "") -> str | None:
    """Why this title fails a reader, or None if it does not.

    An authored title is exempt from the floor. `Excision` and `Gram Matrix`
    are how the author named those cards, and a derivation that overruled them
    would be writing titles rather than reading them.
    """
    text = title.strip()
    if not text or text in {"?", "Untitled"}:
        return "no title"
    if not _typesets(text):
        return "does not typeset"
    if IMAGE.search(text) or re.search(r"\.(png|jpe?g|gif|svg)\b", text):
        return "an image is not a title"
    if EMPHASIS.search(MATH.sub("", text)) or FOOTNOTE.search(text):
        return "carries markdown markup"
    if text == authored.strip():
        return None
    if readable(text) < FLOOR and not MATH.search(text):
        return "names nothing"
    return None


# `source` and `occurrence` titles are composed from the exam sitting, not from a
# statement -- their bodies are provenance remarks, so deriving from them would
# replace "UGA algebra Fall 2018, problem 1" with the remark that says so.
COMPOSED_KINDS = {"source", "occurrence"}
# The title scalar, including the wrapped continuation lines `yaml.safe_dump`
# writes past its width. Replacing only the first line leaves the rest of the
# old title behind as a second mapping key.
TITLE_LINE = re.compile(r"^title:.*(?:\n[ \t]+\S.*)*$", re.M)


def _front_matter(text: str) -> tuple[str, str]:
    _, front, body = text.split("---", 2)
    return front, body


def _sitting_titles(meta: dict[str, dict], degenerate_now: dict[str, str | None]) -> dict[str, str]:
    """Occurrences named the way the corpus already names them.

    2,798 occurrence cards read `P-XYDVS at UGA algebra Spring 2020`. The 22
    that came through `route_authored_md` carry a first-line cut of the problem
    statement instead, which is the same defect in a card whose title was never
    supposed to come from a statement at all.
    """
    out: dict[str, str] = {}
    for card_id, card in meta.items():
        if card["kind"] != "occurrence" or not degenerate_now[card_id]:
            continue
        target = next(relation["target"] for relation in card["relations"] if relation["kind"] == "instance-of")
        out[card_id] = f"{target} at {meta[card['payload']['source']]['title']}"
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="card-titles")
    parser.add_argument("--write", action="store_true", help="rewrite the corpus front matter")
    parser.add_argument("--root", type=Path, default=REPO)
    args = parser.parse_args(argv)

    paths: dict[str, Path] = {}
    meta: dict[str, dict] = {}
    bodies: dict[str, str] = {}
    for path in sorted((args.root / "corpus").rglob("*.md")):
        text = path.read_text()
        if not text.startswith("---"):
            continue
        front, body = _front_matter(text)
        card = yaml.safe_load(front)
        paths[card["id"]], meta[card["id"]], bodies[card["id"]] = path, card, body

    statements = {card_id: bodies[card_id] for card_id in meta if meta[card_id]["kind"] not in COMPOSED_KINDS}
    before = {card_id: degenerate(str(card["title"]), authored_title(bodies[card_id])) for card_id, card in meta.items()}
    pinned = {card_id: str(meta[card_id]["title"]) for card_id in statements if not before[card_id]}
    titles = retitle(statements, pinned)
    titles.update(_sitting_titles(meta, before))
    changed = [card_id for card_id, card in meta.items() if card_id in titles and titles[card_id] != str(card["title"])]
    after = {card_id: degenerate(titles.get(card_id, str(card["title"])), authored_title(bodies[card_id])) for card_id, card in meta.items()}
    for label, verdicts in (("before", before), ("after", after)):
        counts = collections.Counter(reason for reason in verdicts.values() if reason)
        print(f"degenerate {label}: {sum(counts.values())} of {len(verdicts)}  {dict(counts)}")
    print(f"{len(changed)} retitled")
    if not args.write:
        for card_id, reason in after.items():
            if reason:
                print(f"    {card_id}: {reason}: {titles[card_id]!r}")
        return 0
    for card_id in changed:
        front, body = _front_matter(paths[card_id].read_text())
        # A function replacement, never a template: a title is full of
        # backslashes, and `re.sub` reads `\text` in a replacement string as an
        # escape and writes a tab.
        line = f"title: {json.dumps(titles[card_id])}"
        paths[card_id].write_text(f"---{TITLE_LINE.sub(lambda _: line, front, count=1)}---{body}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
