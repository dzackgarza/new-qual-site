"""A generated card title names the statement, and generating it costs no body.

`title_of` and the head/body splitter read the same furniture filter, and the two
want opposite answers about an enumerator. A bare `a.` is worthless as a title --
92 cards carried one -- but hoisting it out of the body would leave a multi-part
problem with an unlabelled part (a) beside a labelled (b). These tests pin both
halves, because widening one filter to fix the titles silently breaks the split.
"""

from route_apply import NOT_A_TITLE, NOT_A_TITLE_ALONE, title_of


def generated(body: str) -> str:
    return title_of({}, body)


def test_title_skips_a_bare_enumerator() -> None:
    body = "a.\nWhat is the degree of the antipodal map on the $n$-sphere?\n"
    assert generated(body) == "What is the degree of the antipodal map on the $n$-sphere?"


def test_title_skips_a_lone_display_math_delimiter() -> None:
    body = "\\[\n\\int_0^1 f(x)\\, dx = 0\n\\]\n"
    assert generated(body) == "\\int_0^1 f(x)\\, dx = 0"


def test_title_keeps_an_enumerator_that_carries_the_statement() -> None:
    """Only a *bare* marker is furniture. `1. Parts` is the statement's opening."""
    assert generated("1. Parts\n") == "1. Parts"


def test_authored_title_still_wins_over_the_first_clause() -> None:
    body = ':::{.problem title="Schwarz reflection"}\na.\nState the principle.\n:::\n'
    assert generated(body) == "Schwarz reflection"


def test_the_body_splitter_does_not_treat_an_enumerator_as_furniture() -> None:
    """`NOT_A_TITLE` also drives the head/body split, where `a.` is content.

    Fold `NOT_A_TITLE_ALONE` into it and part (a) of every multi-part problem
    loses its label to the page.
    """
    assert not NOT_A_TITLE.match("a.")
    assert not NOT_A_TITLE.match("\\[")
    assert NOT_A_TITLE_ALONE.match("a.")
    assert NOT_A_TITLE_ALONE.match("\\[")
