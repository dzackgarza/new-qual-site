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
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 84 Exercise 2, printed p. 513. The ranks (n-1)(n-2)/2 for the complete graph on n vertices and 4 for the utilities graph K_{3,3}, from rank = 1 - chi. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. The two answers, (n-1)(n-2)/2 and 4, are correct and are unchanged. Corrected: the proof obtained the rank from Lemma 85.2 (printed p. 514), which is a theorem of §85 stated after this exercise; the rank is now obtained from the theorems of §84 that the exercise precedes, namely Theorem 84.4 (printed p. 509), that a maximal tree contains every vertex, and Theorem 84.7 (printed p. 511), that the fundamental group of a connected graph is free with one generator for each edge outside a maximal tree. Corrected: the two graphs were not said to be connected or brought under the hypotheses of those theorems, and the count is now made with the hypothesis of connectivity checked (a complete graph on n >= 1 vertices and K_{3,3} are connected). What the certificate does not cover: the identification of the utilities graph with K_{3,3} is the usual one and the printed exercise's reference to §64; it is not proved here.
---

::: {.exercise}

What is the cardinality of a system of free generators for the fundamental group of the complete graph on $n$ vertices?
of the utilities graph?
(See §64.)

:::

::: {.solution}

Let $X$ be a finite connected graph with $V$ vertices and $E$ edges. By Theorem 84.4 (printed p. 509) a maximal tree $T$ in $X$ contains all $V$ vertices, and a tree with $V$ vertices has $V-1$ edges; by Theorem 84.7 (printed p. 511) the group $\pi_1(X)$ is free, with a system of free generators in bijective correspondence with the edges of $X$ not in $T$. Hence
$$
\operatorname{rank}\pi_1(X)=E-(V-1)=E-V+1.
$$

For the complete graph $K_n$ on $n$ vertices, $V=n$ and $E=\binom n2$, and $K_n$ is connected for $n\ge1$. So
$$
\operatorname{rank}\pi_1(K_n)
=\binom n2-n+1
=\frac{(n-1)(n-2)}2 .
$$

The utilities graph is the complete bipartite graph $K_{3,3}$. It has $6$ vertices and $3\cdot3=9$ edges, and it is connected. Hence
$$
\operatorname{rank}\pi_1(K_{3,3})=9-6+1=4.
$$
Thus the required cardinalities are
$$
\boxed{\frac{(n-1)(n-2)}2\quad\text{and}\quad4.}
$$

:::
