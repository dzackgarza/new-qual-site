---
schema: qual/card@1
id: P-WESTOP07-01
kind: problem
title: Distinguish $\RR$ and $\RR^2$ from higher-dimensional Euclidean spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. Prove that $\RR$ is not homeomorphic to $\RR^n$ for any $n>1$.
2. Prove that $\RR^2$ is not homeomorphic to $\RR^n$ for any $n>2$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every
$$
n>1,
$$
the punctured space
$$
\RR^n\setminus\{0\}
$$
is path-connected.


::: pf-proof

Let
$$
x,y\in\RR^n\setminus\{0\}.
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

::: {.pf-step #s1-2}

The space
$$
\RR\setminus\{0\}
$$
is disconnected.


::: pf-proof

One has
$$
\RR\setminus\{0\}
=
(-\infty,0)
\sqcup
(0,\infty),
$$
a union of two nonempty disjoint open subsets in the subspace topology.

:::

:::

::: {.pf-step #s1-3}

For
$$
n>1,
$$
one has
$$
\boxed{
\RR
\not\cong
\RR^n}.
$$


::: pf-proof

Suppose
$$
h:\RR\to\RR^n
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
\RR\setminus\{0\}
\cong
\RR^n\setminus\{p\}.
$$
Translation identifies
$$
\RR^n\setminus\{p\}
$$
with
$$
\RR^n\setminus\{0\}.
$$
But step [](#s1-2){.pf-ref} says the first punctured space is disconnected, while step [](#s1-1){.pf-ref} says the second is path-connected. Contradiction.

:::

:::

::: {.pf-step #s1-4}

For every
$$
m\ge2,
$$
the punctured space
$$
\RR^m\setminus\{0\}
$$
deformation retracts onto
$$
S^{m-1}.
$$


::: pf-proof

Define
$$
H:
(\RR^m\setminus\{0\})\times[0,1]
\to
\RR^m\setminus\{0\}
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

::: {.pf-step #s1-5}

One has
$$
\pi_1(\RR^2\setminus\{0\})
\cong
\ZZ.
$$


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
\RR^2\setminus\{0\}
\simeq
S^1.
$$
Homotopy equivalent spaces have isomorphic fundamental groups, and
$$
\pi_1(S^1)\cong\ZZ.
$$

:::

:::

::: {.pf-step #s1-6}

For every
$$
n>2,
$$
one has
$$
\pi_1(\RR^n\setminus\{0\})
=0.
$$


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
\RR^n\setminus\{0\}
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

::: {.pf-step #s1-7}

For every
$$
n>2,
$$
one has
$$
\boxed{
\RR^2
\not\cong
\RR^n}.
$$


::: pf-proof

Suppose
$$
h:\RR^2\to\RR^n
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
\RR^2\setminus\{0\}
\cong
\RR^n\setminus\{p\}.
$$
After translating the target, the right-hand side is homeomorphic to
$$
\RR^n\setminus\{0\}.
$$
Homeomorphic spaces have isomorphic fundamental groups, contradicting steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref}:
$$
\ZZ
\not\cong
0.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (1), and step [](#s1-7){.pf-ref} proves part (2).

:::

:::

:::
