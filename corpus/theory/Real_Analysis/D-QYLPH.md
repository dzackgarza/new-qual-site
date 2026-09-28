---
schema: qual/card@1
id: D-QYLPH
kind: definition
title: Measure on a measurable space
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.definition}
Let $(X, \mcm)$ be a measurable space.
A \dfn{measure} on $(X,\mcm)$ is a function $\mu\colon \mcm \to [0,\infty]$ such that

1. $\mu(\emptyset) = 0$, and

2. $\mu$ is \dfn{countably additive}: if $(E_k)_{k\geq 1}$ is a sequence of pairwise disjoint sets in $\mcm$, then
$$
\mu\qty{\bigcup_{k\geq 1} E_k} = \sum_{k\geq 1} \mu(E_k).
$$
:::

::: {.remark}
Countable additivity is also called $\sigma$-additivity.
A function $\mu\colon\mcm\to[0,\infty]$ with $\mu(\emptyset)=0$ for which the identity in (2) is required only for finite families of pairwise disjoint sets is called \dfn{finitely additive}.
:::
