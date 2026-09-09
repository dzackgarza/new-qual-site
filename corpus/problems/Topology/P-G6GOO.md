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
---

::: problem
Let $X$ be a finite connected graph whose fundamental group is the free group on generators (e.g. the wedge sum $S^1 \vee S^1$ or the theta graph with 3 edges).
(1) Construct the **universal covering space** $\widetilde{X}$ of $X$ as the tree $T$ of non-backtracking reduced paths from a basepoint $x_0 \in X$.
(2) Prove that $\widetilde{X}$ is a connected, acyclic tree (hence simply connected: $\pi_1(\widetilde{X}) = 0$).
(3) Explain why for a 3-valent graph (like the theta graph), the universal cover is the **infinite 3-regular tree** $T_3$.
:::

::: solution
Choose a base vertex $x_0\in X$.

<1>1. Define the vertices of $\widetilde X$ to be the reduced edge-paths in $X$ starting at $x_0$, including the empty path.
For a reduced path $\gamma$ ending at a vertex $v$ and an oriented edge $e$ issuing from $v$, join $\gamma$ by an edge to the reduced path obtained from $\gamma e$ after cancelling a terminal backtrack if one occurs.
Map this edge homeomorphically to $e$ and map each vertex-path to its endpoint.

<1>2. The resulting map $p:\widetilde X\to X$ is a covering map.
::: proof
At a vertex represented by $\gamma$ ending at $v$, the incident edges of $\widetilde X$ are in bijection with the oriented edge germs at $v$. Hence the star of $\gamma$ maps homeomorphically onto the star of $v$. These stars give evenly covered neighborhoods.
:::

<1>3. The graph $\widetilde X$ is connected and has no cycles.
::: proof
Every vertex $\gamma=e_1\cdots e_n$ is joined to the empty path by successively deleting its terminal edges, so $\widetilde X$ is connected.

If a nontrivial reduced closed edge-path existed in $\widetilde X$, projecting it to $X$ would give a nontrivial reduced word which, starting from some reduced path $\gamma$, returns after successive reduction to the same path $\gamma$. Cancelling the common initial word would force the projected reduced word to represent the identity in the free edge-path groupoid of a graph, hence to be empty, a contradiction.
:::

<1>4. Therefore $\widetilde X$ is a tree. In particular it is contractible and simply connected, so $p$ is the universal covering map.

<1>5. If every vertex of $X$ has valence $3$, then every vertex of $\widetilde X$ also has valence $3$, because a covering preserves vertex stars. A finite connected $3$-regular graph contains a cycle, so its universal cover is infinite. Hence $\widetilde X$ is the infinite $3$-regular tree $T_3$.
:::
