---
schema: qual/card@1
id: P-APAF18C
kind: problem
title: Positive-definiteness of $B^{-1}-A^{-1}$ when $A-B$ is positive definite
classification:
  areas:
  - applied-algebra
  topics:
  - Positive Definite Matrices
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $A,B\in\mathbb{R}^{n\times n}$ be two symmetric positive definite matrices.
If $A-B$ is positive definite, is $B^{-1}-A^{-1}$ necessarily positive definite?
If yes, give a proof; if no, give a counterexample.
:::

::: {.solution}
Yes.

<1>1. Set
\[
C=B^{-1/2}AB^{-1/2}.
\]
Then $C$ is symmetric positive definite and $C-I$ is positive definite.
::: {.proof}
Because $B$ is symmetric positive definite, the symmetric positive definite square root $B^{1/2}$ exists and is invertible. Congruence preserves positive definiteness, so
\[
C=B^{-1/2}AB^{-1/2}>0.
\]
Moreover
\[
C-I=B^{-1/2}(A-B)B^{-1/2}>0
\]
by the hypothesis $A-B>0$.
:::

<1>2. One has
\[
I-C^{-1}>0.
\]
::: {.proof}
By the spectral theorem, there is an orthogonal matrix $Q$ and positive eigenvalues $\lambda_1,\ldots,\lambda_n$ such that
\[
C=Q\operatorname{diag}(\lambda_1,\ldots,\lambda_n)Q^T.
\]
Since $C-I>0$, every eigenvalue of $C-I$ is positive, so
\[
\lambda_i-1>0,
\qquad\text{hence}\qquad
\lambda_i>1
\]
for all $i$. Therefore
\[
1-\lambda_i^{-1}>0
\]
for every $i$, and thus
\[
I-C^{-1}
=Q\operatorname{diag}(1-\lambda_1^{-1},\ldots,1-\lambda_n^{-1})Q^T
>0.
\]
:::

<1>3. The matrix $B^{-1}-A^{-1}$ is positive definite.
::: {.proof}
Since
\[
A=B^{1/2}CB^{1/2},
\]
we have
\[
A^{-1}=B^{-1/2}C^{-1}B^{-1/2}.
\]
Also
\[
B^{-1}=B^{-1/2}IB^{-1/2}.
\]
Hence
\[
B^{-1}-A^{-1}
=B^{-1/2}(I-C^{-1})B^{-1/2}.
\]
By <1>2 the middle factor is positive definite, and congruence by the invertible matrix $B^{-1/2}$ preserves positive definiteness. Therefore
\[
\boxed{B^{-1}-A^{-1}>0}.
\]
:::
:::
