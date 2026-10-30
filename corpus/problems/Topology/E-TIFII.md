---
schema: qual/card@1
id: E-TIFII
kind: problem
title: Infinite sets with the cofinite topology are compact
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
Show that any infinite set with the cofinite topology is compact.
:::

::: {.solution}

Let $X$ be an infinite set with the cofinite topology.

::: pf

::: {.pf-step #s1}

In the cofinite topology, every nonempty open set has finite complement.

::: pf-proof

This is the definition of the cofinite topology.

:::

:::

::: pf-step

Let $\mathcal U$ be an open cover of $X$ and choose one nonempty $U_0\in\mathcal U$. Then $X\setminus U_0$ is finite.

::: pf-proof

Such a $U_0$ exists because $X$ is nonempty; apply step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

For each of the finitely many points of $X\setminus U_0$, choose one member of $\mathcal U$ containing it. Together with $U_0$ these form a finite subcover.

::: pf-proof

Every point is covered because $\mathcal U$ is a cover.

:::

:::

::: pf-step

Hence $X$ is compact.

::: pf-proof

Every open cover has the finite subcover constructed in step [](#s3){.pf-ref}.

:::

:::

:::

:::

::: {.remark title="Variations"}
$\RR$ with the cofinite topology is compact: $\RR$ is an infinite set, so the main proof applies unchanged.
:::
