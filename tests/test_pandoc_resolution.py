"""The compiler runs the Pandoc release it is pinned to, whatever `PATH` holds.

A direct `.venv/bin/python -m qualc.authoring ...` from a shell whose `PATH`
lacked `~/.local/bin` reached the host's Pandoc 3.1.3 and died, while the same
command through a login shell worked.
"""

from __future__ import annotations

import os
import subprocess
import sys
import textwrap


def test_a_pandoc_server_starts_when_path_holds_only_the_system_pandoc() -> None:
    probe = textwrap.dedent(
        """
        from qualc.pandoc_batch import PandocServer
        from qualc.model import MARKDOWN
        with PandocServer() as pandoc:
            [result] = pandoc.read_markdown(["[[Sylow]]"], MARKDOWN)
        print(type(result).__name__)
        """
    )
    environment = {**os.environ, "PATH": "/usr/bin:/bin"}

    result = subprocess.run([sys.executable, "-c", probe], capture_output=True, text=True, env=environment)

    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "PandocOutput"
