---
schema: qual/card@1
id: E-T7PYZ
kind: problem
title: $\RR$ with the cofinite topology is compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Point-Set Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
Show that $\RR$ with the cofinite topology is compact.
:::

::: {.solution}

Let $\mathcal{U}$ be an open cover of $\RR$ in the cofinite topology.

::: pf

::: {.pf-step #s1}

Some $U_0 \in \mathcal{U}$ is nonempty, and $\RR \setminus U_0 = \theset{x_1, \ldots, x_n}$ is finite.

::: pf-proof

The union of $\mathcal{U}$ is $\RR \neq \emptyset$, so some member is nonempty. In the cofinite topology every nonempty open set has finite complement.

:::

:::

::: {.pf-step #s2}

For each $j = 1, \ldots, n$, choose $U_j \in \mathcal{U}$ with $x_j \in U_j$.

::: pf-proof

$\mathcal{U}$ covers $\RR$.

:::

:::

::: pf-step

$\theset{U_0, U_1, \ldots, U_n}$ is a finite subcover of $\mathcal{U}$, so $\RR$ is compact.

::: pf-proof

$U_0$ contains every point except $x_1, \ldots, x_n$ by step [](#s1){.pf-ref}, and each $x_j$ lies in $U_j$ by step [](#s2){.pf-ref}.

:::

:::

:::

:::
