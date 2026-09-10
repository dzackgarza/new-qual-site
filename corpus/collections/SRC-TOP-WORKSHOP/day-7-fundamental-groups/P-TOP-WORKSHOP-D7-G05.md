---
schema: qual/card@1
id: P-TOP-WORKSHOP-D7-G05
kind: problem
title: An index-four subgroup and covering space of a free group
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Groups
  - Cell Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $F(a,b)$ be the free group of two generators.
What are the presentation complex and the Cayley complex for $F(a,b)$?
Find an index $4$ subgroup and the covering space that corresponds to it.
:::

::: {.solution}
The presentation complex for
\[
F(a,b)=\langle a,b\mid\ \rangle
\]
is the wedge of two circles \(S^1_a\vee S^1_b\): one vertex and two oriented \(1\)-cells, with no \(2\)-cells. Its Cayley complex is therefore just its Cayley graph, the \(4\)-regular tree with vertices indexed by \(F(a,b)\) and directed \(a\)- and \(b\)-edges
\[
g\longrightarrow ga,\qquad g\longrightarrow gb.
\]

For an index-four subgroup, define
\[
\phi:F(a,b)\twoheadrightarrow\mathbb Z/4,
\qquad \phi(a)=1,\quad \phi(b)=0,
\]
and let \(H=\ker\phi\). Then \([F(a,b):H]=4\).

The corresponding based covering graph has vertices \(v_0,v_1,v_2,v_3\). For each \(i\pmod4\), there is an \(a\)-edge from \(v_i\) to \(v_{i+1}\), and there is a \(b\)-loop at every \(v_i\). The covering map sends every \(a\)-edge to the \(a\)-circle and every \(b\)-loop to the \(b\)-circle. It is visibly a connected four-sheeted cover of the two-petal rose.

With basepoint \(v_0\), a free basis for \(H\) is
\[
a^4,\quad b,\quad aba^{-1},\quad a^2ba^{-2},\quad a^3ba^{-3}.
\]
In particular \(H\) has rank \(5=1+4(2-1)\), as the covering graph also shows.
:::
