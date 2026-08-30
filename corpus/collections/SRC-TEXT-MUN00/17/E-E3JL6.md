---
schema: qual/card@1
id: E-E3JL6
kind: exercise
title: Products of Hausdorff spaces are Hausdorff
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}

Show that the product of two Hausdorff spaces is Hausdorff.
:::

::: solution
**Goal:** Separate points in $X\times Y$ by product neighborhoods.

<1> Let $(x_1,y_1)\neq (x_2,y_2)$.
    If $x_1\neq x_2$, since $X$ is Hausdorff there exist disjoint open sets $U_1,U_2\subseteq X$
    with $x_i\in U_i$.
    Then $U_1\times Y$ and $U_2\times Y$ are disjoint open neighborhoods of the two points in $X\times Y$.

<1> If $x_1=x_2$, then $y_1\neq y_2$.
    By Hausdorffness of $Y$, choose disjoint open sets $V_1,V_2\subseteq Y$ with $y_i\in V_i$.
    Then $X\times V_1$ and $X\times V_2$ are disjoint neighborhoods of the points.

<1> In both cases, distinct points have disjoint neighborhoods. Therefore $X\times Y$ is Hausdorff.

Authored by **Codex 5.3 Spark Extra High**.
:::
