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

import yaml

from qualc.authoring import RESTORED_SECTIONS, commit_day, dated_records, previous_source, source_identity

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


def folded(day: str) -> str:
    """The fixture card carrying one dated event whose note is a folded scalar over lines."""
    return CARD.replace(
        "\nreview: draft\n",
        "\nreview: draft\n"
        "audit:\n"
        "- event: source-checked\n"
        "  by: claude\n"
        f"  date: {day}\n"
        "  note: >-\n"
        "    The statement matches the printed exercise, read in the text version of the book,\n"
        "    and the local group is Hatcher's `M|x` in the notation of printed p. 234.\n",
    )


FOLDED = folded("2026-11-11")


def twice_recorded(day: str) -> str:
    """The fixture card carrying two dated audit events of one day and one author."""
    return CARD.replace(
        "\nreview: draft\n",
        "\nreview: draft\n"
        "audit:\n"
        "- event: source-checked\n"
        "  by: claude\n"
        f"  date: {day}\n"
        "  note: The statement matches the printed exercise.\n"
        "- event: source-checked\n"
        "  by: claude\n"
        f"  date: {day}\n"
        "  note: The local group is Hatcher's `M|x` on printed p. 234.\n",
    )


TWICE_RECORDED = twice_recorded("2026-11-11")
# Two dated COMPLAINTS records of one day, so the day alone does not identify either.
TWICE_RECORDED_COMPLAINTS = """# Mathematical issues and papercuts

## Open findings

**Searched outside the retained sets (2026-11-10).** The observation.

**A second search on the same day (2026-11-10).** Another observation.
"""

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

# A numbered list in the stated record format: two items with no blank line between
# them, the first carrying a continuation line, the second a paragraph of evidence.
NUMBERED_COMPLAINTS = """# Mathematical issues and papercuts

## Open findings

7. **Published-solution coverage gaps — open, 2026-11-07.** These are source obligations,
   not claims that the displayed mathematics is false.
8. **A later item, 2026-11-08.** Its own text stands here.

   *Searched, and found nothing.* The evidence the item records.
"""


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True).stdout


def staged_records(root: Path) -> str:
    """The payload the shared staged hook sends: every staged path at the index."""
    names = git(root, "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z")
    return "".join(json.dumps({"path": path, "version": "index"}) + "\n" for path in names.split("\0") if path)


def run_staged(root: Path) -> subprocess.CompletedProcess[str]:
    """The project's staged validator, fed as the shared hook feeds it."""
    return subprocess.run([sys.executable, "-m", "qualc.authoring", "check-changes", "--mode", "staged"], cwd=root, input=staged_records(root), capture_output=True, text=True)


def run_push(root: Path, tip: str, *paths: str) -> subprocess.CompletedProcess[str]:
    """The project's push validator, fed as the shared hook feeds it: the pushed tip."""
    payload = "".join(json.dumps({"path": path, "version": tip}) + "\n" for path in paths)
    return subprocess.run([sys.executable, "-m", "qualc.authoring", "check-changes", "--mode", "push"], cwd=root, input=payload, capture_output=True, text=True)


