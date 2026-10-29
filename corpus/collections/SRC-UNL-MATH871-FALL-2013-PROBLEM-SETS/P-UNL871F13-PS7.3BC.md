---
schema: qual/card@1
id: P-UNL871F13-PS7.3BC
kind: problem
title: Components of excluded-point and included-point real lines
classification:
  areas: [topology]
  topics: [Connectedness]
relations: []
review: draft
---

::: {.problem}
For each of the following topologies on the underlying set $\RR$, determine whether the resulting space is connected or path-connected, and determine its connected components and path components.

1. The excluded-point topology (with excluded point $0$).

2. The included-point topology (with included point $0$).
:::

::: {.solution}

::: pf

::: pf-step

In the excluded-point topology with excluded point $0$, the open sets
are
$$
\RR
$$
and all subsets of
$$
\RR\setminus\{0\}.
$$


::: pf-proof

This is the definition of the excluded-point topology.
Equivalently, every subset not containing $0$ is open, while the only open
set containing $0$ is the whole space.

:::

:::

::: {.pf-step #s1-2}

Let
$$
x,y\in\RR
$$
be distinct nonzero points.
Define
$$
\gamma:[0,1]\to\RR
$$
by
$$
\gamma(t)
=
\begin{cases}
x,&0\le t<\frac12,\\
0,&t=\frac12,\\
y,&\frac12<t\le1.
\end{cases}
$$
Then $\gamma$ is continuous for the excluded-point topology.


::: pf-proof

Let
$$
U
$$
be open.

If
$$
0\in U,
$$
then by the excluded-point topology
$$
U=\RR,
$$
so
$$
\gamma^{-1}(U)
=
[0,1].
$$

If
$$
0\notin U,
$$
then the preimage is determined only by whether $x$ and $y$ belong to $U$.
Thus it is one of
$$
\varnothing,
\qquad
\left[0,\frac12\right),
\qquad
\left(\frac12,1\right],
\qquad
\left[0,\frac12\right)
\cup
\left(\frac12,1\right].
$$
Each is open in the subspace topology on
$$
[0,1].
$$
Therefore $\gamma$ is continuous.

:::

:::

::: {.pf-step #s1-3}

Every nonzero point can also be joined to $0$ by a path.


::: pf-proof

For
$$
x\ne0,
$$
define
$$
\eta(t)
=
\begin{cases}
x,&0\le t<1,\\
0,&t=1.
\end{cases}
$$
If $U$ is open and does not contain $0$, then
$$
\eta^{-1}(U)
$$
is either
$$
\varnothing
$$
or
$$
[0,1),
$$
both open in $[0,1]$.
If $0\in U$, then
$$
U=\RR
$$
and the preimage is all of $[0,1]$.
Thus $\eta$ is continuous.

:::

:::

::: {.pf-step #s1-4}

Hence the excluded-point real line is path-connected.


::: pf-proof

If both endpoints are nonzero, use step [](#s1-2){.pf-ref}.
If one endpoint is $0$, use step [](#s1-3){.pf-ref} or reverse that path.
Thus every two points can be joined by a path.

:::

:::

::: {.pf-step #s1-5}

Therefore, in the excluded-point topology,
$$
\boxed{
\text{there is exactly one path component and exactly one connected component, namely }\RR.
}
$$


::: pf-proof

Path-connected spaces are connected.
By step [](#s1-4){.pf-ref}, the whole space is path-connected, so it is itself the unique
path component and therefore also the unique connected component.

:::

:::

::: pf-step

In the included-point topology with included point $0$, the open sets
are
$$
\varnothing
$$
and all subsets containing $0$.


::: pf-proof

This is the definition of the included-point topology.

:::

:::

::: {.pf-step #s1-7}

Let
$$
x,y\in\RR.
$$
Define
$$
\gamma:[0,1]\to\RR
$$
by
$$
\gamma(t)
=
\begin{cases}
x,&t=0,\\
0,&0<t<1,\\
y,&t=1.
\end{cases}
$$
Then $\gamma$ is continuous for the included-point topology.


::: pf-proof

Let
$$
U
$$
be open.
If
$$
U=\varnothing,
$$
then the preimage is empty.

Otherwise
$$
0\in U.
$$
Depending on whether $x$ and $y$ lie in $U$, the preimage is one of
$$
(0,1),
\qquad
[0,1),
\qquad
(0,1],
\qquad
[0,1].
$$
Each is open in the subspace topology on $[0,1]$.
Hence $\gamma$ is continuous.

:::

:::

::: {.pf-step #s1-8}

Therefore the included-point real line is path-connected.


::: pf-proof

Step [](#s1-7){.pf-ref} constructs a path between arbitrary
$$
x,y\in\RR.
$$

:::

:::

::: {.pf-step #s1-9}

Consequently, in the included-point topology,
$$
\boxed{
\text{there is exactly one path component and exactly one connected component, namely }\RR.
}
$$


::: pf-proof

As in step [](#s1-5){.pf-ref}, path-connectedness implies connectedness, and the whole
space is the unique component of each type.

:::

:::

::: {.pf-step #s1-10}

The complete answer is:
$$
\boxed{
\begin{array}{c|cc|cc}
&\text{connected}
&\text{path-connected}
&\text{connected components}
&\text{path components}\\
\hline
\text{excluded-point}
&\mathrm{yes}
&\mathrm{yes}
&\RR
&\RR\\
\text{included-point}
&\mathrm{yes}
&\mathrm{yes}
&\RR
&\RR
\end{array}
}
$$


::: pf-proof

Collect steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} and [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} gives all requested classifications.

:::

:::

:::
