---
schema: qual/card@1
id: P-LZRAH
kind: problem
title: Matrices with $\tr(A^k)=0$ for all $k$
classification:
  areas:
  - algebra
  topics:
  - Trace
  - Nilpotence
  - Eigenvalues and Eigenvectors
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $A\in M_n(F)$, where $F$ has characteristic $0$. Suppose
\[
\operatorname{tr}(A^k)=0
\]
for every $k\ge1$. What can you conclude about $A$?
:::

::: {.solution}
The matrix $A$ is nilpotent.

Pass to an algebraic closure of $F$ and let the eigenvalues of $A$ be
\[
\lambda_1,\ldots,\lambda_n
\]
with algebraic multiplicity. Then
\[
\operatorname{tr}(A^k)=\lambda_1^k+\cdots+\lambda_n^k.
\]
Thus every power sum
\[
p_k:=\sum_i\lambda_i^k
\]
vanishes.

Write the characteristic polynomial as
\[
\chi_A(x)=x^n-e_1x^{n-1}+e_2x^{n-2}-\cdots+(-1)^ne_n,
\]
where $e_j$ are the elementary symmetric functions of the eigenvalues. Newton's identities give, for $1\le m\le n$,
\[
me_m=\sum_{i=1}^m(-1)^{i-1}e_{m-i}p_i.
\]
Since every $p_i=0$ and $m$ is invertible in characteristic $0$, induction gives
\[
e_1=e_2=\cdots=e_n=0.
\]
Hence
\[
\chi_A(x)=x^n.
\]
By Cayley--Hamilton,
\[
A^n=0.
\]
Therefore $A$ is nilpotent.
:::
