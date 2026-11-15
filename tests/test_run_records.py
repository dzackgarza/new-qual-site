"""The record each run leaves behind, read back the way a timing question is.

Issue #145: a run of the suite and a run of `qualc check` each write a file
named by commit and start time, in a directory no later run overwrites and
outside git, and a timing question is answered from that file instead of from
a second run of the work.

Nothing here times anything. `qualc check` writes the wall time of each of its
checks as they run; pytest writes a duration for every report it makes and a
JUnit report beside them. These tests read those files back, which is the
reading a person does when they ask where a run's time went.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

import pytest
from conftest import ROOT, fixture_repo, run_qualc
from qualc import runrecord

PROBE = ROOT / "tests" / "fixtures" / "run_record_probe.py"
NAME = re.compile(r"^[0-9a-f]{12}-\d{8}T\d{6}\.\d{3}Z-(qualc-check|qualc-build|pytest)\.json$")


def git(root: Path, *args: str) -> str:
    done = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, check=True)
    return done.stdout.strip()


def committed(root: Path) -> str:
    """The fixture repo as a commit, since a record is named by one."""
    git(root, "init", "-q", "-b", "main")
    git(root, "add", "-A")
    git(root, "-c", "user.email=record@example.invalid", "-c", "user.name=record", "commit", "-qm", "fixture")
    return git(root, "rev-parse", "HEAD")


def test_qualc_check_writes_its_record(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    work = fixture_repo(tmp_path)
    commit = committed(work)
    store = tmp_path / "records"
    monkeypatch.setenv(runrecord.DIRECTORY_ENV, str(store))

    result = run_qualc("check", work)
    assert result.returncode == 0, result.stderr
    assert f"record: {store}" in result.stdout

    found = runrecord.records(runrecord.QUALC_CHECK)
    assert len(found) == 1, [path for path, _ in found]
    path, record = found[0]
    assert NAME.match(path.name), path.name
    assert path.name.startswith(commit[:12])
    assert record["commit"] == commit
    assert record["command"] == "check"
    assert record["exit_status"] == 0
    assert not path.is_relative_to(work), "the record belongs outside the checkout"

    checks = {entry["check"]: entry for entry in record["checks"]}
    # Every check the run performed is in the record, and none of them is a
    # zero-length stage standing in for one that was never reached.
    assert {"parse-cards", "validate-index", "parse-wiki-pages", "lamport-proofs"} <= set(checks)
    assert checks["parse-cards"]["seconds"] > 0
    assert all(entry["seconds"] >= 0 for entry in checks.values()), checks
    assert all(entry["errors"] == 0 for entry in checks.values()), checks
    assert sum(entry["seconds"] for entry in checks.values()) <= record["wall_seconds"] + 0.001
    assert record["cards"] > 0 and record["wiki_pages"] > 0


def test_pytest_run_writes_its_record(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    store = tmp_path / "records"
    monkeypatch.setenv(runrecord.DIRECTORY_ENV, str(store))
    environment = {**os.environ, runrecord.DIRECTORY_ENV: str(store), "PYTEST_ADDOPTS": ""}
    result = subprocess.run(
        [sys.executable, "-m", "pytest", str(PROBE), "-q", "-o", "addopts=", "-p", "no:cacheprovider"],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr

    found = runrecord.records(runrecord.PYTEST)
    assert len(found) == 1, [path for path, _ in found]
    path, record = found[0]
    assert NAME.match(path.name), path.name
    assert record["commit"] == git(ROOT, "rev-parse", "HEAD")
    assert record["exit_status"] == 0
    assert record["collected"] == 2

    reported = {entry["nodeid"]: entry for entry in record["tests"] if entry["phase"] == "call"}
    # pytest's own duration for each test, not a clock this test started: the
    # slow probe is the one the record puts first.
    assert set(reported) == {f"{PROBE.relative_to(ROOT)}::{name}" for name in ("test_recorded_slowly", "test_recorded_quickly")}
    assert record["tests"][0]["nodeid"].endswith("test_recorded_slowly")
    assert reported[f"{PROBE.relative_to(ROOT)}::test_recorded_slowly"]["seconds"] >= 0.02

    # pytest's `--junit-xml` report is kept beside the record, so no number in
    # it rests on this repository's own bookkeeping.
    junit = store / record["artifacts"]["junit_xml"]
    assert junit.is_file()
    # pytest's own per-case `time`, not a value this repository computed: the
    # one number that must be there is pytest's, and it is somewhere near the
    # duration the record gives the same test.
    body = junit.read_text()
    assert 'name="test_recorded_slowly" time="' in body
    measured = re.search(r'name="test_recorded_slowly" time="([0-9.]+)"', body)
    assert measured is not None
    assert float(measured.group(1)) > 0


def test_the_default_store_is_outside_the_checkout(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(runrecord.DIRECTORY_ENV, raising=False)
    store = runrecord.records_dir()
    assert not store.is_relative_to(ROOT), store
    # Outside git follows from outside the checkout: there is no index that
    # could hold a record and no formatter that could rewrite one.
    assert not store.is_relative_to(ROOT / "build")
    assert subprocess.run(["git", "-C", str(store), "rev-parse", "--show-toplevel"], capture_output=True, check=False).returncode != 0


def test_a_checkout_with_no_commit_to_name_a_run_writes_none(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert runrecord.new_run(runrecord.QUALC_CHECK, tmp_path) is None
    assert capsys.readouterr().err == ""

    # A work tree that exists but whose commit cannot be read is the one way a
    # run would leave no record without saying anything.
    (tmp_path / ".git").mkdir()
    assert runrecord.new_run(runrecord.QUALC_CHECK, tmp_path) is None
    assert "writes no record" in capsys.readouterr().err
