---
schema: qual/card@1
id: P-UGAP08S-05
kind: problem
title: Orthogonally diagonalize a three-by-three constant-off-diagonal matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let
\[
A=\begin{pmatrix}
2&1&1\\
1&2&1\\
1&1&2
\end{pmatrix}.
\]
Find an orthogonal matrix $Q$ such that $Q^{-1}AQ$ is diagonal.
:::

::: {.solution}
<1>1. Write
\[
A
=
I_3+J,
\]
where
\[
J
=
\begin{pmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{pmatrix}.
\]

::: {.proof}
Adding the identity matrix to the all-ones matrix changes each diagonal
entry from $1$ to $2$ and leaves the off-diagonal entries equal to $1$.
:::

<1>2. The vector
\[
u_1
=
\begin{pmatrix}
1\\
1\\
1
\end{pmatrix}
\]
is an eigenvector with eigenvalue
\[
4.
\]

::: {.proof}
One has
\[
Ju_1
=
3u_1.
\]
Therefore
\[
Au_1
=
(I_3+J)u_1
=
u_1+3u_1
=
4u_1.
\]
:::

<1>3. Every vector
\[
v
\]
orthogonal to $u_1$ is an eigenvector with eigenvalue
\[
1.
\]

::: {.proof}
Let
\[
v
=
\begin{pmatrix}
x\\y\\z
\end{pmatrix}
\]
with
\[
x+y+z=0.
\]
Then
\[
Jv
=
\begin{pmatrix}
x+y+z\\
x+y+z\\
x+y+z
\end{pmatrix}
=
0.
\]
Hence
\[
Av
=
(I_3+J)v
=
v.
\]
:::

<1>4. Choose
\[
u_2
=
\begin{pmatrix}
1\\
-1\\
0
\end{pmatrix}
\]
and
\[
u_3
=
\begin{pmatrix}
1\\
1\\
-2
\end{pmatrix}.
\]
Then
\[
u_1,u_2,u_3
\]
are pairwise orthogonal eigenvectors.

::: {.proof}
The coordinate sums of $u_2$ and $u_3$ are zero, so step <1>3 gives
eigenvalue $1$ for both.

Their dot products are
\[
u_1\cdot u_2
=
1-1+0
=
0,
\]
\[
u_1\cdot u_3
=
1+1-2
=
0,
\]
and
\[
u_2\cdot u_3
=
1-1+0
=
0.
\]
:::

<1>5. Their norms are
\[
\|u_1\|
=
\sqrt3,
\qquad
\|u_2\|
=
\sqrt2,
\qquad
\|u_3\|
=
\sqrt6.
\]

::: {.proof}
Compute directly:
\[
1^2+1^2+1^2=3,
\]
\[
1^2+(-1)^2=2,
\]
and
\[
1^2+1^2+(-2)^2=6.
\]
:::

<1>6. Hence an orthonormal eigenbasis is
\[
v_1
=
\frac1{\sqrt3}
\begin{pmatrix}
1\\1\\1
\end{pmatrix},
\]
\[
v_2
=
\frac1{\sqrt2}
\begin{pmatrix}
1\\-1\\0
\end{pmatrix},
\]
\[
v_3
=
\frac1{\sqrt6}
\begin{pmatrix}
1\\1\\-2
\end{pmatrix}.
\]

::: {.proof}
Normalize the pairwise orthogonal eigenvectors from steps <1>4--<1>5.
:::

<1>7. Define
\[
\boxed{
Q
=
\begin{pmatrix}
\frac1{\sqrt3}
&
\frac1{\sqrt2}
&
\frac1{\sqrt6}
\\[2mm]
\frac1{\sqrt3}
&
-\frac1{\sqrt2}
&
\frac1{\sqrt6}
\\[2mm]
\frac1{\sqrt3}
&
0
&
-\frac2{\sqrt6}
\end{pmatrix}.
}
\]
Then $Q$ is orthogonal.

::: {.proof}
Its columns are the orthonormal vectors
\[
v_1,v_2,v_3.
\]
Therefore
\[
Q^TQ
=
I,
\]
so
\[
Q^{-1}
=
Q^T.
\]
:::

<1>8. One has
\[
AQ
=
Q
\begin{pmatrix}
4&0&0\\
0&1&0\\
0&0&1
\end{pmatrix}.
\]

::: {.proof}
The columns of $Q$ are eigenvectors of $A$ with eigenvalues
\[
4,1,1,
\]
respectively.
Multiplying $A$ by $Q$ therefore multiplies each column by its eigenvalue.
:::

<1>9. Hence
\[
\boxed{
Q^{-1}AQ
=
Q^TAQ
=
\begin{pmatrix}
4&0&0\\
0&1&0\\
0&0&1
\end{pmatrix}.
}
\]

::: {.proof}
Left-multiply the identity in step <1>8 by
\[
Q^{-1}=Q^T.
\]
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>7 gives an explicit orthogonal matrix and step <1>9 gives the
required diagonalization.
:::
:::
