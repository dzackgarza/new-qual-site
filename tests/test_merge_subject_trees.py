"""The subject-tree merge must carry a fenced div whole.

A line-wise merge splits one, because a bare `:::` closer already appears in the
page it merges into and so is treated as an anchor rather than as content. The
resulting page is unreadable to Pandoc, which drops it from the page index and
dangles every link into it -- the failure this pass hit for real.
"""

from merge_subject_trees import div_depth, merge_text

BASE = """# Sets

:::{.definition title="Open"}
A set is open when it is a neighbourhood of each of its points.
:::

## Exercises
"""

INCOMING = """# Sets

:::{.definition title="Open"}
A set is open when it is a neighbourhood of each of its points.
:::

:::{.definition title="Closed"}
A set is closed when its complement is open.
:::

## Exercises
"""


def test_a_div_only_the_incoming_page_holds_arrives_whole() -> None:
    merged, added, _ = merge_text(BASE, INCOMING)

    assert "A set is closed when its complement is open." in merged
    assert merged.count(":::{.definition") == 2
    assert div_depth(merged) == 0
    # The opener, the statement and the closer all crossed, not just the prose.
    assert added.count(":::") == 1
    assert any(line.startswith(':::{.definition title="Closed"') for line in added)


def test_the_base_page_survives_the_merge_unreworded() -> None:
    merged, _, _ = merge_text(BASE, INCOMING)

    for line in BASE.splitlines():
        assert line in merged.splitlines()


def test_incoming_tags_are_kept_and_existing_ones_are_not_duplicated() -> None:
    base = "# Q\n\n## 1\n\n[[P-AAAAA]]\n"
    incoming = "# Q\n\n## 1\n\n[[P-AAAAA]] [[P-BBBBB]]\n"

    merged, _, tags = merge_text(base, incoming)

    assert tags == ["P-BBBBB"]
    assert merged.count("[[P-AAAAA]]") == 1
    assert "[[P-BBBBB]]" in merged
