"""Card schema.

Every card has a minimal schema (`CardBase`). Collection and problem cards
extend it, as do the other kinds. `kind` selects the source spec on
collection cards. This is a closed discriminated union, not one weak
record with forty optional fields. Unknown metadata fields are rejected, so
a typo fails the build.
"""

from __future__ import annotations

import io
import re
from collections.abc import Callable
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from datetime import date
from pathlib import Path, PurePosixPath
from typing import Annotated, Literal, cast, get_args

import panflute as pf
import yaml
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    TypeAdapter,
    field_validator,
    model_validator,
)

from .diagnostics import Diagnostic, DiagnosticCode
from .pandoc_batch import PandocBatchError, PandocFailure, PandocServer, read_markdown_parallel


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)


# --- dates ------------------------------------------------------------------
# Unknown is a case, never a sentinel like `year: 0` or `season: NA`.

Term = Literal["spring", "summer", "fall"]

# Written in the order the terms fall within one calendar year, and read back
# out for anything that has to sort sittings. A second list of the same three
# names is a second thing to keep right.
TERMS_IN_YEAR_ORDER: tuple[Term, ...] = get_args(Term)


class AcademicTerm(Strict):
    kind: Literal["academic-term"]
    year: int
    term: Term


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
    term: Term


class UnknownDate(Strict):
    kind: Literal["unknown"]


DateSpec = Annotated[
    AcademicTerm | YearOnly | TermOnly | UnknownDate,
    Field(discriminator="kind"),
]


# --- minimal card schema ----------------------------------------------------

