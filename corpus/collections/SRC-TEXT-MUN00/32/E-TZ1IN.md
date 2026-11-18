---
schema: qual/card@1
id: E-TZ1IN
kind: problem
title: Complete normality characterized by separated sets
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "Doug's World", "Munkres - Topology -
    Chapter 4 Solutions" (30 August 2017; the file names no author), the second item printed there
    under the heading "Problem 32.6", printed pp. 6-7
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf); checked against Munkres, Topology (2000),
    Section 32 Exercise 6, printed p. 205, Theorem 17.2 (closed sets in subspaces) and the printed
    hint. What was corrected: the source calls the ambient set S = X - (closure A cap closure B)
    and then asserts "the sets A' = A cap S and B' = B cap S are closed in S" and "Then V_A and V_B
    are open in X because S is open", which needs the two facts the card supplies: A is contained
    in closure A, hence in S by separatedness, so A' = S cap closure A is the trace of a closed set
    of X, and likewise for B. The converse direction is the source's.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof, and the statement's omitted hypothesis named. The reading
    found that the printed equivalence fails as stated: Munkres' normality requires one-point sets to be
    closed, and without that the separated-sets condition is vacuous on the two-point indiscrete space,
    which is not normal. The forward direction is proved in general; the converse now carries the
    hypothesis that one-point sets are closed, which the argument uses both for points of a subspace and
    for the closed sets it separates. The two directions are split into steps at the ambient-and-subspace
    closures, which the earlier prose ran together. The statement itself is unchanged. Checked against
    Munkres, Topology (2000), Section 32 Exercise 6, printed p. 205.
---

::: {.exercise}

A space $X$ is said to be completely normal if every subspace of $X$ is normal.
Show that $X$ is completely normal if and only if for every pair $A, B$ of separated sets in $X$ (that is, sets such that $\overline{A} \cap B = \varnothing$ and $A \cap \overline{B} = \varnothing$), there exist disjoint open sets containing them.
[Hint: If $X$ is completely normal, consider $X - (\overline{A} \cap \overline{B})$.]
:::

::: {.solution}

The argument follows **"Doug's World", "Munkres - Topology - Chapter 4 Solutions" (30 August 2017), the second item printed under the heading "Problem 32.6", printed pp. 6--7** (`tmp/sources/munkres-solutions-dougsworld-ch4.pdf`), whose two directions these are, with the ambient-and-subspace closures separated as below.

The exercise as printed needs one hypothesis the statement leaves implicit, and the solution names it: Munkres' *normal* requires one-point sets to be closed (§31, printed p. 195), so the implication from the separated-sets condition back to complete normality requires one-point sets to be closed in $X$. Without it the condition is vacuous on some spaces that are not normal: in the two-point indiscrete space no two nonempty sets are separated, both closures being the whole space, yet that space is not normal, its points not being closed, and it is a subspace of itself. The forward implication needs no such hypothesis, and with one-point sets closed the two are equivalent, which is the content of the exercise for the spaces the book considers.

The statement was checked against Munkres, *Topology* (2000), §32 Exercise 6, printed p. 205, with the definition of normality in §31 (printed p. 195) and Theorems 17.2 and 17.4. Throughout, $X$ is a space, $\overline{A}$ is the closure of $A$ in $X$, $\overline{A}^{Y}$ is its closure in a subspace $Y$, and $A$ and $B$ are *separated* when $\overline{A}\cap B=\varnothing$ and $A\cap\overline{B}=\varnothing$.

::: pf

