---
schema: qual/card@1
id: FF-7JOOD
kind: fact
title: Diameter of a set
slogan: 'The diameter is the largest distance present in the set, interpreted as a supremum.'
prompts:
- What is the diameter of set?
classification:
  areas:
  - real-analysis
  topics:
  - Metric Spaces
relations: []
review: draft
---

::: {.fact}
Let $(X, d)$ be a metric space and let $A\subseteq X$ be nonempty.
The diameter of $A$ is
$$
\diam(A) = \sup_{x, y\in A} d(x, y)\in[0,\infty].
$$
:::
