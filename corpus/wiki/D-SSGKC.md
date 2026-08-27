---
schema: qual/card@1
id: D-SSGKC
kind: definition
title: Quadratic Form
classification:
  areas:
  - algebra
  topics:
  - Quadratic Forms
  - Bilinear Forms
  - Diagonalization
relations:
- kind: related-to
  target: D-NRRIT
review: draft
---

::: {.definition}
In coordinates, a **quadratic form** in $n$ variables is a polynomial every one of whose terms has degree $2$:
\[
q(x_1, \cdots, x_n) = \sum_{i} a_{ii}x_i^2 + \sum_{i < j} 2a_{ij}x_ix_j = X^t A X, \qquad X = (x_1,\cdots,x_n)^t
,\]
where $A = (a_{ij})$ is the **symmetric** matrix of the form; the factor $2$ is put in so that $A$ has no halves in it.
Over $\RR$ the symmetric $A$ is orthogonally diagonalizable by the spectral theorem, so an orthogonal change of variable $X = PX'$ replaces $A$ by $P^t A P = P\inv A P$ and makes $q$ a sum of scaled squares $\sum_i \lambda_i x_i'^2$ with the $\lambda_i$ the eigenvalues of $A$.

Counting the signs $(p, m)$ of the nonzero $\lambda_i$ gives the **signature** of a nondegenerate form, which by Sylvester's law does not depend on the diagonalizing basis.
The level sets $\ts{q = c}$ are the conics and quadrics, and the signature is what classifies them.
:::

::: {.concept}
See Artin, *Algebra*, §8.7, (8.7.2)-(8.7.3), pp. 245-247; the signature and Sylvester's law are at §8.4, p. 240.
The basis-free formulation, as a function $q$ with $q(\lambda x) = \lambda^2 q(x)$ whose polarization is bilinear, is the related card of the same title.
:::
