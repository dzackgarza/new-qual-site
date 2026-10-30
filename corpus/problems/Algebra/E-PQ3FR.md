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
audit:
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source left the ring unqualified; the statement now assumes R commutative with identity, as the solution does.'
---

::: {.exercise}
Let $R$ be a commutative ring with identity, and suppose $\mfm \in \mspec R$ is a proper maximal ideal.
Show that under either of the following two conditions, $R$ is local:

- $R\sm \mfm \subseteq \units{R}$, so every element of $R\sm \mfm$ is a unit, or

- $1 + \mfm \subseteq \units{R}$.
:::

::: {.solution}
Let $N \coloneqq R\sm \units{R}$ be the set of nonunits of $R$.

::: pf

::: {.pf-step #m-is-unique-maximal-ideal}
If $R\sm \mfm \subseteq \units{R}$, then $\mfm$ is the only maximal ideal of $R$.

::: pf-proof
The proper ideal $\mfm$ contains no unit, so $\mfm\subseteq N$, and the hypothesis gives $N\subseteq\mfm$; hence $\mfm=N$.
A proper ideal $I$ contains no unit, so $I\subseteq N=\mfm$.
:::

:::

::: pf-step
If $1 + \mfm \subseteq \units{R}$, then $R\sm \mfm \subseteq \units{R}$, so $R$ is local by step [](#m-is-unique-maximal-ideal){.pf-ref}.

::: pf-proof
Let $r\in R\sm \mfm$.
By maximality, $\mfm+\generators{r} = R$, so $rt + m = 1$ for some $t\in R$ and $m\in \mfm$.
Then $rt = 1-m \in 1 + \mfm \subseteq \units{R}$, so $r$ is a unit.
:::

:::

:::

:::
