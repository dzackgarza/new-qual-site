---
schema: qual/card@1
id: E-YZWG5
kind: problem
title: Separating disjoint compact sets in a Hausdorff space
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 5, printed p. 171, with Lemma 26.4;
    the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.5, PDF pp. 12-13. Lemma 26.4 at each point of A
    gives disjoint open sets, and finitely many of them cover the compact A; the union of
    the one side and the intersection of the other are disjoint open sets around A and B.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $A$ and $B$ be disjoint compact subspaces of the Hausdorff space $X$.
Show that there exist disjoint open sets $U$ and $V$ containing $A$ and $B$, respectively.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.5, PDF pp. 12--13** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

Let $A,B$ be disjoint compact subspaces of the Hausdorff space $X$. For each $x\in A$, Lemma 26.4 gives disjoint open sets $U_{x}\ni x$ and $V_{x}\supset B$. The $U_{x}$ cover the compact $A$, so $A\subset U_{x_{1}}\cup\cdots\cup U_{x_{n}}$ for finitely many points. Put
$$
U=U_{x_{1}}\cup\cdots\cup U_{x_{n}},\qquad V=V_{x_{1}}\cap\cdots\cap V_{x_{n}} .
$$
Then $U\ni A$ and $V\supset B$ are open, and they are disjoint: a point $c\in U\cap V$ lies in some $U_{x_{i}}$ and in $V\subset V_{x_{i}}$, contradicting $U_{x_{i}}\cap V_{x_{i}}=\varnothing$.
:::
