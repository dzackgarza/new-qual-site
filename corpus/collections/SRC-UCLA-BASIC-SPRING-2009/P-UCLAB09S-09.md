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
Problem 9. Call a real symmetric $n\times n$ matrix $A$ a reflection if
\[
A^2=I,
\qquad
\operatorname{rank}(A-I)=1.
\]
Given distinct unit vectors $x,y\in\mathbb R^n$, prove that there is a reflection satisfying
\[
Ax=y,
\qquad
Ay=x,
\]
and that this reflection is unique.
:::

::: {.solution}
Let
\[
d=\|x-y\|_2.
\]
Since $x\ne y$,
\[
d>0.
\]
Define the unit vector
\[
u=\frac{x-y}{d}.
\]

<1>1. Define
\[
\boxed{
A=I-2uu^T.
}
\]
Then $A$ is real symmetric.

::: {.proof}
Since
\[
(uu^T)^T=uu^T,
\]
one has
\[
A^T
=
I-2(uu^T)^T
=
I-2uu^T
=A.
\]
:::

<1>2. One has
\[
A^2=I.
\]

::: {.proof}
Because
\[
\|u\|_2=1,
\]
one has
\[
u^Tu=1.
\]
Thus
\[
(uu^T)^2
=
u(u^Tu)u^T
=
uu^T.
\]
Therefore
\[
\begin{aligned}
A^2
&=
(I-2uu^T)^2\\
&=
I-4uu^T+4(uu^T)^2\\
&=
I.
\end{aligned}
\]
:::

<1>3. One has
\[
\operatorname{rank}(A-I)=1.
\]

::: {.proof}
Since
\[
A-I=-2uu^T,
\]
its image is
\[
\operatorname{span}\{u\}.
\]
Because
\[
u\ne0,
\]
this image is one-dimensional.
Hence
\[
\operatorname{rank}(A-I)=1.
\]
Thus $A$ is a reflection in the sense of the problem.
:::

<1>4. One has
\[
2u(u^Tx)=x-y.
\]

::: {.proof}
Let
\[
c=x^Ty.
\]
Since
\[
\|x\|=\|y\|=1,
\]
one has
\[
d^2
=
\|x-y\|^2
=
2-2c
=
2(1-c).
\]
Also
\[
u^Tx
=
\frac{(x-y)^Tx}{d}
=
\frac{1-c}{d}.
\]
Therefore
\[
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
\]
:::

<1>5. The matrix $A$ satisfies
\[
\boxed{Ax=y}.
\]

::: {.proof}
Using step <1>4,
\[
\begin{aligned}
Ax
&=
x-2u(u^Tx)\\
&=
x-(x-y)\\
&=
y.
\end{aligned}
\]
:::

<1>6. The matrix $A$ also satisfies
\[
\boxed{Ay=x}.
\]

::: {.proof}
Since
\[
u=\frac{x-y}{d},
\]
one has
\[
u^Ty
=
\frac{x^Ty-\|y\|^2}{d}
=
\frac{c-1}{d}
=
-\frac{1-c}{d}.
\]
Hence, as in step <1>4,
\[
2u(u^Ty)
=
-(x-y).
\]
Therefore
\[
\begin{aligned}
Ay
&=
y-2u(u^Ty)\\
&=
y+(x-y)\\
&=
x.
\end{aligned}
\]
:::

<1>7. Thus a reflection interchanging $x$ and $y$ exists.

::: {.proof}
Steps <1>1--<1>3 verify that the matrix $A$ is a reflection, and steps <1>5--<1>6 verify
\[
Ax=y,
\qquad
Ay=x.
\]
:::

<1>8. Let $B$ be any reflection satisfying
\[
Bx=y,
\qquad
By=x.
\]
Then
\[
B(x-y)=-(x-y).
\]

::: {.proof}
By linearity,
\[
\begin{aligned}
B(x-y)
&=
Bx-By\\
&=
y-x\\
&=
-(x-y).
\end{aligned}
\]
Thus $x-y$ is a $(-1)$-eigenvector of $B$.
:::

<1>9. For any reflection $B$, the $(-1)$-eigenspace is one-dimensional.

::: {.proof}
Since
\[
B^2=I,
\]
the minimal polynomial of $B$ divides
\[
(t-1)(t+1),
\]
which has distinct roots.
Thus
\[
\mathbb R^n
=
E_1(B)\oplus E_{-1}(B).
\]
On $E_1(B)$,
\[
B-I=0,
\]
while on $E_{-1}(B)$,
\[
B-I=-2I.
\]
Therefore
\[
\operatorname{rank}(B-I)
=
\dim E_{-1}(B).
\]
By the definition of reflection,
\[
\operatorname{rank}(B-I)=1.
\]
Hence
\[
\dim E_{-1}(B)=1.
\]
:::

<1>10. For such a $B$,
\[
E_{-1}(B)=\operatorname{span}\{u\}.
\]

::: {.proof}
By step <1>8,
\[
x-y
\]
is a nonzero $(-1)$-eigenvector.
Thus
\[
u
=
\frac{x-y}{\|x-y\|}
\]
also lies in
\[
E_{-1}(B).
\]
By step <1>9, this eigenspace is one-dimensional, so it equals
\[
\operatorname{span}\{u\}.
\]
:::

<1>11. The $1$-eigenspace of $B$ is
\[
u^\perp.
\]

::: {.proof}
The matrix $B$ is symmetric.
Eigenvectors of a real symmetric matrix corresponding to distinct eigenvalues are orthogonal.
Thus
\[
E_1(B)
\subseteq
E_{-1}(B)^\perp
=
u^\perp.
\]
By step <1>9,
\[
\dim E_{-1}(B)=1,
\]
so
\[
\dim E_1(B)=n-1.
\]
The space
\[
u^\perp
\]
also has dimension $n-1$.
Hence
\[
E_1(B)=u^\perp.
\]
:::

<1>12. The reflection $B$ must equal
\[
I-2uu^T.
\]

::: {.proof}
Every vector $z\in\mathbb R^n$ decomposes uniquely as
\[
z=z_\perp+(u^Tz)u,
\qquad
z_\perp\in u^\perp.
\]
By step <1>11,
\[
Bz_\perp=z_\perp,
\]
while by step <1>10,
\[
Bu=-u.
\]
Therefore
\[
\begin{aligned}
Bz
&=
z_\perp-(u^Tz)u\\
&=
z-2(u^Tz)u\\
&=
(I-2uu^T)z.
\end{aligned}
\]
Thus
\[
B=I-2uu^T.
\]
:::

<1>13. Therefore the reflection is unique.

::: {.proof}
Step <1>7 constructs the reflection
\[
A=I-2uu^T,
\]
and step <1>12 shows that every reflection satisfying the two interchange conditions must equal this matrix.
:::

<1>14. Q.E.D.

::: {.proof}
Steps <1>1--<1>7 prove existence, and steps <1>8--<1>13 prove uniqueness.
:::
:::
