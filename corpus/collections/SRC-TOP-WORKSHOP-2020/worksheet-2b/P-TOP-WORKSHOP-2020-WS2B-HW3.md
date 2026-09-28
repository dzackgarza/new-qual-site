---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2B-HW3
kind: problem
title: The mapping cylinder of a constant map $D^2\to\{y\}$
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Cell Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Let $X=D^2$, $Y=\{y\}$ a singleton, and $f:X\to Y$ be the constant function.
Construct and describe the mapping cylinder.
:::

::: {.solution}
For a map $f\colon X\to Y$, the mapping cylinder is
$$
M_f=\bigl((X\times[0,1])\sqcup Y\bigr)\big/\bigl((x,1)\sim f(x)\text{ for all }x\in X\bigr).
$$

<1>1. For $f\colon D^2\to\{y\}$, $M_f$ is the (unreduced) cone $CD^2=(D^2\times[0,1])/(D^2\times\{1\})$, which is also the join $D^2\ast\{y\}$.
::: {.proof}
Since $Y=\{y\}$, the relation identifies all of $D^2\times\{1\}$ with the single point $y$ and nothing else, which is the defining quotient of the cone. The base $D^2\times\{0\}$ is a copy of $D^2$ in $M_f$.
:::

<1>2. $M_f$ is homeomorphic to the closed $3$-ball.
::: {.proof}
Regard $D^2\subset\mathbb R^2\times\{0\}\subset\mathbb R^3$ and let $a=(0,0,1)$. The map $D^2\times[0,1]\to\mathbb R^3$, $(x,t)\mapsto(1-t)x+ta$, is continuous, collapses exactly $D^2\times\{1\}$ to $a$, and is otherwise injective, so it induces a continuous bijection from the compact space $M_f$ onto the solid cone $\{(1-t)x+ta\}$, which is Hausdorff; hence a homeomorphism. The solid cone is a compact convex subset of $\mathbb R^3$ with nonempty interior, hence homeomorphic to $D^3$.
:::
:::
