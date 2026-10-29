---
schema: qual/card@1
id: E-W4NZW
kind: problem
title: The cofinite topology on $\RR$ is compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Point-Set Topology
relations: []
review: draft
---

::: {.exercise}
Show that $\RR$ with the cofinite topology is compact.
:::

::: {.solution}

Let $\mathcal U$ be an open cover of $\RR$ in the cofinite topology.

::: pf

::: {.pf-step #finite-complement}

Some $U_0\in\mathcal U$ has finite complement $\RR\setminus U_0$.

::: pf-proof

Since $\RR$ is nonempty, $\mathcal U$ has a nonempty member $U_0$, and a nonempty open set in the cofinite topology has finite complement.

:::

:::

::: pf-step

$\mathcal U$ has a finite subcover.

::: pf-proof

By step [](#finite-complement){.pf-ref}, write $\RR\setminus U_0=\{x_1,\ldots,x_k\}$ and choose $U_j\in\mathcal U$ with $x_j\in U_j$. Then $U_0,U_1,\ldots,U_k$ cover $\RR$.

:::

:::

:::

:::
