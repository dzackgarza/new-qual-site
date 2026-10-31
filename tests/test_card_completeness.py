"""The standalone completeness report counts complete and incomplete problem cards."""

from __future__ import annotations

from pathlib import Path

from qualc.card_completeness import main


def test_report_counts_complete_and_incomplete_problem_cards(tmp_path: Path, monkeypatch, capsys) -> None:
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    (corpus / "P-COMPLETE.md").write_text(
        "---\nkind: problem\ntitle: Complete\nclassification:\n  areas: [algebra]\n  topics: [Groups]\n---\nA problem.\n"
    )
    (corpus / "P-INCOMPLETE.md").write_text(
        "---\nkind: problem\ntitle: Incomplete\nclassification:\n  areas: [algebra]\n  topics: []\n---\nA problem.\n"
    )
    monkeypatch.chdir(tmp_path)
    main()
    output = capsys.readouterr().out
    assert "complete:   1" in output
    assert "incomplete: 1" in output
    assert "P-INCOMPLETE: no-topics" in output
