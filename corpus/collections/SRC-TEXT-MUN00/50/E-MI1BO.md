---
schema: qual/card@1
id: E-MI1BO
kind: problem
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

::: {.solution}

::: pf

::: pf-step

Let $x\in X$. Since $X$ is locally $m$-euclidean, choose an open neighborhood $U$ of $x$ and a homeomorphism
    $$\phi:U\to V,$$
    with $V\subset\mathbb R^m$ open.

:::

::: pf-step

Local compactness at $x$.

::: pf-proof

::: pf-step

In $\mathbb R^m$ there is $r>0$ with
    $$\overline{B_{V}( \phi(x),r)}\subset V,$$
    where $\overline{B_V}$ is closure in $\mathbb R^m$.

:::

::: pf-step

Put
    $$K:=\phi^{-1}\!\left(\overline{B_{V}(\phi(x),r)}\right).$$
    Then $K\subset U$ and $K$ is compact because $\phi^{-1}$ is a homeomorphism $V\to U$ and closed balls in $\mathbb R^m$ are compact.

:::

::: pf-step

Let
    $$W:=\phi^{-1}\!\left(B_V(\phi(x),r/2)\right).$$
    Since $B_V(\phi(x),r/2)$ is open in $V$, $W$ is open in $U$, hence open in $X$, and $x\in W\subset K$.

:::

::: pf-step

$K$ is a compact neighborhood of $x$ in $X$, so $X$ is locally compact at $x$.

:::

:::

:::

::: pf-step

Local metrizability at $x$.

::: pf-proof

::: pf-step

Let $d_V$ be the Euclidean metric restricted to $V$.

:::

::: pf-step

Define for $a,b\in U$
    $$d_U(a,b):=d_V(\phi(a),\phi(b)).$$
    This is a metric on $U$ and generates the subspace topology because $\phi$ is a homeomorphism.

:::

::: pf-step

Since $x\in U$, there is a metrizable neighborhood $U$ of $x$ in $X$.

:::

::: pf-step

Therefore $X$ is locally metrizable.

:::

:::

:::

:::

:::
