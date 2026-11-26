# Running checks

The push path compiles nothing and writes no queue. `build`, `site`, `crawl` and `preview` all reach the
whole-corpus compile, so none of them is on the push path: `.github/workflows/development.yml` builds,
crawls and deploys on a push to `main`, and its `corpus-reports` job runs `just _reports-ci` for
`BACKLOG.md`, `queues/C-unsolved-cards.md` and `queues/D-prose-only-solutions.md`. `tests/test_push_gate_dependencies.py` holds that shape —
it reads the `justfile` and fails if a recipe a commit or push reaches compiles the corpus, renders the
site, or writes the queue, which is the defect issue #100 recorded when a push ran a full build with
eight Pandoc servers and the queue refusal made it run a second time.

The fan-out of that build is `QUALC_PARALLEL_WORKERS`, a validated integer in 1..8
(`tools/qualc/pandoc_batch.py`). Left unset, the count is the CPU count reduced by the one-minute load
average, rounded up, and by one reserved core, so a machine already carrying work gets fewer Pandoc
servers and a loaded machine gets one. A gate run that does build sets the value explicitly for its
machine instead of taking whatever the default gives there.

Push hooks validate committed card blobs selected for every outgoing ref, including cards committed
without hooks, and run the shared syntax checks. The `test-commit` and `test-push` recipes run `qualc.authoring check-staged` and `check-changes --mode push`
on the exact Git blob identities. `just test-push` additionally runs the extraction detector, macro
mirror check, and focused parser and Git-boundary tests. It is the explicit project diagnostic command;
the shared Git hooks own the automatic syntax and card-data checks.
The full test suite and report generation run in CI. Download the
`corpus-reports` workflow artifact for current `BACKLOG.md`,
`queues/C-unsolved-cards.md` and `queues/D-prose-only-solutions.md` measurements. Select the run for the revision under review:
`gh run view <run-id> --json headSha,status,conclusion`, then download its reports with
`gh run download <run-id> -n corpus-reports -D /tmp/qual-reports-<run-id>`.
Check `corpus-reports-revision.txt` against that run's `headSha` before reading the reports.
Checked-in reports describe their last regeneration; use the selected run's artifact for
that revision's measurements. The site is never
built locally: `.github/workflows/development.yml` builds, crawls and deploys it on every push to
`main`, and `gh run download <run-id> -n github-pages` fetches a built site.

## Every run leaves a duration record

A run of the suite and a run of `qualc` each write one record of what took the time — per test,
per check — named by the commit the run was against and the UTC instant it started, so two runs
are two files and no later run overwrites either. The directory is outside the checkout and
outside git: `build/` is rewritten by every build and `tmp/` and `.scratch/` are scratch, so the
records live in

```
$XDG_STATE_HOME/new-qual-site/run-records
```

(`~/.local/state/new-qual-site/run-records` when `XDG_STATE_HOME` is unset) as `<commit12>-<YYYYMMDD>T<HHMMSS>.<mmm>Z-<tool>.json`. `QUALC_RUN_RECORD_DIR` moves the store,
which is how CI puts a run's records where its upload step can reach them, and every CI workflow
uploads that run's records as an artifact with `if: always()` and 90-day retention. A run whose
root is not a git work tree has no commit to be named by and writes none.

The durations are the ones the tool already reports, not a second measurement over it.
`pytest` keeps every report's duration (`TestReport.duration`, the controller's when xdist is
running) and keeps pytest's own `--junit-xml` report beside them; the hooks are in
`tests/conftest.py`, the writer is `tools/qualc/runrecord.py`. `qualc` reports no duration of its
own, so it times each check as it runs — `parse-cards`, `validate-index`, the wiki link passes,
`lamport-proofs`, and a build's catalog, site and search-index steps — and records that check's
wall time with the number of diagnostics it raised.

Read a record; do not re-run the work to watch a total split. `just timings` lists the ten
most recent runs:

```sh
just timings
uv run python -m qualc.runrecord --tool qualc-check --latest
uv run python -m qualc.runrecord --tool pytest --limit 3
```

A record is a measurement and nothing acts on it: it is not a gate, and `qualc check` does not
fail because a check was slow.

## The gates the `justfile` adds

The `ai_review_ci_*` variables at the top of the `justfile` are the ai-review-ci contract that
its doctor and workflow installers read.

`test-commit` runs two repository gates before the shared syntax check.

`_no-worktrees` enforces QUAL-09: one checkout, one branch. Documentation alone did not hold.
The rule was written down and the fleet rebuilt 27 worktrees anyway, each copying the 353MB
tracked `assets/` tree, and they filled the volume on 2026-09-10 while they held a megabyte of
authored prose between them. With the gate, a stream that opens a worktree finds out at its next
commit, before the volume does.

`_no-bare-disposition` enforces [Sources and gaps](../../AGENTS.md#sources-and-gaps): what the
corpus lacks is added in an ordinary commit of the cards themselves. A queue tick or a
reconciliation note rides in the commit that carries the cards it describes. Committed alone, it
spends a full gate run to move a marker and reports progress that the corpus did not make. A
collection `index.md` marked `completion: complete` with no card touched is the same kind of
commit, so the gate treats queue files and a bare `index.md` alike; an index change that rides
with card work passes. Size does not separate the cases: a six-line reconciliation note
committed alone is still a disposition committed alone. The author does: the steward files work
into the queues under the maintainer's `users.noreply.github.com` address, and a worker commits
under the account address and never commits queue state by itself.

`test-push` names its pytest files explicitly, so site builds and corpus scans stay in CI, and
runs them with `-n 0`, so this small selection does not start one process per CPU.

`test-ci` writes this run's duration record (issue #145), the point of the run past the gate
itself. The test tier runs inside the shared QC workflow, and a workflow that calls another
cannot add a step to it. `.qc-triage/` is the one directory that workflow uploads with
`always()`, so `test-ci` copies the records of the run that just happened there, the record of a
failing run included.

`_ci-setup` restores full TeX Live from the qc-ci setup cache, keyed on `ci/texlive.profile`,
and installs it only when the cache did not supply `lualatex`.
