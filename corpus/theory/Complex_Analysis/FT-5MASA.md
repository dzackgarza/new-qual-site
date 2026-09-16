---
schema: qual/card@1
id: FT-5MASA
kind: theorem
title: Cauchy inequalities
prompts:
- State the Cauchy inequalities for $f^{(n)}(z_0)$.
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Cauchy Integral Formula
relations:
- kind: variant-of
  target: FT-REHJT
review: draft
---

::: {.theorem}
Let $z_0\in\CC$ and $R>0$, let $f$ be [[D-E7A5W|holomorphic]] on an open set containing the closed disc $\abs{z-z_0}\le R$, and let $\gamma$ be the circle $\abs{z-z_0}=R$.
Then for every integer $n\ge0$,
$$
\abs{f^{(n)}(z_0)} \leq \frac{n!\, \sup_{z\in\gamma} \abs{f(z)}}{R^{n}}.
$$
:::
