---
schema: qual/card@1
id: P-AGXGATHRANKONE
kind: problem
title: The variety of $2\times 3$ matrices of rank at most one
classification:
  areas:
  - algebraic-geometry
  topics:
  - Determinantal Varieties
  - Irreducibility
  - Dimension
relations: []
review: draft
---

::: problem
Define
\[
X \da \ts{M \in \mat(2\times 3, k) \st \rk M \leq 1} \subseteq \AA^6/k
.\]

Show that $X$ is an irreducible variety, and find its dimension.
:::

::: solution
We use the following fact from linear algebra.

*Matrix minor*: for an $m\times n$ matrix, a *minor of order* $\ell$ is the determinant of an $\ell\times \ell$ submatrix obtained by deleting any $m-\ell$ rows and any $n-\ell$ columns.

*Rank is a function of minors*: if $A\in \mat(m \times n, k)$, then the rank of $A$ equals the order of the largest nonzero minor.

Thus
\[
M_{ij} = 0 \text{ for all } \ell\times \ell \text{ minors } M_{ij} \iff \rk(M) < \ell
,\]
following from the fact that if one takes $\ell = \min(m,n)$ and all $\ell\times \ell$ minors vanish, then the largest nonzero minor must be of size $j\times j$ for $j\leq \ell -1$.
But $\det M_{ij}$ is a polynomial $f_{ij}$ in its entries, so $X$ can be written as
\[
X = V\qty{\ts{f_{ij}}}
,\]
which exhibits $X$ as a variety.
Thus
\[
M =  \begin{bmatrix} x & y & z \\ a & b & c \end{bmatrix} \implies X = V\qty{\gens{xb-ya, yc-zb, xc-za}} \subset \AA^6
.\]

**Claim**: the ideal above is prime, so the coordinate ring $A(X)$ is a domain and thus $X$ is irreducible.

**Claim**: $\dim (X) = 4$.

Heuristic: there are three degrees of freedom in choosing the first row $x,y,z$.
To enforce the rank one condition, the second row must be a scalar multiple of the first, yielding one degree of freedom for the scalar.

> Note: I looked at this for a couple of hours, but I don't know how to prove either of these statements with the tools we have so far.
:::
