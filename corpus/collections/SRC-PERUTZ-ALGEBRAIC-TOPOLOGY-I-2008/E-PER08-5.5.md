---
schema: qual/card@1
id: E-PER08-5.5
kind: problem
title: Maps with unique path lifting that are not covering maps
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
---

::: {.problem}
A surjective map p: Y $\\to$ X which has unique path-lifting need not be a covering map.
(You may choose Y not to be locally path connected.
For a harder exercise, find an example where Y is locally path connected.)
:::

::: {.solution}
Take $X=\mathbb Q$ with its usual subspace topology from $\mathbb R$, take $Y$ to be the same underlying set with the discrete topology, and let
\[
p:Y\to X
\]
be the identity on the underlying set.

<1>1. $p$ is continuous, surjective, and has unique path lifting.
::: {.proof}
Continuity is immediate because every subset of the discrete space $Y$ is open.
Every continuous path $\gamma:I\to\mathbb Q$ is constant: its image is connected, while every connected subset of $\mathbb Q$ is a singleton.
Thus, given $y\in Y$ over $\gamma(0)$, the only possible lift is the constant path at $y$, and it exists.
Hence $p$ has unique path lifting.
:::

<1>2. $p$ is not a covering map.
::: {.proof}
If $U\subseteq\mathbb Q$ were an evenly covered neighbourhood of $x$, then because $p$ is bijective there could be only one sheet, namely $p^{-1}(U)=U$ with the discrete topology, and $p|_U$ would have to be a homeomorphism onto $U$ with its usual topology.
Hence $U$ would be discrete.
But no nonempty open subset of $\mathbb Q$ is discrete.
Therefore no point has an evenly covered neighbourhood.
:::

This example even has $Y$ locally path connected, since $Y$ is discrete.
:::
