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
Let $V=M_n(\mathbb R)$. Prove that
\[
\langle A,B\rangle=\operatorname{tr}(A^TB)
\]
defines an inner product on $V$. For $n=2$, find an orthonormal basis.
:::

::: {.solution}
<1>1. For
\[
A=(a_{ij}),
\qquad
B=(b_{ij}),
\]
one has
\[
\boxed{
\operatorname{tr}(A^TB)
=
\sum_{i,j=1}^n a_{ij}b_{ij}.
}
\]

::: {.proof}
The $j$th diagonal entry of $A^TB$ is
\[
(A^TB)_{jj}
=
\sum_{i=1}^n
(A^T)_{ji}B_{ij}
=
\sum_{i=1}^n
a_{ij}b_{ij}.
\]
Summing over $j$ gives the formula.
:::

<1>2. The form is bilinear.

::: {.proof}
Using step <1>1,
\[
\langle A,B\rangle
=
\sum_{i,j}a_{ij}b_{ij}.
\]
This expression is linear in the entries of $A$ while $B$ is fixed and linear in the entries of $B$ while $A$ is fixed.
Thus the form is bilinear.
:::

<1>3. The form is symmetric:
\[
\langle A,B\rangle
=
\langle B,A\rangle.
\]

::: {.proof}
By step <1>1,
\[
\langle A,B\rangle
=
\sum_{i,j}a_{ij}b_{ij}
=
\sum_{i,j}b_{ij}a_{ij}
=
\langle B,A\rangle.
\]
:::

<1>4. One has
\[
\langle A,A\rangle
=
\sum_{i,j=1}^n a_{ij}^2
\ge
0.
\]

::: {.proof}
Apply step <1>1 with
\[
B=A.
\]
The result is a sum of squares.
:::

<1>5. Equality
\[
\langle A,A\rangle=0
\]
holds if and only if
\[
A=0.
\]

::: {.proof}
By step <1>4,
\[
\langle A,A\rangle
=
\sum_{i,j}a_{ij}^2.
\]
This sum vanishes exactly when every entry $a_{ij}$ is zero.
:::

<1>6. Therefore
\[
\boxed{
\langle A,B\rangle
=
\operatorname{tr}(A^TB)
}
\]
defines an inner product on
\[
M_n(\mathbb R).
\]

::: {.proof}
Steps <1>2--<1>5 establish bilinearity, symmetry, and positive definiteness.
:::

<1>7. For
\[
n=2,
\]
define
\[
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
\]
\[
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
\]

::: {.proof}
These are the standard matrix units.
:::

<1>8. The four matrices in step <1>7 are orthonormal.

::: {.proof}
By step <1>1,
\[
\langle E_{ij},E_{kl}\rangle
=
\sum_{r,s}
(E_{ij})_{rs}
(E_{kl})_{rs}.
\]
Each matrix unit has exactly one entry equal to $1$ and all others equal to $0$.
Thus the inner product is
\[
1
\]
when
\[
(i,j)=(k,l)
\]
and
\[
0
\]
otherwise.
:::

<1>9. The four matrices form a basis of
\[
M_2(\mathbb R).
\]

::: {.proof}
Every matrix
\[
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
\]
has the unique expansion
\[
aE_{11}
+
bE_{12}
+
cE_{21}
+
dE_{22}.
\]
Thus the four matrix units span and are linearly independent.
:::

<1>10. Hence an orthonormal basis for
\[
M_2(\mathbb R)
\]
is
\[
\boxed{
\{E_{11},E_{12},E_{21},E_{22}\}.
}
\]

::: {.proof}
Combine steps <1>8--<1>9.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>6 proves the inner-product assertion, and step <1>10 gives the requested orthonormal basis for $n=2$.
:::
:::
