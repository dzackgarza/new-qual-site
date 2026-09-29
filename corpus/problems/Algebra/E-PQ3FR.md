---
schema: qual/card@1
id: E-PQ3FR
kind: problem
title: A ring is local if $R\setminus\mfm$ consists of units, or if $1+\mfm$ consists
  of units
classification:
  areas:
  - algebra
  topics:
  - Local Rings
  - Maximal Ideals
  - Rings
relations: []
review: draft
---

::: {.exercise}
Suppose $\mfm \in \mspec R$ is a proper maximal ideal.
Show that under either of the following two conditions, $R$ is local:

- $R\sm \mfm \subseteq \unitsof{R}$, so every element of $R\sm \mfm$ is a unit, or

- $1 + \mfm \subseteq \unitsof{R}$
:::

::: {.solution}
Let $R$ be a commutative ring with identity and $N \da R\sm \unitsof{R}$ its set of nonunits.

::: pf

::: {.pf-step #m-is-unique-maximal-ideal}
If $R\sm \mfm \subseteq \unitsof{R}$, then $\mfm$ is the only maximal ideal of $R$.

::: pf-proof
The proper ideal $\mfm$ contains no unit, so $\mfm\subseteq N$, and the hypothesis gives $N\subseteq\mfm$; hence $\mfm=N$.
A proper ideal $I$ contains no unit, so $I\subseteq N=\mfm$.
:::

:::

::: pf-step
If $1 + \mfm \subseteq \unitsof{R}$, then $R\sm \mfm \subseteq \unitsof{R}$, so $R$ is local by step [](#m-is-unique-maximal-ideal){.pf-ref}.

::: pf-proof
Let $r\in R\sm \mfm$.
By maximality, $\mfm+\gens{r} = R$, so $rt + m = 1$ for some $t\in R$ and $m\in \mfm$.
Then $rt = 1-m \in 1 + \mfm \subseteq \unitsof{R}$, so $r$ is a unit.
:::

:::

:::

:::
