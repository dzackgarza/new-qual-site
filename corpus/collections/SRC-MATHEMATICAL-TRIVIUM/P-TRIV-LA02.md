---
schema: qual/card@1
id: P-TRIV-LA02
kind: problem
title: Powers, inverse, eigenvalues and diagonalization of $\begin{pmatrix}1&2\\5&4\end{pmatrix}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 2, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the matrix $A = { \left[ \begin{array} { l l } { 1 } & { 2 } \\ { 5 } & { 4 } \end{array} \right] }$

(a)Find $A ^ { T } , A ^ { 2 } , A ^ { 3 } , A ^ { - 1 }$ , TrA, det A.

(b) Find the eigenvalues and the eigenvectors of A.

(c) Write the transformation that reduces A to diagonal form.
:::

Let
$$
A=
\begin{pmatrix}
1&2\\
5&4
\end{pmatrix}.
$$

::: pf

::: pf-step

The transpose is
$$
\boxed{
A^T=
\begin{pmatrix}
1&5\\
2&4
\end{pmatrix}.
}
$$


::: pf-proof

Transpose exchanges rows and columns.

:::

:::

::: pf-step

One has
$$
\boxed{
A^2=
\begin{pmatrix}
11&10\\
25&26
\end{pmatrix}.
}
$$


::: pf-proof

Direct multiplication gives
$$
\begin{pmatrix}
1&2\\
5&4
\end{pmatrix}
\begin{pmatrix}
1&2\\
5&4
\end{pmatrix}
=
\begin{pmatrix}
1+10&2+8\\
5+20&10+16
\end{pmatrix}.
$$

:::

:::

::: pf-step

One has
$$
\boxed{
A^3=
\begin{pmatrix}
61&62\\
155&154
\end{pmatrix}.
}
$$


::: pf-proof

Multiply step <1>2 by $A$:
$$
\begin{pmatrix}
11&10\\
25&26
\end{pmatrix}
\begin{pmatrix}
1&2\\
5&4
\end{pmatrix}
=
\begin{pmatrix}
61&62\\
155&154
\end{pmatrix}.
$$

:::

:::

::: pf-step

The trace and determinant are
$$
\boxed{
\operatorname{tr}A=5,
\qquad
\det A=-6.
}
$$


::: pf-proof

One has
$$
\operatorname{tr}A=1+4=5
$$
and
$$
\det A
=
1\cdot4-2\cdot5
=
-6.
$$

:::

:::

::: pf-step

The inverse is
$$
\boxed{
A^{-1}
=
\begin{pmatrix}
-2/3&1/3\\
5/6&-1/6
\end{pmatrix}.
}
$$


::: pf-proof

Since $\det A=-6\neq0$,
$$
A^{-1}
=
\frac1{-6}
\begin{pmatrix}
4&-2\\
-5&1
\end{pmatrix}.
$$
Simplifying gives the displayed matrix.

:::

:::

::: pf-step

Part (a) follows.


::: pf-proof

Steps <1>1--<1>5 compute all requested quantities.

:::

:::

::: pf-step

The characteristic polynomial is
$$
\chi_A(\lambda)
=
\lambda^2-5\lambda-6
=
(\lambda-6)(\lambda+1).
$$


::: pf-proof

Using step <1>4,
$$
\chi_A(\lambda)
=
\lambda^2
-
(\operatorname{tr}A)\lambda
+
\det A
=
\lambda^2-5\lambda-6.
$$

:::

:::

::: pf-step

The eigenvalues are
$$
\boxed{6\text{ and }-1}.
$$


::: pf-proof

These are the roots of the characteristic polynomial in step <1>7.

:::

:::

::: pf-step

For $\lambda=6$, an eigenvector is
$$
\boxed{
v_6=
\begin{pmatrix}
2\\
5
\end{pmatrix}.
}
$$


::: pf-proof

One has
$$
(A-6I)
\begin{pmatrix}
2\\
5
\end{pmatrix}
=
\begin{pmatrix}
-5&2\\
5&-2
\end{pmatrix}
\begin{pmatrix}
2\\
5
\end{pmatrix}
=
\begin{pmatrix}
0\\
0
\end{pmatrix}.
$$

:::

:::

::: pf-step

For $\lambda=-1$, an eigenvector is
$$
\boxed{
v_{-1}
=
\begin{pmatrix}
1\\
-1
\end{pmatrix}.
}
$$


::: pf-proof

One has
$$
(A+I)
\begin{pmatrix}
1\\
-1
\end{pmatrix}
=
\begin{pmatrix}
2&2\\
5&5
\end{pmatrix}
\begin{pmatrix}
1\\
-1
\end{pmatrix}
=
\begin{pmatrix}
0\\
0
\end{pmatrix}.
$$

:::

:::

::: pf-step

Part (b) follows.


::: pf-proof

Steps <1>8--<1>10 give both eigenvalues and corresponding eigenvectors.

:::

:::

::: pf-step

Define
$$
P=
\begin{pmatrix}
2&1\\
5&-1
\end{pmatrix}.
$$
Then
$$
\det P=-7\neq0.
$$


::: pf-proof

The columns of $P$ are the two eigenvectors from steps <1>9 and <1>10.
Their determinant is
$$
2(-1)-5(1)=-7.
$$

:::

:::

::: pf-step

One has
$$
\boxed{
P^{-1}AP
=
\begin{pmatrix}
6&0\\
0&-1
\end{pmatrix}.
}
$$


::: pf-proof

Since the first column of $P$ is an eigenvector for $6$ and the second an
eigenvector for $-1$,
$$
AP
=
P
\begin{pmatrix}
6&0\\
0&-1
\end{pmatrix}.
$$
Multiply on the left by $P^{-1}$.

:::

:::

::: pf-step

The change of coordinates
$$
x=Py
$$
reduces the transformation to diagonal form.


::: pf-proof

If the original transformation is
$$
x\longmapsto Ax,
$$
then with $x=Py$,
$$
y\longmapsto P^{-1}AP,y.
$$
Step <1>13 shows that this matrix is diagonal.

:::

:::

::: pf-step

Part (c) follows.


::: pf-proof

Steps <1>12--<1>14 give the diagonalizing transformation.

:::

:::

::: pf-qed

Steps <1>6, <1>11, and <1>15 establish parts (a), (b), and (c), respectively.

:::

:::
