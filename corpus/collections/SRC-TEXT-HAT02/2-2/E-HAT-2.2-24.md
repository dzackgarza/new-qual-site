---
schema: qual/card@1
id: E-HAT-2.2-24
kind: problem
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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 2.2, Exercise 24.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Compared the two figures with the printed page (page 158 of the text): the five-vertex graph is
    $K_5$ and the six-vertex graph is $K_{3,3}$. Read the counts: $K_5$ forces $F=7$ against
    $2E\ge3F$, and $K_{3,3}$ forces $F=5$ against $2E\ge4F$, the last bound using that a face of a
    simple bipartite graph has at least four sides, a closed walk of length two needing a repeated
    edge.
- event: solution-written
  by: claude
  date: 2026-11-08
  note: >-
    The stored solution was placeholder text - three steps whose proofs read "setup.", "Euler
    characteristic of the sphere.", "these are the two graphs in the statement" - and it is
    replaced by a proof. The figure on the printed p. 157 was rendered and read: its first graph
    is K_5 (five vertices, all pairs joined) and its second is K_3,3 (two groups of three, all
    cross edges and no others), which is what the statement's "five and six vertices" and the
    bracketed remark about non-embeddability in R^2 require.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 24 as printed on p. 157. The rewritten proof: V-E+F=2 by the
    definition of chi on p. 146 with Theorem 2.44 p. 146 and the homology of S^2 from
    Corollary 2.14 p. 114; the double count of (face, side) pairs giving 3F <= 2E, valid because
    the sides are identified in pairs so there are exactly 2E of them; then K_5 forces F=7 and
    21 <= 20, and K_3,3 forces F=5 and, since every closed walk in a bipartite graph is even and
    every face has at least three sides, 20 <= 18. What is not covered: that the boundary of a
    face is a closed walk of length equal to its number of sides is argued from the side pairing
    and not proved formally.
---

::: {.problem}
Suppose we build $S^2$ from a finite collection of polygons by identifying edges in pairs.
Show that in the resulting CW structure on $S^2$ the 1 skeleton cannot be either of the two graphs shown, with five and six vertices.
[This is one step in a proof that neither of these graphs embeds in $\RR^2$.]
:::

::: {.solution}
Let $V$, $E$, $F$ be the numbers of $0$-cells, $1$-cells and $2$-cells of the CW structure on $S^2$ obtained by identifying the sides of a finite collection of polygons in pairs. These are the numbers of vertices, edges and faces of its $1$-skeleton, the polygons being the $2$-cells.

::: pf

::: {.pf-step #s1}

$V-E+F=2$.

::: pf-proof

By the definition of the Euler characteristic of a finite CW complex as the alternating sum of the numbers of its cells (p. 146), $\chi(S^2)=V-E+F$. By Theorem 2.44 (p. 146), $\chi(S^2)$ is the alternating sum of the ranks of the homology groups, and $H_0(S^2)=\ZZ$, $H_1(S^2)=0$, $H_2(S^2)=\ZZ$ by Corollary 2.14 (p. 114), so
$$
\chi(S^2)=1-0+1=2.
$$

:::

:::

::: {.pf-step #s2}

The total number of sides of the polygons is $2E$, and every polygon has at least $3$ sides, so
$$
3F\le 2E.
$$

::: pf-proof

Each side borders exactly one face, its own, so the number of sides is the number of pairs (face, side). The sides are identified in pairs, and each pair becomes one edge of the $1$-skeleton, so the number of sides is exactly $2E$. A polygon has at least three sides. Hence $3F\le 2E$.

:::

:::

::: {.pf-step #s3}

The two graphs in the figure on p. 157 are $K_5$ and $K_{3,3}$.

::: pf-proof

The first has five vertices and an edge between every two of them: the complete graph $K_5$. The second has six vertices in two groups of three, with an edge from each vertex of one group to each vertex of the other and no further edges: the complete bipartite graph $K_{3,3}$. Both readings are of the printed figure.

:::

:::

::: {.pf-step #s4}

$K_5$ has $V=5$ and $E=10$, while $K_{3,3}$ has $V=6$ and $E=9$.

::: pf-proof

$K_5$ has one edge for each unordered pair of distinct vertices, $\binom52=10$. $K_{3,3}$ has one edge for each pair with one vertex in each group, $3\cdot3=9$.

:::

:::

::: {.pf-step #s5}

The $1$-skeleton is not $K_5$.

::: pf-proof

Suppose it were. Then $V=5$ and $E=10$, so step [](#s1){.pf-ref} gives $5-10+F=2$, that is $F=7$. Step [](#s2){.pf-ref} then gives $3\cdot7\le 2\cdot10$, that is $21\le 20$, which is false.

:::

:::

::: {.pf-step #s6}

The $1$-skeleton is not $K_{3,3}$.

::: pf-proof

Suppose it were. Then $V=6$ and $E=9$, so step [](#s1){.pf-ref} gives $6-9+F=2$, that is $F=5$. The boundary of a face is the image in the $1$-skeleton of the boundary of its polygon, a closed walk whose length is the number of sides of that polygon: consecutive sides are identified with edges and consecutive vertices with their endpoints. In a bipartite graph every closed walk has even length, since the two parts alternate along it. Every face therefore has an even number of sides, and at least three, hence at least four. With step [](#s2){.pf-ref}, $4\cdot5\le2\cdot9$, that is $20\le18$, which is false.

:::

:::

::: pf-step

The $1$-skeleton is neither of the two graphs.

::: pf-proof

Steps [](#s5){.pf-ref} and [](#s6){.pf-ref} exclude $K_5$ and $K_{3,3}$, and by step [](#s3){.pf-ref} these are the two graphs printed.

:::

:::

:::

:::
