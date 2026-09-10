---
schema: qual/card@1
id: P-YLFU2
kind: problem
title: 'Structure theorem for finitely generated modules over a PID: invariant factors
  and elementary divisors'
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Modules
  - Principal Ideal Domains
relations: []
review: draft
---

::: problem
State and prove the structure theorem for finitely generated modules over a PID, in both invariant-factor and elementary-divisor form.
:::

::: solution
Let $R$ be a PID and let $M$ be a finitely generated $R$-module. Then
\[
M\cong R^r\oplus\bigoplus_{i=1}^s R/(d_i),
\]
where
\[
d_1\mid d_2\mid\cdots\mid d_s
\]
and each $d_i$ is nonzero and nonunit. The integer $r$ and the invariant factors $d_i$, up to multiplication by units, are unique.

To prove existence, choose a surjection
\[
R^n\twoheadrightarrow M
\]
with kernel $N$. Since $R$ is a PID, the submodule $N\le R^n$ is free of finite rank. Choose bases of $R^n$ and $N$ and let $A$ be the matrix of the inclusion $N\hookrightarrow R^n$. Smith normal form gives invertible matrices $U,V$ such that
\[
UAV=\operatorname{diag}(d_1,\ldots,d_s,0,\ldots,0),
\qquad
d_1\mid\cdots\mid d_s.
\]
Taking the quotient of $R^n$ by the image gives
\[
M\cong R^{n-s}\oplus\bigoplus_{i=1}^s R/(d_i).
\]

Factor each invariant factor into prime powers. Since distinct prime powers are comaximal, the Chinese remainder theorem gives
\[
R/(d_i)
\cong
\bigoplus_{p^e\parallel d_i} R/(p^e).
\]
Thus one obtains the elementary-divisor form
\[
M\cong R^r\oplus\bigoplus_j R/(p_j^{e_j}),
\]
where the $p_j$ are prime elements, not necessarily distinct.

Conversely, grouping the elementary divisors by prime and aligning equal-prime powers in nondecreasing order reconstructs invariant factors satisfying the divisibility chain.

Uniqueness of the invariant factors follows from Smith normal form, equivalently from the determinantal ideals of a presentation matrix; uniqueness of the elementary divisors follows from unique factorization in the PID together with primary decomposition.
:::
