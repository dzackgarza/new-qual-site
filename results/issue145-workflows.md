# Issue #145 — the workflow half, as a patch

`issue145-workflows.patch` is a `git apply`-able diff for the file a push from this
connection cannot carry (a workflow file). Apply it from the repository root:

```sh
git apply results/issue145-workflows.patch
```

## Files it touches

- `.github/workflows/development.yml`

Nothing else is in the patch, and the part that runs before it — `qualc`'s per-check
timing, the pytest hooks, the store, the `test-ci` hand-off — is on `main`.

`actionlint` 1.7.12 reports nothing on the three workflow files as they stand with this
patch applied; `git apply --check` accepts it against `main`.

## What it does

- `build` job: `QUALC_RUN_RECORD_DIR: ${{ runner.temp }}/run-records` is set on the
  `Build catalog and static site` step, which is where the `runner` context exists (a
  job-level `env` does not carry it). The record therefore lands outside the checkout,
  and the step right after the job's steps uploads it with `if: always()`,
  `retention-days: 90`, and `if-no-files-found: error` — the build always writes a
  record, so a missing one is a broken run, not a soft warning.
- `run-records` (new job, `needs: qc-ci`, `if: always()`): the test tier runs inside the
  reusable `dzackgarza/ai-review-ci/.github/workflows/_qc.yml`, and a workflow that calls
  another cannot add a step to it. So the repository's own `test-ci` recipe (`justfile`)
  copies a run's records into `.qc-triage/`, which that shared workflow already uploads
  with `if: always()`; this job downloads that artifact and republishes the records under
  a name of their own with 90-day retention. The download has no `continue-on-error`: if
  the tier's artifact is absent the job fails and says so.

`actions/download-artifact` is pinned to `v5.0.0`,
`634f93cb2916e3fdff6788551b99b062d0335ce0`, read from GitHub's tag ref for that
repository; `actions/upload-artifact` reuses the pin already in this workflow.

## What it deliberately does not touch

- `.github/workflows/ambient.yml` — the ambient tier runs `_ambient-semgrep` and
  `_ambient-python-debt` (`dzackgarza/ai-review-ci`, `justfiles/python.just`), no test and
  no `qualc check`, so it writes no record today. It gets no job until it writes one.
- `.github/workflows/corpus-review-crawl.yml` — same reason: it runs `qualc.index`
  subcommands and no test or check, so there is no record for it to upload.

Both files are therefore unchanged, rather than carrying an upload step that could only
pass by warning about nothing.

## What it does not do

It does not change the shared QC workflow, which is not this repository's file. It does
not make a record a gate: nothing reads a record back to pass or fail a check.
