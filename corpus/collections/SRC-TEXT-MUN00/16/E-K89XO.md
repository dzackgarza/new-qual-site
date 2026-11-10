---
schema: qual/card@1
id: E-K89XO
kind: problem
title: Projections from a product are open maps
classification:
  areas:
  - topology
  topics:
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §16 Exercise 4, printed p. 92, with the
    definition of the product topology and Theorem 15.1 on printed p. 87; the stored
    statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 16.4, printed p. 152.
    The proof is his: a point of pi_1(U) has a product basis element A x B around it inside
    U, and then the whole of A projects into pi_1(U). pi_2 is the same argument.
    (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

A map $f: X \to Y$ is said to be an open map if for every open set $U$ of $X$, the set $f(U)$ is open in $Y$.
Show that $\pi_1: X \times Y \to X$ and $\pi_2: X \times Y \to Y$ are open maps.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 16.4, printed p. 152** (`tmp/sources/munkres-solutions-whitman.pdf`); the proof for $\pi_{1}$ is his, and $\pi_{2}$ is the same argument with the roles of the factors exchanged.

Let $U$ be open in $X\times Y$ and let $x\in\pi_{1}(U)$. Choose $y\in Y$ with $(x,y)\in U$. By the definition of the product topology there is a basis element $A\times B$, with $A$ open in $X$ and $B$ open in $Y$, such that $(x,y)\in A\times B\subset U$. Then $x\in A$, and for every $x'\in A$ the point $(x',y)$ lies in $A\times B\subset U$, so $x'=\pi_{1}(x',y)\in\pi_{1}(U)$. Hence
$$
x\in A\subset\pi_{1}(U),
$$
and $A$ is an open set of $X$ containing $x$. As $x\in\pi_{1}(U)$ was arbitrary, $\pi_{1}(U)$ is a union of open sets of $X$ and is open in $X$. So $\pi_{1}$ is an open map, and by the same argument with the two factors interchanged so is $\pi_{2}$.
:::
