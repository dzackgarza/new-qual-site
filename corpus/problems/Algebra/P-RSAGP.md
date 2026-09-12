---
schema: qual/card@1
id: P-RSAGP
kind: problem
title: Bilinear forms and orthogonal matrices
classification:
  areas:
  - algebra
  topics:
  - Bilinear Forms
  - Matrix Groups
  - Quadratic Forms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
(1) What is a bilinear form on a vector space $V$ over a field $K$?
(2) When are two bilinear forms equivalent (congruent)?
(3) What is an orthogonal matrix $Q \in \operatorname{O}(n)$, and what are its special geometric and algebraic properties?
:::

::: solution
A bilinear form on a $K$-vector space $V$ is a map
\[
B:V\times V\to K
\]
that is linear in each argument. In a basis $e_1,\dots,e_n$, its Gram matrix is
\[
M=(B(e_i,e_j)),
\]
and if $x,y$ are coordinate columns then
\[
B(x,y)=x^TM y.
\]

Two bilinear forms are equivalent if there is $P\in\operatorname{GL}_n(K)$ carrying one to the other. Their matrices are then related by congruence:
\[
M_2=P^TM_1P.
\]
Thus congruence, not similarity, is the natural change-of-basis relation for bilinear forms.

Over $\mathbb R$, an orthogonal matrix is a matrix $Q$ satisfying
\[
Q^TQ=I,
\]
equivalently $Q^{-1}=Q^T$. It preserves the Euclidean inner product:
\[
\langle Qx,Qy\rangle=x^TQ^TQy=\langle x,y\rangle.
\]
Hence it preserves lengths, distances, and angles; its columns and rows are orthonormal; and
\[
(\det Q)^2=1,
\]
so $\det Q=\pm1$. Its complex eigenvalues have absolute value $1$.

For an orthogonal change of basis, congruence and similarity have the same matrix expression,
\[
Q^TAQ=Q^{-1}AQ.
\]
This identity is one reason orthogonal diagonalization is especially natural for real symmetric matrices.
:::
