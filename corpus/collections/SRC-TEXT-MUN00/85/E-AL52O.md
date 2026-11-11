---
schema: qual/card@1
id: E-AL52O
kind: problem
title: The Euler number is a topological invariant
classification:
  areas:
  - topology
  topics:
  - Graphs
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 85 Exercise 1, printed p. 515. The Euler number is a topological invariant, by counting the cells of a subdivision and Theorem 84.2. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. Corrected: the proof cited "Theorem 84.1" for the statement that the projection onto the quotient by a contractible subcomplex is a homotopy equivalence, which is false, and it used CW pairs and homology, neither of which the book develops in these chapters. The invariance is now proved from the book's own results: Theorem 84.4 (printed p. 509) and Theorem 84.7 (printed p. 511) give that the fundamental group of a connected finite graph with V vertices and E edges is free of rank E - V + 1, Corollary 52.5 (printed p. 334) gives that a homeomorphism induces an isomorphism of fundamental groups, and Corollary 69.5 (printed p. 423), with Theorem 67.8 (printed p. 411) behind it, gives that any system of free generators of a finitely generated free group has as many elements as any other. So the rank, hence 1 - chi, is an invariant of the space. Corrected: the disconnected case summed "the ranks of the components" as if the rank of a free group on several components were defined; it now sums the Euler numbers of the components, which add because vertices and edges do, and uses that a homeomorphism carries components to components. Corrected: the structure was not a Lamport proof -- steps had claims without proofs and a "Q.E.D." was typed. What the certificate does not cover: subdivision invariance of V - E is used only through Theorem 84.7's count, so no separate argument about subdivisions is needed.
---

::: {.exercise}

Show that the Euler number of a finite linear graph $X$ is a topological invariant of $X$.
[Hint: First consider the case where $X$ is connected.]

:::

::: {.solution}

For a finite linear graph with $V$ vertices and $E$ edges, the Euler number is $\chi(X)=V-E$ (Definition, printed p. 514). A homeomorphism $h:X\to Y$ of finite linear graphs induces an isomorphism $h_*$ of fundamental groups at corresponding base points (Corollary 52.5, printed p. 334).

::: pf

::: {.pf-step #connected}

If $X$ is connected, then $\chi(X)=1-\operatorname{rank}\pi_1(X,x_0)$, and $\chi(X)=\chi(Y)$ for every finite linear graph $Y$ homeomorphic to $X$.

::: pf-proof

::: {.pf-step}

$\chi(X)=1-\operatorname{rank}\pi_1(X,x_0)$.

::: {.pf-proof}

Let $T$ be a maximal tree in the connected graph $X$. By Theorem 84.4 (printed p. 509) $T$ contains all $V$ vertices, and a tree with $V$ vertices has $V-1$ edges. By Theorem 84.7 (printed p. 511) the fundamental group of $X$ is free, with a system of free generators in bijective correspondence with the $E-(V-1)$ edges of $X$ not in $T$. So
$$
\operatorname{rank}\pi_1(X,x_0)=E-V+1=1-\chi(X).
$$

:::

:::

::: {.pf-step}

$\operatorname{rank}\pi_1$ depends only on the group.

::: {.pf-proof}

If a free group has $n$ free generators, then every system of free generators for it has $n$ elements (Corollary 69.5, printed p. 423, whose proof passes to the free abelian group $G/[G,G]$ and uses Theorem 67.8, printed p. 411, that the number of elements in a finite basis of a free abelian group is determined by the group). Hence the number $\operatorname{rank}\pi_1(X,x_0)$ is an invariant of the isomorphism class of $\pi_1(X,x_0)$.

:::

:::

::: {.pf-step}

$\chi(X)=\chi(Y)$.

::: {.pf-proof}

Let $h:X\to Y$ be a homeomorphism and put $y_0=h(x_0)$; then $h_*:\pi_1(X,x_0)\to\pi_1(Y,y_0)$ is an isomorphism (Corollary 52.5, printed p. 334), so $\pi_1(Y,y_0)$ is free with $\operatorname{rank}\pi_1(X,x_0)$ generators. Since $Y$ is homeomorphic to the connected space $X$ it is connected, so the first step applied to $Y$ gives $\chi(Y)=1-\operatorname{rank}\pi_1(Y,y_0)=1-\operatorname{rank}\pi_1(X,x_0)=\chi(X)$.

:::

:::

:::

:::

::: {.pf-step}

For every finite linear graph $X$, $\chi(X)$ is a topological invariant.

::: pf-proof

Let $X$ have components $X_1,\dots,X_c$. Each component of a linear graph is a subgraph, because it contains every edge that meets it, and it is a finite linear graph. The vertices and the edges of $X$ are the disjoint unions of those of the components, so
$$
V=\sum_{i=1}^c V_i,\qquad E=\sum_{i=1}^c E_i,\qquad \chi(X)=\sum_{i=1}^c\chi(X_i).
$$
A homeomorphism $h:X\to Y$ carries components of $X$ onto components of $Y$ and restricts to a homeomorphism of each component with its image, so by step [](#connected){.pf-ref} it pairs the components of $X$ with those of $Y$ having equal Euler number. Hence
$$
\chi(Y)=\sum_{i=1}^c\chi(X_i)=\chi(X).
$$

:::

:::

:::

:::
