---
schema: qual/card@1
id: P-UCLAB10F-09
kind: problem
title: Convergence of a linear stationary iteration
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Fall 2010.
---

::: {.problem}
Consider the iteration
$$
\vec x_{k+1}=A^{-1}(B\vec x_k+\vec c),
$$
where
$$
\vec c=\begin{pmatrix}1\\1\end{pmatrix},\qquad
A=\begin{pmatrix}2&0\\0&2\end{pmatrix},\qquad
B=\begin{pmatrix}2&1\\1&2\end{pmatrix}.
$$

(a) Assuming the iteration converges, to what vector $\vec x$ does it converge?

(b) Does the iteration converge for arbitrary initial vectors $\vec x_0$?
Justify your answer.
:::

::: {.solution}

Since
$$
A^{-1}=\frac12I,
$$
write the iteration as
$$
\vec x_{k+1}=C\vec x_k+\vec d,
$$
where
$$
C=A^{-1}B
=
\begin{pmatrix}
1&\frac12\\[1mm]
\frac12&1
\end{pmatrix}
$$
and
$$
\vec d=A^{-1}\vec c
=
\begin{pmatrix}
\frac12\\[1mm]
\frac12
\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1-1}

If the iteration converges to a vector $\vec x$, then
$$
\vec x=C\vec x+\vec d.
$$


::: pf-proof

Assume
$$
\vec x_k\to\vec x.
$$
Matrix multiplication and addition are continuous, so passing to the limit in
$$
\vec x_{k+1}=C\vec x_k+\vec d
$$
gives
$$
\vec x=C\vec x+\vec d.
$$

:::

:::

::: {.pf-step #s1-2}

The unique fixed point is
$$
\boxed{
\vec x=
\begin{pmatrix}
-1\\
-1
\end{pmatrix}
}.
$$


::: pf-proof

The fixed-point equation from step [](#s1-1){.pf-ref} is
$$
(I-C)\vec x=\vec d.
$$
Now
$$
I-C
=
\begin{pmatrix}
0&-\frac12\\[1mm]
-\frac12&0
\end{pmatrix},
$$
so the equations are
$$
-\frac12x_2=\frac12,
\qquad
-\frac12x_1=\frac12.
$$
Hence
$$
x_1=x_2=-1.
$$
Thus any convergent iteration must converge to the displayed vector.

:::

:::

::: {.pf-step #s1-3}

If
$$
\vec x_*=
\begin{pmatrix}
-1\\
-1
\end{pmatrix},
\qquad
\vec e_k=\vec x_k-\vec x_*,
$$
then
$$
\vec e_{k+1}=C\vec e_k.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\vec x_*=C\vec x_*+\vec d.
$$
Subtract this fixed-point identity from
$$
\vec x_{k+1}=C\vec x_k+\vec d
$$
to obtain
$$
\vec x_{k+1}-\vec x_*
=
C(\vec x_k-\vec x_*).
$$

:::

:::

::: {.pf-step #s1-4}

The matrix $C$ has eigenvalue
$$
\frac32
$$
with eigenvector
$$
u=
\begin{pmatrix}
1\\
1
\end{pmatrix}.
$$


::: pf-proof

Direct multiplication gives
$$
Cu
=
\begin{pmatrix}
1+\frac12\\[1mm]
\frac12+1
\end{pmatrix}
=
\frac32
\begin{pmatrix}
1\\
1
\end{pmatrix}.
$$

:::

:::

::: {.pf-step #s1-5}

The iteration does not converge for arbitrary initial vectors.


::: pf-proof

Take
$$
\vec x_0=
\begin{pmatrix}
0\\
0
\end{pmatrix}.
$$
Then
$$
\vec e_0
=
\vec x_0-\vec x_*
=
\begin{pmatrix}
1\\
1
\end{pmatrix}
=u.
$$
By steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref},
$$
\vec e_k=C^ku
=
\left(\frac32\right)^ku.
$$
Therefore
$$
\|\vec e_k\|\to\infty,
$$
so $\vec x_k$ does not converge.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} answers part (a), and step [](#s1-5){.pf-ref} answers part (b) negatively.

:::

:::

:::
