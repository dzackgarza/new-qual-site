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
Let $G$ be a compact Lie group and let $\rho:G\to \GL(V)$ be a finite-dimensional continuous complex representation. Show that $\rho$ is equivalent to a unitary representation.
:::

::: {.solution}
Choose a Hermitian inner product $\inner{-}{-}_0$ on $V$, and let $\mu$ be the Haar probability measure on $G$, which is both left and right invariant because $G$ is compact.

::: pf

::: {.pf-step #average}
$\inner{v}{w}_G\coloneqq\int_G\inner{\rho(g)v}{\rho(g)w}_0\,d\mu(g)$ is a Hermitian inner product on $V$.

::: pf-proof
It is sesquilinear and Hermitian because the integrand is.
For $v\ne0$ the integrand $g\mapsto\inner{\rho(g)v}{\rho(g)v}_0$ is continuous, nonnegative, and positive at the identity, so it is positive on an open neighbourhood of the identity, which has positive Haar measure; hence $\inner{v}{v}_G>0$.
:::

:::

::: {.pf-step #invariant}
Every $\rho(h)$ is unitary for $\inner{-}{-}_G$.

::: pf-proof
By right invariance of $\mu$,
$$
\begin{aligned}
\inner{\rho(h)v}{\rho(h)w}_G
&=\int_G\inner{\rho(gh)v}{\rho(gh)w}_0\,d\mu(g)\\
&=\int_G\inner{\rho(g)v}{\rho(g)w}_0\,d\mu(g)
=\inner{v}{w}_G.
\end{aligned}
$$
:::

:::

::: pf-step
$\rho$ is equivalent to a unitary representation.

::: pf-proof
Let $P:\CC^n\to V$ send the standard basis to an orthonormal basis for $\inner{-}{-}_G$.
By step [](#invariant){.pf-ref}, each $P^{-1}\rho(g)P$ is a unitary matrix, so $g\mapsto P^{-1}\rho(g)P$ is a unitary representation equivalent to $\rho$.
:::

:::

:::

:::
