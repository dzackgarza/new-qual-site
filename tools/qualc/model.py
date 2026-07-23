"""Card schema.

One required envelope; `kind` selects an exact payload. This is a closed
discriminated union, not one weak record with forty optional fields.
Unknown metadata fields are rejected, so a typo fails the build.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Annotated, Literal

import panflute as pf
import yaml
from pydantic import BaseModel, ConfigDict, Field


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)


# --- dates ------------------------------------------------------------------
# Unknown is a case, never a sentinel like `year: 0` or `season: NA`.


class AcademicTerm(Strict):
    kind: Literal["academic-term"]
    year: int
    term: Literal["spring", "fall"]


class YearOnly(Strict):
    kind: Literal["year"]
    year: int


class TermOnly(Strict):
    """Season known, year not.

    Not hypothetical: 20 make-me-a-qual records (all NUS) carry a real season
    under the sentinel `year: 1970`. Without this case the season is lost, since
    `AcademicTerm` demands a year and `YearOnly` demands one too.
    """

    kind: Literal["term"]
    term: Literal["spring", "fall"]


class UnknownDate(Strict):
    kind: Literal["unknown"]


DateSpec = Annotated[
    AcademicTerm | YearOnly | TermOnly | UnknownDate,
    Field(discriminator="kind"),
]


# --- envelope ---------------------------------------------------------------

RelationKind = Literal[
    "instance-of",
    "solves",
    "hints-at",
    "uses",
    "related-to",
    "cites",
    "variant-of",
    "extracted-from",
]

# `\work` and `\todo` both land on `draft`; `\done` on `reviewed`. `verified` is
# deliberately unpopulated by migration -- it is reserved for a later checking
# pass, and claiming it on import would assert a review that never happened.
Review = Literal["draft", "reviewed", "verified"]


class Classification(Strict):
    areas: list[str]
    topics: list[str]


class Relation(Strict):
    kind: RelationKind
    target: str


class Envelope(Strict):
    card_schema: Literal["qual/card@1"] = Field(alias="schema")
    id: str
    title: str
    classification: Classification
    relations: list[Relation]
    review: Review


# --- payloads ---------------------------------------------------------------


class OccurrencePayload(Strict):
    source: str
    locator: str


class ExamSource(Strict):
    """A sitting of a qualifying exam."""

    source_kind: Literal["university-exam"]
    institution: str
    area: str
    date: DateSpec


class TextbookSource(Strict):
    """A cited book. Carries no institution -- a textbook is not sat anywhere."""

    source_kind: Literal["textbook"]
    textbook: str
    date: DateSpec


class ContributedArtifact(Strict):
    """A PDF, scan, or handwritten note contributed to the corpus.

    `provenance` is required and free text because the honest answer is often a
    sentence ("Neil's Fall 2019 solution set, origin unrecorded"). Requiring it
    stops an artifact entering the corpus with no account of where it came from.
    """

    source_kind: Literal["contributed-artifact"]
    provenance: str
    date: DateSpec


SourcePayload = Annotated[
    ExamSource | TextbookSource | ContributedArtifact,
    Field(discriminator="source_kind"),
]


class ProblemCard(Envelope):
    kind: Literal["problem"]


class OccurrenceCard(Envelope):
    kind: Literal["occurrence"]
    payload: OccurrencePayload


class SourceCard(Envelope):
    kind: Literal["source"]
    payload: SourcePayload


# Every remaining kind is envelope plus prose body. They are separate classes
# rather than one class with a `kind` field because the union is what makes an
# unknown kind a build failure instead of a silently accepted string.
class SolutionCard(Envelope):
    kind: Literal["solution"]


class HintCard(Envelope):
    kind: Literal["hint"]


class DefinitionCard(Envelope):
    kind: Literal["definition"]


class TheoremCard(Envelope):
    kind: Literal["theorem"]


class PropositionCard(Envelope):
    kind: Literal["proposition"]


class CorollaryCard(Envelope):
    kind: Literal["corollary"]


class LemmaCard(Envelope):
    kind: Literal["lemma"]


class ProofCard(Envelope):
    kind: Literal["proof"]


class ExampleCard(Envelope):
    kind: Literal["example"]


class ExerciseCard(Envelope):
    kind: Literal["exercise"]


class RemarkCard(Envelope):
    kind: Literal["remark"]


class StrategyCard(Envelope):
    kind: Literal["strategy"]


class ConceptCard(Envelope):
    kind: Literal["concept"]


class FactCard(Envelope):
    """A result stated without proof -- cited, folkloric, or assumed."""

    kind: Literal["fact"]


class ClaimCard(Envelope):
    """A local assertion discharged by a surrounding argument.

    Measured never to occur at the top level in either prose repo, so a
    standalone claim card is unusual by construction; the kind exists so that a
    deliberately promoted claim has somewhere to go.
    """

    kind: Literal["claim"]


class WarningCard(Envelope):
    """Editorial errata and caveats, often correcting the original exam's wording."""

    kind: Literal["warning"]


