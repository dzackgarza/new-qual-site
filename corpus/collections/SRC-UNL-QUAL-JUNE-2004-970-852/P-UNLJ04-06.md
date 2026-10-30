---
schema: qual/card@1
id: P-UNLJ04-06
kind: problem
title: A Hall-type criterion for disjoint prescribed subsets
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Question 6 of the retained June 2004 UNL Mathematics Qualifying Exam 970/852 PDF.
---

::: {.problem}
Let $A _ { 1 } , A _ { 2 } , \ldots , A _ { n }$ be finite sets, and $d _ { 1 } , d _ { 2 } , \ldots , d _ { n }$ non-negative integers.
Prove that there are disjoint subsets $D _ { i } \subset A _ { i }$ with $\cardinality{ D _ { i } } = d _ { i }$ if and only if for all $I \subset$ $\{ 1 , 2 , \ldots , n \}$ we have

$$
\cardinality{ \bigcup _ { i \in I } A _ { i } } \geq \sum _ { i \in I } d _ { i } .
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The stated inequality is necessary.


::: pf-proof

Assume there are pairwise-disjoint subsets
$$
D_i\subseteq A_i,
\qquad
\cardinality{D_i}=d_i.
$$
Let
$$
I\subseteq\{1,\ldots,n\}.
$$
Then
$$
\bigsqcup_{i\in I}D_i
\subseteq
\bigcup_{i\in I}A_i.
$$
Therefore
$$
\cardinality{
\bigcup_{i\in I}A_i
}
\ge
\cardinality{
\bigsqcup_{i\in I}D_i
}
=
\sum_{i\in I}\cardinality{D_i}
=
\sum_{i\in I}d_i.
$$

:::

:::

::: {.pf-step #s1-2}

Assume now that
$$
\cardinality{
\bigcup_{i\in I}A_i
}
\ge
\sum_{i\in I}d_i
$$
for every
$$
I\subseteq\{1,\ldots,n\}.
$$
Construct a bipartite graph with left vertex set
$$
L
\coloneqq
\{
(i,j):
1\le i\le n, 1\le j\le d_i
\}
$$
and right vertex set
$$
R
\coloneqq
\bigcup_{i=1}^nA_i.
$$


::: pf-proof

For every left vertex
$$
(i,j)
$$
and every
$$
a\in R,
$$
join
$$
(i,j)
$$
to
$$
a
$$
exactly when
$$
a\in A_i.
$$
Thus the
$$
d_i
$$
copies associated with index
$$
i
$$
all have neighborhood
$$
A_i.
$$

:::

:::

::: {.pf-step #s1-3}

This bipartite graph satisfies Hall's condition:
$$
\boxed{
\cardinality{N(S)}\ge\cardinality{S}
}
$$
for every
$$
S\subseteq L.
$$


::: pf-proof

Fix
$$
S\subseteq L
$$
and let
$$
I(S)
\coloneqq
\{
i:
(i,j)\in S
\text{ for some }j
\}.
$$
By construction,
$$
N(S)
=
\bigcup_{i\in I(S)}A_i.
$$
Hence the assumed inequality gives
$$
\cardinality{N(S)}
=
\cardinality{
\bigcup_{i\in I(S)}A_i
}
\ge
\sum_{i\in I(S)}d_i.
$$
For each
$$
i\in I(S),
$$
the set
$$
S
$$
contains at most
$$
d_i
$$
of the vertices
$$
(i,1),\ldots,(i,d_i).
$$
Therefore
$$
\cardinality{S}
\le
\sum_{i\in I(S)}d_i.
$$
Combining the two inequalities yields
$$
\cardinality{N(S)}\ge\cardinality{S}.
$$

:::

:::

::: {.pf-step #s1-4}

By Hall's marriage theorem, there is a matching saturating every vertex of
$$
L.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} is exactly Hall's condition for the finite bipartite graph constructed in step [](#s1-2){.pf-ref}. Hall's theorem therefore gives an injective assignment
$$
m:L\to R
$$
such that
$$
m(i,j)\in A_i
$$
for every
$$
(i,j)\in L.
$$

:::

:::

::: {.pf-step #s1-5}

For each
$$
i,
$$
define
$$
D_i
\coloneqq
\{
m(i,j):
1\le j\le d_i
\}.
$$
Then
$$
D_i\subseteq A_i
$$
and
$$
\cardinality{D_i}=d_i.
$$


::: pf-proof

Every matched element
$$
m(i,j)
$$
lies in
$$
A_i
$$
by step [](#s1-4){.pf-ref}, so
$$
D_i\subseteq A_i.
$$

Because a matching uses distinct right vertices for distinct left vertices, the values
$$
m(i,1),\ldots,m(i,d_i)
$$
are distinct. Hence
$$
\cardinality{D_i}=d_i.
$$

:::

:::

::: {.pf-step #s1-6}

The sets
$$
D_1,\ldots,D_n
$$
are pairwise disjoint.


::: pf-proof

If
$$
i\ne i',
$$
then every left vertex
$$
(i,j)
$$
is distinct from every left vertex
$$
(i',j').
$$
Since
$$
m
$$
is a matching, distinct left vertices have distinct matched right vertices. Therefore no element can lie in both
$$
D_i
$$
and
$$
D_{i'}.
$$

:::

:::

::: {.pf-step #s1-7}

Thus the stated condition is sufficient.


::: pf-proof

Steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} produce pairwise-disjoint subsets
$$
D_i\subseteq A_i
$$
with
$$
\cardinality{D_i}=d_i
$$
for every
$$
i.
$$

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
\exists\text{ pairwise-disjoint }D_i\subseteq A_i, \cardinality{D_i}=d_i
\iff
\cardinality{
\bigcup_{i\in I}A_i
}
\ge
\sum_{i\in I}d_i
\text{ for all }I.}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} proves necessity, and step [](#s1-7){.pf-ref} proves sufficiency.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required equivalence.

:::

:::

:::
