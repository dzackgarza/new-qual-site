---
schema: qual/card@1
id: P-G6GOO
kind: problem
title: The infinite $3$-regular tree as a universal cover
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Justin sheet 4, Problem 6 is the theta-graph case of this construction.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Three of the card's five steps asserted their claim with no proof body: the construction
    itself, the passage from tree to universal cover, and the identification of the cover of a
    cubic graph with the infinite 3-regular tree. Each now carries a `pf-proof`. No claim was
    changed and no construction altered. Checked: that appending and cancelling a terminal
    backtrack really lands on a reduced path, so the edge set is well defined; that a tree is
    contractible through the geodesic retraction to a root; that a finite connected
    $3$-regular graph cannot be a tree ($E=V-1$ against $3V=2E$); and that two connected
    $3$-regular trees are isomorphic, which is what licenses the definite article in $T_3$.
    Not checked: no published solution was read; the source is the Justin sheet recorded in the
    `source-checked` event.
---

::: {.problem}
Let $X$ be a finite connected graph, for example the wedge sum $S^1 \vee S^1$ or the theta graph with $3$ edges.

(a) Construct the universal covering space $\widetilde{X}$ of $X$ as the graph $T$ of reduced (non-backtracking) edge-paths from a base vertex $x_0 \in X$.

(b) Prove that $\widetilde{X}$ is a connected, acyclic graph, that is, a tree; hence $\pi_1(\widetilde{X}) = 0$.

(c) Explain why, when every vertex of $X$ has valence $3$ (as in the theta graph), the universal cover is the infinite $3$-regular tree $T_3$.
:::

::: {.solution}

Choose a base vertex $x_0\in X$.

::: pf

::: pf-step

Define the vertices of $\widetilde X$ to be the reduced edge-paths in $X$ starting at $x_0$, including the empty path.
For a reduced path $\gamma$ ending at a vertex $v$ and an oriented edge $e$ issuing from $v$, join $\gamma$ by an edge to the reduced path obtained from $\gamma e$ after cancelling a terminal backtrack if one occurs.
Map this edge homeomorphically to $e$ and map each vertex-path to its endpoint.

::: pf-proof

A reduced edge-path is a word $e_1\cdots e_n$ with $e_{i+1}\ne\bar e_i$, the bar denoting the reversed edge; its endpoints are determined by the word, so 'ending at $v$' makes sense, and the empty word is the reduced path at $x_0$. Appending an edge $e$ issuing from the endpoint of $\gamma$ gives a path that is reduced unless $e$ is the reverse of the last letter of $\gamma$, in which case deleting those two letters leaves a reduced path; so the other end of the new edge is again a vertex of $\widetilde X$. Sending each edge to the edge of $X$ it was built from is compatible with the endpoint maps on vertices, so it defines a continuous map of graphs $p\colon\widetilde X\to X$ (Munkres, §83).

:::

:::

::: pf-step

The resulting map $p:\widetilde X\to X$ is a covering map.

::: pf-proof

At a vertex represented by $\gamma$ ending at $v$, the incident edges of $\widetilde X$ are in bijection with the oriented edge germs at $v$. Hence the star of $\gamma$ maps homeomorphically onto the star of $v$. These stars give evenly covered neighborhoods.

:::

:::

::: pf-step

The graph $\widetilde X$ is connected and has no cycles.

::: pf-proof

Every vertex $\gamma=e_1\cdots e_n$ is joined to the empty path by successively deleting its terminal edges, so $\widetilde X$ is connected.

If a nontrivial reduced closed edge-path existed in $\widetilde X$, projecting it to $X$ would give a nontrivial reduced word which, starting from some reduced path $\gamma$, returns after successive reduction to the same path $\gamma$. Cancelling the common initial word would force the projected reduced word to represent the identity in the free edge-path groupoid of a graph, hence to be empty, a contradiction.

:::

:::

::: pf-step

Therefore $\widetilde X$ is a tree. In particular it is contractible and simply connected, so $p$ is the universal covering map.

::: pf-proof

A tree is a connected acyclic graph, which is step 3. Fix a root, the empty path. Each vertex has a unique reduced path to the root: one exists by connectedness, and two would form a cycle. Sliding every point of the tree along its path to the root at unit speed, $H(x,t)=$ the point at distance $(1-t)\,d(x,\text{root})$ from $x$ on that path, is a deformation retraction onto the root, so $\widetilde X$ is contractible and hence simply connected. A covering map whose total space is connected and simply connected is the universal covering (Munkres, §82).

:::

:::

::: pf-step

If every vertex of $X$ has valence $3$, then every vertex of $\widetilde X$ also has valence $3$, because a covering preserves vertex stars. A finite connected $3$-regular graph contains a cycle, so its universal cover is infinite. Hence $\widetilde X$ is the infinite $3$-regular tree $T_3$.

::: pf-proof

At a vertex $\gamma$ over $v$, the bijection of step 2 between the edges of $\widetilde X$ at $\gamma$ and the edge germs at $v$ shows that the valences agree, so $\widetilde X$ is $3$-regular. A finite connected graph with $V$ vertices and $E$ edges that is a tree has $E=V-1$, while $3$-regularity gives $3V=2E$, that is $E=3V/2$; the two are incompatible for $V\ge1$, so a finite connected $3$-regular graph is not a tree and contains a cycle. Since $\widetilde X$ is a tree by step 4 it is not finite, so it is an infinite $3$-regular tree. Any two connected $3$-regular trees are isomorphic: match a root with a root and extend outward level by level, sending the two edges of a vertex other than the one back to the previous level onto the two corresponding edges; that is well defined because every vertex is incident with exactly three edges. Hence $\widetilde X\cong T_3$.

:::

:::

:::
:::