RelationKind = Literal[
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

# Whether a collection's listed problems are the whole source, or a prefix
# still being extracted. Omitted YAML is `complete`, so existing filled exams
# do not need a field. `incomplete` is the remaining-work signal on a
# collection whose source is only partly on the card.
Completion = Literal["complete", "incomplete"]


class Classification(Strict):
    areas: list[str]
    # Free author strings ("Linear Maps", "Sylow Theory"), not a registry of slugs.
    topics: list[str]


class Relation(Strict):
    kind: RelationKind
    target: str


class CardBase(Strict):
    card_schema: Literal["qual/card@1"] = Field(alias="schema")
    id: str
    title: str
    # Questions that front this card for review. A list because one statement
    # can be asked for in several ways, and nothing picks between them. Empty
    # means the card has no review prompt; no prompt is derived from the title.
    prompts: list[str] = []
    classification: Classification
    relations: list[Relation]
    review: Review


# --- source specs -----------------------------------------------------------


# Collection-list ids are `P-` or `E-` followed by uppercase alphanumerics, with
# optional internal hyphens (e.g. `P-MMCHV`, `P-MMAQ-AWWA4FOL2L`, `E-BV7DD`).
# Wiki exercise survivors of an exam item keep the `E-` id. A workshop section
# that is another source lists that collection (`SRC-…`) instead of copying its
# problem list. A list entry that matches neither is a typo and must fail the
# build.
PROBLEM_ID_RE = re.compile(r"^[PE]-[A-Z0-9.]+(?:-[A-Z0-9.]+)*$")
COLLECTION_ID_RE = re.compile(r"^SRC-[A-Z0-9]+(?:-[A-Z0-9]+)*$")


class ProblemEntry(Strict):
    """One problem's appearance in one collection.

    `comment` says where the problem sits in *this* source -- "Problem 6",
    "§52.2". It belongs to the pairing and not to the problem: `P-4X7XU` sits on
    two exams and is numbered differently on each, which a field on the card
    could not express without deleting one appearance. It says nothing the
    collection already says; a comment repeating the collection's own name and
    date is noise, and is not written at all.

    A bare id in YAML is this entry with no comment. That is the common case --
    most appearances have nothing to add -- so it stays the plain spelling and
    is widened here rather than at every author's keyboard:

        problems:
        - P-MMCHV                      # no comment
        - id: P-4X7XU                  # a comment
          comment: Problem 6
    """

    id: str
    comment: str | None = None

    @model_validator(mode="before")
    @classmethod
    def _widen_bare_id(cls, value: object) -> object:
        return {"id": value} if isinstance(value, str) else value


def _check_problem_ids(v: list[ProblemEntry]) -> list[ProblemEntry]:
    for entry in v:
        if not PROBLEM_ID_RE.match(entry.id):
            raise ValueError(f"not a problem id: {entry.id!r}")
    return v


def _check_section_entry_ids(v: list[ProblemEntry]) -> list[ProblemEntry]:
    for entry in v:
        if not PROBLEM_ID_RE.match(entry.id) and not COLLECTION_ID_RE.match(entry.id):
            raise ValueError(f"not a problem or collection id: {entry.id!r}")
    return v


class ExamSource(Strict):
    """One instance of a qualifying exam, identified by institution + area + date.

    `problems` is the exam's table of contents: the problem IDs in order of
    appearance. Position is the list index, so it is queryable without scraping
    prose. Empty until the exam is curated.
    """

    source_kind: Literal["university-exam"]
    institution: str
    area: str
    date: DateSpec
    problems: list[ProblemEntry] = []

    @field_validator("problems")
    @classmethod
    def _problems_are_problem_ids(cls, v: list[ProblemEntry]) -> list[ProblemEntry]:
        return _check_problem_ids(v)


class CollectionSection(Strict):
    """A named grouping of a collection's contents (chapter, workshop day, …).

    Entries are problem ids, or another collection when that section *is* that
    source (an exam paper inside a workshop packet). The nested collection
    owns the problem list and the sheet's provenance href.
    """

    name: str
    problems: list[ProblemEntry] = []

    @field_validator("problems")
    @classmethod
    def _problems_are_list_ids(cls, v: list[ProblemEntry]) -> list[ProblemEntry]:
        return _check_section_entry_ids(v)


class TextbookSource(Strict):
    """A cited book. Carries no institution -- a textbook is not sat anywhere.

    `sections` groups the book's problems by chapter / section; within a section
    the problem IDs are ordered and position is the index.
    """

    source_kind: Literal["textbook"]
    textbook: str
    date: DateSpec
    sections: list[CollectionSection] = []


class HomeworkSource(Strict):
    """A homework sheet or problem set."""

    source_kind: Literal["homework"]
    area: str
    date: DateSpec
    problems: list[ProblemEntry] = []

    @field_validator("problems")
    @classmethod
    def _problems_are_problem_ids(cls, v: list[ProblemEntry]) -> list[ProblemEntry]:
        return _check_problem_ids(v)


class CompilationSource(Strict):
    """A compilation PDF, workshop packet, or other multi-part document."""

    source_kind: Literal["compilation"]
    area: str
    date: DateSpec
    problems: list[ProblemEntry] = []
    sections: list[CollectionSection] = []

    @field_validator("problems")
    @classmethod
    def _problems_are_problem_ids(cls, v: list[ProblemEntry]) -> list[ProblemEntry]:
        return _check_problem_ids(v)

    @model_validator(mode="after")
    def _problems_or_sections(self) -> CompilationSource:
        if self.problems and self.sections:
            raise ValueError("a compilation lists problems or sections, not both")
        return self

    def listed_problem_ids(self) -> list[str]:
        if self.sections:
            return [e.id for section in self.sections for e in section.problems if PROBLEM_ID_RE.match(e.id)]
        return [e.id for e in self.problems]


SourceSpec = Annotated[
    ExamSource | TextbookSource | HomeworkSource | CompilationSource,
    Field(discriminator="source_kind"),
]


# Who did what to a problem, and when. Three events, because three separate
# things get checked: the solution was written, the statement was checked
# against the original source, and the solution was reviewed for correctness.
AuditEventKind = Literal["solution-written", "source-checked", "solution-reviewed"]


class AuditEvent(Strict):
    """One dated audit event on a problem or exercise card.

    Repeated events of one kind are the normal case: a solution reviewed twice
    records two `solution-reviewed` entries. Entries are read in the order
    authored, and nothing derives a status from them. Whether a card is solved
    still follows from its solution section, never from this list.

    `date` is a `datetime.date`, so a mistyped day fails the build instead of
    being stored as a string nobody can sort. `by` is whatever handle or name
    the author writes; there is no registry of people.

    The field is `date` and not `on` because PyYAML reads YAML 1.1, where a
    bare `on` is the boolean `true`. An `on:` key never reaches pydantic as a
    key at all.
    """

    event: AuditEventKind
    by: str
    date: date
    note: str | None = None


# The two kinds that pose work to a reader are the two that carry `audit`.
class ProblemCard(CardBase):
    kind: Literal["problem"]
    audit: list[AuditEvent] = []


class ExerciseCard(CardBase):
    kind: Literal["exercise"]
    audit: list[AuditEvent] = []


class CollectionCard(CardBase):
    """An exam, homework sheet, compilation, or textbook collection.

    The card is the collection: it houses the ordered problem list. Appearances
    on a problem page are generated from that list.

    `completion` is `incomplete` when the list is a prefix of the source and
    further extraction is pending; it is not a substitute for listing the
    problems that have already been written.

    `provenance` is a list of links to source material: `https://` URLs or
    repo-relative paths such as `assets/attachments/...`.
    """

    kind: Literal["collection"]
    source: SourceSpec
    completion: Completion = "complete"
    provenance: list[str] = []

    @field_validator("provenance")
    @classmethod
    def _provenance_hrefs(cls, v: list[str]) -> list[str]:
        hrefs = []
        for href in v:
            href = href.strip()
            if not href:
                raise ValueError("provenance href is empty")
            hrefs.append(href)
        return hrefs


# Every remaining kind is CardBase plus a prose body. They are separate classes
# rather than one class with a `kind` field because the union is what makes an
# unknown kind a build failure instead of a silently accepted string.
class HintCard(CardBase):
    kind: Literal["hint"]


class DefinitionCard(CardBase):
    kind: Literal["definition"]


class TheoremCard(CardBase):
    kind: Literal["theorem"]


class PropositionCard(CardBase):
    kind: Literal["proposition"]


class CorollaryCard(CardBase):
    kind: Literal["corollary"]


class LemmaCard(CardBase):
    kind: Literal["lemma"]


class ProofCard(CardBase):
    kind: Literal["proof"]


class ExampleCard(CardBase):
    kind: Literal["example"]


class RemarkCard(CardBase):
    kind: Literal["remark"]


class StrategyCard(CardBase):
    kind: Literal["strategy"]


class ConceptCard(CardBase):
    kind: Literal["concept"]


class FactCard(CardBase):
    """A result stated without proof -- cited, folkloric, or assumed."""

    kind: Literal["fact"]


class ClaimCard(CardBase):
    """A local assertion discharged by a surrounding argument.

    Measured never to occur at the top level in either prose repo, so a
    standalone claim card is unusual by construction; the kind exists so that a
    deliberately promoted claim has somewhere to go.
    """

    kind: Literal["claim"]


class WarningCard(CardBase):
    """Editorial errata and caveats, often correcting the original exam's wording."""

    kind: Literal["warning"]


class SloganCard(CardBase):
    """A one-line informal gloss of what a result really says."""

    kind: Literal["slogan"]


Card = Annotated[
    ProblemCard
    | CollectionCard
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

# Authored fenced-div class -> semantic section kind. Total over every class
# measured in the two prose repos; an unmapped class is a build failure, never
# silent prose. A section kind need not be a card kind: `solution` deliberately
# exists only inside a problem/exercise card. `warnings` is plural in the source
# and singular downstream: the div vocabulary is an input format, not the
# domain type.
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


# `tex_math_dollars` is strict about its delimiters in two ways the corpus broke:
# `$ x $` needs no space inside them, and `$$ ... $$` allows no blank line between
# them. Either way the dollars survive as text and the macros between them are
# dropped on the way to HTML. The reader says nothing about it, but a delimiter it
# declined becomes a `Str` of nothing but dollar signs, and the corpus escapes no
# dollar sign anywhere, so that token is the defect rather than a proxy for it.
#
# A dollar attached to content -- `$L^1$` as a wikilink's title, which pandoc reads
# as plain text -- is left alone: MathJax typesets it on the page the same as it
# does a card title.
TEXT_DOLLAR = re.compile(r'"t":"Str","c":"\$+"')


def unread_math(ast_json: str, path: Path) -> Diagnostic | None:
    """Report a dollar sign the reader left as text instead of reading as math."""
    if not TEXT_DOLLAR.search(ast_json):
        return None
    return Diagnostic(
        DiagnosticCode.UNREAD_MATH,
        str(path),
        "a $ reached the page as text: write $x$ not $ x $, and leave no blank line inside $$ ... $$",
    )


def to_ast(markdown: str) -> str:
    """Read a card body, and treat any reader diagnostic as a build failure.

    pandoc is invoked directly rather than through `pf.convert_text` for one
    reason: panflute raises `OSError("")` on a non-zero exit and drops the
    message, and the message is the whole point. The parsing is still entirely
    pandoc's; only the error handling is ours.

    The gate's justification is narrow and worth stating exactly, because it was
    twice overstated: a parse the parser warned about should not be indexed. It
    is not evidence-backed protection against a known corpus hazard. The only
    worked example is input I constructed, no card or qual-wiki file provokes it,
    and the measured count in real data is zero. See
    `tests/test_reader_warnings.py`.

    A cost I claimed for it does not exist. I said qual-wiki emits "benign"
    warnings that would trip this gate during WS2. Measured: its 263 authored
    files -- WS2's actual input -- emit **zero** pandoc warnings in this dialect.
    The one warning I had glimpsed comes from a `TexDocs/` aggregate, which WS2
    excludes, and it is not benign either: that file carries two
    `\\newcommand{\\sech}`, one disabled with a leading `%`, and pandoc keeps the
    disabled one, ignores the author's active one, and emits the `%` stripped so
    the generated LaTeX holds a duplicate definition. I called it benign without
    reading it.
    """
    with PandocServer() as pandoc:
        result = pandoc.read_markdown([markdown], MARKDOWN)[0]
    match result:
        case PandocFailure(error=error):
            raise PandocBatchError(error)
    warnings = [message.message for message in result.messages if message.verbosity == "WARNING"]
    if warnings:
        raise ValueError("\n".join(warnings))
    return result.output


def from_ast(ast: str) -> pf.Doc:
    loader = cast(
        Callable[[io.StringIO], object],
        vars(pf)["load"],
    )
    document: object = loader(io.StringIO(ast))
    if not isinstance(document, pf.Doc):
        raise TypeError("pandoc JSON did not decode to a document")
    return document


def to_json(document: pf.Doc) -> str:
    stream = io.StringIO()
    dumper = cast(Callable[[pf.Doc, io.StringIO], None], vars(pf)["dump"])
    dumper(document, stream)
    return stream.getvalue()


# A caption ending in an image suffix is the figure's own file path. Pandoc's
# implicit-figure syntax makes the caption out of the alt text, and the authored
# vault wrote the path there, so 93 figures across 22 pages were captioned
# `_attachments/Pasted image 20211031235625.png`.
FILE_CAPTION = re.compile(r"\.(png|jpe?g|gif|svg|webp|pdf)$", re.IGNORECASE)


# panflute's stubs expose Link but not Image; both carry `.url`. Fetch Image
# dynamically and narrow by isinstance against the tuple at runtime, then cast
# for the attribute access mypy cannot narrow through the tuple.
_Image = cast(type[pf.Element], vars(pf)["Image"])
LINKING_ELEMENTS = (pf.Link, _Image)


def _figure_targets(element: pf.Figure) -> list[str]:
    """Every url the figure points at: its image, and any link wrapping it."""
    urls: list[str] = []

    def collect(node: pf.Element, doc: pf.Doc) -> pf.Element:
        del doc
        if isinstance(node, LINKING_ELEMENTS):
            urls.append(cast(pf.Link, node).url)
        return node

    pf.Doc(*element.content).walk(collect)
    return urls


def drop_path_captions(element: pf.Element, doc: pf.Doc) -> pf.Element:
    """Take the caption off a figure captioned with its own path.

    Two spellings of one defect. Most are a file: a caption ending in an image
    suffix. One is a page, `![[000_Solution Compendia]]`, an Obsidian embed
    whose alt text is the page path and carries no suffix to match on; there the
    caption is compared against the target the figure points at instead.

    The `alt` text is left as it stands. It is not displayed, and it is the last
    pointer from the rendered page back to the file in the vault; a caption a
    reader can use has to be written, and writing one here would invent it.
    """
    del doc
    if not isinstance(element, pf.Figure):
        return element
    caption = pf.stringify(element.caption).strip()
    if not caption:
        return element
    repeats_target = any(caption == PurePosixPath(url).stem or caption == url for url in _figure_targets(element))
    if FILE_CAPTION.search(caption) or repeats_target:
        element.caption = pf.Caption()
    return element


def split_front_matter(text: str, path: Path) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: card must start with YAML front matter")
    _, fm, body = text.split("---\n", 2)
    meta = yaml.safe_load(fm)
    if not isinstance(meta, dict):
        raise TypeError(f"{path}: front matter must be a mapping")
    return meta, body


class UnmappedDivClass(ValueError):
    """A fenced-div class with no semantic section kind. Carries the classes so the caller
    can emit a typed diagnostic rather than re-parsing its own message."""

    def __init__(self, classes: list[str]) -> None:
        self.classes = classes
        super().__init__(f"unmapped fenced-div class(es): {', '.join(classes)}")


@dataclass(frozen=True)
class NormalizedAst:
    ast: str
    sections: list[tuple[str, str]]


@dataclass(frozen=True)
class AstDiagnostic:
    code: DiagnosticCode
    message: str


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
        raise UnmappedDivClass(sorted(set(unknown)))
    return found


def _normalize_ast(source: str) -> NormalizedAst | AstDiagnostic:
    try:
        document = from_ast(source).walk(drop_path_captions)
        return NormalizedAst(
            ast=to_json(document),
            sections=extract_sections(document),
        )
    except UnmappedDivClass as exc:
        return AstDiagnostic(DiagnosticCode.UNMAPPED_DIV_CLASS, str(exc))
    except (TypeError, ValueError) as exc:
        return AstDiagnostic(DiagnosticCode.CARD_UNREADABLE, str(exc))


def parse_cards_with(
    pandoc: PandocServer,
    paths: list[Path],
) -> tuple[list[ParsedCard], list[Diagnostic]]:
    adapter: TypeAdapter[Card] = TypeAdapter(Card)
    prepared: list[tuple[Path, Card, str]] = []
    errors: list[Diagnostic] = []
    for path in paths:
        try:
            meta, body = split_front_matter(path.read_text(), path)
            card: Card = adapter.validate_python(meta)
            prepared.append((path, card, body))
        except (OSError, TypeError, ValueError, yaml.YAMLError) as exc:
            errors.append(Diagnostic(DiagnosticCode.CARD_UNREADABLE, str(path), str(exc)))

    bodies = [body for _, _, body in prepared]
    results = read_markdown_parallel(bodies, MARKDOWN) if len(bodies) >= 1_000 else pandoc.read_markdown(bodies, MARKDOWN)
    processable: list[tuple[Path, Card, str]] = []
    for (path, card, _), result in zip(prepared, results, strict=True):
        if isinstance(result, PandocFailure):
            errors.append(Diagnostic(DiagnosticCode.CARD_UNREADABLE, str(path), result.error))
            continue
        warnings = [message.message for message in result.messages if message.verbosity == "WARNING"]
        if warnings:
            errors.append(Diagnostic(DiagnosticCode.READER_WARNING, str(path), "; ".join(warnings)))
            continue
        padded = unread_math(result.output, path)
        if padded:
            errors.append(padded)
        processable.append((path, card, result.output))

    sources = [source for _, _, source in processable]
    if len(sources) >= 1_000:
        with ProcessPoolExecutor(max_workers=4) as executor:
            normalized = list(executor.map(_normalize_ast, sources, chunksize=64))
    else:
        normalized = [_normalize_ast(source) for source in sources]

    parsed: list[ParsedCard] = []
    for (path, card, _), normalized_result in zip(processable, normalized, strict=True):
        if isinstance(normalized_result, NormalizedAst):
            parsed.append(
                ParsedCard(
                    card=card,
                    ast=normalized_result.ast,
                    source_path=str(path),
                    sections=normalized_result.sections,
                )
            )
        else:
            errors.append(
                Diagnostic(
                    normalized_result.code,
                    str(path),
                    normalized_result.message,
                )
            )
    return parsed, errors


def parse_cards(paths: list[Path]) -> tuple[list[ParsedCard], list[Diagnostic]]:
    with PandocServer() as pandoc:
        return parse_cards_with(pandoc, paths)


def parse_card(path: Path) -> ParsedCard:
    parsed, errors = parse_cards([path])
    if errors:
        raise ValueError(errors[0])
    return parsed[0]


def discover(corpus: Path) -> list[Path]:
    """The corpus layout is semantically inert: every .md under it is a card,
    and its path contributes nothing but an edit link."""
    return sorted(p for p in corpus.rglob("*.md"))
