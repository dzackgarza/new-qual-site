# Issue #145 — the workflow half, as a patch

`issue145-workflows.patch` is a `git apply`-able diff for the files a push from this
connection cannot carry (workflow files). Apply it from the repository root:

```sh
git apply results/issue145-workflows.patch
```

## Files it touches

- `.github/workflows/development.yml`
- `.github/workflows/ambient.yml`
- `.github/workflows/corpus-review-crawl.yml`

Nothing outside `.github/workflows/` is in the patch. The part that runs before it —
`qualc`'s per-check timing, the pytest hooks, the store — is on `main`.

## What it does

Each workflow uploads that run's duration records as an artifact with `if: always()`
and `retention-days: 90`.

- `development.yml`
  - `build`: sets `QUALC_RUN_RECORD_DIR=${{ runner.temp }}/run-records`, so the record of
    `uv run qualc build` lands outside the checkout, and uploads it after the build steps
    with `if: always()`.
  - `run-records` (new job): the test tier runs inside the reusable
    `dzackgarza/ai-review-ci/.github/workflows/_qc.yml`, and a workflow that calls another
    cannot add a step to it. So the repository's own `test-ci` recipe (`justfile`) copies a
    run's records into `.qc-triage/`, which that shared workflow already uploads with
    `if: always()`; this job collects that artifact and republishes just the records under
    a name of their own with 90-day retention.
- `ambient.yml`: the same `run-records` job for the scheduled audit tier. The ambient tier
  runs no test and no `qualc check` today, so the artifact is empty (`if-no-files-found:
  warn`) until it does.
- `corpus-review-crawl.yml`: sets the record directory and adds the upload step to `review`.
  That workflow runs neither the suite nor `qualc check` today, so the step uploads nothing
  yet; it is there so that a run of either reaches an artifact without anyone remembering
  to add the step.

`actions/download-artifact` is pinned to `v5.0.0`, `634f93cb2916e3fdff6788551b99b062d0335ce0`,
read from GitHub's tag ref for that repository; `actions/upload-artifact` reuses the pin
already in these workflows.

## What it does not do

It does not change the shared QC workflow, which is not this repository's file. It does not
make a record a gate: nothing reads a record back to pass or fail a check.
