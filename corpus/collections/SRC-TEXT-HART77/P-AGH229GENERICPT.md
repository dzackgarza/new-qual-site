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
If $X$ is a topological space and $Z$ an irreducible closed subset of $X$, a **generic point** for $Z$ is a point $\zeta$ such that $Z = \cl\qty{\ts{\zeta}}$.
If $X$ is a scheme, show that every nonempty irreducible closed subset has a unique generic point.
:::

::: {.solution}
Let
\[
Z\subseteq X
\]
be a nonempty irreducible closed subset.

<1>1. Choose an affine open subset
\[
U=\operatorname{Spec}A\subseteq X
\]
such that
\[
Z\cap U\ne\varnothing.
\]
Then $Z\cap U$ is a nonempty irreducible closed subset of $U$.
::: {.proof}
An affine open cover of $X$ covers the nonempty set $Z$, so some affine open $U$ meets it.

Since $Z$ is closed in $X$, the intersection $Z\cap U$ is closed in the subspace $U$.  It is irreducible because every nonempty open subset of an irreducible space is irreducible: if
\[
Z\cap U=C_1\cup C_2
\]
with $C_1,C_2$ closed in $Z\cap U$, then taking closures in $Z$ would write the dense open subset $Z\cap U$ as contained in the union of two proper closed subsets unless one $C_i$ were the whole intersection.  Equivalently, the standard topological lemma says a nonempty open subspace of an irreducible space is irreducible.
:::

<1>2. There is a unique prime ideal
\[
\mathfrak p\subseteq A
\]
such that
\[
\boxed{Z\cap U=V(\mathfrak p).}
\]
::: {.proof}
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

<1>3. Let
\[
\zeta\in U
\]
be the point corresponding to $\mathfrak p$.  Then
\[
\overline{\{\zeta\}}^{\,U}
=Z\cap U.
\]
::: {.proof}
In an affine spectrum, the closure of the point corresponding to a prime $\mathfrak p$ is
\[
V(\mathfrak p).
\]
Apply <1>2.
:::

<1>4. The closure of $\zeta$ in $X$ is exactly $Z$:
\[
\boxed{
\overline{\{\zeta\}}^{\,X}=Z.
}
\]
::: {.proof}
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
by <1>3.

The subset $Z\cap U$ is a nonempty open subset of the irreducible space $Z$, hence is dense in $Z$.  The closed subset
\[
\overline{\{\zeta\}}^{\,X}
\subseteq Z
\]
contains this dense subset, so it contains all of $Z$.  Together with the first inclusion, equality follows.
:::

<1>5. Thus every nonempty irreducible closed subset of a scheme has a generic point.
::: {.proof}
The point $\zeta$ constructed in <1>3 satisfies the defining condition by <1>4.
:::

<1>6. If $\zeta$ is a generic point of $Z$, then $\zeta$ belongs to every nonempty open subset of $Z$.
::: {.proof}
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

<1>7. The generic point of $Z$ is unique.
::: {.proof}
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
is a nonempty open subset of $Z$, so <1>6 applied to the generic point $\eta$ gives
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
As in <1>2, equality of these closed sets for prime ideals implies
\[
\mathfrak p=\mathfrak q.
\]
Therefore
\[
\zeta=\eta.
\]
:::

<1>8. Hence every nonempty irreducible closed subset $Z$ of a scheme has a unique generic point:
\[
\boxed{
Z=\overline{\{\zeta\}}
\quad\text{for a unique }\zeta\in Z.
}
\]
::: {.proof}
Existence is <1>5 and uniqueness is <1>7.
:::

<1>9. Q.E.D.
::: {.proof}
Step <1>8 is the assertion of the exercise.
:::
:::
