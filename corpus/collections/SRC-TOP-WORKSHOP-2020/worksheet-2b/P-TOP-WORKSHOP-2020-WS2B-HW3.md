---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2B-HW3
kind: problem
title: The mapping cylinder of a constant map $D^2\to\{y\}$ (warm-up)
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

::: solution
**Goal:** Give an explicit description of the mapping cylinder for the constant map.

<1>1. Definition: <2>1. For any map $f:X\to Y$, the mapping cylinder is $$M_f=(X\times [0,1])\sqcup Y\Big/\!\sim,$$ with $(x,1)\sim f(x)$ for every $x\in X$.
<2>2. Here $Y=\{y\}$, so every point of $D^2\times\{1\}$ is identified to the same top point $y$.
<2>3. The subset $D^2\times\{0\}$ remains the original disk, embedded as a subspace of the cylinder.

<1>2. Geometry.
<2>1. $M_f$ is the cone on $D^2$ (also called the reduced cone $D^2\ast\{y\}$). <2>2. It is homeomorphic to a 3-ball: points of $D^2\times(0,1]$ sweep all rays to the top tip $y$.
<2>3. So the mapping cylinder is a cone with base $D^2$ and a single cone apex.
:::
