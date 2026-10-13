---
schema: qual/card@1
id: P-UCLAB17F-02
kind: problem
title: Characteristic polynomials of AB and BA
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2017, `assets/attachments/basic-17F.pdf`.
---

::: {.problem}
Let $A,B$ be $n\times n$ matrices.

(a) Show that $AB$ and $BA$ have the same characteristic polynomial if $A$ is invertible.

(b) Is the result true without assuming $A$ invertible? Prove your claim.
:::

::: {.solution}
<1>1. If $A$ is invertible, then
\[
AB
\]
and
\[
BA
\]
are similar.

::: {.proof}
One has
\[
A^{-1}(AB)A
=
BA.
\]
Thus $BA$ is obtained from $AB$ by conjugation with the invertible matrix $A$.
:::

<1>2. Therefore, if $A$ is invertible,
\[
\boxed{\chi_{AB}(t)=\chi_{BA}(t)}.
\]

::: {.proof}
Similar matrices have the same characteristic polynomial.
Apply step <1>1.
:::

<1>3. For arbitrary square matrices $X,Y$ of the same size,
\[
\boxed{\det(I+XY)=\det(I+YX)}.
\]

::: {.proof}
Consider the block matrix
\[
M=
\begin{pmatrix}
I&X\\
-Y&I
\end{pmatrix}.
\]
Multiply on the left by
\[
\begin{pmatrix}
I&0\\
Y&I
\end{pmatrix},
\]
whose determinant is $1$.
This gives
\[
\begin{pmatrix}
I&X\\
0&I+YX
\end{pmatrix}.
\]
Hence
\[
\det M=\det(I+YX).
\]

On the other hand, multiply $M$ on the left by
\[
\begin{pmatrix}
I&-X\\
0&I
\end{pmatrix},
\]
which also has determinant $1$.
The result is
\[
\begin{pmatrix}
I+XY&0\\
-Y&I
\end{pmatrix}.
\]
Therefore
\[
\det M=\det(I+XY).
\]
Comparing the two formulas proves the identity.
:::

<1>4. For every nonzero scalar $t$,
\[
\det(tI-AB)
=
\det(tI-BA).
\]

::: {.proof}
For $t\ne0$,
\[
\begin{aligned}
\det(tI-AB)
&=
t^n
\det\left(
I-\frac1tAB
\right)\\
&=
t^n
\det\left(
I-\frac1tBA
\right)\\
&=
\det(tI-BA),
\end{aligned}
\]
where step <1>3 is applied with
\[
X=-\frac1tA,
\qquad
Y=B.
\]
:::

<1>5. The equality in step <1>4 holds for all $t$, including $t=0$.

::: {.proof}
Both functions
\[
t\longmapsto\det(tI-AB)
\]
and
\[
t\longmapsto\det(tI-BA)
\]
are polynomials in $t$.
By step <1>4, they agree for every nonzero complex number $t$.
Two polynomials agreeing at infinitely many points are identical.
Thus they agree for all $t$.
:::

<1>6. Hence the answer to part (b) is yes:
\[
\boxed{\chi_{AB}(t)=\chi_{BA}(t)}
\]
for all square matrices $A,B$ of the same size, without any invertibility hypothesis.

::: {.proof}
Step <1>5 is exactly the equality of the two characteristic polynomials.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>2 proves part (a), and steps <1>3--<1>6 prove the stronger statement required in part (b).
:::
:::
