---
schema: qual/card@1
id: P-UCLAB08S-12
kind: problem
title: Spectral theorem from the maximum Rayleigh quotient
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
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Spring 2008.
---

::: {.problem}
Let $A=(a_{ij})$ be a real symmetric $n\times n$ matrix and let
\[
S=\{x\in\mathbb R^n:\|x\|=1\}.
\]
Choose $x\in S$ such that
\[
(Ax,x)=\sup_{y\in S}(Ay,y),
\]
which exists by compactness.

<1>1. Prove that $(x,y)=0$ implies $(Ax,y)=0$.
Hint: expand $(A(x+\varepsilon y),x+\varepsilon y)$.

<1>2. Use <1>1 to prove that $x$ is an eigenvector of $A$.

<1>3. Use induction to prove that $\mathbb R^n$ has an orthonormal basis of eigenvectors for $A$.
If you use <1>3 in proving an earlier part, give a proof of <1>3 that does not depend on those earlier parts.
:::

::: {.solution}
Let
\[
\lambda=(Ax,x),
\]
where
\[
x\in S
\]
maximizes the Rayleigh quotient
\[
y\longmapsto(Ay,y)
\]
on the unit sphere.

<1>1. Let
\[
y\in\mathbb R^n
\]
satisfy
\[
(x,y)=0.
\]
For every real $\varepsilon$, define
\[
u_\varepsilon
=
\frac{x+\varepsilon y}
{\|x+\varepsilon y\|}.
\]
Then
\[
u_\varepsilon\in S.
\]

::: {.proof}
Since
\[
\|x\|=1
\]
and
\[
(x,y)=0,
\]
one has
\[
\|x+\varepsilon y\|^2
=
1+\varepsilon^2\|y\|^2
>
0.
\]
Thus $u_\varepsilon$ is well-defined and has norm $1$.
:::

<1>2. Maximality of $x$ gives
\[
(Au_\varepsilon,u_\varepsilon)
\le
\lambda.
\]

::: {.proof}
By step <1>1,
\[
u_\varepsilon\in S.
\]
The point $x$ was chosen to maximize
\[
(Ay,y)
\]
over $y\in S$.
Hence the inequality holds.
:::

<1>3. One has
\[
(A(x+\varepsilon y),x+\varepsilon y)
=
\lambda
+
2\varepsilon(Ax,y)
+
\varepsilon^2(Ay,y).
\]

::: {.proof}
Expand bilinearly:
\[
\begin{aligned}
(A(x+\varepsilon y),x+\varepsilon y)
&=
(Ax,x)
+
\varepsilon(Ax,y)
+
\varepsilon(Ay,x)
+
\varepsilon^2(Ay,y).
\end{aligned}
\]
Since $A$ is symmetric,
\[
(Ay,x)=(y,Ax)=(Ax,y).
\]
Also
\[
(Ax,x)=\lambda.
\]
Substitute these identities.
:::

<1>4. For every real $\varepsilon$,
\[
2\varepsilon(Ax,y)
+
\varepsilon^2
\bigl(
(Ay,y)-\lambda\|y\|^2
\bigr)
\le
0.
\]

::: {.proof}
By step <1>2,
\[
\frac{
(A(x+\varepsilon y),x+\varepsilon y)
}{
\|x+\varepsilon y\|^2
}
\le
\lambda.
\]
By orthogonality,
\[
\|x+\varepsilon y\|^2
=
1+\varepsilon^2\|y\|^2.
\]
Insert the expansion from step <1>3 and multiply by the positive denominator:
\[
\lambda
+
2\varepsilon(Ax,y)
+
\varepsilon^2(Ay,y)
\le
\lambda
+
\lambda\varepsilon^2\|y\|^2.
\]
Rearranging gives the claimed inequality.
:::

<1>5. If
\[
(x,y)=0,
\]
then
\[
\boxed{(Ax,y)=0}.
\]

::: {.proof}
Suppose
\[
(Ax,y)\ne0.
\]
In step <1>4, the term linear in $\varepsilon$ would dominate the quadratic term for sufficiently small $\varepsilon$ having the same sign as $(Ax,y)$.
More explicitly, write
\[
a=(Ax,y)
\ne0
\]
and
\[
b=(Ay,y)-\lambda\|y\|^2.
\]
The inequality says
\[
2a\varepsilon+b\varepsilon^2\le0
\]
for every $\varepsilon$.
Choose $\varepsilon$ with the same sign as $a$ and sufficiently small that
\[
|b\varepsilon|<|a|.
\]
Then
\[
2a\varepsilon+b\varepsilon^2
\ge
2|a||\varepsilon|-|b|\varepsilon^2
>
|a||\varepsilon|
>
0,
\]
a contradiction.
Hence
\[
(Ax,y)=0.
\]
This proves part <1>1.
:::

<1>6. The vector $Ax$ belongs to
\[
\operatorname{span}\{x\}.
\]

::: {.proof}
Step <1>5 says
\[
(Ax,y)=0
\]
for every
\[
y\in x^\perp.
\]
Thus
\[
Ax\in(x^\perp)^\perp.
\]
In finite-dimensional Euclidean space,
\[
(x^\perp)^\perp
=
\operatorname{span}\{x\}.
\]
:::

<1>7. Therefore
\[
\boxed{Ax=\lambda x}.
\]

::: {.proof}
By step <1>6, there is a scalar $\mu$ such that
\[
Ax=\mu x.
\]
Taking inner products with $x$ and using
\[
\|x\|=1,
\]
gives
\[
\mu
=
(Ax,x)
=
\lambda.
\]
Hence
\[
Ax=\lambda x.
\]
This proves part <1>2.
:::

<1>8. If
\[
y\in x^\perp,
\]
then
\[
Ay\in x^\perp.
\]

::: {.proof}
By symmetry of $A$ and step <1>7,
\[
\begin{aligned}
(Ay,x)
&=
(y,Ax)\\
&=
(y,\lambda x)\\
&=
\lambda(y,x)\\
&=
0.
\end{aligned}
\]
Thus
\[
Ay\perp x.
\]
:::

<1>9. The restriction
\[
A|_{x^\perp}:x^\perp\to x^\perp
\]
is symmetric.

::: {.proof}
Step <1>8 shows the restriction is well-defined.
For
\[
y,z\in x^\perp,
\]
one has
\[
(Ay,z)
=(y,Az)
\]
because $A$ is symmetric on all of $\mathbb R^n$.
Hence the restriction is symmetric on $x^\perp$.
:::

<1>10. Every real symmetric $n\times n$ matrix has an orthonormal basis of eigenvectors.

::: {.proof}
Proceed by induction on $n$.

For
\[
n=1,
\]
the statement is immediate.

Assume the theorem holds in dimension $n-1$.
Choose the maximizing unit vector $x$ as in the problem.
By steps <1>1--<1>7, $x$ is an eigenvector.
The orthogonal complement
\[
x^\perp
\]
has dimension $n-1$.
By steps <1>8--<1>9, it is invariant under $A$ and the restriction of $A$ to it is symmetric.
The induction hypothesis therefore gives an orthonormal basis
\[
v_2,\ldots,v_n
\]
of $x^\perp$ consisting of eigenvectors of the restriction.
Then
\[
x,v_2,\ldots,v_n
\]
is an orthonormal basis of $\mathbb R^n$ consisting entirely of eigenvectors of $A$.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>5 proves part <1>1, step <1>7 proves part <1>2, and step <1>10 proves part <1>3 by induction using only the earlier conclusions just established directly from the maximizing property.
:::
:::
