---
schema: qual/card@1
id: FF-XKATS
kind: fact
title: Series expansion for $\sinh(z)$
prompts:
- What is the series expansion of $\sinh(z)$?
classification:
  areas:
  - complex-analysis
  topics:
  - Hyperbolic Functions
  - Power Series
relations: []
review: draft
---

::: {.fact}
$$
\sinh x=x+\frac{x^{3}}{3 !}+\frac{x^{5}}{5 !}+\frac{x^{7}}{7 !}+\cdots=\sum_{n=0}^{\infty} \frac{x^{2 n+1}}{(2 n+1) !}
.$$
:::
