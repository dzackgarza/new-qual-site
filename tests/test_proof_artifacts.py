"""The proof-artifact entry point, checked against the tree it checks.

Issue #111's third acceptance item, and the #148 it absorbed: `proofs/justfile` is the
documented way to check this repository's certificates, and it still ran `lake env lean`
on twenty-three files that left the tree under #141, so a reader following it failed on
its first line. A corrected file list would drift the same way, so what is checked here
is the rule instead: the recipe names only artifacts that are present, it names no Lean
file at all, and every artifact under `proofs/cards/` is named by it.

The registry half is the check `qualc check` runs, in `certificates.registry_errors`, so
the two entry points cannot disagree; that it reaches the gate too is one of these tests.

These trees are fixtures rather than this repository wherever a rule is what is under
test. The two tests at the end read the real `proofs/` -- statically, with no network --
because "the entry point runs against the current layout" is a claim about this tree.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from conftest import ROOT, diagnostic_codes, fixture_repo
from qualc import certificates, proofs
from qualc.diagnostics import DiagnosticCode

CARD = """---
schema: qual/card@1
id: P-ONE
kind: problem
title: A group of order $p^2$ is abelian
classification:
  areas:
  - algebra
  topics:
  - Groups
relations: []
review: draft
---

::: {.problem}
A group of order $p^2$ is abelian.
:::

::: {.solution}
Its centre is nontrivial, so it is cyclic.
:::
"""

REGISTRY = """# Proof artifacts

## 1. Group lemmas proved in Lean

| File | Card | What it proves | Covers |
| --- | --- | --- | --- |
| `cards/Kept.sage` | `P-ONE` | the fixture computation | the statement |
"""

RECIPE = """check:
    @sage proofs/cards/Kept.sage
"""


def tree(tmp_path: Path, recipe: str = RECIPE, registry: str = REGISTRY, artifacts: tuple[str, ...] = ("Kept.sage",)) -> Path:
    """A repository root with one card, one artifact and one recipe."""
    root = tmp_path / "repo"
    (root / "corpus").mkdir(parents=True)
    (root / "corpus" / "P-ONE.md").write_text(CARD)
    (root / "proofs" / "cards").mkdir(parents=True)
    (root / "proofs" / "README.md").write_text(registry)
    (root / "proofs" / "justfile").write_text(recipe)
    for artifact in artifacts:
        (root / "proofs" / "cards" / artifact).write_text("# the fixture artifact\n")
    return root


def codes(errors: list) -> list[DiagnosticCode]:
    return [error.code for error in errors]


def test_a_recipe_naming_a_file_the_tree_lost_is_an_error(tmp_path: Path) -> None:
    """The #148 shape: the target is right, the file is gone.

    The error names the justfile line, because the repair is to that line.
    """
    recipe = RECIPE + "    @sage proofs/cards/Gone.sage\n"
    root = tree(tmp_path, recipe=recipe, artifacts=("Kept.sage",))

    errors = proofs.recipe_errors(root / "proofs")

    assert codes(errors) == [DiagnosticCode.PROOF_RECIPE_TARGET_MISSING]
    assert errors[0].where == "proofs/justfile:3"
    assert "cards/Gone.sage" in errors[0].detail


def test_a_recipe_invoking_a_lean_file_is_an_error_even_when_the_file_is_here(tmp_path: Path) -> None:
    """Lean declaration validation is lean-categories'; this tree elaborates nothing.

    The file is present, so the rule is about what the recipe may invoke rather than
    about what the tree happens to carry.
    """
    recipe = RECIPE + "    @lake env lean proofs/cards/Kept.lean\n"
    root = tree(tmp_path, recipe=recipe, artifacts=("Kept.sage", "Kept.lean"))

    errors = proofs.recipe_errors(root / "proofs")

    assert codes(errors) == [DiagnosticCode.PROOF_RECIPE_LEAN_TARGET]
    assert errors[0].where == "proofs/justfile:3"


def test_an_artifact_no_recipe_invokes_is_reported(tmp_path: Path) -> None:
    """An artifact that lands in `cards/` and is never run is a check nobody runs."""
    root = tree(tmp_path, artifacts=("Kept.sage", "Unrun.sage"))

    errors = proofs.recipe_errors(root / "proofs")

    assert codes(errors) == [DiagnosticCode.PROOF_RECIPE_ARTIFACT_UNCHECKED]
    assert "cards/Unrun.sage" in errors[0].detail


def test_a_covers_cell_outside_the_certificate_sections_is_an_error(tmp_path: Path) -> None:
    """Section 6 lists repairs with no certificate; a `Covers` cell there claims one.

    Only sections 1 and 2 are read as certificates, so a row that says what it covers
    in any other table records a certification the page will never state.
    """
    registry = REGISTRY + """
## 6. Step repairs, expository

| Card | What the repair does | Covers |
| --- | --- | --- |
| `P-ONE` | rewrites a closing step | part |
"""
    root = tree(tmp_path, registry=registry)

    errors = certificates.unread_section_errors(root / "proofs" / "README.md")

    assert codes(errors) == [DiagnosticCode.CERTIFICATE_SECTION_UNREAD]
    assert "line" in errors[0].detail


def test_the_entry_point_passes_on_a_tree_that_agrees_with_itself(tmp_path: Path) -> None:
    root = tree(tmp_path)

    assert proofs.diagnostics(root) == []
    assert proofs.main(["--root", str(root)]) == 0


def test_the_entry_point_fails_on_a_row_for_a_card_the_corpus_lacks(tmp_path: Path) -> None:
    """The registry rule `qualc check` owns, reached without the pandoc build."""
    registry = REGISTRY.replace("`P-ONE`", "`P-NOT-A-CARD`")
    root = tree(tmp_path, registry=registry)

    errors = proofs.diagnostics(root)

    assert DiagnosticCode.CERTIFICATE_CARD_UNKNOWN in codes(errors)
    assert proofs.main(["--root", str(root)]) == 1


def test_the_corpus_gate_reports_the_unread_scope_too(tmp_path: Path) -> None:
    """One function, two entry points: `qualc check` fails on the same row."""
    work = fixture_repo(tmp_path)
    (work / "proofs").mkdir()
    (work / "proofs" / "README.md").write_text(
        """# Proof artifacts

## 6. Step repairs, expository, with the backing theorem checked

No machine certificate exists for any of them.

| Card | What the repair does | Covers |
| --- | --- | --- |
| `EXE-CENTER` | rewrites a closing step | the statement |
"""
    )

    assert DiagnosticCode.CERTIFICATE_SECTION_UNREAD in diagnostic_codes(work)


def test_this_repository_recipe_names_only_files_it_has() -> None:
    """The current layout, read without running anything and without a network."""
    assert proofs.recipe_errors(ROOT / "proofs") == []
    assert certificates.unread_section_errors(ROOT / "proofs" / "README.md") == []


def test_this_repository_checks_every_artifact_it_keeps() -> None:
    """Every retained Sage, GAP and Python artifact is invoked by the recipe.

    Issue #111's wording is "keeps checking the Sage/GAP artifacts retained in this
    repository": an artifact that stops being invoked stops being checked, silently.
    """
    retained = proofs.retained_artifacts(ROOT / "proofs")

    assert retained == proofs.checked_artifacts(ROOT / "proofs")
    assert sorted(Path(artifact).suffix for artifact in retained) == [".g", ".py", ".sage", ".sage"]
