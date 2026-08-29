---
schema: qual/card@1
id: FD-4GI2R
kind: definition
title: Equicontinuity
prompts:
- What does it mean for a family of functions to be equicontinuous?
classification:
  areas:
  - complex-analysis
  topics:
  - Equicontinuity
  - Sequences of Functions
relations: []
review: draft
---

::: {.definition}
A family of functions $f_n$ is **equicontinuous** iff for every $\eps$ there exists a $\delta = \delta(\eps)$ (not depending on $n$ or $f_n$) such that
$$
\abs{x-y}<\delta \implies \abs{f_n(x) - f_n(y)} < \eps
\qquad \forall n
.$$
:::
