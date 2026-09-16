---
schema: qual/card@1
id: FD-5I73B
kind: definition
title: Diameter of a subset of a metric space
prompts:
- What is the diameter of a set $A$ in a metric space?
classification:
  areas:
  - real-analysis
  topics:
  - Metric Spaces
relations: []
review: draft
---

::: {.definition}
Let $(X,d)$ be a metric space and let $A\subseteq X$ be nonempty.
The \dfn{diameter} of $A$ is
$$
\diam(A) \coloneqq \sup_{x, y\in A} d(x, y) \in [0,\infty].
$$
:::
