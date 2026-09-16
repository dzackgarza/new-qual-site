---
schema: qual/card@1
id: C-EBAGE
kind: corollary
title: Lipschitz implies uniformly continuous
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Uniform Continuity
  - Continuity
relations: []
review: draft
---

::: {.corollary}
Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces and let $f\colon X\to Y$ be Lipschitz: there exists $C > 0$ such that $d_Y(f(x_1), f(x_2)) \leq C\, d_X(x_1, x_2)$ for all $x_1, x_2 \in X$.
Then $f$ is [[D-WGYSB|uniformly continuous]].
:::

::: {.proof}
Let $\varepsilon > 0$ and put $\delta \coloneqq \varepsilon / C$.
If $d_X(x_1, x_2) < \delta$, then $d_Y(f(x_1), f(x_2)) \leq C\, d_X(x_1, x_2) < C\delta = \varepsilon$.
Since $\delta$ depends only on $\varepsilon$, $f$ is uniformly continuous.
:::
