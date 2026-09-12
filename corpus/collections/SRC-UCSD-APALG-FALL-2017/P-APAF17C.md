---
schema: qual/card@1
id: P-APAF17C
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

::: problem
Let $A,B\in\mathbb{R}^{n\times n}$ be two real symmetric positive definite matrices.
If $A-B$ is positive definite, is $B^{-1}-A^{-1}$ also positive definite?
If yes, give a proof; if not, give a counterexample.
:::

::: {.solution}
Yes. In fact,
\[
A-B>0\qquad\Longrightarrow\qquad B^{-1}-A^{-1}>0.
\]

<1>1. Put
\[
C=B^{-1/2}AB^{-1/2}.
\]
Then $C$ is symmetric positive definite and
\[
C-I=B^{-1/2}(A-B)B^{-1/2}>0.
\]
::: {.proof}
A congruence by an invertible matrix preserves positive definiteness: if $M>0$ and $S$ is invertible, then for $x\ne0$,
\[
x^TS^TMSx=(Sx)^TM(Sx)>0.
\]
Apply this to $M=A-B$ and $S=B^{-1/2}$. Also $C$ is positive definite by the same argument applied to $A$.
:::

<1>2. One has
\[
I-C^{-1}>0.
\]
::: {.proof}
By the real spectral theorem, there is an orthogonal matrix $Q$ and positive eigenvalues $\lambda_1,\ldots,\lambda_n$ such that
\[
C=Q\operatorname{diag}(\lambda_1,\ldots,\lambda_n)Q^T.
\]
Since $C-I>0$, all eigenvalues satisfy $\lambda_i>1$. Therefore
\[
I-C^{-1}
=Q\operatorname{diag}\left(1-\lambda_1^{-1},\ldots,1-\lambda_n^{-1}\right)Q^T,
\]
and every diagonal entry $1-\lambda_i^{-1}$ is positive. Hence $I-C^{-1}>0$.
:::

<1>3. Therefore
\[
B^{-1}-A^{-1}>0.
\]
::: {.proof}
Since
\[
A=B^{1/2}CB^{1/2},
\]
inverting gives
\[
A^{-1}=B^{-1/2}C^{-1}B^{-1/2}.
\]
Also
\[
B^{-1}=B^{-1/2}IB^{-1/2}.
\]
Thus
\[
B^{-1}-A^{-1}
=B^{-1/2}(I-C^{-1})B^{-1/2}.
\]
By <1>2 the middle factor is positive definite, and congruence by the invertible matrix $B^{-1/2}$ preserves positive definiteness. Hence the difference is positive definite.
:::
:::
