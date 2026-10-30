---
schema: qual/card@1
id: PR-5ZSSQ
kind: proposition
title: Contraction mapping principle
slogan: 'A strict contraction on a complete metric space has exactly one fixed point, found by iteration.'
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Metric Spaces
  - Completeness
relations: []
review: draft
---

::: {.proposition}
Let $(X,d)$ be a nonempty complete metric space, and let $f\colon X\to X$ be a map for which there exists $c\in[0,1)$ with
$$
d(f(x),f(y)) \leq c\, d(x,y) \quad\text{for all } x, y\in X.
$$
Then $f$ has a unique fixed point: there is exactly one $x^*\in X$ with $f(x^*) = x^*$.
:::