class SloganCard(Envelope):
    """A one-line informal gloss of what a result really says."""

    kind: Literal["slogan"]


Card = Annotated[
    ProblemCard
    | OccurrenceCard
    | SourceCard
    | SolutionCard
    | HintCard
    | DefinitionCard
    | TheoremCard
    | PropositionCard
    | CorollaryCard
    | LemmaCard
    | ProofCard
    | ExampleCard
    | ExerciseCard
    | RemarkCard
    | StrategyCard
    | ConceptCard
    | FactCard
    | ClaimCard
    | WarningCard
    | SloganCard,
    Field(discriminator="kind"),
]

# Authored fenced-div class -> card kind. Total over every class measured in the
# two prose repos; an unmapped class is a build failure, never silent prose.
# `warnings` is plural in the source and singular as a kind: the div vocabulary
# is an input format, not the domain type.
DIV_CLASS_TO_KIND = {
    "problem": "problem",
    "solution": "solution",
    "hint": "hint",
    "definition": "definition",
    "theorem": "theorem",
    "proposition": "proposition",
    "corollary": "corollary",
    "lemma": "lemma",
    "proof": "proof",
    "example": "example",
    "exercise": "exercise",
    "remark": "remark",
    "strategy": "strategy",
    "concept": "concept",
    "fact": "fact",
    "claim": "claim",
    "warnings": "warning",
    "slogan": "slogan",
}

# Presentational only, carrying no semantics. Recorded rather than ignored, so
# that "we never looked at it" and "we looked and it means nothing" stay
# distinguishable.
NON_SEMANTIC_CLASSES = {"foldopen"}

# The two sets above are total over the authored corpus: every class measured in
# the prose repos is in one of them. Anything else is a typo or an environment
# nobody has classified, and both must stop the build rather than become prose.
KNOWN_CLASSES = set(DIV_CLASS_TO_KIND) | NON_SEMANTIC_CLASSES


class ParsedCard(Strict):
    """A validated card, its body as a pandoc AST, and its semantic sections."""

    card: Card
    ast: str  # pandoc JSON; the emitter composes pages out of these, never text
    source_path: str
    sections: list[tuple[str, str]]  # (section kind, plain text, for search)


# The reader dialect, in one place because every read has to agree.
#
# This is not a set assembled here. It is the dialect the corpus was written in,
# copied from the author's own toolchain -- `~/.pandoc/bin/fmt-pipeline` reads
# `markdown+fenced_divs+raw_tex+tex_math_dollars+tex_math_single_backslash
# +wikilinks_title_after_pipe`, and the sibling scripts that produce HTML and
# LaTeX pass `tex_math_single_backslash` too. Every file in `qual-wiki` has been
# read and written through those scripts for years.
#
# `qualc` called bare `pandoc -f markdown` and so did not speak that dialect.
# Two of the extensions are the difference between reading the corpus and
# mangling it:
#
#   tex_math_single_backslash -- off in pandoc's stock `markdown`, where `\[`
#     is simply an escaped `[`. Without it `\[ x^2 \]` reads as the literal
#     characters `[ x^2 ]`, and a markdown round trip writes back
#     `` `\int`{=tex}*{`\mathbb{R}`{=tex}} `` -- the subscript reinterpreted as
#     an emphasis marker, which is how two corpus cards came to be stored corrupt.
#   wikilinks_title_after_pipe -- without it `[[Sylow Theorems]]` is `Str
#     "[[Sylow"`, not a Link. There are 360 of them in qual-wiki, and WS2
#     requires them to resolve.
#
# The remaining three are pandoc defaults, written out so this string can be
# diffed against the toolchain it came from rather than inferred.
MARKDOWN = "markdown+fenced_divs+raw_tex+tex_math_dollars+tex_math_single_backslash+wikilinks_title_after_pipe"


