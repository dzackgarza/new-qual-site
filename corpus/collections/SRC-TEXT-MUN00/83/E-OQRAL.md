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
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 83 Exercise 2, printed p. 506. Euler numbers of an arc, a circle, a wedge and the complete graph, and the multiplicativity of the Euler number under an n-fold covering. Checked against the definition of the Euler number, printed p. 505, and Theorem 85.1. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. The previous note said the definition of the Euler number is on printed p. 505 and cited Theorem 85.1; the definition is the first paragraph of this printed exercise, on p. 506, and is repeated in §85 on p. 514, and Theorem 85.1 has nothing to do with the exercise. Corrected: the value for a wedge of n circles was justified by the sentence "one more vertex than the total excess contributed by its n cycles", which says nothing; it is now computed from the model with one vertex and n loop edges. Corrected: the values for the circle and the wedge were said to hold "for any subdivision" with no reason; the proof now notes that subdividing an edge adds one vertex and one edge, so $V-E$ is unchanged, which is what makes the model-independent reading legitimate. Corrected: the relation under a covering was asserted from "every vertex has exactly r lifts and every edge has exactly r lifted edges" without saying where the lifted graph structure comes from; it now cites Theorem 83.4 (printed p. 505). What the certificate does not cover: the topological invariance of the Euler number is the next exercise (§85 Exercise 1), not proved here.
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

For a finite graph, the Euler number is
$$
\chi(X)=V-E,
$$
the number of vertices minus the number of edges (printed p. 506). Subdividing an edge replaces it by two edges and adds one vertex, so $V-E$ does not change: the value depends on the graph, not on the model chosen for it.

An arc has $V=2$, $E=1$, hence
$$
\chi=1.
$$

A circle, in any model, has as many vertices as edges, because one may start from a model with $V=E=1$ and each subdivision adds one of each; so
$$
\chi=0 .
$$

A wedge of $n$ circles has a model with one vertex and $n$ loop edges, hence
$$
\chi=1-n .
$$
This agrees with the value for $n=1$ above and with the arc for $n=0$.

The complete graph $K_n$ has
$$
V=n,\qquad E=\binom n2,
$$
so
$$
\chi(K_n)=n-\binom n2=\frac{n(3-n)}2 .
$$

Finally, let $p:E\to X$ be an $r$-fold covering of a finite graph. By Theorem 83.4 (printed p. 505) the space $E$ is a linear graph whose edges are the path components of the sets $p^{-1}(A)$ for edges $A$ of $X$, and each of those components maps homeomorphically onto $A$. Hence every edge of $X$ is the image of exactly $r$ edges of $E$, and every vertex of $X$ is the image of exactly $r$ vertices of $E$. Therefore
$$
V(E)=rV(X),\qquad E(E)=rE(X),
$$
and hence
$$
\boxed{\chi(E)=r\chi(X).}
$$

:::
