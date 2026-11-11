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
    Checked against Munkres, Topology (2000), Section 84 Exercise 2, printed p. 513. The ranks (n-1)(n-2)/2 for the complete graph on n vertices and 4 for the utilities graph, which is K_{3,3} with 9 edges and 6 vertices, both from rank = 1 - chi and Lemma 85.2. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

What is the cardinality of a system of free generators for the fundamental group of the complete graph on $n$ vertices?
of the utilities graph?
(See §64.)
:::

::: {.solution}
For a finite connected graph $X$, Lemma 85.2 gives
$$
\operatorname{rank}\pi_1(X)=1-\chi(X)=E-V+1.
$$

For the complete graph $K_n$,
$$
V=n,\qquad E=\binom n2,
$$
so
$$
\operatorname{rank}\pi_1(K_n)
=\binom n2-n+1
=\frac{(n-1)(n-2)}2.
$$

The utilities graph is $K_{3,3}$. It has $6$ vertices and $3\cdot3=9$ edges. Hence
$$
\operatorname{rank}\pi_1(K_{3,3})=9-6+1=4.
$$
Thus the required cardinalities are
$$
\boxed{\frac{(n-1)(n-2)}2\quad\text{and}\quad4.}
$$
:::
