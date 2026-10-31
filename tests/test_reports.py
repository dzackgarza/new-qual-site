"""Hosted reports use one parsed corpus for backlog and unsolved output."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from conftest import fixture_repo

ROOT = Path(__file__).resolve().parent.parent


def test_combined_reports_match_the_standalone_unsolved_queue(tmp_path: Path) -> None:
    work = fixture_repo(
        tmp_path,
        {
            "P-EXTRA.md": (
                "---\nschema: qual/card@1\nid: P-EXTRA\nkind: problem\n"
                "title: An unsolved problem\nclassification:\n  areas: [algebra]\n"
                "  topics: [Groups]\nrelations: []\nreview: draft\n---\n\n"
                "::: problem\nProve the claim.\n:::\n"
            )
        },
    )
    combined = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "backlog.py"),
            "--root",
            str(work),
            "--with-unsolved",
        ],
        capture_output=True,
        text=True,
    )
    assert combined.returncode == 0, combined.stderr
    backlog = work / "BACKLOG.md"
    queue = work / "queues" / "C-unsolved-cards.md"
    assert backlog.is_file()
    assert 'P-EXTRA — "An unsolved problem"' in queue.read_text()
    combined_queue = queue.read_bytes()

    standalone = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "unsolved_queue.py"),
            "--root",
            str(work),
        ],
        capture_output=True,
        text=True,
    )
    assert standalone.returncode == 0, standalone.stderr
    assert queue.read_bytes() == combined_queue
