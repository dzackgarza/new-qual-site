---
schema: qual/card@1
id: E-OLLMN
kind: problem
title: Closed subsets of closed subspaces are closed
classification:
  areas:
  - topology
  topics:
  - Closed Sets
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 2, printed p. 100, with Theorem 17.2
    on printed p. 95; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 17.2, PDF p. 6. A closed-in-Y set is Y cap C with
    C closed in X (Theorem 17.2), and an intersection of two closed sets of X is closed.
    (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Show that if $A$ is closed in $Y$ and $Y$ is closed in $X$, then $A$ is closed in $X$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 17.2, PDF p. 6** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the one-line argument is theirs. Whitman proves the same thing on his printed p. 159 by exhibiting $X-A$ as a union of two open sets.

Since $A$ is closed in the subspace $Y$, Theorem 17.2 (printed p. 95) gives a set $C$ closed in $X$ with $A=Y\cap C$. Both $Y$ (by hypothesis) and $C$ are closed in $X$, and an intersection of closed sets is closed (Theorem 17.1, printed p. 95); hence $A$ is closed in $X$.
:::
