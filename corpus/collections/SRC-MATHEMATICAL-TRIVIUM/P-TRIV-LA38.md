---
schema: qual/card@1
id: P-TRIV-LA38
kind: problem
title: Rotation--scaling--shear decomposition of $SL_2(\RR)$ matrices
classification:
  areas: [prelim]
  topics:
  - Special Linear Group
  - Matrix Decompositions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 38, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the matrix $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, $a, b, c, d \in \RR$, $\det A = 1$. It transforms the basis vectors $\vec{e}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$, $\vec{e}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$ into $\vec{g}_1 = \begin{bmatrix} a \\ c \end{bmatrix}$, $\vec{g}_2 = \begin{bmatrix} b \\ d \end{bmatrix}$. One can obtain a useful decomposition of $A$ by making an inverse transformation in three steps.

(a) Construct the rotation matrix $R^{-1}$ that sends $\vec{g}_1$ to $R^{-1}(\vec{g}_1) \parallel \vec{e}_1$. How does it act on $\vec{g}_2$?

(b) Construct the diagonal matrix $P^{-1}$ such that $\det P^{-1} = 1$ and $P^{-1}(R^{-1}(\vec{g}_1)) = \vec{e}_1$. Show that the components of $P^{-1}(R^{-1}(\vec{g}_2))$ are $\begin{bmatrix} x \\ 1 \end{bmatrix}$, $x \in \RR$.

(c) Apply a shear transformation $T^{-1}$ that leaves $\vec{e}_1$ invariant and sends $P^{-1}(R^{-1}(\vec{g}_2))$ to $\vec{e}_2$. Then, we have $T^{-1}P^{-1}R^{-1}A = E$, or $A = RPT$.

(d) Show that this decomposition is unique.
:::

::: {.solution}

Write
$$
g_1=
\begin{pmatrix}a\\c\end{pmatrix},
\qquad
g_2=
\begin{pmatrix}b\\d\end{pmatrix},
$$
and put
$$
r=\sqrt{a^2+c^2}>0.
$$

::: pf

