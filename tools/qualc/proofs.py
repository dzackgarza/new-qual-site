"""The proof-artifact check this repository runs on itself.

Lean declarations are validated in lean-categories, not here (issue #141): no
`.lean` file and no lake project lives under `proofs/` any more, and a Lean
certificate of a card is the declaration a section-1 row of `proofs/README.md`
links on lean-categories main, or the file at the commit that still carries it.
What this repository can check is everything around those declarations:

- the **registry** — the rows that map a certificate to a card — by the same
  function `qualc check` uses, so a row's link is followed, its card is looked
  up and its `Covers` cell is required, and a row in a section that certifies
  nothing is an error instead of a silently unread line;
- the **recipe** — `proofs/justfile`, the documented entry point — against the
  tree it names: every artifact it invokes is there, no `.lean` file is invoked
  at all, and every artifact left in `cards/` is invoked, so neither the #148
  shape (a recipe invoking files that have left the repository) nor its
  opposite (an artifact nobody runs) can reappear without failing.

It reads the corpus front matter for the card ids and nothing else, so it needs
no pandoc and no build: `python -m qualc.proofs` finishes in seconds, which is
what lets `proofs/justfile`'s `check` be an entry point a reader follows.

The exact computations themselves are run by the recipe, not here: Sage, GAP and
Python are the images' business (`proofs/README.md` §2 records which).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

from . import certificates as certificate
from .diagnostics import Diagnostic, DiagnosticCode
from .model import discover, split_front_matter

# What the recipe may invoke: the retained artifacts, by extension. A recorded
# output (`.out`) is evidence of a run, not a computation, so it is not one.
ARTIFACT_SUFFIXES = (".sage", ".g", ".py")

# A path the recipe names: an artifact under `cards/`, or a Lean file, which it
# must not name at all.
_NAMED = re.compile(r"cards/[\w.\-/]+\.(?:lean|sage|g|py)\b")

# Lean declaration validation belongs to lean-categories; this repository's
# recipe is for the artifacts that are still here.
RECIPE = "proofs/justfile"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="qualc.proofs",
        description="Check the proof-artifact registry and recipe against this tree.",
    )
    ap.add_argument("--root", type=Path, default=Path.cwd(), help="repository root")
    args = ap.parse_args(argv)
    errors = diagnostics(args.root)
    if errors:
        print(f"{len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1
    registry = certificate.load(args.root / "proofs")
    print(
        f"{sum(len(entries) for entries in registry.values())} certificate rows for "
        f"{len(registry)} cards resolve; {RECIPE} invokes "
        f"{len(checked_artifacts(args.root / 'proofs'))} artifact(s) and no Lean file"
    )
    return 0


def diagnostics(root: Path) -> list[Diagnostic]:
    """Every error `proofs/` carries: the registry's rows and the recipe's targets."""
    ids, errors = card_ids(root)
    errors.extend(certificate.registry_errors(root, certificate.load(root / "proofs"), ids))
    errors.extend(recipe_errors(root / "proofs"))
    return errors


def card_ids(root: Path) -> tuple[set[str], list[Diagnostic]]:
    """Every card id the corpus carries, from the front matter alone.

    No pandoc and no schema: this check is about `proofs/`, and the corpus is
    read only to know which ids a certificate row may name. A card the
    front-matter reader cannot parse is reported here, because a row naming that
    card would otherwise be called unknown for the wrong reason. A file with no
    `id` is not reported: the corpus gate owns that.
    """
    ids: set[str] = set()
    errors: list[Diagnostic] = []
    for path in discover(root / "corpus"):
        try:
            meta, _ = split_front_matter(path.read_text(), path)
        except (OSError, TypeError, ValueError, yaml.YAMLError) as error:
            errors.append(Diagnostic(DiagnosticCode.CARD_UNREADABLE, str(path), str(error)))
            continue
        identity = meta.get("id")
        if isinstance(identity, str):
            ids.add(identity)
    return ids, errors


def recipe_errors(proofs: Path) -> list[Diagnostic]:
    """`proofs/justfile` against the tree: what it names, and what it leaves out.

    #148 is the shape: `check` ran `lake env lean cards/FieldHomework1.lean` and
    twenty-two more, the tree carried none of them, and the documented entry
    point failed on its first line. The repair is not a corrected file list to
    drift again but a rule — the recipe names artifacts that are here, names no
    Lean file, and covers every artifact in `cards/`.
    """
    justfile = proofs / "justfile"
    if not justfile.is_file():
        return [
            Diagnostic(
                DiagnosticCode.PROOF_RECIPE_TARGET_MISSING,
                RECIPE,
                "the documented proof-checking entry point is not in the tree",
            )
        ]
    errors: list[Diagnostic] = []
    targets = named_targets(justfile)
    for number, target in targets:
        if target.endswith(".lean"):
            errors.append(
                Diagnostic(
                    DiagnosticCode.PROOF_RECIPE_LEAN_TARGET,
                    f"{RECIPE}:{number}",
                    f"invokes {target}: Lean declarations are validated in lean-categories, "
                    "and this tree holds no Lean file to invoke",
                )
            )
        elif not (proofs / target).is_file():
            errors.append(
                Diagnostic(
                    DiagnosticCode.PROOF_RECIPE_TARGET_MISSING,
                    f"{RECIPE}:{number}",
                    f"invokes {target}, which the tree does not carry",
                )
            )
    for artifact in retained_artifacts(proofs):
        if artifact not in {target for _, target in targets}:
            errors.append(
                Diagnostic(
                    DiagnosticCode.PROOF_RECIPE_ARTIFACT_UNCHECKED,
                    RECIPE,
                    f"does not invoke {artifact}, which is retained in the tree",
                )
            )
    return errors


def named_targets(justfile: Path) -> list[tuple[int, str]]:
    """Every `cards/...` path the recipe names, once, with the line naming it."""
    seen: set[str] = set()
    out: list[tuple[int, str]] = []
    for number, line in enumerate(justfile.read_text().splitlines(), 1):
        if line.lstrip().startswith("#"):
            continue
        for target in _NAMED.findall(line):
            if target not in seen:
                seen.add(target)
                out.append((number, target))
    return out


def retained_artifacts(proofs: Path) -> list[str]:
    """The checkable artifacts under `cards/`, as the recipe must name them."""
    cards = proofs / "cards"
    if not cards.is_dir():
        return []
    return sorted(
        f"cards/{path.name}" for path in cards.iterdir() if path.suffix in ARTIFACT_SUFFIXES
    )


def checked_artifacts(proofs: Path) -> list[str]:
    """The artifacts the recipe does invoke, which is what a green run covers."""
    justfile = proofs / "justfile"
    if not justfile.is_file():
        return []
    named = {target for _, target in named_targets(justfile)}
    return [artifact for artifact in retained_artifacts(proofs) if artifact in named]


if __name__ == "__main__":
    raise SystemExit(main())
