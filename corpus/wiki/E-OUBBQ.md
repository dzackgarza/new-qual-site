---
schema: qual/card@1
id: E-OUBBQ
kind: exercise
title: Uniform continuity of $x^n$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Continuity
  - Continuity
relations: []
review: draft
---

:::{.problem}
Show that $f(x) = x^n$ is uniformly continuous on any interval $[-M, M]$.

:::

:::{.solution}
\[
\abs{x^n - y^n} = \abs{y-x}\abs{\sum_{1\leq k \leq n} x^k y^{n-k}} \leq n M^{n-1}\abs{y-x} \convergesto{y\to x}0
.\]
:::

