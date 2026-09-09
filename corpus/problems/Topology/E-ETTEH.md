---
schema: qual/card@1
id: E-ETTEH
kind: problem
title: In a locally path-connected space, open subsets are locally path-connected,
  connectedness is equivalent to path-connectedness, and path components are the open
  connected components
classification:
  areas:
  - topology
  topics:
  - Connectedness
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

::: exercise
Let $X$ be a locally path-connected topological space. Prove that:
(1) Every open subset $U \subseteq X$ is locally path-connected.
(2) $X$ is connected if and only if $X$ is path-connected.
(3) Every path component of $X$ is a connected component of $X$.
(4) Every connected component (and path component) of $X$ is open in $X$.
:::

::: solution
<1>1. Let $U\subseteq X$ be open. If $x\in U$ and $V$ is a neighborhood of $x$ in $U$, then $V$ contains an open neighborhood $V'$ of $x$ in $X$ with $V'\subseteq U$. Since $X$ is locally path-connected, $V'$ contains a path-connected open neighborhood $W$ of $x$. Thus $U$ is locally path-connected.

<1>2. Every path component $P$ of $X$ is open.
<2>1. If $x\in P$, choose a path-connected open neighborhood $W$ of $x$.
<2>2. Every point of $W$ can be joined to $x$ by a path, so $W\subseteq P$.
<2>3. Hence $P$ is a union of open sets and is open.

<1>3. Path components coincide with connected components.
<2>1. Every path-connected set is connected, so each path component $P$ lies in a connected component $C$.
<2>2. The path components partition $C$, and each is open in $C$ by <1>2.
<2>3. If $C$ contained two or more path components, one path component and the union of the others would form a separation of $C$. This contradicts connectedness. Hence $C=P$.

<1>4. Therefore every connected component is also a path component and is open. Components are always closed, so in a locally path-connected space every component is clopen.

<1>5. Finally, path-connectedness always implies connectedness. Conversely, if $X$ is connected, it has only one connected component; by <1>3 that component is a path component. Hence $X$ is path-connected.
:::
