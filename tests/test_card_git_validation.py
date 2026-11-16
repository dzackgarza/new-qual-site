"""Local card validation reads the Git content that will be committed or pushed."""

from __future__ import annotations

import json
import shlex
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
CARD = (ROOT / "tests/fixtures/kinds/PRB-INDEXP.md").read_text()
# The fixture card carrying a dated audit event, as every repaired card does.
RECORDED = CARD.replace(
    "\nreview: draft\n",
    "\nreview: draft\n"
    "audit:\n"
    "- event: source-checked\n"
    "  by: claude\n"
    "  date: 2026-11-11\n"
    "  note: The statement matches the printed exercise.\n",
)


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True).stdout


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    git(tmp_path, "init", "-q")
    git(tmp_path, "config", "user.name", "Card validation test")
    git(tmp_path, "config", "user.email", "card-validation@example.invalid")
    git(tmp_path, "config", "commit.gpgsign", "false")
    hooks = tmp_path / ".git" / "hooks"
    git(tmp_path, "config", "core.hooksPath", str(hooks))
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    (corpus / "one card.md").write_text(CARD)
    # Unchanged historical defects are outside the local diff's scope.
    (corpus / "unrelated.md").write_text("---\ntitle: Series: invalid\n---\n")
    git(tmp_path, "add", "corpus")
    git(tmp_path, "commit", "-qm", "initial cards")
    return tmp_path


def check(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, "-m", "qualc.authoring", *args], cwd=root, capture_output=True, text=True)


@pytest.mark.parametrize(
    ("source", "diagnostic"),
    [
        (CARD.replace("title:", "title: Series: ", 1), "mapping values are not allowed"),
        (CARD.replace("review: draft", "review: draft\nreview: verified"), "duplicate key"),
        (CARD.replace("kind: problem", "kind: problem\nunrecognised: value"), "extra_forbidden"),
        (CARD.replace("kind: problem", "kind: unrelated"), "union_tag_invalid"),
        (CARD.replace("review: draft", "review: [draft]"), "literal_error"),
        (CARD.replace("id: PRB-INDEXP\n", ""), "Field required"),
        (CARD.replace(":::\n", "", 1), "unclosed fenced div"),
        (CARD.replace("\n\n::: {.hint}", "\nA trailing line.\n::: {.hint}", 1), "follows text"),
        (CARD + "\nLet $x \\in \\mathbb{R}$.\n", "is written with its semantic macro"),
        (CARD + "\nThen $\\norm{ f } $ is finite.\n", "a $ reached the page as text"),
        (CARD + "\nLet \\(x \\in A\\).\n", "delimits math"),
        (CARD + "\nLet $a \\definedas b$.\n", "is written \\coloneqq"),
        (CARD + "\nThen $|f(z)| \\le 1$.\n", "is written with the semantic macro for its meaning"),
        (CARD + "\nThen $\\left\\| f \\right\\|_2 \\le 1$.\n", "is written with the semantic macro for its meaning"),
        (CARD + "\n\\begin{tikzcd}\n\ta \\\\\n\t& b\n\t\\arrow[from=1-1, to=2-1]\n\\end{tikzcd}\n", "tikzcd compilation produced no SVG"),
    ],
)
def test_staged_header_errors_cannot_be_hidden_by_a_valid_worktree(repo: Path, source: str, diagnostic: str) -> None:
    card = repo / "corpus/one card.md"
    card.write_text(source)
    git(repo, "add", "corpus/one card.md")
    card.write_text(CARD)

    result = check(repo, "check-staged")

    assert result.returncode == 1, result.stdout
    assert "corpus/one card.md" in result.stderr
    assert diagnostic in result.stderr
    assert git(repo, "show", ":corpus/one card.md") == source
    assert card.read_text() == CARD


