---
schema: qual/card@1
id: P-UCLAB10S-06
kind: problem
title: Jordan powers and a second-order recurrence
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
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Spring 2010.
---

::: {.problem}
Problem 6. Let
\[
A=\begin{pmatrix}4&-4\\1&0\end{pmatrix}.
\]

(i) Find the Jordan form $J$ of $A$ and a matrix $P$ such that $P^{-1}AP=J$.

(ii) Compute $A^{100}$ and $J^{100}$.

(iii) Find a formula for $a_n$ when
\[
a_{n+1}=4a_n-4a_{n-1},\qquad a_0=a,\quad a_1=b.
\]
:::

::: pf

::: pf-step

The characteristic polynomial of $A$ is
\[
\chi_A(\lambda)
=
(\lambda-2)^2.
\]


::: pf-proof

Compute
\[
\begin{aligned}
\chi_A(\lambda)
&=
\det
\begin{pmatrix}
\lambda-4&4\\
-1&\lambda
\end{pmatrix}\\
&=
\lambda(\lambda-4)+4\\
&=
\lambda^2-4\lambda+4\\
&=
(\lambda-2)^2.
\end{aligned}
\]

:::

:::

::: pf-step

The eigenspace for eigenvalue $2$ is
\[
\ker(A-2I)
=
\operatorname{span}
\left\{
\begin{pmatrix}
2\\1
\end{pmatrix}
\right\}.
\]


::: pf-proof

One has
\[
A-2I
=
\begin{pmatrix}
2&-4\\
1&-2
\end{pmatrix}.
\]
Solving
\[
(A-2I)
\begin{pmatrix}
x\\y
\end{pmatrix}
=0
\]
gives
\[
x=2y.
\]
Thus the eigenspace is the stated line.

:::

:::

::: pf-step

Let
\[
v=
\begin{pmatrix}
2\\1
\end{pmatrix},
\qquad
w=
\begin{pmatrix}
1\\0
\end{pmatrix}.
\]
Then
\[
(A-2I)w=v.
\]


::: pf-proof

Direct multiplication gives
\[
(A-2I)w
=
\begin{pmatrix}
2&-4\\
1&-2
\end{pmatrix}
\begin{pmatrix}
1\\0
\end{pmatrix}
=
\begin{pmatrix}
2\\1
\end{pmatrix}
=v.
\]

:::

:::

::: pf-step

With
\[
P=
\begin{pmatrix}
2&1\\
1&0
\end{pmatrix},
\]
one has
\[
\boxed{
P^{-1}
=
\begin{pmatrix}
0&1\\
1&-2
\end{pmatrix}
}
\]
and
\[
\boxed{
P^{-1}AP
=
J
=
\begin{pmatrix}
2&1\\
0&2
\end{pmatrix}.
}
\]


::: pf-proof

The columns of $P$ are $v,w$.
Since
\[
\det P=-1,
\]
the displayed inverse follows from the $2\times2$ inverse formula.

Also,
\[
Av=2v
\]
and step <1>3 gives
\[
Aw
=
2w+v.
\]
Thus the coordinate columns of $A$ in the basis $(v,w)$ are
\[
\begin{pmatrix}
2\\0
\end{pmatrix}
\quad\text{and}\quad
\begin{pmatrix}
1\\2
\end{pmatrix},
\]
which gives the displayed Jordan matrix.
This proves part (i).

:::

:::

::: pf-step

For every positive integer $m$,
\[
\boxed{
J^m
=
\begin{pmatrix}
2^m&m2^{m-1}\\
0&2^m
\end{pmatrix}.
}
\]


::: pf-proof

Write
\[
J=2I+N,
\qquad
N=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
\]
Since
\[
N^2=0,
\]
the binomial theorem gives
\[
J^m
=(2I+N)^m
=
2^mI
+
m2^{m-1}N.
\]
This is the displayed matrix.

:::

:::

::: pf-step

In particular,
\[
\boxed{
J^{100}
=
\begin{pmatrix}
2^{100}&100\,2^{99}\\
0&2^{100}
\end{pmatrix}.
}
\]


::: pf-proof

Set
\[
m=100
\]
in step <1>5.

:::

:::

::: pf-step

For every positive integer $m$,
\[
A^m
=
P J^mP^{-1}
=
2^{m-1}
\begin{pmatrix}
2m+2&-4m\\
m&2-2m
\end{pmatrix}.
\]


::: pf-proof

Since
\[
A=PJP^{-1},
\]
one has
\[
A^m=PJ^mP^{-1}.
\]
Using step <1>5, put
\[
d=2^m,
\qquad
c=m2^{m-1}.
\]
Then
\[
\begin{aligned}
PJ^mP^{-1}
&=
\begin{pmatrix}
2&1\\
1&0
\end{pmatrix}
\begin{pmatrix}
d&c\\
0&d
\end{pmatrix}
\begin{pmatrix}
0&1\\
1&-2
\end{pmatrix}\\
&=
\begin{pmatrix}
d+2c&-4c\\
c&d-2c
\end{pmatrix}.
\end{aligned}
\]
Substitute the values of $c,d$ and factor out $2^{m-1}$.

:::

:::

::: pf-step

Therefore
\[
\boxed{
A^{100}
=
2^{99}
\begin{pmatrix}
202&-400\\
100&-198
\end{pmatrix}.
}
\]


::: pf-proof

Set
\[
m=100
\]
in step <1>7.
Together with step <1>6, this completes part (ii).

:::

:::

::: pf-step

The characteristic equation of the recurrence
\[
a_{n+1}=4a_n-4a_{n-1}
\]
is
\[
(r-2)^2=0.
\]


::: pf-proof

Substitute a trial solution
\[
a_n=r^n.
\]
Then
\[
r^{n+1}
=
4r^n-4r^{n-1},
\]
so for nonzero $r$,
\[
r^2-4r+4=0.
\]
This factors as
\[
(r-2)^2=0.
\]

:::

:::

::: pf-step

Every solution of the recurrence has the form
\[
a_n=(C+Dn)2^n.
\]


::: pf-proof

For a second-order linear recurrence with repeated characteristic root $r=2$, the two linearly independent solutions are
\[
2^n
\quad\text{and}\quad
n2^n.
\]
Hence the general solution is their linear combination.

Direct verification is also immediate:
\[
(C+D(n+1))2^{n+1}
=
4(C+Dn)2^n
-
4(C+D(n-1))2^{n-1}.
\]

:::

:::

::: pf-step

The initial conditions give
\[
C=a
\qquad\text{and}\qquad
D=\frac b2-a.
\]


::: pf-proof

At
\[
n=0,
\]
one has
\[
a_0=C=a.
\]
At
\[
n=1,
\]
one has
\[
a_1
=
2(C+D)
=b.
\]
Thus
\[
D=\frac b2-C
=
\frac b2-a.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
a_n
=
\left(
a+n\left(\frac b2-a\right)
\right)2^n.
}
\]


::: pf-proof

Substitute the constants from step <1>11 into the formula from step <1>10.
This proves part (iii).

:::

:::

::: pf-qed

Step <1>4 proves part (i), steps <1>6--<1>8 prove part (ii), and step <1>12 proves part (iii).

:::

:::
