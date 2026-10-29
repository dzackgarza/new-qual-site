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
Let $T:\RR^3\to\RR^3$ be a rotation about the axis determined by $(1,0,-1)$ through an angle of $30^\circ$; either orientation may be used.

(a) Find the matrix representation $A\in M_3(\RR)$ of $T$ in the standard basis.
You need not multiply out matrices, but you must evaluate inverses.

(b) Find all eigenvalues of $A$ in $M_3(\RR)$.

(c) Find all eigenvalues of $A$ when regarded as an element of $M_3(\CC)$.
:::

::: {.solution}

Let
\[
u_3
=
\frac1{\sqrt2}(1,0,-1)
\]
be the unit vector along the rotation axis.

::: pf

::: pf-step

An orthonormal basis of the plane perpendicular to the axis is
\[
u_1
=
\frac1{\sqrt2}(1,0,1),
\qquad
u_2
=
(0,1,0).
\]


::: pf-proof

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

:::

::: pf-step

In the ordered orthonormal basis
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


::: pf-proof

The transformation is a rotation through
\[
30^\circ=\frac{\pi}{6}
\]
on the plane perpendicular to the axis and fixes the axis pointwise.
The displayed matrix is the standard rotation matrix on the first two coordinates, with $1$ on the axis coordinate.

:::

:::

::: {.pf-step #s1-3}

Let
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


::: pf-proof

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

:::

::: {.pf-step #s1-4}

In the standard basis,
\[
\boxed{A=QRQ^T}.
\]


::: pf-proof

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
Step [](#s1-3){.pf-ref} computes the inverse explicitly.

:::

:::

::: {.pf-step #s1-5}

Over $\RR$, the only eigenvalue of $A$ is
\[
\boxed{1}.
\]


::: pf-proof

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

:::

::: {.pf-step #s1-6}

Over $\CC$, the eigenvalues are
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


::: pf-proof

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

:::

::: pf-qed

Step [](#s1-4){.pf-ref} answers part (a), step [](#s1-5){.pf-ref} answers part (b), and step [](#s1-6){.pf-ref} answers part (c).

:::

:::

:::
