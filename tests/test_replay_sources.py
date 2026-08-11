"""Proof helpers for the fresh-source replay command."""

from __future__ import annotations

from pathlib import Path

from replay_sources import compare_ledger_rows, resolve_target


ROOT = Path(__file__).resolve().parent.parent


def test_ledger_comparison_rejects_a_source_path_drift() -> None:
    rows = [{"repo": "qual-wiki", "path": "README.md", "disposition": "dropped", "reason": "documentation"}]

    result = compare_ledger_rows(
        rows,
        {"qual-wiki": {"README.md", "new.md"}},
    )

    assert result == ["qual-wiki: missing ledger row for new.md"]


def test_resolve_target_follows_the_committed_g6_route_map() -> None:
    target = resolve_target(ROOT, "wiki/Topology/ReviewDoc/sections/001_Definitions.md")

    assert target == ROOT / "wiki/40_Topology/020_Point_Set/001_Definitions.md"
