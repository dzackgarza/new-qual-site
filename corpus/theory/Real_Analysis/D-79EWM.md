---
schema: qual/card@1
id: D-79EWM
kind: definition
title: Outer measure on a set
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.definition}
Let $X$ be a nonempty set.
An \dfn{outer measure} on $X$ is a function $\mu^*\colon\mathcal P(X)\to[0,\infty]$ such that

1. $\mu^*(\varnothing)=0$,

2. $\mu^*(A)\leq\mu^*(B)$ whenever $A\subseteq B\subseteq X$, and

3. $\mu^*\qty{\bigcup_{j\geq1}A_j}\leq\sum_{j\geq1}\mu^*(A_j)$ for every sequence $(A_j)_{j\geq1}$ of subsets of $X$.
:::
