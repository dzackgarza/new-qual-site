---
schema: qual/card@1
id: E-TBLM7
kind: problem
title: Locally compact Hausdorff spaces are completely regular
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
    Transcribed from the located published solutions: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S33.pdf, Exercise 33.7, page 2 of the file
    (tmp/sources/munkres-solutions-poulsen-S33.pdf, Internet Archive snapshot 20200331153844), and
    "Doug's World", "Munkres - Topology - Chapter 4 Solutions", Problem 33.7, printed p. 9
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf); checked against Munkres, Topology (2000),
    Section 33 Exercise 7, printed p. 213, Theorem 29.1 (the one-point compactification is compact
    Hausdorff), Theorem 32.3 and Theorem 33.1. Moller's chain is the card's: a locally compact
    Hausdorff space is an open subspace of its compact Hausdorff one-point compactification, a
    subspace of a normal space, a subspace of a completely regular space, and a subspace of a
    completely regular space is completely regular. The card runs the same argument through
    Urysohn's lemma applied to the closed set A union {infinity}. No correction to the mathematics
    was needed.
---

::: {.exercise}

Show that every locally compact Hausdorff space is completely regular.
:::

::: {.solution}
Let $X$ be locally compact Hausdorff. Its one-point compactification $X^*=X\cup\{\infty\}$ is compact Hausdorff, hence normal.

Let $A\subset X$ be closed and $x\in X\setminus A$. The set
$$
A^*=A\cup\{\infty\}
$$
is closed in $X^*$, because its complement $X\setminus A$ is open in $X$, hence open in $X^*$ away from the point at infinity. By Urysohn's lemma there is a continuous
$$
F:X^*\to[0,1]
$$
with $F(x)=0$ and $F(A^*)=\{1\}$. Restricting $F$ to $X$ gives a continuous function separating $x$ from $A$. Therefore $X$ is completely regular.
:::
