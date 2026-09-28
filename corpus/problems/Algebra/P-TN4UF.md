---
schema: qual/card@1
id: P-TN4UF
kind: problem
title: Finite-dimensional representations of a compact Lie group are equivalent to unitary ones
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Semisimplicity
  - Inner Product Spaces
relations: []
review: draft
---

::: {.problem}
Let $G$ be a compact Lie group and let $\rho:G\to GL(V)$ be a finite-dimensional continuous complex representation. Show that $\rho$ is equivalent to a unitary representation.
:::

::: {.solution}
Choose any Hermitian inner product $\langle-,-\rangle_0$ on $V$. Let $\mu$ be normalized Haar probability measure on the compact group $G$. Define
\[
\langle v,w\rangle_G
=\int_G\langle \rho(g)v,\rho(g)w\rangle_0\,d\mu(g).
\]
This is again a Hermitian inner product: positivity follows because the integrand is continuous and nonnegative, and for $v\ne0$ its value at the identity is positive.

For $h\in G$, left invariance of Haar measure gives
\[
\begin{aligned}
\langle\rho(h)v,\rho(h)w\rangle_G
&=\int_G\langle\rho(g)\rho(h)v,\rho(g)\rho(h)w\rangle_0\,d\mu(g)\\
&=\int_G\langle\rho(gh)v,\rho(gh)w\rangle_0\,d\mu(g)\\
&=\langle v,w\rangle_G.
\end{aligned}
\]
Thus every $\rho(h)$ is unitary with respect to $\langle-,-\rangle_G$.

Choose an orthonormal basis for this invariant Hermitian form. In that basis, all matrices $\rho(g)$ are unitary. Hence the original representation is equivalent to a unitary representation.
:::
