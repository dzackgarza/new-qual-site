---
schema: qual/card@1
id: PR-GV5CF
kind: proposition
title: Simultaneous diagonalizability of commuting diagonalizable operators
slogan: 'Commuting diagonalizable operators share an eigenbasis.'
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

::: {.proof}
One direction is immediate: diagonal matrices commute, so simultaneously diagonalizable operators commute.

For the converse, suppose the family is finite and pairwise commuting, and induct on its size.
For one operator the statement is its diagonalizability.
Otherwise let $A$ be a member of the family and write $V=\bigoplus_i E_i$ over the distinct eigenvalues $\mu_i$ of $A$, which is a direct sum because $A$ is diagonalizable.
If $A_jA=AA_j$ and $v\in E_i$, then $A(A_jv)=A_jAv=\mu_iA_jv$, so $A_jv\in E_i$ and each $E_i$ is invariant under every other $A_j$.
The minimal polynomial of the restriction $A_j\restrict_{E_i}$ divides the minimal polynomial of $A_j$, so the restriction is diagonalizable, and by induction the restrictions of the other operators to $E_i$ are simultaneously diagonalizable.
The union over $i$ of bases of the $E_i$ on which they are all diagonal is a basis of $V$ on which every member of the family is diagonal.

For an arbitrary family, the span of the operators in $\Endo(V)$ is finite-dimensional, so it has a basis $A_{i_1},\ldots,A_{i_r}$ drawn from the family; a basis diagonalizing those diagonalizes every linear combination of them, hence every member of the family.
:::

::: {.remark}
The implication from simultaneous diagonalizability to commuting holds for any family of operators, since diagonal matrices commute.
:::

::: {.example}
Commuting operators need not be simultaneously diagonalizable without the diagonalizability hypothesis: $\begin{bmatrix} 1 & 1 \\ 0 & 1\end{bmatrix}$ commutes with itself and is not diagonalizable.
:::
