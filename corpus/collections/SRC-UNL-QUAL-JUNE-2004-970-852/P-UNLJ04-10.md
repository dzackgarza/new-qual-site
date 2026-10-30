---
schema: qual/card@1
id: P-UNLJ04-10
kind: problem
title: Turán theorem by minimum-degree reduction
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Question 10 of the retained June 2004 UNL Mathematics Qualifying Exam 970/852 PDF.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Part (c) of the source claims two K_r sharing r-1 vertices for every r, which fails for r=2 (a single edge). The statement now restricts that claim to r >= 3.
---

::: {.problem}
a. State Turán's theorem concerning the maximum number of edges in a graph on $n$ vertices not containing a $K_{r}$.

b. Prove that if $G$ is a graph with $n \geq r + 1$ vertices and $t_{r-1}(n) + 1$ edges, then for every $n'$ with $r \leq n' \leq n$ there is a subgraph $H$ of $G$ with $n'$ vertices and at least $t_{r-1}(n') + 1$ edges.
[Hint: consider a vertex in $G$ of minimum degree.]

c. From the previous part deduce Turán's theorem, and also the stronger fact that, for $r \geq 3$, such a $G$ contains two $K_{r}$ subgraphs sharing $r - 1$ vertices.
:::

::: {.solution}

Write
$$
q=r-1,
$$
and let
$$
t_q(n)
$$
denote the number of edges in the balanced complete
$$
q
$$
-partite Turán graph
$$
T_q(n).
$$

::: pf

