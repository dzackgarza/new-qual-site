---
schema: qual/card@1
id: E-CLSFF
kind: problem
title: Meromorphic functions on $\CP^1$
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Principal Parts
  - Poles
  - Liouville's Theorem
  - Riemann Surfaces
relations: []
review: draft
---

::: {.exercise}
Show that the only meromorphic functions on $\CP^1$ are rational functions.
:::

::: {.solution}
Let $f$ be meromorphic on $\CP^1$.

::: pf

::: {.pf-step #finite-poles}
$f$ has finitely many poles $a_1,\ldots,a_n$ in $\CC$, and with $P_j$ the principal part of $f$ at $a_j$, the function $g\coloneqq f-\sum_{j=1}^nP_j$ is entire.

::: pf-proof
The poles of $f$ are isolated in the compact space $\CP^1$, so there are finitely many.
Each $P_j$ is a rational function holomorphic away from $a_j$, and $f-P_j$ has a removable singularity at $a_j$.
:::

:::

::: {.pf-step #g-polynomial}
$g$ is a polynomial.

::: pf-proof
Each $P_j$ is rational and so meromorphic on $\CP^1$; hence $g$ is meromorphic at $\infty$, and $g(1/w)=\sum_{k=-m}^{\infty}c_kw^k$ near $w=0$ for some $m\ge0$.
Then $h(z)\coloneqq g(z)-\sum_{k=1}^m c_{-k}z^k$ is entire with a removable singularity at $\infty$, so $h$ extends to a holomorphic function on the compact Riemann surface $\CP^1$ and is constant.
:::

:::

::: pf-step
$f$ is rational.

::: pf-proof
$f=g+\sum_{j=1}^nP_j$, which is rational by step [](#finite-poles){.pf-ref} and step [](#g-polynomial){.pf-ref}.
:::

:::

:::

:::
