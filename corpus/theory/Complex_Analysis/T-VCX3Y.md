---
schema: qual/card@1
id: T-VCX3Y
kind: theorem
title: Argument Principle, Zeros/Poles Version
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Zeros
  - Poles
  - Meromorphic Functions
relations:
- kind: variant-of
  target: T-JXDQT
review: draft
---

:::{.theorem}
For $f$ meromorphic in $\Omega$ with multisets of zeros \( Z_f \da \ts{ z_j } \) and poles \( P_f\da \ts{ p_k } \) (so repeated with multiplicity)
for $\gamma \da \bd \Omega$ not intersecting any of the zeros or poles,
\[
{1\over 2\pi i} \int_\gamma \del_{\log} f(z) \dz
&= \# Z_f - \# P_f
,\]
where $\# Z_f$ and $\# P_f$ are the number of zeros and poles respectively, counted with multiplicity.
:::
