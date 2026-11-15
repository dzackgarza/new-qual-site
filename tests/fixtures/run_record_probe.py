"""Two tests, named so only `tests/test_run_records.py` collects them.

The duration record of a pytest run is proved by running this module as a real
pytest session and reading the record back. It is not a `test_*.py` file, so the
suite's own collection does not descend into it: what it asserts is the file's
name and its two runs, and being collected by accident would add both to every
run of the suite.
"""

from __future__ import annotations

import time


def test_recorded_slowly() -> None:
    time.sleep(0.02)


def test_recorded_quickly() -> None:
    assert True
