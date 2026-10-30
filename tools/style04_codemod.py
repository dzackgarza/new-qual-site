#!/usr/bin/env python3
r"""One-time STYLE-04 codemod: `\definedas` to `\coloneqq`, and each raw bar to the macro for its meaning.

A bar has several meanings, so the rewrite reads a classification that records the meaning of
every bar occurrence, keyed by card id, math span and occurrence. A reader produces that
classification by reading each occurrence in context; this tool only applies it.

    style04_codemod.py list [--shard K/N] [PATH ...]   print each bar-bearing span with numbered bars
    style04_codemod.py apply TSV ...                     rewrite the corpus from classification files
    style04_codemod.py verify                            compare each changed card's Pandoc AST with HEAD

A classification line is `CARD-ID S<span> h<hash> LABEL ...`, one label per numbered bar:

    abs( abs)  norm( norm)  card( card)  det( det)  order( order)   paired delimiters
    st  div  given  restrict  eval  parallel                          single bars
    +                                                                 joins this bar to the previous one (`||` as a norm)

Delete this tool once the rewrite is committed; the STYLE-04 card check in
`tools/qualc/authoring.py` keeps the raw forms out.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

from qualc.authoring import BAR_GLYPHS, BAR_SIZES, DEFINEDAS, TEX_TOKEN, bar_tokens, math_spans
from qualc.model import FRONT_MATTER

ROOT = Path(__file__).resolve().parent.parent
PAIRED = {
    "abs": "\\abs",
    "norm": "\\norm",
    "card": "\\cardinality",
    "det": "\\determinant",
    "order": "\\elementorder",
    "index": "\\subgroupindex",
    "measure": "\\setmeasure",
    "totvar": "\\totalvariation",
    "multi": "\\multiindexsize",
    "length": "\\lengthof",
    "linsys": "\\linearsystem",
    "realiz": "\\realization",
    "new:degree": "\\gradeddegree",
    "new:underlying": "\\underlyingspace",
    "new:matrixmodulus": "\\operatorabs",
    "new:matrixabs": "\\operatorabs",
    "new:opabs": "\\operatorabs",
    "new:support": "\\divisorsupport",
    "new:mesh": "\\partitionmesh",
    "new:matrix": "\\entrymatrix",
    "new:arclength": "\\abs",
}
SINGLE = {
    "st": "\\st",
    "div": "\\divides",
    "given": "\\given",
    "restrict": "\\restrict",
    "eval": "\\evalfrom",
    "parallel": "\\parallel",
    "pres": "\\presentationbar",
    "exactdiv": "\\exactlydivides",
    "new:thetaparam": "\\thetaseparator",
    "new:ket": "\\diracbar",
    "new:innerbar": "\\diracbar",
    "new:braket": "\\diracbar",
    "new:pairing": "\\blockseparator",
    "new:pairsep": "\\blockseparator",
    "new:augment": "\\arrayrule",
    "new:columnrule": "\\arrayrule",
    "new:column": "\\arrayrule",
    "new:colbar": "\\arrayrule",
    "new:longdivision": "\\arrayrule",
    "new:diagequals": "\\verticalequals",
}
WRAPPED = {"eval": "\\evaluated", "restrict": "\\restricted"}
INSERTED = {*PAIRED.values(), *SINGLE.values(), *WRAPPED.values(), "\\coloneqq", "{", "}"}


@dataclass(frozen=True)
class Span:
    index: int
    field: str
    text: str

    @property
    def digest(self) -> str:
        return "h" + hashlib.sha1(self.text.encode()).hexdigest()[:8]


def scalars(node: yaml.Node, path: str = ""):
    if isinstance(node, yaml.ScalarNode):
        yield path, node
    elif isinstance(node, yaml.SequenceNode):
        for position, item in enumerate(node.value):
            yield from scalars(item, f"{path}[{position}]")
    elif isinstance(node, yaml.MappingNode):
        for key, value in node.value:
            yield from scalars(value, f"{path}.{key.value}" if path else key.value)


def card_parts(text: str) -> tuple[str, str, int]:
    match = FRONT_MATTER.match(text)
    if match is None:
        return "", text, 0
    return match["front"], match["body"], match.start("body")


def spans(text: str) -> tuple[str, list[tuple[Span, yaml.ScalarNode | None, int, int]]]:
    """Card id and every math span: front-matter scalars first, then the body, in document order."""
    front, body, body_start = card_parts(text)
    found: list[tuple[Span, yaml.ScalarNode | None, int, int]] = []
    node = yaml.compose(front)
    card_id = ""
    for field, scalar in scalars(node) if node is not None else ():
        if field == "id":
            card_id = scalar.value
        for start, end in math_spans(scalar.value):
            found.append((Span(len(found), field, scalar.value[start:end]), scalar, start, end))
    for start, end in math_spans(body):
        found.append((Span(len(found), "body", body[start:end]), None, body_start + start, body_start + end))
    return card_id, found


def listing(path: Path) -> str:
    text = path.read_text()
    card_id, found = spans(text)
    lines: list[str] = []
    for span, scalar, start, end in found:
        bars = bar_tokens(span.text)
        if not bars:
            continue
        marked = span.text
        for number, bar in reversed(list(enumerate(bars, 1))):
            marked = f"{marked[: bar.start]}⟨{number}⟩{marked[bar.start :]}"
        source = scalar.value if scalar is not None else text
        before = source[max(0, start - 120) : start].replace("\n", "⏎")
        after = source[end : end + 80].replace("\n", "⏎")
        marked = marked.replace("\n", "⏎")
        lines.append(f"{span.index:>3} {span.digest} [{span.field}] …{before}⟪{marked}⟫{after}…")
    if not lines:
        return ""
    return f"## {card_id or path.relative_to(ROOT)} {path.relative_to(ROOT)}\n" + "\n".join(f"S{line.lstrip()}" for line in lines) + "\n"


def bar_paths() -> list[Path]:
    paths = []
    for path in sorted((ROOT / "corpus").rglob("*.md")) + sorted((ROOT / "wiki").rglob("*.md")):
        text = path.read_text()
        if "|" in text or "vert" in text or "Vert" in text:
            if listing(path):
                paths.append(path)
    return paths


def frames(math: str) -> tuple[dict[int, tuple[int, ...]], dict[int, int], dict[int, tuple[int, int]]]:
    """Group stack before each token, the `\\left` partner of each `\\right`, and token spans."""
    stack: list[tuple[int, str]] = []
    before: dict[int, tuple[int, ...]] = {}
    partner: dict[int, int] = {}
    tokens: dict[int, tuple[int, int]] = {}
    for match in TEX_TOKEN.finditer(math):
        start, token = match.start(), match.group()
        before[start] = tuple(frame for frame, _ in stack)
        tokens[start] = (start, match.end())
        if token in ("{", "\\left", "\\begin"):
            stack.append((start, token))
        elif token in ("}", "\\right", "\\end"):
            if not stack:
                raise ValueError(f"unbalanced {token}")
            opened, kind = stack.pop()
            expected = {"}": "{", "\\right": "\\left", "\\end": "\\begin"}[token]
            if kind != expected:
                raise ValueError(f"{token} closes {kind}")
            if token == "\\right":
                partner[start] = opened
    return before, partner, tokens


def control(name: str, following: str) -> str:
    return name + (" " if following[:1].isalpha() else "")


def rewrite(math: str, labels: list[str]) -> str:
    bars = bar_tokens(math)
    if len(bars) != len(labels):
        raise ValueError(f"{len(labels)} labels for {len(bars)} bars")
    before, partner, _ = frames(math)
    edits: list[tuple[int, int, str]] = []
    openers: list[tuple[str, int, int]] = []
    previous_end = -1
    for position, (bar, label) in enumerate(zip(bars, labels, strict=True)):
        prefix = next((size for size in BAR_SIZES if bar.text.startswith(size) and bar.text[len(size) :].lstrip() in BAR_GLYPHS), "")
        following = math[bar.end :]
        if label == "+":
            if position == 0 or math[previous_end : bar.start].strip():
                raise ValueError(f"bar {position + 1} joins a bar it does not touch")
            edits.append((bar.start, bar.end, ""))
        elif label.endswith("(") and label[:-1] in PAIRED:
            if prefix.startswith("\\right") or prefix.endswith("r"):
                raise ValueError(f"bar {position + 1} opens with {prefix}")
            lead = math[: bar.start].rstrip()
            wrap = lead.endswith(("^", "_"))
            openers.append((label[:-1], position, bar.start))
            edits.append((bar.start, bar.end, ("{" if wrap else "") + PAIRED[label[:-1]] + "{"))
        elif label.endswith(")") and label[:-1] in PAIRED:
            if not openers:
                raise ValueError(f"bar {position + 1} closes nothing")
            kind, opened, opened_at = openers.pop()
            if kind != label[:-1]:
                raise ValueError(f"bar {position + 1} closes {label} but bar {opened + 1} opened {kind}")
            if prefix == "\\right":
                if partner.get(bar.start) != opened_at:
                    raise ValueError(f"bar {position + 1} is not the \\right of bar {opened + 1}")
            elif bars[opened].text.startswith("\\left"):
                raise ValueError(f"bar {opened + 1} opens with \\left but bar {position + 1} has no \\right")
            elif before[opened_at] != before[bar.start]:
                raise ValueError(f"bars {opened + 1} and {position + 1} sit in different groups")
            wrap = math[:opened_at].rstrip().endswith(("^", "_"))
            edits.append((bar.start, bar.end, "}" + ("}" if wrap else "")))
        elif label in SINGLE:
            if prefix == "\\right" and label in WRAPPED:
                left = partner[bar.start]
                dot = re.match(r"\\left\s*\.", math[left:])
                if dot is None:
                    raise ValueError(f"bar {position + 1} closes a \\left that is not \\left.")
                edits.append((left, left + dot.end(), WRAPPED[label] + "{"))
                edits.append((bar.start, bar.end, "}"))
            elif prefix in ("\\left", "\\right"):
                raise ValueError(f"bar {position + 1} labelled {label} carries {prefix}")
            else:
                edits.append((bar.start, bar.end, control(SINGLE[label], following)))
        else:
            raise ValueError(f"bar {position + 1} has unknown label {label!r}")
        previous_end = bar.end
    if openers:
        raise ValueError(f"bar {openers[-1][1] + 1} is never closed")
    for start, end, replacement in sorted(edits, reverse=True):
        math = math[:start] + replacement + math[end:]
    return math


def emit_scalar(value: str, style: str | None) -> str:
    if style == "'":
        return "'" + value.replace("'", "''") + "'"
    if style is None and "\n" not in value:
        try:
            if yaml.safe_load(f"k: {value}") == {"k": value}:
                return value
        except yaml.YAMLError:
            pass
    if style in ("|", ">"):
        raise ValueError("block scalar")
    return json.dumps(value, ensure_ascii=False)


def read_classification(paths: list[Path]) -> dict[str, dict[int, tuple[str, list[str]]]]:
    table: dict[str, dict[int, tuple[str, list[str]]]] = {}
    for path in paths:
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            card_id, span, digest, *labels = line.split()
            index = int(span.removeprefix("S"))
            entry = table.setdefault(card_id, {})
            if index in entry:
                raise ValueError(f"{path}:{number}: {card_id} S{index} classified twice")
            entry[index] = (digest, labels)
    return table


def apply(paths: list[Path]) -> int:
    table = read_classification(paths)
    problems: list[str] = []
    seen: set[str] = set()
    for path in sorted((ROOT / "corpus").rglob("*.md")) + sorted((ROOT / "wiki").rglob("*.md")):
        text = path.read_text()
        has_bars = "|" in text or "vert" in text or "Vert" in text
        if not has_bars and not DEFINEDAS.search(text):
            continue
        try:
            card_id, found = spans(text)
        except (ValueError, yaml.YAMLError) as exc:
            problems.append(f"{path.relative_to(ROOT)}: {exc}")
            continue
        key = card_id or str(path.relative_to(ROOT))
        seen.add(key)
        entries = table.get(key, {})
        edits: list[tuple[int, int, str]] = []
        scalar_values: dict[int, tuple[yaml.ScalarNode, str]] = {}
        front_start = text.index("\n") + 1
        for span, scalar, start, end in found:
            if not bar_tokens(span.text):
                continue
            if span.index not in entries:
                problems.append(f"{key} S{span.index}: unclassified")
                continue
            digest, labels = entries[span.index]
            if digest != span.digest:
                problems.append(f"{key} S{span.index}: span changed since classification")
                continue
            try:
                new = rewrite(span.text, labels)
            except ValueError as exc:
                problems.append(f"{key} S{span.index}: {exc}")
                continue
            if scalar is None:
                edits.append((start, end, new))
            else:
                current = scalar_values.get(id(scalar), (scalar, scalar.value))[1]
                scalar_values[id(scalar)] = (scalar, current.replace(span.text, new, 1))
        for scalar, value in scalar_values.values():
            edits.append((front_start + scalar.start_mark.index, front_start + scalar.end_mark.index, emit_scalar(value, scalar.style)))
        for start, end, replacement in sorted(edits, reverse=True):
            text = text[:start] + replacement + text[end:]
        text = DEFINEDAS.sub(lambda _: "\\coloneqq", text)
        if text != path.read_text():
            path.write_text(text)
    for card_id in sorted(set(table) - seen):
        problems.append(f"{card_id}: classified but not found")
    print("\n".join(problems), file=sys.stderr)
    return 1 if problems else 0


def pandoc(text: str) -> dict:
    return json.loads(subprocess.run(["pandoc", "--from", "markdown", "--to", "json"], input=text, check=True, capture_output=True, text=True).stdout)


def math_strings(node, found: list[str]) -> None:
    if isinstance(node, dict):
        if node.get("t") == "Math":
            found.append(node["c"][1])
            return
        for value in node.values():
            math_strings(value, found)
    elif isinstance(node, list):
        for value in node:
            math_strings(value, found)


def without_math(node):
    if isinstance(node, dict):
        if node.get("t") == "Math":
            return {"t": "Math", "c": [node["c"][0], ""]}
        return {key: without_math(value) for key, value in node.items()}
    if isinstance(node, list):
        return [without_math(value) for value in node]
    return node


def substitution_only(old: str, new: str) -> str | None:
    """None when the only token differences are bar glyphs replaced by the inserted macros."""
    removable = BAR_GLYPHS | BAR_SIZES | {"\\left", ".", "\\definedas"}
    old_tokens = [token for token in TEX_TOKEN.findall(old) if not token.isspace()]
    new_tokens = [token for token in TEX_TOKEN.findall(new) if not token.isspace()]
    matcher = difflib.SequenceMatcher(a=old_tokens, b=new_tokens, autojunk=False)
    for tag, a0, a1, b0, b1 in matcher.get_opcodes():
        if tag == "equal":
            continue
        if not set(old_tokens[a0:a1]) <= removable or not set(new_tokens[b0:b1]) <= INSERTED:
            return f"{old_tokens[a0:a1]} -> {new_tokens[b0:b1]}"
    if any(bar_tokens(new)) or DEFINEDAS.search(new):
        return "raw form remains"
    return None


def verify() -> int:
    names = subprocess.run(["git", "diff", "--name-only", "HEAD", "--", "corpus", "wiki"], cwd=ROOT, check=True, capture_output=True, text=True).stdout.split()
    problems: list[str] = []
    for name in names:
        new_text = (ROOT / name).read_text()
        old_text = subprocess.run(["git", "show", f"HEAD:{name}"], cwd=ROOT, check=True, capture_output=True, text=True).stdout
        old_front, old_body, _ = card_parts(old_text)
        new_front, new_body, _ = card_parts(new_text)
        old_ast, new_ast = pandoc(old_body), pandoc(new_body)
        if without_math(old_ast) != without_math(new_ast):
            problems.append(f"{name}: body changed outside mathematics")
        old_math: list[str] = []
        new_math: list[str] = []
        math_strings(old_ast, old_math)
        math_strings(new_ast, new_math)
        scanned = [old_body[start:end] for start, end in math_spans(old_body)]
        if [re.sub(r"\s", "", item) for item in old_math] != [re.sub(r"\s", "", item) for item in scanned]:
            problems.append(f"{name}: math spans disagree with Pandoc")
        old_math += flatten(yaml.safe_load(old_front))
        new_math += flatten(yaml.safe_load(new_front))
        if len(old_math) != len(new_math):
            problems.append(f"{name}: math span count changed")
            continue
        for old, new in zip(old_math, new_math, strict=True):
            if old != new and (reason := substitution_only(old, new)):
                problems.append(f"{name}: {reason}")
    print("\n".join(problems), file=sys.stderr)
    print(f"{len(names)} changed file(s) verified, {len(problems)} problem(s)")
    return 1 if problems else 0


def flatten(value) -> list[str]:
    if isinstance(value, str):
        return [value[start:end] for start, end in math_spans(value)]
    if isinstance(value, dict):
        return [item for key in sorted(value) for item in flatten(value[key])]
    if isinstance(value, list):
        return [item for entry in value for item in flatten(entry)]
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    listed = commands.add_parser("list")
    listed.add_argument("--shard")
    listed.add_argument("paths", nargs="*", type=Path)
    applied = commands.add_parser("apply")
    applied.add_argument("tables", nargs="+", type=Path)
    commands.add_parser("verify")
    commands.add_parser("paths")
    args = parser.parse_args()
    if args.command == "paths":
        print("\n".join(str(path.relative_to(ROOT)) for path in bar_paths()))
        return 0
    if args.command == "list":
        paths = [path.resolve() for path in args.paths]
        for path in paths:
            print(listing(path), end="")
        return 0
    if args.command == "apply":
        return apply(args.tables)
    return verify()


if __name__ == "__main__":
    raise SystemExit(main())
