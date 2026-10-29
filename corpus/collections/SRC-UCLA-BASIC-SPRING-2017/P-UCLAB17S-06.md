---
schema: qual/card@1
id: P-UCLAB17S-06
kind: problem
title: Frobenius inner product on real matrices
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2017, `assets/attachments/basic-17S.pdf`.
---

::: {.problem}
Let $V=M_n(\RR)$. Prove that
$$
\langle A,B\rangle=\operatorname{tr}(A^TB)
$$
defines an inner product on $V$. For $n=2$, find an orthonormal basis.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For
$$
A=(a_{ij}),
\qquad
B=(b_{ij}),
$$
one has
$$
\boxed{
\operatorname{tr}(A^TB)
=
\sum_{i,j=1}^n a_{ij}b_{ij}.
}
$$


::: pf-proof

The $j$th diagonal entry of $A^TB$ is
$$
(A^TB)_{jj}
=
\sum_{i=1}^n
(A^T)_{ji}B_{ij}
=
\sum_{i=1}^n
a_{ij}b_{ij}.
$$
Summing over $j$ gives the formula.

:::

:::

::: {.pf-step #s1-2}

The form is bilinear.


::: pf-proof

Using step [](#s1-1){.pf-ref},
$$
\langle A,B\rangle
=
\sum_{i,j}a_{ij}b_{ij}.
$$
This expression is linear in the entries of $A$ while $B$ is fixed and linear in the entries of $B$ while $A$ is fixed.
Thus the form is bilinear.

:::

:::

::: {.pf-step #s1-3}

The form is symmetric:
$$
\langle A,B\rangle
=
\langle B,A\rangle.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\langle A,B\rangle
=
\sum_{i,j}a_{ij}b_{ij}
=
\sum_{i,j}b_{ij}a_{ij}
=
\langle B,A\rangle.
$$

:::

:::

::: {.pf-step #s1-4}

One has
$$
\langle A,A\rangle
=
\sum_{i,j=1}^n a_{ij}^2
\ge
0.
$$


::: pf-proof

Apply step [](#s1-1){.pf-ref} with
$$
B=A.
$$
The result is a sum of squares.

:::

:::

::: {.pf-step #s1-5}

Equality
$$
\langle A,A\rangle=0
$$
holds if and only if
$$
A=0.
$$


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
\langle A,A\rangle
=
\sum_{i,j}a_{ij}^2.
$$
This sum vanishes exactly when every entry $a_{ij}$ is zero.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\langle A,B\rangle
=
\operatorname{tr}(A^TB)
}
$$
defines an inner product on
$$
M_n(\RR).
$$


::: pf-proof

Steps [](#s1-2){.pf-ref} through [](#s1-5){.pf-ref} establish bilinearity, symmetry, and positive definiteness.

:::

:::

::: {.pf-step #s1-7}

For
$$
n=2,
$$
define
$$
E_{11}
=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\quad
E_{12}
=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
$$
$$
E_{21}
=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix},
\quad
E_{22}
=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}.
$$


::: pf-proof

These are the standard matrix units.

:::

:::

::: {.pf-step #s1-8}

The four matrices in step [](#s1-7){.pf-ref} are orthonormal.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\langle E_{ij},E_{kl}\rangle
=
\sum_{r,s}
(E_{ij})_{rs}
(E_{kl})_{rs}.
$$
Each matrix unit has exactly one entry equal to $1$ and all others equal to $0$.
Thus the inner product is
$$
1
$$
when
$$
(i,j)=(k,l)
$$
and
$$
0
$$
otherwise.

:::

:::

::: {.pf-step #s1-9}

The four matrices form a basis of
$$
M_2(\RR).
$$


::: pf-proof

Every matrix
$$
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
$$
has the unique expansion
$$
aE_{11}
+
bE_{12}
+
cE_{21}
+
dE_{22}.
$$
Thus the four matrix units span and are linearly independent.

:::

:::

::: {.pf-step #s1-10}

Hence an orthonormal basis for
$$
M_2(\RR)
$$
is
$$
\boxed{
\{E_{11},E_{12},E_{21},E_{22}\}.
}
$$


::: pf-proof

Combine steps [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves the inner-product assertion, and step [](#s1-10){.pf-ref} gives the requested orthonormal basis for $n=2$.

:::

:::

:::
