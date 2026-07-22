"""Card schema.

One required envelope; `kind` selects an exact payload. This is a closed
discriminated union, not one weak record with forty optional fields.
Unknown metadata fields are rejected, so a typo fails the build.
"""

from __future__ import annotations

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


class UnknownDate(Strict):
    kind: Literal["unknown"]


DateSpec = Annotated[AcademicTerm | YearOnly | UnknownDate, Field(discriminator="kind")]


# --- envelope ---------------------------------------------------------------

RelationKind = Literal["instance-of", "solves", "hints-at", "uses", "related-to"]
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


class SourcePayload(Strict):
    source_kind: Literal["university-exam"]
    institution: str
    area: str
    date: DateSpec


class ProblemCard(Envelope):
    kind: Literal["problem"]


class OccurrenceCard(Envelope):
    kind: Literal["occurrence"]
    payload: OccurrencePayload


class SourceCard(Envelope):
    kind: Literal["source"]
    payload: SourcePayload


class SolutionCard(Envelope):
    kind: Literal["solution"]


class HintCard(Envelope):
    kind: Literal["hint"]


class DefinitionCard(Envelope):
    kind: Literal["definition"]


Card = Annotated[
    ProblemCard | OccurrenceCard | SourceCard | SolutionCard | HintCard | DefinitionCard,
    Field(discriminator="kind"),
]

# Fenced-div classes the compiler treats as semantic sections. Anything else in
# a card body is ordinary prose.
SECTION_KINDS = {"problem", "solution", "hint", "strategy", "definition", "remark"}


class ParsedCard(Strict):
    """A validated card, its body as a pandoc AST, and its semantic sections."""

    card: Card
    ast: str  # pandoc JSON; the emitter composes pages out of these, never text
    source_path: str
    sections: list[tuple[str, str]]  # (section kind, plain text, for search)


def to_ast(markdown: str) -> str:
    ast: str = pf.convert_text(markdown, output_format="json", standalone=True)
    return ast


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
    found: list[tuple[str, str]] = []
    for block in doc.content:
        if isinstance(block, pf.Div):
            kind = next((c for c in block.classes if c in SECTION_KINDS), None)
            if kind:
                found.append((kind, pf.stringify(block).strip()))
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
