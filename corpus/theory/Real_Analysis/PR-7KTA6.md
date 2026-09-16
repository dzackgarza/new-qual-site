---
schema: qual/card@1
id: PR-7KTA6
kind: proposition
title: Convexity bound $(a+b)^p \leq 2^{p-1}(a^p+b^p)$
classification:
  areas:
  - real-analysis
  topics:
  - Norms
  - Lp Spaces
relations: []
review: draft
---

::: {.proposition}
Let $p\geq1$ and $a,b\geq0$.
Then
$$
(a+b)^p \leq 2^{p-1} (a^p + b^p) .
$$
:::

::: {.proof}
The function $t\mapsto t^p$ is convex on $[0,\infty)$ for $p\geq1$, so
$$
\qty{\frac{a+b}{2}}^p\le\frac{a^p+b^p}{2}.
$$
Multiplying by $2^p$ gives the inequality.
:::
