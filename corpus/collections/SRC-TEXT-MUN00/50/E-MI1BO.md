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
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked against Munkres, Topology (2000), supplementary Exercise 1 of §50, printed p. 317, with the
    definition of local m-euclidean given there, Theorem 26.5 for the compactness of a closed ball and the fact
    that a subspace of a metrizable space is metrizable (Theorem 20.1 and Theorem 30.2 for the countable basis).
    Local compactness at x: inside a chart phi: U -> V with V open in R^m, a closed ball about phi(x) lies in V,
    and its preimage is a compact neighbourhood of x inside U. Local metrizability: U is homeomorphic to an open
    subset of R^m, hence metrizable. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Math StackExchange 459890, "Showing that $X$ is locally compact
    and locally metrizable" (2013-08-05), is supplementary Exercise 1 of §50, and the answer 459896 by Anthony
    Carapetis (2013-08-05), kept at tmp/sources/mse-459890-munkres-50-supp-1.md, gives the proof in two
    sentences: the two properties are local and are possessed by Euclidean space, so a Euclidean neighbourhood
    $U\cong\RR^m$ of a point is metrizable and a Euclidean closed ball in it is a compact neighbourhood. That
    is correct and is the card's argument; the card supplies the details the answer leaves implicit, that a
    closed ball in $\RR^m$ is compact (Theorem 27.3), that a subspace of a metrizable space is metrizable
    (Theorem 20.1 and its restriction to the subspace), and that the ball is a neighbourhood of the point
    inside $U$. Murayama's selection has no Chapter 8, dbFin has no chapter-8 page, and the AoPS post *Topology
    by Munkres Chapter 8 | Day 18* (https://artofproblemsolving.com/community/c3401823h3647630) answers §50
    with its formulas lost. Nothing needed correction.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the two containers state why their subclaims suffice, and the 9
    leaf steps that asserted their claim with no justification each carry a sentence deriving it. The
    mathematics is unchanged: a point has a neighbourhood homeomorphic to an open set of $\RR^m$, a
    closed ball with compact closure inside that open set pulls back to a compact neighbourhood, and the
    restricted Euclidean metric transported along the homeomorphism metrizes a neighbourhood of the point.
    Checked against Munkres, Topology (2000), section 50, where local $m$-euclideanity is defined and
    these two consequences are drawn. Nothing in the statement was changed.

---

::: {.exercise}

A space $X$ is said to be locally $m$-euclidean if for each $x \in X$, there is a neighborhood of $x$ that is homeomorphic to an open set of $\RR^m$.
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
    with $V\subset\RR^m$ open.


::: pf-proof
This is the definition of local $m$-euclideanity at $x$: a neighbourhood homeomorphic to an open set of $\RR^m$.
:::

:::

::: pf-step

Local compactness at $x$.

::: pf-proof

::: pf-step

In $\RR^m$ there is $r>0$ with
    $$\overline{B_{V}( \phi(x),r)}\subset V,$$
    where $\overline{B_V}$ is closure in $\RR^m$.


::: pf-proof
$V$ is open and contains $\phi(x)$, and $\RR^m$ is locally compact, so some closed ball about $\phi(x)$ lies inside $V$.
:::

:::

::: pf-step

Put
    $$K:=\phi^{-1}\!\left(\overline{B_{V}(\phi(x),r)}\right).$$
    Then $K\subset U$ and $K$ is compact because $\phi^{-1}$ is a homeomorphism $V\to U$ and closed balls in $\RR^m$ are compact.


::: pf-proof
$K$ is the preimage of a compact set under a homeomorphism, hence compact, and it contains $x$ because $\phi(x)$ lies in the ball.
:::

:::

::: pf-step

Let
    $$W:=\phi^{-1}\!\left(B_V(\phi(x),r/2)\right).$$
    Since $B_V(\phi(x),r/2)$ is open in $V$, $W$ is open in $U$, hence open in $X$, and $x\in W\subset K$.


::: pf-proof
$W$ is open, contains $x$ and is contained in $K$, so $K$ is a neighbourhood of $x$.
:::

:::

::: pf-step

$K$ is a compact neighborhood of $x$ in $X$, so $X$ is locally compact at $x$.


::: pf-proof
Every point has a compact neighbourhood, which is the definition of local compactness.
:::

:::

:::

:::

::: pf-step

Local metrizability at $x$.

::: pf-proof

::: pf-step

Let $d_V$ be the Euclidean metric restricted to $V$.


::: pf-proof
A subspace of a metric space is metrizable with the restricted metric.
:::

:::

::: pf-step

Define for $a,b\in U$
    $$d_U(a,b):=d_V(\phi(a),\phi(b)).$$
    This is a metric on $U$ and generates the subspace topology because $\phi$ is a homeomorphism.


::: pf-proof
It is a metric because $\phi$ is a bijection and $d_V$ is a metric, and it induces the topology of $U$ because $\phi$ is a homeomorphism onto the open set $V$.
:::

:::

::: pf-step

Since $x\in U$, there is a metrizable neighborhood $U$ of $x$ in $X$.


::: pf-proof
$U$ with the metric $d_U$ is homeomorphic to the open subset $V$ of $\RR^m$, hence is a metrizable neighbourhood of $x$.
:::

:::

::: pf-step

Therefore $X$ is locally metrizable.


::: pf-proof
Every point has a metrizable neighbourhood, which is the definition of local metrizability.
:::

:::

:::

:::

:::

:::
