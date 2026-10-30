---
schema: qual/card@1
id: P-5CDU3
kind: problem
title: For a nondegenerate skew-symmetric form, $\dim U+\dim U^\perp=\dim V$, and a subspace $W$ with $W^\perp=W$ exists
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Bilinear Forms
relations: []
review: draft
---

::: {.problem}
Let $V$ be a finite-dimensional vector space over a field $F$ of characteristic $0$.
Let $B:V\times V\to F$ be a non-degenerate, skew-symmetric bilinear form.
(In particular, we have $B(x,y)=-B(y,x)$ for all $x,y\in V$.)
If $U$ is a subset of $V$, let
$$
U^\perp=\{v\in V\mid B(u,v)=0 \text{ for all } u\in U\}.
$$

(a) Let $U$ be a subspace of $V$.
Prove that $U^\perp$ is a subspace of $V$ and that
$$
\dim_F(U)+\dim_F(U^\perp)=\dim_F(V).
$$

(b) Prove that there exists a subspace $W$ of $V$ such that $W^\perp=W$.
:::
