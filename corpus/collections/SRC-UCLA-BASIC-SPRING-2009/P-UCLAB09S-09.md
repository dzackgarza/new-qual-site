---
schema: qual/card@1
id: P-UCLAB09S-09
kind: problem
title: Unique reflection interchanging two unit vectors
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
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Spring 2009.
---

::: {.problem}
Call a real symmetric $n\times n$ matrix $A$ a reflection if
$$
A^2=I,
\qquad
\operatorname{rank}(A-I)=1.
$$
Given distinct unit vectors $x,y\in\RR^n$, prove that there is a reflection satisfying
$$
Ax=y,
\qquad
Ay=x,
$$
and that this reflection is unique.
:::

::: {.solution}

Let
$$
d=\norm{x-y}_2.
$$
Since $x\ne y$,
$$
d>0.
$$
Define the unit vector
$$
u=\frac{x-y}{d}.
$$

::: pf

::: {.pf-step #s1-1}

Define
$$
\boxed{
A=I-2uu^T.
}
$$
Then $A$ is real symmetric.


::: pf-proof

Since
$$
(uu^T)^T=uu^T,
$$
one has
$$
A^T
=
I-2(uu^T)^T
=
I-2uu^T
=A.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
A^2=I.
$$


::: pf-proof

Because
$$
\norm{u}_2=1,
$$
one has
$$
u^Tu=1.
$$
Thus
$$
(uu^T)^2
=
u(u^Tu)u^T
=
uu^T.
$$
Therefore
$$
\begin{aligned}
A^2
&=
(I-2uu^T)^2\\
&=
I-4uu^T+4(uu^T)^2\\
&=
I.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

One has
$$
\operatorname{rank}(A-I)=1.
$$


::: pf-proof

Since
$$
A-I=-2uu^T,
$$
its image is
$$
\operatorname{span}\{u\}.
$$
Because
$$
u\ne0,
$$
this image is one-dimensional.
Hence
$$
\operatorname{rank}(A-I)=1.
$$
Thus $A$ is a reflection in the sense of the problem.

:::

:::

::: {.pf-step #s1-4}

One has
$$
2u(u^Tx)=x-y.
$$


::: pf-proof

Let
$$
c=x^Ty.
$$
Since
$$
\norm{x}=\norm{y}=1,
$$
one has
$$
d^2
=
\norm{x-y}^2
=
2-2c
=
2(1-c).
$$
Also
$$
u^Tx
=
\frac{(x-y)^Tx}{d}
=
\frac{1-c}{d}.
$$
Therefore
$$
\begin{aligned}
2u(u^Tx)
&=
2\frac{x-y}{d}
\frac{1-c}{d}\\
&=
\frac{2(1-c)}{d^2}(x-y)\\
&=
x-y.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

The matrix $A$ satisfies
$$
\boxed{Ax=y}.
$$


::: pf-proof

Using step [](#s1-4){.pf-ref},
$$
\begin{aligned}
Ax
&=
x-2u(u^Tx)\\
&=
x-(x-y)\\
&=
y.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-6}

The matrix $A$ also satisfies
$$
\boxed{Ay=x}.
$$


::: pf-proof

Since
$$
u=\frac{x-y}{d},
$$
one has
$$
u^Ty
=
\frac{x^Ty-\norm{y}^2}{d}
=
\frac{c-1}{d}
=
-\frac{1-c}{d}.
$$
Hence, as in step [](#s1-4){.pf-ref},
$$
2u(u^Ty)
=
-(x-y).
$$
Therefore
$$
\begin{aligned}
Ay
&=
y-2u(u^Ty)\\
&=
y+(x-y)\\
&=
x.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-7}

Thus a reflection interchanging $x$ and $y$ exists.


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} verify that the matrix $A$ is a reflection, and steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} verify
$$
Ax=y,
\qquad
Ay=x.
$$

:::

:::

::: {.pf-step #s1-8}

Let $B$ be any reflection satisfying
$$
Bx=y,
\qquad
By=x.
$$
Then
$$
B(x-y)=-(x-y).
$$


::: pf-proof

By linearity,
$$
\begin{aligned}
B(x-y)
&=
Bx-By\\
&=
y-x\\
&=
-(x-y).
\end{aligned}
$$
Thus $x-y$ is a $(-1)$-eigenvector of $B$.

:::

:::

::: {.pf-step #s1-9}

For any reflection $B$, the $(-1)$-eigenspace is one-dimensional.


::: pf-proof

Since
$$
B^2=I,
$$
the minimal polynomial of $B$ divides
$$
(t-1)(t+1),
$$
which has distinct roots.
Thus
$$
\RR^n
=
E_1(B)\oplus E_{-1}(B).
$$
On $E_1(B)$,
$$
B-I=0,
$$
while on $E_{-1}(B)$,
$$
B-I=-2I.
$$
Therefore
$$
\operatorname{rank}(B-I)
=
\dim E_{-1}(B).
$$
By the definition of reflection,
$$
\operatorname{rank}(B-I)=1.
$$
Hence
$$
\dim E_{-1}(B)=1.
$$

:::

:::

::: {.pf-step #s1-10}

For such a $B$,
$$
E_{-1}(B)=\operatorname{span}\{u\}.
$$


::: pf-proof

By step [](#s1-8){.pf-ref},
$$
x-y
$$
is a nonzero $(-1)$-eigenvector.
Thus
$$
u
=
\frac{x-y}{\norm{x-y}}
$$
also lies in
$$
E_{-1}(B).
$$
By step [](#s1-9){.pf-ref}, this eigenspace is one-dimensional, so it equals
$$
\operatorname{span}\{u\}.
$$

:::

:::

::: {.pf-step #s1-11}

The $1$-eigenspace of $B$ is
$$
u^\perp.
$$


::: pf-proof

The matrix $B$ is symmetric.
Eigenvectors of a real symmetric matrix corresponding to distinct eigenvalues are orthogonal.
Thus
$$
E_1(B)
\subseteq
E_{-1}(B)^\perp
=
u^\perp.
$$
By step [](#s1-9){.pf-ref},
$$
\dim E_{-1}(B)=1,
$$
so
$$
\dim E_1(B)=n-1.
$$
The space
$$
u^\perp
$$
also has dimension $n-1$.
Hence
$$
E_1(B)=u^\perp.
$$

:::

:::

::: {.pf-step #s1-12}

The reflection $B$ must equal
$$
I-2uu^T.
$$


::: pf-proof

Every vector $z\in\RR^n$ decomposes uniquely as
$$
z=z_\perp+(u^Tz)u,
\qquad
z_\perp\in u^\perp.
$$
By step [](#s1-11){.pf-ref},
$$
Bz_\perp=z_\perp,
$$
while by step [](#s1-10){.pf-ref},
$$
Bu=-u.
$$
Therefore
$$
\begin{aligned}
Bz
&=
z_\perp-(u^Tz)u\\
&=
z-2(u^Tz)u\\
&=
(I-2uu^T)z.
\end{aligned}
$$
Thus
$$
B=I-2uu^T.
$$

:::

:::

::: {.pf-step #s1-13}

Therefore the reflection is unique.


::: pf-proof

Step [](#s1-7){.pf-ref} constructs the reflection
$$
A=I-2uu^T,
$$
and step [](#s1-12){.pf-ref} shows that every reflection satisfying the two interchange conditions must equal this matrix.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-7){.pf-ref} prove existence, and steps [](#s1-8){.pf-ref} through [](#s1-13){.pf-ref} prove uniqueness.

:::

:::

:::