::: {.pf-step #s1-1}

Define
$$
R=
\frac1r
\begin{pmatrix}
a&-c\\
c&a
\end{pmatrix}.
$$
Then $R$ is a rotation matrix.


::: pf-proof

Its columns are orthonormal because
$$
a^2+c^2=r^2,
$$
and
$$
\det R
=
\frac{a^2+c^2}{r^2}
=1.
$$
Thus $R\in SO(2)$.

:::

:::

::: {.pf-step #s1-2}

One has
$$
R^{-1}g_1
=
\begin{pmatrix}r\\0\end{pmatrix}.
$$


::: pf-proof

Since
$$
R^{-1}=R^T
=
\frac1r
\begin{pmatrix}
a&c\\
-c&a
\end{pmatrix},
$$
direct multiplication gives
$$
R^{-1}g_1
=
\frac1r
\begin{pmatrix}
a^2+c^2\\
-ca+ac
\end{pmatrix}
=
\begin{pmatrix}r\\0\end{pmatrix}.
$$

:::

:::

::: {.pf-step #s1-3}

The transformed second column is
$$
R^{-1}g_2
=
\begin{pmatrix}
\dfrac{ab+cd}{r}\\[4pt]
\dfrac1r
\end{pmatrix}.
$$


::: pf-proof

Direct multiplication gives first component $(ab+cd)/r$. The second is
$$
\frac{-cb+ad}{r}
=
\frac{ad-bc}{r}
=
\frac1r,
$$
because $\det A=1$.

:::

:::

::: {.pf-step #s1-4}

Part (a) follows.


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} construct the required rotation and describe its action on
both columns.

:::

:::

::: {.pf-step #s1-5}

Define
$$
P^{-1}
=
\begin{pmatrix}
r^{-1}&0\\
0&r
\end{pmatrix}.
$$
Then
$$
\det P^{-1}=1
$$
and
$$
P^{-1}R^{-1}g_1=e_1.
$$


::: pf-proof

The determinant is $r^{-1}r=1$. By step [](#s1-2){.pf-ref},
$$
P^{-1}
\begin{pmatrix}r\\0\end{pmatrix}
=
\begin{pmatrix}1\\0\end{pmatrix}.
$$

:::

:::

::: {.pf-step #s1-6}

One has
$$
P^{-1}R^{-1}g_2
=
\begin{pmatrix}x\\1\end{pmatrix},
\qquad
x=\frac{ab+cd}{r^2}.
$$


::: pf-proof

Apply $P^{-1}$ to the vector in step [](#s1-3){.pf-ref}:
$$
\begin{pmatrix}
r^{-1}&0\\
0&r
\end{pmatrix}
\begin{pmatrix}
(ab+cd)/r\\
1/r
\end{pmatrix}
=
\begin{pmatrix}
(ab+cd)/r^2\\
1
\end{pmatrix}.
$$

:::

:::

::: {.pf-step #s1-7}

Part (b) follows.


::: pf-proof

Steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} give the required diagonal transformation and the claimed
coordinates of the second column.

:::

:::

::: {.pf-step #s1-8}

Define
$$
T^{-1}
=
\begin{pmatrix}
1&-x\\
0&1
\end{pmatrix}.
$$
Then
$$
T^{-1}e_1=e_1
$$
and
$$
T^{-1}
\begin{pmatrix}x\\1\end{pmatrix}
=
e_2.
$$


::: pf-proof

Directly,
$$
\begin{pmatrix}
1&-x\\
0&1
\end{pmatrix}
\begin{pmatrix}1\\0\end{pmatrix}
=
\begin{pmatrix}1\\0\end{pmatrix},
$$
and
$$
\begin{pmatrix}
1&-x\\
0&1
\end{pmatrix}
\begin{pmatrix}x\\1\end{pmatrix}
=
\begin{pmatrix}0\\1\end{pmatrix}.
$$

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
T^{-1}P^{-1}R^{-1}A=I.
$$


::: pf-proof

The columns of $A$ are $g_1,g_2$. By steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref}, the first two inverse
steps send those columns to
$$
e_1
\qquad\text{and}\qquad
\begin{pmatrix}x\\1\end{pmatrix}.
$$
Step [](#s1-8){.pf-ref} sends these to $e_1,e_2$, respectively. Hence the resulting matrix
is the identity.

:::

:::

::: {.pf-step #s1-10}

Thus
$$
\boxed{A=RPT},
$$
where
$$
R=
\frac1r
\begin{pmatrix}
a&-c\\
c&a
\end{pmatrix},
$$
$$
P=
\begin{pmatrix}
r&0\\
0&r^{-1}
\end{pmatrix},
$$
and
$$
T=
\begin{pmatrix}
1&x\\
0&1
\end{pmatrix},
\qquad
x=\frac{ab+cd}{a^2+c^2}.
$$


::: pf-proof

Invert the identity in step [](#s1-9){.pf-ref}. The formulas for $P$ and $T$ are the
inverses of those in steps [](#s1-5){.pf-ref} and [](#s1-8){.pf-ref}, and $r^2=a^2+c^2$.

:::

:::

::: {.pf-step #s1-11}

Part (c) follows.


::: pf-proof

Steps [](#s1-8){.pf-ref} through [](#s1-10){.pf-ref} construct the required shear and yield the decomposition.

:::

:::

::: {.pf-step #s1-12}

The factor $R$ is uniquely determined.


::: pf-proof

In any decomposition of the required form, the first column of $A$ is
$$
A e_1=RPT e_1.
$$
Since
$$
Te_1=e_1
$$
and
$$
Pe_1=r e_1
$$
with $r>0$, one has
$$
g_1=rRe_1.
$$
Thus $r=\norm{g_1}$ and $Re_1=g_1/\norm{g_1}$. A rotation in $SO(2)$ is uniquely
determined by its first column, so $R$ is unique.

:::

:::

::: {.pf-step #s1-13}

The factor $P$ is uniquely determined.


::: pf-proof

Step [](#s1-12){.pf-ref} fixes
$$
r=\norm{g_1}=\sqrt{a^2+c^2}.
$$
The required positive diagonal matrix with determinant $1$ and first diagonal
entry $r$ is uniquely
$$
P=\operatorname{diag}(r,r^{-1}).
$$

:::

:::

::: {.pf-step #s1-14}

The factor $T$ is uniquely determined.


::: pf-proof

Once $R$ and $P$ are fixed,
$$
T=P^{-1}R^{-1}A.
$$
Equivalently, step [](#s1-6){.pf-ref} uniquely determines its shear parameter
$$
x=\frac{ab+cd}{r^2}.
$$

:::

:::

::: {.pf-step #s1-15}

Therefore the decomposition
$$
\boxed{A=RPT}
$$
with $R\in SO(2)$, $P=\operatorname{diag}(r,r^{-1})$ for $r>0$, and
$T=\begin{pmatrix}1&x\\0&1\end{pmatrix}$ is unique.


::: pf-proof

Steps [](#s1-12){.pf-ref} through [](#s1-14){.pf-ref} show uniqueness of the three factors successively.

:::

:::

::: {.pf-step #s1-16}

Part (d) follows.


::: pf-proof

This is step [](#s1-15){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref}, [](#s1-7){.pf-ref}, and [](#s1-11){.pf-ref}, and [](#s1-16){.pf-ref} establish parts (a)--(d).

:::

:::

:::
