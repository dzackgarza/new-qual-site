---
schema: qual/card@1
id: PR-4BVDD
kind: proposition
title: Uniform convergence of the exponential series on discs
slogan: 'The exponential series converges uniformly on every bounded set by the Weierstrass $M$-test.'
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Power Series
  - Entire Functions
relations: []
review: draft
---

::: {.proposition}
The series $e^z=\sum_{n\ge0}\frac{z^n}{n!}$ converges uniformly on every bounded subset of $\CC$, in particular on every disc in $\CC$.

This is [@Rud76, ch. 7, Theorem 7.10] applied on $\abs z\le r$ with $M_n=r^n/n!$, which are the terms of $e^r$; a bounded subset of $\CC$ lies in some such disc.
:::
