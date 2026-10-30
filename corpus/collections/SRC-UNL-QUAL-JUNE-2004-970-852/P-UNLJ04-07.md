---
schema: qual/card@1
id: P-UNLJ04-07
kind: problem
title: Connectivity of cubic graphs and snarls
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Question 7 of the retained June 2004 UNL Mathematics Qualifying Exam 970/852 PDF.
---

::: {.problem}
a. Prove that every cubic 3 edge-connected graph is 3-connected.

b. Let us define a snarl as a graph that can be obtained from $K _ { 4 }$ by repeated applications of the operation of subdividing two edges and joining the two new vertices.
   Show that every snarl is 3-connected.
   (In fact it is true that every 3-connected cubic graph is a snarl.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let
$$
G
$$
be cubic and $3$-edge-connected.
Then
$$
G
$$
has no cut vertex.


::: pf-proof

Suppose
$$
v
$$
were a cut vertex.
Then
$$
G-v
$$
has at least two components.

The three edges incident to
$$
v
$$
are distributed among these components.
Hence some component
$$
C
$$
is incident to at most one of those three edges.

Every edge from
$$
C
$$
to
$$
V(G)\setminus C
$$
must be incident to
$$
v,
$$
because
$$
C
$$
is a component of
$$
G-v.
$$
Thus at most one edge leaves
$$
C.
$$
Deleting that edge disconnects
$$
G,
$$
contradicting $3$-edge-connectivity.

:::

:::

::: {.pf-step #s1-2}

Suppose
$$
\{u,v\}
$$
is a two-vertex cut of
$$
G.
$$
If
$$
G-\{u,v\}
$$
has at least three components, then
$$
G
$$
has an edge cut of size at most $2$.


::: pf-proof

At most
$$
\deg(u)+\deg(v)=6
$$
edges join the components of
$$
G-\{u,v\}
$$
to
$$
\{u,v\}.
$$
If there are at least three components, one component
$$
C
$$
is incident to at most
$$
2
$$
of these edges.

Those are all edges from
$$
C
$$
to its complement.
Deleting them disconnects
$$
G,
$$
contradicting $3$-edge-connectivity.

:::

:::

::: {.pf-step #s1-3}

Suppose
$$
G-\{u,v\}
$$
has exactly two components
$$
A
$$
and
$$
B.
$$
If fewer than three edges join either component to
$$
\{u,v\},
$$
then
$$
G
$$
has an edge cut of size at most $2$.


::: pf-proof

For either component, the set of edges joining it to
$$
\{u,v\}
$$
is exactly the edge boundary of that component.
If this boundary has size at most
$$
2,
$$
deleting it disconnects the graph, contradicting $3$-edge-connectivity.

:::

:::

::: {.pf-step #s1-4}

Hence, in the only remaining case, exactly three edges join
$$
A
$$
to
$$
\{u,v\},
$$
and exactly three edges join
$$
B
$$
to
$$
\{u,v\}.
$$
Moreover,
$$
uv\notin E(G).
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, each of the two components has at least three boundary edges, so together they account for at least six edges incident to
$$
u
$$
or
$$
v.
$$

Because
$$
G
$$
is cubic,
$$
u
$$
and
$$
v
$$
have only six incident edge slots in total.
Thus both boundaries have size exactly
$$
3.
$$

If
$$
uv
$$
were an edge, it would consume one degree at each of
$$
u
$$
and
$$
v,
$$
leaving only four edge slots from
$$
\{u,v\}
$$
to
$$
A\cup B,
$$
contradicting the six boundary edges just obtained.

:::

:::

::: {.pf-step #s1-5}

Let
$$
a
$$
be the number of edges from
$$
u
$$
to
$$
A,
$$
and let
$$
b
$$
be the number of edges from
$$
v
$$
to
$$
A.
$$
Then
$$
a+b=3.
$$
The cases
$$
(a,b)=(3,0)
\quad\text{and}\quad
(0,3)
$$
are impossible.


::: pf-proof

The equation
$$
a+b=3
$$
is the boundary-size statement from step [](#s1-4){.pf-ref}.

Suppose
$$
(a,b)=(3,0).
$$
Then all three neighbors of
$$
u
$$
lie in
$$
A,
$$
and because
$$
v
$$
has no neighbor in
$$
A
$$
and
$$
uv
$$
is absent, all three neighbors of
$$
v
$$
lie in
$$
B.
$$
There is then no edge joining
$$
A\cup\{u\}
$$
to
$$
B\cup\{v\},
$$
so
$$
G
$$
would be disconnected.

The case
$$
(a,b)=(0,3)
$$
is symmetric.

:::

:::

::: {.pf-step #s1-6}

In the remaining cases
$$
(a,b)=(1,2)
\quad\text{or}\quad
(2,1),
$$
the graph has a $2$-edge cut.


::: pf-proof

Assume
$$
(a,b)=(1,2).
$$
Since
$$
v
$$
has degree
$$
3
$$
and no edge
$$
uv,
$$
it has exactly one edge to
$$
B.
$$

Consider the vertex set
$$
A\cup\{v\}.
$$
Exactly two edges leave it:

1. the unique edge from
   $$
   A
   $$
   to
   $$
   u;
   $$

2. the unique edge from
   $$
   v
   $$
   to
   $$
   B.
   $$

Deleting these two edges disconnects the graph, contradicting $3$-edge-connectivity.

The case
$$
(a,b)=(2,1)
$$
is symmetric, using
$$
A\cup\{u\}.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore every cubic $3$-edge-connected graph is $3$-connected.


::: pf-proof

Step [](#s1-1){.pf-ref} rules out vertex cuts of size
$$
1.
$$
Steps [](#s1-2){.pf-ref} through [](#s1-6){.pf-ref} rule out vertex cuts of size
$$
2.
$$
Thus deleting fewer than three vertices never disconnects
$$
G,
$$
so
$$
G
$$
is $3$-connected.

:::

:::

::: {.pf-step #s1-8}

The graph
$$
K_4
$$
is cubic and $3$-connected.


::: pf-proof

Every vertex of
$$
K_4
$$
has degree
$$
3.
$$
Deleting one or two vertices leaves respectively
$$
K_3
$$
or
$$
K_2,
$$
both connected.
Hence
$$
K_4
$$
is $3$-connected.

:::

:::

::: {.pf-step #s1-9}

Let
$$
G
$$
be a cubic $3$-connected graph.
Form
$$
G'
$$
by subdividing two distinct edges
$$
ab
$$
and
$$
cd
$$
with new vertices
$$
x
$$
and
$$
y,
$$
respectively, and adding the edge
$$
xy.
$$
Then
$$
G'
$$
is cubic.


::: pf-proof

Subdividing
$$
ab
$$
replaces it by
$$
ax
$$
and
$$
xb,
$$
so the degrees of
$$
a
$$
and
$$
b
$$
do not change.
Likewise the degrees of
$$
c
$$
and
$$
d
$$
do not change.

The new vertex
$$
x
$$
has incident edges
$$
ax,xb,xy,
$$
so
$$
\deg(x)=3.
$$
Similarly,
$$
\deg(y)=3.
$$
All original vertices retain degree
$$
3.
$$

:::

:::

::: {.pf-step #s1-10}

If
$$
S\subseteq V(G')
$$
has
$$
\cardinality{S}\le2
$$
and
$$
S\cap\{x,y\}=\varnothing,
$$
then
$$
G'-S
$$
is connected.


::: pf-proof

The graph
$$
G-(S\cap V(G))
$$
is connected because
$$
G
$$
is $3$-connected.

Every occurrence of the original edge
$$
ab
$$
in a path can be replaced in
$$
G'
$$
by the path
$$
a-x-b,
$$
and every occurrence of
$$
cd
$$
can be replaced by
$$
c-y-d.
$$
Since
$$
x,y\notin S,
$$
these replacements remain available.

Thus all surviving original vertices lie in one connected component of
$$
G'-S.
$$
The vertices
$$
x
$$
and
$$
y
$$
are attached to surviving endpoints of their subdivided edges or to each other, so every surviving new vertex lies in that same component.

:::

:::

::: {.pf-step #s1-11}

If
$$
S=\{x,z\}
$$
with
$$
z\in V(G),
$$
then
$$
G'-S
$$
is connected.
The same holds with
$$
x
$$
and
$$
y
$$
interchanged.


::: pf-proof

Because
$$
G
$$
is $3$-connected,
$$
G-z
$$
is $2$-connected whenever it has at least three vertices.
In particular it has no bridge.

Deleting
$$
x
$$
from
$$
G'
$$
has the effect, on the original graph, of deleting the edge
$$
ab.
$$
Thus
$$
G'-\{x,z\}
$$
is obtained from
$$
G-z-ab
$$
by subdividing the surviving edge
$$
cd
$$
with
$$
y
$$
.

Since
$$
ab
$$
is not a bridge of
$$
G-z
$$
when both endpoints survive, deleting it does not disconnect
$$
G-z.
$$
If
$$
z
$$
is an endpoint of
$$
ab,
$$
that edge is already absent from
$$
G-z.
$$
Hence the resulting graph is connected in either case.

Subdividing an edge preserves connectedness, so
$$
G'-\{x,z\}
$$
is connected.

:::

:::

::: {.pf-step #s1-12}

The graph
$$
G'-\{x,y\}
$$
is connected.


::: pf-proof

Deleting
$$
x
$$
and
$$
y
$$
from
$$
G'
$$
corresponds to deleting the two original edges
$$
ab
$$
and
$$
cd
$$
from
$$
G.
$$

A $3$-connected graph has edge-connectivity at least
$$
3
$$
by the standard inequality
$$
\kappa(G)\le\lambda(G).
$$
Therefore deleting two edges cannot disconnect
$$
G.
$$
Hence
$$
G'-\{x,y\}
$$
is connected.

:::

:::

::: {.pf-step #s1-13}

The snarl operation preserves $3$-connectivity.


::: pf-proof

Let
$$
S\subseteq V(G')
$$
with
$$
\cardinality{S}\le2.
$$

If
$$
S
$$
contains neither new vertex, step [](#s1-10){.pf-ref} applies.

If
$$
S
$$
contains exactly one of
$$
x,y,
$$
then either
$$
S
$$
contains no other vertex, in which case the same argument as step [](#s1-11){.pf-ref} with no
$$
z
$$
is easier, or it contains one original vertex and step [](#s1-11){.pf-ref} applies.

If
$$
S=\{x,y\},
$$
step [](#s1-12){.pf-ref} applies.

Thus deleting fewer than three vertices from
$$
G'
$$
never disconnects it.

:::

:::

::: {.pf-step #s1-14}

Every snarl is $3$-connected.


::: pf-proof

Proceed by induction on the number of snarl operations.

The initial graph
$$
K_4
$$
is cubic and $3$-connected by step [](#s1-8){.pf-ref}.

Assume the current graph is cubic and $3$-connected.
Applying one snarl operation produces a cubic graph by step [](#s1-9){.pf-ref} and a $3$-connected graph by step [](#s1-13){.pf-ref}.

Therefore every graph obtained from
$$
K_4
$$
by finitely many such operations is $3$-connected.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} proves part (a), and step [](#s1-14){.pf-ref} proves part (b).

:::

:::

:::
