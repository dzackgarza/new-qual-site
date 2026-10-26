---
schema: qual/card@1
id: P-WESTOP07-01
kind: problem
title: Distinguish $\mathbb R$ and $\mathbb R^2$ from higher-dimensional Euclidean spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. Prove that $\mathbb R$ is not homeomorphic to $\mathbb R^n$ for any $n>1$.
2. Prove that $\mathbb R^2$ is not homeomorphic to $\mathbb R^n$ for any $n>2$.
:::

::: pf

::: pf-step

For every
$$
n>1,
$$
the punctured space
$$
\mathbb R^n\setminus\{0\}
$$
is path-connected.


::: pf-proof

Let
$$
x,y\in\mathbb R^n\setminus\{0\}.
$$
If the line segment from
$$
x
$$
to
$$
y
$$
does not pass through the origin, it is a path in the punctured space.

If the segment does pass through the origin, then
$$
x
$$
and
$$
y
$$
lie on the same line through the origin on opposite sides. Since
$$
n>1,
$$
choose a point
$$
z
$$
not lying on that line. Then neither segment
$$
[x,z]
$$
nor
$$
[z,y]
$$
passes through the origin. Concatenating the two segments gives a path from
$$
x
$$
to
$$
y
$$
inside the punctured space.

:::

:::

::: pf-step

The space
$$
\mathbb R\setminus\{0\}
$$
is disconnected.


::: pf-proof

One has
$$
\mathbb R\setminus\{0\}
=
(-\infty,0)
\sqcup
(0,\infty),
$$
a union of two nonempty disjoint open subsets in the subspace topology.

:::

:::

::: pf-step

For
$$
n>1,
$$
one has
$$
\boxed{
\mathbb R
\not\cong
\mathbb R^n}.
$$


::: pf-proof

Suppose
$$
h:\mathbb R\to\mathbb R^n
$$
were a homeomorphism. Let
$$
p=h(0).
$$
Restricting
$$
h
$$
would give a homeomorphism
$$
\mathbb R\setminus\{0\}
\cong
\mathbb R^n\setminus\{p\}.
$$
Translation identifies
$$
\mathbb R^n\setminus\{p\}
$$
with
$$
\mathbb R^n\setminus\{0\}.
$$
But step <1>2 says the first punctured space is disconnected, while step <1>1 says the second is path-connected. Contradiction.

:::

:::

::: pf-step

For every
$$
m\ge2,
$$
the punctured space
$$
\mathbb R^m\setminus\{0\}
$$
deformation retracts onto
$$
S^{m-1}.
$$


::: pf-proof

Define
$$
H:
(\mathbb R^m\setminus\{0\})\times[0,1]
\to
\mathbb R^m\setminus\{0\}
$$
by
$$
H(x,t)
=
\left(
(1-t)+\frac{t}{\|x\|}
\right)x.
$$
At
$$
t=0
$$
this is
$$
x.
$$
At
$$
t=1
$$
it is
$$
x/\|x\|
\in
S^{m-1}.
$$
If
$$
x\in S^{m-1},
$$
then
$$
H(x,t)=x
$$
for all
$$
t.
$$
The scalar factor is always positive, so the homotopy never passes through the origin. Thus this is a strong deformation retraction.

:::

:::

::: pf-step

One has
$$
\pi_1(\mathbb R^2\setminus\{0\})
\cong
\mathbb Z.
$$


::: pf-proof

By step <1>4,
$$
\mathbb R^2\setminus\{0\}
\simeq
S^1.
$$
Homotopy equivalent spaces have isomorphic fundamental groups, and
$$
\pi_1(S^1)\cong\mathbb Z.
$$

:::

:::

::: pf-step

For every
$$
n>2,
$$
one has
$$
\pi_1(\mathbb R^n\setminus\{0\})
=0.
$$


::: pf-proof

By step <1>4,
$$
\mathbb R^n\setminus\{0\}
\simeq
S^{n-1}.
$$
Since
$$
n-1\ge2,
$$
the sphere
$$
S^{n-1}
$$
is simply connected. Therefore the punctured Euclidean space has trivial fundamental group.

:::

:::

::: pf-step

For every
$$
n>2,
$$
one has
$$
\boxed{
\mathbb R^2
\not\cong
\mathbb R^n}.
$$


::: pf-proof

Suppose
$$
h:\mathbb R^2\to\mathbb R^n
$$
were a homeomorphism, and set
$$
p=h(0).
$$
Then
$$
h
$$
would restrict to a homeomorphism
$$
\mathbb R^2\setminus\{0\}
\cong
\mathbb R^n\setminus\{p\}.
$$
After translating the target, the right-hand side is homeomorphic to
$$
\mathbb R^n\setminus\{0\}.
$$
Homeomorphic spaces have isomorphic fundamental groups, contradicting steps <1>5--<1>6:
$$
\mathbb Z
\not\cong
0.
$$

:::

:::

::: pf-qed

Step <1>3 proves part (1), and step <1>7 proves part (2).

:::

:::
