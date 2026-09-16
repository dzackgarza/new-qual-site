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
<1>1. In the cofinite topology, every nonempty open set has finite complement.
::: {.proof}
This is the definition of the cofinite topology.
:::

<1>2. Let $\mathcal U$ be an open cover and choose one nonempty $U_0\in\mathcal U$. Then $X\setminus U_0$ is finite.
::: {.proof}
Apply <1>1.
:::

<1>3. For each of the finitely many points of $X\setminus U_0$, choose one member of $\mathcal U$ containing it. Together with $U_0$ these form a finite subcover.
::: {.proof}
Every point is covered because $\mathcal U$ is a cover.
:::

<1>4. Hence every space with the cofinite topology is compact.
::: {.proof}
Every open cover has the finite subcover constructed in <1>3.
:::
:::
