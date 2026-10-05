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
<1>1. Prove that every connected subset $A\subset\mathbb R$ is arcwise connected.
<1>2. Give an example of a connected subset of $\mathbb R^2$ that is not arcwise connected.
:::

::: {.solution}
<1>1. Let $A\subseteq\mathbb R$ be connected and let
\[
x,y\in A
\]
with
\[
x<y.
\]
Then
\[
[x,y]\subseteq A.
\]

::: {.proof}
Suppose some
\[
c\in(x,y)
\]
did not belong to $A$.
Then
\[
U=A\cap(-\infty,c)
\]
and
\[
V=A\cap(c,\infty)
\]
would be disjoint nonempty subsets of $A$, because
\[
x\in U
\qquad\text{and}\qquad
y\in V.
\]
Both are open in the subspace topology on $A$, and
\[
A=U\cup V
\]
because
\[
c\notin A.
\]
This would disconnect $A$, contradicting the hypothesis.
Therefore every point between $x$ and $y$ belongs to $A$.
:::

<1>2. Every connected subset of $\mathbb R$ is arcwise connected.

::: {.proof}
Let
\[
x,y\in A.
\]
If
\[
x=y,
\]
the constant path joins them.
Otherwise, after interchanging them if necessary, assume
\[
x<y.
\]
By step <1>1,
\[
[x,y]\subseteq A.
\]
Define
\[
\gamma:[0,1]\to A,
\qquad
\gamma(t)=(1-t)x+ty.
\]
Then $\gamma$ is continuous,
\[
\gamma(0)=x,
\qquad
\gamma(1)=y,
\]
and its image is exactly $[x,y]\subseteq A$.
Thus every pair of points can be joined by an arc.
:::

<1>3. For part <1>2, define
\[
G
=
\left\{
\left(x,\sin\frac1x\right):
0<x\le1
\right\}
\]
and
\[
X
=
G
\cup
\bigl(
\{0\}\times[-1,1]
\bigr).
\]

::: {.proof}
This is the standard topologist's sine curve.
:::

<1>4. The set $G$ is connected.

::: {.proof}
The interval
\[
(0,1]
\]
is connected.
The map
\[
\phi:(0,1]\to\mathbb R^2,
\qquad
\phi(x)
=
\left(
x,\sin\frac1x
\right)
\]
is continuous.
The continuous image of a connected space is connected.
Hence
\[
G=\phi((0,1])
\]
is connected.
:::

<1>5. One has
\[
\overline G
=
G
\cup
\bigl(
\{0\}\times[-1,1]
\bigr)
=
X.
\]

::: {.proof}
Every point of $G$ lies in its closure.

Fix
\[
y\in[-1,1].
\]
Choose
\[
\theta\in\mathbb R
\]
with
\[
\sin\theta=y.
\]
For sufficiently large positive integers $n$, set
\[
x_n
=
\frac1{\theta+2\pi n},
\]
choosing $n$ so the denominator is positive.
Then
\[
x_n\to0
\]
and
\[
\sin\frac1{x_n}
=
\sin(\theta+2\pi n)
=
y.
\]
Thus
\[
\left(
x_n,\sin\frac1{x_n}
\right)
\to
(0,y),
\]
so every point of
\[
\{0\}\times[-1,1]
\]
lies in $\overline G$.

Conversely, any limit point of $G$ whose first coordinate is positive lies on the graph by continuity, while if the first coordinate is $0$, the second coordinate must lie in $[-1,1]$.
Thus the closure is exactly $X$.
:::

<1>6. The set $X$ is connected.

::: {.proof}
By step <1>4, $G$ is connected.
The closure of a connected subset of a topological space is connected.
By step <1>5,
\[
X=\overline G.
\]
Hence $X$ is connected.
:::

<1>7. Suppose, for contradiction, that there is a continuous path
\[
\gamma:[0,1]\to X
\]
from
\[
(0,0)
\]
to some point of $G$.
Write
\[
\gamma(t)
=
\bigl(
u(t),v(t)
\bigr).
\]

