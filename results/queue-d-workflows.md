# Queue D — the workflow half, as a patch

`queue-d-workflows.patch` is a `git apply`-able diff for the one file a push from this
connection cannot carry (a workflow file). Apply it from the repository root:

```sh
git apply results/queue-d-workflows.patch
```

## Files it touches

- `.github/workflows/development.yml`

Nothing else. Everything that runs before it — `tools/qualc/prose.py`, `just prose-only`,
`just backlog --with-queues`, the `prose-only-solutions` section of the report — is on
`main`.

## What it does

It adds `queues/D-prose-only-solutions.md` to the `corpus-reports` job's
`actions/upload-artifact` path list, beside `queues/C-unsolved-cards.md`, so the
per-card list ships in the same artifact as the count that names it. `_reports-ci`
already writes the file (`tools/backlog.py --with-queues`), and `BACKLOG.md` — already
in that list — carries the count itself.

## What it deliberately does not touch

The job's steps, its triggers, its permissions and the other two workflow files. The
queue is written by the same recipe the report already runs; only the upload path grows.

## What it does not do

It does not make the count a gate. Queue D is a measurement, and nothing reads it back to
pass or fail a check.
