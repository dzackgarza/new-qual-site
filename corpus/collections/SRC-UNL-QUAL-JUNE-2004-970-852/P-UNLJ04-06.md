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
Prove that there are disjoint subsets $D _ { i } \subset A _ { i }$ with $| D _ { i } | = d _ { i }$ if and only if for all $I \subset$ $\{ 1 , 2 , \ldots , n \}$ we have

$$
\left| \bigcup _ { i \in I } A _ { i } \right| \geq \sum _ { i \in I } d _ { i } .
$$
:::

::: pf

::: pf-step

The stated inequality is necessary.


::: pf-proof

Assume there are pairwise-disjoint subsets
$$
D_i\subseteq A_i,
\qquad
|D_i|=d_i.
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
\left|
\bigcup_{i\in I}A_i
\right|
\ge
\left|
\bigsqcup_{i\in I}D_i
\right|
=
\sum_{i\in I}|D_i|
=
\sum_{i\in I}d_i.
$$

:::

:::

::: pf-step

Assume now that
$$
\left|
\bigcup_{i\in I}A_i
\right|
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

::: pf-step

This bipartite graph satisfies Hall's condition:
$$
\boxed{
|N(S)|\ge|S|
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
|N(S)|
=
\left|
\bigcup_{i\in I(S)}A_i
\right|
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
|S|
\le
\sum_{i\in I(S)}d_i.
$$
Combining the two inequalities yields
$$
|N(S)|\ge|S|.
$$

:::

:::

::: pf-step

By Hall's marriage theorem, there is a matching saturating every vertex of
$$
L.
$$


::: pf-proof

Step <1>3 is exactly Hall's condition for the finite bipartite graph constructed in step <1>2. Hall's theorem therefore gives an injective assignment
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

::: pf-step

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
|D_i|=d_i.
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
by step <1>4, so
$$
D_i\subseteq A_i.
$$

Because a matching uses distinct right vertices for distinct left vertices, the values
$$
m(i,1),\ldots,m(i,d_i)
$$
are distinct. Hence
$$
|D_i|=d_i.
$$

:::

:::

::: pf-step

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

::: pf-step

Thus the stated condition is sufficient.


::: pf-proof

Steps <1>5--<1>6 produce pairwise-disjoint subsets
$$
D_i\subseteq A_i
$$
with
$$
|D_i|=d_i
$$
for every
$$
i.
$$

:::

:::

::: pf-step

Therefore
$$
\boxed{
\exists\text{ pairwise-disjoint }D_i\subseteq A_i, |D_i|=d_i
\iff
\left|
\bigcup_{i\in I}A_i
\right|
\ge
\sum_{i\in I}d_i
\text{ for all }I.}
$$


::: pf-proof

Step <1>1 proves necessity, and step <1>7 proves sufficiency.

:::

:::

::: pf-qed

Step <1>8 is the required equivalence.

:::

:::
