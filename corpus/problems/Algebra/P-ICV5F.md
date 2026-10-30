---
schema: qual/card@1
id: P-ICV5F
kind: problem
title: Eigenvalues of Hermitian matrices are real, and eigenvalues of unitary matrices
  have modulus $1$
classification:
  areas:
  - algebra
  topics:
  - Eigenvalues and Eigenvectors
  - Inner Product Spaces
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Prove that the eigenvalues of a Hermitian matrix are real and those of a unitary matrix have modulus $1$.
:::

::: {.solution}
Write $\inner{v}{w}=\sum_i v_i\overline{w_i}$ for the standard Hermitian inner product on $\CC^n$ and $\norm{v}=\inner{v}{v}^{1/2}$.

::: pf

::: pf-step

Every eigenvalue of a Hermitian matrix is real.

::: pf-proof

Let $A=A^*$ and let $Av=\lambda v$ with $v\ne0$. Then
$$
\lambda\inner{v}{v}
=\inner{Av}{v}
=\inner{v}{A^*v}
=\inner{v}{Av}
=\overline\lambda\inner{v}{v}.
$$
Since $\inner{v}{v}>0$, one gets $\lambda=\overline\lambda$, so $\lambda\in\RR$.

:::

:::

::: pf-step

Every eigenvalue of a unitary matrix has modulus $1$.

::: pf-proof

Let $U^*U=I$ and $Uv=\lambda v$ with $v\ne0$. Unitary matrices preserve norms, so
$$
\norm{v}=\norm{Uv}=\norm{\lambda v}=\abs{\lambda}\,\norm{v}.
$$
Thus $\abs{\lambda}=1$.

:::

:::

:::

:::
