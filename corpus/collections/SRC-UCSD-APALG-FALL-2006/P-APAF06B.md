---
schema: qual/card@1
id: P-APAF06B
kind: problem
title: Unique factorization $A=UH$ with orthonormal columns and Hermitian positive semidefinite $H$
classification:
  areas:
  - applied-algebra
  topics:
  - Singular Values
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Given $A \in M_{m,n}$ with $m \geq n$, prove that there exists a unique $U \in M_{m,n}$ with orthonormal columns, and a unique Hermitian positive semidefinite $H \in M_n$ such that $A = UH$.

(State in detail any auxiliary results that you use.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Uniqueness of the positive semidefinite factor $H$:

::: pf-proof

::: pf-step

Suppose $A = UH$ with $U \in M_{m,n}$ satisfying $U^* U = I_n$ and $H \in M_n$ Hermitian positive semidefinite ($H = H^* \ge 0$).

::: pf-proof

setup.

:::

:::

::: pf-step

Compute the Gram matrix $A^* A$:
\[
A^* A = (UH)^* (UH) = H^* (U^* U) H = H I_n H = H^2.
\]

::: pf-proof

properties of the adjoint and $U^* U = I_n$.

:::

:::

::: pf-step

Since $x^* (A^* A) x = \|Ax\|^2 \ge 0$, $A^* A$ is a Hermitian positive semidefinite matrix in $M_n$.

::: pf-proof

definition of positive semidefiniteness.

:::

:::

::: pf-step

By the Spectral Theorem, every Hermitian positive semidefinite matrix has a **unique** Hermitian positive semidefinite square root.
Thus $H$ must be uniquely given by:
\[
H = \sqrt{A^* A}.
\]

::: pf-proof

Spectral Theorem for normal matrices.

:::

:::

:::

:::

::: {.pf-step #s2}

Existence of $U$ and $H$ via the Singular Value Decomposition (SVD):

::: pf-proof

::: pf-step

By the SVD for rectangular matrices, write $A = V \Sigma W^*$ where $V \in M_{m,n}$ has orthonormal columns ($V^* V = I_n$), $W \in M_n$ is unitary ($W^* W = I_n$), and $\Sigma = \operatorname{diag}(\sigma_1, \dots, \sigma_n)$ with $\sigma_1 \ge \cdots \ge \sigma_n \ge 0$.

::: pf-proof

Singular Value Decomposition Theorem.

:::

:::

::: pf-step

Compute $A^* A = (W \Sigma V^*)(V \Sigma W^*) = W \Sigma^2 W^*$, which gives:
\[
H = \sqrt{A^* A} = W \Sigma W^*.
\]
$H$ is Hermitian ($H^* = W \Sigma W^* = H$) and positive semidefinite (eigenvalues $\sigma_i \ge 0$).

::: pf-proof

spectral decomposition of $A^* A$.

:::

:::

::: pf-step

Define $U = V W^* \in M_{m,n}$.
Compute $U^* U = (W V^*)(V W^*) = W I_n W^* = I_n$, so $U$ has orthonormal columns.

::: pf-proof

unitary invariance of inner products.

:::

:::

::: pf-step

Check the product:
\[
UH = (V W^*) (W \Sigma W^*) = V \Sigma W^* = A.
\]

::: pf-proof

$W^* W = I_n$.

:::

:::

:::

:::

::: {.pf-step #s3}

Uniqueness of $U$ when $A$ has full column rank:

::: pf-proof

::: pf-step

If $A$ has full column rank $n$, all singular values $\sigma_i > 0$, so $H$ is strictly positive definite and invertible.

::: pf-proof

eigenvalues of $H$ are the singular values of $A$.

:::

:::

::: pf-step

Multiplying $A = UH$ on the right by $H^{-1}$ yields:
\[
U = A H^{-1},
\]
which proves $U$ is uniquely determined.

::: pf-proof

invertibility of $H$.

:::

:::

::: pf-step

When $\operatorname{rank}(A) < n$, $U$ is uniquely determined on the subspace $\operatorname{im}(H) = (\ker A)^\perp$, and any isometric extension to $\ker H$ provides a valid polar factor $U$.

::: pf-proof

orthogonal decomposition $\mathbb{C}^n = \operatorname{im}(H) \oplus \ker(H)$.

:::

:::

:::

:::

::: pf-step

Conclusion:
$A = UH$ exists with $H = \sqrt{A^* A}$ unique, and $U$ unique whenever $A$ has full column rank. Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