def validate_candidate(root: Path, mode: str, monkeypatch: pytest.MonkeyPatch, stamp: str, *paths: str) -> subprocess.CompletedProcess[str]:
    """Run the shared validator on the staged candidate, or commit it and validate the push."""
    monkeypatch.setenv("GIT_COMMITTER_DATE", stamp)
    if mode == "staged":
        return run_staged(root)
    git(root, "commit", "-qm", "validate the candidate")
    tip = git(root, "rev-parse", "HEAD").strip()
    return run_push(root, tip, *paths)


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
    """The staged chain: a hook builds the changed-file payload and runs qualc check-changes."""
    runner = root / ".git" / "hooks" / "staged-gate.py"
    runner.write_text(
        "import json, subprocess, sys\n"
        "names = subprocess.run(['git', 'diff', '--cached', '--name-only', '--diff-filter=ACMR', '-z'], check=True, stdout=subprocess.PIPE).stdout.decode()\n"
        "records = ''.join(json.dumps({'path': path, 'version': 'index'}) + '\\n' for path in names.split('\\0') if path)\n"
        f"raise SystemExit(subprocess.run([sys.executable, '-m', 'qualc.authoring', 'check-changes', '--mode', 'staged'], input=records.encode()).returncode)\n"
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


@pytest.mark.parametrize("mode", ("staged", "push"))
@pytest.mark.parametrize(
    ("case", "accepted"),
    [
        ("edit", False),
        ("delete", False),
        ("same-day-edit", True),
        ("append", True),
        ("restore", True),
        ("same-identity-twin-delete", False),
        ("same-identity-history-delete", False),
    ],
)
def test_the_dated_event_rule_through_the_shared_gate(repo: Path, monkeypatch: pytest.MonkeyPatch, mode: str, case: str, accepted: bool) -> None:
    """The QUAL-11 cases take the same one-to-one rule in both Git modes.

    A restoration's base is the commit that rewrote the record, already upstream in push
    mode; the candidate is only the repair. In the twin cases the base holds A rewritten
    and B original. One candidate restores A and deletes B; the other leaves A rewritten
    and replaces B with A's earlier text. Both must name B.
    """
    original = TWICE_RECORDED if case in ("same-identity-twin-delete", "same-identity-history-delete") else RECORDED
    card = repo / "corpus/one card.md"
    card.write_text(original)
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-11T09:00:00 +0000")
    git(repo, "commit", "-qm", "record the event on its day")

    if case in ("restore", "same-identity-twin-delete", "same-identity-history-delete"):
        card.write_text(original.replace("matches the printed exercise", "matches the printed statement"))
        git(repo, "add", "corpus/one card.md")
        monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-14T09:00:00 +0000")
        git(repo, "commit", "-qm", "rewrite the event before the repair")

    base = git(repo, "rev-parse", "HEAD").strip()
    if mode == "push":
        track(repo, base)

    candidates = {
        "edit": RECORDED.replace("matches the printed exercise", "matches the printed statement"),
        "delete": CARD,
        "same-day-edit": RECORDED.replace("matches the printed exercise", "matches the printed statement"),
        "append": RECORDED.replace(
            "  note: The statement matches the printed exercise.\n",
            "  note: The statement matches the printed exercise.\n"
            "- event: solution-reviewed\n"
            "  by: claude\n"
            "  date: 2026-11-16\n"
            "  note: The solution follows the source's argument.\n",
        ),
        "restore": RECORDED,
        "same-identity-twin-delete": RECORDED,
        "same-identity-history-delete": TWICE_RECORDED.replace(
            "matches the printed exercise", "matches the printed statement"
        ).replace(
            "The local group is Hatcher's `M|x` on printed p. 234.",
            "The statement matches the printed exercise.",
        ),
    }
    card.write_text(candidates[case])
    git(repo, "add", "corpus/one card.md")
    stamp = "2026-11-11T12:00:00 +0000" if case == "same-day-edit" else "2026-11-16T09:00:00 +0000"

    result = validate_candidate(repo, mode, monkeypatch, stamp, "corpus/one card.md")

    if accepted:
        assert result.returncode == 0, result.stderr
    else:
        assert result.returncode == 1, result.stdout
        assert "QUAL-11" in result.stderr
        assert "dated 2026-11-11" in result.stderr
        if case in ("same-identity-twin-delete", "same-identity-history-delete"):
            assert "The local group is Hatcher" in result.stderr


@pytest.mark.parametrize("mode", ("staged", "push"))
def test_restoring_both_events_of_one_identity_is_accepted(repo: Path, monkeypatch: pytest.MonkeyPatch, mode: str) -> None:
    """Two introduced texts restore together even though no earlier snapshot holds both.

    This is the punctured-line history: A was introduced and rewritten before B was
    introduced, and B was then rewritten too. Restoring A and B brings back every text
    introduced under their shared identity, rather than the multiset in one old revision.
    """
    first = "The statement matches the printed exercise."
    rewritten_first = "The statement matches the printed statement."
    second = "The local group is Hatcher's `M|x` on printed p. 234."
    rewritten_second = "The local group is Hatcher's `N|y` on printed p. 235."
    card = repo / "corpus/one card.md"
    for source, stamp in (
        (RECORDED, "2026-11-11T09:00:00 +0000"),
        (RECORDED.replace(first, rewritten_first), "2026-11-12T09:00:00 +0000"),
        (TWICE_RECORDED.replace(first, rewritten_first), "2026-11-13T09:00:00 +0000"),
        (TWICE_RECORDED.replace(first, rewritten_first).replace(second, rewritten_second), "2026-11-14T09:00:00 +0000"),
    ):
        card.write_text(source)
        git(repo, "add", "corpus/one card.md")
        monkeypatch.setenv("GIT_COMMITTER_DATE", stamp)
        git(repo, "commit", "-qm", "introduce or rewrite one dated event")
    if mode == "push":
        track(repo, git(repo, "rev-parse", "HEAD").strip())

    card.write_text(TWICE_RECORDED)
    git(repo, "add", "corpus/one card.md")
    result = validate_candidate(repo, mode, monkeypatch, "2026-11-16T09:00:00 +0000", "corpus/one card.md")

    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize("mode", ("staged", "push"))
def test_a_rewrite_beside_an_introduction_is_not_an_introduction(repo: Path, monkeypatch: pytest.MonkeyPatch, mode: str) -> None:
    """A commit that rewrites A while introducing B introduces B alone.

    A' must not become a text that the later restoration must carry: the only texts
    introduced under this identity are A and B, even though one commit brought in both
    the rewritten A' and the new B.
    """
    first = "The statement matches the printed exercise."
    rewritten_first = "The statement matches the printed statement."
    second = "The local group is Hatcher's `M|x` on printed p. 234."
    rewritten_second = "The local group is Hatcher's `N|y` on printed p. 235."
    card = repo / "corpus/one card.md"
    for source, stamp in (
        (RECORDED, "2026-11-11T09:00:00 +0000"),
        (TWICE_RECORDED.replace(first, rewritten_first), "2026-11-12T09:00:00 +0000"),
        (TWICE_RECORDED.replace(first, rewritten_first).replace(second, rewritten_second), "2026-11-14T09:00:00 +0000"),
    ):
        card.write_text(source)
        git(repo, "add", "corpus/one card.md")
        monkeypatch.setenv("GIT_COMMITTER_DATE", stamp)
        git(repo, "commit", "-qm", "rewrite one event or introduce another")
    if mode == "push":
        track(repo, git(repo, "rev-parse", "HEAD").strip())

    card.write_text(TWICE_RECORDED)
    git(repo, "add", "corpus/one card.md")
    result = validate_candidate(repo, mode, monkeypatch, "2026-11-16T09:00:00 +0000", "corpus/one card.md")

    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize("mode", ("staged", "push"))
def test_reordering_then_duplicating_an_event_is_refused(repo: Path, monkeypatch: pytest.MonkeyPatch, mode: str) -> None:
    """An exact reorder does not make B into A's earlier record or permit A's deletion."""
    first = "- event: source-checked\n  by: claude\n  date: 2026-11-11\n  note: The statement matches the printed exercise.\n"
    second = "- event: source-checked\n  by: claude\n  date: 2026-11-11\n  note: The local group is Hatcher's `M|x` on printed p. 234.\n"
    reordered = TWICE_RECORDED.replace(first + second, second + first)
    duplicated = reordered.replace(first, second)
    assert duplicated != reordered
    card = repo / "corpus/one card.md"
    for source, stamp in (
        (TWICE_RECORDED, "2026-11-11T09:00:00 +0000"),
        (reordered, "2026-11-14T09:00:00 +0000"),
    ):
        card.write_text(source)
        git(repo, "add", "corpus/one card.md")
        monkeypatch.setenv("GIT_COMMITTER_DATE", stamp)
        git(repo, "commit", "-qm", "record or reorder the dated events")
    if mode == "push":
        track(repo, git(repo, "rev-parse", "HEAD").strip())

    card.write_text(duplicated)
    git(repo, "add", "corpus/one card.md")
    result = validate_candidate(repo, mode, monkeypatch, "2026-11-16T09:00:00 +0000", "corpus/one card.md")

    assert result.returncode == 1, result.stdout
    assert "multiple dated audit events share one identity" in result.stderr
    assert "The statement matches the printed exercise." in result.stderr
    assert "QUAL-11" in result.stderr


@pytest.mark.parametrize("mode", ("staged", "push"))
def test_reordering_then_duplicating_a_complaint_is_refused(repo: Path, monkeypatch: pytest.MonkeyPatch, mode: str) -> None:
    """The same reorder-then-duplicate history is ambiguous for COMPLAINTS records."""
    first = "**Searched outside the retained sets (2026-11-10).** The observation."
    second = "**A second search on the same day (2026-11-10).** Another observation."
    reordered = TWICE_RECORDED_COMPLAINTS.replace(f"{first}\n\n{second}", f"{second}\n\n{first}")
    duplicated = reordered.replace(first, second)
    assert duplicated != reordered
    path = repo / "COMPLAINTS.md"
    for source, stamp in (
        (TWICE_RECORDED_COMPLAINTS, "2026-11-10T09:00:00 +0000"),
        (reordered, "2026-11-14T09:00:00 +0000"),
    ):
        path.write_text(source)
        git(repo, "add", "COMPLAINTS.md")
        monkeypatch.setenv("GIT_COMMITTER_DATE", stamp)
        git(repo, "commit", "-qm", "record or reorder the dated complaints")
    if mode == "push":
        track(repo, git(repo, "rev-parse", "HEAD").strip())

    path.write_text(duplicated)
    git(repo, "add", "COMPLAINTS.md")
    result = validate_candidate(repo, mode, monkeypatch, "2026-11-16T09:00:00 +0000", "COMPLAINTS.md")

    assert result.returncode == 1, result.stdout
    assert "multiple dated COMPLAINTS records share one identity" in result.stderr
    assert "Searched outside the retained sets" in result.stderr
    assert "QUAL-11" in result.stderr


def test_restoring_one_event_does_not_excuse_a_rewrite_of_another(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """QUAL-11 judges each record: a restoration beside a rewrite does not excuse it.

    Two events of one day and one author are the case the day cannot tell apart. A commit
    that restores one of them and gives the other text written that day is still a commit
    that rewrote a dated record, and what the gate knows about the restored one says
    nothing about the other.
    """
    card = repo / "corpus/one card.md"
    card.write_text(TWICE_RECORDED)
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-11T09:00:00 +0000")
    git(repo, "commit", "-qm", "record both events on their day")

    card.write_text(
        TWICE_RECORDED.replace("matches the printed exercise", "matches the printed statement").replace(
            "`M|x` on printed p. 234", "`N|y` on printed p. 235"
        )
    )
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-14T09:00:00 +0000")
    git(repo, "commit", "-qm", "rewrite both records in place")

    card.write_text(TWICE_RECORDED.replace("`M|x` on printed p. 234", "`Q|z` on printed p. 236"))
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")

    result = check(repo, "check-staged")

    assert result.returncode == 1, result.stdout
    assert "the source-checked event by claude dated 2026-11-11" in result.stderr
    assert "QUAL-11" in result.stderr


def test_restoring_one_record_does_not_excuse_a_rewrite_of_another(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """The COMPLAINTS records of one day are judged one by one for the same reason."""
    path = repo / "COMPLAINTS.md"
    path.write_text(TWICE_RECORDED_COMPLAINTS)
    git(repo, "add", "COMPLAINTS.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-10T09:00:00 +0000")
    git(repo, "commit", "-qm", "record both findings on their day")

    path.write_text(TWICE_RECORDED_COMPLAINTS.replace("The observation.", "The corrected observation.").replace(
        "Another observation.", "Another corrected observation."
    ))
    git(repo, "add", "COMPLAINTS.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-14T09:00:00 +0000")
    git(repo, "commit", "-qm", "rewrite both records in place")

    path.write_text(TWICE_RECORDED_COMPLAINTS.replace("Another observation.", "A third observation."))
    git(repo, "add", "COMPLAINTS.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")

    result = check(repo, "check-staged")

    assert result.returncode == 1, result.stdout
    assert "the record dated 2026-11-10" in result.stderr
    assert "QUAL-11" in result.stderr


@pytest.mark.parametrize("mode", ("staged", "push"))
@pytest.mark.parametrize("leave_rewritten", (False, True))
def test_restoring_one_complaint_does_not_excuse_deleting_its_twin(repo: Path, monkeypatch: pytest.MonkeyPatch, mode: str, leave_rewritten: bool) -> None:
    """A's earlier text never consumes B, including while A stays rewritten."""
    path = repo / "COMPLAINTS.md"
    path.write_text(TWICE_RECORDED_COMPLAINTS)
    git(repo, "add", "COMPLAINTS.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-10T09:00:00 +0000")
    git(repo, "commit", "-qm", "record both findings on their day")

    path.write_text(TWICE_RECORDED_COMPLAINTS.replace("The observation.", "The corrected observation."))
    git(repo, "add", "COMPLAINTS.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-14T09:00:00 +0000")
    git(repo, "commit", "-qm", "rewrite the first finding")
    if mode == "push":
        track(repo, git(repo, "rev-parse", "HEAD").strip())

    if leave_rewritten:
        candidate = TWICE_RECORDED_COMPLAINTS.replace("The observation.", "The corrected observation.").replace(
            "**A second search on the same day (2026-11-10).** Another observation.",
            "**Searched outside the retained sets (2026-11-10).** The observation.",
        )
    else:
        candidate = TWICE_RECORDED_COMPLAINTS.replace("\n**A second search on the same day (2026-11-10).** Another observation.\n", "")
    path.write_text(candidate)
    git(repo, "add", "COMPLAINTS.md")

    result = validate_candidate(repo, mode, monkeypatch, "2026-11-16T09:00:00 +0000", "COMPLAINTS.md")

    assert result.returncode == 1, result.stdout
    assert "QUAL-11" in result.stderr
    assert "A second search on the same day" in result.stderr


def test_deleting_one_of_two_events_of_a_day_is_refused(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """An event the commit leaves standing is no restoration of the one it removes.

    The two events share their day, their kind and their author, and the text that goes
    stands in an earlier revision of the card — which is what the restoration rule looks
    for. Read as a group without regard to which records the commit brings in, the
    survivor would excuse the deletion.
    """
    card = repo / "corpus/one card.md"
    card.write_text(TWICE_RECORDED)
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-11T09:00:00 +0000")
    git(repo, "commit", "-qm", "record both events on their day")

    card.write_text(
        TWICE_RECORDED.replace(
            "- event: source-checked\n  by: claude\n  date: 2026-11-11\n  note: The local group is Hatcher's `M|x` on printed p. 234.\n",
            "",
        )
    )
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")

    result = run_staged(repo)

    assert result.returncode == 1, result.stdout
    assert "corpus/one card.md: the source-checked event by claude dated 2026-11-11" in result.stderr
    assert "The local group is Hatcher" in result.stderr
    assert "QUAL-11" in result.stderr


def test_deleting_one_of_two_records_of_a_day_is_refused(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """The COMPLAINTS records of one day are judged the same way: the survivor is no shield."""
    path = repo / "COMPLAINTS.md"
    path.write_text(TWICE_RECORDED_COMPLAINTS)
    git(repo, "add", "COMPLAINTS.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-10T09:00:00 +0000")
    git(repo, "commit", "-qm", "record both findings on their day")

    path.write_text(TWICE_RECORDED_COMPLAINTS.replace("**Searched outside the retained sets (2026-11-10).** The observation.\n\n", ""))
    git(repo, "add", "COMPLAINTS.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")

    result = run_staged(repo)

    assert result.returncode == 1, result.stdout
    assert "COMPLAINTS.md: the record dated 2026-11-10" in result.stderr
    assert "Searched outside the retained sets" in result.stderr
    assert "QUAL-11" in result.stderr


@pytest.mark.parametrize("mode", ("staged", "push"))
def test_a_non_markdown_blob_does_not_shield_a_deleted_card(repo: Path, monkeypatch: pytest.MonkeyPatch, mode: str) -> None:
    """Only a Markdown card can carry the retired card's id and its dated events."""
    card = repo / "corpus/one card.md"
    card.write_text(RECORDED)
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-11T09:00:00 +0000")
    git(repo, "commit", "-qm", "record the event on its day")
    if mode == "push":
        track(repo, git(repo, "rev-parse", "HEAD").strip())

    card.unlink()
    (repo / "corpus/not-a-card.txt").write_text(RECORDED)
    git(repo, "add", "-A")

    result = validate_candidate(repo, mode, monkeypatch, "2026-11-16T09:00:00 +0000", "corpus/not-a-card.txt")

    assert result.returncode == 1, result.stdout
    assert "corpus/one card.md: the source-checked event" in result.stderr
    assert "QUAL-11" in result.stderr


def test_a_card_moved_below_gits_similarity_threshold_is_not_a_deletion(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A move Git cannot pair by similarity is still a move, and the card keeps its events.

    With the body rewritten the two paths share too little for Git to record a rename, so
    the move arrives as a deletion and an addition. The addition carries the card's id and
    is compared with the retired path's text; reading the retired path as a card deleted
    would report every one of its dated events as deleted and refuse the move.
    """
    card = repo / "corpus/one card.md"
    card.write_text(RECORDED)
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-15T09:00:00 +0000")
    git(repo, "commit", "-qm", "record a dated event")

    front, _, _ = RECORDED.partition("\n---\n")
    moved = repo / "corpus/moved card.md"
    (repo / "corpus/one card.md").unlink()
    moved.write_text(front + "\n---\n\n" + "A body written at the new path, unlike the old one.\n" * 40)
    git(repo, "add", "-A")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")

    status = git(repo, "diff", "--cached", "--name-status")
    assert "D\tcorpus/one card.md" in status and "A\tcorpus/moved card.md" in status, f"Git paired the paths; the test no longer exercises the threshold:\n{status}"

    result = run_staged(repo)

    assert result.returncode == 0, result.stderr


def test_a_restored_event_matches_a_note_folded_over_lines(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """An authored note is a folded scalar, and its record has no line breaks.

    A note long enough to wrap is stored as `>-` text, so the record the gate compares is
    the folded note while the earlier revision holds the wrapped one. The restoration
    rule therefore has to compare them as text, not as layout.
    """
    card = repo / "corpus/one card.md"
    card.write_text(FOLDED)
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-11T09:00:00 +0000")
    git(repo, "commit", "-qm", "record the folded event on its day")

    card.write_text(FOLDED.replace("printed exercise, read", "printed statement, read"))
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-14T09:00:00 +0000")
    git(repo, "commit", "-qm", "rewrite the folded record in place")

    card.write_text(FOLDED)
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")

    result = check(repo, "check-staged")

    assert result.returncode == 0, result.stderr


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


def test_a_numbered_complaint_is_one_record_with_its_continuation(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """QUAL-11 protects the numbered item, and the evidence it holds is part of it.

    The items of a list are records one by one even where no blank line separates them,
    and an item's continuation line and evidence are what the item records. Splitting
    the file at blank lines would protect only the item's opening line and leave its
    evidence editable or deletable.
    """
    path = repo / "COMPLAINTS.md"
    path.write_text(NUMBERED_COMPLAINTS)
    git(repo, "add", "COMPLAINTS.md")
    git(repo, "commit", "-qm", "record the findings")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")

    evidence = NUMBERED_COMPLAINTS.replace("The evidence the item records.", "The evidence the item records, checked twice.")
    path.write_text(evidence)
    git(repo, "add", "COMPLAINTS.md")
    refused = check(repo, "check-staged")
    assert refused.returncode == 1, refused.stdout
    assert "COMPLAINTS.md: the record dated 2026-11-08" in refused.stderr
    assert "QUAL-11" in refused.stderr

    continuation = NUMBERED_COMPLAINTS.replace(
        "These are source obligations,\n   not claims that the displayed mathematics is false.",
        "These are source obligations.",
    )
    path.write_text(continuation)
    git(repo, "add", "COMPLAINTS.md")
    refused = check(repo, "check-staged")
    assert refused.returncode == 1, refused.stdout
    assert "COMPLAINTS.md: the record dated 2026-11-07" in refused.stderr

    removed = NUMBERED_COMPLAINTS.replace("\n   *Searched, and found nothing.* The evidence the item records.\n", "")
    path.write_text(removed)
    git(repo, "add", "COMPLAINTS.md")
    refused = check(repo, "check-staged")
    assert refused.returncode == 1, refused.stdout
    assert "COMPLAINTS.md: the record dated 2026-11-08" in refused.stderr

    path.write_text(NUMBERED_COMPLAINTS + "\n9. **A correction, 2026-11-16.** The record stands.\n")
    git(repo, "add", "COMPLAINTS.md")
    appended = check(repo, "check-staged")
    assert appended.returncode == 0, appended.stderr


def test_a_restored_heading_is_read_as_the_record_of_its_own_day() -> None:
    """A restored heading states its day mid-title, and the gate reads it there."""
    heading, day = next(iter(RESTORED_SECTIONS.items()))
    assert [found for found, _ in dated_records(f"{heading}\n\nWhat the section says.\n")] == [day]


@pytest.mark.parametrize("mode", ("staged", "push"))
def test_a_restored_complaints_section_is_protected_through_the_shared_gate(repo: Path, monkeypatch: pytest.MonkeyPatch, mode: str) -> None:
    """The named restored section is a dated record in both validator modes."""
    heading, day = next(iter(RESTORED_SECTIONS.items()))
    path = repo / "COMPLAINTS.md"
    path.write_text(f"{heading}\n\nWhat that day found.\n")
    git(repo, "add", "COMPLAINTS.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", f"{day.isoformat()}T09:00:00 +0000")
    git(repo, "commit", "-qm", "record the restored section")
    if mode == "push":
        track(repo, git(repo, "rev-parse", "HEAD").strip())

    path.write_text(f"{heading}\n\nAn edited record.\n")
    git(repo, "add", "COMPLAINTS.md")

    result = validate_candidate(repo, mode, monkeypatch, "2026-11-16T09:00:00 +0000", "COMPLAINTS.md")

    assert result.returncode == 1, result.stdout
    assert f"COMPLAINTS.md: the record dated {day}" in result.stderr
    assert "QUAL-11" in result.stderr


def test_deleting_the_complaints_file_is_refused(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Deleting COMPLAINTS.md deletes every dated record it states (QUAL-11).

    The shared hook's payload lists only the paths that survive a change, so a commit
    that deletes the file gives the gate nothing to compare; the deletion is read from
    Git's own diff instead.
    """
    path = repo / "COMPLAINTS.md"
    path.write_text(COMPLAINTS)
    git(repo, "add", "COMPLAINTS.md")
    git(repo, "commit", "-qm", "record findings")
    install_gate(repo)
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")
    recorded = git(repo, "rev-parse", "HEAD")

    git(repo, "rm", "-q", "COMPLAINTS.md")
    refused = subprocess.run(["git", "commit", "-qm", "drop the complaints file"], cwd=repo, capture_output=True, text=True)

    assert refused.returncode != 0, refused.stdout
    assert "COMPLAINTS.md: the record dated 2026-11-10" in refused.stderr
    assert "QUAL-11" in refused.stderr
    assert git(repo, "rev-parse", "HEAD") == recorded
    assert "D  COMPLAINTS.md" in git(repo, "status", "--porcelain")


def test_deleting_a_card_deletes_its_dated_events(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A card's dated events are deleted with the card, so the deletion is refused.

    The path is gone from the commit, so there is no blob to read for the comparison:
    the earlier text is read at the base and its events are compared with nothing.
    """
    card = repo / "corpus/one card.md"
    card.write_text(RECORDED)
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "record a dated event")
    install_gate(repo)
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")
    recorded = git(repo, "rev-parse", "HEAD")

    git(repo, "rm", "-q", "corpus/one card.md")
    refused = subprocess.run(["git", "commit", "-qm", "drop the card"], cwd=repo, capture_output=True, text=True)

    assert refused.returncode != 0, refused.stdout
    assert "corpus/one card.md: the source-checked event by claude dated 2026-11-11" in refused.stderr
    assert "was changed or deleted" in refused.stderr
    assert git(repo, "rev-parse", "HEAD") == recorded


@pytest.mark.parametrize("mode", ["staged", "push"])
@pytest.mark.parametrize("transfer", ["complete", "missing", "rewritten", "unchanged-copy"])
def test_card_merge_preserves_retired_dated_events(repo: Path, monkeypatch: pytest.MonkeyPatch, mode: str, transfer: str) -> None:
    """CARD-04 retires a card, not the records it carries (QUAL-11)."""
    survivor = repo / "corpus/one card.md"
    retired = repo / "corpus/retired.md"
    note = "The local group is Hatcher's `M|x` on printed p. 234."
    original = RECORDED if transfer != "unchanged-copy" else TWICE_RECORDED
    survivor.write_text(original)
    retired.write_text(RECORDED.replace("PRB-INDEXP", "PRB-RETIRED").replace("The statement matches the printed exercise.", note))
    git(repo, "add", "-A")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-15T09:00:00 +0000")
    git(repo, "commit", "-qm", "record both cards")
    if mode == "push":
        track(repo, git(repo, "rev-parse", "HEAD").strip())

    git(repo, "rm", "corpus/retired.md")
    if transfer == "complete":
        survivor.write_text(TWICE_RECORDED)
    elif transfer == "rewritten":
        survivor.write_text(TWICE_RECORDED.replace(note, "A different historical observation."))
    else:
        survivor.write_text(original + "\nMerged the statements.\n")
    git(repo, "add", "corpus/one card.md")
    if mode == "staged":
        # Worktree text must not rescue an incomplete transfer in the staged blob.
        survivor.write_text(TWICE_RECORDED)

    result = validate_candidate(repo, mode, monkeypatch, "2026-11-16T09:00:00 +0000", "corpus/one card.md")
    if transfer == "complete":
        assert result.returncode == 0, result.stderr
    else:
        assert result.returncode == 1, result.stdout
        assert "corpus/retired.md: the source-checked event by claude dated 2026-11-11" in result.stderr
        assert "was changed or deleted" in result.stderr


@pytest.mark.parametrize("copies", [1, 2])
def test_card_merge_counts_identical_events_from_each_retired_card(repo: Path, monkeypatch: pytest.MonkeyPatch, copies: int) -> None:
    survivor = repo / "corpus/one card.md"
    for name in ("A", "B"):
        (repo / f"corpus/retired-{name}.md").write_text(RECORDED.replace("PRB-INDEXP", f"PRB-RETIRED-{name}"))
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-15T09:00:00 +0000")
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "record two retired cards")
    git(repo, "rm", "corpus/retired-A.md", "corpus/retired-B.md")
    extra = RECORDED.split("audit:\n", 1)[1].split("---\n", 1)[0]
    survivor.write_text(CARD.replace("review: draft\n", "review: draft\naudit:\n" + extra * copies))
    git(repo, "add", "corpus/one card.md")
    result = validate_candidate(repo, "staged", monkeypatch, "2026-11-16T09:00:00 +0000")
    assert result.returncode == (0 if copies == 2 else 1), result.stderr
    if copies == 1:
        assert "without reusing an occurrence (QUAL-11)" in result.stderr


def test_card_merge_does_not_split_one_retired_history_across_survivors(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    survivor = repo / "corpus/one card.md"
    other = repo / "corpus/other.md"
    other.write_text(CARD.replace("PRB-INDEXP", "PRB-OTHER"))
    (repo / "corpus/retired.md").write_text(TWICE_RECORDED.replace("PRB-INDEXP", "PRB-RETIRED"))
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-15T09:00:00 +0000")
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "record two events on the retired card")
    git(repo, "rm", "corpus/retired.md")
    survivor.write_text(RECORDED)
    other.write_text(RECORDED.replace("PRB-INDEXP", "PRB-OTHER").replace("The statement matches the printed exercise.", "The local group is Hatcher's `M|x` on printed p. 234."))
    git(repo, "add", "-A")
    result = validate_candidate(repo, "staged", monkeypatch, "2026-11-16T09:00:00 +0000")
    assert result.returncode == 1, result.stdout
    assert "corpus/retired.md:" in result.stderr
    assert "QUAL-11" in result.stderr


@pytest.mark.parametrize("preserve_survivor", [False, True])
def test_card_merge_with_moved_survivor_reserves_its_history(repo: Path, monkeypatch: pytest.MonkeyPatch, preserve_survivor: bool) -> None:
    old_survivor = repo / "corpus/one card.md"
    other_note = "The local group is Hatcher's `M|x` on printed p. 234."
    retired = repo / "corpus/retired.md"
    old_survivor.write_text(RECORDED.replace("The statement matches the printed exercise.", other_note).replace("by: claude", "by: reader") + "\nDifferent exposition.\n" * 100)
    retired.write_text(RECORDED.replace("PRB-INDEXP", "PRB-RETIRED"))
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-15T09:00:00 +0000")
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "record both cards")
    git(repo, "rm", "corpus/one card.md", "corpus/retired.md")
    moved = repo / "corpus/moved.md"
    merged = TWICE_RECORDED.replace("- event: source-checked\n  by: claude\n  date: 2026-11-11\n  note: " + other_note, "- event: source-checked\n  by: reader\n  date: 2026-11-11\n  note: " + other_note)
    moved.write_text(merged if preserve_survivor else RECORDED)
    git(repo, "add", "corpus/moved.md")
    diff = git(repo, "diff", "--cached", "--find-renames", "--name-status")
    assert re.search(r"R\d+\s+corpus/retired.md\s+corpus/moved.md", diff), diff
    result = validate_candidate(repo, "staged", monkeypatch, "2026-11-16T09:00:00 +0000")
    assert result.returncode == (0 if preserve_survivor else 1), result.stderr
    if not preserve_survivor:
        assert "QUAL-11" in result.stderr


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


def test_commit_card_supplies_the_restoration_history(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """The sanctioned commit-card route calls the dated-record comparison with its history."""
    card = repo / "corpus/one card.md"
    card.write_text(RECORDED)
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-11T09:00:00 +0000")
    git(repo, "commit", "-qm", "record the event on its day")
    card.write_text(RECORDED + "\nA reviewed remark.\n")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")

    result = check(repo, "commit", "corpus/one card.md", "review the card")

    assert result.returncode == 0, result.stderr
    assert git(repo, "show", "HEAD:corpus/one card.md") == card.read_text()


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
        [sys.executable, "-m", "qualc.authoring", "check-changes", "--mode", "push"],
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
    # The push gate replays the commits above the branch's upstream, so a deletion-only
    # range still has a base to read the deleted text at.
    track(repo, git(repo, "rev-parse", "HEAD").strip())

    def push() -> subprocess.CompletedProcess[str]:
        # A deletion-only range gives the shared hook no changed card to send.
        return subprocess.run([sys.executable, "-m", "qualc.authoring", "check-changes", "--mode", "push"], cwd=repo, input="", capture_output=True, text=True)

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


def merge_published_edit(repo: Path, monkeypatch: pytest.MonkeyPatch) -> str:
    """Publish a same-day edit of a dated event, commit locally beside it, and start a later day's merge.

    The published side edits the event on its own day, which the gate accepts there. The
    merge, made the next day, carries that edit unchanged. Returns the published commit;
    the merge is left uncommitted so a test can commit it as it stands or edit it first.
    """
    card = repo / "corpus/one card.md"
    card.write_text(recorded("2026-11-15"))
    git(repo, "add", "corpus/one card.md")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-15T09:00:00 +0000")
    git(repo, "commit", "-qm", "record the day's event")
    branch = git(repo, "symbolic-ref", "--short", "HEAD").strip()
    git(repo, "switch", "-qc", "published")
    card.write_text(recorded("2026-11-15").replace("matches the printed exercise", "matches the printed statement"))
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "repair the note on its own day")
    published = git(repo, "rev-parse", "HEAD").strip()
    git(repo, "switch", "-q", branch)
    (repo / "notes.txt").write_text("A local change beside the card.\n")
    git(repo, "add", "notes.txt")
    git(repo, "commit", "-qm", "local work")
    track(repo, published)
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-16T09:00:00 +0000")
    git(repo, "merge", "-q", "--no-commit", "--no-ff", published)
    return published


def test_the_push_gate_does_not_rejudge_published_changes_a_merge_carries(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A merge of the upstream into local work publishes only what the merge itself authored.

    Replayed against its first parent, the merge would present every published change as
    its own, judged on the merge's day: the same-day edit becomes a rewrite of an event
    dated before it. The published commit was judged on its own day when it was pushed.
    """
    merge_published_edit(repo, monkeypatch)
    git(repo, "commit", "-qm", "merge the upstream")

    result = run_push(repo, git(repo, "rev-parse", "HEAD").strip())

    assert result.returncode == 0, result.stderr


def test_the_push_gate_judges_what_a_merge_itself_rewrites(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A merge result that rewrites a dated event, beyond what either side carried, is refused."""
    merge_published_edit(repo, monkeypatch)
    card = repo / "corpus/one card.md"
    card.write_text(recorded("2026-11-15").replace("matches the printed exercise", "agrees with the printed exercise"))
    git(repo, "add", "corpus/one card.md")
    git(repo, "commit", "-qm", "merge the upstream and rewrite the event")

    result = run_push(repo, git(repo, "rev-parse", "HEAD").strip())

    assert result.returncode == 1
    assert "corpus/one card.md: the source-checked event by claude dated 2026-11-15" in result.stderr
    assert "QUAL-11" in result.stderr


def test_the_push_gate_needs_the_branch_upstream(repo: Path) -> None:
    """With no upstream there is no base for the published range, so the check fails loudly."""
    tip = git(repo, "rev-parse", "HEAD").strip()
    result = run_push(repo, tip, "corpus/one card.md")
    assert result.returncode != 0
    assert "upstream" in result.stderr


def test_a_malformed_id_line_is_reported_rather_than_read_as_no_identity() -> None:
    """The id is read without validating the rest of the header, and not by swallowing it.

    A deleted blob is read for the card it held. If a YAML error on its id line read as
    "no identity", a move of that card would silently compare nothing, so the error is
    raised and the commit that touches the card reports it. Only a header with no id
    line, or an id that is not a nonempty scalar, has no identity to match.
    """
    with pytest.raises(yaml.YAMLError):
        source_identity(CARD.replace("id: PRB-INDEXP\n", "id: [PRB-INDEXP\n"))
    assert source_identity(CARD.replace("id: PRB-INDEXP\n", "")) is None
    assert source_identity(CARD.replace("id: PRB-INDEXP\n", "id:\n")) is None


def test_a_missing_revision_raises_rather_than_reading_as_an_empty_source(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(repo)
    with pytest.raises(subprocess.CalledProcessError):
        previous_source(Path("corpus/one card.md"), "0000000000000000000000000000000000000000")


# Issue #111's second acceptance criterion: a later mathematical correction to a card
# arrives with its certificate in the same change. `solution-corrected` is the marker
# that makes "a mathematical correction" decidable, so the gate can refuse the recording
# of one on a card no certificate row covers for the whole statement.
CORRECTION = (
    "audit:\n"
    "- event: solution-corrected\n"
    "  by: claude\n"
    "  date: 2026-11-18\n"
    "  note: The closing step is repaired.\n"
)

REGISTRY_ROW = (
    "# Proof artifacts\n"
    "\n"
    "## 1. Group lemmas proved in Lean\n"
    "\n"
    "| File | Card | What it proves | Covers |\n"
    "| --- | --- | --- | --- |\n"
    "| `cards/Kept.sage` | `P-INDEXP` | the fixture computation | the statement |\n"
)


def corrected(root: Path) -> None:
    """Stage the fixture card carrying one recorded correction.

    The card is re-identified as `P-INDEXP`: the registry's card-id syntax is `P-` or
    `E-` followed by a source code, so the fixture's own `PRB-INDEXP` id is not one the
    certificate tables can name.
    """
    card = root / "corpus/one card.md"
    source = CARD.replace("id: PRB-INDEXP", "id: P-INDEXP")
    card.write_text(source.replace("\nreview: draft\n", "\nreview: draft\n" + CORRECTION))
    git(root, "add", "corpus/one card.md")


def test_a_recorded_correction_without_a_certificate_is_refused(repo: Path) -> None:
    corrected(repo)

    result = check(repo, "check-staged")

    assert result.returncode == 1, result.stdout
    assert "corpus/one card.md" in result.stderr
    assert "solution-corrected" in result.stderr
    assert "certifies no statement for P-INDEXP" in result.stderr


def test_a_recorded_correction_with_its_certificate_is_accepted(repo: Path) -> None:
    corrected(repo)
    (repo / "proofs").mkdir()
    (repo / "proofs" / "README.md").write_text(REGISTRY_ROW)
    git(repo, "add", "proofs/README.md")

    result = check(repo, "check-staged")

    assert result.returncode == 0, result.stderr


def test_a_row_covering_part_of_the_statement_does_not_carry_a_correction(repo: Path) -> None:
    """`part` is not `the statement`: the criterion names the corrected claim itself."""
    corrected(repo)
    (repo / "proofs").mkdir()
    (repo / "proofs" / "README.md").write_text(REGISTRY_ROW.replace("| the statement |", "| part |"))
    git(repo, "add", "proofs/README.md")

    result = check(repo, "check-staged")

    assert result.returncode == 1, result.stdout
    assert "certifies no statement for P-INDEXP" in result.stderr
