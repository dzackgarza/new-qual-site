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
As on [[T-GRDSOC]], the ideal $\mfm=\bigoplus_{i\geq1}R_i$ is the unique maximal ideal, so $R$ is a zero-dimensional local ring with residue field $R_0=k$, and its socle $\theset{r \st \mfm r=0}$ is one-dimensional and equal to $R_n$.

Let $0\neq a\in R_i$ be homogeneous.
The ideal $Ra$ is nonzero, and $R$ is Artinian, so the chain $Ra\supseteq\mfm(Ra)\supseteq\mfm^2(Ra)\supseteq\cdots$ stabilizes; if $\mfm^kN=\mfm^{k+1}N$ for $N=\mfm^k(Ra)$, then $N=0$ by Nakayama, so some $\mfm^k(Ra)$ is nonzero and killed by $\mfm$, that is, it is a nonzero subspace of the socle $R_n$.
Hence $ab\in R_n$ is nonzero for some $b\in R$, and comparing degrees gives $b\in R_{n-i}$.

So the adjoint $R_i\to\Hom_k(R_{n-i},R_n)$ has zero kernel, and the same argument with the roles of $i$ and $n-i$ interchanged shows that the other adjoint has zero kernel.
Two injections between spaces of the same finite dimension are isomorphisms, and $\dim_k R_n=1$.
:::
