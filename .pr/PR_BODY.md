Refs #17

## Observed production failure

The main-only Pages workflow for merge commit `d6aa9713` failed before corpus parsing:

<https://github.com/dzackgarza/new-qual-site/actions/runs/30200698902>

```text
FileNotFoundError: [Errno 2] No such file or directory: 'pandoc'
```

Checkout, `setup-uv`, and `uv sync --frozen` succeeded. The first
`PandocServer` subprocess could not start because the workflow did not provision
the repository's non-Python build dependency.

## Claim map

- [x] Provision Pandoc through an existing setup action that downloads the requested
  release and adds it to `PATH`.
  - Contract:
    <https://github.com/r-lib/actions/tree/d3c5be51b12e724e68f33216ca3c148b66d5f0b6/setup-pandoc>
- [x] Pin the action by immutable SHA.
  - `r-lib/actions/setup-pandoc@d3c5be51b12e724e68f33216ca3c148b66d5f0b6`
- [x] Pin Pandoc to the exact measured local build version.
  - `3.6.1`, with the required `+server` feature
- [x] Preserve the hard missing-dependency failure.
  - No fallback, optional path, generated default, or runtime shim is added.
- [x] Keep the workflow syntactically and semantically valid.
  - The edited workflow round-trips through `ruamel.yaml` byte-for-byte.
  - The repository commit gate and 47-test push gate pass.

## Post-merge production proof

The Pages workflow runs only on `main`. After merge, verify that both its build
and deploy jobs succeed for the merge commit, then fetch and browser-inspect the
live finite-groups traversal before treating the deployment as delivered.
