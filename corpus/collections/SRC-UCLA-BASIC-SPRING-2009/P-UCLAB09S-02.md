---
schema: qual/card@1
id: P-UCLAB09S-02
kind: problem
title: Operator norm of a two-by-two matrix
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
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Spring 2009.
---

::: {.problem}
Compute the operator norm of
$$
A=\begin{pmatrix}2&1\\0&\sqrt3\end{pmatrix};
$$
that is, determine the maximum of $\|Ax\|$ over all unit vectors $x$.
:::

::: {.solution}

::: pf

::: pf-step

One has
$$
A^TA
=
\begin{pmatrix}
4&2\\
2&4
\end{pmatrix}.
$$


::: pf-proof

Since
$$
A=
\begin{pmatrix}
2&1\\
0&\sqrt3
\end{pmatrix},
$$
one has
$$
A^T
=
\begin{pmatrix}
2&0\\
1&\sqrt3
\end{pmatrix}.
$$
Therefore
$$
\begin{aligned}
A^TA
&=
\begin{pmatrix}
2&0\\
1&\sqrt3
\end{pmatrix}
\begin{pmatrix}
2&1\\
0&\sqrt3
\end{pmatrix}\\
&=
\begin{pmatrix}
4&2\\
2&1+3
\end{pmatrix}\\
&=
\begin{pmatrix}
4&2\\
2&4
\end{pmatrix}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

The eigenvalues of $A^TA$ are
$$
\boxed{6\text{ and }2}.
$$


::: pf-proof

The characteristic polynomial is
$$
\begin{aligned}
\det(\lambda I-A^TA)
&=
\det
\begin{pmatrix}
\lambda-4&-2\\
-2&\lambda-4
\end{pmatrix}\\
&=
(\lambda-4)^2-4\\
&=
(\lambda-6)(\lambda-2).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

For every unit vector $x\in\RR^2$,
$$
\|Ax\|_2^2
=
x^TA^TAx
\le
6.
$$


::: pf-proof

The matrix $A^TA$ is real symmetric.
By the spectral theorem, it has an orthonormal eigenbasis, and its Rayleigh quotient
$$
x^TA^TAx
$$
on unit vectors lies between its smallest and largest eigenvalues.
By step [](#s1-2){.pf-ref}, the largest eigenvalue is $6$.
Hence
$$
x^TA^TAx\le6.
$$
Since
$$
\|Ax\|_2^2
=
(Ax)^TAx
=
x^TA^TAx,
$$
the claimed inequality follows.

:::

:::

::: {.pf-step #s1-4}

Equality in step [](#s1-3){.pf-ref} is attained.


::: pf-proof

For
$$
v=
\frac1{\sqrt2}
\begin{pmatrix}
1\\
1
\end{pmatrix},
$$
one has
$$
\|v\|_2=1
$$
and
$$
A^TAv
=
6v.
$$
Therefore
$$
\|Av\|_2^2
=
v^TA^TAv
=
6v^Tv
=6.
$$
Hence
$$
\|Av\|_2=\sqrt6.
$$

:::

:::

::: {.pf-step #s1-5}

Thus the operator norm is
$$
\boxed{\|A\|_{\mathrm{op}}=\sqrt6}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} shows that
$$
\|Ax\|_2\le\sqrt6
$$
for every unit vector $x$.
Step [](#s1-4){.pf-ref} gives a unit vector for which equality holds.
Therefore the maximum is exactly $\sqrt6$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required value of the operator norm.

:::

:::

:::
