---
schema: qual/card@1
id: P-TOPF21C
kind: problem
title: "A simply-connected closed 3-manifold is homotopy equivalent to S^3"
classification:
  areas:
  - topology
  topics:
  - Homotopy Type
  - Manifolds
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Let $X$ be a $3$-dimensional simply-connected closed manifold (compact, no boundary).
Show that $X$ is homotopy equivalent to $S^3$.
:::

::: solution
**Goal:** Show $X \simeq S^3$.

<1> Apply Poincaré in dimension three.
    *Proof:*
    <2>1. By the Poincaré theorem for closed $3$-manifolds, any closed, simply-connected $3$-manifold is homeomorphic to $S^3$.
    <2>2. Since $X$ is closed and simply-connected, there exists a homeomorphism
        $h\colon X\to S^3$.

<1> Turn homeomorphism into homotopy equivalence.
    *Proof:*
    <2>1. A homeomorphism has a continuous inverse.
    <2>2. Therefore $h$ and $h^{-1}$ give a homotopy equivalence between $X$ and $S^3$.
    <2>3. Hence $X$ is homotopy equivalent to $S^3$.

Authored by **Codex 5.3 Spark Extra High**.
:::
