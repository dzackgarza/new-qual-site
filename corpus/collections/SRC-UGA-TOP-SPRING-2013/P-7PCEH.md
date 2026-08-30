---
schema: qual/card@1
id: P-7PCEH
kind: problem
title: Definition of deformation retract; isomorphic $\pi_1$ of the figure-eight and
  the theta space; $\pi_1$ of the theta space free on two generators
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Fundamental Group
  - Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
a. Let $A$ be a subspace of a topological space $X$.
Define what it means for $A$ to be a **deformation retract** of $X$.

b. Consider $X_1$ the "planar figure eight" and $$X_2 = S^1 \cup ({0} \times [-1, 1])$$ (the "theta space"). Show that $X_1$ and $X_2$ have isomorphic fundamental groups.

c. Prove that the fundamental group of $X_2$ is a free group on two generators.
:::

::: solution
**Goal:** Define deformation retraction and identify graph homotopy types.

<1> Part (a): a subspace $A\subseteq X$ is a deformation retract if there is a homotopy
    $H\colon X\times I\to X$
    with $H_0=\mathrm{id}_X$, $H_1(X)\subseteq A$, and $H_t|_A=\mathrm{id}_A$ for all $t$.

<1> Part (b): both $X_1$ and $X_2$ are connected 1-complexes.
    In $X_2$, contract each circular arc to a single edge, so the complex has two vertices and three edges between them.
    In $X_1$, the usual two loops already form a graph with one vertex and two loops.
    Both graphs are homotopy equivalent to a wedge of two circles, so $\pi_1(X_1)\cong\pi_1(X_2)$.

<1> Part (c): $X_2$ has $V=2$ vertices and $E=3$ edges, so for a connected graph
    $$
    \operatorname{rank}\pi_1=E-V+1=2.
    $$
    A spanning tree has one edge; the two edges not in the tree give two free generators.
    Hence $\pi_1(X_2)\cong F_2$.

Authored by **Codex 5.3 Spark Extra High**.
:::
