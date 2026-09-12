---
schema: qual/card@1
id: E-O13MH
kind: problem
title: Connectedness under refinement of topologies
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $\mathcal{T}$ and $\mathcal{T}'$ be two topologies on $X$.
If $\mathcal{T}' \supset \mathcal{T}$, what does connectedness of $X$ in one topology imply about connectedness in the other?
:::

::: {.solution}
Assume $\mathcal T\subseteq\mathcal T'$, so $\mathcal T'$ is finer.

If $X$ is connected in the finer topology $\mathcal T'$, then it is connected in the coarser topology $\mathcal T$: any separation by $\mathcal T$-open sets would also be a separation by $\mathcal T'$-open sets.

Equivalently, if $X$ is disconnected in the coarser topology, it remains disconnected in every finer topology.

The converse implications fail. For example, $\mathbb R$ with its standard topology is connected, while the finer lower-limit topology $\mathbb R_\ell$ is disconnected. Thus connectedness can be destroyed by refinement, but cannot be created by refinement.
:::
