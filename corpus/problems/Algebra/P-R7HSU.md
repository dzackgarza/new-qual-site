---
schema: qual/card@1
id: P-R7HSU
kind: problem
title: The cokernel of $A\in M_n(\mathbb{Z})$ is finite iff $\det A\neq 0$, with order
  $|\det A|$
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Determinants
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $A \in M_n(\mathbb{Z})$ be an $n \times n$ matrix with integer entries, viewed as a $\mathbb{Z}$-module homomorphism $A: \mathbb{Z}^n \to \mathbb{Z}^n$.
(1) Prove that the cokernel $\operatorname{coker}(A) = \mathbb{Z}^n / \operatorname{im}(A)$ is **finite** if and only if $\det(A) \ne 0$.
(2) Prove that when $\det(A) \ne 0$, the order of the cokernel is given by:
$$|\operatorname{coker}(A)| = |\det(A)|.$$
:::

::: solution
Take Smith normal form
\[
UAV=\operatorname{diag}(d_1,\dots,d_n),
\]
with $U,V\in\operatorname{GL}_n(\mathbb Z)$ and $d_1\mid\cdots\mid d_n$, allowing some $d_i=0$. Since $U$ and $V$ are automorphisms of $\mathbb Z^n$,
\[
\operatorname{coker}(A)\cong\bigoplus_{i=1}^n\mathbb Z/d_i\mathbb Z,
\]
where $\mathbb Z/0\mathbb Z$ means $\mathbb Z$.

Thus the cokernel is finite iff every $d_i\neq0$, equivalently iff
\[
\det A\neq0.
\]
When this holds,
\[
|\operatorname{coker}(A)|=\prod_i |d_i|.
\]
Because $\det U,\det V=\pm1$,
\[
|\det A|=\prod_i|d_i|,
\]
so
\[
|\operatorname{coker}(A)|=|\det A|.
\]
:::
