---
schema: qual/card@1
id: P-APAS06B
kind: problem
title: Polar factorization $A=UH$ for tall $A\in M_{m,n}$
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
  by: OpenAI
  date: 2026-09-10
---

::: problem
Given $A\in M_{m,n}$ with $m\ge n$, prove that there exists a unique $U\in M_{m,n}$ with orthonormal columns, and a unique Hermitian positive semidefinite $H\in M_n$ such that $A=UH$.
:::

::: solution
The uniqueness assertion for $U$ is false as printed when $A$ is rank-deficient. For example, if $A=0$, then necessarily $H=0$, but every $m\times n$ matrix with orthonormal columns satisfies $A=UH$. Thus $U$ is not unique as soon as there is more than one such isometry.

The correct polar-factorization statement is the following: for every $A\in M_{m,n}$ with $m\ge n$, there is a unique Hermitian positive semidefinite matrix
\[
H=(A^*A)^{1/2}
\]
and at least one $U\in M_{m,n}$ with orthonormal columns such that $A=UH$. Moreover, $U$ is unique if and only if $A$ has full column rank $n$.

Indeed, let
\[
A=W\Sigma V^*
\]
be a singular-value decomposition in which $W\in M_{m,n}$ has orthonormal columns, $V\in M_n$ is unitary, and $\Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_n)$ with every $\sigma_i\ge0$. Set
\[
U=WV^*,\qquad H=V\Sigma V^*.
\]
Then
\[
U^*U=VW^*WV^*=I_n,
\]
so $U$ has orthonormal columns, while $H$ is Hermitian positive semidefinite and
\[
UH=WV^*V\Sigma V^*=W\Sigma V^*=A.
\]
Furthermore,
\[
A^*A=V\Sigma^2V^*=H^2.
\]
A Hermitian positive semidefinite matrix has a unique Hermitian positive semidefinite square root, so every factorization $A=U'H'$ with $(U')^*U'=I_n$ and $H'\ge0$ satisfies
\[
(H')^2=A^*A,
\]
and hence $H'=H$. Thus $H$ is always unique.

Suppose now that $A$ has full column rank. Then $A^*A$ is positive definite, so $H$ is invertible. Any factorization $A=UH$ therefore satisfies
\[
U=AH^{-1},
\]
which proves uniqueness of $U$.

Conversely, suppose $\operatorname{rank}A<n$. Then $\ker H=\ker A$ is nonzero. In the singular-value decomposition above, after reordering the singular values we may write
\[
\Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_r,0,\ldots,0),
\qquad r<n.
\]
Choose a unitary diagonal matrix
\[
D=\operatorname{diag}(1,\ldots,1,-1,1,\ldots,1)
\]
whose $-1$ occurs in one of the zero-singular-value positions. Then $D\Sigma=\Sigma$, so
\[
U'=WDV^*
\]
also has orthonormal columns and
\[
U'H=WDV^*V\Sigma V^*=WD\Sigma V^*=W\Sigma V^*=A.
\]
But $U'\ne U$. Hence $U$ is not unique when $A$ fails to have full column rank.
:::
