---
schema: qual/card@1
id: T-7LQ7X
kind: theorem
title: Monotonicity and countable subadditivity of measures
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.theorem}
Let $(X, \mcm, \mu)$ be a [[D-QYLPH|measure]] space.

1. (Monotonicity) If $E,F\in\mcm$ and $E \subseteq F$, then $\mu(E) \leq \mu(F)$.

2. (Countable subadditivity) If $E_k\in\mcm$ for $k\geq1$, then
$$
\mu\qty{\bigcup_{k\geq 1} E_k} \leq \sum_{k\geq 1} \mu(E_k).
$$
:::
