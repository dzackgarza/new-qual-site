---
schema: qual/card@1
id: P-TRIV-LA13
kind: problem
title: Rotation and reflection matrices in $\mathbb{R}^2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 13, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the matrices $A = { \left[ \begin{array} { l l } { \cos \phi } & { - \sin \phi } \\ { \sin \phi } & { \cos \phi } \end{array} \right] } , B = { \left[ \begin{array} { l l } { \cos \phi } & { \sin \phi } \\ { \sin \phi } & { - \cos \phi } \end{array} \right] }$

(a) Calculate $A ^ { - 1 } , B ^ { - 1 }$

(b) Give a geometrical interpretation of the action of A and B on vectors in $\mathbb { R } ^ { 2 }$

(c) What can one say about the eigenvectors of A and B?
:::

Write
$$
c=\cos\phi,
\qquad
s=\sin\phi.
$$

::: pf

::: pf-step

One has
$$
A^TA=I.
$$


::: pf-proof

Since
$$
A^T=
\begin{pmatrix}
c&s\\
-s&c
\end{pmatrix},
$$
direct multiplication gives
$$
A^TA=
\begin{pmatrix}
c^2+s^2&0\\
0&c^2+s^2
\end{pmatrix}
=I.
$$

:::

:::

::: pf-step

Therefore
$$
\boxed{
A^{-1}
=
A^T
=
\begin{pmatrix}
\cos\phi&\sin\phi\\
-\sin\phi&\cos\phi
\end{pmatrix}.
}
$$


::: pf-proof

This follows from step <1>1.

:::

:::

::: pf-step

One has
$$
B^2=I.
$$


::: pf-proof

Direct multiplication gives
$$
B^2
=
\begin{pmatrix}
c&s\\
s&-c
\end{pmatrix}^2
=
\begin{pmatrix}
c^2+s^2&0\\
0&c^2+s^2
\end{pmatrix}
=I.
$$

:::

:::

::: pf-step

Therefore
$$
\boxed{B^{-1}=B}.
$$


::: pf-proof

Step <1>3 gives $B^2=I$.

:::

:::

::: pf-step

Part (a) follows.


::: pf-proof

Steps <1>2 and <1>4 give both inverses.

:::

:::

::: pf-step

The matrix $A$ rotates vectors counterclockwise by angle $\phi$.


::: pf-proof

For a unit vector
$$
v=
\begin{pmatrix}
\cos\theta\\
\sin\theta
\end{pmatrix},
$$
one has
$$
Av
=
\begin{pmatrix}
\cos(\theta+\phi)\\
\sin(\theta+\phi)
\end{pmatrix}
$$
by the angle-addition formulas.

:::

:::

::: pf-step

The matrix $B$ reflects vectors across the line making angle
$$
\frac\phi2
$$
with the positive $x$-axis.


::: pf-proof

Reflection across a line making angle $\theta$ with the $x$-axis has matrix
$$
\begin{pmatrix}
\cos2\theta&\sin2\theta\\
\sin2\theta&-\cos2\theta
\end{pmatrix}.
$$
Setting $\theta=\phi/2$ gives exactly $B$.

:::

:::

::: pf-step

Part (b) follows.


::: pf-proof

Steps <1>6 and <1>7 give the geometrical interpretations.

:::

:::

::: pf-step

The reflection matrix $B$ has eigenvalue $1$ with eigenvector
$$
u_+
=
\begin{pmatrix}
\cos(\phi/2)\\
\sin(\phi/2)
\end{pmatrix}
$$
and eigenvalue $-1$ with eigenvector
$$
u_-
=
\begin{pmatrix}
-\sin(\phi/2)\\
\cos(\phi/2)
\end{pmatrix}.
$$


::: pf-proof

By step <1>7, vectors along the reflection axis are fixed, while vectors
perpendicular to that axis have their sign reversed. The two displayed vectors
span those two directions.

:::

:::

::: pf-step

Over $\mathbb C$, the rotation matrix $A$ has eigenvalues
$$
e^{i\phi}
\qquad\text{and}\qquad
e^{-i\phi},
$$
with eigenvectors
$$
\begin{pmatrix}1\\-i\end{pmatrix}
\qquad\text{and}\qquad
\begin{pmatrix}1\\i\end{pmatrix},
$$
respectively.


::: pf-proof

Directly,
$$
A
\begin{pmatrix}1\\-i\end{pmatrix}
=
(c+is)
\begin{pmatrix}1\\-i\end{pmatrix}
=
e^{i\phi}
\begin{pmatrix}1\\-i\end{pmatrix},
$$
and similarly for $e^{-i\phi}$.

:::

:::

::: pf-step

Over $\mathbb R$, $A$ has real eigenvectors only when
$$
\sin\phi=0.
$$


::: pf-proof

The eigenvalues from step <1>10 are real exactly when
$$
e^{i\phi}=\pm1,
$$
equivalently $\phi\equiv0$ or $\pi$ modulo $2\pi$. In those cases
$$
A=I
$$
or
$$
A=-I,
$$
so every nonzero real vector is an eigenvector. Otherwise the eigenvalues are
nonreal, hence there are no real eigendirections.

:::

:::

::: pf-step

Part (c) follows.


::: pf-proof

Steps <1>9--<1>11 describe the eigendirections of both matrices.

:::

:::

::: pf-qed

Steps <1>5, <1>8, and <1>12 establish parts (a), (b), and (c), respectively.

:::

:::
