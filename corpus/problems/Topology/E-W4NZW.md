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

#### Exercise
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $\mathcal U$ be an open cover of $\mathbb R$ in the cofinite topology and choose a nonempty $U_0\in\mathcal U$.

::: pf-proof

A cover of the nonempty space contains a nonempty member.

:::

:::

::: {.pf-step #s2}

The complement $\mathbb R\setminus U_0$ is finite.

::: pf-proof

This is the definition of a nonempty cofinite-open set.

:::

:::

::: {.pf-step #s3}

Choose one member of $\mathcal U$ for each point of this finite complement. Together with $U_0$ they form a finite subcover.

::: pf-proof

$U_0$ covers everything except finitely many points, and the chosen additional sets cover those points.

:::

:::

::: pf-step

Hence $\mathbb R$ with the cofinite topology is compact.

::: pf-proof

Every open cover has a finite subcover by steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
