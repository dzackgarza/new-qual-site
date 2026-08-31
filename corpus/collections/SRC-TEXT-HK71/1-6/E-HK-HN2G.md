---
schema: qual/card@1
id: E-HK-HN2G
kind: exercise
title: Determinant criterion for $2 \times 2$ invertibility via row operations
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
Let

$$
A = \left[ \begin{array}{c c} a & b \\ c & d \end{array} \right].
$$

Prove, using elementary row operations, that $A$ is invertible if and only if $(ad - bc) \neq 0$ .
:::

::: {.solution}
<1>1. Criterion for invertibility via elementary row operations: <2>1. A square matrix $A \in M_2(F)$ is invertible if and only if it is row-equivalent to the identity matrix $I_2$ (i.e. its reduced row echelon form is $I_2$).
::: {.proof}
Hoffman–Kunze Theorem 1.13 on invertible matrices and row equivalence.
:::

<1>2. **Case 1: $a \neq 0$:** <2>1. Multiply row 1 by $\frac{1}{a}$:
\[
\begin{pmatrix} a & b \\ c & d \end{pmatrix} \xrightarrow{R_1 \leftarrow \frac{1}{a} R_1} \begin{pmatrix} 1 & b/a \\ c & d \end{pmatrix}.
\]
::: {.proof}
elementary row operation (scaling by non-zero scalar).
:::
<2>2. Add $-c$ times row 1 to row 2:
\[
\begin{pmatrix} 1 & b/a \\ c & d \end{pmatrix} \xrightarrow{R_2 \leftarrow R_2 - c R_1} \begin{pmatrix} 1 & b/a \\ 0 & d - c(b/a) \end{pmatrix} = \begin{pmatrix} 1 & b/a \\ 0 & \frac{ad - bc}{a} \end{pmatrix}.
\]
::: {.proof}
elementary row operation (row addition).
:::
<2>3. If $ad - bc = 0$, the matrix has a row of zeros $\begin{pmatrix} 1 & b/a \\ 0 & 0 \end{pmatrix}$, so its rank is 1 and it cannot be row-reduced to $I_2$.
Thus $A$ is not invertible.
::: {.proof}
a matrix with a zero row in row echelon form cannot be row-equivalent to $I_2$.
:::
<2>4. If $ad - bc \neq 0$, the entry $\delta = \frac{ad - bc}{a} \neq 0$.
Scale row 2 by $\frac{1}{\delta}$:
\[
\begin{pmatrix} 1 & b/a \\ 0 & \delta \end{pmatrix} \xrightarrow{R_2 \leftarrow \frac{1}{\delta} R_2} \begin{pmatrix} 1 & b/a \\ 0 & 1 \end{pmatrix} \xrightarrow{R_1 \leftarrow R_1 - \frac{b}{a} R_2} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2.
\]
Thus $A$ is row-equivalent to $I_2$, so $A$ is invertible.
::: {.proof}
sequence of elementary row operations producing $I_2$.
:::

<1>3. **Case 2: $a = 0$:** <2>1. If $a = 0$, then $ad - bc = -bc$.
::: {.proof}
$0 \cdot d - bc = -bc$.
:::
<2>2. If $c = 0$, the first column of $A = \begin{pmatrix} 0 & b \\ 0 & d \end{pmatrix}$ is zero, so $A$ has non-trivial nullspace and rank $\le 1$, meaning $A$ is not invertible.
Note that $ad - bc = -0 \cdot b = 0$.
::: {.proof}
a matrix with a zero column cannot be row-reduced to $I_2$.
:::
<2>3. If $c \neq 0$, swap rows 1 and 2:
\[
\begin{pmatrix} 0 & b \\ c & d \end{pmatrix} \xrightarrow{R_1 \leftrightarrow R_2} \begin{pmatrix} c & d \\ 0 & b \end{pmatrix} \xrightarrow{R_1 \leftarrow \frac{1}{c} R_1} \begin{pmatrix} 1 & d/c \\ 0 & b \end{pmatrix}.
\]
::: {.proof}
elementary row operations.
:::
<2>4. If $b = 0$, the second row is zero, so $A$ is not invertible, and $ad - bc = -0 \cdot c = 0$.
::: {.proof}
rank 1 matrix cannot be row-reduced to $I_2$.
:::
<2>5. If $b \neq 0$, then $ad - bc = -bc \neq 0$.
Scale $R_2$ by $1/b$ and clear the $(1,2)$ entry:
\[
\begin{pmatrix} 1 & d/c \\ 0 & b \end{pmatrix} \xrightarrow{R_2 \leftarrow \frac{1}{b} R_2} \begin{pmatrix} 1 & d/c \\ 0 & 1 \end{pmatrix} \xrightarrow{R_1 \leftarrow R_1 - \frac{d}{c} R_2} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2.
\]
Thus $A$ is invertible.
::: {.proof}
sequence of elementary row operations producing $I_2$.
:::

<1>4. Conclusion: In all cases, $A$ is row-equivalent to $I_2$ if and only if $ad - bc \neq 0$.
::: {.proof}
<1>2 and <1>3.
:::
Q.E.D.
:::
