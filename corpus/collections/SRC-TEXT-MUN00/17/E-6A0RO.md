---
schema: qual/card@1
id: E-6A0RO
kind: problem
title: Hausdorff spaces and the closed diagonal
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 13, printed p. 101; the stored
    statement is the printed equivalence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 17.13, PDF p. 8. The complement of the diagonal is
    covered by the products of disjoint neighbourhoods, and a basis element inside that
    complement has disjoint factors. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Show that $X$ is Hausdorff if and only if the diagonal $\Delta = \theset{x \times x \mid x \in X}$ is closed in $X \times X$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 17.13, PDF p. 8** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both directions are theirs. Whitman, printed p. 165, proves the same two directions with Theorem 17.5 and Corollary 17.7 in place of the direct openness arguments.

*If $X$ is Hausdorff then $\Delta$ is closed.* It suffices to show $X\times X-\Delta$ open. Let $(x,y)\in X\times X-\Delta$, so $x\ne y$. Choose disjoint open $U\ni x$, $V\ni y$. For $(u,v)\in U\times V$ we have $u\in U$, $v\in V$ and $U\cap V=\varnothing$, so $u\ne v$; hence $(x,y)\in U\times V\subset X\times X-\Delta$, and $U\times V$ is a basis element of $X\times X$. So $X\times X-\Delta$ is open and $\Delta$ is closed.

*If $\Delta$ is closed then $X$ is Hausdorff.* Let $x\ne y$ in $X$. Then $(x,y)\in X\times X-\Delta$, which is open, so there is a basis element $U\times V$ of $X\times X$ with
$$
(x,y)\in U\times V\subset X\times X-\Delta .
$$
Here $U$ and $V$ are open in $X$, and $U\cap V=\varnothing$: a point $z\in U\cap V$ would give $(z,z)\in U\times V\subset X\times X-\Delta$ while $(z,z)\in\Delta$. So $U$ and $V$ are disjoint neighbourhoods of $x$ and $y$, and $X$ is Hausdorff.
:::
