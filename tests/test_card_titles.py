"""A card title is the opening of its own statement, cut where a reader can read it.

The importers used to take the first non-empty *line*, which is how 29 cards came
to be titled `Let`: a qualifying-exam problem names its objects, displays them,
and only then asks the question. These pin the derivation that replaced it, and
the measure the audit applies to a title that arrives some other way.

`NOT_A_TITLE` drives the head/body split, where a bare
enumerator is statement rather than furniture; that is a separate question from
what makes a line worth titling a card after, and the last test holds them apart.
"""

from card_titles import NOT_A_TITLE, DegenerateReason, degenerate, retitle, title_of


def test_title_reaches_past_a_lead_in_to_the_question() -> None:
    body = (
        "Let\n\\[\nA \\in M_3(\\CC)\n\\]\n(a) Find the Jordan canonical form of $A$.\n"
    )
    assert (
        title_of(body)
        == "Let $A \\in M_3(\\CC)$ Find the Jordan canonical form of $A$."
    )


def test_title_carries_the_display_a_statement_is_about() -> None:
    """`Show that` names nothing; the identity it introduces is the statement."""
    body = (
        "Show that\n$$\n\\int_0^\\infty \\frac{\\sin x}{x} dx = \\frac{\\pi}{2}\n$$\n"
    )
    assert (
        title_of(body)
        == "Show that $\\int_0^\\infty \\frac{\\sin x}{x} dx = \\frac{\\pi}{2}$"
    )


def test_title_joins_a_wrapped_line_rather_than_splitting_its_mathematics() -> None:
    """The corpus wraps at 72 columns, so a `$...$` can straddle two lines."""
    body = "Evaluate $\\displaystyle{ \\int_0^\\infty \\frac{x \\sin x}{x^2+a^2}\n dx }$ for $a > 0$.\n"
    assert (
        title_of(body)
        == "Evaluate $\\displaystyle{ \\int_0^\\infty \\frac{x \\sin x}{x^2+a^2} dx }$ for $a > 0$."
    )


def test_authored_title_wins_over_the_statement() -> None:
    body = ':::{.problem title="Schwarz reflection"}\na.\nState the principle.\n:::\n'
    assert title_of(body) == "Schwarz reflection"


def test_a_short_authored_title_takes_the_statement_only_to_break_a_tie() -> None:
    """Two definitions both titled `Dense` are indistinguishable in a list."""
    first = ':::{.definition title="Dense"}\nA subset $A \\subseteq X$ is dense iff $\\cl_X(A) = X$.\n:::\n'
    second = ':::{.definition title="Dense"}\nA subspace $Q$ is dense iff every ball meets it.\n:::\n'
    titles = retitle({"D-1": first, "D-2": second})
    assert (
        titles["D-1"]
        == "Dense: A subset $A \\subseteq X$ is dense iff $\\cl_X(A) = X$."
    )
    assert titles["D-2"] == "Dense: A subspace $Q$ is dense iff every ball meets it."


def test_a_statement_of_only_a_figure_admits_it_rather_than_inventing_words() -> None:
    body = ':::{.exercise title="?"}\n![figure](../../assets/figures/2021-05-17.png)\n:::\n'
    assert title_of(body) == "Untitled"
    assert degenerate(title_of(body)) == DegenerateReason.NO_TITLE


def test_a_cut_never_falls_inside_the_mathematics() -> None:
    """A title cut mid-formula prints its source instead of typesetting."""
    body = "Show that " + " ".join(
        f"$x_{{{n}}} + y_{{{n}}}$ is small" for n in range(20)
    )
    assert degenerate(title_of(body)) is None


def test_an_aligned_display_reaches_the_title_inside_its_environment() -> None:
    """The corpus writes `\\[ a &= b \\\\ &= c \\]`, where the alignment characters
    have no environment; a title's mathematics is inline, where a bare `&` is
    "Misplaced &". The site's renderer wraps such a block in `aligned` before
    typesetting it, and the title has to carry the wrapper itself."""
    body = "Plancherel:\n\\[\n\\|f\\|^2 &= \\|\\hat f\\|^2 \\\\ &= 1\n.\\]\n"
    title = title_of(body)
    assert (
        title
        == "Plancherel: $\\begin{aligned}\\|f\\|^2 &= \\|\\hat f\\|^2 \\\\ &= 1\\end{aligned}$"
    )
    assert degenerate(title) is None


def test_a_padded_delimiter_never_reaches_a_title() -> None:
    """The corpus writes `$ x $` as often as `$x$`. Pandoc opens no math span on
    `$ `, so the whole span reaches the page as source with its operators
    dropped: `$ \\cos(z) = \\cosh(?) $` renders as "(z) = (?)"."""
    body = ':::{.fact title="Angle addition: $ \\cosh(x+iy) = \\cdots $"}\nbody\n:::\n'
    assert title_of(body) == "Angle addition: $\\cosh(x+iy) = \\cdots$"
    assert (
        degenerate("Angle addition: $ \\cosh(x+iy) $")
        == DegenerateReason.DOES_NOT_TYPESET
    )
    assert degenerate("Angle addition: $\\cosh(x+iy)$") is None


def test_degenerate_names_the_defects_a_reader_meets() -> None:
    assert degenerate("Let") == DegenerateReason.NAMES_NOTHING
    assert degenerate("?") == DegenerateReason.NO_TITLE
    assert degenerate("Show that $\\frac{a}{b") == DegenerateReason.DOES_NOT_TYPESET
    assert degenerate("Show that $a &= b$") == DegenerateReason.DOES_NOT_TYPESET
    assert (
        degenerate("![[_attachments/Pasted image 20210517.png]]")
        == DegenerateReason.IMAGE_NOT_TITLE
    )
    assert (
        degenerate("**Main Idea**: deformation retract")
        == DegenerateReason.MARKDOWN_MARKUP
    )


def test_degenerate_leaves_the_authors_own_naming_alone() -> None:
    """`Excision` is short, and it is exactly what that card is called."""
    assert degenerate("Excision") == DegenerateReason.NAMES_NOTHING
    assert degenerate("Excision", authored="Excision") is None


def test_a_title_of_mathematics_alone_is_not_degenerate() -> None:
    """`/problems.html` typesets its row titles, so a formula reads as a formula."""
    assert degenerate("Compute $H_*(\\RP^2 \\times \\RP^2; \\ZZ)$") is None


def test_the_body_splitter_still_treats_an_enumerator_as_statement() -> None:
    """Fold a bare `a.` into `NOT_A_TITLE` and part (a) loses its label to the page."""
    assert not NOT_A_TITLE.match("a.")
    assert not NOT_A_TITLE.match("\\[")
    assert NOT_A_TITLE.match("\\envlist")
