---
schema: qual/card@1
id: P-APAS24D
kind: problem
title: Diagonal similarity making a matrix norm close to the spectral radius
classification:
  areas:
  - applied-algebra
  topics:
  - Norms
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Given an upper triangular matrix $A\in M_n(\mathbb{C})=\mathbb{C}^{n\times n}$ and $\varepsilon\in\mathbb{R}$, $\varepsilon>0$, prove there exists $\eta\in\mathbb{R}$, $\eta>0$, such that the diagonal matrix $D=(d_{ij})\in M_n(\mathbb{R})=\mathbb{R}^{n\times n}$ with entries
\[
d_{jj}=\eta^{j-1},
\]
for $1\le j\le n$, satisfies
\[
\|A\|\le\rho(A)+\varepsilon,
\]
where the matrix norm $\|\cdot\|$ is defined by
\[
\|B\|=\|D^{-1}BD\|_1
\]
for all $B\in M_n(\mathbb{C})=\mathbb{C}^{n\times n}$.
:::

::: {.solution}
Let
\[
D=\operatorname{diag}(1,\eta,\eta^2,\ldots,\eta^{n-1}).
\]
Since $A$ is upper triangular, so is $D^{-1}AD$, and its entries are
\[
(D^{-1}AD)_{ij}=\eta^{\,j-i}a_{ij}
\qquad(i\le j).
\]
In particular, the diagonal entries are unchanged. Since the eigenvalues of an upper-triangular matrix are its diagonal entries,
\[
\rho(A)=\max_j|a_{jj}|.
\]

Let
\[
C=\sum_{1\le i<j\le n}|a_{ij}|.
\]
If $C=0$, then $A$ is diagonal and for every $\eta>0$,
\[
\|A\|=\|A\|_1=\rho(A).
\]
Assume $C>0$. Choose
\[
0<\eta\le1
\qquad\text{with}\qquad
\eta C<\varepsilon.
\]
For each column $j$,
\[
\sum_{i=1}^n |(D^{-1}AD)_{ij}|
=
|a_{jj}|+\sum_{i<j}\eta^{j-i}|a_{ij}|.
\]
Because $j-i\ge1$ and $0<\eta\le1$,
\[
\eta^{j-i}\le\eta.
\]
Hence
\[
\sum_i |(D^{-1}AD)_{ij}|
\le
|a_{jj}|+\eta C
<
\rho(A)+\varepsilon.
\]
Taking the maximum over columns gives
\[
\|A\|
=\|D^{-1}AD\|_1
\le\rho(A)+\varepsilon.
\]
Thus such an $\eta>0$ exists.
:::
