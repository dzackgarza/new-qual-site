---
schema: qual/card@1
id: FF-EMDBP
kind: fact
title: $p\dash$test for integrals.
prompts:
- For which $p$ do $\int_0^1 x^{-p}$ and $\int_1^\infty x^{-p}$ converge?
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Lp Spaces
relations: []
review: draft
---

::: {.fact}
$$
\int_0^1 {1\over x^p} < \infty \iff  p < 1 \\
\int_1^\infty {1\over x^p} < \infty \iff  p > 1 
.$$
:::
