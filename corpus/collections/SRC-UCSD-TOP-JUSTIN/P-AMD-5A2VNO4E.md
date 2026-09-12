---
schema: qual/card@1
id: P-AMD-5A2VNO4E
kind: problem
title: Letters of the alphabet up to homeomorphism and homotopy
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Homotopy
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Classify the letters of the alphabet up to homeomorphism, and up to homotopy.
:::

::: {.solution}
<1>1. As preserved, the problem does not determine a unique classification of the alphabet.
::: {.proof}
The retained source, *Justin's Problems*, says only “Classify the letters of the alphabet up to homeomorphism, and up to homotopy.” It does not specify uppercase versus lowercase letters, a font, whether strokes have positive thickness or are treated as one-dimensional centerlines, or how crossings/junctions are interpreted. These choices change the underlying topological spaces. For example, a lowercase ``i`` in an ordinary font is disconnected, whereas an uppercase ``I`` may be an interval or a tree with extra branches depending on the font; a capital ``Q`` may have a tail meeting the loop at one point or crossing it. Hence there is no source-faithful partition of the 26 letter names without additional glyph data.
:::

<1>2. If a letter is specified as a finite one-dimensional CW complex (a finite graph), then its homotopy type is completely determined, component by component, by the number of connected components and the first Betti number of each component.
::: {.proof}
Let $G$ be a finite connected graph. Choose a maximal tree $T\subset G$. Collapsing $T$ to a point is a homotopy equivalence and leaves one circle for each edge not in $T$. Since a tree on $V$ vertices has $V-1$ edges, the number of remaining edges is
$$
E-(V-1)=E-V+1=1-\chi(G)=\operatorname{rank}H_1(G;\mathbb Z).
$$
Thus
$$
G\simeq \bigvee^{\beta_1(G)}S^1.
$$
For a disconnected finite graph, apply this argument to each connected component. Therefore two specified finite graph glyphs are homotopy equivalent exactly when their components can be paired with equal first Betti numbers.
:::

<1>3. Homeomorphism of finite graph glyphs is finer than equality of Betti numbers or of the multiset of local valences.
::: {.proof}
A homeomorphism preserves the full incidence pattern of branch points and endpoints, not merely the multiset of their valences. For instance, consider two trees having four vertices of valence $3$ and six endpoints. In the first, the four trivalent vertices form a path of length $3$, with respectively $2,1,1,2$ endpoint leaves attached. In the second, one trivalent vertex is adjacent to each of the other three trivalent vertices, and each outer trivalent vertex has two endpoint leaves. Both trees have the same valence multiset—four vertices of valence $3$ and six of valence $1$—but deleting the set of branch points leaves different branch-point adjacency graphs (a path versus a $3$-star), so they are not homeomorphic.
:::

<1>4. For a specified finite graph glyph, its homeomorphism type is obtained by suppressing valence-$2$ vertices and recording the resulting incidence graph, with a circle component recorded separately when it has no vertices of valence different from $2$.
::: {.proof}
Subdividing an edge by inserting a valence-$2$ vertex does not change the underlying topological space. Conversely, in a finite graph every point whose punctured sufficiently small neighborhood has a number of components different from $2$ is topologically distinguished; these are precisely the endpoints and branch points. A homeomorphism must biject these distinguished points and preserve which pairs are joined by components of their complement. Suppressing all valence-$2$ subdivision vertices therefore leaves exactly the incidence data determining the homeomorphism type, except for components homeomorphic to $S^1$, which contain no distinguished point and must be recorded separately.
:::

<1>5. Consequently, once concrete glyphs are supplied, the requested classification is algorithmic: compute the reduced incidence graph for homeomorphism and the componentwise first Betti numbers for homotopy. But the retained problem statement alone does not determine which glyph graph corresponds to each letter.
::: {.proof}
This follows from <1>1--<1>4. Any explicit alphabet partition would require additional graphical conventions not present in the preserved source.
:::
:::
