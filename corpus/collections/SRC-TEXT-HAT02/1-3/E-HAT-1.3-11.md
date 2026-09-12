---
schema: qual/card@1
id: E-HAT-1.3-11
kind: problem
title: "Common covering space without a common cover"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: >-
    Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 11.
    Hatcher's covering-space definition allows nonsurjective maps, so the literal
    statement needs the intended connected-common-base interpretation; Hatcher's
    later published clarification gives the same two-vertex, three-edge construction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Constructed the common double cover explicitly and proved neither quotient graph can nontrivially cover a connected graph.
---

Construct finite graphs $X_1$ and $X_2$ having a common finite-sheeted covering space $\tilde{X}_1 = \tilde{X}_2$, but such that there is no space having both $X_1$ and $X_2$ as covering spaces.

::: remark
Under Hatcher's convention a covering map need not be surjective, so the literal statement would fail for the disconnected common target $X_1\sqcup X_2$.
The intended statement is that there is no **connected** space covered by both $X_1$ and $X_2$; equivalently, one may require covering maps to be surjective.
:::

::: {.solution}
Let $X_1$ be the theta graph: two vertices joined by three distinct edges.
Let $X_2$ be the dumbbell graph: two vertices joined by one edge, with one loop attached at each vertex.

<1>1. Construct a graph $Z$ from two circles $C_1,C_2$ by choosing two antipodal vertices $N_i,S_i$ on each circle and adjoining one edge from $N_1$ to $N_2$ and one edge from $S_1$ to $S_2$.
Then $Z$ has four vertices and six edges.
::: {.proof}
Each circle is subdivided by its two chosen vertices into two edges, so the two circles contribute four edges.
The two joining edges contribute two more.
:::

<1>2. There is a free involution $\alpha$ of $Z$ whose quotient is $X_1$.
::: {.proof}
Define $\alpha$ by
\[
N_1\leftrightarrow S_2,
\qquad
S_1\leftrightarrow N_2.
\]
Choose the two semicircle edges of $C_1$ to map to the corresponding opposite semicircle edges of $C_2$, and interchange the two joining edges.
No vertex or edge interior point is fixed.

The two vertex orbits give two quotient vertices.
The four semicircle edges form two edge orbits joining these vertices, and the two joining edges form a third such orbit.
Hence
\[
Z/\langle\alpha\rangle\cong X_1.
\]
Because the action is free on vertices and edge interiors, the quotient map
\[
Z\to X_1
\]
is a two-sheeted covering.
:::

<1>3. There is a second free involution $\beta$ of $Z$ whose quotient is $X_2$.
::: {.proof}
Define $\beta$ by
\[
N_i\leftrightarrow S_i
\qquad(i=1,2),
\]
interchanging the two semicircle edges of each $C_i$ and interchanging the two joining edges.
Again no vertex or edge interior point is fixed.

The two vertices $N_1,S_1$ form one orbit and $N_2,S_2$ the other.
For each $i$, the two semicircles of $C_i$ form one edge orbit whose image is a loop at the corresponding quotient vertex.
The two joining edges form one edge orbit joining the quotient vertices.
Thus
\[
Z/\langle\beta\rangle\cong X_2,
\]
and
\[
Z\to X_2
\]
is also a two-sheeted covering.
:::

<1>4. Hence $X_1$ and $X_2$ have the common finite-sheeted covering space $Z$.
::: {.proof}
This is <1>2--<1>3.
:::

<1>5. Neither $X_1$ nor $X_2$ admits a nontrivial covering map onto a connected graph.
::: {.proof}
Both graphs have exactly two branch vertices, and every branch vertex has valence $3$.
Let
\[
p:X_i\to W
\]
be a covering with $W$ connected.
The valence of a point is preserved by a local homeomorphism, so the preimage of every valence-$3$ vertex of $W$ consists of valence-$3$ vertices of $X_i$.
Since $X_i$ has exactly two such vertices and the number of sheets is constant on connected $W$, the degree of $p$ is either $1$ or $2$.

If the degree were $2$, then $W$ would have exactly one valence-$3$ vertex.
But a finite graph has an even number of odd-valence vertices, since
\[
\sum_v \deg(v)=2|E|.
\]
All other points of $W$ have valence $2$, so this is impossible.
Therefore the degree is $1$, and $p$ is an isomorphism of covering spaces.
:::

<1>6. The graphs $X_1$ and $X_2$ are not homeomorphic.
::: {.proof}
In $X_2$, the unique edge joining the two loop vertices is a separating edge: deleting an interior point of it disconnects the graph.
In the theta graph $X_1$, deleting an interior point of any edge leaves the other two edges joining the two vertices, so the graph remains connected.
This topological property distinguishes the two graphs.
:::

<1>7. Therefore no connected space is covered by both $X_1$ and $X_2$.
::: {.proof}
If a connected graph $W$ were covered by both, <1>5 would force both covering maps to have degree $1$.
Hence
\[
X_1\cong W\cong X_2,
\]
contradicting <1>6.
:::
:::
