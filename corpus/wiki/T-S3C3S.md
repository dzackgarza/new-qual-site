---
schema: qual/card@1
id: T-S3C3S
kind: theorem
title: "Lebesgue Density"
classification:
  areas:
  - real-analysis
  topics:
  - approximations-to-the-identity
  - differentiation
  - integrals
relations: []
review: draft
---
:::{.theorem title="Lebesgue Density"}
\[
A_{h}(f)(x):=\frac{1}{2 h} \int_{x-h}^{x+h} f(y) d y
\implies \norm{A_h(f) - f} \converges{h\to 0}\to 0
.\]
:::
