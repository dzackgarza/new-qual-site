---
schema: qual/card@1
id: E-AMD-5LBXBRCH
kind: problem
title: A finite group is solvable iff its composition factors have prime order
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Subgroup Series
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that a finite group $G$ is solvable if and only if all of its composition factors are cyclic groups of prime order.
:::

::: {.solution}
Let $G$ be finite.

::: pf

::: {.pf-step #simple-solvable}
A simple solvable group $S$ is cyclic of prime order.

::: pf-proof
The commutator subgroup $[S,S]$ is normal in $S$. If $[S,S]=S$, the derived series never descends, contradicting solvability; so $[S,S]=1$ and $S$ is abelian. A simple abelian group has no proper nontrivial subgroups, so it is cyclic of prime order.
:::

:::

::: pf-step
If $G$ is solvable, every composition factor of $G$ is cyclic of prime order.

::: pf-proof
Subgroups and quotients of solvable groups are solvable, so each composition factor is simple and solvable; apply step [](#simple-solvable){.pf-ref}.
:::

:::

::: pf-step
If every composition factor of $G$ is cyclic of prime order, $G$ is solvable.

::: pf-proof
A composition series $1=G_0\trianglelefteq G_1\trianglelefteq\cdots\trianglelefteq G_r=G$ then has abelian factors $G_{i+1}/G_i$, so it is a subnormal series with abelian factors.
:::

:::

:::

:::
