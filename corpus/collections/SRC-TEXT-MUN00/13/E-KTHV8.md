---
schema: qual/card@1
id: E-KTHV8
kind: problem
title: Sets containing a neighborhood of each of their points are open
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §13 Exercise 1, printed p. 83; the stored
    statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 13.1, printed p. 141.
    The content is his: the chosen open sets U_x cover A, so A is a union of open sets and
    therefore open. Nothing else is used. (tmp/sources/munkres-solutions-whitman.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps and re-checked every step: the union claim against the
    printed exercise (Munkres §13 Exercise 1, printed p. 83) and Whitman's text of Exercise
    13.1 at printed p. 141. Nothing outside that argument is used; the printed statement
    needed no repair.
---

::: {.exercise}

Let $X$ be a topological space; let $A$ be a subset of $X$.
Suppose that for each $x \in A$ there is an open set $U$ containing $x$ such that $U \subset A$.
Show that $A$ is open in $X$.
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 13.1, printed p. 141** (`tmp/sources/munkres-solutions-whitman.pdf`); the argument below is his, with the selection of the sets $U_x$ stated as its own step.

::: pf

::: {.pf-step #choice}
For each $x\in A$ there is an open set $U_{x}$ of $X$ with $x\in U_{x}$ and $U_{x}\subset A$.

::: pf-proof
The hypothesis states exactly this: for each $x\in A$ there is an open set $U$ of $X$ containing $x$ with $U\subset A$. Fix such a $U$ for each $x$ and call it $U_{x}$; the choice is made once, independently at each $x$.
:::

:::

::: {.pf-step #union}
$\bigcup_{x\in A}U_{x}=A$.

::: pf-proof
If $y\in\bigcup_{x\in A}U_{x}$, then $y\in U_{x}$ for some $x\in A$, and $U_{x}\subset A$ by step [](#choice){.pf-ref}, so $y\in A$. If conversely $y\in A$, then $y\in U_{y}$ by step [](#choice){.pf-ref}, so $y$ lies in the union. Each inclusion was shown for an arbitrary element of its left-hand side, so the two sets are equal.
:::

:::

::: {.pf-step #open}
$A$ is open in $X$.

::: pf-proof
By step [](#union){.pf-ref}, $A$ is the union of the family $(U_{x})_{x\in A}$ of subsets of $X$, and by step [](#choice){.pf-ref} every member of that family is open in $X$. A topology is closed under the union of any subcollection, so $A$ is open in $X$.
:::

:::

:::
:::
