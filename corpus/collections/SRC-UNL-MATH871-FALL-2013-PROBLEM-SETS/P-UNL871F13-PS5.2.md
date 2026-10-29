---
schema: qual/card@1
id: P-UNL871F13-PS5.2
kind: problem
title: Composition, products, and corestrictions of open maps
classification:
  areas: [topology]
  topics: [Product Topology, Continuity]
relations: []
review: draft
---

::: {.problem}
1. Show that a composition of open maps is open.

2. Show that a finite product of open maps is open.
   Determine whether the corresponding assertion is true for an infinite product.

3. Suppose $f:X\to Y$ is open and $f(X)\subseteq B\subseteq Y$.
   Show that the corestriction
   $$
   f^B:X\to B
   $$
   is open when $B$ has the subspace topology.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A composition of open maps is open.


::: pf-proof

Let
$$
f:X\to Y,
\qquad
g:Y\to Z
$$
be open maps.
Let
$$
U\subseteq X
$$
be open.
Since $f$ is open,
$$
f(U)
$$
is open in $Y$.
Since $g$ is open,
$$
g(f(U))
$$
is open in $Z$.
But
$$
(g\circ f)(U)
=
g(f(U)).
$$
Thus
$$
g\circ f
$$
is open.

:::

:::

::: {.pf-step #s1-2}

Let
$$
f_i:X_i\to Y_i,
\qquad
1\le i\le n,
$$
be open maps.
Then the product map
$$
F
\coloneqq
\prod_{i=1}^n f_i:
\prod_{i=1}^nX_i
\to
\prod_{i=1}^nY_i
$$
is open.


::: pf-proof

It suffices to check a basis for the finite product topology.
Let
$$
U
=
U_1\times\cdots\times U_n,
$$
where every
$$
U_i\subseteq X_i
$$
is open.
Then
$$
F(U)
=
f_1(U_1)
\times\cdots\times
f_n(U_n).
$$
Each
$$
f_i(U_i)
$$
is open in $Y_i$ because $f_i$ is open.
Hence
$$
F(U)
$$
is open in the finite product.

An arbitrary open subset of the domain is a union of such basis elements,
and images commute with unions.
Therefore $F$ is open.

:::

:::

::: {.pf-step #s1-3}

The corresponding assertion is false for an infinite product.


::: pf-proof

For every
$$
n\in\NN,
$$
let
$$
X_n=(0,1),
\qquad
Y_n=\RR,
$$
and let
$$
f_n:X_n\hookrightarrow Y_n
$$
be the inclusion.

Each $f_n$ is open.
Indeed, every open subset of the subspace $(0,1)$ is open in
$\RR$, because $(0,1)$ itself is open in $mathbb R$.

Consider the product map
$$
F
=
\prod_{n=1}^{\infty}f_n:
(0,1)^{\NN}
\longrightarrow
\RR^{\NN}.
$$
The whole domain
$$
(0,1)^{\NN}
$$
is open in itself.
Its image is
$$
F\bigl((0,1)^{\NN}\bigr)
=
(0,1)^{\NN}.
$$

We claim this subset is not open in the product topology of
$$
\RR^{\NN}.
$$
Take, for example,
$$
x
=
\left(
\frac12,\frac12,\frac12,\dots
\right).
$$
Every basic product neighborhood of $x$ restricts only finitely many
coordinates.
Thus there exists some unrestricted coordinate
$$
m
$$
for which the neighborhood contains a point whose $m$th coordinate is,
say,
$$
2.
$$
That point does not lie in
$$
(0,1)^{\NN}.
$$
Hence no basic neighborhood of $x$ is contained in the image.

Therefore $F$ is not an open map.

:::

:::

::: {.pf-step #s1-4}

Suppose
$$
f:X\to Y
$$
is open and
$$
f(X)\subseteq B\subseteq Y.
$$
Then the corestriction
$$
f^B:X\to B
$$
is open.


::: pf-proof

Let
$$
U\subseteq X
$$
be open.
Since $f$ is open,
$$
f(U)
$$
is open in $Y$.
Moreover,
$$
f(U)
\subseteq
f(X)
\subseteq
B.
$$
Thus
$$
f^B(U)
=
f(U)
=
B\cap f(U).
$$
Because $f(U)$ is open in $Y$, the intersection
$$
B\cap f(U)
$$
is open in the subspace topology on $B$.
Therefore $f^B$ is open.

:::

:::

::: {.pf-step #s1-5}

The complete answer is:

1. compositions of open maps are open;
2. finite products of open maps are open;
3. infinite products of open maps need not be open;
4. corestriction to a subspace containing the image preserves openness.


::: pf-proof

This is exactly steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} settle every part of the problem.

:::

:::

:::
