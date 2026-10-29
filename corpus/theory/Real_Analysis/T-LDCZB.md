---
schema: qual/card@1
id: T-LDCZB
kind: theorem
title: Riesz representation theorem for Hilbert spaces
slogan: 'Every continuous linear functional on a Hilbert space is inner product with a unique vector.'
prompts:
- What is the Riesz representation theorem for Hilbert spaces?
classification:
  areas:
  - real-analysis
  topics:
  - Riesz Representation
  - Hilbert Spaces
  - Dual Spaces
relations: []
review: draft
---

::: {.theorem}
Let $H$ be a [[D-7QQUO|Hilbert space]], with inner product linear in the first argument, and let $\Lambda\in \dualof{H}$ be a continuous [[D-EPSKF|linear functional]] on $H$.
Then there exists a unique $y \in H$ such that
$$
\Lambda(x) = \inner{x}{y} \quad\text{for all } x\in H ,
$$
and $\norm{y}_H = \norm{\Lambda}_{\dualof{H}}$, the [[D-T4LOC|dual norm]] of $\Lambda$.
:::
