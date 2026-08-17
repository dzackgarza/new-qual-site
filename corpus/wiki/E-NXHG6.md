---
schema: qual/card@1
id: E-NXHG6
kind: exercise
title: Every non-unit of $R$ is contained in a maximal ideal
classification:
  areas:
  - algebra
  topics:
  - maximal-ideals
  - ideals
  - zorns-lemma
relations: []
review: draft
solved: true
---

::: {.exercise title="?"}
Show that every non-unit of $R$ is contained in a maximal ideal.
:::

::: {.solution}
This follows because if $x\in R\sm R\units$, then $Rx \normal R$ and $Rx\neq R$ implies $R/Rx \neq 0$.
Then there exists some $\bar \mfm \in \mspec R/Rx$, and by the correspondence theorem this lifts to some $\mfm \in \mspec R$ containing $Rx$.
:::
