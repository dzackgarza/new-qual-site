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
---

::: {.exercise}
\[
I = \int_\RR {x\sin(x) \over 1 + x^2}\dx
.\]

:::

::: {.solution}
Write $f(z) = {ze^{iz} \over 1+z^2}$. Since $f\in \bigo\qty{1\over z}$ on the semicircle of radius $R$, whose length is $\pi R$, the ML estimate bounds the arc integral only by a constant; Jordan's lemma gives decay:

![Semicircular contour](../../assets/Complex_Analysis/040_Residues/figures/2021-12-23_18-14-14.png)

Write $f(z) = e^{iz}g(z)$ where $g(z) \definedas {z\over 1 + z^2}$.
Write $C_1 = [-R, R]$ and $C_R = \theset{Re^{it} \st t\in [0, \pi]}$. By Jordan's lemma,
\[
\abs{\int_{C_R} e^{iz} g(z)\dz }\leq \pi M_R,\, \qquad M_R \definedas \sup_{z\in C_R}\abs{z\over 1+z^2}\leq {R\over R^2-1}
,\]
so the arc integral tends to zero.
By the residue theorem,
\[
2\pi i \sum_{z_k\in \HH}\Res_{z=z_k}f(z) = \qty{\int_{C_1} + \int_{C_R}}f \converges{R\to\infty} \int_\RR {xe^{ix}\over 1+x^2}\dx
,\]
and $I$ is the imaginary part of the right side.
Since $1+z^2 = (z+i)(z-i)$, the only pole in $\HH$ is the simple pole $z = i$, and
\[
2\pi i \Res_{z=i} f(z) 
&= 2\pi i \lim_{z\to i} {ze^{iz} \over z+i} \\
&= 2\pi i {ie^{-1}\over 2i} = {\pi i \over e}
,\]
so
\[
I = \Im{\pi i\over e} = {\pi \over e}
.\]
:::
