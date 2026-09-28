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
---

::: {.exercise}
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
Both are $e^{\pm iz}g(z)$ with $g(z)={1\over 2(z+i)}\to0$ as $\abs z\to\infty$, so Jordan's lemma applies on semicircles: for $e^{i\alpha z}$ with $\alpha>0$ on the upper half-plane (for $f_1$), and with $\alpha<0$ on the lower half-plane (for $f_2$). For $f_1$, use the upper contour:

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
&= \pi i \inverseof{e}
,\]
so
\[
I = -{i\pi \over e}
.\]
:::
