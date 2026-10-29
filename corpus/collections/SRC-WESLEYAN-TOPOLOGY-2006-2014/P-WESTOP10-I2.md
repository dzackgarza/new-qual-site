---
schema: qual/card@1
id: P-WESTOP10-I2
kind: problem
title: Point-set properties of $\RR^n$ and the closed long ray
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
For each of the spaces $\RR^n$ and $\overline{S_\Omega}$, determine which of the following properties hold, and justify each answer:

1. connected;
2. path-connected;
3. compact;
4. Hausdorff;
5. completely regular;
6. normal;
7. metrizable.
:::

::: {.solution}

Assume
$$
n\ge1.
$$
Write
$$
\overline{S_\Omega}
$$
for the closed long ray, obtained from the long ray
$$
S_\Omega
=
\omega_1\times[0,1)
$$
with lexicographic order by adjoining its final endpoint
$$
\Omega.
$$

::: pf

::: {.pf-step #s1-1}

The Euclidean space
$$
\RR^n
$$
is path-connected, hence connected.


::: pf-proof

For
$$
x,y\in\RR^n,
$$
the straight-line path
$$
\gamma(t)
=
(1-t)x+ty,
\qquad
0\le t\le1,
$$
is continuous and joins $x$ to $y$.
Thus
$$
\RR^n
$$
is path-connected.
Every path-connected space is connected.

:::

:::

::: {.pf-step #s1-2}

The space
$$
\RR^n
$$
is not compact.


::: pf-proof

It is unbounded.
By the Heine--Borel theorem, a subset of Euclidean space is compact if and
only if it is closed and bounded.
Thus
$$
\RR^n
$$
is not compact.

Equivalently, the open cover
$$
\{B(0,m):m\in\NN\}
$$
has no finite subcover.

:::

:::

::: {.pf-step #s1-3}

The space
$$
\RR^n
$$
is Hausdorff, completely regular, normal, and metrizable.


::: pf-proof

The Euclidean metric
$$
d(x,y)
=
\left(
\sum_{j=1}^n
(x_j-y_j)^2
\right)^{1/2}
$$
induces the usual topology.
Every metric space is Hausdorff, completely regular, and normal.
Thus all four properties hold.

:::

:::

::: {.pf-step #s1-4}

Therefore, for
$$
n\ge1,
$$
the classification of
$$
\RR^n
$$
is
$$
\boxed{
\begin{array}{c|ccccccc}
&\text{connected}
&\text{path-connected}
&\text{compact}
&\text{Hausdorff}
&\text{completely regular}
&\text{normal}
&\text{metrizable}\\
\hline
\RR^n
&\mathrm{yes}
&\mathrm{yes}
&\mathrm{no}
&\mathrm{yes}
&\mathrm{yes}
&\mathrm{yes}
&\mathrm{yes}
\end{array}
}
$$


::: pf-proof

Collect steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

The closed long ray
$$
\overline{S_\Omega}
$$
is a linearly ordered topological space whose order is order-complete and
densely ordered between distinct nonconsecutive points.


::: pf-proof

The lexicographic order on
$$
\omega_1\times[0,1)
$$
is a linear order.
Adjoining the final point
$$
\Omega
$$
gives both a first and a last endpoint.

Every nonempty subset bounded above has a least upper bound:
take the least ordinal coordinate above all coordinates occurring in the
set, and within the final relevant fiber take the usual real supremum.
If the set is cofinal in the long ray, its supremum is the added point
$$
\Omega.
$$

Between two points with distinct ordinal coordinates there is always a
point in the earlier vertical fiber with slightly larger second coordinate;
within one fiber this is just density of
$$
[0,1)
$$
in its usual order.

:::

:::

::: {.pf-step #s1-6}

The closed long ray is connected.


::: pf-proof

A linearly ordered set with the order topology is connected whenever it is a
linear continuum: it has the least-upper-bound property and no gaps.
Step [](#s1-5){.pf-ref} gives precisely these properties.
Hence
$$
\boxed{
\overline{S_\Omega}
\text{ is connected}.
}
$$

:::

:::

::: {.pf-step #s1-7}

The closed long ray is not path-connected.


::: pf-proof

Suppose there were a path
$$
\gamma:[0,1]\to\overline{S_\Omega}
$$
from some point
$$
x<\Omega
$$
to
$$
\Omega.
$$
The image
$$
K
=
\gamma([0,1])
$$
is connected because $[0,1]$ is connected.

Connected subsets of a linearly ordered topological space are convex.
Since $K$ contains both
$$
x
\quad\text{and}\quad
\Omega,
$$
it must contain the whole interval
$$
[x,\Omega].
$$

But
$$
\gamma([0,1])
$$
is a continuous image of the separable space $[0,1]$, hence is separable.
The interval
$$
[x,\Omega]
$$
is not separable:
for any countable subset, the set of ordinal coordinates occurring in it
has countable supremum
$$
\beta<\omega_1,
$$
so the open tail above a point with first coordinate greater than $\beta$
misses that countable set.
Thus no countable subset can be dense in
$$
[x,\Omega].
$$
Contradiction.

Hence no point below $\Omega$ can be joined to $\Omega$ by a path.
Therefore
$$
\boxed{
\overline{S_\Omega}
\text{ is not path-connected}.
}
$$

:::

:::

::: {.pf-step #s1-8}

The closed long ray is compact.


::: pf-proof

A complete linear order with both endpoints is compact in its order
topology.
By step [](#s1-5){.pf-ref},
$$
\overline{S_\Omega}
$$
is order-complete and has both a first point and the last point
$$
\Omega.
$$
Therefore
$$
\boxed{
\overline{S_\Omega}
\text{ is compact}.
}
$$

:::

:::

::: {.pf-step #s1-9}

The closed long ray is Hausdorff and normal.


::: pf-proof

Every linearly ordered topological space is Hausdorff.
Moreover, every linearly ordered topological space is hereditarily normal
(indeed, monotonically normal).
Therefore
$$
\overline{S_\Omega}
$$
is both Hausdorff and normal.

:::

:::

::: {.pf-step #s1-10}

The closed long ray is completely regular.


::: pf-proof

A normal $T_1$ space is completely regular by Urysohn's lemma:
given a point
$$
x
$$
and a closed set
$$
F
$$
not containing it, normality separates
$$
\{x\}
\quad\text{and}\quad
F
$$
by a continuous function
$$
u:X\to[0,1].
$$

By step [](#s1-9){.pf-ref}, the closed long ray is Hausdorff, hence $T_1$, and normal.
Thus it is completely regular.

:::

:::

::: {.pf-step #s1-11}

The endpoint
$$
\Omega
$$
has no countable local base.


::: pf-proof

Suppose
$$
U_1,U_2,\dots
$$
were a countable local base at $\Omega$.
For each $n$, because $U_n$ is a neighborhood of the final point, choose
$$
a_n<\Omega
$$
such that
$$
(a_n,\Omega]
\subseteq
U_n.
$$

The set of ordinal coordinates appearing among the countably many $a_n$ has
countable supremum, so there is a point
$$
b<\Omega
$$
strictly above every $a_n$.
Then
$$
(b,\Omega]
$$
is a neighborhood of $\Omega$.

If the $U_n$ formed a local base, some $U_n$ would satisfy
$$
U_n
\subseteq
(b,\Omega].
$$
But
$$
(a_n,\Omega]
\subseteq
U_n,
$$
and since
$$
a_n<b,
$$
the tail
$$
(a_n,\Omega]
$$
contains points at or below $b$ and therefore is not contained in
$$
(b,\Omega].
$$
Contradiction.

:::

:::

::: {.pf-step #s1-12}

The closed long ray is not metrizable.


::: pf-proof

Every metric space is first countable.
Step [](#s1-11){.pf-ref} shows that
$$
\overline{S_\Omega}
$$
is not first countable at its endpoint.
Hence it cannot be metrizable.

:::

:::

::: {.pf-step #s1-13}

Therefore the classification of the closed long ray is
$$
\boxed{
\begin{array}{c|ccccccc}
&\text{connected}
&\text{path-connected}
&\text{compact}
&\text{Hausdorff}
&\text{completely regular}
&\text{normal}
&\text{metrizable}\\
\hline
\overline{S_\Omega}
&\mathrm{yes}
&\mathrm{no}
&\mathrm{yes}
&\mathrm{yes}
&\mathrm{yes}
&\mathrm{yes}
&\mathrm{no}
\end{array}
}
$$


::: pf-proof

Combine steps [](#s1-6){.pf-ref} through [](#s1-12){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} and [](#s1-13){.pf-ref} give all requested properties of the two spaces.

:::

:::

:::
