---
schema: qual/card@1
id: FF-LF5ND
kind: fact
title: Taylor series of $\cosh z$
slogan: '$\cosh z$ keeps exactly the even terms of the exponential series.'
prompts:
- What is the series expansion of $\cosh(z)$?
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
\cosh z=1+\frac{z^{2}}{2 !}+\frac{z^{4}}{4 !}+\frac{z^{6}}{6 !}+\cdots=\sum_{n=0}^{\infty} \frac{z^{2 n}}{(2 n) !}.
$$
:::
