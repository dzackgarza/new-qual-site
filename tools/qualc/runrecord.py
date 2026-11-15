"""One duration record per run of `qualc` and per run of the test suite.

A timing question -- how long `qualc check` takes, which of its checks is the
expensive one, which test is the slow one, whether the last run got slower --
is answered from a record, never by running the work again to watch a total
split. So each run writes one record, named by the commit it ran against and
the instant it started, and no later run can overwrite it: the record
directory is outside the checkout (`build/` is rewritten by every build,
`tmp/` and `.scratch/` are scratch) and outside git, so a record can never be
staged, committed, or swept up by a formatter.

The numbers are the ones the tool already reports, not a second measurement
laid over it. `pytest` reports a duration for every report it makes
(`TestReport.duration`, on the controller too when xdist is running); the
suite's plugin keeps those and keeps pytest's own `--junit-xml` file beside
them. `qualc` has no such report of its own, so it times each check it runs,
which is the one place a clock is the right source.

A record is a measurement and nothing acts on it: it is not a gate, and
`qualc check` never fails because a check was slow.

    just timings                    # the ten most recent runs, both tools
    uv run python -m qualc.runrecord # the same
    uv run python -m qualc.runrecord --tool qualc-check --limit 3
    uv run python -m qualc.runrecord --latest --tool pytest

`QUALC_RUN_RECORD_DIR` moves the store, which is how CI keeps a run's records
where its upload step can reach them; the default is under `$XDG_STATE_HOME`
and is stated in AGENTS.md.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import subprocess
import sys
import time
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, cast

SCHEMA = "qualc/run-record@1"
DIRECTORY_ENV = "QUALC_RUN_RECORD_DIR"
STORE_PARTS = ("new-qual-site", "run-records")

QUALC_CHECK = "qualc-check"
QUALC_BUILD = "qualc-build"
PYTEST = "pytest"


def records_dir() -> Path:
    """Where records live: outside the checkout, and outside every path a run rewrites."""
    override = os.environ.get(DIRECTORY_ENV)
    if override:
        return Path(override).expanduser().resolve()
    state = os.environ.get("XDG_STATE_HOME")
    base = Path(state).expanduser() if state else Path.home() / ".local" / "state"
    return base.joinpath(*STORE_PARTS).resolve()


def _git(root: Path, *args: str) -> subprocess.CompletedProcess[str] | None:
    try:
        return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, check=False)
    except OSError:
        return None


def current_commit(root: Path) -> str | None:
    """The commit this run is named by, or None where there is no commit to name.

    A record's name is the pair (commit, start), so a checkout that is not a
    git work tree, or one with no commit yet, has no name to give. That is also
    what keeps the suite's fixture repos -- built in a temporary directory and
    not under git -- from filling the store with runs that describe no revision.
    """
    result = _git(root, "rev-parse", "--verify", "HEAD")
    if result is None or result.returncode != 0:
        return None
    commit = result.stdout.strip()
    return commit if len(commit) == 40 else None


def work_tree_dirty(root: Path) -> bool:
    """Whether tracked files differ from the commit, which makes timings less comparable."""
    result = _git(root, "status", "--porcelain", "--untracked-files=no")
    return bool(result is not None and result.returncode == 0 and result.stdout.strip())


@dataclass
class Run:
    """One invocation, from the moment it started."""

    tool: str
    commit: str
    started: datetime
    directory: Path
    dirty: bool = False
    extra: dict[str, Any] = field(default_factory=dict)

    @property
    def started_at(self) -> str:
        return self.started.isoformat(timespec="milliseconds")

    @property
    def stamp(self) -> str:
        millis = f"{self.started.microsecond // 1000:03d}"
        return f"{self.started.strftime('%Y%m%dT%H%M%S')}.{millis}Z"

    @property
    def stem(self) -> str:
        return f"{self.commit[:12]}-{self.stamp}-{self.tool}"

    def path(self, suffix: str = ".json") -> Path:
        return self.directory / f"{self.stem}{suffix}"

    def write(
        self,
        *,
        exit_status: int,
        entries: dict[str, Any],
        artifacts: dict[str, str] | None = None,
        wall_seconds: float | None = None,
    ) -> Path:
        """Write this run's record, atomically, and answer where it went."""
        finished = datetime.now(UTC)
        record: dict[str, Any] = {
            "schema": SCHEMA,
            "tool": self.tool,
            "commit": self.commit,
            "commit_short": self.commit[:12],
            "work_tree_dirty": self.dirty,
            "started_at": self.started_at,
            "finished_at": finished.isoformat(timespec="milliseconds"),
            "wall_seconds": round(wall_seconds if wall_seconds is not None else (finished - self.started).total_seconds(), 3),
            "exit_status": exit_status,
            "argv": list(sys.argv),
            "python": platform.python_version(),
            "host": platform.node(),
            **self.extra,
            **entries,
        }
        if artifacts:
            record["artifacts"] = artifacts
        destination = self.path()
        destination.parent.mkdir(parents=True, exist_ok=True)
        partial = destination.with_name(destination.name + ".partial")
        partial.write_text(json.dumps(record, indent=2, sort_keys=False) + "\n")
        os.replace(partial, destination)
        return destination


