# ai-review-ci contract variables consumed by doctor and workflow installers.
ai_review_ci_schema_version := "1"
ai_review_ci_profile := "python"
ai_review_ci_ref := "main"
ai_review_ci_release_channel := "main"
ai_review_ci_workflow_template_version := "1"
ai_review_ci_local_delegation := "global-justfile"
ai_review_ci_default_branch := "main"

# List available recipes
default:
    @just --list

# Validate every card against the schema and the registries
check:
    uv run qualc check

# Compile the corpus: catalog.sqlite + QMD and static HTML projections
build:
    uv run qualc build

# Build and render the site to build/quarto/_site
site: build

# Serve the compiled site
preview port="8000": build
    uv run python -m http.server {{ port }} --directory build/quarto/_site

# Prove the architectural invariants hold
test:
    uv run --group dev pytest -q

# Query the catalog directly (e.g. just query "select id, title from cards limit 5")
query sql: build
    @sqlite3 -box build/catalog.sqlite {{ quote(sql) }}

# Reconcile every pinned make-me-a-qual row (additive; legacy generated imports stay until audited)
import:
    uv run python tools/import_mmaq.py --root .

# Refresh the MathJax macro set from pandoc-config
macros:
    uv run python tools/sync_macros.py

# Run immediate commit-tier quality checks
test-commit:
    @just -f ~/ai-review-ci/justfiles/python.just -d . test-commit

# Run the full project suite before pushing
test-push:
    @just -f ~/ai-review-ci/justfiles/python.just -d . test-push

# Run the CI acceptance gate
test-ci:
    @just -f ~/ai-review-ci/justfiles/python.just -d . test-ci
