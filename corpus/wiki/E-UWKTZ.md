---
schema: qual/card@1
id: E-UWKTZ
kind: exercise
title: "Show that if $f$ is entire and $f(1/z)$ has a pole at $z=0$, then $f$\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
  - polynomials
  - poles
  - singularities
relations: []
review: draft
---
:::{.exercise title="?"}
Show that if $f$ is entire and $f(1/z)$ has a pole at $z=0$, then $f$ is a polynomial.

:::

:::{.solution}
Write $f(z) = \sum_{k\geq 0}c_k z^k$, so $g(z) \da f(1/z) = \sum_{k\geq 0} c_k z^{-k}$.
Since $z=0$ is a pole of $g$, $c_k = 0$ for all $k\geq m$ for $m$ the order of the pole, so $f(z) = \sum_{0\leq k\leq m}c_k z^k$ is a polynomial of degree at most $m$.
:::
