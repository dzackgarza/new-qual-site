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

- $R\sm \mfm \subseteq R\units$, so every element of $R\sm \mfm$ is a unit, or

- $1 + \mfm \subseteq R\units$
:::

::: {.solution}
Let $R$ be a commutative ring with identity and $N \da R\sm R\units$ its set of nonunits.

<1>1. If $R\sm \mfm \subseteq R\units$, then $\mfm$ is the only maximal ideal of $R$.

::: {.proof}
The proper ideal $\mfm$ contains no unit, so $\mfm\subseteq N$, and the hypothesis gives $N\subseteq\mfm$; hence $\mfm=N$.
A proper ideal $I$ contains no unit, so $I\subseteq N=\mfm$.
:::

<1>2. If $1 + \mfm \subseteq R\units$, then $R\sm \mfm \subseteq R\units$, so $R$ is local by step <1>1.

::: {.proof}
Let $r\in R\sm \mfm$.
By maximality, $\mfm+\gens{r} = R$, so $rt + m = 1$ for some $t\in R$ and $m\in \mfm$.
Then $rt = 1-m \in 1 + \mfm \subseteq R\units$, so $r$ is a unit.
:::
:::
