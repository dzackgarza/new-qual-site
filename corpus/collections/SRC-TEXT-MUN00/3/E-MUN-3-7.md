---
schema: qual/card@1
id: E-MUN-3-7
kind: problem
title: The restriction of an order relation is an order relation
classification:
  areas:
  - topology
  topics:
  - Relations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §3 Exercise 7, printed p. 29; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.7,
    printed pp. 26-27 (tmp/sources/munkres-solutions-whitman.pdf). The restriction here
    is < cap (A_0 x A_0), the same definition as in Exercise 2, and the three checks are
    his.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose into numbered steps; the three checks are Whitman's (Exercise 3.7,
    printed pp. 26-27), as the card cites. Checked: trichotomy, nonreflexivity and transitivity of
    the restricted relation, each against the definition. Not checked: the cited pages, because
    tmp/sources holds no copy of the Whitman manual and the Munkres text is not retained in this
    VM (ad-text-mun00 is blocked), so the printed exercise was not re-read.
---

::: {.exercise}

Show that the restriction of an order relation is an order relation.
:::

::: {.solution}

The argument is that of the retained published solution: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.7, printed ps 26-27, which the card cites; it is restructured into numbered steps below. Here an order relation on a set is a relation that is transitive, and satisfies trichotomy: for distinct $x,y$ exactly one of $x<y$, $y<x$ holds; the restriction to $A_0\subset A$ is $\prec\;=\;<\cap(A_0\times A_0)$.

::: pf

::: {.pf-step #rel}

$\prec$ is a relation on $A_0$.

::: pf-proof

It is a subset of $A_0\times A_0$ by construction.

:::

:::

::: {.pf-step #trich}

$\prec$ is trichotomous.

::: pf-proof

Let $x\neq y$ in $A_0$. They are distinct elements of $A$ and $<$ is trichotomous on $A$, so exactly one of $x<y$, $y<x$ holds; since $x,y\in A_0$, that pair also lies in $A_0\times A_0$, so exactly one of $x\prec y$, $y\prec x$ holds.

:::

:::

::: {.pf-step #nonref}

$\prec$ is nonreflexive.

::: pf-proof

For $x\in A_0$, $x\in A$ and $<$ is nonreflexive, so not $x<x$, that is $(x,x)\notin\,<$; hence $(x,x)\notin\prec$.

:::

:::

::: {.pf-step #trans}

$\prec$ is transitive.

::: pf-proof

If $x\prec y$ and $y\prec z$ then $x<y$ and $y<z$, so $x<z$ by transitivity of $<$; and $x,z\in A_0$ gives $(x,z)\in A_0\times A_0$, hence $x\prec z$.

:::

:::

::: {.pf-step #done}

$\prec$ is an order relation on $A_0$.

::: pf-proof

Steps [](#trich){.pf-ref}, [](#nonref){.pf-ref} and [](#trans){.pf-ref}.

:::

:::

:::

:::
