"""Local card validation reads the Git content that will be committed or pushed."""

from __future__ import annotations

import json
import re
import shlex
import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

from qualc.authoring import commit_day, previous_source

ROOT = Path(__file__).resolve().parent.parent
CARD = (ROOT / "tests/fixtures/kinds/PRB-INDEXP.md").read_text()


def recorded(day: str) -> str:
    """The fixture card carrying one dated audit event."""
    return CARD.replace(
        "\nreview: draft\n",
        "\nreview: draft\n"
        "audit:\n"
        "- event: source-checked\n"
        "  by: claude\n"
        f"  date: {day}\n"
        "  note: The statement matches the printed exercise.\n",
    )


RECORDED = recorded("2026-11-11")
# A root-level complaints file in the stated record format: a dated section, and a
# dated paragraph inside an undated entry.
COMPLAINTS = """# Mathematical issues and papercuts

## Recording an issue

Add a descriptive heading with the observed evidence.

## Open findings

### A search entry

**Searched outside the retained sets (2026-11-10).** The observation.

*Further note, 2026-11-12: an appended paragraph.*

## 2026-11-09: an older section

Another observation.
"""


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True).stdout


def staged_records(root: Path) -> str:
    """The payload the shared staged hook sends: every staged path at the index."""
    names = git(root, "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z")
    return "".join(json.dumps({"path": path, "version": "index"}) + "\n" for path in names.split("\0") if path)


def run_staged(root: Path) -> subprocess.CompletedProcess[str]:
    """The project's staged validator, fed as the shared hook feeds it."""
    return subprocess.run([sys.executable, str(ROOT / "scripts/local-validate.py"), "--mode", "staged"], cwd=root, input=staged_records(root), capture_output=True, text=True)


def run_push(root: Path, tip: str, *paths: str) -> subprocess.CompletedProcess[str]:
    """The project's push validator, fed as the shared hook feeds it: the pushed tip."""
    payload = "".join(json.dumps({"path": path, "version": tip}) + "\n" for path in paths)
    return subprocess.run([sys.executable, str(ROOT / "scripts/local-validate.py"), "--mode", "push"], cwd=root, input=payload, capture_output=True, text=True)


def track(root: Path, commit: str) -> None:
    """Give the current branch the upstream the push gate reads, at `commit`.

    The remote's URL is never contacted; it supplies the fetch refspec that maps the
    merge ref to the remote-tracking ref.
    """
    branch = git(root, "symbolic-ref", "--short", "HEAD").strip()
    git(root, "remote", "add", "omm", "https://example.invalid/new-qual-site.git")
    git(root, "config", f"branch.{branch}.remote", "omm")
    git(root, "config", f"branch.{branch}.merge", "refs/heads/main")
    git(root, "update-ref", "refs/remotes/omm/main", commit)


