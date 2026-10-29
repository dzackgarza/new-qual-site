---
schema: qual/card@1
id: P-UCLAB17S-10
kind: problem
title: Compact chain-connected sets
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2017, `assets/attachments/basic-17S.pdf`.
---

::: {.problem}
Let $K\subset\RR^n$ be compact. Assume that for every $\varepsilon>0$ and $a,b\in K$ there is a finite sequence $a=x_0,x_1,\dots,x_m=b$ in $K$ with $\|x_k-x_{k-1}\|<\varepsilon$.

(a) Show that $K$ is connected.

(b) Give an example showing that $K$ need not be path connected.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Suppose, for contradiction, that $K$ is disconnected.
Then there exist disjoint nonempty subsets
\[
U,V\subseteq K
\]
such that
\[
K=U\cup V
\]
and both $U$ and $V$ are open in $K$.


::: pf-proof

This is the definition of disconnectedness.
Since each is the complement in $K$ of the other, both are also closed in $K$.

:::

:::

::: pf-step

The sets $U$ and $V$ are compact.


::: pf-proof

The set $K$ is compact by hypothesis.
By step [](#s1-1){.pf-ref}, $U$ and $V$ are closed subsets of $K$.
Closed subsets of compact spaces are compact.

:::

:::

::: pf-step

The distance
\[
\delta
=
\inf\{\|u-v\|:u\in U,\ v\in V\}
\]
is strictly positive.


::: pf-proof

The continuous function
\[
(u,v)\longmapsto\|u-v\|
\]
on the compact product
\[
U\times V
\]
attains its minimum.
Because
\[
U\cap V=\varnothing,
\]
that minimum cannot be $0$.
Hence
\[
\delta>0.
\]

:::

:::

::: {.pf-step #s1-4}

Choose
\[
a\in U,
\qquad
b\in V,
\]
and apply the chain hypothesis with
\[
\varepsilon=\delta.
\]
Then there are points
\[
a=x_0,x_1,\ldots,x_m=b
\]
in $K$ with
\[
\|x_k-x_{k-1}\|<\delta.
\]


::: pf-proof

This is exactly the assumed chain property.

:::

:::

::: {.pf-step #s1-5}

Some adjacent pair in the chain from step [](#s1-4){.pf-ref} has one point in $U$ and the other in $V$.


::: pf-proof

The chain starts in $U$ and ends in $V$.
Let $j$ be the smallest index for which
\[
x_j\in V.
\]
Then
\[
j\ge1
\]
and
\[
x_{j-1}\in U.
\]

:::

:::

::: {.pf-step #s1-6}

Step [](#s1-5){.pf-ref} contradicts the definition of $\delta$.


::: pf-proof

Since
\[
x_{j-1}\in U
\qquad\text{and}\qquad
x_j\in V,
\]
the definition of $\delta$ gives
\[
\|x_j-x_{j-1}\|
\ge
\delta.
\]
But step [](#s1-4){.pf-ref} gives
\[
\|x_j-x_{j-1}\|
<
\delta.
\]
Contradiction.

:::

:::

::: {.pf-step #s1-7}

Therefore
\[
\boxed{K\text{ is connected}.}
\]


::: pf-proof

The assumption of disconnectedness in step [](#s1-1){.pf-ref} led to the contradiction in step [](#s1-6){.pf-ref}.
This proves part (a).

:::

:::

::: {.pf-step #s1-8}

Every connected metric space is $\varepsilon$-chain connected for every $\varepsilon>0$.


::: pf-proof

Let $X$ be connected, fix
\[
a\in X
\]
and
\[
\varepsilon>0.
\]
Let $R$ be the set of all points that can be joined to $a$ by a finite $\varepsilon$-chain.

The set $R$ is open: if
\[
x\in R
\]
and
\[
d(x,y)<\varepsilon,
\]
append $y$ to an $\varepsilon$-chain from $a$ to $x$.

The complement is also open: if
\[
y\notin R
\]
and
\[
d(y,z)<\varepsilon,
\]
then $z$ cannot belong to $R$, because otherwise appending $y$ to a chain ending at $z$ would put $y$ in $R$.

Thus $R$ is nonempty, open, and closed.
Connectedness forces
\[
R=X.
\]

:::

:::

::: {.pf-step #s1-9}

Define the closed topologist's sine curve
\[
\boxed{
K_0
=
\left\{
\left(x,\sin\frac1x\right):
0<x\le1
\right\}
\cup
\bigl(
\{0\}\times[-1,1]
\bigr).
}
\]


::: pf-proof

This is a subset of
\[
[0,1]\times[-1,1].
\]

:::

:::

::: {.pf-step #s1-10}

The set $K_0$ is compact.


::: pf-proof

Let
\[
G
=
\left\{
\left(x,\sin\frac1x\right):
0<x\le1
\right\}.
\]
The closure of $G$ in $\RR^2$ is exactly $K_0$:
every point
\[
(0,y),
\qquad
y\in[-1,1],
\]
is approached by a sequence
\[
\left(x_n,\sin\frac1{x_n}\right)
\]
with
\[
x_n\to0,
\]
while there are no other new limit points.
Thus
\[
K_0=\overline G
\]
is closed.
It is bounded by step [](#s1-9){.pf-ref}.
Hence Heine--Borel implies compactness.

:::

:::

::: {.pf-step #s1-11}

The set $K_0$ is connected.


::: pf-proof

The interval
\[
(0,1]
\]
is connected, and the map
\[
x\longmapsto
\left(
x,\sin\frac1x
\right)
\]
is continuous.
Thus $G$ is connected.
The closure of a connected set is connected, and by step [](#s1-10){.pf-ref},
\[
\overline G=K_0.
\]

:::

:::

::: {.pf-step #s1-12}

Consequently $K_0$ satisfies the chain hypothesis of the problem.


::: pf-proof

Apply step [](#s1-8){.pf-ref} to the connected metric space $K_0$ from step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

The set $K_0$ is not path connected.


::: pf-proof

Suppose there were a path
\[
\gamma(t)
=
\bigl(
u(t),v(t)
\bigr),
\qquad
0\le t\le1,
\]
from
\[
(0,0)
\]
to a point of $G$.

Choose $t_1$ with
\[
u(t_1)>0,
\]
and let $t_0$ be the last time in $[0,t_1]$ for which
\[
u(t_0)=0.
\]
Then
\[
u(t)>0
\]
for
\[
t_0<t\le t_1,
\]
so
\[
v(t)
=
\sin\frac1{u(t)}
\]
there.

By continuity of $u$, it assumes arbitrarily small positive values immediately after $t_0$.
Choose sequences
\[
s_n,t_n\downarrow t_0
\]
so that
\[
u(s_n)
=
\frac1{\pi/2+2\pi n},
\]
and
\[
u(t_n)
=
\frac1{3\pi/2+2\pi n}.
\]
Then
\[
v(s_n)=1
\]
for every $n$, while
\[
v(t_n)=-1
\]
for every $n$.
Both sequences of parameters converge to $t_0$, contradicting continuity of $v$ at $t_0$.
Thus no such path exists.

:::

:::

::: {.pf-step #s1-14}

Therefore the chain condition does not imply path connectedness.


::: pf-proof

The set $K_0$ is compact by step [](#s1-10){.pf-ref} and satisfies the required chain condition by step [](#s1-12){.pf-ref}, but it is not path connected by step [](#s1-13){.pf-ref}.
This proves part (b).

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} proves part (a), and step [](#s1-14){.pf-ref} gives the requested example for part (b).

:::

:::

:::
