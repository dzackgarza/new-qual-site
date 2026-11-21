---
schema: qual/card@1
id: E-OQRAL
kind: problem
title: Euler numbers of standard graphs and their coverings
classification:
  areas:
  - topology
  topics:
  - Graphs
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §83 Exercise 2, printed p. 506. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md. No source was saved. The queries were the Stack Exchange advanced search
    "Euler number covering space graph n-fold" (no hits) and the similar-question search from "Euler
    characteristic of a finite covering space of a graph" (15 items). Both threads that came back were read
    and rejected: 369456 computes chi(Y) = n chi(X) for CW complexes through spectral sequences, which is not
    the graph count this exercise asks for, and 1499238 is about Stallings folds and proves nothing here. The
    card keeps its own proof, which counts vertices and edges of the covering graph over a maximal tree.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 83 Exercise 2, printed p. 506. Euler numbers of an arc, a circle, a wedge and the complete graph, and the multiplicativity of the Euler number under an n-fold covering. Checked against the definition of the Euler number, printed p. 505, and Theorem 85.1. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. The previous note said the definition of the Euler number is on printed p. 505 and cited Theorem 85.1; the definition is the first paragraph of this printed exercise, on p. 506, and is repeated in §85 on p. 514, and Theorem 85.1 has nothing to do with the exercise. Corrected: the value for a wedge of n circles was justified by the sentence "one more vertex than the total excess contributed by its n cycles", which says nothing; it is now computed from the model with one vertex and n loop edges. Corrected: the values for the circle and the wedge were said to hold "for any subdivision" with no reason; the proof now notes that subdividing an edge adds one vertex and one edge, so $V-E$ is unchanged, which is what makes the model-independent reading legitimate. Corrected: the relation under a covering was asserted from "every vertex has exactly r lifts and every edge has exactly r lifted edges" without saying where the lifted graph structure comes from; it now cites Theorem 83.4 (printed p. 505). What the certificate does not cover: the topological invariance of the Euler number is the next exercise (§85 Exercise 1), not proved here.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. Repair of notation: the exercise calls the total
    space of the covering E, and the count of edges was also written E, so the earlier
    prose contained both "E(E)" and "E(E) = rE(X)"; the total space is written Y below
    and the step says why. Pages checked: the definition of the Euler number is the first
    sentence of this exercise on printed p. 506, and Theorem 83.4, which gives the graph
    structure of the total space and the homeomorphism of each edge onto its image, is on
    printed p. 505. Each value re-checked: subdivision adds one vertex and one edge, which
    is what authorizes the one-vertex model of the circle and the n-loop model of the
    wedge; the arc gives 1; the wedge 1-n, agreeing with the circle at n=1 and the arc at
    n=0; the complete graph gives n - C(n,2) = n(3-n)/2, agreeing with a point at n=1 and
    an arc at n=2. In the covering part, both counts are now derived rather than asserted:
    the components of the preimage of an edge correspond to the points of the fibre over an
    interior point, giving r edges per edge of X; and the points over a vertex of X are
    vertices of Y, since a point of Y over a vertex cannot be interior to an edge of Y
    (its image would then be an edge of X having a vertex as an interior point). What is
    not proved here, as before: the topological invariance of the Euler number, which is
    §85 Exercise 1.
---

::: {.exercise}

The Euler number of a finite linear graph $X$ equals the number of vertices of $X$ minus the number of edges of $X$.
It is in fact a topological invariant of $X$, as we shall see.
What is the Euler number of an arc?
a circle?
a wedge of $n$ circles?
the complete graph on $n$ vertices?
If $E$ is an $n$-fold covering space of $X$, how are the Euler numbers of $E$ and $X$ related?

:::

::: {.solution}
The argument is the card's own; no retained set solves this exercise, as the audit records. In the last part the total space of the covering, called $E$ in the exercise, is written $Y$, because $E$ also denotes a number of edges in this count.

Throughout, $X$ is a finite linear graph with $V(X)$ vertices and $e(X)$ edges, and $\chi(X)=V(X)-e(X)$ (printed p. 506, where the exercise states the definition; the exercise is §83 Exercise 2, printed p. 506). A covering $p:Y\to X$ of degree $r$ is one with $\cardinality{p^{\inverseof{}}(x)}=r$ for every $x\in X$.

::: pf

