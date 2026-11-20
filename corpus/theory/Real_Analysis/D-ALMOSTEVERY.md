---
schema: qual/card@1
id: D-ALMOSTEVERY
kind: definition
title: Almost everywhere
prompts:
- What does it mean for a property to hold almost everywhere?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.definition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space.
A property $P(x)$ of points of $X$ holds \dfn{almost everywhere} if there is a set $N\in\mcm$ with $\mu(N)=0$ such that $P(x)$ holds for every $x\in X\setminus N$.
One says $\mu$-almost everywhere when the measure has to be named.
:::

::: {.remark}
A countable union of null sets is null, so a property that holds almost everywhere for each of countably many properties holds for all of them simultaneously almost everywhere.
:::
