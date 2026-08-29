"""GitHub Pages deploys the compiled site."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def test_pages_workflow_uses_the_direct_build_and_immutable_actions() -> None:
    workflow = yaml.safe_load((ROOT / ".github/workflows/pages.yml").read_text())
    jobs = workflow["jobs"]
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