def new_run(tool: str, root: Path | None = None) -> Run | None:
    """Start a record for `tool` at `root`, or None where no commit names it."""
    where = Path.cwd() if root is None else Path(root)
    commit = current_commit(where)
    if commit is None:
        # Not a checkout at all is the ordinary fixture case and stays quiet.
        # A checkout whose commit could not be read is the one way a run would
        # silently leave no record, so say so instead of passing it over.
        if _within_work_tree(where):
            print(f"run record: no commit at {where}; this run writes no record", file=sys.stderr)
        return None
    return Run(tool=tool, commit=commit, started=datetime.now(UTC), directory=records_dir(), dirty=work_tree_dirty(where))


def _within_work_tree(root: Path) -> bool:
    where = root.resolve()
    for candidate in (where, *where.parents):
        if (candidate / ".git").exists():
            return True
    return False


@contextmanager
def check(log: list[dict[str, Any]], name: str, errors: list[Any] | None = None) -> Iterator[dict[str, Any]]:
    """Time one check into `log`, including the count of diagnostics it raised.

    The clock is this module's own because `qualc check` has no report to read:
    it runs its checks in one pass and prints a total.
    """
    entry: dict[str, Any] = {"check": name, "seconds": 0.0, "errors": 0}
    before = len(errors) if errors is not None else 0
    started = time.perf_counter()
    try:
        yield entry
    finally:
        entry["seconds"] = round(time.perf_counter() - started, 6)
        if errors is not None:
            entry["errors"] = len(errors) - before
        log.append(entry)


def read_record(path: Path | str) -> dict[str, Any]:
    return cast("dict[str, Any]", json.loads(Path(path).read_text()))


def records(tool: str | None = None) -> list[tuple[Path, dict[str, Any]]]:
    """Every readable record in the store, newest first."""
    directory = records_dir()
    if not directory.is_dir():
        return []
    found: list[tuple[Path, dict[str, Any]]] = []
    for path in directory.glob("*.json"):
        try:
            record = read_record(path)
        except (OSError, ValueError):
            # A half-written or foreign file is not a record; `show` reports it
            # rather than hiding it, since a record that cannot be read is the
            # one thing this store exists to prevent.
            print(f"unreadable record: {path}", file=sys.stderr)
            continue
        if tool is not None and record.get("tool") != tool:
            continue
        found.append((path, record))
    found.sort(key=lambda item: str(item[1].get("started_at", "")), reverse=True)
    return found


def latest(tool: str | None = None) -> tuple[Path, dict[str, Any]] | None:
    found = records(tool)
    return found[0] if found else None


