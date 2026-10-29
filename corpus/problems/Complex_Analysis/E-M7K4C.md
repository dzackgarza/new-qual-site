---
schema: qual/card@1
id: E-M7K4C
kind: problem
title: Cauchy formula and principal parts
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Residues
  - Principal Parts
  - Contour Integration
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source does not give the centers or orientation of the circles or the sign of epsilon; the statement takes positively oriented circles centered at 0 and epsilon > 0.
---

::: {.exercise}
Compute
$$
\int_\gamma {z^2+1 \over z(z^2 + 4)}\dz
$$
where $\gamma$ is the positively oriented circle centered at $0$ of radius

(a) $1$,

(b) $2+\varepsilon$, with $\varepsilon>0$.

:::

::: {.solution}
Write $f(z)\coloneqq\frac{z^2+1}{z(z^2+4)}$; its poles are $0$ and $\pm2i$, all simple.

::: pf

::: pf-step
(a) $\int_{\abs z=1}f\,dz=\boxed{\frac{i\pi}2}$.

::: pf-proof
$\frac{z^2+1}{z^2+4}$ is holomorphic on $\abs z\le1$, so Cauchy's integral formula gives $2\pi i\cdot\frac{0+1}{0+4}$.
:::

:::

::: {.pf-step #partial-fractions}
$f(z)=\dfrac{1/4}{z}+\dfrac{3/8}{z+2i}+\dfrac{3/8}{z-2i}$.

::: pf-proof
By the cover-up method, the coefficients are $\frac{z^2+1}{z^2+4}\big|_{z=0}=\frac14$, $\frac{z^2+1}{z(z-2i)}\big|_{z=-2i}=\frac{-3}{(-2i)(-4i)}=\frac38$ and $\frac{z^2+1}{z(z+2i)}\big|_{z=2i}=\frac{-3}{(2i)(4i)}=\frac38$.
:::

:::

::: pf-step
(b) $\int_{\abs z=2+\varepsilon}f\,dz=\boxed{2\pi i}$.

::: pf-proof
All three poles lie inside the circle, so by step [](#partial-fractions){.pf-ref} the integral is $2\pi i\qty(\frac14+\frac38+\frac38)=2\pi i$.
:::

:::

:::

:::
