---
schema: qual/card@1
id: E-DUK6M
kind: problem
title: $\int_\RR\frac{xe^{2ix}}{x^2-1}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
---

::: {.exercise}
\[
I \da \int_\RR {xe^{2ix} \over x^2-1}\dx = i\pi \cos(2)
.\]

:::

::: {.solution}
Let $f(z)={ze^{2iz}\over z^2-1}$. The denominator is $(z-1)(z+1)$, so $f$ has simple poles at $\pm1$ on $\RR$, and $I$ is a principal value there.
For $0<\eps<1<R$, define the contour

- $C_1: [-R, -1-\eps]$, $[-1+\eps, 1-\eps]$ and $[1+\eps, R]$ on the real axis
- $C_2: -1 + \eps e^{it}$, $t$ from $\pi$ to $0$ (clockwise, above $-1$)
- $C_4: 1 + \eps e^{it}$, $t$ from $\pi$ to $0$ (clockwise, above $1$)
- $C_R: Re^{it}, t\in [0, \pi]$
- $\Gamma = C_1 + C_2 + C_4 + C_R$

The contour is the semicircle indented at both poles:

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-21_01-47-37.png)

$\int_\Gamma f = 0$ since $\Gamma$ encloses no singularities.
By Jordan's lemma, $\int_{C_R}f\to 0$, since $\abs{z/(z^2-1)}\le R/(R^2-1)$ on $C_R$.
A clockwise half-circle about a simple pole contributes $-\pi i$ times the residue in the limit $\eps\to0$.
With
\[
\Res_{z=-1} f(z) = \lim_{z\to -1} {ze^{2iz} \over z-1} = {e^{-2i} \over 2},
\qquad
\Res_{z=1} f(z) = \lim_{z\to 1} {ze^{2iz} \over z+1} = {e^{2i} \over 2}
,\]
letting $\eps\to0$ and $R\to\infty$ gives
\[
0 = I - \pi i\qty{{e^{-2i} \over 2} + {e^{2i}\over 2}}
,\]
so
\[
I = \pi i \cos(2)
.\]
:::

