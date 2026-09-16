---
schema: qual/card@1
id: PR-4BVDD
kind: proposition
title: Uniform convergence of the exponential series on discs
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
:::

::: {.proof}
A bounded set lies in a disc $\abs{z}\le R$ for some $R>0$.
There $\abs{z^n/n!}\le R^n/n!$, and $\sum_n R^n/n!=e^R<\infty$, so the Weierstrass $M$-test gives uniform convergence.
:::
