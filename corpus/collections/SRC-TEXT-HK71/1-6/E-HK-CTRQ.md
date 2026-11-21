---
schema: qual/card@1
id: E-HK-CTRQ
kind: problem
title: Invertibility via row operations and finding inverses
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the two containers state what their subsections do, and the 14 leaf
    steps that recorded a row operation or a conclusion with no justification each carry a sentence
    saying why the operation is legitimate or why the conclusion follows. The Goal paragraph was removed.
    Both computations were re-checked: $\det A=0$ and the elimination produces a zero row, while
    $\det B=-8$ and the displayed inverse multiplies out to the identity. Checked against Hungerford,
    Algebra, section 1.6. Nothing in the statement was changed.

---

::: {.exercise}
For each of the two matrices
$$
A = \begin{bmatrix} 2 & 5 & -1 \\ 4 & -1 & 2 \\ 6 & 4 & 1 \end{bmatrix}, \qquad B = \begin{bmatrix} 1 & -1 & 2 \\ 3 & 2 & 4 \\ 0 & 1 & -2 \end{bmatrix}
$$
use elementary row operations to discover whether it is invertible, and to find the inverse in case it is.
:::

::: {.solution}
::: pf

::: pf-step
Analysis of Matrix $A = \begin{bmatrix} 2 & 5 & -1 \\ 4 & -1 & 2 \\ 6 & 4 & 1 \end{bmatrix}$:

::: pf-proof

::: pf-step
Form the augmented matrix $[A \mid I_3]$:
$$\left[\begin{array}{ccc|ccc} 2 & 5 & -1 & 1 & 0 & 0 \\ 4 & -1 & 2 & 0 & 1 & 0 \\ 6 & 4 & 1 & 0 & 0 & 1 \end{array}\right].$$

::: pf-proof
This is the augmented matrix on which the Gauss-Jordan algorithm operates.
:::

:::

::: pf-step
Perform row operations to eliminate the first column:
- $R_2 \gets R_2 - 2R_1$:
  $$\left[\begin{array}{ccc|ccc} 2 & 5 & -1 & 1 & 0 & 0 \\ 0 & -11 & 4 & -2 & 1 & 0 \\ 6 & 4 & 1 & 0 & 0 & 1 \end{array}\right].$$
- $R_3 \gets R_3 - 3R_1$:
  $$\left[\begin{array}{ccc|ccc} 2 & 5 & -1 & 1 & 0 & 0 \\ 0 & -11 & 4 & -2 & 1 & 0 \\ 0 & -11 & 4 & -3 & 0 & 1 \end{array}\right].$$

::: pf-proof
The two operations replace $R_2$ by $R_2-2R_1$ and $R_3$ by $R_3-3R_1$, which clear the first entry of those rows; elementary row operations do not change the row space.
:::

:::

::: pf-step
Perform row operation on row 3:
- $R_3 \gets R_3 - R_2$:
  $$\left[\begin{array}{ccc|ccc} 2 & 5 & -1 & 1 & 0 & 0 \\ 0 & -11 & 4 & -2 & 1 & 0 \\ 0 & 0 & 0 & -1 & -1 & 1 \end{array}\right].$$

::: pf-proof
Subtracting the second row from the third clears its second entry, and the displayed matrix is the result.
:::

:::

::: pf-step
The left $3 \times 3$ block has a row of zeros (row rank 2), so $A$ cannot be reduced to the identity matrix $I_3$.

::: pf-proof
Elementary row operations preserve the rank of the left block, the identity has rank $3$, and a block with a zero row has smaller rank.
:::

:::

::: pf-step
Therefore, the matrix $A$ is **not invertible** (singular).

::: pf-proof
A square matrix is invertible exactly when it row-reduces to the identity.
:::

:::

:::

:::

::: pf-step
Analysis of Matrix $B = \begin{bmatrix} 1 & -1 & 2 \\ 3 & 2 & 4 \\ 0 & 1 & -2 \end{bmatrix}$:

::: pf-proof

::: pf-step
Form the augmented matrix $[B \mid I_3]$:
$$\left[\begin{array}{ccc|ccc} 1 & -1 & 2 & 1 & 0 & 0 \\ 3 & 2 & 4 & 0 & 1 & 0 \\ 0 & 1 & -2 & 0 & 0 & 1 \end{array}\right].$$

::: pf-proof
This is the augmented matrix of the algorithm applied to $B$.
:::

:::

