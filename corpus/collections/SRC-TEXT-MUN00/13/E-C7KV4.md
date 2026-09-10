---
schema: qual/card@1
id: E-C7KV4
kind: problem
title: The lower limit and K-topologies are not comparable
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
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

Show that the topologies of $\mathbb{R}_\ell$ and $\mathbb{R}_K$ are not comparable.
:::

::: {.solution}
Recall that $\mathbb R_\ell$ has basis $[a,b)$ and $\mathbb R_K$ has basis consisting of ordinary intervals $(a,b)$ and sets $(a,b)-K$, where $K=\{1/n:n\in\mathbb Z_+\}$.

First,
\[
[0,1)\in\mathbb R_\ell
\]
but $[0,1)$ is not open in $\mathbb R_K$: every $\mathbb R_K$-basic neighborhood of $0$ contains negative points, so no such neighborhood is contained in $[0,1)$. Hence $\mathbb R_\ell$ is not coarser than $\mathbb R_K$.

Conversely,
\[
(-1,1)-K
\]
is $\mathbb R_K$-open. It is not $\mathbb R_\ell$-open. Indeed $0$ belongs to it, but every lower-limit basic neighborhood $[0,b)$ of $0$ with $b>0$ contains $1/n$ for all sufficiently large $n$, hence meets $K$. Thus no lower-limit basic neighborhood of $0$ lies inside $(-1,1)-K$. Therefore $\mathbb R_K$ is not coarser than $\mathbb R_\ell$ either.
:::
