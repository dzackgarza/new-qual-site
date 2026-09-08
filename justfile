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

# Parse one card and validate its schema (no cross-card or mathematical review)
check-card path:
    @uv run python -c \
        'import sys; from pathlib import Path; from qualc.model import parse_card; card = parse_card(Path(sys.argv[1])); print(f"{card.card.id}: schema and Markdown parsing OK (single card)")' \
        {{quote(path)}}

# List live cards without solution sections in one corpus directory (TSV)
unsolved-in directory:
    @uv run --project {{quote(justfile_directory())}} python -m qualc.authoring unsolved {{quote(directory)}}

# Read the complete authored card or collection, without parsing or rebuilding
read-card path:
    @cat -- {{quote(path)}}

# Inspect one card's changes against its last commit, including staged edits
diff-card path:
    @git --literal-pathspecs diff HEAD -- {{quote(path)}}

# Commit one reviewed prose card without hooks; preserve other staged work
commit-card path message:
    #!/usr/bin/env bash
    set -euo pipefail
    card_path=$(realpath --relative-to="$(git rev-parse --show-toplevel)" -- {{quote(path)}})
    case "$card_path" in
        corpus/*.md) ;;
        *) echo "commit-card requires a Markdown card under corpus/" >&2; exit 1 ;;
    esac
    test -f "$card_path"
    git --literal-pathspecs ls-files --error-unmatch -- "$card_path"
    git --literal-pathspecs commit --only --no-verify -m {{quote(message)}} -- "$card_path"

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

# Report pages the home page cannot reach, and links to pages that are not there
crawl: build
    uv run python tools/crawl.py

# Serve the compiled site the way GitHub Pages serves it, 404.html included
preview port="8000": build
    uv run python tools/preview.py {{ port }}

# Prove the architectural invariants hold
test:
    uv run --group dev pytest -q

# Query the catalog directly (e.g. just query "select id, title from cards limit 5")
query sql: build
    @sqlite3 -box build/catalog.sqlite {{ quote(sql) }}

# Lint prose for handwaving and weak reasoning (pass files, or defaults to corpus)
vale *args:
    vale --config .vale.ini {{ if args == '' { 'corpus/problems/**/*.md corpus/collections/**/*.md' } else { args } }}

# Report problem/exercise cards missing metadata (title, areas, topics, body)
complete *args:
    uv run python -m qualc.card_completeness {{ args }}

# Regenerate BACKLOG.md unless already current for HEAD (runs before every push)
backlog:
    uv run python tools/backlog.py

# Sample up to n live cards without solution sections in one corpus directory
sample-unsolved directory n="5":
    @uv run --project {{quote(justfile_directory())}} python -m qualc.authoring sample {{quote(directory)}} {{quote(n)}}

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
