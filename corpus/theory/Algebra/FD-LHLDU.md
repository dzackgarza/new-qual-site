---
schema: qual/card@1
id: FD-LHLDU
kind: definition
title: '$\gens{p}$-primary module'
prompts:
- For $R$ a PID and $p \in R$ prime, when is an $R\dash$module $\gens{p}\dash$primary?
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Primary Decomposition
  - Torsion
relations: []
review: draft
---

::: {.definition}
Let $R$ be a [[D-HTIL5|principal ideal domain]], $p\in R$ a prime, and $M$ an $R$-module.
$M$ is \dfn{$\gens{p}$-primary} if every $m\in M$ is annihilated by some power of $p$: for each $m\in M$ there is $n\geq 1$ with $p^n m = 0$.
:::

::: {.remark}
For any $R$-module $M$, the $p$-primary component $M[p^\infty] \coloneqq \theset{ m \in M \st p^n m = 0 \text{ for some } n\geq 1}$ is a submodule, and $M$ is $\gens{p}$-primary if and only if $M[p^\infty]=M$.
:::
