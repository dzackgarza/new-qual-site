---
schema: qual/card@1
id: E-HAT-1.2-5
kind: problem
title: Fundamental group of planar graph is free on boundary loops of complementary regions
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Free Groups
  - Planar Graphs
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $X \subset \mathbb{R}^2$ be a connected graph that is the union of a finite number of straight line segments.
Show that $\pi_1(X)$ is free with a basis consisting of loops formed by the boundaries of the bounded complementary regions of $X$, joined to a basepoint by suitably chosen paths in $X$.
[Assume the Jordan curve theorem for polygonal simple closed curves, which is equivalent to the case that $X$ is homeomorphic to $S^1$.]
:::

::: {.solution}

::: pf

::: pf-step

$X$ is a finite connected graph, so $\pi_1(X)$ is a free group.

::: pf-proof

the fundamental group of a finite connected graph is free (a graph is homotopy equivalent to a wedge of circles).

:::

:::

::: {.pf-step #s2}

The rank of $\pi_1(X)$ equals the number of bounded complementary regions of $X$.

::: pf-proof

::: pf-step

Let $V$ be the number of vertices and $E$ the number of edges of $X$.

::: pf-proof

setup.

:::

:::

::: {.pf-step #s2-2}

$X$ is homotopy equivalent to a wedge of $E - V + 1$ circles.

::: pf-proof

a connected graph with $V$ vertices and $E$ edges is homotopy equivalent to a wedge of $E - V + 1$ circles (collapse a maximal tree).

:::

:::

::: {.pf-step #s2-3}

By Euler's formula for planar graphs, the number of bounded complementary regions is $E - V + 1$.

::: pf-proof

for a connected planar graph, $V - E + F = 2$ where $F$ is the number of faces (including the unbounded one); the number of bounded faces is $F - 1 = E - V + 1$.

:::

:::

::: pf-step

Hence the rank of $\pi_1(X)$ equals the number of bounded complementary regions.

::: pf-proof

Steps [](#s2-2){.pf-ref} and [](#s2-3){.pf-ref}.

:::

:::

:::

:::

::: pf-step

The boundary of each bounded complementary region is a simple closed polygonal curve, hence a loop in $X$.

::: pf-proof

the boundary of a bounded face of a planar graph is a simple closed curve (by the Jordan curve theorem for polygonal curves).

:::

:::

::: {.pf-step #s4}

These boundary loops, joined to a basepoint by paths in $X$, form a free basis of $\pi_1(X)$.

::: pf-proof

::: pf-step

The boundary loops of the bounded regions are independent in $\pi_1(X)$.

::: pf-proof

they correspond to the generators of the free group (each bounded region contributes one generator).

:::

:::

::: pf-step

They generate $\pi_1(X)$.

::: pf-proof

the number of bounded regions equals the rank (step [](#s2){.pf-ref}), and the boundary loops are independent, so they form a basis.

:::

:::

:::

:::

::: pf-qed

Step [](#s4){.pf-ref}.

:::

:::

:::
