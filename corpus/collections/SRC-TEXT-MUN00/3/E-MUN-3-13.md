---
schema: qual/card@1
id: E-MUN-3-13
kind: problem
title: The least upper bound property implies the greatest lower bound property
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
    Read against Munkres, Topology (2000), §3 Exercise 13, printed p. 29; the exercise
    prints the theorem "if an ordered set A has the least upper bound property, then it
    has the greatest lower bound property" and asks for the proof. The stored statement
    matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.13,
    printed p. 35 (tmp/sources/munkres-solutions-whitman.pdf). His proof through the set
    B_0 of lower bounds is the one below.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose into numbered steps; the argument through the set of lower bounds
    is Whitman's (Exercise 3.13, printed p. 35), as the card cites. Checked: nonemptiness and
    boundedness of B_0, the two halves of the greatest-lower-bound claim, and that the two uses of
    the least upper bound property are legitimate. Not checked: the cited page, because
    tmp/sources holds no copy of the Whitman manual and the Munkres text is not retained in this
    VM.
---

::: {.exercise}

Prove the following:

Theorem. If an ordered set $A$ has the least upper bound property, then it has the greatest lower bound property.
:::

::: {.solution}

The argument is that of the retained published solution: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.13, printed p 35, which the card cites; it is restructured into numbered steps below. Here $A$ is an ordered set; a subset is bounded below if it has a lower bound in $A$, and the greatest lower bound property is that every nonempty bounded-below subset has a greatest lower bound.

::: pf

::: {.pf-step #bounded}

$B_0$ is nonempty and bounded above.

::: pf-proof

By hypothesis $A_0$ has a lower bound, which lies in $B_0$; and for any $a\in A_0$, every $x\in B_0$ satisfies $x\leq a$, so $a$ is an upper bound of $B_0$.

:::

:::

::: {.pf-step #sup}

$c\coloneqq\sup B_0$ exists.

::: pf-proof

The least upper bound property applies to the nonempty, bounded-above set $B_0$.

:::

:::

::: {.pf-step #lower}

$c$ is a lower bound of $A_0$.

::: pf-proof

Let $x\in A_0$. Every $y\in B_0$ satisfies $y\leq x$, so $x$ is an upper bound of $B_0$; since $c$ is the least upper bound, $c\leq x$.

:::

:::

::: {.pf-step #greatest}

$c$ is the greatest lower bound of $A_0$.

::: pf-proof

Let $y$ be a lower bound of $A_0$. Then $y\in B_0$, and $c$ is an upper bound of $B_0$, so $y\leq c$; hence $c$ is a lower bound by step [](#lower){.pf-ref} and every lower bound is below it.

:::

:::

::: {.pf-step #done}

$A$ has the greatest lower bound property.

::: pf-proof

Let $A_0\subset A$ be nonempty and bounded below; steps [](#bounded){.pf-ref} to [](#greatest){.pf-ref} produce its greatest lower bound $c$.

:::

:::

:::

:::
