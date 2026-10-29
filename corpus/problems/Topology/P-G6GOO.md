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

:::

::: pf-step

If every vertex of $X$ has valence $3$, then every vertex of $\widetilde X$ also has valence $3$, because a covering preserves vertex stars. A finite connected $3$-regular graph contains a cycle, so its universal cover is infinite. Hence $\widetilde X$ is the infinite $3$-regular tree $T_3$.

:::

:::

:::
