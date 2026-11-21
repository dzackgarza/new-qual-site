---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-06
kind: problem
title: A compact set meets each fiber of a cover in finitely many points
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(Purdue Jan ’08) Let $p:E\to B$ be a covering map.
Suppose that points are closed in $B$.
Let $A\subset E$ be compact.
Prove that for every $b\in B$, the set $A\cap p^{-1}(b)$ is finite.
:::

::: {.solution}

The argument is the card's own: the fibre is closed and discrete, so its intersection with the compact set $A$ is a closed discrete subset of a compact space, hence finite.

::: pf

::: {.pf-step #closed}

$p^{-1}(b)$ is closed in $E$.

::: pf-proof

Points of $B$ are closed and $p$ is continuous, so $p^{-1}(b)$ is the preimage of a closed set under a continuous map.

:::

:::

::: {.pf-step #discrete}

$p^{-1}(b)$ is a discrete subspace of $E$.

::: pf-proof

Let $e\in p^{-1}(b)$ and let $U$ be an evenly covered neighbourhood of $b$, with $p^{-1}(U)$ a disjoint union of sheets each mapped homeomorphically onto $U$. Let $V$ be the sheet containing $e$. If $e'\in V\cap p^{-1}(b)$, then $p(e')=b=p(e)$ with $e',e\in V$, and $p$ is injective on $V$, so $e'=e$. Hence $V\cap p^{-1}(b)=\{e\}$: every point of the fibre is isolated in the fibre.

:::

:::

::: {.pf-step #compact}

$A\cap p^{-1}(b)$ is compact.

::: pf-proof

It is the intersection of the compact set $A$ with the closed set $p^{-1}(b)$ from step [](#closed){.pf-ref}. A closed subset of a compact space is compact, and a closed subspace of the compact space $A$ is compact.

:::

:::

::: {.pf-step #finite}

$A\cap p^{-1}(b)$ is finite.

::: pf-proof

A discrete subspace of a compact space is finite: the singleton sets $\{e'\}$, $e'\in A\cap p^{-1}(b)$, are open in the subspace topology by step [](#discrete){.pf-ref} and form an open cover of the compact space of step [](#compact){.pf-ref}, so finitely many of them cover it, which means the set has finitely many points:
$$
\boxed{A \text{ compact}\implies A\cap p^{-1}(b)\ \text{is finite for every } b\in B.}
$$

:::

:::

:::

:::
