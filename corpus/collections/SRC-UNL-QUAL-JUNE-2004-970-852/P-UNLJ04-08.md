---
schema: qual/card@1
id: P-UNLJ04-08
kind: problem
title: Large cuts in graphs and cubic graphs
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Question 8 of the retained June 2004 UNL Mathematics Qualifying Exam 970/852 PDF.
---

::: {.problem}
Prove that every graph $G$ has a bipartition $V(G)=X\cup Y$ with the property that $e(X,Y)\ge e(G)/2$.
Further, show that if $G$ is cubic, then one can achieve $e(X,Y)\ge n(G)=2e(G)/3$.
:::

::: {.solution}

For a bipartition
$$
V(G)=X\sqcup Y,
$$
write
$$
e(X,Y)
$$
for the number of edges with one endpoint in
$$
X
$$
and the other in
$$
Y.
$$

::: pf

::: pf-step

Choose a bipartition
$$
V(G)=X\sqcup Y
$$
for which
$$
e(X,Y)
$$
is maximal.


::: pf-proof

There are finitely many bipartitions of the finite vertex set
$$
V(G),
$$
so the integer-valued function
$$
(X,Y)\longmapsto e(X,Y)
$$
attains a maximum.

:::

:::

::: {.pf-step #s1-2}

For every vertex
$$
v\in V(G),
$$
the number of crossing edges incident to
$$
v
$$
is at least the number of noncrossing edges incident to
$$
v.
$$


::: pf-proof

Suppose
$$
v\in X.
$$
Let
$$
c(v)
$$
be the number of neighbors of
$$
v
$$
in
$$
Y,
$$
and let
$$
s(v)
$$
be the number of neighbors of
$$
v
$$
in
$$
X.
$$

If
$$
s(v)>c(v),
$$
move
$$
v
$$
from
$$
X
$$
to
$$
Y.
$$
The
$$
s(v)
$$
formerly noncrossing edges at
$$
v
$$
become crossing, while the
$$
c(v)
$$
formerly crossing edges become noncrossing. Hence the cut size changes by
$$
s(v)-c(v)>0,
$$
contradicting maximality.

Thus
$$
c(v)\ge s(v).
$$
The argument is identical if
$$
v\in Y.
$$

:::

:::

::: {.pf-step #s1-3}

For every graph,
$$
\boxed{
e(X,Y)\ge\frac{e(G)}2}.
$$


::: pf-proof

Let
$$
E_{\mathrm{cross}}
$$
be the set of crossing edges and
$$
E_{\mathrm{same}}
$$
the set of noncrossing edges.

Summing the inequality from step [](#s1-2){.pf-ref} over all vertices gives
$$
\sum_{v\in V(G)}c(v)
\ge
\sum_{v\in V(G)}s(v).
$$
Every crossing edge contributes
$$
1
$$
to
$$
c(v)
$$
at each of its two endpoints, so
$$
\sum_v c(v)
=
2e(X,Y).
$$
Likewise,
$$
\sum_v s(v)
=
2\cardinality{E_{\mathrm{same}}}.
$$
Therefore
$$
e(X,Y)
\ge
\cardinality{E_{\mathrm{same}}}.
$$
Since
$$
e(G)
=
e(X,Y)+\cardinality{E_{\mathrm{same}}},
$$
we get
$$
e(G)
\le
2e(X,Y),
$$
hence
$$
e(X,Y)
\ge
\frac{e(G)}2.
$$

:::

:::

::: {.pf-step #s1-4}

Now suppose
$$
G
$$
is cubic. Then every vertex is incident to at least two crossing edges.


::: pf-proof

For every vertex
$$
v,
$$
one has
$$
c(v)+s(v)=3.
$$
Step [](#s1-2){.pf-ref} gives
$$
c(v)\ge s(v).
$$
Since
$$
c(v)
$$
and
$$
s(v)
$$
are nonnegative integers summing to
$$
3,
$$
this forces
$$
c(v)\ge2.
$$

:::

:::

::: {.pf-step #s1-5}

For a cubic graph,
$$
\boxed{
e(X,Y)\ge n(G)}.
$$


::: pf-proof

Sum the inequality
$$
c(v)\ge2
$$
from step [](#s1-4){.pf-ref} over all
$$
n(G)
$$
vertices:
$$
\sum_{v\in V(G)}c(v)
\ge
2n(G).
$$
But
$$
\sum_v c(v)
=
2e(X,Y).
$$
Therefore
$$
2e(X,Y)
\ge
2n(G),
$$
so
$$
e(X,Y)\ge n(G).
$$

:::

:::

::: {.pf-step #s1-6}

In a cubic graph,
$$
n(G)=\frac{2e(G)}3.
$$


::: pf-proof

The handshaking lemma gives
$$
\sum_{v\in V(G)}\deg(v)
=
2e(G).
$$
Since every vertex has degree
$$
3,
$$
the left-hand side is
$$
3n(G).
$$
Hence
$$
3n(G)
=
2e(G),
$$
so
$$
n(G)
=
\frac{2e(G)}3.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore, if $G$ is cubic, one can achieve
$$
\boxed{
e(X,Y)
\ge
n(G)
=
\frac{2e(G)}3}.
$$


::: pf-proof

Combine steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves the general bound, and step [](#s1-7){.pf-ref} proves the stronger cubic bound.

:::

:::

:::
