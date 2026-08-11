"""Pinned SSH source revisions used by the archive replay."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SourceRevision:
    name: str
    ssh_url: str
    branch: str
    commit: str


SOURCE_REVISIONS: tuple[SourceRevision, ...] = (
    SourceRevision(
        "qual-wiki",
        "git@github.com:dzackgarza/qual-wiki.git",
        "main",
        "064e3e8815c69d763469e5384b9f85c767f9b9b6",
    ),
    SourceRevision(
        "qual-review-and-solutions",
        "git@github.com:dzackgarza/qual-review-and-solutions.git",
        "master",
        "590a8929b2326cc770a246e934ab36fb30b0c7ab",
    ),
    SourceRevision(
        "make-me-a-qual",
        "git@github.com:dzackgarza/make-me-a-qual.git",
        "master",
        "beba581e5b32f54ff469ed603a0885d51591e5fc",
    ),
    SourceRevision(
        "Analysis-Qual-Compendium",
        "git@github.com:dzackgarza/Analysis-Qual-Compendium.git",
        "master",
        "15168d8df736c3bc99be57e8b48e0675e0cd4e2f",
    ),
    SourceRevision(
        "math-flashcards",
        "git@github.com:dzackgarza/math-flashcards.git",
        "master",
        "cecb473ed7627603d95a9ed6a8e11537711905ef",
    ),
)

TARGET_COMMIT = "510f68f84d41594949b88cf7e280a49821856a8c"
