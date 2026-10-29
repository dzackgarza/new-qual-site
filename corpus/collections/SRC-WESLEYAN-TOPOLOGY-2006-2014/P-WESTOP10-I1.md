---
schema: qual/card@1
id: P-WESTOP10-I1
kind: problem
title: Compare three topologies on the square $[0,1]^2$
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $I=[0,1]$. Compare the following three topologies on $I\times I$:

1. the product topology;
2. the dictionary-order topology on $I\times I$;
3. the topology inherited by $I\times I$ as a subspace of $\RR\times\RR$ equipped with the dictionary-order topology.
:::

::: {.solution}

Write
$$
\tau_{mathrm{prod}}
$$
for the product topology,
$$
\tau_{mathrm{ord}}
$$
for the order topology on $I\times I$ with its intrinsic lexicographic
order, and
$$
\tau_{mathrm{sub}}
$$
for the subspace topology inherited from
$$
\RR\times\RR
$$
with the lexicographic order topology.

Recall that
$$
(x,y)<_{mathrm{lex}}(x',y')
$$
if either
$$
x<x',
$$
or
$$
x=x'
\quad\text{and}\quad
y<y'.
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
\tau_{mathrm{ord}}
\subseteq
\tau_{mathrm{sub}}.
$$


::: pf-proof

A basis for the intrinsic order topology consists of open order intervals
$$
(a,b)_{I\times I}
$$
together with initial and final intervals at the minimum
$$
(0,0)
$$
and maximum
$$
(1,1).
$$

If
$$
a,b\in I\times I,
$$
then
$$
(a,b)_{I\times I}
=
(a,b)_{\RR\times\RR}
\cap
(I\times I).
$$
Thus every ordinary intrinsic interval is subspace-open.

For an initial interval
$$
[(0,0),b)_{I\times I},
$$
choose, for example,
$$
c=(0,-1)
$$
in the ambient lexicographic plane. Then
$$
[(0,0),b)_{I\times I}
=
(c,b)_{\RR\times\RR}
\cap
(I\times I).
$$
Similarly, a final interval
$$
(a,(1,1)]_{I\times I}
$$
is obtained by intersecting with an ambient interval ending at
$$
(1,2).
$$
Hence every intrinsic-order basis set is subspace-open.

:::

:::

