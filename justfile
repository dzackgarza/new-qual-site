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

# Serve the compiled site the way GitHub Pages serves it, 404.html included
preview port="8000": build
    uv run python tools/preview.py {{ port }}

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

# Print n random unsolved problem/exercise cards: no solution section and no incoming solves relation
sample-unsolved n="5": build
    @sqlite3 -box build/catalog.sqlite "select id from cards where kind in ('problem', 'exercise') and id not in (select card_id from sections where section_kind = 'solution') and id not in (select target_id from relations where kind = 'solves') order by random() limit {{ n }}"

# Refresh the MathJax macro set from the author's pandoc preamble
macros:
    uv run python tools/sync_macros.py

# Rewrite the unsolved-cards queue from the corpus
unsolved:
    uv run python tools/unsolved_queue.py

# Rewrite the queue when the commit touches the corpus, and stage the result so
# the refresh lands in that commit rather than trailing it. The corpus is the
# only input that can change the queue, and parsing it costs ~25s, so a commit
# that touches nothing else is not made to pay for it.
_unsolved-if-staged:
    #!/usr/bin/env bash
    set -euo pipefail
    if git diff --cached --quiet -- corpus; then
        echo "queues/C-unsolved-cards.md: no staged corpus change"
    else
        uv run python tools/unsolved_queue.py
        git add queues/C-unsolved-cards.md
    fi

# Run immediate commit-tier quality checks
test-commit: _unsolved-if-staged
    @just -f ~/ai-review-ci/justfiles/python.just -d . test-commit

# Run the full project suite before pushing (refreshes BACKLOG.md first)
test-push: backlog
    @just -f ~/ai-review-ci/justfiles/python.just -d . test-push

# Run the CI acceptance gate
test-ci:
    @just -f ~/ai-review-ci/justfiles/python.just -d . test-ci
