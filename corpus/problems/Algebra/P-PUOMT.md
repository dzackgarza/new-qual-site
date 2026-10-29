---
schema: qual/card@1
id: P-PUOMT
kind: problem
title: Normal subgroups of $p$-groups meet the center nontrivially
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Normal Subgroups
  - Centralizers and Normalizers
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite $p$-group and let $1\ne N\trianglelefteq G$. Prove that
$$N\cap Z(G)\ne\{e\}.$$
:::

::: {.solution}
Let $G$ act on $N$ by conjugation; this is an action on $N$ because $N$ is normal.

::: pf

::: {.pf-step #fixed}
The fixed points of the action are the elements of $N\cap Z(G)$, and every other orbit has size divisible by $p$.

::: pf-proof
An element $x\in N$ is fixed exactly when $gxg^{-1}=x$ for all $g\in G$, that is, when $x\in Z(G)$. The orbit of $x$ has size $[G:C_G(x)]$, which divides $\abs{G}$ and so is a power of $p$; it is $1$ only for a fixed point.
:::

:::

::: pf-step
$N\cap Z(G)\ne\{e\}$.

::: pf-proof
Since $N$ is the disjoint union of its orbits, step [](#fixed){.pf-ref} gives
$$\abs{N}\equiv\abs{N\cap Z(G)}\pmod p.$$
As $N$ is a nontrivial subgroup of a $p$-group, $p\mid\abs{N}$, so $p\mid\abs{N\cap Z(G)}$. Since $e\in N\cap Z(G)$, this order is at least $p$.
:::

:::

:::

:::
