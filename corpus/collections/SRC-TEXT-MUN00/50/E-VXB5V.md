---
schema: qual/card@1
id: E-VXB5V
kind: problem
title: Discrete spaces have dimension zero
classification:
  areas:
  - topology
  topics:
  - Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'The source claim needs a nonempty space when the empty space has dimension -1.'
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked against Munkres, Topology (2000), §50 Exercise 1, printed p. 315, with the definitions of order and
    of topological dimension on printed p. 305: the cover by singletons refines any open cover and has order 1.
    What was corrected: the stored statement had narrowed the exercise to nonempty discrete spaces; it now
    states the exercise as printed, and the solution says why the nonempty case is what the book's definition of
    order can speak about, the empty collection having no point to count.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located proves Munkres §50 Exercise 1 (printed p. 315).
    Murayama's selection has no Chapter 8, dbFin has no chapter-8 page, and the ten GitHub repositories of
    Munkres solutions listed in COMPLAINTS.md reach no section past §36. The AoPS post *Topology by Munkres
    Chapter 8 | Day 18* (https://artofproblemsolving.com/community/c3401823h3647630) reaches §50 and its
    formulas are lost in the extraction, as recorded for the earlier posts of that blog; the site answers an
    automated request with a human check, which was not worked around. The Stack Exchange query "discrete
    space dimension zero" returned 4259332, "Prove that every topological space equipped with the discrete
    topology is zero-dimensional", which is about a base of clopen sets, the small inductive notion, and not
    about the covering dimension of §50, so it does not refine an arbitrary open cover by a cover of order 1,
    which is what the exercise asks and what the card constructs from the singletons. Nothing needed
    correction.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the argument into numbered steps. Supplied the two points the prose carried in
    passing: that the order of a refinement is at least one for a nonempty space, which is why
    dimension cannot be negative and the inequality dim X <= 0 becomes an equality, and that a
    refinement in the sense of the definition must be an open cover each of whose members lies in a
    member of the given cover, which is what the singletons are checked against. The restriction to
    nonempty spaces is the earlier correction and is kept, with its reason on the card.
---

::: {.exercise}

Show that any discrete space has dimension 0.
:::

::: {.solution}

The argument is the card's own: no complete published solution was located, and the search is recorded in the card's earlier audit events. Munkres, *Topology* (2000), §50 Exercise 1, printed p. 315, with the definitions of order and of topological dimension on printed p. 305.

Recall the definitions. A family $\mathcal V$ of subsets refines a family $\mathcal U$ when every member of $\mathcal V$ is contained in a member of $\mathcal U$; an open cover $\mathcal V$ has order at most $m$ when no point of the space lies in more than $m$ members of $\mathcal V$; and $\dim X\leq n$ when every open cover of $X$ has an open refinement of order at most $n+1$.

The book's definition of order counts the members containing a point, so it presupposes a point to count; the statement is therefore read for a nonempty space $X$, as the card's correction records.

::: pf

::: {.pf-step #singletons}
In a discrete space every subset is open, so for nonempty $X$ the family $\mathcal V=\{\{x\}\mid x\in X\}$ is an open cover.

::: pf-proof
Each singleton $\{x\}$ is a subset of $X$, hence open in the discrete topology, and every $x$ lies in its own singleton, so the family covers $X$. It is nonempty because $X$ is.
:::

:::

::: {.pf-step #refines}
$\mathcal V$ refines any given open cover $\mathcal U$ of $X$.

::: pf-proof
Let $x\in X$. The family $\mathcal U$ covers $X$, so there is $U_{x}\in\mathcal U$ with $x\in U_{x}$; then $\{x\}\subset U_{x}$, which is the refinement condition for the member $\{x\}$ of $\mathcal V$. This holds for every member of $\mathcal V$.
:::

:::

::: {.pf-step #order}
$\mathcal V$ has order $1$.

::: pf-proof
The only member of $\mathcal V$ containing $x$ is $\{x\}$, because distinct singletons are disjoint; so each point lies in exactly one member and no point lies in two. The order is the largest number of members containing a single point, namely $1$.
:::

:::

::: {.pf-step #upper}
$\dim X\leq0$.

::: pf-proof
Given an open cover $\mathcal U$, steps [](#singletons){.pf-ref}, [](#refines){.pf-ref} and [](#order){.pf-ref} produce an open refinement of order $1$, which is order $\leq 0+1$; since $\mathcal U$ was arbitrary, $\dim X\leq0$ by the definition.
:::

:::

::: {.pf-step #lower}
$\dim X\geq0$ for nonempty $X$, so $\dim X=0$.

::: pf-proof
If $\mathcal V$ is a cover of a nonempty space then some member contains a point $x$, so the order of $\mathcal V$ is at least $1$; hence no open cover has a refinement of order at most $0$ and $\dim X\leq-1$ fails. With step [](#upper){.pf-ref}, the dimension is $0$. The empty space, having no point to count, is assigned dimension $-1$ by convention and is excluded here.
:::

:::

:::

:::
