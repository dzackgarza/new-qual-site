---
schema: qual/card@1
id: P-WESTOP07-09
kind: problem
title: The Moore plane is separable and Hausdorff but not normal
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let
\[
X=\{(p,q)\in\RR^2:q\ge0\}.
\]
Define a basis consisting of ordinary open disks $B((p,q);\varepsilon)$ with $0<\varepsilon<q$, together with sets
\[
B((p,q);q)\cup\{(p,0)\}
\]
whose disk is tangent to the $x$-axis at $(p,0)$.

1. Prove that these sets form a basis for a topology on $X$.
2. Prove that
   \[
   C=\{(p,q):q>0,\ p,q\in\QQ\}
   \]
   is dense, hence $X$ is separable.
3. Prove that the $x$-axis is a closed subspace whose subspace topology is discrete.
4. State the Tietze Extension Theorem and use it to prove that $X$ is not normal.
:::

::: {.solution}

For
$$
p\in\RR,
\qquad
r>0,
$$
write
$$
U(p,r)
\coloneqq
\{(p,0)\}
\cup
B((p,r);r),
$$
where the Euclidean disk
$$
B((p,r);r)
$$
is tangent to the $x$-axis at
$$
(p,0).
$$

::: pf

::: {.pf-step #s1-1}

Every point of $X$ belongs to at least one of the stated basic sets.


::: pf-proof

If
$$
(p,q)\in X
$$
has
$$
q>0,
$$
then for any
$$
0<\varepsilon<q,
$$
the Euclidean disk
$$
B((p,q);\varepsilon)
$$
lies in $X$ and contains the point.

If
$$
q=0,
$$
then
$$
(p,0)\in U(p,r)
$$
for every
$$
r>0.
$$

:::

:::

::: {.pf-step #s1-2}

If an interior point
$$
x=(a,b),
\qquad
b>0,
$$
lies in the intersection of two stated basic sets, then there is an ordinary basic disk
$$
B(x;\delta)
$$
contained in that intersection.


::: pf-proof

Every stated basic set is Euclidean open at each of its points of positive height.

For an ordinary disk this is immediate.

For a tangent basic neighborhood
$$
U(p,r),
$$
the only non-Euclidean-open point is the boundary point
$$
(p,0).
$$
Every point of positive height in
$$
U(p,r)
$$
lies in the Euclidean-open disk
$$
B((p,r);r).
$$

Thus each of the two basic neighborhoods contains some Euclidean disk about
$$
x.
$$
Taking a sufficiently small radius
$$
\delta<b
$$
gives an allowed ordinary basic disk contained in their intersection.

:::

:::

::: {.pf-step #s1-3}

If a boundary point
$$
(p,0)
$$
lies in the intersection of two stated basic sets, then some tangent neighborhood
$$
U(p,r)
$$
is contained in their intersection.


::: pf-proof

An ordinary basic disk contains no point of the $x$-axis. Hence both basic sets containing
$$
(p,0)
$$
must be tangent neighborhoods based at that same point:
$$
U(p,r_1),
\qquad
U(p,r_2).
$$

For
$$
0<r\le r_i,
$$
one has
$$
U(p,r)\subseteq U(p,r_i).
$$
Indeed,
$$
(x,y)\in B((p,r);r)
$$
is equivalent to
$$
(x-p)^2+y^2<2ry.
$$
If
$$
r\le r_i,
$$
then
$$
2ry\le2r_i y,
$$
so the same point lies in
$$
B((p,r_i);r_i).
$$

Taking
$$
r=\min\{r_1,r_2\}
$$
gives
$$
U(p,r)
\subseteq
U(p,r_1)\cap U(p,r_2).
$$

:::

:::

::: {.pf-step #s1-4}

The stated family is a basis for a topology on $X$.


::: pf-proof

Step [](#s1-1){.pf-ref} gives the first basis axiom: every point lies in some basis element.

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} give the second basis axiom: whenever a point lies in the intersection of two basis elements, there is a third basis element containing that point and contained in the intersection.

Therefore the stated family is a basis.

:::

:::

::: {.pf-step #s1-5}

The set
$$
C
\coloneqq
\{(p,q):q>0, p,q\in\QQ\}
$$
meets every nonempty basic open set.


::: pf-proof

An ordinary basic disk lies entirely in the open upper half-plane and is a nonempty Euclidean-open subset of
$$
\RR^2.
$$
Since
$$
\QQ^2
$$
is Euclidean dense, the disk contains a point of
$$
C.
$$

A tangent basic neighborhood
$$
U(p,r)
$$
contains the nonempty Euclidean-open disk
$$
B((p,r);r),
$$
which lies in the region
$$
q>0.
$$
Again Euclidean density of
$$
\QQ^2
$$
gives a point of
$$
C
$$
inside that disk.

:::

:::

::: {.pf-step #s1-6}

The set $C$ is dense in $X$, so $X$ is separable.


::: pf-proof

By step [](#s1-5){.pf-ref} every nonempty basic open set meets
$$
C.
$$
Hence every nonempty open set meets
$$
C,
$$
which is exactly
$$
\overline C=X.
$$
The set
$$
C
$$
is countable because
$$
\QQ^2
$$
is countable.

:::

:::

::: {.pf-step #s1-7}

Let
$$
A
\coloneqq
\RR\times\{0\}.
$$
Then $A$ is closed in $X$.


::: pf-proof

Its complement is
$$
X\setminus A
=
\{(p,q):q>0\}.
$$
For every point
$$
(p,q)
$$
in this complement, choose
$$
0<\varepsilon<q.
$$
Then
$$
B((p,q);\varepsilon)
$$
is a basic neighborhood contained in
$$
X\setminus A.
$$
Thus the complement is open.

:::

:::

::: {.pf-step #s1-8}

The subspace topology on $A$ is discrete.


::: pf-proof

For every
$$
p\in\RR
$$
and every
$$
r>0,
$$
the tangent neighborhood satisfies
$$
U(p,r)\cap A
=
\{(p,0)\}.
$$
Hence every singleton in
$$
A
$$
is open in the subspace topology.

:::

:::

::: {.pf-step #s1-9}

The Tietze Extension Theorem states: if $Y$ is normal, $F\subseteq Y$ is closed, and
$$
u:F\to[-1,1]
$$
is continuous, then there is a continuous extension
$$
U:Y\to[-1,1]
$$
with
$$
U|_F=u.
$$


::: pf-proof

This is the bounded real-valued form of the Tietze Extension Theorem, sufficient for the present application.

:::

:::

::: {.pf-step #s1-10}

There are
$$
2^{\mathfrak c}
$$
continuous functions
$$
u:A\to\{0,1\},
$$
where
$$
\mathfrak c=|\RR|.
$$


::: pf-proof

By step [](#s1-8){.pf-ref},
$$
A
$$
is discrete. Therefore every function
$$
A\to\{0,1\}
$$
is continuous.

Since
$$
|A|=\mathfrak c,
$$
the number of such functions is
$$
2^{|A|}
=
2^{\mathfrak c}.
$$

:::

:::

::: {.pf-step #s1-11}

There are at most
$$
\mathfrak c
$$
continuous functions
$$
X\to\RR.
$$


::: pf-proof

By step [](#s1-6){.pf-ref}, choose a countable dense subset
$$
D\subseteq X.
$$
If two continuous real-valued functions agree on
$$
D,
$$
then they agree on all of
$$
X,
$$
because
$$
\RR
$$
is Hausdorff and the equalizer of two continuous maps to a Hausdorff space is closed.

Thus restriction gives an injection
$$
C(X,\RR)
\hookrightarrow
\RR^D.
$$
Since
$$
D
$$
is countable,
$$
|\RR^D|
=
\mathfrak c^{\aleph_0}
=
\mathfrak c.
$$
Therefore
$$
|C(X,\RR)|
\le
\mathfrak c.
$$

:::

:::

::: {.pf-step #s1-12}

The space $X$ is not normal.


::: pf-proof

Suppose, toward a contradiction, that
$$
X
$$
were normal.

By step [](#s1-7){.pf-ref},
$$
A
$$
is closed. By step [](#s1-10){.pf-ref}, there are
$$
2^{\mathfrak c}
$$
continuous maps
$$
u:A\to\{0,1\}
\subseteq
[-1,1].
$$
Tietze's theorem would extend every one of them to a continuous function
$$
U:X\to[-1,1].
$$

Distinct functions on
$$
A
$$
have distinct extensions, because an extension remembers its restriction to
$$
A.
$$
Thus
$$
X
$$
would admit at least
$$
2^{\mathfrak c}
$$
continuous real-valued functions.

But step [](#s1-11){.pf-ref} shows that it admits at most
$$
\mathfrak c
$$
such functions. Cantor's theorem gives
$$
2^{\mathfrak c}
>
\mathfrak c,
$$
a contradiction.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (1), step [](#s1-6){.pf-ref} proves part (2), steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref} prove part (3), and steps [](#s1-9){.pf-ref} through [](#s1-12){.pf-ref} prove part (4).

:::

:::

:::
