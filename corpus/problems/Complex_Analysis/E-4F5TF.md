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
$$
\int_{\bd\DD} \frac{e^z}{z^2}\dz.
$$

:::

::: {.solution}
Orient $\bd\DD$ counterclockwise.

::: pf

::: pf-step
$\displaystyle\int_{\bd\DD} \frac{e^z}{z^2}\dz=\boxed{2\pi i}$.

::: pf-proof
By Cauchy's integral formula for the first derivative, applied to the entire function $f(z)=e^z$ at $0$, the integral is $2\pi i f'(0) = 2\pi i$.
:::

:::

:::

:::
