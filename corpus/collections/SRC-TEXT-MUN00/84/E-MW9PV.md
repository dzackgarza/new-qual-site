---
schema: qual/card@1
id: E-MW9PV
kind: problem
title: Free ranks of complete and utilities graphs
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
    Munkres §84 Exercise 2, printed p. 513. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved thread is tmp/sources/mse-64192-E-MW9PV.md, read whole.
    Math StackExchange 64192 (asked 2011-09-13) computes the utilities graph: its question gets 4 generators
    from the formula 1 - chi of May's corollary, and answer 64200 by Jason DeVito confirms the count and
    shows that the number of free generators of an embedded graph has no bearing on the surface; answer
    64204 by Rando-Man observes that the induced map on pi_1 of the embedding is not injective. The complete
    graph is not computed in the thread, and the 1 - chi formula is quoted there rather than proved. The card
    therefore keeps its own counts for both graphs and now records the thread with its URLs and what it does
    not supply; the formula is Lemma 85.2 (printed p. 514) in this book. Rejected in the search: nothing else
    was returned for this exercise.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 84 Exercise 2, printed p. 513. The ranks (n-1)(n-2)/2 for the complete graph on n vertices and 4 for the utilities graph K_{3,3}, from rank = 1 - chi. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. The two answers, (n-1)(n-2)/2 and 4, are correct and are unchanged. Corrected: the proof obtained the rank from Lemma 85.2 (printed p. 514), which is a theorem of §85 stated after this exercise; the rank is now obtained from the theorems of §84 that the exercise precedes, namely Theorem 84.4 (printed p. 509), that a maximal tree contains every vertex, and Theorem 84.7 (printed p. 511), that the fundamental group of a connected graph is free with one generator for each edge outside a maximal tree. Corrected: the two graphs were not said to be connected or brought under the hypotheses of those theorems, and the count is now made with the hypothesis of connectivity checked (a complete graph on n >= 1 vertices and K_{3,3} are connected). What the certificate does not cover: the identification of the utilities graph with K_{3,3} is the usual one and the printed exercise's reference to §64; it is not proved here.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the count into numbered steps: the rank formula E - V + 1 from Theorem 84.4 and
    Theorem 84.7, the vertex and edge counts of K_n and of K_{3,3}, and the two evaluations, with
    connectivity of both graphs checked as a hypothesis of those theorems. Also supplied the point
    the earlier text left implicit: that a tree on V vertices has exactly V - 1 edges, which is what
    turns "every vertex lies in T" into the arithmetic. The mathematics is the earlier reading's;
    no defect found. Not re-read this session: printed pp. 509 and 511.
---

::: {.exercise}

What is the cardinality of a system of free generators for the fundamental group of the complete graph on $n$ vertices?
of the utilities graph?
(See §64.)

:::

::: {.solution}

The counts are the card's own; the one published thread on the utilities graph (Math Stack Exchange question 64192, answers 64200 and 64204) computes it from the $1-\chi$ corollary of May but neither computes the complete graph nor proves the formula, as the card's audit records. The statement was checked against Munkres, *Topology* (2000), §84 Exercise 2, printed p. 513, and the theorems used are of that section.

A graph means a $1$-dimensional CW complex, with $V$ vertices and $E$ edges.

::: pf

::: {.pf-step #tree}
A tree on $V$ vertices has exactly $V-1$ edges.

::: pf-proof
Induction on $V$: for $V=1$ there are no edges. For $V>1$ a finite tree has a vertex of degree $1$, since an endpoint of a longest simple path has no neighbour other than its successor on that path; deleting it and its single incident edge leaves a tree on $V-1$ vertices, which has $V-2$ edges by induction, so the original has $V-1$.
:::

:::

::: {.pf-step #rank}
For a finite connected graph $X$ with $V$ vertices and $E$ edges, $\operatorname{rank}\pi_{1}(X)=E-V+1$.

::: pf-proof
By Theorem 84.4 (printed p. 509) a maximal tree $T\subset X$ contains every vertex of $X$, so by step [](#tree){.pf-ref} it has $V-1$ edges. By Theorem 84.7 (printed p. 511) $\pi_{1}(X)$ is free with a system of free generators in bijection with the edges of $X$ outside $T$, of which there are $E-(V-1)=E-V+1$.
:::

:::

::: {.pf-step #kn}
For the complete graph $K_{n}$ on $n\geq1$ vertices, $\operatorname{rank}\pi_{1}(K_{n})=\frac{(n-1)(n-2)}{2}$.

::: pf-proof
$K_{n}$ is connected, any two distinct vertices being joined by an edge (and for $n=1$ the graph is a point). It has $V=n$ and one edge per unordered pair of distinct vertices, so $E=\frac{n(n-1)}{2}$. Then
$$
\operatorname{rank}\pi_{1}(K_{n})=\frac{n(n-1)}{2}-n+1=\frac{n^{2}-3n+2}{2}=\frac{(n-1)(n-2)}{2}
$$
by step [](#rank){.pf-ref}.
:::

:::

::: {.pf-step #utilities}
For the utilities graph $K_{3,3}$, $\operatorname{rank}\pi_{1}(K_{3,3})=4$.

::: pf-proof
$K_{3,3}$ is connected, since any two vertices are joined by an edge or by a two-edge path through one of the three vertices on the opposite side. It has $V=6$ and $E=9$, so step [](#rank){.pf-ref} gives $9-6+1=4$.
:::

:::

::: {.pf-step}
A system of free generators has $\frac{(n-1)(n-2)}{2}$ elements for the complete graph on $n$ vertices and $4$ for the utilities graph.

::: pf-proof
The size of a system of free generators of a free group is its rank, so steps [](#kn){.pf-ref} and [](#utilities){.pf-ref} are the two answers. The identification of the utilities graph with $K_{3,3}$ is the exercise's own reference to §64 and is not reproved here.
:::

:::

:::

:::
