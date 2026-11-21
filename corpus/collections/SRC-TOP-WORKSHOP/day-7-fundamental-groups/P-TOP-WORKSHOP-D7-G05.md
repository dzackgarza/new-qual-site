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
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, and checked: the presentation complex
    of <a,b | > is the wedge of two circles with no 2-cells, so the Cayley complex is the Cayley
    graph, which is a tree because a circuit would spell a nonempty word equal to the identity in
    a free group; phi(a) = 1, phi(b) = 0 defines a homomorphism to Z/4 because a free group has no
    relations, and it is onto, so the kernel has index 4. The covering graph is derived from the
    coset description: a-edges give the 4-cycle, and b-edges are loops because phi(b) = 0 puts b in
    H. The basis step now says where the five words come from: the maximal tree v0-v1-v2-v3 leaves
    the edge v3 -> v0 and the four b-loops outside it, so the words are a^4 and a^i b a^{-i},
    matching E - V + 1 = 5 and Nielsen-Schreier's 1 + 4(2-1). Statement unchanged; the card says
    the argument is its own.
---

::: {.problem}
Let $F(a,b)$ be the free group of two generators.
What are the presentation complex and the Cayley complex for $F(a,b)$?
Find an index $4$ subgroup and the covering space that corresponds to it.
:::

::: {.solution}
The presentation complex of $\langle a,b\mid\ \rangle$ is the wedge of two circles, which has no $2$-cells, so its Cayley complex is its Cayley graph, the $4$-regular tree. The index-four subgroup is the kernel of a homomorphism to $\ZZ/4$ sending $a\mapsto1$, $b\mapsto0$, and the covering graph then has four vertices with $a$-edges forming a cycle and a $b$-loop at each vertex; a spanning tree and the remaining edges give a free basis of five elements, matching the Nielsen--Schreier rank. The argument is this card's own: no retained solution set covers this workshop problem.

::: pf

::: {.pf-step #presentation}
The presentation complex of $F(a,b)=\langle a,b\mid\ \rangle$ is the wedge $S^1_a\vee S^1_b$: one vertex, two oriented $1$-cells, no $2$-cells.

::: pf-proof
The presentation complex of a presentation $\langle X\mid R\rangle$ has one vertex, one $1$-cell per generator and one $2$-cell per relator attached along the word; with no relators there are no $2$-cells, so the complex is a wedge of one circle per generator. Its fundamental group is free on the generators, as computed by van Kampen, giving $\pi_1=F(a,b)$.
:::

:::


::: {.pf-step #cayley}
The Cayley complex of this presentation is its Cayley graph: the tree whose vertices are the elements of $F(a,b)$ and whose directed edges are $g\to ga$ and $g\to gb$.

::: pf-proof
The Cayley complex has one $2$-cell per relator for each vertex, so with no relators it is the Cayley $2$-complex's $1$-skeleton, the Cayley graph. The Cayley graph of a free group on a free generating set is a tree: it is connected, since the generators generate, and it has no circuits, since a circuit would spell a nonempty word equal to the identity in the free group. Every vertex has degree $4$, one edge for each of $a^{\pm1},b^{\pm1}$.
:::

:::


::: {.pf-step #subgroup}
$\phi\colon F(a,b)\to\ZZ/4$, $\phi(a)=1$, $\phi(b)=0$, is a well-defined homomorphism, and $H=\ker\phi$ has index $4$.

::: pf-proof
A homomorphism out of a free group is determined by its values on a free basis, with no relation to satisfy, so $\phi$ exists. It is onto because $\phi(a)$ generates $\ZZ/4$, so the image has order $4$ and the index of the kernel is $4$.
:::

:::


::: {.pf-step #cover}
The covering space of $S^1_a\vee S^1_b$ corresponding to $H$ has vertices $v_0,v_1,v_2,v_3$, an $a$-edge $v_i\to v_{i+1}$ for each $i$ mod $4$, and a $b$-loop at each $v_i$.

::: pf-proof
The cover corresponding to $H$ has one vertex per left coset of $H$, that is four vertices $v_0,\dots,v_3$ with $v_i$ standing for the coset of $a^i$; the $a$-edge lifts at $v_i$ end at the vertex of $Ha^i\cdot a=Ha^{i+1}$, which is $v_{i+1}$; and the $b$-edge lifts at $v_i$ end at the vertex of $Ha^i\cdot b=Ha^i$, since $\phi(b)=0$ means $b\in H$, so the $b$-edges are loops. Each vertex has one $a$-edge in, one out, and one $b$-loop in and out, so every point has a neighborhood evenly covered and the map to the rose, sending each $a$-edge to the $a$-circle and each $b$-loop to the $b$-circle, is a covering map. The graph is connected because the $a$-edges join the four vertices in a cycle, so the cover is connected and corresponds to a subgroup of index $4$.
:::

:::


::: {.pf-step #basis}
With basepoint $v_0$, $H$ is free on $a^4,\ b,\ aba^{-1},\ a^2ba^{-2},\ a^3ba^{-3}$, which is a basis, and $\operatorname{rank}H=5$.

::: pf-proof
Take as spanning tree $T$ the path $v_0\to v_1\to v_2\to v_3$ formed by the $a$-edges out of $v_0,v_1,v_2$. The edges of the covering graph outside $T$ are the $a$-edge $v_3\to v_0$ and the four $b$-loops, five edges in all. The standard fact relating a covering graph to a basis of the subgroup is that the edges outside a maximal tree correspond to a free basis of the subgroup of the base's fundamental group, each such edge $e$ contributing the word read off along the tree path to the start of $e$, then $e$, then the tree path back; the number of such edges is $E-V+1$. Here that gives $a^4$ for the edge $v_3\to v_0$ and $a^iba^{-i}$ for the $b$-loop at $v_i$, $i=0,1,2,3$, that is $b$, $aba^{-1}$, $a^2ba^{-2}$, $a^3ba^{-3}$; together with $a^4$ these are the five listed words. The covering graph has $E=8$, $V=4$, so the rank is $8-4+1=5$, agreeing with Nielsen--Schreier's $1+4(2-1)=5$. Since five elements generate a free group of rank $5$, they are a basis.
:::

:::


::: {.pf-step #conclusion}
The presentation complex is $S^1_a\vee S^1_b$, the Cayley complex its Cayley graph, the index-four subgroup is $\ker\phi$ with the covering graph described, and $H$ has rank $5$ with the displayed basis.

::: pf-proof
Steps [](#presentation){.pf-ref} and [](#cayley){.pf-ref} give the two complexes, [](#subgroup){.pf-ref} and [](#cover){.pf-ref} give the subgroup and its covering space, and [](#basis){.pf-ref} gives the basis and the rank.
:::

:::

:::
:::
