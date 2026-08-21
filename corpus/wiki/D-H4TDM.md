---
schema: qual/card@1
id: D-H4TDM
kind: definition
title: Gram matrix of a bilinear form
classification:
  areas:
  - algebra
  topics:
  - Bilinear Forms
  - Matrices
relations: []
review: draft
---

::: {.definition title="Gram Matrix"}
For $b$ a bilinear form on a finite-dimensional $k\dash$vector space $V$ with ordered basis $\mathcal B = \ts{e_1, \cdots, e_n}$, the **Gram matrix** of $b$ with respect to $\mathcal B$ is
\[
G \da \qty{ b(e_i, e_j) }_{i,j}
,\]
so that $b(x, y) = [x]_{\mathcal B}^t\, G\, [y]_{\mathcal B}$.
Changing basis by an invertible $P$ replaces $G$ with $P^t G P$, so $\det G$ is well defined modulo squares of units, and $b$ is nondegenerate exactly when $G$ is invertible.
:::

::: {.concept}
See Artin, *Algebra*, ch. 8.
:::
