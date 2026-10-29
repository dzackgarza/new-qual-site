---
schema: qual/card@1
id: P-UCLAB11S-11
kind: problem
title: Connected subsets of the line and a planar counterexample
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 11 of the retained UCLA Basic Examination, Spring 2011.
---
::: {.problem}

::: pf

::: pf-step

Prove that every connected subset $A\subset\RR$ is arcwise connected.

:::

::: pf-step

Give an example of a connected subset of $\RR^2$ that is not arcwise connected.

:::

:::

:::

::: {.solution}

::: pf

::: {.pf-step #p2-s1}

Let $A\subseteq\RR$ be connected and let
$$
x,y\in A
$$
with
$$
x<y.
$$
Then
$$
[x,y]\subseteq A.
$$

::: pf-proof

Suppose some
$$
c\in(x,y)
$$
did not belong to $A$.
Then
$$
U=A\cap(-\infty,c)
$$
and
$$
V=A\cap(c,\infty)
$$
would be disjoint nonempty subsets of $A$, because
$$
x\in U
\qquad\text{and}\qquad
y\in V.
$$
Both are open in the subspace topology on $A$, and
$$
A=U\cup V
$$
because
$$
c\notin A.
$$
This would disconnect $A$, contradicting the hypothesis.
Therefore every point between $x$ and $y$ belongs to $A$.

:::

:::

::: {.pf-step #p2-s2}

Every connected subset of $\RR$ is arcwise connected.

::: pf-proof

Let
$$
x,y\in A.
$$
If
$$
x=y,
$$
the constant path joins them.
Otherwise, after interchanging them if necessary, assume
$$
x<y.
$$
By step [](#p2-s1){.pf-ref},
$$
[x,y]\subseteq A.
$$
Define
$$
\gamma:[0,1]\to A,
\qquad
\gamma(t)=(1-t)x+ty.
$$
Then $\gamma$ is continuous,
$$
\gamma(0)=x,
\qquad
\gamma(1)=y,
$$
and its image is exactly $[x,y]\subseteq A$.
Thus every pair of points can be joined by an arc.

:::

:::

::: pf-step

For part step [](#p2-s2){.pf-ref}, define
$$
G
=
\left\{
\left(x,\sin\frac1x\right):
0<x\le1
\right\}
$$
and
$$
X
=
G
\cup
\bigl(
\{0\}\times[-1,1]
\bigr).
$$

::: pf-proof

This is the standard topologist's sine curve.

:::

:::

::: {.pf-step #p2-s4}

The set $G$ is connected.

::: pf-proof

The interval
$$
(0,1]
$$
is connected.
The map
$$
\phi:(0,1]\to\RR^2,
\qquad
\phi(x)
=
\left(
x,\sin\frac1x
\right)
$$
is continuous.
The continuous image of a connected space is connected.
Hence
$$
G=\phi((0,1])
$$
is connected.

:::

:::

::: {.pf-step #p2-s5}

One has
$$
\overline G
=
G
\cup
\bigl(
\{0\}\times[-1,1]
\bigr)
=
X.
$$

::: pf-proof

Every point of $G$ lies in its closure.

Fix
$$
y\in[-1,1].
$$
Choose
$$
\theta\in\RR
$$
with
$$
\sin\theta=y.
$$
For sufficiently large positive integers $n$, set
$$
x_n
=
\frac1{\theta+2\pi n},
$$
choosing $n$ so the denominator is positive.
Then
$$
x_n\to0
$$
and
$$
\sin\frac1{x_n}
=
\sin(\theta+2\pi n)
=
y.
$$
Thus
$$
\left(
x_n,\sin\frac1{x_n}
\right)
\to
(0,y),
$$
so every point of
$$
\{0\}\times[-1,1]
$$
lies in $\overline G$.

Conversely, any limit point of $G$ whose first coordinate is positive lies on the graph by continuity, while if the first coordinate is $0$, the second coordinate must lie in $[-1,1]$.
Thus the closure is exactly $X$.

:::

:::

::: {.pf-step #p2-s6}

The set $X$ is connected.

::: pf-proof

By step [](#p2-s4){.pf-ref}, $G$ is connected.
The closure of a connected subset of a topological space is connected.
By step [](#p2-s5){.pf-ref},
$$
X=\overline G.
$$
Hence $X$ is connected.

:::

:::

::: {.pf-step #p2-s7}

Suppose, for contradiction, that there is a continuous path
$$
\gamma:[0,1]\to X
$$
from
$$
(0,0)
$$
to some point of $G$.
Write
$$
\gamma(t)
=
\bigl(
u(t),v(t)
\bigr).
$$

::: pf-proof

This is the negation of the claim that the vertical segment and the graph lie in different path components.
The coordinate functions $u,v$ are continuous because $\gamma$ is continuous.

:::

:::

::: {.pf-step #p2-s8}

There exist numbers
$$
0\le t_0<t_1\le1
$$
such that
$$
u(t_0)=0,
\qquad
u(t)>0
$$
for
$$
t_0<t\le t_1.
$$

::: pf-proof

Since the endpoint $\gamma(1)$ lies in $G$, one has
$$
u(1)>0.
$$
Choose
$$
t_1
$$
with
$$
u(t_1)>0.
$$
The set
$$
Z
=
\{t\in[0,t_1]:u(t)=0\}
$$
is nonempty because
$$
0\in Z,
$$
and is closed because $u$ is continuous.
Hence $Z$ has a maximum
$$
t_0.
$$
By definition of $t_0$, there are no zeros of $u$ in
$$
(t_0,t_1].
$$
Since points of $X$ have nonnegative first coordinate, one has
$$
u(t)>0
$$
there.

:::

:::

::: {.pf-step #p2-s9}

For every
$$
t\in(t_0,t_1],
$$
one has
$$
\boxed{
v(t)=\sin\frac1{u(t)}.
}
$$

::: pf-proof

When
$$
u(t)>0,
$$
the point
$$
\gamma(t)\in X
$$
cannot lie on the vertical segment
$$
\{0\}\times[-1,1].
$$
Therefore it lies in $G$, whose defining relation is
$$
v=\sin(1/u).
$$

:::

:::

::: {.pf-step #p2-s10}

There are sequences
$$
s_n,t_n\in(t_0,t_1]
$$
such that
$$
s_n\to t_0,
\qquad
t_n\to t_0,
$$
while
$$
v(s_n)=1
\qquad\text{and}\qquad
v(t_n)=-1.
$$

::: pf-proof

Because
$$
u(t_0)=0
$$
and
$$
u(t_1)>0,
$$
the intermediate value theorem shows that $u$ assumes every sufficiently small positive value on $[t_0,t_1]$.

Choose positive numbers
$$
\alpha_n
=
\frac1{\pi/2+2\pi n}
\to0
$$
and
$$
\beta_n
=
\frac1{3\pi/2+2\pi n}
\to0.
$$
For large $n$, choose
$$
s_n,t_n\in(t_0,t_1]
$$
such that
$$
u(s_n)=\alpha_n,
\qquad
u(t_n)=\beta_n.
$$

Any convergent subsequence of $(s_n)$ has limit $s$ with
$$
u(s)=0
$$
by continuity.
By step [](#p2-s8){.pf-ref}, the only zero of $u$ in $[t_0,t_1]$ is $t_0$.
Hence
$$
s_n\to t_0.
$$
Similarly,
$$
t_n\to t_0.
$$

Using step [](#p2-s9){.pf-ref},
$$
v(s_n)
=
\sin\left(\frac1{\alpha_n}\right)
=
\sin\left(\frac\pi2+2\pi n\right)
=1,
$$
while
$$
v(t_n)
=
\sin\left(\frac1{\beta_n}\right)
=
\sin\left(\frac{3\pi}2+2\pi n\right)
=-1.
$$

:::

:::

::: {.pf-step #p2-s11}

Step [](#p2-s10){.pf-ref} contradicts continuity of $v$ at $t_0$.

::: pf-proof

Both sequences
$$
s_n,t_n
$$
converge to $t_0$.
Continuity of $v$ would require
$$
v(s_n)\to v(t_0)
$$
and
$$
v(t_n)\to v(t_0).
$$
But step [](#p2-s10){.pf-ref} gives constant values
$$
v(s_n)=1
$$
and
$$
v(t_n)=-1.
$$
They cannot converge to the same number.

:::

:::

::: {.pf-step #p2-s12}

Therefore $X$ is not arcwise connected.

::: pf-proof

By step [](#p2-s6){.pf-ref}, $X$ is connected.
If it were arcwise connected, there would be a path from
$$
(0,0)
$$
to any chosen point of $G$.
Steps [](#p2-s7){.pf-ref}, [](#p2-s8){.pf-ref}, [](#p2-s9){.pf-ref}, [](#p2-s10){.pf-ref} and [](#p2-s11){.pf-ref} show that no such path exists.
Hence
$$
\boxed{X\text{ is connected but not arcwise connected}.}
$$

:::

:::

::: pf-qed

Step [](#p2-s2){.pf-ref} proves part step [](#p2-s1){.pf-ref}, and step [](#p2-s12){.pf-ref} gives the example required in part step [](#p2-s2){.pf-ref}.

:::

:::

:::
