---
schema: qual/card@1
id: P-ALGS06B
kind: problem
title: "Existence and uniqueness of polar decomposition"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
  note: Compared with Question 1.2 of the official Spring 2006 UCSD algebra exam. The source omits the full-column-rank hypothesis needed for uniqueness of U; A=0 is an immediate counterexample. The card states the necessary hypothesis explicitly.
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Given $A \in M_{m,n}(\mathbb C)$ with $m \geq n$ and $\operatorname{rank}A=n$, prove that there exists a unique $U \in M_{m,n}(\mathbb C)$ with orthonormal columns, and a unique Hermitian positive semidefinite $H \in M_n(\mathbb C)$ such that $A = UH$.
(State in detail any auxiliary results used without proof.)
:::

::: remark
The full-column-rank hypothesis is necessary for uniqueness of $U$. For example, if $A=0$, then $H=0$ but every $m\times n$ matrix with orthonormal columns satisfies $A=UH$.
:::

::: {.solution}
<1>1. The matrix $A^*A$ is Hermitian positive definite.
::: {.proof}
It is Hermitian because $(A^*A)^*=A^*A$. For $0\ne x\in\mathbb C^n$,
\[
x^*A^*Ax=\|Ax\|^2>0,
\]
because $\operatorname{rank}A=n$ implies $\ker A=0$.
:::

<1>2. Let
\[
H=(A^*A)^{1/2}
\]
be the unique Hermitian positive definite square root of $A^*A$.
::: {.proof}
We use the spectral theorem: every Hermitian matrix $B$ is unitarily diagonalizable, $B=V\operatorname{diag}(\lambda_1,\dots,\lambda_n)V^*$ with real eigenvalues. If $B$ is positive definite, then every $\lambda_i>0$, and
\[
B^{1/2}=V\operatorname{diag}(\sqrt{\lambda_1},\dots,\sqrt{\lambda_n})V^*
\]
is Hermitian positive definite and is the unique Hermitian positive semidefinite matrix whose square is $B$.
Applying this to $B=A^*A$ defines $H$. Since $H$ is positive definite, it is invertible.
:::

<1>3. Define
\[
U=AH^{-1}.
\]
Then $U$ has orthonormal columns.
::: {.proof}
Using $H^*=H$ and $H^2=A^*A$,
\[
U^*U
=(H^{-1})^*A^*AH^{-1}
=H^{-1}H^2H^{-1}
=I_n.
\]
The identity $U^*U=I_n$ is exactly the condition that the columns of $U$ are orthonormal.
:::

<1>4. The matrices $U$ and $H$ satisfy $A=UH$.
::: {.proof}
By definition,
\[
UH=AH^{-1}H=A.
\]
:::

<1>5. The positive semidefinite factor $H$ is unique.
::: {.proof}
Suppose
\[
A=VK
\]
with $V^*V=I_n$ and $K$ Hermitian positive semidefinite. Then
\[
A^*A=K V^*V K=K^2.
\]
Thus $K$ is a Hermitian positive semidefinite square root of $A^*A$. By the uniqueness stated in <1>2,
\[
K=(A^*A)^{1/2}=H.
\]
:::

<1>6. The orthonormal-column factor $U$ is unique.
::: {.proof}
By <1>5, any factorization has the same factor $H$. Since $H$ is invertible by <1>2,
\[
U=AH^{-1}.
\]
Thus no other $U$ is possible.
:::

<1>7. Therefore the corrected full-column-rank polar decomposition exists and is unique.
::: {.proof}
Existence is <1>2--<1>4 and uniqueness is <1>5--<1>6.
:::
:::
