---
schema: qual/card@1
id: T-J3AN3
kind: theorem
title: Riesz--Fischer theorem
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

::: {.proof}
For $a=(a_n)\in\ell^2(\NN)$, set
$$
x_N\coloneqq\sum_{n=1}^N a_nu_n.
$$
Orthonormality gives, for $M<N$,
$$
\norm{x_N-x_M}^2=\sum_{n=M+1}^N\abs{a_n}^2,
$$
so $(x_N)$ is Cauchy and converges, by completeness of $\mathcal H$, to some $x$, which lies in $\mathcal H_U$ because each $x_N$ lies in the span of $U$.
Continuity of the inner product yields $\inner{x}{u_n}=a_n$ for every $n$, and taking limits in $\norm{x_N}^2=\sum_{n=1}^N\abs{a_n}^2$ gives
$$
\norm{x}^2=\sum_{n=1}^\infty\abs{a_n}^2.
$$

Conversely, let $x\in\mathcal H_U$ and put $a_n\coloneqq\inner{x}{u_n}$.
Bessel's inequality [[T-4BDE3]] gives $a\in\ell^2(\NN)$.
Applying the construction above produces $y\in\mathcal H_U$ with the same coefficients.
Then $x-y\in\mathcal H_U$ is orthogonal to every $u_n$, hence to the span of $U$ and therefore to its closure $\mathcal H_U$; in particular $x-y$ is orthogonal to itself, so $x=y$.
This proves bijectivity and the norm identity.
:::
