---
schema: qual/card@1
id: PR-GV5CF
kind: proposition
title: Simultaneous diagonalizability of commuting diagonalizable operators
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Matrices
relations: []
review: draft
---

::: {.proposition}
Let $V$ be a finite-dimensional vector space over a field $k$, and let $\theset{A_i}_{i \in I}$ be a family of [[FD-K6FVX|diagonalizable]] linear operators on $V$.
The $A_i$ pairwise commute if and only if they are simultaneously diagonalizable: there is a basis of $V$ in which every $A_i$ is diagonal.
:::

::: {.remark}
The implication from simultaneous diagonalizability to commuting holds for any family of operators, since diagonal matrices commute.
:::

::: {.example}
Commuting operators need not be simultaneously diagonalizable without the diagonalizability hypothesis: $\begin{bmatrix} 1 & 1 \\ 0 & 1\end{bmatrix}$ commutes with itself and is not diagonalizable.
:::
