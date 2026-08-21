---
schema: qual/card@1
id: D-PPYCK
kind: definition
title: Equicontinuity
classification:
  areas:
  - complex-analysis
  topics:
  - Equicontinuity
  - Normal Families
relations: []
review: draft
---

:::{.definition title="Equicontinuity"}
A family $\mcf$ of holomorphic functions is **equicontinuous** on $K$ if 
\[
\forall \eps>0,\, \exists \delta = \delta(\eps) \text{ such that } z,w\in K,\, \abs{z-w}< \delta \implies \abs{f(z) - f(w)} < \eps \quad \forall f\in \mcf
.\]
:::