def test_a_dated_audit_event_is_append_only(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """QUAL-11, issue #147: a dated event is a record, so a correction is a new event.

    The event is dated 2026-11-11 and the commit 2026-11-16. Rewriting the event leaves
    the later events referring to text that is no longer there, which is what four rounds
    of card repairs did on 2026-11-16. An appended event is the sanctioned correction, and
    an event dated the commit's own day is still in flight.
    """
    assert RECORDED != CARD, "the fixture card no longer holds the front matter this test edits"
    card = repo / "corpus/one card.md"
    card.write_text(RECORDED)
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "record a dated event")
    # Git writes this date into the commit the check runs for; pinning it keeps the
    # boundary between the two days independent of when the suite runs.
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")

    card.write_text(RECORDED.replace("matches the printed exercise", "matches the printed statement"))
    git(repo, "add", "corpus/one card.md")
    refused = check(repo, "check-staged")
    assert refused.returncode == 1, refused.stdout
    assert "corpus/one card.md: the source-checked event by claude dated 2026-11-11, whose note begins 'The statement matches the printed exercise.', was changed or deleted" in refused.stderr
    assert "QUAL-11" in refused.stderr

    head = git(repo, "rev-parse", "HEAD")
    hook_free = check(repo, "commit", "corpus/one card.md", "repair the note")
    assert hook_free.returncode == 1, hook_free.stdout
    assert "QUAL-11" in hook_free.stderr
    assert git(repo, "rev-parse", "HEAD") == head

    card.write_text(
        RECORDED.replace(
            "  note: The statement matches the printed exercise.\n",
            "  note: The statement matches the printed exercise.\n"
            "- event: solution-reviewed\n"
            "  by: claude\n"
            "  date: 2026-11-16\n"
            "  note: The solution follows the source's argument.\n",
        )
    )
    git(repo, "add", "corpus/one card.md")
    accepted = check(repo, "check-staged")
    assert accepted.returncode == 0, accepted.stderr
    assert "1 changed file(s) checked" in accepted.stdout

    same_day = RECORDED.replace("date: 2026-11-11", "date: 2026-11-16")
    card.write_text(same_day)
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "record the day's own event")
    card.write_text(same_day.replace("matches the printed exercise", "matches the printed statement"))
    git(repo, "add", "corpus/one card.md")
    in_flight = check(repo, "check-staged")
    assert in_flight.returncode == 0, in_flight.stderr


def test_staged_validation_ignores_unstaged_edits_and_unrelated_cards(repo: Path) -> None:
    card = repo / "corpus/one card.md"
    staged = CARD + "\nAn authored remark.\n"
    card.write_text(staged)
    git(repo, "add", "corpus/one card.md")
    card.write_text(CARD.replace("title:", "title: Series: ", 1))

    result = check(repo, "check-staged")

    assert result.returncode == 0, result.stderr
    assert "1 changed file(s) checked" in result.stdout
    assert git(repo, "show", ":corpus/one card.md") == staged


def test_semantic_bar_macros_and_array_column_rules_pass(repo: Path) -> None:
    card = repo / "corpus/one card.md"
    card.write_text(CARD + "\nThen $\\abs{f} \\le \\norm{g}_2$ on $\\{x \\st x \\divides 6\\}$ and $\\begin{array}{c|c} a & b \\end{array}$, with `a|b` and a | b outside mathematics.\n")
    git(repo, "add", "corpus/one card.md")

    result = check(repo, "check-staged")

    assert result.returncode == 0, result.stderr


def test_outgoing_validation_reads_committed_cards_and_accepts_repairs(repo: Path) -> None:
    base = git(repo, "rev-parse", "HEAD").strip()
    card = repo / "corpus/one card.md"
    card.write_text(CARD.replace("title:", "title: Series: ", 1))
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "hook-free content")
    card.write_text(CARD)
    git(repo, "add", "corpus/one card.md")

    result = check(repo, "check-range", base)

    assert result.returncode == 1
    assert "corpus/one card.md" in result.stderr
    assert "mapping values are not allowed" in result.stderr
    git(repo, "commit", "-qm", "repair title")
    accepted = check(repo, "check-range", base)
    assert accepted.returncode == 0, accepted.stderr


def test_added_renamed_and_deleted_cards_follow_the_outgoing_tree(repo: Path) -> None:
    base = git(repo, "rev-parse", "HEAD").strip()
    renamed = repo / "corpus/renamed card.md"
    (repo / "corpus/one card.md").rename(renamed)
    added = repo / "corpus/added card.md"
    added.write_text(CARD.replace("PRB-INDEXP", "P-ADDED"))
    # Git records deletion without interpreting the deleted malformed card.
    (repo / "corpus/unrelated.md").rename(repo / "retired.txt")
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "update card paths")
    result = check(repo, "check-range", base)
    assert result.returncode == 0, result.stderr
    assert "2 changed file(s) checked" in result.stdout
    renamed.write_text(CARD.replace("title:", "title: Series: ", 1))
    git(repo, "add", "corpus/renamed card.md")
    git(repo, "commit", "-qm", "invalid renamed card")
    rejected = check(repo, "check-range", base)
    assert rejected.returncode == 1
    assert "corpus/renamed card.md" in rejected.stderr