def to_ast(markdown: str) -> str:
    """Read a card body, and treat any reader diagnostic as a build failure.

    pandoc is invoked directly rather than through `pf.convert_text` for one
    reason: panflute raises `OSError("")` on a non-zero exit and drops the
    message, and the message is the whole point. The parsing is still entirely
    pandoc's; only the error handling is ours.

    A warning from this reader is not cosmetic: it can mean the card was
    truncated. See `tests/test_reader_warnings.py` for the one worked example,
    which is synthetic -- no card and no file in qual-wiki provokes it. The gate
    is here because a parse pandoc was unsure of should not be indexed, not
    because the corpus is known to contain such a parse.
    """
    proc = subprocess.run(
        ["pandoc", "--from", MARKDOWN, "--to", "json", "--standalone", "--fail-if-warnings"],
        input=markdown,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise ValueError(proc.stderr.strip())
    return proc.stdout


def from_ast(ast: str) -> pf.Doc:
    doc: pf.Doc = pf.convert_text(ast, input_format="json", output_format="panflute", standalone=True)
    return doc


def split_front_matter(text: str, path: Path) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: card must start with YAML front matter")
    _, fm, body = text.split("---\n", 2)
    meta = yaml.safe_load(fm)
    if not isinstance(meta, dict):
        raise ValueError(f"{path}: front matter must be a mapping")
    return meta, body


def extract_sections(doc: pf.Doc) -> list[tuple[str, str]]:
    """Collect semantic sections wherever they appear, including nested ones.

    Nesting is normal here -- a `solution` containing a `proof` is the corpus's
    dominant compound shape, and a `claim` is never anything but nested. A
    nested section is indexed in addition to its parent, not instead of it: the
    parent's text already includes the child's, because `pf.stringify` recurses.

    Descent follows the whole block tree rather than chains of divs, because a
    proof quoted inside a `>` block is still a proof.

    Raises on any class outside `KNOWN_CLASSES`: an unclassified environment is
    a build failure, never silent prose.
    """
    found: list[tuple[str, str]] = []
    unknown: list[str] = []

    def walk(element: pf.Element) -> None:
        if isinstance(element, pf.Div):
            unknown.extend(c for c in element.classes if c not in KNOWN_CLASSES)
            cls = next((c for c in element.classes if c in DIV_CLASS_TO_KIND), None)
            if cls:
                # Record the domain kind, not the authored class: `warnings` in
                # the source is a `warning` everywhere downstream.
                found.append((DIV_CLASS_TO_KIND[cls], pf.stringify(element).strip()))
        # Leaf inlines carry no `content`; everything with children exposes it.
        if hasattr(element, "content"):
            for child in element.content:
                if isinstance(child, pf.Element):
                    walk(child)

    for block in doc.content:
        walk(block)
    if unknown:
        raise ValueError(f"unmapped fenced-div class(es): {', '.join(sorted(set(unknown)))}")
    return found


def parse_card(path: Path) -> ParsedCard:
    meta, body = split_front_matter(path.read_text(), path)
    from pydantic import TypeAdapter

    card: Card = TypeAdapter(Card).validate_python(meta)
    ast = to_ast(body)
    return ParsedCard(
        card=card,
        ast=ast,
        source_path=str(path),
        sections=extract_sections(from_ast(ast)),
    )


def discover(corpus: Path) -> list[Path]:
    """The corpus layout is semantically inert: every .md under it is a card,
    and its path contributes nothing but an edit link."""
    return sorted(p for p in corpus.rglob("*.md"))
