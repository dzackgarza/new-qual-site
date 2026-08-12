---
schema: qual/card@1
id: D-TIHRR
kind: definition
title: "Equicontinuous Family"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.definition title="Equicontinuous Family"}
A family of functions $f_n$ is **equicontinuous** iff for every $\eps$ there exists a $\delta = \delta(\eps)$ (not depending on $n$ or $f_n$) such that 
\[
\abs{x-y}<\eps \implies \abs{f_n(x) - f_n(y)} < \eps
&& \forall n
.\]
:::