def test_pathspec_commit_validates_its_temporary_index(repo: Path) -> None:
    hook = repo / ".git/hooks/pre-commit"
    hook.write_text(f"#!/bin/sh\nexec {shlex.quote(sys.executable)} -m qualc.authoring check-staged\n")
    hook.chmod(0o755)
    other = repo / "corpus/other.md"
    other.write_text(CARD.replace("title:", "title: Series: ", 1))
    git(repo, "add", "corpus/other.md")
    staged_before = git(repo, "diff", "--cached")
    target = repo / "corpus/one card.md"
    target.write_text(CARD + "\nA reviewed remark.\n")

    git(repo, "commit", "--only", "-qm", "review card", "--", "corpus/one card.md")

    assert git(repo, "show", "HEAD:corpus/one card.md") == target.read_text()
    assert git(repo, "diff", "--cached") == staged_before
    head = git(repo, "rev-parse", "HEAD")
    target.write_text(CARD.replace("title:", "title: Series: ", 1))
    result = subprocess.run(["git", "commit", "--only", "-qm", "invalid card", "--", "corpus/one card.md"], cwd=repo, capture_output=True, text=True)
    assert result.returncode != 0
    assert "corpus/one card.md" in result.stderr
    assert git(repo, "rev-parse", "HEAD") == head
    assert git(repo, "diff", "--cached") == staged_before


def test_shared_push_payload_validates_each_exact_candidate_commit(repo: Path) -> None:
    valid = git(repo, "rev-parse", "HEAD").strip()
    card = repo / "corpus/one card.md"
    card.write_text(CARD.replace("title:", "title: Series: ", 1))
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "invalid candidate")
    invalid = git(repo, "rev-parse", "HEAD").strip()
    card.write_text(CARD)
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "valid HEAD")
    payload = "\n".join(json.dumps({"path": "corpus/one card.md", "version": commit}) for commit in (valid, invalid))

    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts/local-validate.py"), "--mode", "push"],
        cwd=repo,
        input=payload,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert "corpus/one card.md" in result.stderr
    assert "mapping values are not allowed" in result.stderr


def test_push_rejects_a_deleted_card_that_is_still_referenced(repo: Path) -> None:
    collection = (ROOT / "tests/fixtures/kinds/SRC-HW.md").read_text().replace("    term: spring\n", "    term: spring\n  problems:\n  - P-GONE\n")
    (repo / "corpus/P-GONE.md").write_text(CARD.replace("PRB-INDEXP", "P-GONE"))
    (repo / "corpus/SRC-HW.md").write_text(collection)
    (repo / "wiki").mkdir()
    (repo / "wiki/groups.md").write_text("---\ntitle: Groups\norder: 1\n---\n\nSee [[P-GONE]] and [[groups]].\n")
    (repo / "publications").mkdir()
    (repo / "publications/guide.yaml").write_text(
        "schema: qual/publication@2\nid: GUIDE-ALGEBRA\nkind: study-guide\ntitle: Algebra\nlede: Groups.\nsections:\n"
        "  - slug: groups\n    title: Groups\n    parent: GUIDE-ALGEBRA\n    lede: Groups.\n    items:\n      - ref: P-GONE\n"
    )
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "reference the card")

    def push() -> subprocess.CompletedProcess[str]:
        # A deletion-only range gives the shared hook no changed card to send.
        return subprocess.run([sys.executable, str(ROOT / "scripts/local-validate.py"), "--mode", "push"], cwd=repo, input="", capture_output=True, text=True)

    assert push().returncode == 0
    git(repo, "rm", "-q", "corpus/P-GONE.md")
    git(repo, "commit", "-qm", "merge the card away")

    result = push()

    assert result.returncode == 1
    for referrer in ("corpus/SRC-HW.md", "wiki/groups.md", "publications/guide.yaml"):
        assert f"{referrer}: " in result.stderr
    assert result.stderr.count("'P-GONE'") == 3
