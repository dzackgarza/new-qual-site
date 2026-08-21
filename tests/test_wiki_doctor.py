"""Wiki doctor reports named measurements, not verdicts about the mathematics."""

from __future__ import annotations

import json
from pathlib import Path

from wiki_doctor import ALL, main, run


def _write(path: Path, body: str, *, order: int = 1, title: str | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["---", f"order: {order}"]
    if title is not None:
        lines.append(f"title: {title}")
    lines.extend(["---", "", body])
    text = "\n".join(lines)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text)


def _findings(root: Path, name: str) -> list[str]:
    [check] = run([name], root=root)
    return check.findings


def test_empty_bodies_are_the_stripped_body_and_not_a_discard_rule(tmp_path: Path) -> None:
    wiki = tmp_path / "wiki"
    _write(wiki / "empty.md", "")
    _write(wiki / "spaces.md", "   \n")
    _write(wiki / "prose.md", "A sentence.\n")
    assert _findings(tmp_path, "empty-bodies") == [
        "wiki/empty.md",
        "wiki/spaces.md",
    ]


def test_order_at_least_100001_is_the_integer_floor(tmp_path: Path) -> None:
    wiki = tmp_path / "wiki"
    _write(wiki / "placeholder.md", "Note.\n", order=100001)
    _write(wiki / "above.md", "Note.\n", order=100003)
    _write(wiki / "assigned.md", "Note.\n", order=100000)
    assert _findings(tmp_path, "order-at-least-100001") == [
        "wiki/above.md: order 100003",
        "wiki/placeholder.md: order 100001",
    ]


def test_one_markdown_child_directory_is_index_plus_one_file_and_no_nested_md(
    tmp_path: Path,
) -> None:
    wiki = tmp_path / "wiki"
    _write(wiki / "PSet6" / "index.md", "Landing.\n", title="PSet 6")
    _write(wiki / "PSet6" / "PSet6.md", "Homework.\n", title="Homework")
    _write(wiki / "TwoKids" / "index.md", "Landing.\n")
    _write(wiki / "TwoKids" / "a.md", "A.\n")
    _write(wiki / "TwoKids" / "b.md", "B.\n")
    _write(wiki / "Nested" / "index.md", "Landing.\n")
    _write(wiki / "Nested" / "only.md", "Child.\n")
    _write(wiki / "Nested" / "deeper" / "leaf.md", "Nested.\n")
    _write(wiki / "index.md", "Home.\n")
    _write(wiki / "peer.md", "Peer.\n")
    assert _findings(tmp_path, "one-markdown-child-directories") == [
        "wiki/PSet6 (index.md + PSet6.md)",
    ]


def test_sibling_duplicate_titles_measure_authored_title_fields_in_one_directory(
    tmp_path: Path,
) -> None:
    wiki = tmp_path / "wiki"
    _write(wiki / "Modules" / "index.md", "Landing.\n", title="Modules")
    _write(wiki / "Modules" / "40_Modules.md", "Note.\n", title="Modules")
    _write(wiki / "Elsewhere" / "index.md", "Landing.\n", title="Modules")
    _write(wiki / "Untitled" / "a.md", "A.\n")
    _write(wiki / "Untitled" / "b.md", "B.\n")
    assert _findings(tmp_path, "sibling-duplicate-titles") == [
        "wiki/Modules: title 'Modules' on 40_Modules.md, index.md",
    ]


def test_obsidian_embed_syntax_is_bang_brackets_not_a_wikilink(tmp_path: Path) -> None:
    wiki = tmp_path / "wiki"
    _write(wiki / "embed.md", "![[Obsidian/Workshops/week]]\n")
    _write(wiki / "link.md", "See [[P-ABCDE]].\n")
    assert _findings(tmp_path, "obsidian-embed-syntax") == ["wiki/embed.md"]


def test_notion_hosts_are_the_two_domains_not_lookalikes(tmp_path: Path) -> None:
    wiki = tmp_path / "wiki"
    _write(wiki / "so.md", "https://www.notion.so/abc\n")
    _write(wiki / "site.md", "https://team.notion.site/notes\n")
    _write(wiki / "word.md", "These used to live in Notion.\n")
    _write(wiki / "mynotion.md", "See https://mynotion.so/page\n")
    _write(wiki / "soccer.md", "https://notion.soccer/fixture\n")
    assert _findings(tmp_path, "notion-so-or-notion-site-urls") == [
        "wiki/site.md",
        "wiki/so.md",
    ]


def test_hash_todo_is_standalone_marker_not_todolist_or_url_fragment(
    tmp_path: Path,
) -> None:
    wiki = tmp_path / "wiki"
    _write(wiki / "todo.md", "Proof. #todo finish the estimate.\n")
    _write(wiki / "todolist.md", "See the #todolist for remaining work.\n")
    _write(wiki / "fragment.md", "https://example.com/#todo\n")
    assert _findings(tmp_path, "hash-todo-markers") == ["wiki/todo.md"]


def test_line_shape_markers(tmp_path: Path) -> None:
    wiki = tmp_path / "wiki"
    _write(wiki / "todo.md", "Proof. #todo finish the estimate.\n")
    _write(wiki / "tags.md", "Tags: #resources/algebra\n")
    _write(wiki / "resources.md", "#resources/algebra\n\nA sentence.\n")
    _write(wiki / "tasks.md", "- [ ] first\n- [x] second\nA sentence.\n")
    _write(wiki / "clean.md", "A sentence about tagging resources.\n")
    assert _findings(tmp_path, "hash-todo-markers") == ["wiki/todo.md"]
    assert _findings(tmp_path, "tags-colon-lines") == ["wiki/tags.md"]
    assert _findings(tmp_path, "hash-resources-only-lines") == ["wiki/resources.md"]
    assert _findings(tmp_path, "task-list-item-lines") == ["wiki/tasks.md: 2"]


def test_heading_or_wikilink_only_bodies_ignore_prose_and_empty_pages(tmp_path: Path) -> None:
    wiki = tmp_path / "wiki"
    _write(wiki / "heading.md", "# Extra problems\n")
    _write(wiki / "list.md", "# Enumerating\n\n[[P-ABCDE]]\n- [[P-FGHIJ]]\n")
    _write(wiki / "prose.md", "# Title\n\nThis sitting asks the same question.\n")
    _write(wiki / "empty.md", "")
    assert _findings(tmp_path, "heading-or-wikilink-only-bodies") == [
        "wiki/heading.md",
        "wiki/list.md",
    ]


def test_unreadable_front_matter_is_named_and_does_not_stop_other_checks(
    tmp_path: Path,
) -> None:
    wiki = tmp_path / "wiki"
    wiki.mkdir()
    (wiki / "broken.md").write_text("---\norder: [\n---\n")
    _write(wiki / "empty.md", "")
    assert any(finding.startswith("wiki/broken.md:") for finding in _findings(tmp_path, "unreadable-wiki-pages"))
    assert _findings(tmp_path, "empty-bodies") == ["wiki/empty.md"]


def test_doctor_exits_zero_with_findings_and_is_not_a_gate(tmp_path: Path) -> None:
    _write(tmp_path / "wiki" / "empty.md", "")
    assert main(["--root", str(tmp_path), "--json"]) == 0
    # The CLI prints JSON to stdout; capture via run() rather than the print.
    payload = [{"check": check.name, "ok": check.ok, "findings": check.findings} for check in run(ALL, root=tmp_path)]
    dumped = json.dumps(payload)
    assert "empty-bodies" in dumped
    assert payload[ALL.index("empty-bodies")]["findings"] == ["wiki/empty.md"]