::: {.pf-step #forward}

If $X$ is completely normal, then every pair of separated sets in $X$ has disjoint open neighbourhoods.

:::: pf-proof

Let $A,B$ be separated subsets of $X$. The hint of the exercise directs attention to the subspace $Y\coloneqq X-(\overline{A}\cap\overline{B})$.

::: {.pf-step #inside}

$A\subset Y$ and $B\subset Y$, where $Y\coloneqq X-(\overline{A}\cap\overline{B})$.

::: pf-proof

Since $A\cap\overline{B}=\varnothing$ one has $A\cap(\overline{A}\cap\overline{B})=\varnothing$, so $A\subset Y$; and $B\cap\overline{A}=\varnothing$ gives $B\subset Y$ in the same way.

:::

:::

::: {.pf-step #closed-in-Y}

$Y$ is open in $X$, and $\overline{A}\cap Y$ and $\overline{B}\cap Y$ are disjoint closed subsets of $Y$.

::: pf-proof

$\overline{A}\cap\overline{B}$ is closed in $X$, being an intersection of closed sets, so its complement $Y$ is open. The sets $\overline{A}$ and $\overline{B}$ are closed in $X$, so their intersections with $Y$ are closed in $Y$ (Theorem 17.2). They are disjoint, because a common point would lie in $\overline{A}\cap\overline{B}$ and in its complement.

:::

:::

::: {.pf-step #normal-in-Y}

There are disjoint sets $U^{\prime},V^{\prime}$, open in $Y$, with $\overline{A}\cap Y\subset U^{\prime}$ and $\overline{B}\cap Y\subset V^{\prime}$.

::: pf-proof

$Y$ is a subspace of the completely normal space $X$, hence normal; and $Y$ contains the two disjoint closed subsets $\overline{A}\cap Y$ and $\overline{B}\cap Y$, which by step [](#inside){.pf-ref} contain $A$ and $B$ respectively. Normality of $Y$ gives disjoint open-in-$Y$ sets about them.

:::

:::

::: {.pf-step #open-in-X}

$U^{\prime}$ and $V^{\prime}$ are open in $X$.

::: pf-proof

$Y$ is open in $X$ by step [](#closed-in-Y){.pf-ref}, and a set open in an open subspace is open in the space: by the definition of the subspace topology (§16, printed p. 88) $U^{\prime}=Y\cap O$ for some open $O\subset X$, and that intersection of open sets is open.

:::

:::

::: pf-step

Disjoint open sets of $X$ contain $A$ and $B$.

::: pf-proof

By steps [](#open-in-X){.pf-ref} and [](#inside){.pf-ref} the sets $U^{\prime}$ and $V^{\prime}$ are disjoint open sets of $X$ with $A\subset\overline{A}\cap Y\subset U^{\prime}$ and $B\subset V^{\prime}$.

:::

:::

::::

:::

::: {.pf-step #converse}

If every pair of separated sets in $X$ has disjoint open neighbourhoods and one-point sets in $X$ are closed, then $X$ is completely normal.

:::: pf-proof

Assume those two hypotheses and let $Y$ be a subspace of $X$.

::: {.pf-step #separated}

For a subspace $Y\subset X$ and disjoint closed subsets $A,B$ of $Y$, the sets $A$ and $B$ are separated in $X$.

::: pf-proof

Because $A$ is closed in $Y$ it equals its closure in $Y$, and the closure in $Y$ is the trace of the closure in $X$: $A=\overline{A}^{Y}=Y\cap\overline{A}$ (Theorem 17.4). Since $B\subset Y$, one has $B\cap\overline{A}=B\cap(Y\cap\overline{A})=B\cap A=\varnothing$; and symmetrically $A\cap\overline{B}=\varnothing$ from $B=Y\cap\overline{B}$. So $A$ and $B$ are separated in $X$.

:::

:::

::: {.pf-step #neighbourhoods}

There are disjoint open sets $U,V$ of $X$ with $A\subset U$ and $B\subset V$.

::: pf-proof

This is the hypothesis on separated pairs, applied to step [](#separated){.pf-ref}.

:::

:::

::: {.pf-step #traces}

$U\cap Y$ and $V\cap Y$ are disjoint open sets of $Y$ containing $A$ and $B$.

::: pf-proof

Intersections of open sets of $X$ with $Y$ are open in $Y$; they are disjoint because $U\cap V=\varnothing$; and they contain $A$ and $B$ because $A,B\subset Y$.

:::

:::

::: {.pf-step #points}

One-point sets in $Y$ are closed.

::: pf-proof

For $y\in Y$ the set $\theset{y}$ is closed in $X$ by hypothesis, so $Y\cap\theset{y}=\theset{y}$ is closed in $Y$ (Theorem 17.2).

:::

:::

::: pf-step

Every subspace $Y$ of $X$ is normal, so $X$ is completely normal.

::: pf-proof

Let $A,B$ be disjoint closed subsets of $Y$. Steps [](#traces){.pf-ref} and [](#points){.pf-ref} give disjoint open sets of $Y$ containing them and the closedness of one-point sets in $Y$; those are the two clauses of the definition of normality (§31, printed p. 195), so $Y$ is normal. As $Y$ was arbitrary, every subspace is normal.

:::

:::

::::

:::

::: pf-step

Therefore, for spaces with closed one-point sets, $X$ is completely normal if and only if every pair of separated sets in $X$ has disjoint open neighbourhoods.

::: pf-proof

Step [](#forward){.pf-ref} is the implication from complete normality to the separated-sets condition, and needs no hypothesis beyond complete normality. Step [](#converse){.pf-ref} is the converse, under the closedness of one-point sets that the definition of normality requires and that complete normality itself supplies, since $X$ is a subspace of $X$. So the equivalence holds for every space in the sense of the book, and the counterexample in the introduction is what the condition fails to exclude when the closedness of one-point sets is dropped.

:::

:::

:::

:::
