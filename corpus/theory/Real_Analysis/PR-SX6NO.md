---
schema: qual/card@1
id: PR-SX6NO
kind: proposition
title: Lipschitz maps are uniformly continuous
slogan: 'A global Lipschitz bound gives one delta that works everywhere.'
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
Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces and let $f\colon X\to Y$ be Lipschitz: there is $C\geq0$ with $d_Y(f(x),f(y))\leq C\,d_X(x,y)$ for all $x,y\in X$.
Then $f$ is [[D-WGYSB|uniformly continuous]].
:::

::: {.proof}
If $C=0$ then $d_Y(f(x),f(y))=0$ for all $x,y\in X$, so $f$ is constant and every $\delta>0$ works.
If $C>0$, given $\varepsilon>0$, take $\delta\coloneqq\varepsilon/C$.
If $d_X(x,y)<\delta$, then
$$
d_Y(f(x),f(y)) \leq C\,d_X(x,y) < C\delta = \varepsilon .
$$
:::
