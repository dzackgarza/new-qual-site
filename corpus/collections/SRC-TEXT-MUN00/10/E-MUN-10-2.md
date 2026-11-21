---
schema: qual/card@1
id: E-MUN-10-2
kind: problem
title: Immediate successors in well-ordered sets
classification:
  areas:
  - topology
  topics:
  - Well-Ordered Sets
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §10 Exercise 2, printed p. 67; both parts are
    stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 10.2, printed p. 108.
    (a) is his: the set of elements above a is nonempty because a is not the largest, and
    its smallest element has nothing strictly between it and a. (b) is his example Z with
    the usual order, in which n+1 is an immediate successor of n, while the negative
    integers have no smallest element.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the set of elements above a with its least
    element, the absence of anything strictly between, and Z with its usual order as the
    counterexample. The exercise was re-read in the book's text at
    tmp/sources/munkres-2000-topology.md and stands on printed p. 67 as the card records.
    The retained solution's cited page was not re-read in this pass.
---

::: {.exercise}

(a) Show that in a well-ordered set, every element except the largest (if one exists) has an immediate successor.

(b) Find a set in which every element has an immediate successor that is not well-ordered.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.2, printed p. 108** (`tmp/sources/munkres-solutions-whitman.pdf`); (a) is his, the set of elements above $a$ being nonempty because $a$ is not the largest, and (b) is his example, $\ZZ$ with the usual order.

Notation: an order relation $<$ on $A$ is a well-ordering when every nonempty subset of $A$ has a least element, and $b$ is an immediate successor of $a$ when $a<b$ and no $z\in A$ satisfies $a<z<b$.

::: pf

::: {.pf-step #successor}
(a) If $A$ is well ordered by $<$ and $a\in A$ is not the largest element, then $a$ has an immediate successor.

::: pf-proof
The elements above $a$ form a nonempty subset with a least element, and that element is the immediate successor.

::: {.pf-step #above}
$X=\{y\in A\mid a<y\}$ is a nonempty subset of $A$ with a least element $b$.

::: pf-proof
Because $a$ is not the largest element there is $x\in A$ with $a<x$, and then $x\in X$; so $X\ne\varnothing$. Since $A$ is well ordered and $X\subseteq A$ is nonempty, $X$ has a least element, which we call $b$.
:::

:::

::: {.pf-step #nothing-between}
$a<b$, and there is no $z\in A$ with $a<z<b$; so $b$ is an immediate successor of $a$.

::: pf-proof
$b\in X$, so $a<b$ by the definition of $X$. If $z\in A$ had $a<z<b$, then $z\in X$ and $z<b$, contradicting the minimality of $b$ in $X$.
:::

:::

:::

:::

::: {.pf-step #integers}
(b) In $\ZZ$ with the usual order every element has an immediate successor, and $\ZZ$ is not well ordered.

::: pf-proof
For $n\in\ZZ$ the integer $n+1$ satisfies $n<n+1$, and no integer $z$ satisfies $n<z<n+1$: if $z\ge n+1$ or $z\le n$ then $z$ is not strictly between them, and there is no other possibility for an integer. So $n+1$ is an immediate successor of $n$, and every element of $\ZZ$ has one. But $\ZZ$ is not well ordered: the set $\ZZ_{-}=\{n\in\ZZ\mid n<0\}$ is a nonempty subset of $\ZZ$ with no least element, since for every negative $n$ the integer $n-1$ is negative and smaller. So a set in which every element has an immediate successor need not be well ordered, as (b) demands.
:::

:::

:::
:::
