"""Typed check diagnostics.

Every check failure used to be a formatted string, so the only way a test could
assert *which* diagnostic fired was substring matching on stderr. That passes
when the message is reworded, passes when a different diagnostic happens to
share a word, and says nothing about the failure's identity. Five tests were
written that way.

A `code` makes the identity explicit and machine-checkable, and leaves the
wording free to change. The CLI owns presentation: `--json` emits the structured
form for programs, and the default human output is unchanged.
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
