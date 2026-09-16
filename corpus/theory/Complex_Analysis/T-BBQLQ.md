---
schema: qual/card@1
id: T-BBQLQ
kind: theorem
title: Holomorphic functions on a compact connected complex manifold are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Riemann Surfaces
  - Compactness
relations: []
review: draft
---

::: {.theorem}
Let $X$ be a compact connected complex manifold.
Then every holomorphic function $f\colon X\to\CC$ is constant.
:::

::: {.proof}
Since $X$ is compact, $\abs f$ attains its maximum $M$ at some point.
The set $S\coloneqq\ts{x\in X\st f(x)=c}$, for $c$ a value with $\abs c=M$ attained by $f$, is nonempty and closed.
At a point of $S$, $f$ read in a holomorphic chart is holomorphic on a connected open subset of $\CC^n$ with an interior maximum of $\abs f$; by the maximum modulus principle, applied on complex lines through the point, $f$ is constant near that point, so $S$ is open.
As $X$ is connected, $S=X$.
:::
