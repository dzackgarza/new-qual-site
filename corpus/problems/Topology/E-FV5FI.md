---
schema: qual/card@1
id: E-FV5FI
kind: problem
title: Compact subsets of metric spaces are bounded
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
Show that if $X$ is a metric space and $A\subseteq X$ is compact then $A$ is bounded.
:::

::: {.solution}
If $A=\varnothing$, it is bounded. Otherwise fix $p\in A$.

::: pf

::: {.pf-step #cover}

The open balls $B(p,n)$, $n\in\NN$, cover $A$, so finitely many $B(p,n_1),\ldots,B(p,n_k)$ cover $A$.

::: pf-proof

Every point of $X$ is at finite distance from $p$, so it lies in some $B(p,n)$, and balls are open. The second claim is compactness of $A$.

:::

:::

::: pf-qed

Let $N\coloneqq\max\{n_1,\ldots,n_k\}$. By step [](#cover){.pf-ref}, each $a\in A$ lies in some $B(p,n_j)\subseteq B(p,N)$, so $A\subseteq B(p,N)$ and $A$ is bounded.

:::

:::

:::
