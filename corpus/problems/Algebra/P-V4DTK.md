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

::: problem
Describe the irreducible representations of the compact Lie groups $\operatorname{SO}(2)$ and $\operatorname{SO}(3)$ over $\mathbb{C}$ and $\mathbb{R}$.
:::

::: solution
For $\operatorname{SO}(2)\cong S^1$, every irreducible complex representation is one-dimensional because the group is abelian. They are
\[
\chi_n(R_\theta)=e^{in\theta},\qquad n\in\mathbb Z.
\]
Over $\mathbb R$, the irreducibles are the trivial one-dimensional representation and, for each $m\ge1$, the two-dimensional rotation representation
\[
R_\theta\longmapsto
\begin{pmatrix}
\cos(m\theta)&-\sin(m\theta)\\
\sin(m\theta)&\cos(m\theta)
\end{pmatrix}.
\]

For $\operatorname{SO}(3)$, use the double cover
\[
\operatorname{SU}(2)\to\operatorname{SO}(3).
\]
The irreducible complex representations of $\operatorname{SU}(2)$ are
\[
\operatorname{Sym}^m(\mathbb C^2),\qquad m\ge0,
\]
of dimension $m+1$. The central element $-I$ acts by $(-1)^m$, so the representation descends to $\operatorname{SO}(3)$ exactly when $m=2\ell$ is even. Hence the irreducible complex representations of $\operatorname{SO}(3)$ are indexed by $\ell\ge0$ and have dimensions
\[
2\ell+1.
\]
They may be realized as the degree-$\ell$ spherical harmonics. These models are defined over $\mathbb R$, giving the irreducible real representations of the same dimensions.
:::
