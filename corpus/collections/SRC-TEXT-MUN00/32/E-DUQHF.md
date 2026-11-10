---
schema: qual/card@1
id: E-DUQHF
kind: problem
title: Closed subspaces of normal spaces are normal
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: Ana Emilia de Orellana, "Solutions -
    Topology Munkres", Section 32 Exercise 1, printed p. 33
    (tmp/sources/munkres-solutions-anadeore.pdf), checked against Munkres, Topology (2000),
    Section 32 Exercise 1, printed p. 205, and Theorem 17.3 (a set closed in a closed subspace is
    closed in the space). "Doug's World", "Munkres - Topology - Chapter 4 Solutions" (30 August
    2017), does not treat this exercise: its Section 32 begins at printed p. 6 with Problem 32.3. What was corrected: Orellana writes "A = Ã cap Y and B = B̃ cap Y with Ã,
    B̃ closed sets in X" and then jumps to the disjoint open sets of X, omitting the observation that
    Ã and B̃ may be taken to be A and B themselves because Y is closed; the card makes that step.
    Orellana's is the only located proof of the exercise.
---

::: {.exercise}

Show that a closed subspace of a normal space is normal.
:::

::: {.solution}
Let $X$ be normal and let $Y \subseteq X$ be closed.

::: pf

::: pf-step
$Y$ is $T_1$.

::: pf-proof
Each singleton is closed in $X$, so its intersection with $Y$ is closed in $Y$.
:::

:::

::: pf-step
Any two disjoint closed subsets $A, B$ of $Y$ have disjoint open neighborhoods in $Y$, so $Y$ is normal.

::: pf-proof

::: pf-step
$A$ and $B$ are closed in $X$.

::: pf-proof
$A$ is closed in $Y$ and $Y$ is closed in $X$, so $A$ is closed in $X$; the same holds for $B$.
:::

:::

::: pf-step
There are disjoint open sets $U, V \subseteq X$ with $A \subseteq U$ and $B \subseteq V$.

::: pf-proof
$A$ and $B$ are disjoint closed sets in the normal space $X$.
:::

:::

::: pf-step
$U \cap Y$ and $V \cap Y$ are disjoint open sets in $Y$ that contain $A$ and $B$.

::: pf-proof
They are open in the subspace topology, disjoint because $U \cap V = \varnothing$, and contain $A$ and $B$ because $A, B \subseteq Y$.
:::

:::

:::

:::

:::

:::
