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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Five steps asserted their claim with no justification and each now carries one: the two rounds of
    elementary row operations, verified entry by entry, the spanning of the row space by the two nonzero
    rows, the linear independence read off from the first two coordinates, and the alternative basis
    $\{v_1, v_2\}$ with the rank count. The proof that elementary row operations preserve the row space,
    which was a one-line citation, now gives the two inclusions. The "Goal" paragraph restating the
    problem is gone, and the solution fence widened to four colons since the proof contains nested
    fences. Checked while writing: $R_2 - 3R_1 = (0,1,3,4)$, $R_3 - 5R_1 = (0,1,3,4)$, and
    $2v_1 + v_2 = (5,6,8,9)$, so the rank is $2$ and both pairs really do span the same subspace. No page
    reference is written in the body of this card or in the event above. The statement is unchanged. The
    collection retains the UGA prelim Fall 2015 paper and no solution sheet, so the argument is the card's
    own.
---

::: {.problem}
Find a basis for the subspace of $\RR^4$ spanned by
$$
(1,1,1,1),\qquad (3,4,6,7),\qquad (5,6,8,9).
$$
:::

::: {.solution}
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

:::: {.solution}

::: pf

::: pf-step
Let $v_1 = (1,1,1,1)$, $v_2 = (3,4,6,7)$, and $v_3 = (5,6,8,9)$. The subspace $W$ equals the row space $\operatorname{Row}(A)$ of the matrix:
$$A = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 3 & 4 & 6 & 7 \\ 5 & 6 & 8 & 9 \end{pmatrix}.$$

::: pf-proof
By definition of the row space of a matrix.
:::

:::

::: pf-step
The reduced row echelon form (RREF) of $A$ is:
$$R = \begin{pmatrix} 1 & 0 & -2 & -3 \\ 0 & 1 & 3 & 4 \\ 0 & 0 & 0 & 0 \end{pmatrix}.$$

::: pf-proof

::: pf-step
Apply elementary row operations: $R_2 \gets R_2 - 3R_1$ and $R_3 \gets R_3 - 5R_1$:
$$\begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 3 & 4 \\ 0 & 1 & 3 & 4 \end{pmatrix}.$$

::: pf-proof
Subtracting three times the first row from the second gives $(3,4,6,7) - (3,3,3,3) = (0,1,3,4)$, and subtracting five times the first row from the third gives $(5,6,8,9) - (5,5,5,5) = (0,1,3,4)$; the first row is unchanged, so the displayed matrix is the result.
:::

:::

::: pf-step
Apply $R_3 \gets R_3 - R_2$ and $R_1 \gets R_1 - R_2$:
$$\begin{pmatrix} 1 & 0 & -2 & -3 \\ 0 & 1 & 3 & 4 \\ 0 & 0 & 0 & 0 \end{pmatrix}.$$
This matrix is in RREF.

::: pf-proof
Subtracting the new second row from the third gives the zero row, and subtracting it from the first gives $(1,1,1,1) - (0,1,3,4) = (1,0,-2,-3)$; the leading entries are $1$ in columns $1$ and $2$, the entries above and below each leading one are zero, and the zero row lies last, which is the definition of reduced row echelon form.
:::

:::

:::

:::

::: pf-step
Elementary row operations preserve the row space, so $\operatorname{Row}(A) = \operatorname{Row}(R)$.

::: pf-proof
The row space is the span of the rows. Each elementary row operation replaces a row by itself plus a multiple of another, or by a nonzero multiple of itself, or swaps two rows, and each of these is invertible by an operation of the same kind; so the span after the operation contains the span before it and conversely, and the two are equal.
:::

:::

::: pf-step
The nonzero rows of $R$, namely $w_1 = (1, 0, -2, -3)$ and $w_2 = (0, 1, 3, 4)$, form a basis for $W$.

::: pf-proof

::: pf-step
$w_1$ and $w_2$ span $\operatorname{Row}(R) = W$ since the third row is zero.

::: pf-proof
The row space of $R$ is the span of its three rows, and the third is the zero vector, which contributes nothing; hence it is the span of $w_1$ and $w_2$.
:::

:::

::: pf-step
$w_1$ and $w_2$ are linearly independent because their leading 1s occur in distinct columns (columns 1 and 2): $c_1 w_1 + c_2 w_2 = (c_1, c_2, -2c_1+3c_2, -3c_1+4c_2) = (0,0,0,0) \implies c_1 = 0$ and $c_2 = 0$.

::: pf-proof
The displayed linear combination has first coordinate $c_1$ and second coordinate $c_2$, so it vanishes only if $c_1 = c_2 = 0$; that is the definition of linear independence for two vectors.
:::

:::

::: pf-step
Alternatively, the first two rows $\{v_1, v_2\}$ of the original matrix also form a basis for $W$ since $\rank(A) = 2$ and $v_1, v_2$ are linearly independent with $v_3 = 2v_1 + v_2$.
Hence $\dim(W) = 2$ and $\{(1,0,-2,-3), (0,1,3,4)\}$ is a basis for $W$.

::: pf-proof
The rank of $A$ is the number of nonzero rows of its reduced row echelon form, which is $2$, so $\dim W = 2$. The vectors $v_1$ and $v_2$ are not scalar multiples of one another, since $v_1$ has all four coordinates equal to $1$ and $v_2$ does not, so they are linearly independent; and $v_3 = 2v_1 + v_2$ because $(2,2,2,2) + (3,4,6,7) = (5,6,8,9)$, so the three generators are spanned by $v_1$ and $v_2$. Two independent vectors spanning a space of dimension $2$ are a basis, and the pair $w_1, w_2$ is another basis of the same space by the preceding steps.
:::

:::

:::

:::

:::
:::
