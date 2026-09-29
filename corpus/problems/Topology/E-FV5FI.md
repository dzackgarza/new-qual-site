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
**Goal:** Show that if $X$ is a metric space and $A \subseteq X$ is compact, then $A$ is bounded.

::: pf

::: pf-step

Fix a point $p \in X$; the open balls $\theset{B(p, n)}_{n \in \NN}$ form an open cover of $X$.

::: pf-proof

Every point of $X$ is at finite distance from $p$, so it lies in some $B(p, n)$; balls are open in a metric space.

:::

:::

::: {.pf-step #s2}

The restriction to $A$ is an open cover of $A$, so it has a finite subcover $B(p, n_1), \ldots, B(p, n_k)$.

::: pf-proof

$A$ is compact.

:::

:::

::: {.pf-step #s3}

Let $N := \max\theset{n_1, \ldots, n_k}$; then $A \subseteq B(p, N)$.

::: pf-proof

Each $a \in A$ lies in some $B(p, n_j) \subseteq B(p, N)$ since $n_j \leq N$.

:::

:::

::: {.pf-step #s4}

$A$ is bounded.

::: pf-proof

$A$ is contained in a ball of finite radius $N$ centered at $p$, which is the definition of boundedness in a metric space.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} establish the claim.

:::

:::

:::
