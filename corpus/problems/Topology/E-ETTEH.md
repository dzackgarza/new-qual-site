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

::: {.exercise}
Let $X$ be a locally path-connected topological space. Prove that:

(1) Every open subset $U \subseteq X$ is locally path-connected.

(2) $X$ is connected if and only if $X$ is path-connected.

(3) Every path component of $X$ is a connected component of $X$.

(4) Every connected component (and path component) of $X$ is open in $X$.
:::

::: {.solution}

::: pf

::: pf-step

(1) Every open $U\subseteq X$ is locally path-connected.

::: pf-proof

Let $x\in U$ and let $V$ be a neighborhood of $x$ in $U$. Since $U$ is open, $V$ contains an open neighborhood $V'$ of $x$ in $X$ with $V'\subseteq U$. Since $X$ is locally path-connected, $V'$ contains a path-connected open neighborhood $W$ of $x$, and $W$ is open in $U$.

:::

:::

::: {.pf-step #s2}

Every path component $P$ of $X$ is open.

::: pf-proof

If $x\in P$, choose a path-connected open neighborhood $W$ of $x$. Every point of $W$ is joined to $x$ by a path, so $W\subseteq P$. Hence $P$ is a union of open sets.

:::

:::

::: {.pf-step #s3}

(3) Path components coincide with connected components.

::: pf-proof

Every path-connected set is connected, so each path component $P$ lies in a connected component $C$. The path components contained in $C$ partition $C$, and each is open by step [](#s2){.pf-ref}. If $C$ contained two or more path components, one of them and the union of the others would form a separation of $C$. Hence $C=P$.

:::

:::

::: pf-step

(4) Every connected component and every path component of $X$ is open.

::: pf-proof

This follows from steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: pf-step

(2) $X$ is connected if and only if $X$ is path-connected.

::: pf-proof

Path-connectedness always implies connectedness. Conversely, if $X$ is connected, it is its own unique connected component, which is a path component by step [](#s3){.pf-ref}. Hence $X$ is path-connected.

:::

:::

:::

:::
