---
schema: qual/card@1
id: P-WESTOP07-05
kind: problem
title: Intrinsic characterizations of subspaces of compact Hausdorff and simply connected spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Give an intrinsic condition on a topological space $X$ characterizing each of the following situations, with some explanation but not necessarily a complete proof:

1. $X$ is homeomorphic to an open subspace of a compact Hausdorff space.
2. $X$ is homeomorphic to an arbitrary subspace of a compact Hausdorff space.
3. $X$ is homeomorphic to an arbitrary subspace of a simply connected space, where simply connected means path-connected with trivial fundamental group.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One has
$$
\boxed{
X\text{ is homeomorphic to an open subspace of a compact Hausdorff space}
\iff
X\text{ is locally compact Hausdorff}.}
$$


::: pf-proof

Suppose first that
$$
X
$$
is homeomorphic to an open subspace
$$
U
$$
of a compact Hausdorff space
$$
K.
$$
Then
$$
U
$$
is Hausdorff. For every
$$
x\in U,
$$
regularity of the compact Hausdorff space
$$
K
$$
gives an open neighborhood
$$
V
$$
of
$$
x
$$
whose closure in
$$
K
$$
is contained in
$$
U.
$$
That closure is compact, so
$$
U
$$
is locally compact.

Conversely, let
$$
X
$$
be locally compact Hausdorff. If
$$
X
$$
is compact, take
$$
K=X.
$$
If
$$
X
$$
is not compact, its one-point compactification
$$
X^*
=
X\cup\{\infty\}
$$
is compact Hausdorff, and
$$
X=X^*\setminus\{\infty\}
$$
is open because
$$
\{\infty\}
$$
is closed in the Hausdorff space
$$
X^*.
$$
Thus
$$
X
$$
is homeomorphic to an open subspace of a compact Hausdorff space.

:::

:::

::: pf-step

A space is called Tychonoff if it is completely regular and Hausdorff.


::: pf-proof

Complete regularity means that whenever
$$
F\subseteq X
$$
is closed and
$$
x\notin F,
$$
there is a continuous function
$$
f:X\to[0,1]
$$
such that
$$
f(x)=0
$$
and
$$
f(F)=\{1\}.
$$
This, together with the Hausdorff condition, is the standard intrinsic definition of a Tychonoff space.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\boxed{
X\text{ is homeomorphic to a subspace of a compact Hausdorff space}
\iff
X\text{ is Tychonoff}.}
$$


::: pf-proof

Every compact Hausdorff space is Tychonoff, and the Tychonoff property is hereditary to subspaces. Hence every subspace of a compact Hausdorff space is Tychonoff.

Conversely, let
$$
X
$$
be Tychonoff. Let
$$
C(X,[0,1])
$$
be the set of continuous functions from
$$
X
$$
to
$$
[0,1].
$$
Define the evaluation map
$$
e:X
\to
[0,1]^{C(X,[0,1])}
$$
by
$$
e(x)(f)=f(x).
$$
Complete regularity and the Hausdorff property imply that continuous
$$
[0,1]
$$
-valued functions separate points and closed sets. Consequently
$$
e
$$
is a topological embedding.

By Tychonoff's theorem, the cube
$$
[0,1]^{C(X,[0,1])}
$$
is compact, and it is Hausdorff because
$$
[0,1]
$$
is Hausdorff. Thus
$$
X
$$
embeds as a subspace of a compact Hausdorff space.

:::

:::

::: {.pf-step #s1-4}

Every topological space is homeomorphic to a subspace of a contractible space.


::: pf-proof

For a nonempty space
$$
X,
$$
form the cone
$$
CX
\coloneqq
(X\times[0,1])/
(X\times\{1\}),
$$
where the entire top
$$
X\times\{1\}
$$
is collapsed to a single apex.

Let
$$
q:X\times[0,1]\to CX
$$
be the quotient map. The map
$$
i:X\to CX,
\qquad
i(x)=q(x,0),
$$
is injective.

It is a topological embedding. Indeed, if
$$
U\subseteq X
$$
is open, then
$$
U\times[0,1/2)
$$
is open and saturated for the quotient relation, so
$$
q(U\times[0,1/2))
$$
is open in
$$
CX.
$$
Its intersection with
$$
i(X)
$$
is exactly
$$
i(U).
$$
Thus the subspace topology on
$$
i(X)
$$
is the original topology on
$$
X.
$$

The cone is contractible: define
$$
H:CX\times[0,1]\to CX
$$
by
$$
H(q(x,t),s)
=
q(x,t+s(1-t)).
$$
At
$$
s=0
$$
this is the identity, and at
$$
s=1
$$
every point is sent to the apex. The formula is well-defined on the collapsed top.

:::

:::

::: {.pf-step #s1-5}

Every topological space is homeomorphic to a subspace of a simply connected space.


::: pf-proof

If
$$
X
$$
is nonempty, step [](#s1-4){.pf-ref} embeds it in the contractible space
$$
CX.
$$
A contractible space is path-connected and has trivial fundamental group, hence is simply connected.

If
$$
X=\varnothing,
$$
it embeds as the empty subspace of any simply connected space, for example a point.

:::

:::

::: {.pf-step #s1-6}

Thus the three intrinsic characterizations are
$$
\boxed{
\begin{array}{c|c}
\text{Ambient situation}
&
\text{Intrinsic condition on }X
\\
\hline
\text{open subspace of compact Hausdorff}
&
\text{locally compact Hausdorff}
\\
\text{subspace of compact Hausdorff}
&
\text{Tychonoff}
\\
\text{subspace of simply connected}
&
\text{no condition; every space qualifies}
\end{array}}
$$


::: pf-proof

These are steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref}, and [](#s1-5){.pf-ref}, respectively.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} gives the requested intrinsic characterizations.

:::

:::

:::
