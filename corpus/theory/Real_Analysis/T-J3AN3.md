---
schema: qual/card@1
id: T-J3AN3
kind: theorem
title: Riesz-Fischer
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
Let $U = \theset{u_n}_{n=1}^\infty$ be an orthonormal set in a Hilbert space $\mathcal H$, and let $\mathcal H_U = \overline{\operatorname{span}} U$.
Then the coefficient map
\[
\mathcal H_U &\longrightarrow \ell^2(\NN) \\
\vector x &\longmapsto
\theset{\inner{\vector x}{\vector u_n}}_{n=1}^\infty
\]
is an isometric isomorphism.
Equivalently, for every $\theset{a_n}\in\ell^2(\NN)$ there is a unique $\vector x\in\mathcal H_U$ such that
\[
a_n=\inner{\vector x}{\vector u_n}\quad\text{for all }n,
\qquad
\norm{\vector x}^2=\sum_{n=1}^\infty\abs{a_n}^2.
\]

In particular, if $U$ is complete, so $\mathcal H_U=\mathcal H$, then the coefficient map $\mathcal H\to\ell^2(\NN)$ is an isometric isomorphism.
:::

::: {.proof}
For $a=(a_n)\in\ell^2(\NN)$, set
\[
x_N=\sum_{n=1}^N a_nu_n.
\]
Orthogonality gives
\[
\norm{x_N-x_M}^2=\sum_{n=M+1}^N\abs{a_n}^2,
\]
so $(x_N)$ is Cauchy and converges, by completeness of $\mathcal H$, to some $x\in\mathcal H_U$.
Continuity of the inner product yields $\inner{x}{u_n}=a_n$ for every $n$, and taking limits in $\norm{x_N}^2=\sum_{n=1}^N\abs{a_n}^2$ gives
\[
\norm{x}^2=\sum_{n=1}^\infty\abs{a_n}^2.
\]

Conversely, let $x\in\mathcal H_U$ and put $a_n=\inner{x}{u_n}$.
Bessel's inequality gives $a\in\ell^2$.
Applying the construction above produces $y\in\mathcal H_U$ with the same coefficients.
Then $x-y\in\mathcal H_U$ is orthogonal to every $u_n$, hence to $\operatorname{span}U$ and therefore to its closure $\mathcal H_U$; thus $x-y=0$.
This proves both bijectivity and the norm identity.
:::
