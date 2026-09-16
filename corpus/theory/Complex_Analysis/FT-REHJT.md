---
schema: qual/card@1
id: FT-REHJT
kind: theorem
title: Cauchy inequalities for Taylor coefficients
prompts:
- State the Cauchy inequalities in the form bounding $\abs{f^{(n)}(z_0)/n!}$.
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Cauchy Integral Formula
relations:
- kind: variant-of
  target: FT-5MASA
review: draft
---

::: {.theorem}
Let $z_0\in\CC$ and $R>0$, and let $f$ be [[D-E7A5W|holomorphic]] on an open set containing the closed disc $\abs{z-z_0}\le R$.
Then for every integer $n\ge0$,
$$
\abs{f^{(n)} (z_0) \over n!} \leq R^{-n} \sup_{\abs{z-z_0}=R} \abs{f(z)}.
$$
:::
