---
schema: qual/card@1
id: PR-SX6NO
kind: proposition
title: Lipschitz maps are uniformly continuous
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
  - Metric Spaces
relations: []
review: draft
---

::: {.proposition}
Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces and let $f\colon X\to Y$ be Lipschitz: there is $C>0$ with $d_Y(f(x),f(y))\leq C\,d_X(x,y)$ for all $x,y\in X$.
Then $f$ is [[D-WGYSB|uniformly continuous]].
:::

::: {.proof}
Given $\varepsilon>0$, take $\delta\coloneqq\varepsilon/C$.
If $d_X(x,y)<\delta$, then
$$
d_Y(f(x),f(y)) \leq C\,d_X(x,y) < C\delta = \varepsilon .
$$
:::
