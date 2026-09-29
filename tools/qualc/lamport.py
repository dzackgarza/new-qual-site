"""Structured proofs: the pandoc-config `lamport_proof.lua` filter, run in batch.

A solution's proof is written in the filter's syntax (`::: {.pf}`, `.pf-step`,
`.pf-proof`, `.pf-qed`, `[step](#label){.pf-ref}`). The filter owns the grammar,
the numbering and the rendering; this module only runs it over many documents in
one `pandoc lua` process.
"""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path

from .pandoc_batch import pandoc_executable

LAMPORT_FILTER = Path.home() / ".pandoc" / "filters" / "lamport_proof.lua"
_BATCH = Path(__file__).with_name("lamport_batch.lua")

# The filter's classes (lamport_proof.lua, "Surface syntax"). They are proof
# structure the filter interprets, not section kinds.
LAMPORT_CLASSES = {
    "pf",
    "pf-step",
    "pf-qed",
    "pf-proof",
    "pf-ref",
    "pf-assume",
    "pf-prove",
    "pf-case",
    "pf-suffices",
    "pf-define",
    "pf-let",
    "pf-conj",
    "pf-disj",
}


@dataclass(frozen=True)
class LamportError:
    message: str


def _has_proof(document: str) -> bool:
    return '"pf"' in document


def apply_lamport(documents: list[str], output: str) -> list[str | LamportError]:
    """Each Pandoc JSON document with the filter applied for `output`, or its error.

    Documents holding no `.pf` root pass through unchanged and cost nothing.
    """
    indices = [index for index, document in enumerate(documents) if _has_proof(document)]
    results: list[str | LamportError] = list(documents)
    if not indices:
        return results
    completed = subprocess.run(
        [str(pandoc_executable()), "lua", str(_BATCH), str(LAMPORT_FILTER), output],
        input=json.dumps([documents[index] for index in indices]),
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"pandoc lua {_BATCH.name} failed (exit {completed.returncode}): {completed.stderr.strip()[:500]}")
    for index, entry in zip(indices, json.loads(completed.stdout), strict=True):
        results[index] = entry["ok"] if "ok" in entry else LamportError(entry["error"])
    return results
