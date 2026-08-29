---
schema: qual/card@1
id: E-ETTEH
kind: exercise
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
---

::: exercise
Let $X$ be a locally path-connected topological space. Prove that:
(1) Every open subset $U \subseteq X$ is locally path-connected.
(2) $X$ is connected if and only if $X$ is path-connected.
(3) Every path component of $X$ is a connected component of $X$.
(4) Every connected component (and path component) of $X$ is open in $X$.
:::

::: solution
**Goal:** Prove the foundational topological properties of locally path-connected spaces.

<1>1. Part (1): Open subsets $U \subseteq X$ are locally path-connected:
    *Proof:*
    <2>1. Let $U \subseteq X$ be open, and let $x \in U$.
    <2>2. Let $V \subseteq U$ be any open neighborhood of $x$ in $U$.
    <2>3. Since $U$ is open in $X$, $V$ is also an open neighborhood of $x$ in $X$.
    <2>4. Because $X$ is locally path-connected, there exists a path-connected open neighborhood $W \subseteq X$ such that $x \in W \subseteq V$.
    <2>5. Since $W \subseteq V \subseteq U$, $W$ is an open path-connected neighborhood of $x$ contained in $V$.
    <2>6. Thus $U$ is locally path-connected.

<1>2. Part (4): Path components are open in $X$:
    *Proof:*
    <2>1. Let $P \subseteq X$ be a path component of $X$, and let $x \in P$.
    <2>2. Since $X$ is locally path-connected, there exists a path-connected open neighborhood $W_x$ of $x$ in $X$.
    <2>3. Because $W_x$ is path-connected and contains $x \in P$, every point in $W_x$ can be connected by a path to $x$, and hence to every point in $P$.
    <2>4. By maximality of the path component $P$, we must have $W_x \subseteq P$.
    <2>5. Thus $P = \bigcup_{x \in P} W_x$ is a union of open sets, so $P$ is open in $X$.

<1>3. Part (3): Path components are connected components:
    *Proof:*
    <2>1. In any topological space, every path-connected set is connected, so each path component $P$ is contained in some connected component $C$: $P \subseteq C$.
    <2>2. By Step <1>2, every path component of $X$ is open.
    <2>3. The connected component $C$ is partitioned into path components: $C = \bigcup_{\alpha} P_\alpha$.
    <2>4. Each $P_\alpha$ is open in $X$, hence open in the subspace topology on $C$.
    <2>5. If $C$ contained more than one path component, say $P$ and $\bigcup_{\alpha \ne 0} P_\alpha$, then $P$ and $C \setminus P$ would form a non-trivial clopen separation of $C$, contradicting that $C$ is connected.
    <2>6. Therefore, $C = P$ consists of exactly one path component.
    <2>7. Thus the path components of $X$ are precisely the connected components of $X$, and all connected components are open (and closed) in $X$.

<1>4. Part (2): $X$ is connected $\iff X$ is path-connected:
    *Proof:*
    <2>1. $(\impliedby)$ In any space, path-connected implies connected.
    <2>2. $(\implies)$ Suppose $X$ is connected.
    <2>3. By Part (3), $X$ has only one connected component, which is a single path component.
    <2>4. Thus $X$ is path-connected.

<1>5. Conclusion:
    In a locally path-connected space, open sets are locally path-connected, path components coincide with connected components, components are open, and connectedness is equivalent to path-connectedness. Q.E.D.
:::