::: {.pf-step #well-defined}
Subdividing an edge of a finite graph replaces one edge by two and adds one vertex, so $V-e$ is unchanged; in particular a value of $\chi$ computed from any model obtained by subdividing a given one is a value for the graph.

::: pf-proof
A subdivision of an edge $A$ inserts a new vertex in the interior of $A$ and cuts $A$ into the two closed subarcs meeting at it; no other vertex or edge is created or destroyed, so $V$ increases by $1$ and $e$ by $1$, and $V-e$ is the same. This is what makes it legitimate to compute $\chi$ from a convenient model, the circle below being the one place where that is used.
:::

:::

::: {.pf-step #arc}
An arc has $\chi=1$.

::: pf-proof
An arc is the graph with two vertices and the single edge between them, so $V=2$ and $e=1$, and $\chi=2-1=1$.
:::

:::

::: {.pf-step #circle}
A circle has $\chi=0$.

::: pf-proof
In the model with one vertex and the single loop edge, $V=1$ and $e=1$, so $\chi=0$; and every other model of the circle is obtained by subdividing this one, which by step [](#well-defined){.pf-ref} does not change $V-e$.
:::

:::

::: {.pf-step #wedge}
A wedge of $n$ circles has $\chi=1-n$.

::: pf-proof
The model is one vertex, the wedge point, with $n$ loop edges, one for each circle, so $V=1$ and $e=n$, and $\chi=1-n$. For $n=1$ this is the value for the circle in step [](#circle){.pf-ref}, and for $n=0$ the value $1$ for the arc in step [](#arc){.pf-ref}.
:::

:::

::: {.pf-step #complete}
The complete graph $K_n$ on $n\ge1$ vertices has $\chi(K_n)=n(3-n)/2$.

::: pf-proof
$K_n$ is the graph on $n$ vertices in which every pair of distinct vertices is joined by exactly one edge, so $V=n$ and $e=\binom n2=n(n-1)/2$; it is a finite linear graph, realized by placing the $n$ vertices on a circle in $\RR^3$ and drawing the chords in general position. Hence
$$
\chi(K_n)=n-\frac{n(n-1)}{2}=\frac{2n-n^2+n}{2}=\frac{n(3-n)}{2}.
$$
For $n=1$ this is $1$, the value for a single point, and for $n=2$ it is $1$, the value for an arc, as it should be.
:::

:::

::: {.pf-step}
For an $r$-fold covering $p:Y\to X$ of finite graphs, $\chi(Y)=r\,\chi(X)$.

::: pf-proof

::: {.pf-step #edges}
Every edge of $X$ is the image of exactly $r$ edges of $Y$.

::: pf-proof
By Theorem 83.4 (printed p. 505) the space $Y$ is a linear graph whose edges are the path components of the sets $p^{\inverseof{}}(A)$ for edges $A$ of $X$, and $p$ maps each such component homeomorphically onto $A$. Fix an edge $A$ and a point $a$ in its interior; the components of $p^{\inverseof{}}(A)$ partition $p^{\inverseof{}}(A)$, so they correspond bijectively to the points of the fibre $p^{\inverseof{}}(a)$, since each component meets the fibre in exactly one point (it maps homeomorphically onto $A$). That fibre has exactly $r$ points, so $A$ is the image of exactly $r$ edges of $Y$.
:::

:::

::: {.pf-step #vertices}
Every vertex of $X$ is the image of exactly $r$ vertices of $Y$.

::: pf-proof
A vertex of $Y$ is an endpoint of an edge $B$ of $Y$, and $p$ maps $B$ homeomorphically onto the edge $p(B)$ of $X$ (Theorem 83.4, printed p. 505), carrying endpoints to endpoints; so the image of a vertex of $Y$ is a vertex of $X$. Conversely, let $v$ be a vertex of $X$ and $y\in p^{\inverseof{}}(v)$. If $y$ were an interior point of an edge $B$ of $Y$, then $p(B)$ would be an edge of $X$ containing $v=p(y)$ as an interior point, since $p$ restricts to a homeomorphism of $B$ onto $p(B)$; but the vertices of a linear graph are the endpoints of its edges and the edges of a linear graph meet only at their endpoints, so the interior of an edge contains no vertex. Hence every point of $p^{\inverseof{}}(v)$ is a vertex of $Y$, and the vertices of $Y$ over $v$ are exactly the $r$ points of that fibre.
:::

:::

::: {.pf-step #mult}
$\chi(Y)=r\,\chi(X)$.

::: pf-proof
Summing the counts of steps [](#edges){.pf-ref} and [](#vertices){.pf-ref} over the finitely many edges and vertices of $X$ gives $e(Y)=r\,e(X)$ and $V(Y)=r\,V(X)$; hence $\chi(Y)=V(Y)-e(Y)=r(V(X)-e(X))=r\,\chi(X)$.
:::

:::

:::

:::

:::
:::
