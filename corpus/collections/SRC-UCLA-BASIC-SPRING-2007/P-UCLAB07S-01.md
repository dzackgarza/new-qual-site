---
schema: qual/card@1
id: P-UCLAB07S-01
kind: problem
title: Normal equations for full-column-rank least squares
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
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Spring 2007.
---

::: {.problem}
Let $A$ be a real $m\times n$ matrix with $m>n$ and linearly independent columns, and let $b\in\RR^m$.
Show that the vector $x^*\in\RR^n$ minimizing
\[
g(x)=\|Ax-b\|_2^2
\]
is the solution of the normal equations
\[
A^TAx=A^Tb.
\]
:::

::: {.solution}

::: pf

::: pf-step

The matrix
\[
A^TA
\]
is positive definite.


::: pf-proof

Let
\[
v\in\RR^n
\]
be nonzero.
Since the columns of $A$ are linearly independent,
\[
Av\ne0.
\]
Therefore
\[
v^TA^TAv
=(Av)^T(Av)
=
\|Av\|_2^2
>
0.
\]
Thus $A^TA$ is positive definite.

:::

:::

::: {.pf-step #s1-2}

Consequently
\[
A^TA
\]
is invertible.


::: pf-proof

If
\[
A^TAv=0,
\]
then
\[
0
=
v^TA^TAv
=
\|Av\|_2^2,
\]
so
\[
Av=0.
\]
Column independence gives
\[
v=0.
\]
Hence the kernel of $A^TA$ is trivial.
Since it is a square matrix, it is invertible.

:::

:::

::: {.pf-step #s1-3}

The normal equations
\[
A^TAx=A^Tb
\]
have the unique solution
\[
\boxed{
x^*
=(A^TA)^{-1}A^Tb
}.
\]


::: pf-proof

This follows immediately from invertibility in step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Let
\[
r=b-Ax^*.
\]
Then
\[
A^Tr=0.
\]


::: pf-proof

The vector $x^*$ satisfies the normal equations, so
\[
A^TAx^*
=
A^Tb.
\]
Rearranging,
\[
A^T(b-Ax^*)
=0.
\]
This is
\[
A^Tr=0.
\]

:::

:::

::: {.pf-step #s1-5}

The residual $r$ is orthogonal to the column space of $A$.


::: pf-proof

Every vector in the column space has the form
\[
Ay
\]
for some
\[
y\in\RR^n.
\]
Then
\[
\begin{aligned}
r\cdot Ay
&=
r^TAy\\
&=
(A^Tr)^Ty\\
&=
0
\end{aligned}
\]
by step [](#s1-4){.pf-ref}.
Thus
\[
r\perp\operatorname{im}A.
\]

:::

:::

::: {.pf-step #s1-6}

For every
\[
x\in\RR^n,
\]
one has
\[
Ax-b
=
A(x-x^*)-r.
\]


::: pf-proof

By definition,
\[
r=b-Ax^*.
\]
Hence
\[
-r
=
Ax^*-b.
\]
Therefore
\[
A(x-x^*)-r
=
Ax-Ax^*+Ax^*-b
=
Ax-b.
\]

:::

:::

::: {.pf-step #s1-7}

The two vectors
\[
A(x-x^*)
\]
and
\[
r
\]
are orthogonal.


::: pf-proof

The first lies in
\[
\operatorname{im}A.
\]
The second is orthogonal to $\operatorname{im}A$ by step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

For every
\[
x\in\RR^n,
\]
one has
\[
\boxed{
g(x)
=
\|A(x-x^*)\|_2^2
+
\|r\|_2^2
}.
\]


::: pf-proof

By step [](#s1-6){.pf-ref},
\[
Ax-b
=
A(x-x^*)-r.
\]
By step [](#s1-7){.pf-ref}, the summands are orthogonal.
The Pythagorean theorem therefore gives
\[
\|Ax-b\|_2^2
=
\|A(x-x^*)\|_2^2
+
\|r\|_2^2.
\]
Since
\[
g(x)=\|Ax-b\|_2^2,
\]
the formula follows.

:::

:::

::: {.pf-step #s1-9}

The vector $x^*$ is the unique minimizer of $g$.


::: pf-proof

Step [](#s1-8){.pf-ref} shows
\[
g(x)
\ge
\|r\|_2^2
=
g(x^*)
\]
for every $x$.
Equality holds exactly when
\[
A(x-x^*)=0.
\]
Since the columns of $A$ are linearly independent,
\[
\ker A=\{0\}.
\]
Thus equality holds only when
\[
x=x^*.
\]
Hence $x^*$ is the unique minimizer.

:::

:::

::: {.pf-step #s1-10}

Therefore the vector minimizing
\[
\|Ax-b\|_2^2
\]
is exactly the unique solution of
\[
\boxed{A^TAx=A^Tb}.
\]


::: pf-proof

Step [](#s1-3){.pf-ref} gives the unique solution of the normal equations, and step [](#s1-9){.pf-ref} proves that this vector is exactly the unique minimizer.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required conclusion.

:::

:::

:::
