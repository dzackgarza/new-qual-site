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

# Resolve a card ID or path to its current editable corpus path
path-card card:
    @uv run --project {{quote(justfile_directory())}} python -m qualc.authoring path {{quote(card)}}

# Parse one card by ID or path (no cross-card or mathematical review)
check-card card:
    @uv run --project {{quote(justfile_directory())}} python -m qualc.authoring check {{quote(card)}}

# List authored collection appearances in source order, optionally in one section
list-cards collection section="":
    @uv run --project {{quote(justfile_directory())}} python -m qualc.authoring list {{quote(collection)}} {{quote(section)}}

# List collection appearances without solution sections, in authored source order
unsolved-in collection section="":
    @uv run --project {{quote(justfile_directory())}} python -m qualc.authoring unsolved {{quote(collection)}} {{quote(section)}}

# Read a card by ID or path, with its recorded appearances and source resources
read-card card:
    @uv run --project {{quote(justfile_directory())}} python -m qualc.authoring read {{quote(card)}}

# Inspect one card's changes against its last commit, including staged edits
diff-card card:
    @uv run --project {{quote(justfile_directory())}} python -m qualc.authoring diff {{quote(card)}}

# Commit one reviewed prose card without hooks; preserve other staged work
commit-card card message:
    @uv run --project {{quote(justfile_directory())}} python -m qualc.authoring commit {{quote(card)}} {{quote(message)}}

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

# Sample up to n unsolved card IDs and show their appearances in source order
sample-unsolved collection n="5" section="":
    @uv run --project {{quote(justfile_directory())}} python -m qualc.authoring sample {{quote(collection)}} {{quote(n)}} {{quote(section)}}

# Refresh the MathJax macro set from the author's pandoc preamble
macros:
    uv run python tools/sync_macros.py

# Rewrite the unsolved-cards queue from the corpus
unsolved:
    uv run python tools/unsolved_queue.py

# Report problem cards whose statements still contain Unicode mathematics outside LaTeX
extraction-detector:
    uv run python tools/extraction_detector.py

# Reject staged cards that introduce or increase raw extraction mathematics
[private]
_extraction-detector-staged:
    uv run python tools/extraction_detector.py --staged-gate

# Update Queue C from only the staged card diff and stage the generated result.
# `just unsolved` remains the independent full rebuild/oracle. The incremental path
# starts from HEAD's generated queue, removes the old state of changed cards, and
# inserts their staged state, so one-card commits do not reparse the whole corpus.
_unsolved-if-staged:
    #!/usr/bin/env bash
    set -euo pipefail
    if git diff --cached --quiet -- corpus; then
        echo "queues/C-unsolved-cards.md: no staged corpus change"
    else
        uv run python tools/unsolved_queue.py --incremental-staged
        git add queues/C-unsolved-cards.md
    fi

# Fail if any worktree exists (QUAL-09: one checkout, one branch)
#
# Documentation alone did not hold. The rule was written down and the fleet rebuilt
# 27 worktrees anyway, each copying the 353MB tracked assets/ tree, filling the volume
# on 2026-09-10 while holding a megabyte of authored prose between them. This is the
# enforcement: a stream that opens a worktree finds out at its very next commit,
# instead of the volume finding out first.
[private]
_no-worktrees:
    #!/usr/bin/env bash
    set -euo pipefail
    extra=$(git worktree list --porcelain | grep -c '^worktree ' || true)
    if [ "$extra" -gt 1 ]; then
        echo "QUAL-09: $((extra - 1)) worktree(s) exist. Streams work directly on main in this clone." >&2
        git worktree list | tail -n +2 >&2
        echo "Land the work on main, then: git worktree remove <path> && git worktree prune" >&2
        exit 1
    fi

# Reject a commit whose only content is a queue tick
#
# AGENTS.md, "A disposition is not a unit of work": a queue disposition rides in the commit
# carrying the cards it describes. A one-line tick committed alone spends a full gate run to
# move a marker and reports progress the corpus did not make. Real queue filings are large and
# pass; this only catches the bare tick.
[private]
_no-bare-disposition:
    #!/usr/bin/env bash
    set -euo pipefail
    staged=$(git diff --cached --name-only)
    [ -z "$staged" ] && exit 0
    # A collection index marked `completion: complete` with no card touched is the same
    # species as a queue tick — a marker moved, nothing authored. Treat queue files and
    # bare index.md the same way; an index change riding with card work is fine and passes.
    outside=$(printf '%s\n' "$staged" | grep -vE '^queues/|(^|/)index\.md$' || true)
    [ -n "$outside" ] && exit 0
    # Size is the wrong test: a six-line reconciliation note committed alone is still a
    # disposition committed alone. What distinguishes a real queue filing is who writes it —
    # the steward files work into queues with the maintainer noreply address, while a worker
    # commits under the account address and should never be committing queue state by itself.
    author=$(git config user.email)
    case "$author" in
        *users.noreply.github.com) exit 0 ;;
    esac
    echo "Refusing a commit that changes only queue files and collection indexes." >&2
    echo "" >&2
    echo "AGENTS.md, 'A disposition is not a unit of work': a disposition, a reconciliation note" >&2
    echo "or queue tick rides in the commit carrying the cards it describes. Stage the card work" >&2
    echo "alongside it, or leave the queue edit uncommitted until the cards it describes land." >&2
    exit 1

# Run immediate commit-tier quality checks
test-commit: _no-worktrees _unsolved-if-staged _extraction-detector-staged _no-bare-disposition
    @just -f ~/ai-review-ci/justfiles/python.just -d . test-commit

# Run the full project suite before pushing (refreshes BACKLOG.md first)
test-push: backlog
    @just -f ~/ai-review-ci/justfiles/python.just -d . test-push

# Run the CI acceptance gate
test-ci:
    @just -f ~/ai-review-ci/justfiles/python.just -d . test-ci
