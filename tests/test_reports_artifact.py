"""What CI's `corpus-reports` artifact carries, and the patch that finishes Queue D's half.

The `reports` job uploads an explicit path list, so a report not named in it is not in the
artifact however often it is written. Queue C is named there. Queue D is not, and the
addition is a workflow edit: a push from this project's GitHub connection is refused for
workflow files ("...without `workflows` permission"), so the line lives in
`results/queue-d-workflows.patch` until someone applies it.

This module decides that patch. Two facts, both read from the workflow file rather than
from the report:

* the artifact's path list names Queue C (the queue that has always been published), and
* Queue D is either named there already, or the committed patch applies cleanly to this
  tree and names it when applied.

The second test passes in both worlds by design: it must not go red for a change nobody
here can push, and once the patch is applied the first branch is what holds.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WORKFLOW = Path(".github/workflows/development.yml")
PATCH = ROOT / "results" / "queue-d-workflows.patch"
QUEUE_C = "queues/C-unsolved-cards.md"
QUEUE_D = "queues/D-prose-only-solutions.md"


def artifact_paths(workflow_text: str) -> list[str]:
    """The `corpus-reports` artifact's path list, read off the job that uploads it."""
    document = yaml.safe_load(workflow_text)
    uploads = [
        step
        for step in document["jobs"]["reports"]["steps"]
        if str(step.get("uses", "")).startswith("actions/upload-artifact")
    ]
    assert len(uploads) == 1, f"the reports job uploads {len(uploads)} artifacts; this test reads one"
    entries = uploads[0]["with"]["path"]
    return [line.strip() for line in entries.splitlines() if line.strip()]


def test_the_report_artifact_names_the_published_queues() -> None:
    paths = artifact_paths(WORKFLOW.read_text())
    assert QUEUE_C in paths, f"the unsolved queue left the corpus-reports artifact: {paths}"
    assert QUEUE_D in paths or PATCH.is_file(), (
        f"{QUEUE_D} is not in the corpus-reports artifact and no patch adds it: {paths}"
    )


def test_the_workflow_patch_adds_the_prose_queue(tmp_path: Path) -> None:
    if QUEUE_D in artifact_paths(WORKFLOW.read_text()):
        return  # applied: the patch has done its job and is no longer this test's subject
    target = tmp_path / WORKFLOW
    target.parent.mkdir(parents=True)
    shutil.copy(WORKFLOW, target)
    applied = subprocess.run(
        ["git", "apply", str(PATCH)],
        cwd=tmp_path,
        text=True,
        capture_output=True,
        check=False,
    )
    assert applied.returncode == 0, (
        f"{PATCH.relative_to(ROOT)} no longer applies to {WORKFLOW}: {applied.stderr.strip()}"
    )
    paths = artifact_paths(target.read_text())
    assert QUEUE_D in paths, f"the patch applied but the artifact still lacks {QUEUE_D}: {paths}"
    assert QUEUE_C in paths, f"the patch dropped the unsolved queue from the artifact: {paths}"
