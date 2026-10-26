---
schema: qual/card@1
id: P-JWPNL
kind: problem
title: Simple groups; no simple group of order $56$
classification:
  areas:
  - algebra
  topics:
  - Simple Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Define a *simple group*. Prove that a group of order 56 can not be simple.
:::

::: pf

::: pf-step

A group $G$ is simple if $G\neq1$ and the only normal subgroups of $G$ are $1$ and $G$.


::: pf-proof

This is the definition of a simple group.

:::

:::

::: pf-step

If a group $G$ has order $56$, then either it has a normal Sylow $7$-subgroup or it has exactly eight Sylow $7$-subgroups.


::: pf-proof

Since $56=2^3\cdot7$, Sylow's theorems imply $n_7\mid8$ and $n_7\equiv1\pmod7$. Thus $n_7\in\{1,8\}$. A unique Sylow subgroup is normal.

:::

:::

::: pf-step

If $n_7=8$, the Sylow $2$-subgroup of $G$ is unique and normal.


::: pf-proof

Distinct groups of prime order seven intersect in the identity. Consequently the eight Sylow $7$-subgroups account for $8(7-1)=48$ distinct nonidentity elements, leaving precisely seven nonidentity elements of $G$ outside their union. Every Sylow $2$-subgroup has order eight, and none of its seven nonidentity elements belongs to a subgroup of order seven. Hence every Sylow $2$-subgroup consists of the identity and precisely the same seven remaining elements. It follows that there is only one Sylow $2$-subgroup, which is normal.

:::

:::

::: pf-step

No group of order $56$ is simple.


::: pf-proof

By step <1>2 either $G$ has a normal subgroup of order seven, or by step <1>3 it has a normal subgroup of order eight. In both cases this is a nontrivial proper normal subgroup, contradicting simplicity as defined in step <1>1.

:::

:::

::: pf-qed

Steps <1>1 and <1>4 answer the two requests.

:::

:::
