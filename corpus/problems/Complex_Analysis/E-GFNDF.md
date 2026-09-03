---
schema: qual/card@1
id: E-GFNDF
kind: problem
title: The family $\{z^k\}$ on $[0,1]$ is not equicontinuous
classification:
  areas:
  - complex-analysis
  topics:
  - Equicontinuity
  - Counterexamples
  - Sequences of Functions
relations: []
review: draft
---

::: {.exercise}
Give an example of a non-equicontinuous family.
:::

::: {.solution}
Take $f_k(z) \da z^k$ on $[0, 1]$ -- fix any $z_0\in [0, 1)$, then $\abs{f_k(1) - f_k(x_0)} \convergesto{k\to\infty} 1$.
:::
