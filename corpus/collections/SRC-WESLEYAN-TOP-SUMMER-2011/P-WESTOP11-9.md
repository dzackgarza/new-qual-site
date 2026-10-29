---
schema: qual/card@1
id: P-WESTOP11-9
kind: problem
title: Fundamental group of a sphere with a diameter adjoined via its simply connected cover
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $X$ be the space obtained by adjoining to $S^2$ the straight-line segment from the north pole to the south pole. Find a simply connected covering space of $X$ and use it to compute $\pi_1(X)$.
:::

::: {.solution}

Let
\[
N,S\in S^2
\]
denote the north and south poles, and let
\[
e
\]
be the additional closed interval whose endpoints are attached to $N$ and
$S$.

::: pf

::: {.pf-step #s1-1}

For every
\[
n\in\ZZ,
\]
let
\[
S_n^2
\]
be a copy of $S^2$, with poles
\[
N_n,S_n.
\]
For every $n$, attach an interval
\[
e_n
\]
from
\[
N_n
\]
to
\[
S_{n+1}.
\]
Call the resulting space
\[
\widetilde X.
\]


::: pf-proof

Thus $\widetilde X$ is a bi-infinite chain of copies of $S^2$:
\[
\cdots
S_{n-1}^2
\xrightarrow{e_{n-1}}
S_n^2
\xrightarrow{e_n}
S_{n+1}^2
\cdots,
\]
where each connecting edge runs from the north pole of one sphere to the
south pole of the next.

:::

:::

::: {.pf-step #s1-2}

Define
\[
p:\widetilde X\to X
\]
by mapping every sphere
\[
S_n^2
\]
homeomorphically onto the original sphere $S^2$, carrying
\[
N_n\mapsto N,
\qquad
S_n\mapsto S,
\]
and mapping every interval
\[
e_n
\]
homeomorphically onto the added segment $e$.


::: pf-proof

The endpoint assignments are compatible:
the initial point $N_n$ of $e_n$ maps to the initial endpoint $N$ of $e$,
and the terminal point $S_{n+1}$ maps to the terminal endpoint $S$.
Thus the maps on the cells glue to a continuous map
\[
p:\widetilde X\to X.
\]

:::

:::

::: {.pf-step #s1-3}

The map
\[
p:\widetilde X\to X
\]
is a covering map.


::: pf-proof

Away from
\[
N,S,
\]
this is immediate: every point in the interior of the sphere or the added
edge has one corresponding point in each indexed copy, and small
neighborhoods map homeomorphically.

Near $N$, choose a small disk
\[
D_N\subset S^2
\]
together with a short initial half-interval of $e$.
Its inverse image is the disjoint union, over
\[
n\in\ZZ,
\]
of the corresponding disk around $N_n$ together with a short initial
half-interval of $e_n$, each mapped homeomorphically onto the chosen
neighborhood.

Similarly, near $S$, a small disk plus a terminal half-interval of $e$ lifts
to the disjoint union of neighborhoods of the points $S_n$, each using the
terminal half of $e_{n-1}$.

Thus every point has an evenly covered neighborhood.

:::

:::

::: {.pf-step #s1-4}

The space $\widetilde X$ is path-connected.


::: pf-proof

Each sphere $S_n^2$ is path-connected.
The interval $e_n$ joins $S_n^2$ to $S_{n+1}^2$.
Thus all sphere copies lie in one path component.

:::

:::

::: {.pf-step #s1-5}

Every finite subchain
\[
Y_{m,n}
\coloneqq
S_m^2
\cup e_m
\cup S_{m+1}^2
\cup\cdots\cup
e_{n-1}
\cup S_n^2
\]
is simply connected.


::: pf-proof

Proceed by induction on
\[
n-m.
\]
For
\[
n=m,
\]
the space is a single sphere and is simply connected.

Assume
\[
Y_{m,n}
\]
is simply connected.
The next sphere
\[
S_{n+1}^2
\]
is simply connected and is attached to $Y_{m,n}$ by the interval $e_n$.
The union
\[
Y_{m,n+1}
\]
deformation retracts onto the wedge
\[
Y_{m,n}\vee S_{n+1}^2
\]
after collapsing the connecting interval to a point.
By van Kampen, the wedge of two simply connected spaces is simply
connected.
Thus the induction closes.

:::

:::

::: {.pf-step #s1-6}

The whole space
\[
\widetilde X
\]
is simply connected.


::: pf-proof

Let
\[
\gamma:S^1\to\widetilde X
\]
be a loop.
Its image is compact.
The family of open cell neighborhoods in the bi-infinite chain is locally
finite, so a compact subset meets only finitely many sphere and edge cells.
Hence
\[
\gamma(S^1)
\subseteq
Y_{m,n}
\]
for some finite subchain.
By step [](#s1-5){.pf-ref}, the loop is null-homotopic there, hence also in
\[
\widetilde X.
\]

:::

:::

::: {.pf-step #s1-7}

Therefore
\[
p:\widetilde X\to X
\]
is the universal covering space.


::: pf-proof

By steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref}, $p$ is a connected covering.
By step [](#s1-6){.pf-ref}, the total space is simply connected.
A connected simply connected covering is universal.

:::

:::

::: {.pf-step #s1-8}

Define
\[
T:\widetilde X\to\widetilde X
\]
by shifting the index:
\[
T(S_n^2)=S_{n+1}^2,
\qquad
T(e_n)=e_{n+1}.
\]
Then $T$ is a deck transformation.


::: pf-proof

By construction,
\[
p\circ T=p,
\]
because every sphere copy maps to the same sphere and every edge copy maps
to the same added interval.
The shift is a homeomorphism, with inverse the shift
\[
n\mapsto n-1.
\]
Thus it is a deck transformation.

:::

:::

::: {.pf-step #s1-9}

Every deck transformation is a power of $T$.


::: pf-proof

Fix a point
\[
x
\]
in the interior of the original sphere away from the poles.
Its fiber consists of one point
\[
x_n\in S_n^2
\]
for every
\[
n\in\ZZ.
\]

A deck transformation is determined by the image of one point in a connected
covering space.
If a deck transformation sends
\[
x_0
\]
to
\[
x_k,
\]
then
\[
T^k
\]
does the same.
Therefore the two deck transformations are equal.
Hence
\[
\operatorname{Deck}(\widetilde X/X)
=
\langle T\rangle
\cong
\ZZ.
\]

:::

:::

::: {.pf-step #s1-10}

Consequently
\[
\boxed{
\pi_1(X)\cong\ZZ.
}
\]


::: pf-proof

The space $X$ is path-connected, locally path-connected, and semilocally
simply connected, since it is a finite CW complex.
For a universal covering of such a space, the deck-transformation group is
canonically isomorphic to the fundamental group:
\[
\pi_1(X)
\cong
\operatorname{Deck}(\widetilde X/X).
\]
Apply step [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-7){.pf-ref} construct the requested simply connected covering space,
and steps [](#s1-8){.pf-ref} through [](#s1-10){.pf-ref} compute its deck group and hence
\[
\pi_1(X).
\]

:::

:::

:::
