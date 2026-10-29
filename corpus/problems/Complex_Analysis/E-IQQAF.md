---
schema: qual/card@1
id: E-IQQAF
kind: problem
title: $\int_\RR\frac{\cos x}{x^2+1}\,dx$ by a semicircular contour
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Trigonometry
relations: []
review: draft
---

::: {.exercise}
Use a semicircular contour and the residue theorem to evaluate
$$
I = \int_\RR {\cos(x) \over x^2 + 1 }\dx
.$$
:::

::: {.solution}
Let $f(z) \coloneqq {e^{iz} \over z^2 + 1}$, so that $I=\Re\int_\RR f(x)\dx$.
For $R>1$, let $C_1 = [-R, R]$, $C_2 = \theset{Re^{it} \st t\in [0, \pi]}$, and $\Gamma = C_1 + C_2$.

::: pf

::: {.pf-step #residue}
$\int_\Gamma f(z)\dz=2\pi i\Res_{z=i}f(z)={\pi\over e}$.

::: pf-proof
The only pole of $f$ in $\HH$ is $z=i$, and it is simple since $e^{iz}\neq0$, so
$$
\Res_{z=i} f(z) = { e^{iz} \over z+i}\evalfrom_{z=i} = {e^{-1}\over 2i}
,$$
and the residue theorem gives $2\pi i\cdot{e^{-1}\over2i}={\pi\over e}$.
:::

:::

::: {.pf-step #arc}
$\int_{C_2}f(z)\dz\to0$ as $R\to\infty$.

::: pf-proof
On $C_2$, $\abs{e^{iz}}=e^{-\Im z}\le1$ and $\abs{z^2+1}\ge\abs z^2-1=R^2-1$, so the ML estimate gives
$$
\abs{\int_{C_2} f(z)\dz } \leq {\pi R\over R^2-1} \convergesto{R\to\infty}0
.$$
:::

:::

::: pf-step
$I=\boxed{\pi/e}$.

::: pf-proof
By steps [](#residue){.pf-ref} and [](#arc){.pf-ref}, $\int_{-R}^Rf(x)\dx\to\pi/e$, so $I=\Re(\pi/e)=\pi/e$.
:::

:::

:::

:::

::: {.remark}
The imaginary part gives $\int_\RR { \sin x \over x^2 + 1} \dx = 0$, as the oddness of the integrand also shows.
:::
