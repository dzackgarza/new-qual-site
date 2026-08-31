---
schema: qual/card@1
id: P-KOTV2
kind: problem
title: Basis for $\operatorname{span}\{(1,1,1,1),(3,4,6,7),(5,6,8,9)\}$
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
  - Bases
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Find a basis for the subspace of $\mathbb R^4$ spanned by
\[
(1,1,1,1),\qquad (3,4,6,7),\qquad (5,6,8,9).
\]
:::

::: solution
1. It will exactly be the row space of 
$$
A = \left(\begin{array}{rrrr}
1 & 1 & 1 & 1 \\
3 & 4 & 6 & 7 \\
5 & 6 & 8 & 9
\end{array}\right),
$$ 
where we note that $R_3 = 2R_1 + R_2$ but $R_1 \neq \lambda R_2$ and so the first two rows span the correct subspace. We can also compute the RREF, which has the same rowspace, $$\tilde A = \left(\begin{array}{rrrr}
1 & 0 & -2 & -3 \\
0 & 1 & 3 & 4 \\
0 & 0 & 0 & 0
\end{array}\right)$$
from which we find that $\vector v_1 = \thevector{1,0,-2,-3}$ and $\vector v_2 = \thevector{0,1,3,4}$ also do the job. $\qed$
:::

::: {.solution}
**Goal:** Find a basis for the subspace $W = \operatorname{span}\{(1,1,1,1), \, (3,4,6,7), \, (5,6,8,9)\} \subseteq \mathbb{R}^4$.

<1>1. Let $v_1 = (1,1,1,1)$, $v_2 = (3,4,6,7)$, and $v_3 = (5,6,8,9)$. The subspace $W$ equals the row space $\operatorname{Row}(A)$ of the matrix:
    $$A = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 3 & 4 & 6 & 7 \\ 5 & 6 & 8 & 9 \end{pmatrix}.$$
    ::: {.proof}
    By definition of the row space of a matrix.
    :::

<1>2. The reduced row echelon form (RREF) of $A$ is:
    $$R = \begin{pmatrix} 1 & 0 & -2 & -3 \\ 0 & 1 & 3 & 4 \\ 0 & 0 & 0 & 0 \end{pmatrix}.$$
    Proof:
    <2>1. Apply elementary row operations: $R_2 \gets R_2 - 3R_1$ and $R_3 \gets R_3 - 5R_1$:
        $$\begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 3 & 4 \\ 0 & 1 & 3 & 4 \end{pmatrix}.$$
    <2>2. Apply $R_3 \gets R_3 - R_2$ and $R_1 \gets R_1 - R_2$:
        $$\begin{pmatrix} 1 & 0 & -2 & -3 \\ 0 & 1 & 3 & 4 \\ 0 & 0 & 0 & 0 \end{pmatrix}.$$
    This matrix is in RREF.

<1>3. Elementary row operations preserve the row space, so $\operatorname{Row}(A) = \operatorname{Row}(R)$.
    ::: {.proof}
    Standard linear algebra theorem: each elementary row operation is invertible and preserves linear combinations of the rows.
    :::

<1>4. The nonzero rows of $R$, namely $w_1 = (1, 0, -2, -3)$ and $w_2 = (0, 1, 3, 4)$, form a basis for $W$.
    Proof:
    <2>1. $w_1$ and $w_2$ span $\operatorname{Row}(R) = W$ since the third row is zero.
    <2>2. $w_1$ and $w_2$ are linearly independent because their leading 1s occur in distinct columns (columns 1 and 2): $c_1 w_1 + c_2 w_2 = (c_1, c_2, -2c_1+3c_2, -3c_1+4c_2) = (0,0,0,0) \implies c_1 = 0$ and $c_2 = 0$.
    <2>3. Alternatively, the first two rows $\{v_1, v_2\}$ of the original matrix also form a basis for $W$ since $\rank(A) = 2$ and $v_1, v_2$ are linearly independent with $v_3 = 2v_1 + v_2$.
    Hence $\dim(W) = 2$ and $\{(1,0,-2,-3), (0,1,3,4)\}$ is a basis for $W$. Q.E.D.
:::
