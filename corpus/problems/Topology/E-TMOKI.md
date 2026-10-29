---
schema: qual/card@1
id: E-TMOKI
kind: problem
title: The subspace of $\RR^2$ with at least one rational coordinate is connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Euclidean Spaces
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "the set (x, y) in R^2 such that"; the missing "of" is supplied.'
---

::: {.exercise}
Show that the set of $(x, y) \in \RR^2$ such that at least one of $x, y$ is rational with the subspace topology is a connected space.
:::

::: {.solution}

::: pf

::: pf-step

Let
$$X=(\QQ\times\RR)\cup(\RR\times\QQ).$$
For each $q\in\QQ$, the horizontal line $H_q=\RR\times\{q\}$ and vertical line $V_q=\{q\}\times\RR$ are connected.

::: pf-proof

Each is homeomorphic to $\RR$.

:::

:::

::: pf-step

The union
$$Y=V_0\cup\bigcup_{q\in\QQ}H_q$$
is connected.

::: pf-proof

Every $H_q$ meets the connected set $V_0$ at $(0,q)$, and a union of connected sets all meeting a fixed connected set is connected.

:::

:::

::: pf-step

Every vertical line $V_q$ with $q\in\QQ$ meets $Y$ at $(q,0)$.

::: pf-proof

The point $(q,0)$ lies on $V_q$, and it lies on $H_0\subseteq Y$ because $0\in\QQ$.

:::

:::

::: pf-step

Hence
$$X=Y\cup\bigcup_{q\in\QQ}V_q$$
is connected.

::: pf-proof

Every point of $X$ has a rational coordinate, so it lies on some $H_q$ or $V_q$; this gives the displayed equality. Each $V_q$ is connected and meets the connected set $Y$, so the union is connected.

:::

:::

:::

:::
