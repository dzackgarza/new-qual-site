---
schema: qual/card@1
id: E-PQ3FR
kind: exercise
title: "Suppose $\\mfm \\in \\mspec R$ is a proper maximal ideal."
classification:
  areas:
  - algebra
  topics:
  - local-rings
  - maximal-ideals
  - rings
relations: []
review: draft
solved: true
---

::: {.exercise title="?"}
Suppose $\mfm \in \mspec R$ is a proper maximal ideal.
Show that under either of the following two conditions, $R$ is local:

- $R\sm \mfm \subseteq R\units$, so every element of $R\sm \mfm$ is a unit, or

- $1 + \mfm \subseteq R\units$
:::

::: {.solution}
- Sketch: $\mfm$ must contain every non-unit.

  - If $I \neq R$ then $I$ contains no units, so $I\subseteq N \da R\sm R\units$, i.e. $I$ is contained in the non-units.
    But $N \subseteq \mfm$ since no element of $\mfm$ is a unit and no element of $R\sm \mfm$ is a non-unit.

- Sketch: show that every $r\in R\sm \mfm$ is a unit and apply the first part.

  - If $r\in R\sm \mfm$ then $\gens{r, \mfm} = R = \gens{ 1 }$ so $rt + m = 1$ for some $t\in R, m\in \mfm$, so $rt = 1-m \in 1 + \mfm \subseteq R\units$ by assumption.
    Now apply (1).
:::
