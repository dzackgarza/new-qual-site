---
schema: qual/card@1
id: P-TOPS25A
kind: problem
title: Fundamental group of the 2-sphere minus ten points
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: source-checked
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Let $X = S^2 \setminus \{p_1, p_2, \dots, p_{10}\}$ be the topological space obtained by removing 10 distinct points from the 2-sphere $S^2$.
Compute its **fundamental group** $\pi_1(X, x_0)$.
:::

::: solution
<1>1. Choose one deleted point, say $p_{10}$, as the point at infinity for stereographic projection.
<2>1. Stereographic projection gives a homeomorphism
$$
S^2\setminus\{p_{10}\}\cong\mathbb R^2.
$$
<2>2. Under this homeomorphism the other nine deleted points become distinct points $q_1,\dots,q_9\in\mathbb R^2$. Hence
$$
X\cong \mathbb R^2\setminus\{q_1,\dots,q_9\}.
$$

<1>2. The punctured plane $\mathbb R^2\setminus\{q_1,\dots,q_9\}$ is homotopy equivalent to a wedge of nine circles.
<2>1. Choose pairwise disjoint small closed disks $D_i$ centered at $q_i$, and choose a basepoint $x_0$ outside all of them.
<2>2. Join $x_0$ to one point of each boundary circle $\partial D_i$ by embedded arcs whose interiors are pairwise disjoint and avoid the disks.
<2>3. A sufficiently large closed disk containing this configuration, with the interiors of the $D_i$ removed, deformation retracts onto the union of the nine circles $\partial D_i$ and the connecting arcs. Collapsing the tree formed by the connecting arcs gives a wedge $\bigvee_{i=1}^9 S^1$.
<2>4. The complement of the large disk contributes only an outer collar, so the whole punctured plane has the same homotopy type. Therefore
$$
X\simeq \bigvee_{i=1}^9 S^1.
$$

<1>3. By Seifert--van Kampen,
$$
\pi_1(X,x_0)\cong \pi_1\!\left(\bigvee_{i=1}^9 S^1\right)\cong F_9,
$$
the free group on nine generators.
:::