def summary(record: dict[str, Any]) -> list[str]:
    """The lines that answer a timing question about one record."""
    lines = [
        f"{record.get('started_at', '?')}  {record.get('tool', '?')}  {record.get('commit_short', '?')}  "
        f"exit={record.get('exit_status', '?')}  wall={record.get('wall_seconds', '?')}s  "
        f"{'dirty' if record.get('work_tree_dirty') else 'clean'}  python {record.get('python', '?')}"
    ]
    checks = record.get("checks")
    if isinstance(checks, list) and checks:
        for entry in sorted(checks, key=lambda item: float(item.get("seconds", 0.0)), reverse=True):
            lines.append(f"    {entry.get('check', '?'):<24} {entry.get('seconds', 0.0):>8.3f}s  errors={entry.get('errors', 0)}")
    tests = record.get("tests")
    if isinstance(tests, list) and tests:
        slowest = sorted(tests, key=lambda item: float(item.get("seconds", 0.0)), reverse=True)
        lines.append(f"    {len(tests)} test report(s)")
        for entry in slowest[:10]:
            lines.append(f"    {entry.get('seconds', 0.0):>8.3f}s  {entry.get('phase', '?'):<8} {entry.get('nodeid', '?')}")
    for name, path in sorted(dict(record.get("artifacts") or {}).items()):
        lines.append(f"    artifact {name}: {path}")
    return lines


def pytest_configure(config: Any) -> None:
    """Start this test run's record and point pytest's own JUnit report at it.

    Called from `tests/conftest.py`; `pytest` is deliberately not imported here,
    because `qualc` runs on machines with no test dependencies installed.

    An xdist worker returns at once: the controller receives every worker's
    report, so it is the controller that has the whole run and owns the record.
    """
    if hasattr(config, "workerinput"):
        return
    run = new_run(PYTEST)
    if run is None:
        return
    # `--junit-xml` is the report pytest already writes, with a `time` on every
    # test case. Keeping that file beside the record means the record never has
    # to be the only copy of a number. A caller who chose their own path keeps it.
    if config.option.xmlpath is None:
        config.option.xmlpath = str(run.path(".junit.xml"))
        setattr(config, "_qualc_junit", run.path(".junit.xml").name)
    # `sys.argv` here is the interpreter's, which says nothing a reader can use;
    # the arguments pytest was given are what make one run comparable to another.
    run.extra = {"argv": list(config.invocation_params.args)}
    setattr(config, "_qualc_run", run)


def pytest_sessionfinish(session: Any, exitstatus: Any) -> None:
    """Write the record from the durations pytest itself reported.

    `TerminalReporter.stats` holds the `TestReport` objects `--durations` reads,
    each carrying pytest's own `duration`; on an xdist controller they are the
    relayed reports, so this is the run's whole measurement, not one worker's.
    """
    config = session.config
    if hasattr(config, "workerinput"):
        return
    run: Run | None = getattr(config, "_qualc_run", None)
    if run is None:
        return
    tests: list[dict[str, Any]] = []
    reporter = config.pluginmanager.getplugin("terminalreporter")
    for reports in getattr(reporter, "stats", {}).values():
        for report in reports:
            duration = getattr(report, "duration", None)
            if duration is None:
                continue
            tests.append(
                {
                    "nodeid": report.nodeid,
                    "phase": report.when,
                    "seconds": round(duration, 6),
                    "outcome": report.outcome,
                }
            )
    tests.sort(key=lambda entry: entry["seconds"], reverse=True)
    artifacts = {}
    junit = getattr(config, "_qualc_junit", None)
    if junit is not None:
        artifacts["junit_xml"] = junit
    try:
        run.write(
            exit_status=int(exitstatus),
            entries={
                "collected": getattr(session, "testscollected", None),
                "durations_option": config.option.durations,
                "tests": tests,
            },
            artifacts=artifacts,
        )
    except OSError as error:
        # A test run is not a place to fail over its own bookkeeping.
        print(f"could not write the run record: {error}", file=sys.stderr)


def _main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m qualc.runrecord", description="Read the duration records of past runs.")
    parser.add_argument("--tool", choices=[QUALC_CHECK, QUALC_BUILD, PYTEST], help="only records of this tool")
    parser.add_argument("--limit", type=int, default=10, help="how many records to show (default 10)")
    parser.add_argument("--latest", action="store_true", help="show only the most recent matching record")
    parser.add_argument("--dir", action="store_true", help="print the record directory and stop")
    args = parser.parse_args(argv)

    directory = records_dir()
    if args.dir:
        print(directory)
        return 0
    found = records(args.tool)
    if not found:
        print(f"no records in {directory}", file=sys.stderr)
        return 1
    shown = found[:1] if args.latest else found[: args.limit]
    print(f"{len(found)} record(s) in {directory}")
    for path, record in shown:
        for line in summary(record):
            print(line)
        if args.latest:
            print(f"    file {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
