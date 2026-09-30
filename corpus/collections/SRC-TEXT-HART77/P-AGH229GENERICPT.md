---
schema: qual/card@1
id: P-AGH229GENERICPT
kind: problem
title: Irreducible closed subsets of a scheme have unique generic points
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Generic Points
  - Irreducibility
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.9 statement and source-order placement after II.2.8.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
If $X$ is a topological space and $Z$ an irreducible closed subset of $X$, a **generic point** for $Z$ is a point $\zeta$ such that $Z = \cl\qty{\theset{\zeta}}$.
If $X$ is a scheme, show that every nonempty irreducible closed subset has a unique generic point.
:::

::: {.solution}
Let
\[
Z\subseteq X
\]
be a nonempty irreducible closed subset.

::: pf

::: pf-step
Choose an affine open subset
\[
U=\operatorname{Spec}A\subseteq X
\]
such that
\[
Z\cap U\ne\varnothing.
\]
Then $Z\cap U$ is a nonempty irreducible closed subset of $U$.

::: pf-proof
An affine open cover of $X$ covers the nonempty set $Z$, so some affine open $U$ meets it.

Since $Z$ is closed in $X$, the intersection $Z\cap U$ is closed in the subspace $U$.  It is irreducible because every nonempty open subset of an irreducible space is irreducible: if
\[
Z\cap U=C_1\cup C_2
\]
with $C_1,C_2$ closed in $Z\cap U$, then taking closures in $Z$ would write the dense open subset $Z\cap U$ as contained in the union of two proper closed subsets unless one $C_i$ were the whole intersection.  Equivalently, the standard topological lemma says a nonempty open subspace of an irreducible space is irreducible.
:::

:::

::: {.pf-step #unique-prime-for-zcapu}
There is a unique prime ideal
\[
\mathfrak p\subseteq A
\]
such that
\[
\boxed{Z\cap U=V(\mathfrak p).}
\]

::: pf-proof
Any closed subset of $\operatorname{Spec}A$ has the form
\[
V(I)
\]
for some ideal $I\subseteq A$.  The closed subset $V(I)$ is irreducible exactly when its radical
\[
\sqrt I
\]
is prime.

Indeed, if $\sqrt I$ is prime then
\[
V(I)=V(\sqrt I)
\]
is the closure of the point $\sqrt I$, hence irreducible.  Conversely, if $V(I)$ is irreducible and
\[
ab\in\sqrt I,
\]
then
\[
V(I)\subseteq V(ab)=V(a)\cup V(b).
\]
Irreducibility forces
\[
V(I)\subseteq V(a)
\quad\text{or}\quad
V(I)\subseteq V(b),
\]
so
\[
a\in\sqrt I
\quad\text{or}\quad
b\in\sqrt I.
\]
Thus $\sqrt I$ is prime.

Take
\[
\mathfrak p=\sqrt I.
\]
Uniqueness follows because for prime ideals
\[
V(\mathfrak p)=V(\mathfrak q)
\]
implies
\[
\mathfrak p
=\sqrt{\mathfrak p}
=\sqrt{\mathfrak q}
=\mathfrak q.
\]
:::

:::

::: {.pf-step #zeta-closure-in-u}
Let
\[
\zeta\in U
\]
be the point corresponding to $\mathfrak p$.  Then
\[
\overline{\{\zeta\}}^{\,U}
=Z\cap U.
\]

::: pf-proof
In an affine spectrum, the closure of the point corresponding to a prime $\mathfrak p$ is
\[
V(\mathfrak p).
\]
Apply step [](#unique-prime-for-zcapu){.pf-ref}.
:::

:::

::: {.pf-step #zeta-closure-in-x-is-z}
The closure of $\zeta$ in $X$ is exactly $Z$:
\[
\boxed{
\overline{\{\zeta\}}^{\,X}=Z.
}
\]

::: pf-proof
Since $Z$ is closed in $X$ and contains $\zeta$, one has
\[
\overline{\{\zeta\}}^{\,X}
\subseteq Z.
\]

Intersect this closure with the open set $U$.  Closure in an open subspace satisfies
\[
U\cap\overline{\{\zeta\}}^{\,X}
=\overline{\{\zeta\}}^{\,U}
=Z\cap U
\]
by step [](#zeta-closure-in-u){.pf-ref}.

The subset $Z\cap U$ is a nonempty open subset of the irreducible space $Z$, hence is dense in $Z$.  The closed subset
\[
\overline{\{\zeta\}}^{\,X}
\subseteq Z
\]
contains this dense subset, so it contains all of $Z$.  Together with the first inclusion, equality follows.
:::

:::

::: {.pf-step #generic-point-exists}
Thus every nonempty irreducible closed subset of a scheme has a generic point.

::: pf-proof
The point $\zeta$ constructed in step [](#zeta-closure-in-u){.pf-ref} satisfies the defining condition by step [](#zeta-closure-in-x-is-z){.pf-ref}.
:::

:::

::: {.pf-step #generic-point-in-every-open}
If $\zeta$ is a generic point of $Z$, then $\zeta$ belongs to every nonempty open subset of $Z$.

::: pf-proof
Let
\[
W\subseteq Z
\]
be nonempty and open.  Suppose
\[
\zeta\notin W.
\]
Then
\[
Z\setminus W
\]
is a closed subset of $Z$ containing $\zeta$.  Hence it contains the closure of $\zeta$ in $Z$, which is all of $Z$.  This would force $W=\varnothing$, contradiction.
:::

:::

::: {.pf-step #generic-point-unique}
The generic point of $Z$ is unique.

::: pf-proof
Suppose
\[
\zeta,\eta\in Z
\]
are both generic points.  Choose an affine open neighborhood
\[
\zeta\in U=\operatorname{Spec}A.
\]
Then
\[
U\cap Z
\]
is a nonempty open subset of $Z$, so step [](#generic-point-in-every-open){.pf-ref} applied to the generic point $\eta$ gives
\[
\eta\in U.
\]

The closures of $\zeta$ and $\eta$ inside $U$ are both
\[
Z\cap U.
\]
If they correspond to prime ideals $\mathfrak p$ and $\mathfrak q$ of $A$, then
\[
V(\mathfrak p)=V(\mathfrak q).
\]
As in step [](#unique-prime-for-zcapu){.pf-ref}, equality of these closed sets for prime ideals implies
\[
\mathfrak p=\mathfrak q.
\]
Therefore
\[
\zeta=\eta.
\]
:::

:::

::: {.pf-step #unique-generic-point-statement}
Hence every nonempty irreducible closed subset $Z$ of a scheme has a unique generic point:
\[
\boxed{
Z=\overline{\{\zeta\}}
\quad\text{for a unique }\zeta\in Z.
}
\]

::: pf-proof
Existence is step [](#generic-point-exists){.pf-ref} and uniqueness is step [](#generic-point-unique){.pf-ref}.
:::

:::

::: pf-qed
Step [](#unique-generic-point-statement){.pf-ref} is the assertion of the exercise.
:::

:::

:::
