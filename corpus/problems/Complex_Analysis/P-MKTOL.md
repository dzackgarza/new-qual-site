---
schema: qual/card@1
id: P-MKTOL
kind: problem
title: $\int_0^\infty\frac{\sqrt{x}}{1+x^2}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
---

::: {.problem}
Calculate
$$
\int_0^\infty {\sqrt x \over 1 + x^2} \, dx.
$$
:::

::: {.solution}
::: pf

::: {.pf-step #substitute}
$\int_0^\infty\frac{\sqrt x}{1+x^2}\,dx=\int_{-\infty}^\infty\frac{t^2}{1+t^4}\,dt$.

::: pf-proof
Substitute $x=t^2$, $dx=2t\,dt$, $t>0$: the integral becomes $\int_0^\infty\frac{2t^2}{1+t^4}\,dt$, and the integrand is even.
:::

:::

::: {.pf-step #residues}
$\int_{-\infty}^\infty\frac{t^2}{1+t^4}\,dt=\frac{\pi}{\sqrt2}$.

::: pf-proof
Let $h(z)=\frac{z^2}{1+z^4}$, integrated over the boundary of the upper half-disk of radius $R>1$. In the upper half-plane $h$ has simple poles at $e^{i\pi/4}$ and $e^{3i\pi/4}$, with residues $\frac{z^2}{4z^3}=\frac{1}{4z}$, namely $\frac14e^{-i\pi/4}$ and $\frac14e^{-3i\pi/4}$. Their sum is $\frac14\bigl(-i\sqrt2\bigr)$, so the contour integral is $2\pi i\cdot\frac{-i\sqrt2}{4}=\frac{\pi}{\sqrt2}$. On the arc, $\abs{h(z)}\le\frac{R^2}{R^4-1}$, so the arc integral is at most $\frac{\pi R^3}{R^4-1}\to0$ as $R\to\infty$.
:::

:::

::: pf-step
$\int_0^\infty\frac{\sqrt x}{1+x^2}\,dx=\boxed{\frac{\pi}{\sqrt2}}$.

::: pf-proof
Combine steps [](#substitute){.pf-ref} and [](#residues){.pf-ref}.
:::

:::

:::
:::