::: {.pf-step #s1-2}

The inclusion in step [](#s1-1){.pf-ref} is strict:
$$
\boxed{
\tau_{mathrm{ord}}
\subsetneq
\tau_{mathrm{sub}}.
}
$$


::: pf-proof

Fix
$$
x_0\in(0,1)
$$
and consider
$$
U
\coloneqq
\{x_0\}\times
\left[0,\frac12\right).
$$
In the ambient lexicographic plane,
$$
\bigl(
(x_0,-1),
(x_0,1/2)
\bigr)
$$
is open.
Intersecting with the square gives exactly
$$
U.
$$
Thus
$$
U\in\tau_{mathrm{sub}}.
$$

But $U$ is not open in the intrinsic order topology.
At the point
$$
p=(x_0,0),
$$
there is no point of the same vertical fiber lying strictly below $p$ in
$I\times I$.
Hence every intrinsic-order neighborhood of $p$ contains points with first
coordinate strictly less than $x_0$.
Such points are not in $U$.
Therefore $p$ has no intrinsic-order neighborhood contained in $U$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\tau_{mathrm{prod}}
\subseteq
\tau_{mathrm{sub}}.
$$


::: pf-proof

Let
$$
O
$$
be product-open and let
$$
(x_0,y_0)\in O.
$$
Choose a product-basic neighborhood
$$
U\times V
$$
with
$$
(x_0,y_0)
\in
U\times V
\subseteq
O.
$$

Because
$$
V\subseteq I
$$
is open in the subspace topology, choose
$$
\varepsilon>0
$$
such that
$$
(y_0-\varepsilon,y_0+\varepsilon)
\cap I
\subseteq
V.
$$
Then the ambient lexicographic interval
$$
\bigl(
(x_0,y_0-\varepsilon),
(x_0,y_0+\varepsilon)
\bigr)
$$
intersects the square in
$$
\{x_0\}
\times
\bigl(
(y_0-\varepsilon,y_0+\varepsilon)
\cap I
\bigr),
$$
which is contained in
$$
U\times V.
$$
Thus every point of $O$ has a
$$
\tau_{mathrm{sub}}
$$
neighborhood contained in $O$.
Hence
$$
O\in\tau_{mathrm{sub}}.
$$

:::

:::

::: {.pf-step #s1-4}

The inclusion in step [](#s1-3){.pf-ref} is strict:
$$
\boxed{
\tau_{mathrm{prod}}
\subsetneq
\tau_{mathrm{sub}}.
}
$$


::: pf-proof

The set
$$
U
=
\{x_0\}
\times
\left[0,\frac12\right)
$$
from step [](#s1-2){.pf-ref} is
$$
\tau_{mathrm{sub}}
$$
open.

It is not product-open.
Indeed, any product neighborhood of
$$
(x_0,1/4)
$$
contains points whose first coordinate differs from $x_0$, while $U$
contains only points with first coordinate exactly $x_0$.

:::

:::

::: {.pf-step #s1-5}

The intrinsic lexicographic order topology is not contained in the
product topology.


::: pf-proof

Fix
$$
x_0\in(0,1)
$$
and
$$
0<a<b<1.
$$
Then
$$
V
\coloneqq
\{x_0\}\times(a,b)
$$
is the intrinsic order interval
$$
\bigl(
(x_0,a),
(x_0,b)
\bigr)_{I\times I}.
$$
Thus
$$
V\in\tau_{mathrm{ord}}.
$$

But $V$ is not product-open for the same reason as in step [](#s1-4){.pf-ref}:
every product neighborhood of a point
$$
(x_0,y)
\in V
$$
contains points with first coordinate different from $x_0$.
Hence
$$
V\notin\tau_{mathrm{prod}}.
$$

:::

:::

::: {.pf-step #s1-6}

The product topology is not contained in the intrinsic order
topology.


::: pf-proof

Fix
$$
x_0\in(0,1)
$$
and choose
$$
0<\delta<\min\{x_0,1-x_0\}.
$$
Consider the product-open set
$$
W
\coloneqq
(x_0-\delta,x_0+\delta)
\times
\left[0,\frac12\right)
\subseteq
I\times I.
$$
It contains
$$
p=(x_0,0).
$$

Suppose $W$ were intrinsic-order open.
Then $p$ would have an order interval neighborhood
$$
(a,b)_{I\times I}
\subseteq
W.
$$
Because $p$ is the least point in its vertical fiber, the lower endpoint
$a$ must have first coordinate
$$
a_1<x_0.
$$
Choose
$$
x'
$$
with
$$
a_1<x'<x_0
$$
and sufficiently close to $x_0$ that
$$
x'\in(x_0-\delta,x_0+\delta).
$$
Then
$$
(x',1)
$$
lies lexicographically between $a$ and $p$, hence lies in
$$
(a,b)_{I\times I}.
$$
But
$$
(x',1)\notin W
$$
because its second coordinate is $1$.
Contradiction.

Thus
$$
W\in\tau_{mathrm{prod}}
\setminus
\tau_{mathrm{ord}}.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\tau_{mathrm{prod}}
\quad\text{and}\quad
\tau_{mathrm{ord}}
$$
are incomparable.


::: pf-proof

Step [](#s1-5){.pf-ref} gives an intrinsic-order-open set that is not product-open.
Step [](#s1-6){.pf-ref} gives a product-open set that is not intrinsic-order-open.

:::

:::

::: {.pf-step #s1-8}

The complete comparison is
$$
\boxed{
\tau_{mathrm{prod}}
\subsetneq
\tau_{mathrm{sub}},
\qquad
\tau_{mathrm{ord}}
\subsetneq
\tau_{mathrm{sub}},
}
$$
while
$$
\boxed{
\tau_{mathrm{prod}}
\text{ and }
\tau_{mathrm{ord}}
\text{ are incomparable}.
}
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} and [](#s1-4){.pf-ref}, and [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} gives the complete relation among the three topologies.

:::

:::

:::
