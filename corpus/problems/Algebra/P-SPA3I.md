---
schema: qual/card@1
id: P-SPA3I
kind: problem
title: Examples of simple groups
classification:
  areas:
  - algebra
  topics:
  - Simple Groups
  - Classification
relations: []
review: draft
---

::: {.problem}
Give examples of simple groups. Are there infinitely many?
:::

::: {.solution}

A group is simple if it is nontrivial and its only normal subgroups are $1$ and itself.

::: pf

::: {.pf-step #cyclic}

For every prime $p$, the cyclic group $C_p=\ZZ/p\ZZ$ is simple.

::: pf-proof

By Lagrange's theorem a subgroup of $C_p$ has order $1$ or $p$, so the only subgroups are $1$ and $C_p$.

:::

:::

::: {.pf-step #alternating}

For every $n\ge5$, the alternating group $A_n$ is a nonabelian simple group.

::: pf-proof

This is the standard theorem on the simplicity of $A_n$ for $n\ge5$; $A_n$ is nonabelian because $(1\,2\,3)$ and $(1\,2\,4)$ do not commute.

:::

:::

::: pf-qed

There are $\boxed{\text{infinitely many}}$ simple groups, even among finite groups: step [](#cyclic){.pf-ref} gives one for each of the infinitely many primes, and step [](#alternating){.pf-ref} gives the pairwise nonisomorphic nonabelian groups $A_n$, $n\ge5$, of distinct orders $n!/2$.

:::

:::

:::
