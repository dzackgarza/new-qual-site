---
schema: qual/card@1
id: D-E2XVI
kind: definition
title: Metric
classification:
  areas:
  - real-analysis
  topics:
  - Metric Spaces
relations: []
review: draft
---

::: {.definition}
Let $X$ be a set.
A \dfn{metric} on $X$ is a function $\rho\colon X\times X\to[0,\infty)$ such that, for all $x,y,z\in X$,

1. $\rho(x,y)=0$ if and only if $x=y$,

2. $\rho(x,y)=\rho(y,x)$, and

3. $\rho(x,z)\leq\rho(x,y)+\rho(y,z)$.

A \dfn{metric space} is a set together with a metric on it.
:::
