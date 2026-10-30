---
schema: qual/card@1
id: P-UNLJ04-09
kind: problem
title: Chromatic recurrence and acyclic orientations
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Question 9 of the retained June 2004 UNL Mathematics Qualifying Exam 970/852 PDF.
---

::: {.problem}
a. State the chromatic recurrence satisfied by the chromatic polynomial $\chi ( G ; k )$

b. Prove the for any graph G the number of acyclic orientations of G is $\chi ( G ; - 1 )$ . [An orientation of a graph G is an assignment of a direction to every edge of G. Such an orientation is acyclic if the resulting directed graph contains no directed cycles.]
:::

The printed statement in part (b) is missing the standard sign. If
$$
a(G)
$$
denotes the number of acyclic orientations of a finite loopless graph
$$
G,
$$
the correct identity is
$$
\boxed{
a(G)
=
(-1)^{\cardinality{V(G)}}\chi(G;-1)}.
$$

Indeed, for the edgeless graph on one vertex,
$$
a(G)=1
$$
whereas
$$
\chi(G;-1)=-1,
$$
so the unsigned formula is false.

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every non-loop edge
$$
e
$$
of
$$
G,
$$
the chromatic polynomial satisfies
$$
\boxed{
\chi(G;k)
=
\chi(G-e;k)
-\chi(G/e;k)}.
$$


::: pf-proof

Every proper
$$
k
$$
-coloring of
$$
G-e
$$
falls into exactly one of two classes:

1. the endpoints of
$$
e
$$
receive different colors;
2. the endpoints of
$$
e
$$
receive the same color.

The colorings of the first type are exactly the proper colorings of
$$
G.
$$
The colorings of the second type are naturally identified with proper colorings of the contraction
$$
G/e.
$$
Therefore
$$
\chi(G-e;k)
=
\chi(G;k)
+\chi(G/e;k),
$$
which rearranges to the displayed recurrence.

:::

:::

