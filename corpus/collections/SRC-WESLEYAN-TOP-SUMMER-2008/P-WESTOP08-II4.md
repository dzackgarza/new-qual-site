---
schema: qual/card@1
id: P-WESTOP08-II4
kind: problem
title: Uniqueness of lifts from a connected space
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
State the definition of a covering space
\[
p:\widetilde X\to X.
\]
Let $f:Y\to X$ be a map having two lifts
\[
\widetilde f_1,\widetilde f_2:Y\to\widetilde X.
\]
If $Y$ is connected and the two lifts agree at one point of $Y$, prove that
\[
\widetilde f_1=\widetilde f_2
\]
on all of $Y$.
:::

::: pf

::: pf-step

A map
\[
p:\widetilde X\to X
\]
is a covering map if every point
\[
x\in X
\]
has an open neighborhood
\[
U\subseteq X
\]
such that
\[
p^{-1}(U)
\]
is a disjoint union of open sets
\[
p^{-1}(U)
=
\bigsqcup_{\lambda\in\Lambda}
V_\lambda,
\]
and for each $\lambda$ the restriction
\[
p|_{V_\lambda}:V_\lambda\to U
\]
is a homeomorphism.


::: pf-proof

This is the definition of a covering space.
Such a neighborhood $U$ is called evenly covered.

:::

:::

::: pf-step

Since
\[
\widetilde f_1
\quad\text{and}\quad
\widetilde f_2
\]
are lifts of the same map $f$, one has
\[
p\circ\widetilde f_1
=
f
=
p\circ\widetilde f_2.
\]


::: pf-proof

This is exactly the definition of being a lift of $f$ through $p$.

:::

:::

::: pf-step

Define the coincidence set
\[
E
\coloneqq
\{y\in Y:
\widetilde f_1(y)=\widetilde f_2(y)\}.
\]
By hypothesis,
\[
E\ne\varnothing.
\]


::: pf-proof

The two lifts agree at at least one point of $Y$.

:::

:::

::: pf-step

The set $E$ is open in $Y$.


::: pf-proof

Take
\[
y_0\in E.
\]
Set
\[
\widetilde x
\coloneqq
\widetilde f_1(y_0)
=
\widetilde f_2(y_0)
\]
and
\[
x
\coloneqq
f(y_0)
=
p(\widetilde x).
\]

Choose an evenly covered neighborhood
\[
U\ni x.
\]
Let
\[
V
\]
be the sheet over $U$ containing $\widetilde x$.
Thus
\[
p|_V:V\xrightarrow{\cong}U.
\]

By continuity of
\[
f,
\quad
\widetilde f_1,
\quad
\widetilde f_2,
\]
there is an open neighborhood
\[
W\ni y_0
\]
such that
\[
f(W)\subseteq U,
\qquad
\widetilde f_1(W)\subseteq V,
\qquad
\widetilde f_2(W)\subseteq V.
\]

For
\[
y\in W,
\]
step <1>2 gives
\[
p(\widetilde f_1(y))
=
f(y)
=
p(\widetilde f_2(y)).
\]
Both points lie in the same sheet $V$, and
\[
p|_V
\]
is injective.
Therefore
\[
\widetilde f_1(y)
=
\widetilde f_2(y).
\]
Hence
\[
W\subseteq E,
\]
so $E$ is open.

:::

:::

::: pf-step

The complement
\[
Y\setminus E
\]
is open in $Y$.


::: pf-proof

Take
\[
y_0\notin E.
\]
Then
\[
\widetilde f_1(y_0)
\ne
\widetilde f_2(y_0),
\]
but both map under $p$ to
\[
x=f(y_0).
\]

Choose an evenly covered neighborhood
\[
U\ni x.
\]
The two points
\[
\widetilde f_1(y_0),
\qquad
\widetilde f_2(y_0)
\]
must lie in distinct sheets
\[
V_1
\qquad\text{and}\qquad
V_2
\]
over $U$, because each restriction
\[
p|_{V_j}:V_j\to U
\]
is injective.

By continuity, after shrinking to an open neighborhood
\[
W\ni y_0,
\]
one has
\[
\widetilde f_1(W)\subseteq V_1,
\qquad
\widetilde f_2(W)\subseteq V_2.
\]
Since
\[
V_1\cap V_2=\varnothing,
\]
the two lifts cannot agree at any point of $W$.
Thus
\[
W\subseteq Y\setminus E,
\]
so the complement is open.

:::

:::

::: pf-step

Therefore $E$ is both open and closed in $Y$.


::: pf-proof

Step <1>4 gives openness of $E$, while step <1>5 says its complement is
open, equivalently $E$ is closed.

:::

:::

::: pf-step

Since $Y$ is connected and
\[
E\ne\varnothing,
\]
one has
\[
E=Y.
\]


::: pf-proof

A connected space has no nontrivial subset that is both open and closed.
By step <1>3, $E$ is nonempty.
Hence the only possibility is
\[
E=Y.
\]

:::

:::

::: pf-step

Thus
\[
\boxed{
\widetilde f_1
=
\widetilde f_2
}
\]
on all of $Y$.


::: pf-proof

By step <1>7, every point
\[
y\in Y
\]
lies in the coincidence set $E$.

:::

:::

::: pf-qed

Step <1>1 states the definition of a covering space, and steps <1>2--<1>8
prove uniqueness of lifts from a connected domain once they agree at one
point.

:::

:::
