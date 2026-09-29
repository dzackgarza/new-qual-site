---
schema: qual/card@1
id: E-AMD-J2G54GWY
kind: problem
title: Composition factors of finite solvable groups have prime order
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Subgroup Series
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Replaced the verbose proof by the simple-solvable-factor argument.
---

::: {.exercise}
Show that if $G$ is finite and solvable, then every composition factor of $G$ has prime order.
:::

::: {.solution}
Let $S$ be a composition factor of the finite solvable group $G$.

::: pf

::: {.pf-step #composition-factor-simple-and-solvable}
The group $S$ is simple and solvable.

::: pf-proof
A composition factor is simple by definition. Subgroups and quotients of solvable groups are solvable, so every composition factor of $G$ is solvable.
:::

:::

::: {.pf-step #simple-solvable-group-abelian}
A nontrivial simple solvable group is abelian.

::: pf-proof
The derived subgroup $[S,S]$ is characteristic, hence normal, in $S$. Simplicity gives $[S,S]=1$ or $S$. Solvability excludes $[S,S]=S$, so $[S,S]=1$ and $S$ is abelian.
:::

:::

::: {.pf-step #simple-abelian-group-prime-order}
A finite simple abelian group has prime order.

::: pf-proof
Choose a prime $p\mid |S|$. By Cauchy's theorem there is $x\in S$ of order $p$. Since $S$ is abelian, $\langle x\rangle$ is normal; simplicity forces $\langle x\rangle=S$. Hence $|S|=p$.
:::

:::

::: pf-qed
Steps [](#composition-factor-simple-and-solvable){.pf-ref}, [](#simple-solvable-group-abelian){.pf-ref} and [](#simple-abelian-group-prime-order){.pf-ref} show that \(S\) has prime order. Thus every composition factor is cyclic of prime order.
:::

:::

:::
