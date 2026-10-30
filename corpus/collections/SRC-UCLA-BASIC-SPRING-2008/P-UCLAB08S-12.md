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
$$
S=\{x\in\RR^n:\norm{x}=1\}.
$$
Choose $x\in S$ such that
$$
(Ax,x)=\sup_{y\in S}(Ay,y),
$$
which exists by compactness.

::: pf

::: {.pf-step #p1-s1}

Prove that $(x,y)=0$ implies $(Ax,y)=0$.
Hint: expand $(A(x+\varepsilon y),x+\varepsilon y)$.

:::

::: pf-step

Use step [](#p1-s1){.pf-ref} to prove that $x$ is an eigenvector of $A$.

:::

::: {.pf-step #p1-s3}

Use induction to prove that $\RR^n$ has an orthonormal basis of eigenvectors for $A$.

:::

:::

If you use step [](#p1-s3){.pf-ref} in proving an earlier part, give a proof of step [](#p1-s3){.pf-ref} that does not depend on those earlier parts.
:::

::: {.solution}
Let
$$
\lambda=(Ax,x),
$$
where
$$
x\in S
$$
maximizes the Rayleigh quotient
$$
y\longmapsto(Ay,y)
$$
on the unit sphere.

::: pf

::: {.pf-step #p2-s1}

Let
$$
y\in\RR^n
$$
satisfy
$$
(x,y)=0.
$$
For every real $\varepsilon$, define
$$
u_\varepsilon
=
\frac{x+\varepsilon y}
{\norm{x+\varepsilon y}}.
$$
Then
$$
u_\varepsilon\in S.
$$

::: pf-proof

Since
$$
\norm{x}=1
$$
and
$$
(x,y)=0,
$$
one has
$$
\norm{x+\varepsilon y}^2
=
1+\varepsilon^2\norm{y}^2
>
0.
$$
Thus $u_\varepsilon$ is well-defined and has norm $1$.

:::

:::

::: {.pf-step #p2-s2}

Maximality of $x$ gives
$$
(Au_\varepsilon,u_\varepsilon)
\le
\lambda.
$$

::: pf-proof

By step [](#p2-s1){.pf-ref},
$$
u_\varepsilon\in S.
$$
The point $x$ was chosen to maximize
$$
(Ay,y)
$$
over $y\in S$.
Hence the inequality holds.

:::

:::

::: {.pf-step #p2-s3}

One has
$$
(A(x+\varepsilon y),x+\varepsilon y)
=
\lambda
+
2\varepsilon(Ax,y)
+
\varepsilon^2(Ay,y).
$$

::: pf-proof

Expand bilinearly:
$$
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
$$
Since $A$ is symmetric,
$$
(Ay,x)=(y,Ax)=(Ax,y).
$$
Also
$$
(Ax,x)=\lambda.
$$
Substitute these identities.

:::

:::

::: {.pf-step #p2-s4}

For every real $\varepsilon$,
$$
2\varepsilon(Ax,y)
+
\varepsilon^2
\bigl(
(Ay,y)-\lambda\norm{y}^2
\bigr)
\le
0.
$$

::: pf-proof

By step [](#p2-s2){.pf-ref},
$$
\frac{
(A(x+\varepsilon y),x+\varepsilon y)
}{
\norm{x+\varepsilon y}^2
}
\le
\lambda.
$$
By orthogonality,
$$
\norm{x+\varepsilon y}^2
=
1+\varepsilon^2\norm{y}^2.
$$
Insert the expansion from step [](#p2-s3){.pf-ref} and multiply by the positive denominator:
$$
\lambda
+
2\varepsilon(Ax,y)
+
\varepsilon^2(Ay,y)
\le
\lambda
+
\lambda\varepsilon^2\norm{y}^2.
$$
Rearranging gives the claimed inequality.

:::

:::

::: {.pf-step #p2-s5}

If
$$
(x,y)=0,
$$
then
$$
\boxed{(Ax,y)=0}.
$$

::: pf-proof

Suppose
$$
(Ax,y)\ne0.
$$
In step [](#p2-s4){.pf-ref}, the term linear in $\varepsilon$ would dominate the quadratic term for sufficiently small $\varepsilon$ having the same sign as $(Ax,y)$.
More explicitly, write
$$
a=(Ax,y)
\ne0
$$
and
$$
b=(Ay,y)-\lambda\norm{y}^2.
$$
The inequality says
$$
2a\varepsilon+b\varepsilon^2\le0
$$
for every $\varepsilon$.
Choose $\varepsilon$ with the same sign as $a$ and sufficiently small that
$$
\abs{b\varepsilon}<\abs{a}.
$$
Then
$$
2a\varepsilon+b\varepsilon^2
\ge
2\abs{a}\abs{\varepsilon}-\abs{b}\varepsilon^2
>
\abs{a}\abs{\varepsilon}
>
0,
$$
a contradiction.
Hence
$$
(Ax,y)=0.
$$
This proves part step [](#p2-s1){.pf-ref}.

:::

:::

::: {.pf-step #p2-s6}

The vector $Ax$ belongs to
$$
\operatorname{span}\{x\}.
$$

::: pf-proof

Step [](#p2-s5){.pf-ref} says
$$
(Ax,y)=0
$$
for every
$$
y\in x^\perp.
$$
Thus
$$
Ax\in(x^\perp)^\perp.
$$
In finite-dimensional Euclidean space,
$$
(x^\perp)^\perp
=
\operatorname{span}\{x\}.
$$

:::

:::

::: {.pf-step #p2-s7}

Therefore
$$
\boxed{Ax=\lambda x}.
$$

::: pf-proof

By step [](#p2-s6){.pf-ref}, there is a scalar $\mu$ such that
$$
Ax=\mu x.
$$
Taking inner products with $x$ and using
$$
\norm{x}=1,
$$
gives
$$
\mu
=
(Ax,x)
=
\lambda.
$$
Hence
$$
Ax=\lambda x.
$$
This proves part step [](#p2-s2){.pf-ref}.

:::

:::

::: {.pf-step #p2-s8}

If
$$
y\in x^\perp,
$$
then
$$
Ay\in x^\perp.
$$

::: pf-proof

By symmetry of $A$ and step [](#p2-s7){.pf-ref},
$$
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
$$
Thus
$$
Ay\perp x.
$$

:::

:::

::: {.pf-step #p2-s9}

The restriction
$$
A\restrict_{x^\perp}:x^\perp\to x^\perp
$$
is symmetric.

::: pf-proof

Step [](#p2-s8){.pf-ref} shows the restriction is well-defined.
For
$$
y,z\in x^\perp,
$$
one has
$$
(Ay,z)
=(y,Az)
$$
because $A$ is symmetric on all of $\RR^n$.
Hence the restriction is symmetric on $x^\perp$.

:::

:::

::: {.pf-step #p2-s10}

Every real symmetric $n\times n$ matrix has an orthonormal basis of eigenvectors.

::: pf-proof

Proceed by induction on $n$.

For
$$
n=1,
$$
the statement is immediate.

Assume the theorem holds in dimension $n-1$.
Choose the maximizing unit vector $x$ as in the problem.
By steps [](#p2-s1){.pf-ref}, [](#p2-s2){.pf-ref}, [](#p2-s3){.pf-ref}, [](#p2-s4){.pf-ref}, [](#p2-s5){.pf-ref}, [](#p2-s6){.pf-ref} and [](#p2-s7){.pf-ref}, $x$ is an eigenvector.
The orthogonal complement
$$
x^\perp
$$
has dimension $n-1$.
By steps [](#p2-s8){.pf-ref} and [](#p2-s9){.pf-ref}, it is invariant under $A$ and the restriction of $A$ to it is symmetric.
The induction hypothesis therefore gives an orthonormal basis
$$
v_2,\ldots,v_n
$$
of $x^\perp$ consisting of eigenvectors of the restriction.
Then
$$
x,v_2,\ldots,v_n
$$
is an orthonormal basis of $\RR^n$ consisting entirely of eigenvectors of $A$.

:::

:::

::: pf-qed

Step [](#p2-s5){.pf-ref} proves part step [](#p2-s1){.pf-ref}, step [](#p2-s7){.pf-ref} proves part step [](#p2-s2){.pf-ref}, and step [](#p2-s10){.pf-ref} proves part step [](#p2-s3){.pf-ref} by induction using only the earlier conclusions just established directly from the maximizing property.

:::

:::

:::
