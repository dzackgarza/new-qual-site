---
schema: qual/card@1
id: P-BERK85S-18
kind: problem
title: A positive-definite Hermitian factor forces $AB$ to have real spectrum
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used the positive-definite Hermitian square root of A to conjugate AB to
    the Hermitian matrix A^{1/2} B A^{1/2}.
---

::: {.problem}
Let $A,B$ be Hermitian $n\times n$ complex matrices, and suppose $A$ is positive definite. Prove that every eigenvalue of $AB$ is real.
:::

::: {.solution}
::: pf

::: {.pf-step #square-root-exists}
The matrix $A$ has an invertible Hermitian positive-definite square
root $S=A^{1/2}$.

::: pf-proof
By the spectral theorem, there is a unitary matrix $U$ and positive real
numbers $\lambda_1,\ldots,\lambda_n$ such that
$$
A
=
U\operatorname{diag}(\lambda_1,\ldots,\lambda_n)U^*.
$$
Set
$$
S
\coloneqq
U\operatorname{diag}(\sqrt{\lambda_1},\ldots,\sqrt{\lambda_n})U^*.
$$
Then $S=S^*$, every eigenvalue of $S$ is positive, $S$ is invertible, and
$S^2=A$.
:::

:::

::: {.pf-step #ab-similar-to-sbs}
The matrix $AB$ is similar to $SBS$.

::: pf-proof
Since $A=S^2$ and $S$ is invertible,
$$
S^{-1}(AB)S
=
S^{-1}S^2BS
=
SBS.
$$
:::

:::

::: {.pf-step #sbs-is-hermitian}
The matrix $SBS$ is Hermitian.

::: pf-proof
Because both $S$ and $B$ are Hermitian,
$$
(SBS)^*
=
S^*B^*S^*
=
SBS.
$$
:::

:::

::: {.pf-step #eigenvalues-real}
Every eigenvalue of $AB$ is real.

::: pf-proof
By step [](#sbs-is-hermitian){.pf-ref} and the spectral theorem, every eigenvalue of the Hermitian
matrix $SBS$ is real. Similar matrices have the same characteristic
polynomial and therefore the same eigenvalues. Step [](#ab-similar-to-sbs){.pf-ref} now gives
$$
\boxed{\text{every eigenvalue of }AB\text{ lies in }\RR}.
$$
:::

:::

::: pf-qed
Step [](#eigenvalues-real){.pf-ref} is the required conclusion.
:::

:::
:::
