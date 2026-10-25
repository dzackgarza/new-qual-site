#!/usr/bin/env -S uv run --no-sync python
"""Validate card blobs supplied by ai-review-ci's local Git hooks."""

import sys

from qualc.authoring import main

if __name__ == "__main__":
    raise SystemExit(main(["check-changes", *sys.argv[1:]]))
