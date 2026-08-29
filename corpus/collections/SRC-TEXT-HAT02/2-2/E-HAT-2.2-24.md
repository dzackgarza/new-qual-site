---
schema: qual/card@1
id: E-HAT-2.2-24
kind: exercise
title: 1-skeleton of $S^2$ from polygon identifications cannot be certain graphs
classification:
  areas:
  - topology
  topics:
  - Homology
  - CW Complexes
  - Euler Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Suppose we build $S^2$ from a finite collection of polygons by identifying edges in pairs.
Show that in the resulting CW structure on $S^2$ the 1 skeleton cannot be either of the two graphs shown, with five and six vertices.
[This is one step in a proof that neither of these graphs embeds in $\mathbb{R}^2$.]

::: {.solution}
<1>1. Let $V$, $E$, $F$ be the numbers of vertices, edges, and faces (polygons) in the CW structure on $S^2$.
Proof: setup.

<1>2. The Euler characteristic of $S^2$ is $\chi(S^2) = V - E + F = 2$.
Proof: Euler characteristic of the sphere.

<1>3. The two graphs shown are the complete graph $K_5$ (five vertices) and the complete bipartite graph $K_{3,3}$ (six vertices).
Proof: these are the two graphs in the statement (the standard non-planar graphs).

<1>4. $K_5$ has $V = 5$ and $E = 10$; $K_{3,3}$ has $V = 6$ and $E = 9$.
Proof: $K_5$ has $\binom{5}{2} = 10$ edges; $K_{3,3}$ has $3 \cdot 3 = 9$ edges.

<1>5. If the 1-skeleton were $K_5$, then $V - E + F = 5 - 10 + F = 2$, so $F = 7$.
Proof: <1>2 and <1>4.

<1>6. But each face (polygon) has at least $3$ edges, and each edge is shared by exactly $2$ faces, so $2E \ge 3F$, i.e. $20 \ge 21$, a contradiction.
Proof: counting edge-face incidences: $2E = 20$ counts each edge twice (once per adjacent face), and $3F = 21$ is a lower bound on the total number of edge-face incidences (each face has $\ge 3$ edges).

<1>7. If the 1-skeleton were $K_{3,3}$, then $V - E + F = 6 - 9 + F = 2$, so $F = 5$.
Proof: <1>2 and <1>4.

<1>8. But $K_{3,3}$ is bipartite, so every face has at least $4$ edges, giving $2E \ge 4F$, i.e. $18 \ge 20$, a contradiction.
Proof: in a bipartite graph, every cycle has even length, so every face (bounded by a cycle) has at least $4$ edges; hence $2E = 18 \ge 4F = 20$, contradiction.

<1>9. Hence the 1-skeleton cannot be either graph.
Proof: <1>6 and <1>8.

<1>10. Q.E.D.
Proof: <1>9.
:::
