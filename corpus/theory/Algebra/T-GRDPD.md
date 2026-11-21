---
schema: qual/card@1
id: T-GRDPD
kind: theorem
title: Poincaré duality for a finite-dimensional graded Gorenstein algebra
slogan: 'In a graded Gorenstein algebra with R_0 = k, the top piece is one-dimensional and the multiplication pairings into it are perfect.'
classification:
  areas:
  - algebra
  topics:
  - Gorenstein Rings
  - Graded Rings
relations: []
review: draft
---

::: {.theorem}
Let $k$ be a field and let $R = \bigoplus_{i=0}^{n} R_i$ be a finite-dimensional graded commutative $k$-algebra with $R_0 = k$ and $R_n\neq0$.
If $R$ is [[D-DU4UQ|Gorenstein]], then $\dim_k R_n = 1$ and for every $i$ the pairing
$$
R_i \times R_{n-i}\longrightarrow R_n,\qquad (a,b)\longmapsto ab,
$$
is perfect: its two adjoints $R_i\to\Hom_k(R_{n-i},R_n)$ and $R_{n-i}\to\Hom_k(R_i,R_n)$ are isomorphisms.
:::

::: {.proof}
As on [[T-GRDSOC]], the ideal $\mfm=\bigoplus_{i\geq1}R_i$ is the unique maximal ideal, so $R$ is a zero-dimensional local ring with residue field $R_0=k$, and its socle $\theset{r \st \mfm r=0}$ is one-dimensional and equal to $R_n$; in particular $\dim_k R_n=1$.

Let $0\neq a\in R_i$ be homogeneous.
The ideal $Ra$ is nonzero, and $R$ is finite-dimensional over $k$, hence Artinian, so the chain $Ra\supseteq\mfm(Ra)\supseteq\mfm^2(Ra)\supseteq\cdots$ stabilizes; if $\mfm^kN=\mfm^{k+1}N$ for $N=\mfm^k(Ra)$, then $N=0$ by Nakayama, so some $\mfm^k(Ra)$ is nonzero and killed by $\mfm$, that is, it is a nonzero subspace of the socle $R_n$.
Hence there is $b\in R$ with $ab\in R_n$ nonzero.

Write $b=\sum_j b_j$ with $b_j\in R_j$, so that $ab=\sum_j ab_j$ with $ab_j\in R_{i+j}$.
The degree-$d$ component of $ab$ is the sum of those $ab_j$ with $i+j=d$, and $ab\in R_n$ makes that component zero for $d\neq n$; hence $ab_j=0$ whenever $j\neq n-i$, so that $ab_{n-i}=ab\neq0$.
Replacing $b$ by its component $b_{n-i}\in R_{n-i}$, the adjoint $R_i\to\Hom_k(R_{n-i},R_n)$ has zero kernel.

The case $i>n$ is vacuous, both $R_i$ and $R_{n-i}$ being zero, and the same argument with the roles of $i$ and $n-i$ interchanged shows that the other adjoint has zero kernel.
Since $\dim_k R_n=1$, the space $\Hom_k(R_{n-i},R_n)$ has dimension $\dim_k R_{n-i}$, so $\dim_k R_i\leq\dim_k R_{n-i}$ and, interchanging, $\dim_k R_{n-i}\leq\dim_k R_i$; the two dimensions are equal and each injection is an isomorphism.
:::
