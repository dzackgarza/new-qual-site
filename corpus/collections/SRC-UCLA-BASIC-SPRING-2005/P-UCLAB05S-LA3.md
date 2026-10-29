---
schema: qual/card@1
id: P-UCLAB05S-LA3
kind: problem
title: Factorization of a positive semidefinite Hermitian matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra Problem 3 of the official UCLA Basic Exam, May 2005 PDF.
---

::: {.problem}
Let $A$ be a Hermitian-symmetric $n\times n$ complex matrix.
Show that if
\[
\langle Av,v\rangle\geq0
\qquad\text{for every }v\in\CC^n,
\]
then there exists an $n\times n$ matrix $T$ such that
\[
A=T^*T.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

By the spectral theorem, there are a unitary matrix $U$ and real numbers $\lambda_1,\ldots,\lambda_n$ such that
$$
A=UDU^*,
\qquad
D=\operatorname{diag}(\lambda_1,\ldots,\lambda_n).
$$


::: pf-proof

Since $A$ is Hermitian, the spectral theorem for Hermitian matrices gives a unitary basis of eigenvectors. In that basis $A$ is diagonal with real eigenvalues, which is exactly the displayed decomposition.

:::

:::

::: {.pf-step #s1-2}

Every eigenvalue $\lambda_i$ is nonnegative.


::: pf-proof

Let $u_i$ be a unit eigenvector with eigenvalue $\lambda_i$. Then
$$
\langle Au_i,u_i\rangle
=\langle \lambda_i u_i,u_i\rangle
=\lambda_i\langle u_i,u_i\rangle
=\lambda_i.
$$
The hypothesis therefore implies $\lambda_i\ge0$.

:::

:::

::: {.pf-step #s1-3}

Define
$$
D^{1/2}\coloneqq
\operatorname{diag}(\sqrt{\lambda_1},\ldots,\sqrt{\lambda_n})
$$
and
$$
\boxed{T\coloneqq D^{1/2}U^*.}
$$
Then
$$
\boxed{A=T^*T}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, the square roots are real and defined. Since $D^{1/2}$ is Hermitian,
$$
T^*=UD^{1/2}.
$$
Hence
$$
T^*T
=UD^{1/2}D^{1/2}U^*
=UDU^*
=A
$$
by step [](#s1-1){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} constructs the required matrix $T$ and verifies the factorization.

:::

:::

:::
