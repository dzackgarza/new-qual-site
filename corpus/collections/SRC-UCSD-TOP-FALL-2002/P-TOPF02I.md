---
schema: qual/card@1
id: P-TOPF02I
kind: problem
title: "Manifold with trivial cup products has the cohomology of a sphere"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Let $M$ be an $n$-dimensional compact connected manifold.
Suppose all cup products vanish in $H^*(M; \mathbb{Z})$.
Prove that $H^*(M; \mathbb{Z})$ is isomorphic to $H^*(S^n; \mathbb{Z})$.
:::

::: solution
**Goal:** Use duality and the vanishing of all cup products to force the sphere cohomology ring.

<1> Let $0<i<n$. By Poincaré duality over $\mathbb Z$ (for compact connected $n$-manifolds) and nondegenerate pairing
    $$
    H^i(M)\times H^{n-i}(M)\xrightarrow{\smile} H^n(M),
    $$
    any nonzero $\alpha\in H^i(M)$ would pair with some $\beta\in H^{n-i}(M)$ to a nonzero class in $H^n(M)$.
    This contradicts the hypothesis that all cup products are zero.
    Hence $H^i(M)=0$ for $0<i<n$.

<1> Since $M$ is connected, $H^0(M)\cong\mathbb Z$.
    Poincaré duality gives $H^n(M)\cong\mathbb Z$ and all other reduced cohomology groups vanish.
    Therefore
    $$
    H^*(M;\mathbb Z)\cong \mathbb Z\text{ in degree }0\text{ and }n,\text{ and }0\text{ otherwise}.
    $$
    This is exactly $H^*(S^n;\mathbb Z)$.

Authored by **Codex 5.3 Spark Extra High**.
:::
