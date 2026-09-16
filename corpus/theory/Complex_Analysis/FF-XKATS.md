---
schema: qual/card@1
id: FF-XKATS
kind: fact
title: Taylor series of $\sinh z$
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
For every $z\in\CC$,
$$
\sinh z=z+\frac{z^{3}}{3 !}+\frac{z^{5}}{5 !}+\frac{z^{7}}{7 !}+\cdots=\sum_{n=0}^{\infty} \frac{z^{2 n+1}}{(2 n+1) !}.
$$
:::
