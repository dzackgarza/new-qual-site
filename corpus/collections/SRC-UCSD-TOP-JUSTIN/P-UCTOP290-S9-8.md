---
schema: qual/card@1
id: P-UCTOP290-S9-8
kind: problem
title: A torus triangulation needs at least fourteen triangles
classification:
  areas:
  - topology
  topics:
  - Triangulations
  - Euler Characteristic
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 9, Problem 8 in its checked-in extraction.
---

::: {.problem}
Prove that a simplicial triangulation of the
torus has at least fourteen two-simplices,
and exhibit one with fourteen.
:::

::: {.solution}

Let $V,E,F$ be the numbers of vertices, edges,
and triangles. Every edge lies in two triangles,
so $3F=2E$. Since the Euler characteristic
of the torus is zero,
$$
V-E+F=0,\qquad E=3V,\qquad F=2V.
$$
A simplicial complex has at most
$V(V-1)/2$ edges. Therefore
$3V\le V(V-1)/2$, which implies
$V\ge7$ and $F\ge14$.

For equality, label seven vertices by
$\ZZ_7$. Take the fourteen triangles
$$
\{i,i+1,i+3\},\qquad
\{i,i+2,i+3\},
\qquad i\in\ZZ_7,
$$
with indices modulo seven. Each pair
of vertices is an edge, and each edge
belongs to exactly two triangles.
The link of vertex $0$ is the cycle
$$
1-3-2-6-4-5-1;
$$
cyclic relabeling gives a six-cycle
at every vertex. Thus the complex
is a connected closed surface.
Orient the first family of triangles
as $(i,i+1,i+3)$ and the second
in the reverse of $(i,i+2,i+3)$.
The induced orientations cancel on
each common edge, so the surface is
orientable. It has
$V-E+F=7-21+14=0$, hence is a torus.
:::