def install_gate(root: Path) -> None:
    """The staged chain: the hook builds the shared payload and runs the project validator."""
    runner = root / ".git" / "hooks" / "staged-gate.py"
    runner.write_text(
        "import json, subprocess, sys\n"
        "names = subprocess.run(['git', 'diff', '--cached', '--name-only', '--diff-filter=ACMR', '-z'], check=True, stdout=subprocess.PIPE).stdout.decode()\n"
        "records = ''.join(json.dumps({'path': path, 'version': 'index'}) + '\\n' for path in names.split('\\0') if path)\n"
        f"raise SystemExit(subprocess.run([sys.executable, {str(ROOT / 'scripts/local-validate.py')!r}, '--mode', 'staged'], input=records.encode()).returncode)\n"
    )
    hook = root / ".git" / "hooks" / "pre-commit"
    hook.write_text(f"#!/bin/sh\nexec {shlex.quote(sys.executable)} {shlex.quote(str(runner))}\n")
    hook.chmod(0o755)


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
    """QUAL-11, issue #147: a commit that rewrites a dated event is refused by the hook.

    The event is dated 2026-11-11 and the commit 2026-11-16, so the event is a record a
    later session may quote. An appended event is the sanctioned correction, and an event
    dated the commit's own day is still in flight.
    """
    assert RECORDED != CARD, "the fixture card no longer holds the front matter this test edits"
    card = repo / "corpus/one card.md"
    card.write_text(RECORDED)
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "record a dated event")
    install_gate(repo)
    # Git writes this date into the commit the hook validates; pinning it keeps the
    # boundary between the two days independent of when the suite runs.
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")

    recorded = git(repo, "rev-parse", "HEAD")
    card.write_text(RECORDED.replace("matches the printed exercise", "matches the printed statement"))
    git(repo, "add", "corpus/one card.md")
    refused = subprocess.run(["git", "commit", "-qm", "repair the note"], cwd=repo, capture_output=True, text=True)
    assert refused.returncode != 0, refused.stdout
    assert "corpus/one card.md: the source-checked event by claude dated 2026-11-11, whose note begins 'The statement matches the printed exercise.', was changed or deleted" in refused.stderr
    assert "QUAL-11" in refused.stderr
    assert git(repo, "rev-parse", "HEAD") == recorded

    appended = RECORDED.replace(
        "  note: The statement matches the printed exercise.\n",
        "  note: The statement matches the printed exercise.\n"
        "- event: solution-reviewed\n"
        "  by: claude\n"
        "  date: 2026-11-16\n"
        "  note: The solution follows the source's argument.\n",
    )
    card.write_text(appended)
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "append the correction")
    assert git(repo, "rev-parse", "HEAD") != recorded
    assert "- event: solution-reviewed" in git(repo, "show", "HEAD:corpus/one card.md")

    in_flight = appended.replace("follows the source's argument.", "follows the source's argument, checked twice.")
    card.write_text(in_flight)
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "refine the day's own event")
    assert git(repo, "show", "HEAD:corpus/one card.md") == in_flight


