---
schema: qual/card@1
id: D-TIHRR
kind: definition
title: Equicontinuous Family
classification:
  areas:
  - complex-analysis
  topics:
  - Equicontinuity
  - Sequences of Functions
relations: []
review: draft
---

:::{.definition title="Equicontinuous Family"}
A family of functions $f_n$ is **equicontinuous** iff for every $\eps$ there exists a $\delta = \delta(\eps)$ (not depending on $n$ or $f_n$) such that 
\[
\abs{x-y}<\delta \implies \abs{f_n(x) - f_n(y)} < \eps
&& \forall n
.\]

:::{.remark}
Rudin, *Principles of Mathematical Analysis*, 3rd ed., Definition 7.22.
:::
:::
