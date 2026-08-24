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

# Report wiki filesystem measurements as candidates to read (not a gate)
doctor *args:
    uv run python tools/wiki_doctor.py {{ args }}

# List collections with empty provenance, unresolved hrefs, shared hrefs, markdown hrefs, image hrefs, forbidden hrefs, and collection areas with no problem cards (not a gate)
provenance *args:
    uv run python -m qualc.provenance_hrefs {{ args }}

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

# Report problem/exercise cards missing metadata (title, areas, topics, body)
complete *args:
    uv run python -m qualc.card_completeness {{ args }}

# Regenerate BACKLOG.md unless already current for HEAD (runs before every push)
backlog:
    uv run python tools/backlog.py

# Print n random unsolved problem/exercise cards (frontmatter solved: false)
sample-unsolved n="5":
    @rg --files-with-matches '^solved: false$' corpus | shuf -n {{ n }}

# Refresh the MathJax macro set from the author's pandoc preamble
macros:
    uv run python tools/sync_macros.py

# Run immediate commit-tier quality checks
test-commit:
    @just -f ~/ai-review-ci/justfiles/python.just -d . test-commit

# Run the full project suite before pushing (refreshes BACKLOG.md first)
test-push: backlog
    @just -f ~/ai-review-ci/justfiles/python.just -d . test-push

# Run the CI acceptance gate
test-ci:
    @just -f ~/ai-review-ci/justfiles/python.just -d . test-ci
