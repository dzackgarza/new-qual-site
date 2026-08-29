---
schema: qual/card@1
id: E-HK-CTRQ
kind: exercise
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
---

::: {.exercise}
For each of the two matrices
$$
A = \begin{bmatrix} 2 & 5 & -1 \\ 4 & -1 & 2 \\ 6 & 4 & 1 \end{bmatrix}, \qquad B = \begin{bmatrix} 1 & -1 & 2 \\ 3 & 2 & 4 \\ 0 & 1 & -2 \end{bmatrix}
$$
use elementary row operations to discover whether it is invertible, and to find the inverse in case it is.
:::

::: solution
**Goal:** Apply Gauss-Jordan elimination to augmented matrices $[M \mid I_3]$ to determine invertibility and compute matrix inverses.

<1>1. Analysis of Matrix $A = \begin{bmatrix} 2 & 5 & -1 \\ 4 & -1 & 2 \\ 6 & 4 & 1 \end{bmatrix}$:
    *Proof:*
    <2>1. Form the augmented matrix $[A \mid I_3]$:
        $$\left[\begin{array}{ccc|ccc} 2 & 5 & -1 & 1 & 0 & 0 \\ 4 & -1 & 2 & 0 & 1 & 0 \\ 6 & 4 & 1 & 0 & 0 & 1 \end{array}\right].$$
    <2>2. Perform row operations to eliminate the first column:
        - $R_2 \gets R_2 - 2R_1$:
          $$\left[\begin{array}{ccc|ccc} 2 & 5 & -1 & 1 & 0 & 0 \\ 0 & -11 & 4 & -2 & 1 & 0 \\ 6 & 4 & 1 & 0 & 0 & 1 \end{array}\right].$$
        - $R_3 \gets R_3 - 3R_1$:
          $$\left[\begin{array}{ccc|ccc} 2 & 5 & -1 & 1 & 0 & 0 \\ 0 & -11 & 4 & -2 & 1 & 0 \\ 0 & -11 & 4 & -3 & 0 & 1 \end{array}\right].$$
    <2>3. Perform row operation on row 3:
        - $R_3 \gets R_3 - R_2$:
          $$\left[\begin{array}{ccc|ccc} 2 & 5 & -1 & 1 & 0 & 0 \\ 0 & -11 & 4 & -2 & 1 & 0 \\ 0 & 0 & 0 & -1 & -1 & 1 \end{array}\right].$$
    <2>4. The left $3 \times 3$ block has a row of zeros (row rank 2), so $A$ cannot be reduced to the identity matrix $I_3$.
    <2>5. Therefore, the matrix $A$ is **not invertible** (singular).

<1>2. Analysis of Matrix $B = \begin{bmatrix} 1 & -1 & 2 \\ 3 & 2 & 4 \\ 0 & 1 & -2 \end{bmatrix}$:
    *Proof:*
    <2>1. Form the augmented matrix $[B \mid I_3]$:
        $$\left[\begin{array}{ccc|ccc} 1 & -1 & 2 & 1 & 0 & 0 \\ 3 & 2 & 4 & 0 & 1 & 0 \\ 0 & 1 & -2 & 0 & 0 & 1 \end{array}\right].$$
    <2>2. Eliminate the first column below row 1:
        - $R_2 \gets R_2 - 3R_1$:
          $$\left[\begin{array}{ccc|ccc} 1 & -1 & 2 & 1 & 0 & 0 \\ 0 & 5 & -2 & -3 & 1 & 0 \\ 0 & 1 & -2 & 0 & 0 & 1 \end{array}\right].$$
    <2>3. Swap $R_2 \leftrightarrow R_3$:
        $$\left[\begin{array}{ccc|ccc} 1 & -1 & 2 & 1 & 0 & 0 \\ 0 & 1 & -2 & 0 & 0 & 1 \\ 0 & 5 & -2 & -3 & 1 & 0 \end{array}\right].$$
    <2>4. Eliminate the second column:
        - $R_1 \gets R_1 + R_2$:
          $$\left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 1 & 0 & 1 \\ 0 & 1 & -2 & 0 & 0 & 1 \\ 0 & 5 & -2 & -3 & 1 & 0 \end{array}\right].$$
        - $R_3 \gets R_3 - 5R_2$:
          $$\left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 1 & 0 & 1 \\ 0 & 1 & -2 & 0 & 0 & 1 \\ 0 & 0 & 8 & -3 & 1 & -5 \end{array}\right].$$
    <2>5. Scale $R_3 \gets \frac{1}{8} R_3$:
        $$\left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 1 & 0 & 1 \\ 0 & 1 & -2 & 0 & 0 & 1 \\ 0 & 0 & 1 & -\frac{3}{8} & \frac{1}{8} & -\frac{5}{8} \end{array}\right].$$
    <2>6. Eliminate the third column in $R_2$:
        - $R_2 \gets R_2 + 2R_3$:
          - Entry $(2, 1)$: $0 + 2(-3/8) = -3/4 = -6/8$.
          - Entry $(2, 2)$: $0 + 2(1/8) = 1/4 = 2/8$.
          - Entry $(2, 3)$: $1 + 2(-5/8) = 1 - 5/4 = -1/4 = -2/8$.
          $$\left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 1 & 0 & 1 \\ 0 & 1 & 0 & -\frac{3}{4} & \frac{1}{4} & -\frac{1}{4} \\ 0 & 0 & 1 & -\frac{3}{8} & \frac{1}{8} & -\frac{5}{8} \end{array}\right].$$
    <2>7. Writing in common denominator $\frac{1}{8}$:
        $$B^{-1} = \frac{1}{8} \begin{bmatrix} 8 & 0 & 8 \\ -6 & 2 & -2 \\ -3 & 1 & -5 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 1 \\ -\frac{3}{4} & \frac{1}{4} & -\frac{1}{4} \\ -\frac{3}{8} & \frac{1}{8} & -\frac{5}{8} \end{bmatrix}.$$
    <2>8. **Verification:**
        $$\begin{bmatrix} 1 & -1 & 2 \\ 3 & 2 & 4 \\ 0 & 1 & -2 \end{bmatrix} \cdot \frac{1}{8} \begin{bmatrix} 8 & 0 & 8 \\ -6 & 2 & -2 \\ -3 & 1 & -5 \end{bmatrix} = \frac{1}{8} \begin{bmatrix} 8+6-6 & 0-2+2 & 8+2-10 \\ 24-12-12 & 0+4+4 & 24-4-20 \\ 0-6+6 & 0+2-2 & 0-2+10 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}.$$

<1>3. Conclusion:
    $A$ is not invertible; $B$ is invertible with inverse $B^{-1} = \frac{1}{8}\begin{bmatrix} 8 & 0 & 8 \\ -6 & 2 & -2 \\ -3 & 1 & -5 \end{bmatrix}$. Q.E.D.
:::
