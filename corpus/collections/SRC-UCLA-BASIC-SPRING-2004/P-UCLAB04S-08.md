---
schema: qual/card@1
id: P-UCLAB04S-08
kind: problem
title: Matrix and eigenvalues of a three-dimensional rotation
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 of the official UCLA Basic Exam Spring 2004 PDF; the rotation axis is the line through the vector $(1,0,-1)$.
---

::: {.problem}
Let $T:\mathbb R^3\to\mathbb R^3$ be a rotation about the axis determined by $(1,0,-1)$ through an angle of $30^\circ$; either orientation may be used.

(a) Find the matrix representation $A\in M_3(\mathbb R)$ of $T$ in the standard basis.
You need not multiply out matrices, but you must evaluate inverses.

(b) Find all eigenvalues of $A$ in $M_3(\mathbb R)$.

(c) Find all eigenvalues of $A$ when regarded as an element of $M_3(\mathbb C)$.
:::

::: {.solution}
Let
\[
u_3
=
\frac1{\sqrt2}(1,0,-1)
\]
be the unit vector along the rotation axis.

<1>1. An orthonormal basis of the plane perpendicular to the axis is
\[
u_1
=
\frac1{\sqrt2}(1,0,1),
\qquad
u_2
=
(0,1,0).
\]

::: {.proof}
One has
\[
u_1\cdot u_3
=
\frac{1-1}{2}
=0
\]
and
\[
u_2\cdot u_3=0.
\]
Also
\[
\|u_1\|=\|u_2\|=1
\]
and
\[
u_1\cdot u_2=0.
\]
Thus $u_1,u_2$ form an orthonormal basis of the two-dimensional orthogonal complement of the axis.
:::

<1>2. In the ordered orthonormal basis
\[
(u_1,u_2,u_3),
\]
the matrix of $T$ is
\[
R=
\begin{pmatrix}
\cos\frac{\pi}{6}&-\sin\frac{\pi}{6}&0\\
\sin\frac{\pi}{6}&\cos\frac{\pi}{6}&0\\
0&0&1
\end{pmatrix}
=
\begin{pmatrix}
\frac{\sqrt3}{2}&-\frac12&0\\
\frac12&\frac{\sqrt3}{2}&0\\
0&0&1
\end{pmatrix}.
\]

::: {.proof}
The transformation is a rotation through
\[
30^\circ=\frac{\pi}{6}
\]
on the plane perpendicular to the axis and fixes the axis pointwise.
The displayed matrix is the standard rotation matrix on the first two coordinates, with $1$ on the axis coordinate.
:::

<1>3. Let
\[
Q=
\begin{pmatrix}
\frac1{\sqrt2}&0&\frac1{\sqrt2}\\
0&1&0\\
\frac1{\sqrt2}&0&-\frac1{\sqrt2}
\end{pmatrix}.
\]
Then
\[
\boxed{Q^{-1}=Q^T=Q}.
\]

::: {.proof}
The columns of $Q$ are
\[
u_1,u_2,u_3,
\]
which form an orthonormal basis.
Hence $Q$ is orthogonal and
\[
Q^{-1}=Q^T.
\]
The matrix happens to be symmetric, so
\[
Q^T=Q.
\]
:::

<1>4. In the standard basis,
\[
\boxed{A=QRQ^T}.
\]

::: {.proof}
The matrix $Q$ changes coordinates from the basis
\[
(u_1,u_2,u_3)
\]
to the standard basis.
Therefore the standard-basis matrix is
\[
QRQ^{-1}
=
QRQ^T.
\]
Step <1>3 computes the inverse explicitly.
:::

<1>5. Over $\mathbb R$, the only eigenvalue of $A$ is
\[
\boxed{1}.
\]

::: {.proof}
Similarity preserves the characteristic polynomial, so $A$ and $R$ have the same eigenvalues.
The upper-left $2\times2$ rotation block has characteristic polynomial
\[
\lambda^2
-2\cos\frac{\pi}{6}\lambda
+1
=
\lambda^2-\sqrt3\,\lambda+1.
\]
Its discriminant is
\[
3-4=-1<0,
\]
so it has no real eigenvalues.
The final diagonal entry of $R$ is $1$, so $1$ is the only real eigenvalue.
:::

<1>6. Over $\mathbb C$, the eigenvalues are
\[
\boxed{
1,\qquad
e^{i\pi/6}
=
\frac{\sqrt3}{2}+\frac i2,
\qquad
e^{-i\pi/6}
=
\frac{\sqrt3}{2}-\frac i2
}.
\]

::: {.proof}
The two roots of
\[
\lambda^2-\sqrt3\,\lambda+1
\]
are
\[
\frac{\sqrt3\pm i}{2}.
\]
Together with the fixed-axis eigenvalue $1$, these are all three complex eigenvalues.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>4 answers part (a), step <1>5 answers part (b), and step <1>6 answers part (c).
:::
:::
