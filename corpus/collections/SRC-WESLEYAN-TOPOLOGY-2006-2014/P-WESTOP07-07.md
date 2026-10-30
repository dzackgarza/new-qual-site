---
schema: qual/card@1
id: P-WESTOP07-07
kind: problem
title: Second countability, the Sorgenfrey line, and cardinality of continuous functions
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. Prove that every second-countable topological space is separable.
2. Prove that the Sorgenfrey line $\RR_\ell$ is separable but not second countable.
3. If $X$ is separable, prove that there are at most $\mathfrak c$ continuous maps $X\to\RR$, where $\mathfrak c=\cardinality{\RR}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every second-countable space is separable.


::: pf-proof

Let
$$
\mathcal B
=
\{B_1,B_2,\ldots\}
$$
be a countable base for
$$
X.
$$
For every nonempty
$$
B_n,
$$
choose one point
$$
x_n\in B_n.
$$
Let
$$
D
\coloneqq
\{x_n:
B_n\ne\varnothing\}.
$$
Then
$$
D
$$
is countable.

To show that
$$
D
$$
is dense, let
$$
U\subseteq X
$$
be a nonempty open set. Choose
$$
x\in U.
$$
Since
$$
\mathcal B
$$
is a base, some
$$
B_n
$$
satisfies
$$
x\in B_n\subseteq U.
$$
Then
$$
x_n\in B_n\subseteq U,
$$
so every nonempty open set meets
$$
D.
$$
Hence
$$
\overline D=X.
$$

:::

:::

::: {.pf-step #s1-2}

The Sorgenfrey line
$$
\RR_\ell
$$
is separable.


::: pf-proof

Recall that a basis for
$$
\RR_\ell
$$
consists of the half-open intervals
$$
[a,b),
\qquad
a<b.
$$
Every such interval contains a rational number. Therefore
$$
\QQ
$$
meets every nonempty basic open set, hence is dense in
$$
\RR_\ell.
$$
Thus the Sorgenfrey line is separable.

:::

:::

::: {.pf-step #s1-3}

The Sorgenfrey line is not second countable.


::: pf-proof

Suppose
$$
\mathcal B
=
\{B_1,B_2,\ldots\}
$$
were a countable base.

For each
$$
x\in\RR,
$$
the set
$$
[x,x+1)
$$
is an open neighborhood of
$$
x.
$$
Let
$$
n(x)
$$
be the least positive integer
$$
n
$$
such that
$$
x\in B_n\subseteq[x,x+1).
$$
Such an integer exists by the base property.

The map
$$
x\longmapsto n(x)
$$
is injective. Indeed, suppose
$$
x<y
$$
and
$$
n(x)=n(y)=n.
$$
Then
$$
y\in B_n
$$
and
$$
B_n\subseteq[x,x+1),
$$
while also
$$
x\in B_n
$$
and
$$
B_n\subseteq[y,y+1).
$$
But
$$
x<y
$$
implies
$$
x\notin[y,y+1),
$$
a contradiction.

Thus there would be an injection
$$
\RR\hookrightarrow\NN,
$$
which is impossible. Hence
$$
\RR_\ell
$$
is not second countable.

:::

:::

::: {.pf-step #s1-4}

Let
$$
X
$$
be separable and choose a countable dense set
$$
D\subseteq X.
$$
Two continuous maps
$$
f,g:X\to\RR
$$
that agree on
$$
D
$$
agree on all of
$$
X.
$$


::: pf-proof

Consider the map
$$
(f,g):X\to\RR^2.
$$
The diagonal
$$
\Delta
=
\{
(r,r):
r\in\RR
\}
$$
is closed in
$$
\RR^2.
$$
Hence the equalizer
$$
E
\coloneqq
\{
x\in X:
f(x)=g(x)
\}
=
(f,g)^{-1}(\Delta)
$$
is closed in
$$
X.
$$
If
$$
f\restrict_D=g\restrict_D,
$$
then
$$
D\subseteq E.
$$
Since
$$
D
$$
is dense and
$$
E
$$
is closed,
$$
E=X.
$$
Thus
$$
f=g.
$$

:::

:::

::: {.pf-step #s1-5}

Restriction to
$$
D
$$
defines an injection
$$
\boxed{
C(X,\RR)
\hookrightarrow
\RR^D}.
$$


::: pf-proof

Define
$$
R:
C(X,\RR)
\to
\RR^D
$$
by
$$
R(f)=f\restrict_D.
$$
Step [](#s1-4){.pf-ref} says that
$$
R(f)=R(g)
$$
implies
$$
f=g.
$$
Hence
$$
R
$$
is injective.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\cardinality{\RR^D}
\le
\mathfrak c.
$$


::: pf-proof

If
$$
D
$$
is finite, then
$$
\cardinality{\RR^D}
=
\mathfrak c.
$$
If
$$
D
$$
is countably infinite, then
$$
\cardinality{\RR^D}
=
\mathfrak c^{\aleph_0}.
$$
Since
$$
\mathfrak c
=
2^{\aleph_0},
$$
cardinal arithmetic gives
$$
\mathfrak c^{\aleph_0}
=
(2^{\aleph_0})^{\aleph_0}
=
2^{\aleph_0\cdot\aleph_0}
=
2^{\aleph_0}
=
\mathfrak c.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
\cardinality{C(X,\RR)}
\le
\mathfrak c}
$$
for every separable space
$$
X.
$$


::: pf-proof

Combine the injection from step [](#s1-5){.pf-ref} with the cardinal bound from step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part (1), steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} prove part (2), and steps [](#s1-4){.pf-ref} through [](#s1-7){.pf-ref} prove part (3).

:::

:::

:::
