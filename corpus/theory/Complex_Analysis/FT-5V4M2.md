---
schema: qual/card@1
id: FT-5V4M2
kind: theorem
title: Cauchy Integral Formula (First Derivative)
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
For $f$ holomorphic in $U\supseteq \bar D$, then for any $z\in D$,
$$
f(z) = {1 \over 2\pi i} \int_{\bd D} {f(\xi) \over \xi - z} \,d\xi
.$$
:::
