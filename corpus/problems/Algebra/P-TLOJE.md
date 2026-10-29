---
schema: qual/card@1
id: P-TLOJE
kind: problem
title: Abelian groups are nilpotent
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Nilpotent Groups
relations: []
review: draft
---

::: {.problem}
Show that every abelian group is nilpotent.
:::

::: {.solution}
Let $G$ be abelian, and let $\gamma_1(G)=G$ and $\gamma_{i+1}(G)=[\gamma_i(G),G]$ be its lower central series.

::: pf

::: pf-step
$\gamma_2(G)=1$.

::: pf-proof
Every commutator $[x,y]=xyx^{-1}y^{-1}$ is trivial because $G$ is abelian, so $\gamma_2(G)=[G,G]=1$.
:::

:::

::: pf-step
$G$ is nilpotent of class at most $1$.

::: pf-proof
The lower central series reaches $1$ at $\gamma_2(G)$.
:::

:::

:::

:::
