---
schema: qual/card@1
id: E-HAT-1.2-5
kind: exercise
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

Let $X \subset \mathbb{R}^2$ be a connected graph that is the union of a finite number of straight line segments.
Show that $\pi_1(X)$ is free with a basis consisting of loops formed by the boundaries of the bounded complementary regions of $X$, joined to a basepoint by suitably chosen paths in $X$.
[Assume the Jordan curve theorem for polygonal simple closed curves, which is equivalent to the case that $X$ is homeomorphic to $S^1$.]

::: {.solution}
<1>1. $X$ is a finite connected graph, so $\pi_1(X)$ is a free group.
Proof: the fundamental group of a finite connected graph is free (a graph is homotopy equivalent to a wedge of circles).

<1>2. The rank of $\pi_1(X)$ equals the number of bounded complementary regions of $X$.
<2>1. Let $V$ be the number of vertices and $E$ the number of edges of $X$.
Proof: setup.
<2>2. $X$ is homotopy equivalent to a wedge of $E - V + 1$ circles.
Proof: a connected graph with $V$ vertices and $E$ edges is homotopy equivalent to a wedge of $E - V + 1$ circles (collapse a maximal tree).
<2>3. By Euler's formula for planar graphs, the number of bounded complementary regions is $E - V + 1$.
Proof: for a connected planar graph, $V - E + F = 2$ where $F$ is the number of faces (including the unbounded one); the number of bounded faces is $F - 1 = E - V + 1$.
<2>4. Hence the rank of $\pi_1(X)$ equals the number of bounded complementary regions.
Proof: <2>2 and <2>3.

<1>3. The boundary of each bounded complementary region is a simple closed polygonal curve, hence a loop in $X$.
Proof: the boundary of a bounded face of a planar graph is a simple closed curve (by the Jordan curve theorem for polygonal curves).

<1>4. These boundary loops, joined to a basepoint by paths in $X$, form a free basis of $\pi_1(X)$.
<2>1. The boundary loops of the bounded regions are independent in $\pi_1(X)$.
Proof: they correspond to the generators of the free group (each bounded region contributes one generator).
<2>2. They generate $\pi_1(X)$.
Proof: the number of bounded regions equals the rank (<1>2), and the boundary loops are independent, so they form a basis.

<1>5. Q.E.D.
Proof: <1>4.
:::
