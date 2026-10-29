---
schema: qual/card@1
id: P-UCLAB09S-05
kind: problem
title: Matrix exponential $e^{At}$ of a $3\times3$ matrix
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
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Spring 2009.
---

::: {.problem}
Compute $e^{At}$ for
$$
A=\begin{pmatrix}2&1&5\\0&1&3\\1&0&1\end{pmatrix}.
$$
Recall that $e^{At}$ is characterized by
$$
\frac{dx}{dt}(t)=Ax(t)
\quad\Longleftrightarrow\quad
x(t)=e^{At}x(0).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The characteristic polynomial of $A$ is
$$
\boxed{\chi_A(\lambda)=\lambda^2(\lambda-4)}.
$$


::: pf-proof

Compute
$$
\begin{aligned}
\det(A-\lambda I)
&=
\det
\begin{pmatrix}
2-\lambda&1&5\\
0&1-\lambda&3\\
1&0&1-\lambda
\end{pmatrix}\\
&=
(2-\lambda)(1-\lambda)^2
+3
-5(1-\lambda)\\
&=
\lambda^2(4-\lambda).
\end{aligned}
$$
Therefore
$$
\det(\lambda I-A)
=
\lambda^2(\lambda-4).
$$

:::

:::

::: {.pf-step #s1-2}

The eigenspace for eigenvalue $0$ is one-dimensional.


::: pf-proof

Solving
$$
Av=0
$$
for
$$
v=(x,y,z)^T
$$
gives
$$
x+z=0,
\qquad
y+3z=0.
$$
Thus
$$
x=-z,
\qquad
y=-3z,
$$
and the first row equation is then automatically satisfied.
Hence
$$
\ker A
=
\operatorname{span}
\left\{
\begin{pmatrix}
-1\\-3\\1
\end{pmatrix}
\right\},
$$
which has dimension $1$.

:::

:::

::: {.pf-step #s1-3}

The minimal polynomial of $A$ is
$$
\boxed{\mu_A(\lambda)=\lambda^2(\lambda-4)}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, the characteristic polynomial is
$$
\lambda^2(\lambda-4).
$$
The minimal polynomial divides the characteristic polynomial and contains each distinct eigenvalue as a root.
Thus the only possibilities are
$$
\lambda(\lambda-4)
\quad\text{or}\quad
\lambda^2(\lambda-4).
$$
If the first polynomial were the minimal polynomial, it would have distinct roots, and $A$ would be diagonalizable.
But step [](#s1-2){.pf-ref} shows that eigenvalue $0$ has algebraic multiplicity $2$ and geometric multiplicity $1$, so $A$ is not diagonalizable.
Therefore the repeated factor $\lambda^2$ is necessary.

:::

:::

::: pf-step

For every $t$, there are unique scalars $b(t),c(t)$ such that
$$
e^{At}
=
I+b(t)A+c(t)A^2.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
A^2(A-4I)=0,
$$
so every power $A^k$ with $k\ge3$ reduces to a linear combination of
$$
I,\ A,\ A^2.
$$
Therefore the convergent exponential series
$$
e^{At}
=
\sum_{k=0}^\infty\frac{t^kA^k}{k!}
$$
reduces to a polynomial in $A$ of degree at most $2$.

To determine that polynomial, because the minimal polynomial has a double root at $0$ and a simple root at $4$, the scalar polynomial
$$
p_t(\lambda)=1+b(t)\lambda+c(t)\lambda^2
$$
must satisfy
$$
p_t(0)=e^{0t}=1,
\qquad
p_t'(0)=t,
\qquad
p_t(4)=e^{4t}.
$$
These three interpolation conditions determine $b(t),c(t)$ uniquely.

:::

:::

::: pf-step

One has
$$
b(t)=t
$$
and
$$
\boxed{
c(t)
=
\frac{e^{4t}-1-4t}{16}
}.
$$


::: pf-proof

From
$$
p_t'(0)=t,
$$
one gets
$$
b(t)=t.
$$
Then
$$
p_t(4)
=
1+4t+16c(t)
=
e^{4t},
$$
so
$$
c(t)
=
\frac{e^{4t}-1-4t}{16}.
$$

:::

:::

::: {.pf-step #s1-6}

The square of $A$ is
$$
A^2
=
\begin{pmatrix}
9&3&18\\
3&1&6\\
3&1&6
\end{pmatrix}.
$$


::: pf-proof

Direct multiplication of
$$
A
=
\begin{pmatrix}
2&1&5\\
0&1&3\\
1&0&1
\end{pmatrix}
$$
by itself gives the displayed matrix.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
e^{At}
=
I+tA
+
\frac{e^{4t}-1-4t}{16}A^2
}.
$$


::: pf-proof

Set
$$
E(t)
=
I+tA+c(t)A^2,
\qquad
c(t)
=
\frac{e^{4t}-1-4t}{16}.
$$
By step [](#s1-3){.pf-ref},
$$
A^2(A-4I)=0,
$$
so
$$
A^3=4A^2.
$$
Also
$$
c'(t)
=
\frac{e^{4t}-1}{4}.
$$
Therefore
$$
\begin{aligned}
E'(t)
&=
A+c'(t)A^2\\
&=
A+\frac{e^{4t}-1}{4}A^2,
\end{aligned}
$$
while
$$
\begin{aligned}
AE(t)
&=
A+tA^2+c(t)A^3\\
&=
A+\bigl(t+4c(t)\bigr)A^2\\
&=
A+\frac{e^{4t}-1}{4}A^2.
\end{aligned}
$$
Thus
$$
E'(t)=AE(t).
$$
Moreover,
$$
E(0)=I.
$$
By uniqueness for the matrix initial-value problem
$$
X'(t)=AX(t),
\qquad
X(0)=I,
$$
one has
$$
E(t)=e^{At}.
$$
Using step [](#s1-6){.pf-ref} gives a fully explicit matrix.

:::

:::

::: {.pf-step #s1-8}

Explicitly, with
$$
c=\frac{e^{4t}-1-4t}{16},
$$
one has
$$
\boxed{
e^{At}
=
\begin{pmatrix}
1+2t+9c&t+3c&5t+18c\\
3c&1+t+c&3t+6c\\
t+3c&c&1+t+6c
\end{pmatrix}.
}
$$


::: pf-proof

Substitute the matrices $A$ and $A^2$ into the formula in step [](#s1-7){.pf-ref} and add the entries.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the requested matrix exponential.

:::

:::

:::
