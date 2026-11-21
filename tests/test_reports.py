"""Hosted reports use one parsed corpus for the backlog and for both queues."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from conftest import fixture_repo

ROOT = Path(__file__).resolve().parent.parent


def test_combined_reports_match_the_standalone_queues(tmp_path: Path) -> None:
    work = fixture_repo(
        tmp_path,
        {
            "P-EXTRA.md": (
                "---\nschema: qual/card@1\nid: P-EXTRA\nkind: problem\n"
                "title: An unsolved problem\nclassification:\n  areas: [algebra]\n"
                "  topics: [Groups]\nrelations: []\nreview: draft\n---\n\n"
                "::: problem\nProve the claim.\n:::"
            )
        },
    )
    combined = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "backlog.py"),
            "--root",
            str(work),
            "--with-queues",
        ],
        capture_output=True,
        text=True,
    )
    assert combined.returncode == 0, combined.stderr
    backlog = work / "BACKLOG.md"
    queue = work / "queues" / "C-unsolved-cards.md"
    prose_queue = work / "queues" / "D-prose-only-solutions.md"
    assert backlog.is_file()
    assert 'P-EXTRA — "An unsolved problem"' in queue.read_text()
    assert prose_queue.is_file()
    combined_queues = queue.read_bytes(), prose_queue.read_bytes()

    standalone = {
        queue: subprocess.run(
            [sys.executable, str(ROOT / "tools" / "unsolved_queue.py"), "--root", str(work)],
            capture_output=True,
            text=True,
        ),
        prose_queue: subprocess.run(
            [sys.executable, str(ROOT / "tools" / "prose_queue.py"), "--root", str(work)],
            capture_output=True,
            text=True,
        ),
    }
    for path, result in standalone.items():
        assert result.returncode == 0, result.stderr
    assert (queue.read_bytes(), prose_queue.read_bytes()) == combined_queues