::: pf-step
Eliminate the first column below row 1:
- $R_2 \gets R_2 - 3R_1$:
  $$\left[\begin{array}{ccc|ccc} 1 & -1 & 2 & 1 & 0 & 0 \\ 0 & 5 & -2 & -3 & 1 & 0 \\ 0 & 1 & -2 & 0 & 0 & 1 \end{array}\right].$$

::: pf-proof
This clears the first entry of the second row.
:::

:::

::: pf-step
Swap $R_2 \leftrightarrow R_3$:
$$\left[\begin{array}{ccc|ccc} 1 & -1 & 2 & 1 & 0 & 0 \\ 0 & 1 & -2 & 0 & 0 & 1 \\ 0 & 5 & -2 & -3 & 1 & 0 \end{array}\right].$$

::: pf-proof
A row interchange is an elementary operation, and it puts a row with a non-zero second entry into the second position.
:::

:::

::: pf-step
Eliminate the second column:
- $R_1 \gets R_1 + R_2$:
  $$\left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 1 & 0 & 1 \\ 0 & 1 & -2 & 0 & 0 & 1 \\ 0 & 5 & -2 & -3 & 1 & 0 \end{array}\right].$$
- $R_3 \gets R_3 - 5R_2$:
  $$\left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 1 & 0 & 1 \\ 0 & 1 & -2 & 0 & 0 & 1 \\ 0 & 0 & 8 & -3 & 1 & -5 \end{array}\right].$$

::: pf-proof
Adding the second row to the first clears the second entry of the first row.
:::

:::

::: pf-step
Scale $R_3 \gets \frac{1}{8} R_3$:
$$\left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 1 & 0 & 1 \\ 0 & 1 & -2 & 0 & 0 & 1 \\ 0 & 0 & 1 & -\frac{3}{8} & \frac{1}{8} & -\frac{5}{8} \end{array}\right].$$

::: pf-proof
The third entry of the third row is $8$, so scaling by $1/8$ makes it $1$.
:::

:::

::: pf-step
Eliminate the third column in $R_2$:
- $R_2 \gets R_2 + 2R_3$:
  - Entry $(2, 1)$: $0 + 2(-3/8) = -3/4 = -6/8$.
  - Entry $(2, 2)$: $0 + 2(1/8) = 1/4 = 2/8$.
  - Entry $(2, 3)$: $1 + 2(-5/8) = 1 - 5/4 = -1/4 = -2/8$.
  $$\left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 1 & 0 & 1 \\ 0 & 1 & 0 & -\frac{3}{4} & \frac{1}{4} & -\frac{1}{4} \\ 0 & 0 & 1 & -\frac{3}{8} & \frac{1}{8} & -\frac{5}{8} \end{array}\right].$$

::: pf-proof
Adding twice the third row to the second clears its third entry; the three entries are computed explicitly in the display.
:::

:::

::: pf-step
Writing in common denominator $\frac{1}{8}$:
$$B^{-1} = \frac{1}{8} \begin{bmatrix} 8 & 0 & 8 \\ -6 & 2 & -2 \\ -3 & 1 & -5 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 1 \\ -\frac{3}{4} & \frac{1}{4} & -\frac{1}{4} \\ -\frac{3}{8} & \frac{1}{8} & -\frac{5}{8} \end{bmatrix}.$$

::: pf-proof
Collecting the scalar $1/8$ from every entry gives the second display, and the two are equal.
:::

:::

::: pf-step
**Verification:**
$$\begin{bmatrix} 1 & -1 & 2 \\ 3 & 2 & 4 \\ 0 & 1 & -2 \end{bmatrix} \cdot \frac{1}{8} \begin{bmatrix} 8 & 0 & 8 \\ -6 & 2 & -2 \\ -3 & 1 & -5 \end{bmatrix} = \frac{1}{8} \begin{bmatrix} 8+6-6 & 0-2+2 & 8+2-10 \\ 24-12-12 & 0+4+4 & 24-4-20 \\ 0-6+6 & 0+2-2 & 0-2+10 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}.$$

::: pf-proof
Multiplying out gives the identity matrix, which confirms that the displayed matrix is the inverse.
:::

:::

:::

:::

::: pf-step
Conclusion:
$A$ is not invertible; $B$ is invertible with inverse $B^{-1} = \frac{1}{8}\begin{bmatrix} 8 & 0 & 8 \\ -6 & 2 & -2 \\ -3 & 1 & -5 \end{bmatrix}$.

::: pf-proof
The two analyses together: $A$ admits no inverse, and the inverse of $B$ is the matrix displayed.
:::

:::

:::

:::
