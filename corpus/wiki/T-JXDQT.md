---
schema: qual/card@1
id: T-JXDQT
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
relations: []
review: draft
---

:::{.theorem title="Argument Principle, Zeros/Poles Version"}
For $f$ meromorphic in $\Omega$ with multisets of zeros \( Z_f \da \ts{ z_j } \) and poles \( P_f\da \ts{ p_k } \) (so repeated with multiplicity) 
for $\gamma \da \bd \Omega$ not intersecting any of the zeros/poles,

\[  
{1\over 2\pi i} \int_\gamma \logd f(z) \dz
\da {1\over 2\pi i} \int_\gamma {f'(z) \over f(z)} \dz =
&= \size Z_f - \size P_f
,\]
where $\size Z_f$ and $\size P_f$ are the number of zeros and poles respectively, counted with multiplicity.
If $f$ is holomorphic, then
\[
{1\over 2\pi i} \oint_{\bd \Omega} {f'(z) \over f(z)}\dz 
&= \sum_{z_k\in f\inv(0) \intersect \Omega} \mathrm{mult}(f, z_k) \\
{1\over 2\pi i} \oint_{\bd \Omega} {zf'(z) \over f(z)}\dz 
&= \sum_{z_k\in f\inv(0) \intersect \Omega} f(z_k) \mathrm{mult}(f, z_k) \\
.\]

:::
