---
schema: qual/card@1
id: FT-REHJT
kind: theorem
title: Cauchy Inequalities
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
$$
\abs{f^{(n)} (z_0) \over n!} \leq R^{-n} \sup_{\abs{z}=R} \abs{f(z)}
.$$
:::
