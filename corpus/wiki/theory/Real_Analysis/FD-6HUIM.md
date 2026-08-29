---
schema: qual/card@1
id: FD-6HUIM
kind: definition
title: Null Set
prompts:
- What does it mean for a set to be null?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.definition}
A set $A$ is *null* iff for every $\varepsilon>0$ there exists a cover $\theset{U_j}\covers A$ such that $\sum \mu(U_j) < \varepsilon$, i.e. $\mu(A) = 0$.
:::
