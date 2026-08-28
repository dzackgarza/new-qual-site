---
schema: qual/card@1
id: FD-7R4QC
kind: definition
title: Locally Compact
prompts:
- What does it mean for a space to be locally compact?
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Counterexamples
relations: []
review: draft
---

::: {.definition}
A space $X$ is *locally compact* iff for every $x\in X$ there exists an open $U$ and compact $K$ such that $x\in U \subseteq K$.

Compact implies locally compact but not conversely: $\RR^n$.

Non locally-compact spaces:

- $\QQ$,

- $\theset{\vector 0} \union \theset{(x, y) \suchthat x>0} \subset\RR^2$ (since the origin admits no compact neighborhood).
:::
