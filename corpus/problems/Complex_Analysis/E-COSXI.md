---
schema: qual/card@1
id: E-COSXI
kind: problem
title: $\int_\RR\frac{\cos x}{x+i}\,dx$ by Jordan's lemma
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
  note: The source displays the integral I with no request; the statement now asks to compute it.
---

::: {.exercise}
Compute
$$
I \coloneqq \int_\RR {\cos(x) \over x+i}\dx.
$$
:::

::: {.solution}
Since $x+i$ is not real, $\frac{\cos x}{x+i}\neq\Re\frac{e^{ix}}{x+i}$, so we split the cosine instead.
Write $\cos z=\frac12(e^{iz}+e^{-iz})$ and
$$
f_1(z)\coloneqq\frac{e^{iz}}{2(z+i)},\qquad f_2(z)\coloneqq\frac{e^{-iz}}{2(z+i)},
$$
so that $I=\int_\RR f_1+\int_\RR f_2$.
Both have the form $e^{\pm iz}g(z)$ with $g(z)=\frac1{2(z+i)}\to0$ as $\abs z\to\infty$.

::: pf

::: {.pf-step #f1-vanishes}
$\int_\RR f_1=0$.

::: pf-proof
Close the segment $[-R,R]$ with the upper semicircle:

![Semicircular contour](../../assets/Complex_Analysis/040_Residues/figures/2021-12-23_18-14-14.png)

By Jordan's lemma for $e^{iz}$ on the upper half-plane, the arc integral tends to $0$, so $\int_\RR f_1$ is $2\pi i$ times the sum of the residues of $f_1$ in $\HH$.
The only pole of $f_1$ is $z=-i\notin\HH$.
:::

:::

::: pf-step
$I=\boxed{-\frac{i\pi}{e}}$.

::: pf-proof
By step [](#f1-vanishes){.pf-ref}, $I=\int_\RR f_2$.
Close the segment with the lower semicircle, oriented counterclockwise:

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-23_18-39-11.png)

The real axis is then traversed from $R$ to $-R$, so that piece tends to $-I$, and by Jordan's lemma for $e^{-iz}$ on the lower half-plane the arc integral tends to $0$.
The contour encloses the simple pole $z=-i$, so
$$
-I=2\pi i\Res_{z=-i}\frac{e^{-iz}}{2(z+i)}=2\pi i\cdot\frac{e^{-i(-i)}}2=\frac{\pi i}{e}.
$$
:::

:::

:::

:::
