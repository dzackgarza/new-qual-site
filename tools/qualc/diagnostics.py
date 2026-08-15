"""Typed check diagnostics.

Each failure carries a stable `code`, so tests assert which diagnostic fired
and the wording stays free to change. The CLI owns presentation: `--json`
emits the structured form for programs; the default human output is unchanged.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

DiagnosticCode = Literal[
    # identity and registry
    "duplicate-id",
    "unknown-area",
    "unknown-topic",
    "unknown-institution",
    "unknown-textbook",
    # relations
    "dangling-relation",
    "occurrence-missing-source",
    "occurrence-source-not-a-source-card",
    "occurrence-instance-of-count",
    "occurrence-instance-of-not-a-problem",
    # reading
    "card-unreadable",
    "reader-warning",
    "unmapped-div-class",
    # pages
    "page-reference-missing",
    "page-reference-ambiguous",
    "asset-unresolved",
    "unknown-citation",
]


@dataclass(frozen=True)
class Diagnostic:
    """One check failure.

    `where` is a source path or a card id -- enough to find it. `detail` is for
    a human reading the terminal and is deliberately not part of the contract:
    assert on `code`, never on `detail`.
    """

    code: DiagnosticCode
    where: str
    detail: str

    def __str__(self) -> str:
        return f"{self.where}: {self.detail}"

    def as_dict(self) -> dict[str, str]:
        return {"code": self.code, "where": self.where, "detail": self.detail}
