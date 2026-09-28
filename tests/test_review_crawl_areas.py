"""The review crawler walks every registered subject, not a list typed into CI.

The workflow named six areas and never visited `algebraic-geometry`, a wiki
subject with published pages.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_the_area_listing_is_the_wiki_subject_registry() -> None:
    from qualc.index import load_vocabularies

    result = subprocess.run([sys.executable, "-m", "qualc.index", "--root", str(ROOT), "areas"], capture_output=True, text=True)

    assert result.returncode == 0, result.stderr
    listed = result.stdout.split()
    assert "algebraic-geometry" in listed
    assert set(listed) == load_vocabularies(ROOT / "vocabularies", ROOT / "wiki")["areas"]


def test_the_crawl_workflow_reads_areas_from_the_registry() -> None:
    workflow = (ROOT / ".github" / "workflows" / "corpus-review-crawl.yml").read_text()

    assert "qualc.index areas" in workflow