::: {.pf-step #s1-1}

Turán's theorem states:
$$
\boxed{
K_r\nsubseteq G
\Longrightarrow
e(G)\le t_{r-1}(n(G)).}
$$
Equality holds exactly for the Turán graph
$$
T_{r-1}(n(G))
$$
up to isomorphism.


::: pf-proof

Equivalently, among all graphs on
$$
n
$$
vertices containing no
$$
K_r,
$$
the balanced complete
$$
(r-1)
$$
-partite graph has the maximum possible number of edges.

:::

:::

::: pf-step

For
$$
m\ge2,
$$
the Turán numbers satisfy
$$
\boxed{
t_q(m)-t_q(m-1)
=
\left\lfloor
\frac{(q-1)m}{q}
\right\rfloor}.
$$


::: pf-proof

Construct
$$
T_q(m)
$$
from
$$
T_q(m-1)
$$
by adding one vertex to a smallest part.

The smallest part of
$$
T_q(m-1)
$$
has size
$$
\left\lfloor
\frac{m-1}{q}
\right\rfloor.
$$
The new vertex is adjacent to every vertex outside that part, so the number of new edges is
$$
(m-1)
-
\left\lfloor
\frac{m-1}{q}
\right\rfloor
=
\left\lfloor
\frac{(q-1)m}{q}
\right\rfloor.
$$

:::

:::

::: {.pf-step #s1-3}

Let
$$
m\ge q+2
$$
and let
$$
H
$$
be a graph on
$$
m
$$
vertices with exactly
$$
t_q(m)+1
$$
edges. Then
$$
H
$$
has a vertex
$$
v
$$
with
$$
\boxed{
\deg_H(v)
\le
t_q(m)-t_q(m-1)}.
$$


::: pf-proof

Set
$$
d
\coloneqq
t_q(m)-t_q(m-1).
$$
Suppose every vertex had degree at least
$$
d+1.
$$
Then the handshaking lemma would give
$$
2(t_q(m)+1)
=
2e(H)
\ge
m(d+1).
$$
It suffices to show
$$
m(d+1)
>
2(t_q(m)+1),
$$
which is a contradiction.

Write
$$
m=aq+s,
\qquad
0\le s<q.
$$

If
$$
s=0,
$$
then every part of
$$
T_q(m)
$$
has size
$$
a,
$$
and
$$
d=(q-1)a.
$$
Hence
$$
\begin{aligned}
m(d+1)-2(t_q(m)+1)
&=
aq\bigl((q-1)a+1\bigr)
-q(q-1)a^2
-2\\
&=
aq-2\\
&=
m-2
>0.
\end{aligned}
$$

If
$$
1\le s<q,
$$
then
$$
T_q(m)
$$
has
$$
s
$$
parts of size
$$
a+1
$$
and
$$
q-s
$$
parts of size
$$
a.
$$
Thus
$$
d
=
m-(a+1),
$$
so
$$
d+1=m-a.
$$
Also
$$
2t_q(m)
=
m^2
-
\bigl(
qa^2+2as+s
\bigr).
$$
Therefore
$$
\begin{aligned}
m(d+1)-2(t_q(m)+1)
&=
m(m-a)
-m^2
+qa^2+2as+s
-2\\
&=
s(a+1)-2.
\end{aligned}
$$
Because
$$
m\ge q+2,
$$
either
$$
a\ge2
$$
or
$$
a=1
\text{ and }
s\ge2.
$$
Hence
$$
s(a+1)-2>0.
$$

Thus in every case the assumption that all degrees are at least
$$
d+1
$$
is impossible.

:::

:::

::: {.pf-step #s1-4}

If
$$
H
$$
has
$$
m\ge q+2
$$
vertices and at least
$$
t_q(m)+1
$$
edges, then
$$
H
$$
contains a subgraph on
$$
m-1
$$
vertices with at least
$$
t_q(m-1)+1
$$
edges.


::: pf-proof

If
$$
H
$$
has more than
$$
t_q(m)+1
$$
edges, delete surplus edges until a spanning subgraph
$$
H_0
$$
with exactly
$$
t_q(m)+1
$$
edges remains.

By step [](#s1-3){.pf-ref},
$$
H_0
$$
has a vertex
$$
v
$$
with
$$
\deg_{H_0}(v)
\le
t_q(m)-t_q(m-1).
$$
Therefore
$$
\begin{aligned}
e(H_0-v)
&=
e(H_0)-\deg_{H_0}(v)\\
&\ge
t_q(m)+1
-
\bigl(
t_q(m)-t_q(m-1)
\bigr)\\
&=
t_q(m-1)+1.
\end{aligned}
$$
Since
$$
H_0-v
$$
is a subgraph of
$$
H,
$$
the claim follows.

:::

:::

::: {.pf-step #s1-5}

Let
$$
G
$$
have
$$
n\ge r+1
$$
vertices and at least
$$
t_{r-1}(n)+1
$$
edges. Then for every
$$
n'
$$
with
$$
r\le n'\le n,
$$
there is a subgraph
$$
H\subseteq G
$$
with
$$
n(H)=n'
$$
and
$$
\boxed{
e(H)
\ge
t_{r-1}(n')+1}.
$$


::: pf-proof

Apply step [](#s1-4){.pf-ref} repeatedly, reducing the number of vertices one at a time.

At each stage
$$
m>r=q+1,
$$
so
$$
m\ge q+2,
$$
which is exactly the range required by step [](#s1-4){.pf-ref}.

Stop when
$$
m=n'.
$$
The resulting graph is a subgraph of
$$
G
$$
with the asserted number of vertices and edges.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\boxed{
t_{r-1}(r)
=
\binom r2-1}.
$$


::: pf-proof

The balanced complete
$$
(r-1)
$$
-partite graph on
$$
r
$$
vertices has one part of size
$$
2
$$
and
$$
r-2
$$
singleton parts.

Thus it is the complete graph
$$
K_r
$$
with exactly the edge inside the two-vertex part removed. Hence its edge count is
$$
\binom r2-1.
$$

:::

:::

::: {.pf-step #s1-7}

Turán's theorem follows from part (b).


::: pf-proof

Suppose
$$
G
$$
has
$$
n
$$
vertices and more than
$$
t_{r-1}(n)
$$
edges.

Since edge counts are integers,
$$
e(G)
\ge
t_{r-1}(n)+1.
$$
By step [](#s1-5){.pf-ref} with
$$
n'=r,
$$
there is a subgraph
$$
H
$$
on
$$
r
$$
vertices with at least
$$
t_{r-1}(r)+1
$$
edges.

Using step [](#s1-6){.pf-ref},
$$
e(H)
\ge
\binom r2.
$$
But a graph on
$$
r
$$
vertices has at most
$$
\binom r2
$$
edges, so
$$
H=K_r.
$$
Thus every graph with more than
$$
t_{r-1}(n)
$$
edges contains
$$
K_r,
$$
which is the asserted extremal bound.

:::

:::

::: {.pf-step #s1-8}

Assume
$$
r\ge3.
$$
Then
$$
\boxed{
t_{r-1}(r+1)
=
\binom{r+1}{2}-2}.
$$


::: pf-proof

Put
$$
q=r-1.
$$
The balanced complete
$$
q
$$
-partite graph on
$$
q+2=r+1
$$
vertices has two parts of size
$$
2
$$
and all remaining parts of size
$$
1.
$$

Relative to
$$
K_{r+1},
$$
the only missing edges are the one internal edge in each of the two two-vertex parts. Hence exactly two edges are missing.

:::

:::

::: {.pf-step #s1-9}

For
$$
r\ge3,
$$
every graph
$$
G
$$
with
$$
n\ge r+1
$$
vertices and at least
$$
t_{r-1}(n)+1
$$
edges contains two copies of
$$
K_r
$$
sharing
$$
r-1
$$
vertices.


::: pf-proof

Apply step [](#s1-5){.pf-ref} with
$$
n'=r+1.
$$
This gives a subgraph
$$
H
$$
on
$$
r+1
$$
vertices with
$$
e(H)
\ge
t_{r-1}(r+1)+1.
$$
By step [](#s1-8){.pf-ref},
$$
e(H)
\ge
\binom{r+1}{2}-1.
$$
Thus
$$
H
$$
is either
$$
K_{r+1}
$$
or
$$
K_{r+1}
$$
with one edge
$$
xy
$$
deleted.

In the complete case, any two distinct
$$
r
$$
-vertex subsets give two copies of
$$
K_r
$$
whose intersection has
$$
r-1
$$
vertices.

In the one-edge-missing case,
$$
H-x
$$
and
$$
H-y
$$
are both copies of
$$
K_r.
$$
Their vertex sets intersect in the remaining
$$
r-1
$$
vertices.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} states Turán's theorem, step [](#s1-5){.pf-ref} proves part (b), step [](#s1-7){.pf-ref} deduces Turán's theorem from part (b), and steps [](#s1-8){.pf-ref} and [](#s1-9){.pf-ref} prove the stronger conclusion.

:::

:::

:::
