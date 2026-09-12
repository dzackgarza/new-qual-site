---
schema: qual/card@1
id: P-OQCJR
kind: problem
title: $Ax=0$ has a nontrivial solution iff $\rank(A)<m$
classification:
  areas:
  - algebra
  topics:
  - Rank and Nullity
  - Linear Algebra
  - Matrices
relations: []
review: draft
---

::: problem
Let $A\in M_{m\times n}(F)$. Prove that the homogeneous system
\[
Ax=0
\]
has a nonzero solution if and only if
\[
\operatorname{rank}(A)<n.
\]
:::

::: {.solution}
By rank-nullity for the linear map $A:F^n\to F^m$,
\[
n=\dim\ker A+\operatorname{rank}(A).
\]
Hence
\[
\ker A\ne0
\iff \dim\ker A>0
\iff \operatorname{rank}(A)<n.
\]
A nonzero vector in $\ker A$ is exactly a nontrivial solution of $Ax=0$.
:::
