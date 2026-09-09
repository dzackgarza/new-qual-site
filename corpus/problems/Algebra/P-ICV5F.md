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

::: problem
Prove that the eigenvalues of a Hermitian matrix are real and those of a unitary matrix are unitary.
:::


::: {.solution}
<1>1. Every eigenvalue of a Hermitian matrix is real.
::: {.proof}
Let $A=A^*$ and let $Av=\lambda v$ with $v\ne0$. Then
\[
\lambda\langle v,v\rangle
=\langle Av,v\rangle
=\langle v,A^*v\rangle
=\langle v,Av\rangle
=\overline\lambda\langle v,v\rangle.
\]
Since $\langle v,v\rangle>0$, one gets $\lambda=\overline\lambda$, so $\lambda\in\RR$.
:::

<1>2. Every eigenvalue of a unitary matrix has modulus $1$.
::: {.proof}
Let $U^*U=I$ and $Uv=\lambda v$ with $v\ne0$. Unitary matrices preserve norms, so
\[
\|v\|=\|Uv\|=\|\lambda v\|=|\lambda|\,\|v\|.
\]
Thus $|\lambda|=1$.
:::
:::
