"""GitHub Pages deploys the compiled site."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def test_pages_workflow_uses_the_direct_build_and_immutable_actions() -> None:
    workflow = yaml.safe_load((ROOT / ".github/workflows/development.yml").read_text())
    jobs = workflow["jobs"]
    assert jobs["qc-ci"]["uses"] == "dzackgarza/ai-review-ci/.github/workflows/_qc.yml@main"
    assert jobs["qc-ci"]["with"] == {
        "tier": "test-ci",
        "enforcement": "correctness",
        "profile": "python",
        "infra_ref": "main",
        "setup_recipe": "_ci-setup",
        "setup_cache_paths": "~/texlive",
        "setup_cache_key_files": "ci/texlive.profile",
    }
    assert jobs["build"]["needs"] == "qc-ci"
    steps = [*jobs["build"]["steps"], *jobs["deploy"]["steps"]]
    external_actions = [step["uses"] for step in steps if "uses" in step]
    commands = [step["run"] for step in steps if "run" in step]

    assert external_actions
    assert all(re.fullmatch(r"[^@]+@[0-9a-f]{40}", action) for action in external_actions)
    assert "uv run qualc build" in commands
    # `qualc` drives pandoc itself. A workflow that ran the quarto CLI would be
    # a second, disagreeing publisher. Naming the output directory is not that,
    # so this looks for the command, not the word.
    assert not any(re.search(r"(^|[|&;\s])quarto\s", command) for command in commands)
