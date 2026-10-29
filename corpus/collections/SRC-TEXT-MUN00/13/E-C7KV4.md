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

Show that the topologies of $\RR_\ell$ and $\RR_K$ are not comparable.
:::

::: {.solution}
Recall that $\RR_\ell$ has basis $[a,b)$ and $\RR_K$ has basis consisting of ordinary intervals $(a,b)$ and sets $(a,b)-K$, where $K=\{1/n:n\in\ZZ_+\}$.

First,
$$
[0,1)\in\RR_\ell
$$
but $[0,1)$ is not open in $\RR_K$: every $\RR_K$-basic neighborhood of $0$ contains negative points, so no such neighborhood is contained in $[0,1)$. Hence $\RR_\ell$ is not coarser than $\RR_K$.

Conversely,
$$
(-1,1)-K
$$
is $\RR_K$-open. It is not $\RR_\ell$-open. Indeed $0$ belongs to it, but every lower-limit basic neighborhood $[0,b)$ of $0$ with $b>0$ contains $1/n$ for all sufficiently large $n$, hence meets $K$. Thus no lower-limit basic neighborhood of $0$ lies inside $(-1,1)-K$. Therefore $\RR_K$ is not coarser than $\RR_\ell$ either.
:::
