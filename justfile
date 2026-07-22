quarto := "uvx --from quarto-cli quarto"

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

# Compile the corpus: catalog.sqlite + generated Quarto project
build:
    uv run qualc build

# Build and render the site to build/quarto/_site
site: build
    {{quarto}} render build/quarto

# Serve the site with live reload
preview: build
    {{quarto}} preview build/quarto

# Prove the architectural invariants hold
test:
    uv run --group dev pytest -q

# Query the catalog directly (e.g. just query "select id, title from cards limit 5")
query sql: build
    @sqlite3 -box build/catalog.sqlite {{quote(sql)}}

# Re-seed the corpus from make-me-a-qual (one-shot; overwrites imports/ and canonical/)
import:
    uv run python tools/import_mmaq.py

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