def test_a_dated_event_restored_to_its_earlier_text_is_accepted(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """QUAL-11 restores what it protects: the text an event carried on its own day.

    The repository's own historical commits rewrote dated events in place, and the
    correction QUAL-11 asks for is the event as it stood. An event restored to the
    text it carried on its day is that correction, not a rewrite of it, and the gate
    has to tell the two apart: the text it is restoring no longer stands in the text
    the rewrite left, so comparing against that text alone refuses the repair.
    """
    card = repo / "corpus/one card.md"
    card.write_text(RECORDED)
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-11T09:00:00 +0000")
    git(repo, "commit", "-qm", "record the event on its day")

    rewritten = RECORDED.replace("matches the printed exercise", "matches the printed statement")
    card.write_text(rewritten)
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-14T09:00:00 +0000")
    git(repo, "commit", "-qm", "rewrite the record in place")

    card.write_text(RECORDED)
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")

    result = check(repo, "check-staged")

    assert result.returncode == 0, result.stderr
    assert git(repo, "show", ":corpus/one card.md") == RECORDED


def test_a_dated_event_with_new_text_is_still_refused(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """The restoration rule admits only text that stood in an earlier revision.

    Text a session writes today belongs to a new event, so a dated event may not take
    it, and the gate still refuses the rewrite it was built to refuse.
    """
    card = repo / "corpus/one card.md"
    card.write_text(RECORDED)
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-11T09:00:00 +0000")
    git(repo, "commit", "-qm", "record the event on its day")

    card.write_text(RECORDED.replace("matches the printed exercise", "matches the printed statement"))
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")

    result = check(repo, "check-staged")

    assert result.returncode == 1, result.stdout
    assert "the source-checked event by claude dated 2026-11-11" in result.stderr
    assert "QUAL-11" in result.stderr


def test_a_dated_complaints_record_restored_to_its_earlier_text_is_accepted(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """The COMPLAINTS records are held to the same rule, and take the same repair."""
    path = repo / "COMPLAINTS.md"
    path.write_text(COMPLAINTS)
    git(repo, "add", "COMPLAINTS.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-10T09:00:00 +0000")
    git(repo, "commit", "-qm", "record the finding on its day")

    path.write_text(COMPLAINTS.replace("The observation.", "The corrected observation."))
    git(repo, "add", "COMPLAINTS.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-14T09:00:00 +0000")
    git(repo, "commit", "-qm", "rewrite the record in place")

    path.write_text(COMPLAINTS)
    git(repo, "add", "COMPLAINTS.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")

    result = check(repo, "check-staged")

    assert result.returncode == 0, result.stderr
    assert git(repo, "show", ":COMPLAINTS.md") == COMPLAINTS


def test_a_dated_event_may_quote_the_symbols_of_its_day(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """STYLE-04 governs authored prose, and a dated event is not authored now.

    An event records a symbol as the session of its day wrote it, and QUAL-11 forbids
    rewriting it; a style rule applied to it would demand exactly that rewrite. The
    card's body is authored prose and is still held to the rule.
    """
    barred = RECORDED.replace(
        "The statement matches the printed exercise.",
        "The local group is $H_n(M|x;R)$, Hatcher's notation on printed p. 234.",
    )
    card = repo / "corpus/one card.md"
    card.write_text(barred)
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")

    accepted = check(repo, "check-staged")
    assert accepted.returncode == 0, accepted.stderr

    card.write_text(barred + "\nThen $|x| \\le 1$.\n")
    git(repo, "add", "corpus/one card.md")
    refused = check(repo, "check-staged")
    assert refused.returncode == 1, refused.stdout
    assert "is written with the semantic macro for its meaning" in refused.stderr


def test_a_dated_complaints_record_is_append_only(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Issue #147: a dated COMPLAINTS record is a record, so a correction is a new record.

    The record is the paragraph whose lead states the day, and the section whose heading
    states it; an undated entry around them does not shield either.
    """
    path = repo / "COMPLAINTS.md"
    path.write_text(COMPLAINTS)
    git(repo, "add", "COMPLAINTS.md")
    git(repo, "commit", "-qm", "record findings")
    install_gate(repo)
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")
    recorded = git(repo, "rev-parse", "HEAD")

    path.write_text(COMPLAINTS.replace("The observation.", "The corrected observation."))
    git(repo, "add", "COMPLAINTS.md")
    refused = subprocess.run(["git", "commit", "-qm", "rewrite the record"], cwd=repo, capture_output=True, text=True)
    assert refused.returncode != 0, refused.stdout
    assert "COMPLAINTS.md: the record dated 2026-11-10" in refused.stderr
    assert "QUAL-11" in refused.stderr
    assert git(repo, "rev-parse", "HEAD") == recorded

    removed = COMPLAINTS.replace("**Searched outside the retained sets (2026-11-10).** The observation.\n\n", "")
    path.write_text(removed)
    git(repo, "add", "COMPLAINTS.md")
    refused = subprocess.run(["git", "commit", "-qm", "remove the record"], cwd=repo, capture_output=True, text=True)
    assert refused.returncode != 0, refused.stdout
    assert "COMPLAINTS.md: the record dated 2026-11-10" in refused.stderr

    section = COMPLAINTS.replace("## 2026-11-09: an older section\n\nAnother observation.\n", "## 2026-11-09: an older section\n\nA different observation.\n")
    path.write_text(section)
    git(repo, "add", "COMPLAINTS.md")
    refused = subprocess.run(["git", "commit", "-qm", "rewrite the section"], cwd=repo, capture_output=True, text=True)
    assert refused.returncode != 0, refused.stdout
    assert "COMPLAINTS.md: the record dated 2026-11-09" in refused.stderr

    later = COMPLAINTS + "\n## 2026-11-16: a correction\n\nThe record stands.\n"
    path.write_text(later)
    git(repo, "add", "COMPLAINTS.md")
    git(repo, "commit", "-qm", "append the record")
    assert git(repo, "rev-parse", "HEAD") != recorded

    in_flight = later.replace("The record stands.", "The record stands, checked twice.")
    path.write_text(in_flight)
    git(repo, "add", "COMPLAINTS.md")
    git(repo, "commit", "-qm", "refine the day's own record")
    assert git(repo, "show", "HEAD:COMPLAINTS.md") == in_flight


def test_every_dated_complaints_heading_states_its_day_first() -> None:
    """The file's stated record format: a dated section begins with its own day."""
    day = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
    for line in (ROOT / "COMPLAINTS.md").read_text().splitlines():
        if line.startswith("#") and day.search(line) and not re.match(r"^#{1,6} \d{4}-\d{2}-\d{2}:", line):
            pytest.fail(f"a dated heading does not begin with its day: {line}")


def test_a_renamed_card_keeps_the_audit_text_of_its_earlier_path(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A card's earlier text follows the path Git records as the source of the move."""
    card = repo / "corpus/one card.md"
    card.write_text(RECORDED)
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "record a dated event")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")

    git(repo, "mv", "corpus/one card.md", "corpus/renamed card.md")
    moved = check(repo, "check-staged")
    assert moved.returncode == 0, moved.stderr
    git(repo, "commit", "-qm", "move the card")

    final = repo / "corpus/moved card.md"
    final.write_text(RECORDED.replace("matches the printed exercise", "matches the printed statement"))
    (repo / "corpus/renamed card.md").unlink()
    git(repo, "add", "-A")
    refused = check(repo, "check-staged")
    assert refused.returncode == 1, refused.stdout
    assert "corpus/moved card.md" in refused.stderr
    assert "QUAL-11" in refused.stderr


@pytest.mark.parametrize(
    ("stamp", "day"),
    [
        ("2026-11-16T09:00:00 +0000", "2026-11-16"),
        ("1700092800 +0000", "2023-11-16"),
        ("@1794787200 -0800", "2026-11-15"),
    ],
)
def test_the_commit_day_is_gits_parse_of_its_recorded_date(repo: Path, monkeypatch: pytest.MonkeyPatch, stamp: str, day: str) -> None:
    """The day compared with an audit date is the one Git writes, in the commit's zone."""
    monkeypatch.chdir(repo)
    monkeypatch.setenv("GIT_COMMITTER_DATE", stamp)
    assert commit_day("index") == date.fromisoformat(day)


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
    install_gate(repo)
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
    track(repo, valid)
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


def test_the_push_gate_judges_each_commit_by_its_own_day(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """An event edited on its own day stays edited when a later day's commit is pushed."""
    card = repo / "corpus/one card.md"
    card.write_text(recorded("2026-11-15"))
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-15T09:00:00 +0000")
    git(repo, "commit", "-qm", "record the day's event")
    base = git(repo, "rev-parse", "HEAD").strip()
    same_day = recorded("2026-11-15").replace("matches the printed exercise", "matches the printed statement")
    card.write_text(same_day)
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "repair the note on its own day")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")
    card.write_text(
        same_day.replace(
            "  note: The statement matches the printed statement.\n",
            "  note: The statement matches the printed statement.\n"
            "- event: solution-reviewed\n"
            "  by: claude\n"
            "  date: 2026-11-16\n"
            "  note: The solution follows the source's argument.\n",
        )
    )
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "next day")
    tip = git(repo, "rev-parse", "HEAD").strip()

    track(repo, base)
    result = run_push(repo, tip, "corpus/one card.md")

    assert result.returncode == 0, result.stderr


def test_the_push_gate_judges_an_earlier_commit_that_a_later_one_restores(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A rewrite published by an earlier commit is refused even when the tip restores it."""
    card = repo / "corpus/one card.md"
    card.write_text(RECORDED)
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-15T09:00:00 +0000")
    git(repo, "commit", "-qm", "record the dated event")
    base = git(repo, "rev-parse", "HEAD").strip()

    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")
    card.write_text(RECORDED.replace("matches the printed exercise", "matches the printed statement"))
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "--no-verify", "-qm", "rewrite the record without the gate")
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
    git(repo, "commit", "--no-verify", "-qm", "restore the record and append")
    tip = git(repo, "rev-parse", "HEAD").strip()

    track(repo, base)
    result = run_push(repo, tip, "corpus/one card.md")

    assert result.returncode == 1
    assert "corpus/one card.md: the source-checked event by claude dated 2026-11-11" in result.stderr
    assert "QUAL-11" in result.stderr


def test_the_push_gate_needs_the_branch_upstream(repo: Path) -> None:
    """With no upstream there is no base for the published range, so the check fails loudly."""
    tip = git(repo, "rev-parse", "HEAD").strip()
    result = run_push(repo, tip, "corpus/one card.md")
    assert result.returncode != 0
    assert "upstream" in result.stderr


def test_a_missing_revision_raises_rather_than_reading_as_an_empty_source(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(repo)
    with pytest.raises(subprocess.CalledProcessError):
        previous_source(Path("corpus/one card.md"), "0000000000000000000000000000000000000000")
