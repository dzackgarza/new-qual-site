---
schema: qual/card@1
id: E-GD2KF
kind: problem
title: Refining a topology refines the subspace topologies
classification:
  areas:
  - topology
  topics:
  - Subspace Topology
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

If $\mathcal{T}$ and $\mathcal{T}'$ are topologies on $X$ and $\mathcal{T}'$ is strictly finer than $\mathcal{T}$, what can you say about the corresponding subspace topologies on the subset $Y$ of $X$?
:::

::: {.solution}
Let $\mathcal T_Y$ and $\mathcal T'_Y$ be the subspace topologies induced by $\mathcal T$ and $\mathcal T'$. Since $\mathcal T\subseteq\mathcal T'$, every set $Y\cap U$ with $U\in\mathcal T$ is also of the form $Y\cap U$ with $U\in\mathcal T'$. Hence
\[
\mathcal T_Y\subseteq\mathcal T'_Y.
\]
The inclusion need not be strict even when $\mathcal T\subsetneq\mathcal T'$. For example, let
\[
X=\{a,b\},\quad \mathcal T=\{\varnothing,X\},\quad
\mathcal T'=\{\varnothing,\{a\},X\},\quad Y=\{b\}.
\]
Both induced topologies on the singleton $Y$ are $\{\varnothing,Y\}$. Thus refinement passes to every subspace, but strict refinement need not.
:::