::: {.proof}
This is the negation of the claim that the vertical segment and the graph lie in different path components.
The coordinate functions $u,v$ are continuous because $\gamma$ is continuous.
:::

<1>8. There exist numbers
\[
0\le t_0<t_1\le1
\]
such that
\[
u(t_0)=0,
\qquad
u(t)>0
\]
for
\[
t_0<t\le t_1.
\]

::: {.proof}
Since the endpoint $\gamma(1)$ lies in $G$, one has
\[
u(1)>0.
\]
Choose
\[
t_1
\]
with
\[
u(t_1)>0.
\]
The set
\[
Z
=
\{t\in[0,t_1]:u(t)=0\}
\]
is nonempty because
\[
0\in Z,
\]
and is closed because $u$ is continuous.
Hence $Z$ has a maximum
\[
t_0.
\]
By definition of $t_0$, there are no zeros of $u$ in
\[
(t_0,t_1].
\]
Since points of $X$ have nonnegative first coordinate, one has
\[
u(t)>0
\]
there.
:::

<1>9. For every
\[
t\in(t_0,t_1],
\]
one has
\[
\boxed{
v(t)=\sin\frac1{u(t)}.
}
\]

::: {.proof}
When
\[
u(t)>0,
\]
the point
\[
\gamma(t)\in X
\]
cannot lie on the vertical segment
\[
\{0\}\times[-1,1].
\]
Therefore it lies in $G$, whose defining relation is
\[
v=\sin(1/u).
\]
:::

<1>10. There are sequences
\[
s_n,t_n\in(t_0,t_1]
\]
such that
\[
s_n\to t_0,
\qquad
t_n\to t_0,
\]
while
\[
v(s_n)=1
\qquad\text{and}\qquad
v(t_n)=-1.
\]

::: {.proof}
Because
\[
u(t_0)=0
\]
and
\[
u(t_1)>0,
\]
the intermediate value theorem shows that $u$ assumes every sufficiently small positive value on $[t_0,t_1]$.

Choose positive numbers
\[
\alpha_n
=
\frac1{\pi/2+2\pi n}
\to0
\]
and
\[
\beta_n
=
\frac1{3\pi/2+2\pi n}
\to0.
\]
For large $n$, choose
\[
s_n,t_n\in(t_0,t_1]
\]
such that
\[
u(s_n)=\alpha_n,
\qquad
u(t_n)=\beta_n.
\]

Any convergent subsequence of $(s_n)$ has limit $s$ with
\[
u(s)=0
\]
by continuity.
By step <1>8, the only zero of $u$ in $[t_0,t_1]$ is $t_0$.
Hence
\[
s_n\to t_0.
\]
Similarly,
\[
t_n\to t_0.
\]

Using step <1>9,
\[
v(s_n)
=
\sin\left(\frac1{\alpha_n}\right)
=
\sin\left(\frac\pi2+2\pi n\right)
=1,
\]
while
\[
v(t_n)
=
\sin\left(\frac1{\beta_n}\right)
=
\sin\left(\frac{3\pi}2+2\pi n\right)
=-1.
\]
:::

<1>11. Step <1>10 contradicts continuity of $v$ at $t_0$.

::: {.proof}
Both sequences
\[
s_n,t_n
\]
converge to $t_0$.
Continuity of $v$ would require
\[
v(s_n)\to v(t_0)
\]
and
\[
v(t_n)\to v(t_0).
\]
But step <1>10 gives constant values
\[
v(s_n)=1
\]
and
\[
v(t_n)=-1.
\]
They cannot converge to the same number.
:::

<1>12. Therefore $X$ is not arcwise connected.

::: {.proof}
By step <1>6, $X$ is connected.
If it were arcwise connected, there would be a path from
\[
(0,0)
\]
to any chosen point of $G$.
Steps <1>7--<1>11 show that no such path exists.
Hence
\[
\boxed{X\text{ is connected but not arcwise connected}.}
\]
:::

<1>13. Q.E.D.

::: {.proof}
Step <1>2 proves part <1>1, and step <1>12 gives the example required in part <1>2.
:::
:::
