---
schema: qual/card@1
id: P-WESTOP11-7
kind: problem
title: A Hausdorff space with a clopen basis is totally disconnected
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Suppose $X$ is Hausdorff and has a basis consisting of sets that are both open and closed. Show that $X$ is totally disconnected; that is, every connected subset of $X$ consists of one point.
:::

::: {.solution}

Let
$$
C\subseteq X
$$
be connected.

::: pf

::: pf-step

Suppose, toward a contradiction, that $C$ contains two distinct
points
$$
x\ne y.
$$


::: pf-proof

To prove total disconnectedness it suffices to show that no connected subset
can contain two distinct points.

:::

:::

::: pf-step

There exists an open set
$$
U\subseteq X
$$
such that
$$
x\in U
\qquad\text{and}\qquad
y\notin U.
$$


::: pf-proof

Since $X$ is Hausdorff, the singleton
$$
\{y\}
$$
is closed.
Hence
$$
X\setminus\{y\}
$$
is an open neighborhood of $x$ not containing $y$.
Take
$$
U=X\setminus\{y\}.
$$

:::

:::

::: pf-step

Because the topology has a clopen basis, there exists a basis element
$$
B
$$
such that
$$
x\in B\subseteq U.
$$
In particular,
$$
y\notin B.
$$


::: pf-proof

Since
$$
x\in U
$$
and $U$ is open, the basis property gives a basis element $B$ with
$$
x\in B\subseteq U.
$$
By hypothesis every basis element is both open and closed.
Since
$$
y\notin U,
$$
one also has
$$
y\notin B.
$$

:::

:::

::: {.pf-step #s1-4}

The two subsets
$$
C\cap B
\qquad\text{and}\qquad
C\cap(X\setminus B)
$$
are disjoint nonempty open subsets of $C$ whose union is $C$.


::: pf-proof

They are disjoint and their union is
$$
C\cap
\bigl(
B\cup(X\setminus B)
\bigr)
=
C.
$$

Because $B$ is open, $C\cap B$ is open in the subspace topology on $C$.
Because $B$ is closed,
$$
X\setminus B
$$
is open, so
$$
C\cap(X\setminus B)
$$
is also open in $C$.

Finally,
$$
x\in C\cap B
$$
and
$$
y\in C\cap(X\setminus B),
$$
so both sets are nonempty.

:::

:::

::: {.pf-step #s1-5}

This contradicts connectedness of $C$.


::: pf-proof

Step [](#s1-4){.pf-ref} writes $C$ as the union of two disjoint nonempty open subsets.
That is a separation of $C$, impossible because $C$ is connected.

:::

:::

::: {.pf-step #s1-6}

Therefore every connected subset of $X$ has at most one point.


::: pf-proof

The assumption that a connected subset contains two distinct points leads to
the contradiction in step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
X\text{ is totally disconnected}.
}
$$


::: pf-proof

Every singleton is connected, and step [](#s1-6){.pf-ref} says these are the only nonempty
connected subsets.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the desired conclusion.

:::

:::

:::
