---
schema: qual/card@1
id: P-E2CRQ
kind: problem
title: The union of intersecting connected sets is connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Point-Set Topology
relations: []
review: draft
---

::: {.problem}
Suppose $A, B\subseteq \RR^n$ are connected and not disjoint.
Prove that $A\union B$ is also connected.
:::

::: {.solution}

A space $X$ is connected if and only if every continuous map $X\to\{-1,1\}$, with the discrete topology on $\{-1,1\}$, is constant.
Let $f:A\union B\to\{-1,1\}$ be continuous and fix $p\in A\intersect B$.

::: pf

::: {.pf-step #restrictions}
$f$ is constant on $A$ and constant on $B$.

::: pf-proof
The restrictions $\restrictionof{f}{A}$ and $\restrictionof{f}{B}$ are continuous, and $A$ and $B$ are connected.
:::

:::

::: pf-step
$f$ is constant, so $A\union B$ is connected.

::: pf-proof
By step [](#restrictions){.pf-ref}, $f$ takes the value $f(p)$ on all of $A$ and on all of $B$, because $p$ lies in both.
:::

:::

:::

:::
