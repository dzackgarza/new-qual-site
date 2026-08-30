---
schema: qual/card@1
id: E-MI1BO
kind: exercise
title: Locally euclidean spaces are locally compact and locally metrizable
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}

A space $X$ is said to be locally $m$-euclidean if for each $x \in X$, there is a neighborhood of $x$ that is homeomorphic to an open set of $\mathbb{R}^m$.
Such a space $X$ automatically satisfies the $T_1$ axiom, but it need not be Hausdorff.
However, if $X$ is Hausdorff and has a countable basis, then $X$ is called an $m$-manifold.

Throughout these exercises, let $X$ be a space that is locally $m$-euclidean.

Show that $X$ is locally compact and locally metrizable.
:::

::: solution
**Goal:** Prove that a locally $m$-euclidean space is locally compact and locally metrizable.

<1>1. Let $x\in X$. By local euclidean-ness choose an open neighborhood $U$ of $x$ and a homeomorphism
    $$\phi:U\to V,$$
    with $V\subset\mathbb R^m$ open.

<1>2. Local compactness at $x$.
    <2>1. In $\mathbb R^m$ there is $r>0$ with
    $$\overline{B_{V}( \phi(x),r)}\subset V,$$
    where $\overline{B_V}$ is closure in $\mathbb R^m$.
    <2>2. Put
    $$K:=\phi^{-1}\!\left(\overline{B_{V}(\phi(x),r)}\right).$$
    Then $K\subset U$ and $K$ is compact because $\phi^{-1}$ is a homeomorphism $V\to U$ and closed balls in $\mathbb R^m$ are compact.
    <2>3. Let
    $$W:=\phi^{-1}\!\left(B_V(\phi(x),r/2)\right).$$
    Since $B_V(\phi(x),r/2)$ is open in $V$, $W$ is open in $U$, hence open in $X$, and $x\in W\subset K$.
    <2>4. $K$ is a compact neighborhood of $x$ in $X$, so $X$ is locally compact at $x$.

<1>3. Local metrizability at $x$.
    <2>1. Let $d_V$ be the Euclidean metric restricted to $V$.
    <2>2. Define for $a,b\in U$
    $$d_U(a,b):=d_V(\phi(a),\phi(b)).$$
    This is a metric on $U$ and generates the subspace topology because $\phi$ is a homeomorphism.
    <2>3. Since $x\in U$, there is a metrizable neighborhood $U$ of $x$ in $X$.
    <2>4. Therefore $X$ is locally metrizable.
:::
