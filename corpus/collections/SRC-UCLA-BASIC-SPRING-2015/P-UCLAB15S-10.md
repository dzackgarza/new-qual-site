---
schema: qual/card@1
id: P-UCLAB15S-10
kind: problem
title: Determinant identity for a block of an inverse matrix
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Let
\[
M=\begin{pmatrix}A&B\\C&D\end{pmatrix},
\qquad
M^{-1}=\begin{pmatrix}P&Q\\R&S\end{pmatrix},
\]
where $A,\ldots,S$ are $k\times k$ matrices.
Show that
\[
\det(M)\det(S)=\det(A).
\]
:::

::: {.solution}
<1>1. First suppose that $A$ is invertible and define the Schur complement
\[
E=D-CA^{-1}B.
\]

::: {.proof}
This definition is available under the temporary assumption that $A$ is invertible.
:::

<1>2. One has the block factorization
\[
\boxed{
\begin{pmatrix}
I&0\\
-CA^{-1}&I
\end{pmatrix}
\begin{pmatrix}
A&B\\
C&D
\end{pmatrix}
=
\begin{pmatrix}
A&B\\
0&E
\end{pmatrix}.
}
\]

::: {.proof}
Multiply the two block matrices.
The lower-left block is
\[
-CA^{-1}A+C
=
-C+C
=0,
\]
and the lower-right block is
\[
-CA^{-1}B+D
=
E.
\]
:::

<1>3. Hence
\[
\boxed{
\det M
=
\det A\,\det E.
}
\]

::: {.proof}
The left factor in step <1>2 is block lower triangular with identity matrices on its diagonal, so its determinant is $1$.
The right side is block upper triangular, so its determinant is
\[
\det A\,\det E.
\]
Therefore the same is true of $\det M$.
:::

<1>4. Since $M$ is invertible, the Schur complement $E$ is invertible.

::: {.proof}
By step <1>3,
\[
\det M
=
\det A\,\det E.
\]
Both $\det M$ and $\det A$ are nonzero under the present assumptions.
Hence
\[
\det E\ne0.
\]
:::

<1>5. Under the assumption that $A$ is invertible, the lower-right block of $M^{-1}$ is
\[
\boxed{S=E^{-1}}.
\]

::: {.proof}
Use the block factorization
\[
M
=
\begin{pmatrix}
I&0\\
CA^{-1}&I
\end{pmatrix}
\begin{pmatrix}
A&B\\
0&E
\end{pmatrix}.
\]
The inverse of the second factor is
\[
\begin{pmatrix}
A^{-1}&-A^{-1}BE^{-1}\\
0&E^{-1}
\end{pmatrix}.
\]
The inverse of the first factor is
\[
\begin{pmatrix}
I&0\\
-CA^{-1}&I
\end{pmatrix}.
\]
Multiplying these inverses in reverse order shows that the lower-right block of $M^{-1}$ is exactly
\[
E^{-1}.
\]
:::

<1>6. Therefore, when $A$ is invertible,
\[
\boxed{
\det(M)\det(S)=\det(A).
}
\]

::: {.proof}
By steps <1>3 and <1>5,
\[
\begin{aligned}
\det(M)\det(S)
&=
\det(A)\det(E)\det(E^{-1})\\
&=
\det(A).
\end{aligned}
\]
:::

<1>7. Now drop the assumption that $A$ is invertible.
For real or complex $t$, define
\[
M_t
=
\begin{pmatrix}
A+tI&B\\
C&D
\end{pmatrix}.
\]
Then there exist arbitrarily small nonzero values of $t$ for which both
\[
A+tI
\]
and
\[
M_t
\]
are invertible.

::: {.proof}
The determinant
\[
\det(A+tI)
\]
is a polynomial in $t$ that is not identically zero, because its leading term is $t^k$.
Hence it has only finitely many zeros.

Likewise,
\[
\det(M_t)
\]
is a polynomial in $t$.
At
\[
t=0,
\]
it equals
\[
\det M\ne0,
\]
so it is not identically zero.
Thus it also has only finitely many zeros.

Therefore one may choose a sequence
\[
t_j\to0
\]
avoiding the finitely many zeros of both polynomials.
:::

<1>8. For such a sequence $t_j$, write
\[
M_{t_j}^{-1}
=
\begin{pmatrix}
P_j&Q_j\\
R_j&S_j
\end{pmatrix}.
\]
Then
\[
\det(M_{t_j})\det(S_j)
=
\det(A+t_jI).
\]

::: {.proof}
For each $j$, the upper-left block
\[
A+t_jI
\]
is invertible, and $M_{t_j}$ is invertible.
Therefore step <1>6 applies to $M_{t_j}$.
:::

<1>9. One has
\[
M_{t_j}^{-1}\to M^{-1}.
\]

::: {.proof}
Since
\[
M_{t_j}\to M
\]
and $M$ is invertible, matrix inversion is continuous on the open set of invertible matrices.
Therefore
\[
M_{t_j}^{-1}\to M^{-1}.
\]
:::

<1>10. Consequently,
\[
S_j\to S.
\]

::: {.proof}
The lower-right $k\times k$ block is obtained by selecting fixed matrix entries.
Entrywise convergence of the full inverse matrices in step <1>9 therefore gives entrywise convergence of the corresponding blocks.
:::

<1>11. Taking limits in step <1>8 gives
\[
\boxed{
\det(M)\det(S)=\det(A).
}
\]

::: {.proof}
The determinant is continuous in the matrix entries.
Thus
\[
\det(M_{t_j})\to\det(M),
\]
\[
\det(S_j)\to\det(S),
\]
and
\[
\det(A+t_jI)\to\det(A).
\]
Take the limit
\[
j\to\infty
\]
in the identity from step <1>8.
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>11 proves the identity without any invertibility assumption on $A$.
:::
:::
