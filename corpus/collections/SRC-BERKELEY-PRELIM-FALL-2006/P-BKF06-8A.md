---
schema: qual/card@1
id: P-BKF06-8A
kind: problem
title: Kernel, image and cokernel of a $3\times3$ integer matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 8A of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently recomputed the kernel, image, and cokernel. The retained
    solution's displayed diagonal form diag(3,0,0) is correct, but its
    subsequent Z/2 cokernel summand is a typo; the torsion summand is Z/3.
---

::: {.problem}
Let $\mathbb Z$ denote the integers and consider the homomorphism $\mathbb Z^3\to\mathbb Z^3$ defined by
\[
A=\begin{pmatrix}
6&9&12\\
6&9&12\\
12&18&24
\end{pmatrix}.
\]
Compute the structure of $\ker A$, $\operatorname{im}A$, and
\[
\operatorname{coker}A=\mathbb Z^3/\operatorname{im}A.
\]
In each case determine whether the group is free abelian; if it is, give a basis.
:::

::: {.solution}
Set
$$
v=
\begin{pmatrix}
1\\
1\\
2
\end{pmatrix}.
$$

<1>1. The image of $A$ is
$$
\operatorname{im}A
=
3\ZZ v
=
\ZZ
\begin{pmatrix}
3\\
3\\
6
\end{pmatrix}.
$$
In particular, it is free abelian of rank one with basis
$$
\boxed{
\left\{
\begin{pmatrix}
3\\
3\\
6
\end{pmatrix}
\right\}}.
$$

::: {.proof}
The three columns of $A$ are
$$
6v,
\qquad
9v,
\qquad
12v,
$$
so
$$
\operatorname{im}A
=
(6\ZZ+9\ZZ+12\ZZ)v.
$$
Since
$$
6\ZZ+9\ZZ+12\ZZ=3\ZZ,
$$
the claimed description follows. Equivalently,
$9v-6v=3v$ shows that the proposed generator itself lies in the
image.
:::

<1>2. The kernel of $A$ consists of the triples $(x,y,z)\in\ZZ^3$
satisfying
$$
2x+3y+4z=0.
$$

::: {.proof}
For $(x,y,z)^T\in\ZZ^3$,
$$
A
\begin{pmatrix}
x\\
y\\
z
\end{pmatrix}
=
(6x+9y+12z)
\begin{pmatrix}
1\\
1\\
2
\end{pmatrix}.
$$
Since $v\ne0$, this vanishes exactly when
$$
6x+9y+12z=0,
$$
or equivalently $2x+3y+4z=0$.
:::

<1>3. The kernel is free abelian of rank two with basis
$$
\boxed{
\left\{
\begin{pmatrix}
-3\\
2\\
0
\end{pmatrix},
\begin{pmatrix}
-2\\
0\\
1
\end{pmatrix}
\right\}}.
$$

::: {.proof}
If $(x,y,z)$ satisfies the equation in step <1>2, reducing modulo
$2$ shows that $y$ is even. Write $y=2s$. Then
$$
2x+6s+4z=0,
$$
so
$$
x=-3s-2z.
$$
Therefore
$$
\begin{pmatrix}
x\\
y\\
z
\end{pmatrix}
=
s
\begin{pmatrix}
-3\\
2\\
0
\end{pmatrix}
+
z
\begin{pmatrix}
-2\\
0\\
1
\end{pmatrix}.
$$
The two displayed vectors are visibly linearly independent over
$\ZZ$, so they form a basis.
:::

<1>4. The cokernel has structure
$$
\boxed{
\operatorname{coker}A
\simeq
\ZZ^2\oplus\ZZ/3\ZZ
}.
$$
It is not free abelian.

::: {.proof}
By step <1>1,
$$
\operatorname{im}A=3\ZZ v.
$$
The primitive vector $v=(1,1,2)^T$ extends to a basis of $\ZZ^3$;
for example,
$$
v,
\qquad
e_2=
\begin{pmatrix}
0\\
1\\
0
\end{pmatrix},
\qquad
e_3=
\begin{pmatrix}
0\\
0\\
1
\end{pmatrix}
$$
form a basis because the matrix with these columns has determinant
$1$. Hence
$$
\ZZ^3
=
\ZZ v\oplus\ZZ e_2\oplus\ZZ e_3,
$$
and quotienting by $3\ZZ v$ gives
$$
\ZZ^3/3\ZZ v
\simeq
(\ZZ/3\ZZ)\oplus\ZZ\oplus\ZZ.
$$
The class of $v$ has order exactly $3$, so the cokernel has nonzero
torsion and therefore is not free abelian.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1, <1>3, and <1>4 give the structures and the requested
bases in the free cases.
:::
:::
