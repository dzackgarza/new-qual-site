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
---

::: {.exercise}

Let $X$ be a topological space; let $A$ be a subset of $X$.
Suppose that for each $x \in A$ there is an open set $U$ containing $x$ such that $U \subset A$.
Show that $A$ is open in $X$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 13.1, printed p. 141** (`tmp/sources/munkres-solutions-whitman.pdf`); the proof is his.

For each $x\in A$ choose an open set $U_{x}$ of $X$ with $x\in U_{x}$ and $U_{x}\subset A$, as the hypothesis allows. We claim
$$
\bigcup_{x\in A}U_{x}=A .
$$
If $y\in\bigcup_{x\in A}U_{x}$ then $y\in U_{x}$ for some $x\in A$, and $U_{x}\subset A$, so $y\in A$. Conversely, if $y\in A$ then $y\in U_{y}$, so $y$ lies in the union. Hence $A$ is a union of open sets of $X$, and therefore $A$ is open in $X$, since a topology is closed under arbitrary unions.
:::
