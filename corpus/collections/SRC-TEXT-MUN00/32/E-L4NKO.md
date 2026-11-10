---
schema: qual/card@1
id: E-L4NKO
kind: problem
title: Locally compact Hausdorff spaces are regular
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "Doug's World", "Munkres - Topology -
    Chapter 4 Solutions" (30 August 2017; the file names no author), Problem 32.3, printed p. 6
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf); checked against Munkres, Topology (2000),
    Section 32 Exercise 3, printed p. 205, Theorem 32.3 (a compact Hausdorff space is normal),
    Theorem 29.1 and Theorem 31.2(b) (a subspace of a regular space is regular). Its route is
    the one on the card: a compact locally compact Hausdorff space is normal by Theorem 32.3, and
    otherwise the one-point compactification is normal and the space is a subspace of it. The card
    also gives the direct route through Theorem 29.2, which is the statement the source is
    reproducing; no correction to the mathematics was needed.
---

::: {.exercise}

Show that every locally compact Hausdorff space is regular.
:::

::: {.solution}
Let $X$ be locally compact Hausdorff, let $A\subset X$ be closed, and let $x\notin A$. The open set $U=X\setminus A$ is a neighborhood of $x$. By the compact-closure neighborhood lemma from §29, there is a neighborhood $V$ of $x$ such that
$$
\overline V\text{ is compact and }\overline V\subset U.
$$
Then
$$
V\quad\text{and}\quad X\setminus\overline V
$$
are disjoint open sets containing $x$ and $A$, respectively. Thus $X$ is regular.
:::
