---
schema: qual/card@1
id: P-UNL871F13-PS7.2
kind: problem
title: Connectedness and path components of the flea-and-comb space
classification:
  areas: [topology]
  topics: [Connectedness]
relations: []
review: draft
---

::: {.problem}
Let
$$
X=\{(0,1)\}\cup\{(x,0):0\le x\le1\}\cup
\left\{\left(\frac1n,y\right):0\le y\le1,\ n\in\NN\right\}
\subset\RR^2
$$
with the subspace topology.

1. Show that $X\setminus\{(0,1)\}$ is path-connected.

2. Show that $X$ is connected.

3. Show that $X$ is not path-connected.

4. Prove that $X$ has exactly two path components, one of which is not closed in $X$.
:::

::: {.solution}

Set
$$
p\coloneqq(0,1)
$$
and
$$
Y\coloneqq X\setminus\{p\}.
$$

::: pf

::: {.pf-step #s1-1}

Every point of $Y$ can be joined by a path in $Y$ to the point
$$
(0,0).
$$


::: pf-proof

Let
$$
q\in Y.
$$

If
$$
q=(x,0)
$$
lies on the horizontal base, use the straight-line path
$$
\gamma(t)=((1-t)x,0).
$$

If
$$
q=\left(\frac1n,y\right)
$$
lies on the $n$th vertical tooth, first travel vertically down the tooth:
$$
\gamma_1(t)
=
\left(
\frac1n,(1-t)y
\right),
$$
from $q$ to
$$
\left(\frac1n,0\right),
$$
then travel along the horizontal base to
$$
(0,0).
$$

Both pieces lie in $Y$.

:::

:::

::: {.pf-step #s1-2}

The space
$$
Y
$$
is path-connected.


::: pf-proof

Given
$$
q_0,q_1\in Y,
$$
step [](#s1-1){.pf-ref} gives a path from $q_0$ to
$$
(0,0)
$$
and another path from $q_1$ to
$$
(0,0).
$$
Reverse the second path and concatenate.
This gives a path in $Y$ from $q_0$ to $q_1$.

:::

:::

::: {.pf-step #s1-3}

The point
$$
p=(0,1)
$$
lies in the closure of $Y$.


::: pf-proof

For each
$$
n\in\NN,
$$
the point
$$
p_n
=
\left(
\frac1n,1
\right)
$$
lies in $Y$.
Moreover,
$$
p_n\to(0,1)=p
$$
in the Euclidean plane, hence also in the subspace topology on $X$.
Therefore every neighborhood of $p$ in $X$ meets $Y$.

:::

:::

::: {.pf-step #s1-4}

The closure of $Y$ in $X$ is all of $X$:
$$
\overline Y^X=X.
$$


::: pf-proof

Clearly
$$
Y\subseteq\overline Y^X.
$$
Step [](#s1-3){.pf-ref} adds the only missing point
$$
p.
$$
Hence
$$
X
=
Y\cup\{p\}
\subseteq
\overline Y^X.
$$
The reverse inclusion is automatic.

:::

:::

::: {.pf-step #s1-5}

The space $X$ is connected.


::: pf-proof

By step [](#s1-2){.pf-ref}, $Y$ is path-connected and therefore connected.
The closure of a connected subset is connected.
By step [](#s1-4){.pf-ref},
$$
X
=
\overline Y^X.
$$
Hence $X$ is connected.

:::

:::

::: {.pf-step #s1-6}

Define
$$
S
\coloneqq
\{0\}
\cup
\left\{
\frac1n:n\in\NN
\right\}
\subseteq\RR.
$$
Every connected subset of $S$ is a singleton.


::: pf-proof

Every connected subset of
$$
\RR
$$
is an interval.
But $S$ contains no nondegenerate interval.
Therefore a connected subset of $S$ can contain at most one point.

:::

:::

::: {.pf-step #s1-7}

Let
$$
\gamma:[0,1]\to X
$$
be a path.
If
$$
\gamma(t_0)=p
$$
for some $t_0$, then there is an open interval
$$
J
$$
around $t_0$ in $[0,1]$ such that
$$
\gamma(t)=p
\qquad
(t\in J).
$$


::: pf-proof

Write
$$
\gamma(t)
=
(x(t),y(t)).
$$
Since
$$
y(t_0)=1
$$
and $y$ is continuous, there is a connected neighborhood interval
$$
J\ni t_0
$$
such that
$$
y(t)>\frac12
\qquad
(t\in J).
$$

For points of $X$ with second coordinate greater than
$$
\frac12,
$$
the possible first coordinates are exactly in
$$
S
=
\{0\}
\cup
\left\{
\frac1n
\right\}.
$$
Thus
$$
x(J)
\subseteq
S.
$$

The interval $J$ is connected, so its continuous image
$$
x(J)
$$
is connected.
By step [](#s1-6){.pf-ref}, $x(J)$ is a singleton.
Since
$$
x(t_0)=0,
$$
one has
$$
x(t)=0
\qquad
(t\in J).
$$

But the only point of $X$ with
$$
x=0
$$
and
$$
y>\frac12
$$
is
$$
(0,1)=p.
$$
Hence
$$
\gamma(t)=p
$$
throughout $J$.

:::

:::

::: {.pf-step #s1-8}

For any path
$$
\gamma:[0,1]\to X,
$$
the set
$$
A
\coloneqq
\{t\in[0,1]:\gamma(t)=p\}
$$
is both open and closed in
$$
[0,1].
$$


::: pf-proof

The set $A$ is closed because
$$
A
=
\gamma^{-1}(\{p\}),
$$
and
$$
\{p\}
$$
is closed in the Hausdorff space $X$.

Step [](#s1-7){.pf-ref} shows that every point of $A$ has a neighborhood contained in
$A$.
Thus $A$ is open.

:::

:::

::: {.pf-step #s1-9}

Any path that starts at $p$ is constant.


::: pf-proof

Suppose
$$
\gamma(0)=p.
$$
Then
$$
0\in A,
$$
so $A$ is nonempty.
By step [](#s1-8){.pf-ref}, $A$ is clopen in the connected interval
$$
[0,1].
$$
Therefore
$$
A=[0,1].
$$
Hence
$$
\gamma(t)=p
$$
for all $t$.

:::

:::

::: {.pf-step #s1-10}

The space $X$ is not path-connected.


::: pf-proof

By step [](#s1-9){.pf-ref}, there is no path from
$$
p
$$
to any point of
$$
Y.
$$
Since $Y$ is nonempty, $X$ is not path-connected.

:::

:::

::: {.pf-step #s1-11}

The path components of $X$ are exactly
$$
\boxed{
\{p\}
\quad\text{and}\quad
Y.
}
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, $Y$ is one path-connected subset.
By step [](#s1-9){.pf-ref}, the point $p$ cannot be joined by a path to any point of $Y$,
so
$$
\{p\}
$$
is the other path component.
There are no further points in $X$.

:::

:::

::: {.pf-step #s1-12}

The path component
$$
Y
$$
is not closed in $X$.


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
p\in\overline Y^X.
$$
But
$$
p\notin Y.
$$
Hence
$$
Y\ne\overline Y^X,
$$
so $Y$ is not closed.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (1), step [](#s1-5){.pf-ref} proves part (2),
step [](#s1-10){.pf-ref} proves part (3), and steps [](#s1-11){.pf-ref} through [](#s1-12){.pf-ref} prove part (4).

:::

:::

:::
