# #122: the site builds and the tier runs inside the research image

`development-container.patch` applies to `c5efcc703e`, the commit that restored
the push-triggered workflow of before `2d25da7c3f`. Land with
`git apply results/development-container.patch`, which passes `git apply --check`
against that tree and leaves the job's triggers and concurrency untouched, so it
does not re-open the question of when a publish runs — only of where it runs.

## What it changes

- `build` and `reports` run in `container: image: ghcr.io/dzackgarza/sage:develop`
  and stop installing TeX Live, uv, just and pdf2svg, which is the claim issue
  #122 makes about them. Their remaining steps stay as they are: checkout with
  full history, the pandoc-config clone, `uv sync --frozen`, the build, the
  crawl, the revision stamp and the artifact uploads. It does not touch the
  triggers or the concurrency groups: `c5efcc703e` restored the push-triggered
  shape, and this patch changes where the job runs, not when.
- `qc-ci` passes `profile: sage` instead of `profile: python`. `_qc.yml:298`
  puts the test tier in the image only on
  `inputs.profile == 'sage' && inputs.tier == 'test-ci'`; a caller cannot choose
  a container for a reusable workflow any other way. `setup_recipe` becomes
  `_ci-setup-image`, and `setup_cache_paths: ~/texlive` goes with the TeX Live
  install it used to cache.
- The `justfile` gains `_ci-setup-image`, which inside the image does the one
  thing the image lacks for this build: it clones the author's pandoc-config to
  `~/.pandoc`, where the emitter reads `filters/tikzcd.lua` and the macro mirror
  reads `styles/dzg-macros.sty`. `_ci-setup` stays for a bare runner.
- `tests/test_pages_workflow.py` moves with the workflow. It pinned the
  `qc-ci` inputs as a whole mapping, so it is part of this change, not a
  casualty of it: it now pins `profile: sage` and `_ci-setup-image`, asserts the
  image on both containerised jobs, and asserts that neither job reaches for
  `setup-texlive`, `setup-uv`, `setup-just` or `apt-get install`.

## What was checked before writing it

- `check-profile --profile sage` (`gates.py:173`) requires `pyproject.toml` and
  at least one `.sage` file. Both hold: `proofs/cards/DeltaComplexHomology.sage`
  and `proofs/cards/V49FiveSquaresTuples.sage` are tracked. `sage.just` is in
  the profile's `justfile_names`, which `check_profile` does not test.
- The image pulls anonymously: a ghcr token for `repository:dzackgarza/sage:pull`
  is issued, and `GET /v2/dzackgarza/sage/manifests/develop` answers `200`. No
  `credentials:` is needed.
- The image carries what the jobs stop installing: `uv`, `just` (both
  `/usr/local/bin`), `pdf2svg`, `lualatex`, `pdflatex`, `git`, `pandoc`, `node`
  (`/usr/bin`), read from the extracted rootfs at image revision `6301b4e4`.
  Its env sets `SAGE_BIN=/sage/.venv/bin/sage`, which the `sage` profile asserts.
- `rg` is *not* in the image and does not need to be: `_qc.yml`'s own "Install
  QC system packages" step installs `ripgrep`, `pandoc` and `unzip` inside
  whatever container the job runs in.
- JS actions in that container are the established pattern: `_qc.yml` itself
  runs `actions/checkout` and `actions/upload-artifact` under the same `container:`.
- The patch applies with `git apply --check` to a clean `2d25da7c3f` tree, and
  `results/queue-d-workflows.patch`, still pending, passes `git apply --check`
  on top of it (its hunk lands at offset -8 and finds its context).
- The patched `tests/test_pages_workflow.py` passes against the patched
  workflow and fails against the current one, so the pair moves together
  rather than being kept green by a loosened assertion.
- `just --show _ci-setup-image` parses the new recipe, and the patched workflow
  loads as YAML with `push`, `workflow_dispatch` and the `7,37 * * * *`
  schedule intact.

## What is not verified here

Nothing in this checkout can run GitHub Actions, so these are the first run's
questions, not claims:

- whether `uv sync --frozen` resolves against the image's `/opt/uv-python`
  CPython 3.14 without downloading one, and whether that directory is writable
  to the container user;
- whether the container user can write the mounted workspace (checkout and
  `uv sync` both need to);
- whether the `sage` profile's `uv pip install --editable` into `/sage/.venv`
  is permitted to that user.

`ai_review_ci_profile` in the `justfile` stays `"python"` on purpose: the local
hooks delegate to `python.just`, and changing it would point them at a
`sage.just` this repository does not have. It is not what puts the tier in the
image; `profile:` in `development.yml` is.
