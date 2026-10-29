---
schema: qual/card@1
id: P-DQTVL
kind: problem
title: A conformal map from $\DD\setminus[0,1)$ to $\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Complex Logarithm
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Let $D$ be the region obtained by deleting the real interval $[0, 1)$ from $\DD$; find a conformal map from $D$ to $\DD$.
:::

::: {.solution}

Write $D=\{z: 0<\abs{z}<1,\ 0<\arg z<2\pi\}$.

::: pf

::: {.pf-step #root}
$s(z)\coloneqq\abs{z}^{1/2}e^{i\arg z/2}$, with $0<\arg z<2\pi$, maps $D$ biholomorphically onto the upper half-disc $U\coloneqq\{\abs{w}<1,\ \Im w>0\}$.

::: pf-proof
$s$ is a holomorphic branch of $\sqrt z$ on $D$; it halves arguments in $(0,2\pi)$ and takes square roots of moduli in $(0,1)$, with inverse $w\mapsto w^2$.
:::

:::

::: {.pf-step #quadrant}
$T(w)\coloneqq\frac{1+w}{1-w}$ maps $U$ biholomorphically onto the first quadrant.

::: pf-proof
$T$ maps the diameter $(-1,1)$ onto the positive real axis and the upper semicircle onto the positive imaginary axis, and $T(i/2)=\frac{3+4i}{5}$ lies in the first quadrant.
:::

:::

::: pf-step
$$
\boxed{
F(z)=
\frac{\left(\frac{1+\sqrt z}{1-\sqrt z}\right)^2-i}
     {\left(\frac{1+\sqrt z}{1-\sqrt z}\right)^2+i}}
$$
with $\sqrt z=s(z)$ maps $D$ biholomorphically onto $\DD$.

::: pf-proof
Squaring maps the first quadrant onto the upper half-plane, and the Cayley map $\zeta\mapsto\frac{\zeta-i}{\zeta+i}$ maps the upper half-plane onto $\DD$; compose with steps [](#root){.pf-ref} and [](#quadrant){.pf-ref}.
:::

:::

:::

:::
