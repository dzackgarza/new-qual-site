---
schema: qual/card@1
id: T-J3AN3
kind: theorem
title: Riesz--Fischer theorem
slogan: 'An orthonormal sequence identifies its closed span isometrically with $\ell^2$ through Fourier coefficients.'
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - L²
  - Bases
relations: []
review: draft
---

::: {.theorem}
Let $\mathcal H$ be a [[D-7QQUO|Hilbert space]], let $U = (u_n)_{n\geq1}$ be an [[D-4IXAO|orthonormal]] sequence in $\mathcal H$, and let $\mathcal H_U\subseteq\mathcal H$ be the closure of the linear span of $\theset{u_n\suchthat n\geq1}$.
Then the coefficient map
$$
\begin{aligned}
\mathcal H_U &\longrightarrow \ell^2(\NN) \\
x &\longmapsto
(\inner{x}{u_n})_{n\geq1}
\end{aligned}
$$
is an isometric isomorphism.
Equivalently, for every $(a_n)_{n\geq1}\in\ell^2(\NN)$ there is a unique $x\in\mathcal H_U$ such that
$$
a_n=\inner{x}{u_n}\quad\text{for all }n,
\qquad\text{and then}\qquad
\norm{x}^2=\sum_{n=1}^\infty\abs{a_n}^2.
$$

In particular, if $U$ is [[D-SLYE5|complete]], so that $\mathcal H_U=\mathcal H$, then the coefficient map $\mathcal H\to\ell^2(\NN)$ is an isometric isomorphism.
:::
