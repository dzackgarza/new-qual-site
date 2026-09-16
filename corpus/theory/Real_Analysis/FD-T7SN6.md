---
schema: qual/card@1
id: FD-T7SN6
kind: definition
title: Complete measure
prompts:
- What is a complete measure?
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
The measure $\mu$ is \dfn{complete} if every subset of a null set is measurable: whenever $N\in\mcm$, $\mu(N)=0$, and $A\subseteq N$, then $A\in\mcm$.
:::
