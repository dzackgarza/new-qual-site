---
schema: qual/card@1
id: E-AXBZQ
kind: problem
title: $\int_\RR\frac{x\sin x}{1+x^2}\,dx$ by Jordan's lemma
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
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source displays the integral with no instruction; the statement asks to compute it.
---

::: {.exercise}
Compute
$$
I = \int_\RR \frac{x\sin(x)}{1 + x^2}\dx.
$$
:::

::: {.solution}
Let $f(z) = e^{iz}g(z)$ with $g(z) \coloneqq \frac{z}{1 + z^2}$, and for $R>1$ let $C_R = \theset{Re^{it} \st t\in [0, \pi]}$.
Since $\abs{f}=\bigo(1/R)$ on $C_R$, whose length is $\pi R$, the ML estimate does not show that the arc integral vanishes, so we use Jordan's lemma.

![Semicircular contour](../../assets/Complex_Analysis/040_Residues/figures/2021-12-23_18-14-14.png)

::: pf

::: {.pf-step #arc}
$\int_{C_R}f(z)\dz\to0$ as $R\to\infty$.

::: pf-proof
By Jordan's lemma,
$$
\abs{\int_{C_R} e^{iz} g(z)\dz }\leq \pi M_R, \qquad M_R \coloneqq \sup_{z\in C_R}\abs{\frac{z}{1+z^2}}\leq \frac{R}{R^2-1}.
$$
:::

:::

::: {.pf-step #residue}
$\int_{-R}^R f(x)\dx+\int_{C_R}f(z)\dz=\frac{\pi i}{e}$ for $R>1$.

::: pf-proof
Since $1+z^2 = (z+i)(z-i)$, the only pole in $\HH$ is the simple pole $z = i$, and by the residue theorem the left side is
$$
2\pi i \Res_{z=i} f(z)
= 2\pi i \lim_{z\to i} \frac{ze^{iz}}{z+i}
= 2\pi i\,\frac{ie^{-1}}{2i} = \frac{\pi i}{e}.
$$
:::

:::

::: pf-step
$I=\boxed{\pi/e}$.

::: pf-proof
By steps [](#arc){.pf-ref} and [](#residue){.pf-ref}, $\int_{-R}^R\frac{xe^{ix}}{1+x^2}\dx\to\frac{\pi i}{e}$, and $I$ is the imaginary part of this limit.
:::

:::

:::

:::
