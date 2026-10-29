---
schema: qual/card@1
id: E-HYQMG
kind: problem
title: $X$ is Hausdorff if and only if $\Delta(X)$ is closed in $X\times X$
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that a topological space $X$ is Hausdorff if and only if the diagonal $\Delta(X) = \{(x, x) \mid x \in X\}$ is closed in $X \times X$ with the product topology.
:::

::: {.solution}

::: pf

::: pf-step

If $X$ is Hausdorff, then $\Delta(X)$ is closed.

::: pf-proof

Let $(x,y)\notin\Delta(X)$, so $x\ne y$. Choose disjoint open neighborhoods $U\ni x$ and $V\ni y$. Then $(x,y)\in U\times V$, and $U\times V$ is disjoint from $\Delta(X)$ because $(z,z)\in U\times V$ would give $z\in U\cap V$. Hence $(X\times X)\setminus\Delta(X)$ is open, so $\Delta(X)$ is closed.

:::

:::

::: pf-step

If $\Delta(X)$ is closed, then $X$ is Hausdorff.

::: pf-proof

Let $x\ne y$. Then $(x,y)$ lies in the open set $(X\times X)\setminus\Delta(X)$, so some basic open set satisfies
$$(x,y)\in U\times V\subseteq (X\times X)\setminus\Delta(X).$$
If $U\cap V$ contained $z$, then $(z,z)\in U\times V$, contradicting disjointness from the diagonal. Thus $U\cap V=\varnothing$, so $x$ and $y$ have disjoint open neighborhoods.

:::

:::

:::

:::