::: {.pf-step #s1-2}

Let
$$
e=uv.
$$
For an acyclic orientation
$$
\mathcal O
$$
of
$$
G-e,
$$
at most one of the following can occur:
$$
u\leadsto v,
\qquad
v\leadsto u,
$$
where
$$
x\leadsto y
$$
means that there is a directed path from
$$
x
$$
to
$$
y.
$$


::: pf-proof

If both directed paths existed, their concatenation would produce a directed cycle in
$$
G-e,
$$
contradicting acyclicity.

:::

:::

::: {.pf-step #s1-3}

If
$$
u\leadsto v
$$
in
$$
\mathcal O,
$$
then exactly one orientation of
$$
e
$$
extends
$$
\mathcal O
$$
acyclically, namely
$$
u\to v.
$$
Likewise, if
$$
v\leadsto u,
$$
the unique acyclic extension is
$$
v\to u.
$$


::: pf-proof

Suppose
$$
u\leadsto v.
$$
If
$$
e
$$
is oriented
$$
v\to u,
$$
the directed path
$$
u\leadsto v
$$
together with
$$
v\to u
$$
forms a directed cycle.

If instead
$$
e
$$
is oriented
$$
u\to v,
$$
any directed cycle using
$$
e
$$
would require a directed path
$$
v\leadsto u
$$
in
$$
G-e,
$$
which is impossible by step [](#s1-2){.pf-ref}. Since
$$
\mathcal O
$$
was already acyclic, no directed cycle occurs.

The other case is symmetric.

:::

:::

::: {.pf-step #s1-4}

If neither
$$
u\leadsto v
$$
nor
$$
v\leadsto u
$$
occurs in
$$
\mathcal O,
$$
then both orientations of
$$
e
$$
extend
$$
\mathcal O
$$
acyclically.


::: pf-proof

If one orientation of
$$
e
$$
created a directed cycle, deleting
$$
e
$$
from that cycle would give a directed path in
$$
G-e
$$
between
$$
u
$$
and
$$
v.
$$
The direction of that path would be opposite the chosen direction of
$$
e.
$$
By hypothesis no such directed path exists in either direction.

:::

:::

::: {.pf-step #s1-5}

The acyclic orientations of
$$
G/e
$$
are in bijection with the acyclic orientations
$$
\mathcal O
$$
of
$$
G-e
$$
for which neither
$$
u\leadsto v
$$
nor
$$
v\leadsto u
$$
occurs.


::: pf-proof

Given an acyclic orientation of
$$
G/e,
$$
split the contracted vertex back into
$$
u
$$
and
$$
v
$$
and orient every edge of
$$
G-e
$$
as dictated by the corresponding edge of
$$
G/e.
$$
If the lifted orientation contained a directed path
$$
u\leadsto v
$$
or
$$
v\leadsto u,
$$
contracting the endpoints would turn that path into a directed cycle in
$$
G/e.
$$
Thus neither path occurs.

Conversely, take an acyclic orientation of
$$
G-e
$$
with no directed path between
$$
u
$$
and
$$
v
$$
in either direction. Contract
$$
u
$$
and
$$
v.
$$
Any directed cycle created by the contraction would lift either to a directed cycle already present in
$$
G-e
$$
or to a directed path from one of
$$
u,v
$$
to the other. Both alternatives are excluded.

The two constructions are inverse to each other.

:::

:::

::: {.pf-step #s1-6}

The number of acyclic orientations satisfies
$$
\boxed{
a(G)
=
a(G-e)
+a(G/e)}.
$$


::: pf-proof

Start with an acyclic orientation of
$$
G-e.
$$
By steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref}, it contributes:

1. one acyclic extension to
$$
G
$$
if its endpoints are comparable by a directed path;
2. two acyclic extensions if the endpoints are incomparable.

Thus every acyclic orientation of
$$
G-e
$$
contributes one extension, accounting for
$$
a(G-e),
$$
and each incomparable orientation contributes one additional extension.

By step [](#s1-5){.pf-ref}, the number of incomparable orientations is
$$
a(G/e).
$$
Hence
$$
a(G)
=
a(G-e)
+a(G/e).
$$

:::

:::

::: {.pf-step #s1-7}

Define
$$
b(G)
\coloneqq
(-1)^{\cardinality{V(G)}}\chi(G;-1).
$$
Then
$$
b(G)
=
b(G-e)
+b(G/e).
$$


::: pf-proof

Let
$$
n=\cardinality{V(G)}.
$$
Then
$$
\cardinality{V(G-e)}=n,
\qquad
\cardinality{V(G/e)}=n-1.
$$
Evaluate the chromatic recurrence of step [](#s1-1){.pf-ref} at $k=-1$:
$$
\chi(G;-1)
=
\chi(G-e;-1)
-\chi(G/e;-1).
$$
Multiply by $(-1)^n$:
$$
\begin{aligned}
b(G)
&=
(-1)^n\chi(G-e;-1)
-(-1)^n\chi(G/e;-1)\\
&=
b(G-e)
+(-1)^{n-1}\chi(G/e;-1)\\
&=
b(G-e)
+b(G/e).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-8}

If
$$
G
$$
has no edges and
$$
n
$$
vertices, then
$$
a(G)=b(G)=1.
$$


::: pf-proof

There is exactly one orientation of an edgeless graph, and it is acyclic. Thus
$$
a(G)=1.
$$

Also
$$
\chi(G;k)=k^n,
$$
so
$$
b(G)
=
(-1)^n(-1)^n
=1.
$$

:::

:::

::: {.pf-step #s1-9}

For every finite loopless graph,
$$
\boxed{
a(G)
=
(-1)^{\cardinality{V(G)}}\chi(G;-1)}.
$$


::: pf-proof

Induct on the number of edges.

The base case is step [](#s1-8){.pf-ref}.

For a graph with at least one edge, choose a non-loop edge
$$
e.
$$
Both
$$
G-e
$$
and
$$
G/e
$$
have fewer edges after suppressing any duplicate parallel copies that do not affect the chromatic polynomial or the acyclic-orientation recurrence. By the induction hypothesis,
$$
a(G-e)=b(G-e),
\qquad
a(G/e)=b(G/e).
$$
Steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref} therefore give
$$
a(G)
=
a(G-e)+a(G/e)
=
b(G-e)+b(G/e)
=
b(G).
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the chromatic recurrence. Step [](#s1-9){.pf-ref} proves the corrected acyclic-orientation theorem and explains why the unsigned statement printed in the source cannot be correct.

:::

:::

:::
