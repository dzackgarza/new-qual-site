---
schema: qual/card@1
id: E-4F5TF
kind: problem
title: $\int_{\partial\DD}\frac{e^z}{z^2}\,dz$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Contour Integration
relations: []
review: draft
---

::: {.exercise}
Compute
\[
\int_{\bd\DD} {e^z\over z^2}\dz
.\]

:::

::: {.solution}
By Cauchy's integral formula for the derivative, with $f(z)=e^z$,
\[
\int {f(z) \over (z-0)^2}\dz = 2\pi i f^{(1)}(0) = 2\pi i
.\]
:::

