---
schema: qual/card@1
id: P-V4DTK
kind: problem
title: Irreducible representations of $\SO(2)$ and $\SO(3)$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Matrix Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Describe the irreducible representations of the compact Lie groups $\SO(2)$ and $\SO(3)$ over $\CC$ and $\RR$.
:::

::: {.solution}
Write $R_\theta$ for rotation by $\theta$ in $\SO(2)$.

::: pf

::: pf-step
The irreducible complex representations of $\SO(2)$ are the characters $\chi_n(R_\theta)=e^{in\theta}$, $n\in\ZZ$.

::: pf-proof
The group $\SO(2)\cong S^1$ is abelian, so every irreducible complex representation is one-dimensional, that is, a continuous homomorphism $S^1\to\CC^\times$; these are the $\chi_n$, $n\in\ZZ$.
:::

:::

::: pf-step
The irreducible real representations of $\SO(2)$ are the trivial one-dimensional representation and, for each $m\ge1$, the two-dimensional representation
$$
R_\theta\longmapsto
\begin{pmatrix}
\cos(m\theta)&-\sin(m\theta)\\
\sin(m\theta)&\cos(m\theta)
\end{pmatrix}.
$$

::: pf-proof
For $m\ge1$ the complex characters $\chi_m$ and $\chi_{-m}$ are complex conjugates, and their sum is the complexification of the displayed real representation, which has no real invariant line.
The character $\chi_0$ is real and gives the trivial representation.
:::

:::

::: pf-step
The irreducible complex representations of $\SO(3)$ are indexed by $\ell\ge0$ and have dimensions $2\ell+1$.

::: pf-proof
Use the double cover $\SU(2)\to\SO(3)$ with kernel $\{\pm I\}$.
The irreducible complex representations of $\SU(2)$ are $\Sym^m(\CC^2)$, $m\ge0$, of dimension $m+1$.
The central element $-I$ acts by $(-1)^m$, so the representation descends to $\SO(3)$ exactly when $m=2\ell$ is even.
:::

:::

::: pf-step
The irreducible real representations of $\SO(3)$ also have dimensions $2\ell+1$, $\ell\ge0$.

::: pf-proof
The complex representation of dimension $2\ell+1$ is realized as the degree-$\ell$ spherical harmonics, which are defined over $\RR$.
These real models give the irreducible real representations of the same dimensions.
:::

:::

:::
:::
