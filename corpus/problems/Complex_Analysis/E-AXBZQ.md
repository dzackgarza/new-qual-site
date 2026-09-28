---
schema: qual/card@1
id: E-AXBZQ
kind: problem
title: $\int_\RR\frac{x\sin x}{1+x^2}\,dx$ and $\int_\RR\frac{\cos x}{x+i}\,dx$ by Jordan's
  lemma
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

Write $f(z) = e^{iz}g(z)$ where $g(z) \da {z\over 1 + z^2}$.
Write $C_1 = [-R, R]$ and $C_R = \ts{Re^{it} \st t\in [0, \pi]}$. By Jordan's lemma,
\[
\abs{\int_{C_R} e^{iz} g(z)\dz }\leq \pi M_R,\, \qquad M_R \da \sup_{z\in C_R}\abs{z\over 1+z^2}\leq {R\over R^2-1}
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

::: {.exercise title="$\cos(x) / i+x$"}
\[
I \da \int_\RR {\cos(x) \over x+i}\dx
.\]

:::

::: {.solution}
Since $x+i$ is not real, ${\cos(x) \over x+i}\neq \Re\qty{e^{ix}\over x+i}$.
Use $\cos(z) = {1\over 2}(e^{iz} + e^{-iz})$ to decompose into two integrals:
\[
I \da \int_\RR {\cos(x) \over x+i}\dx 
= \int_\RR f_1 + \int_\RR f_2,
\qquad
f_1(z)\da{e^{iz} \over 2(z+i)},\quad f_2(z)\da{e^{-iz} \over 2(z+i)}
.\]
Both are $e^{\pm iz}g(z)$ with $g(z)={1\over 2(z+i)}\to0$ as $\abs z\to\infty$, so Jordan's lemma applies on semicircles: for $e^{i\alpha z}$ with $\alpha>0$ on the upper half-plane (for $f_1$), and with $\alpha<0$ on the lower half-plane (for $f_2$).
For $f_1$, use the upper contour:

![Semicircular contour](../../assets/Complex_Analysis/040_Residues/figures/2021-12-23_18-14-14.png)

By Jordan's lemma the arc integral tends to $0$, so $\int_\RR f_1$ is $2\pi i$ times the sum of the residues of $f_1$ in $\HH$.
The only pole of $f_1$ is $z=-i\notin\HH$, so $\int_\RR f_1=0$ and $I=\int_\RR f_2$.
For $f_2$, use the lower contour:

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-23_18-39-11.png)

With counterclockwise orientation, the real axis is traversed from $R$ to $-R$, so the piece along $\RR$ converges to $-\int_\RR f_2=-I$.
By Jordan's lemma the arc integral tends to $0$, so
\[
-I 
&= 2\pi i \Res_{z=-i} {e^{-iz}\over 2(z+i)} \\
&= 2\pi i \cdot{e^{-i(-i)}\over 2} \\
&= \pi i e\inv
,\]
so 
\[
I = -{i\pi \over e}
.\]
:::

