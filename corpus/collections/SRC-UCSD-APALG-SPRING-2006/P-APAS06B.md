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
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The exam asserted that U is unique for every A, which fails for A=0; the statement now asserts uniqueness of U only when A has rank n.
---

::: {.problem}
Given $A\in M_{m,n}$ with $m\ge n$, prove that there exist a $U\in M_{m,n}$ with orthonormal columns and a unique Hermitian positive semidefinite $H\in M_n$ such that $A=UH$, and that $U$ is also unique when $A$ has rank $n$.
:::

::: {.solution}
Let
$$
A=W\Sigma V^*
$$
be a singular-value decomposition in which $W\in M_{m,n}$ has orthonormal columns, $V\in M_n$ is unitary, and $\Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_n)$ with every $\sigma_i\ge0$. Set
$$
U=WV^*,\qquad H=V\Sigma V^*.
$$
Then
$$
U^*U=VW^*WV^*=I_n,
$$
so $U$ has orthonormal columns, while $H$ is Hermitian positive semidefinite and
$$
UH=WV^*V\Sigma V^*=W\Sigma V^*=A.
$$
Furthermore,
$$
A^*A=V\Sigma^2V^*=H^2.
$$
A Hermitian positive semidefinite matrix has a unique Hermitian positive semidefinite square root, so every factorization $A=U'H'$ with $(U')^*U'=I_n$ and $H'\ge0$ satisfies
$$
(H')^2=A^*A,
$$
and hence $H'=H$. Thus $H$ is always unique.

Suppose now that $A$ has full column rank. Then $A^*A$ is positive definite, so $H$ is invertible. Any factorization $A=UH$ therefore satisfies
$$
U=AH^{-1},
$$
which proves uniqueness of $U$.

:::
