---
schema: qual/card@1
id: E-JZNWV
kind: problem
title: $\int_\RR \frac{x}{(x^2+4x+13)^2}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Poles
relations: []
review: draft
---

::: {.exercise}
Compute
$$
I\coloneqq\int_\RR {x\over (x^2 + 4x+13)^2}\dx
.$$

:::

::: {.solution}
Let $f(z)\coloneqq\frac{z}{(z^2+4z+13)^2}$. Since $z^2+4z+13=(z+2)^2+9$, its zeros are $z_1\coloneqq-2+3i\in\HH$ and $z_2\coloneqq\overline{z_1}=-2-3i$, and $f(z)=\frac{z}{(z-z_1)^2(z-z_2)^2}$.
For $R>\sqrt{13}$ let $\Gamma_R$ be the boundary of the upper half-disk of radius $R$: the segment $[-R,R]$ followed by the arc $C_R=\theset{Re^{it}\st t\in[0,\pi]}$.

![Semicircular contour](../../assets/Complex_Analysis/040_Residues/figures/2021-12-23_18-14-14.png)

::: pf

::: {.pf-step #arc}
$\int_{C_R}f\to0$ as $R\to\infty$.

::: pf-proof
For $\abs z=R\ge2\sqrt{13}$, $\abs{z-z_j}\ge R-\sqrt{13}\ge R/2$, so $\abs{f(z)}\le\frac{R}{(R/2)^4}=16R^{-3}$ and $\abs{\int_{C_R}f}\le\pi R\cdot16R^{-3}\to0$.
:::

:::

::: {.pf-step #residue}
$\Res_{z=z_1}f=\frac{i}{54}$.

::: pf-proof
$z_1$ is a double pole, so
$$
\Res_{z=z_1}f=\frac{d}{dz}\frac{z}{(z-z_2)^2}\Big|_{z=z_1}=-\frac{z_1+z_2}{(z_1-z_2)^3}=-\frac{-4}{(6i)^3}=\frac{4}{-216i}=\frac{i}{54}.
$$
:::

:::

::: pf-step
$I=\boxed{-\frac{\pi}{27}}$.

::: pf-proof
By the residue theorem, $\int_{-R}^Rf+\int_{C_R}f=2\pi i\Res_{z=z_1}f$ for $R>\sqrt{13}$. The integral $I$ converges absolutely since $f(x)=\bigo(\abs x^{-3})$. Letting $R\to\infty$ and using steps [](#arc){.pf-ref} and [](#residue){.pf-ref}, $I=2\pi i\cdot\frac{i}{54}=-\frac{\pi}{27}$.
:::

:::

:::

:::
