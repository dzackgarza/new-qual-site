"""Typed check diagnostics.

Each failure carries a `DiagnosticCode` member, so tests assert which
diagnostic fired and the wording stays free to change. The CLI owns presentation: `--json`
emits the structured form for programs; the default human output is unchanged.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class DiagnosticCode(Enum):
    # identity and registry
    DUPLICATE_ID = "duplicate-id"
    UNKNOWN_AREA = "unknown-area"
    UNKNOWN_INSTITUTION = "unknown-institution"
    UNKNOWN_TEXTBOOK = "unknown-textbook"
    # relations
    DANGLING_RELATION = "dangling-relation"
    # reading
    CARD_UNREADABLE = "card-unreadable"
    READER_WARNING = "reader-warning"
    UNREAD_MATH = "unread-math"
    UNMAPPED_DIV_CLASS = "unmapped-div-class"
    # pages
    PAGE_REFERENCE_MISSING = "page-reference-missing"
    PUBLICATION_REFERENCE_MISSING = "publication-reference-missing"
    PAGE_REFERENCE_AMBIGUOUS = "page-reference-ambiguous"
    PAGE_MISSING_ORDER = "page-missing-order"
    PAGE_DIRECTORY_MISSING_INDEX = "page-directory-missing-index"
    ASSET_UNRESOLVED = "asset-unresolved"
    UNKNOWN_CITATION = "unknown-citation"


@dataclass(frozen=True)
class Diagnostic:
    """One check failure.

    `where` is a source path or a card id -- enough to find it. `detail` is for
    a human reading the terminal and is deliberately not part of the contract:
    assert on the `DiagnosticCode` member, never on `detail`.
    """

    code: DiagnosticCode
    where: str
    detail: str

    def __str__(self) -> str:
        return f"{self.where}: {self.detail}"

    def as_dict(self) -> dict[str, str]:
        return {"code": self.code.value, "where": self.where, "detail": self.detail}
