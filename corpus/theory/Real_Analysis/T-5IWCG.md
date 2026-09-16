---
schema: qual/card@1
id: T-5IWCG
kind: theorem
title: Linear functionals are continuous if and only if bounded
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Continuity
  - Norms
relations: []
review: draft
---

::: {.theorem}
Let $(X,\norm{\cdot})$ be a normed vector space over $\CC$ and let $L\colon X \to \CC$ be a [[D-EPSKF|linear functional]].
The following are equivalent:

1. $L$ is continuous.

2. $L$ is continuous at $0$.

3. $L$ is bounded: there exists $c\geq 0$ such that $\abs{L(x)} \leq c \norm{x}$ for all $x\in X$.
:::
