---
schema: qual/card@1
id: P-CAFA23D
kind: problem
title: "Contour integral of e^{e^{i theta}}"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Evaluate $\displaystyle \int_0^{2\pi} e^{e^{i\theta}}\,d\theta$, carefully explaining your solution.
:::

::: solution
Use the uniformly convergent exponential series on the unit circle:
\[
e^{e^{i\theta}}
=\sum_{n=0}^\infty\frac{e^{in\theta}}{n!}.
\]
Termwise integration is therefore valid, and
\[
\int_0^{2\pi}e^{e^{i\theta}}\,d\theta
=\sum_{n=0}^\infty\frac1{n!}
\int_0^{2\pi}e^{in\theta}\,d\theta.
\]
Every term with $n\ge1$ integrates to $0$, while the $n=0$ term contributes
$2\pi$. Hence
\[
\boxed{\displaystyle
\int_0^{2\pi}e^{e^{i\theta}}\,d\theta=2\pi.}
\]
:::
