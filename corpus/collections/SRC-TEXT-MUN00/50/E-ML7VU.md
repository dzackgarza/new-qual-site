---
schema: qual/card@1
id: E-ML7VU
kind: problem
title: The topologist's sine curve has dimension one
classification:
  areas:
  - topology
  topics:
  - Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked against Munkres, Topology (2000), §50 Exercise 3, printed p. 315, with Example 2 (the interval has
    dimension 1), Corollary 50.3 and Theorem 50.1 for the pieces, and the card of Exercise 50.2 for the lower
    bound. What the card cannot do with the book alone: the decomposition of the sine curve into the closed arcs
    A_n and the closed vertical interval is countable, and the book proves only the finite closed-sum theorem
    (Theorem 50.2); the passage to countably many closed pieces is the countable closed-sum theorem of dimension
    theory, which the card states, cites by author and title (Engelking, Theory of Dimensions Finite and
    Infinite, Theorem 1.5.3; Hurewicz and Wallman, Dimension Theory) and does not prove. Neither book is in the
    checkout and no page of either has been read here, so the citation is by theorem number only, and the card is
    listed in COMPLAINTS.md as the one card of this batch whose proof rests on a borrowed theorem rather than on
    the book.
---

::: {.exercise}

Show that the topologist's sine curve has dimension 1.
:::

::: {.solution}
Let
$$
T=\{(x,\sin(1/x)):0<x\le1\}\cup(\{0\}\times[-1,1])
$$
be the topologist's sine curve.

For $n\ge1$, put
$$
A_n=\{(x,\sin(1/x)):1/(n+1)\le x\le1/n\},
$$
and let
$$
V=\{0\}\times[-1,1].
$$
Each $A_n$ is the continuous image of a compact interval under the embedding
$$
x\longmapsto (x,\sin(1/x)),
$$
so it is an arc, hence homeomorphic to a closed interval and therefore has covering dimension $1$. The set $V$ is also an arc, so $\dim V=1$. Each $A_n$ and $V$ is compact, hence closed in the metric space $T$, and
$$
T=V\cup\bigcup_{n\ge1}A_n.
$$

The sets $F_n=V\cup A_1\cup\cdots\cup A_n$, for $n\ge1$, are closed in $T$ (each $A_j$ and $V$ is compact, hence closed in the metric space $T$), they increase with $n$, and their union is $T$. Each $F_n$ is a finite union of closed subspaces of dimension at most $1$, so $\dim F_n\le1$ by Corollary 50.3.

At this point the book's own tools give only the finite case, Theorem 50.2 and its corollary. The passage from the countably many closed pieces $F_n$ to $T$ is the countable closed-sum theorem of dimension theory: if a metrizable space is the union of countably many closed subspaces of dimension at most $m$, then its dimension is at most $m$. The book states and proves the finite case only, and this theorem is quoted here rather than proved: it is Theorem 1.5.3 of Ryszard Engelking, *Theory of Dimensions, Finite and Infinite* (Heldermann, 1995), and the corresponding sum theorem of Witold Hurewicz and Henry Wallman, *Dimension Theory* (Princeton, 1941). Applying it with $m=1$ gives
$$
\dim T\le 1 .
$$

On the other hand, $T$ is connected, is $T_1$ (indeed metric), and contains more than one point. By [[E-KWBI9]], every such space has dimension at least $1$. Thus
$$
\boxed{\dim T=1}.
$$
:::
