---
schema: qual/card@1
id: FT-5V4M2
kind: theorem
title: Cauchy integral formula on a disc
prompts:
- State the Cauchy integral formula for $f(z)$.
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Contour Integration
relations: []
review: draft
---

::: {.theorem}
Let $D\subseteq\CC$ be an open disc, let $U$ be an open set containing its closure $\overline D$, and let $f$ be [[D-E7A5W|holomorphic]] on $U$.
Then for every $z\in D$,
$$
f(z) = {1 \over 2\pi i} \int_{\bd D} {f(\xi) \over \xi - z} \,d\xi,
$$
where the circle $\bd D$ is oriented counterclockwise.
:::
