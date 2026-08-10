---
schema: qual/card@1
id: FD-4GI2R
kind: definition
title: 'Equicontinuity'
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---

::: {.definition title="Equicontinuity"}
A family of functions $f_n$ is **equicontinuous** iff for every $\eps$ there exists a $\delta = \delta(\eps)$ (not depending on $n$ or $f_n$) such that
$$
\abs{x-y}<\delta \implies \abs{f_n(x) - f_n(y)} < \eps
\qquad \forall n
.$$
:::
