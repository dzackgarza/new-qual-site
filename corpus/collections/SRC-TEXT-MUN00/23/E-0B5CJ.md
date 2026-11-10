---
schema: qual/card@1
id: E-0B5CJ
kind: problem
title: Punctured products of connected spaces are connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §23 Exercise 9, printed p. 152, with Theorem 23.3
    and Theorem 23.6; both sets and both properness hypotheses are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.9, PDF p. 2. Two families of T-shaped sets, one
    over the points of X - A and one over the points of Y - B, are connected and share a
    point, and their union is the complement of A x B; both inclusions are checked on the
    card. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $A$ be a proper subset of $X$, and let $B$ be a proper subset of $Y$.
If $X$ and $Y$ are connected, show that

$$
(X \times Y) - (A \times B)
$$

is connected.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.9, PDF p. 2** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the two families of T-shaped sets and their union are theirs.

Let $X,Y$ be connected and let $A\subsetneq X$, $B\subsetneq Y$ be proper; then $X-A$ and $Y-B$ are nonempty, so choose $c\times d\in(X-A)\times(Y-B)$.

For $x\in X-A$ put $U_{x}=(X\times\{d\})\cup(\{x\}\times Y)$, the union of two connected sets ($X\times\{d\}\cong X$ and $\{x\}\times Y\cong Y$) meeting in $x\times d$; by Theorem 23.3 it is connected. All the $U_{x}$ contain $c\times d$, so $U=\bigcup_{x\in X-A}U_{x}$ is connected.

Similarly, for $y\in Y-B$ the set $V_{y}=(X\times\{y\})\cup(\{c\}\times Y)$ is connected, and $V=\bigcup_{y\in Y-B}V_{y}$ is connected, all the $V_{y}$ containing $c\times d$.

Now $U\cup V$ is connected, being the union of the connected sets $U$ and $V$ which share $c\times d$, and
$$
U\cup V=(X\times Y)-(A\times B).
$$
For the inclusion $\subset$: a point of $X\times\{d\}$ has second coordinate $d\notin B$, so it is not in $A\times B$; a point of $\{x\}\times Y$ with $x\in X-A$ has first coordinate not in $A$, so it is not in $A\times B$ either; hence $U$ and similarly $V$ lie in the complement. For the inclusion $\supset$: let $(x,y)\notin A\times B$, so $x\notin A$ or $y\notin B$; in the first case $(x,y)\in\{x\}\times Y\subset U_{x}\subset U$, and in the second $(x,y)\in X\times\{y\}\subset V_{y}\subset V$.

So $(X\times Y)-(A\times B)$ is connected.
:::
