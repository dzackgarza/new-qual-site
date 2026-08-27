---
schema: qual/card@1
id: D-R4VKE
kind: definition
title: Lebesgue Integral
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations: []
review: draft
---

:::{.definition}
\[
\int_X f \da \sup \ts{ \int s(x) \dmu \st 0\leq s \leq f, s\text{ simple } } 
.\]

Note that if $s = \sum c_j \chi_{E_j}$ is simple, then
\[
\int_X s(x) \dmu \da \sum_{j=1}^n c_j \mu(E_j)
.\]

:::
