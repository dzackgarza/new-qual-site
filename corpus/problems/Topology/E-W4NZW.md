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

::: exercise
Show that $\RR$ with the cofinite topology is compact.

#### Exercise
:::

::: {.solution}
<1>1. Let $\mathcal U$ be an open cover of $\mathbb R$ in the cofinite topology and choose a nonempty $U_0\in\mathcal U$.
::: {.proof}
A cover of the nonempty space contains a nonempty member.
:::

<1>2. The complement $\mathbb R\setminus U_0$ is finite.
::: {.proof}
This is the definition of a nonempty cofinite-open set.
:::

<1>3. Choose one member of $\mathcal U$ for each point of this finite complement. Together with $U_0$ they form a finite subcover.
::: {.proof}
$U_0$ covers everything except finitely many points, and the chosen additional sets cover those points.
:::

<1>4. Hence $\mathbb R$ with the cofinite topology is compact.
::: {.proof}
Every open cover has a finite subcover by <1>1--<1>3.
:::
:::
