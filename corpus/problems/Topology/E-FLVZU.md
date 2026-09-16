---
schema: qual/card@1
id: E-FLVZU
kind: problem
title: Compact topological space
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}
- What does it mean for a topological space to be **compact**?
:::

::: {.solution}
<1>1. A topological space $X$ is compact if every open cover of $X$ has a finite subcover.
::: {.proof}
Explicitly, whenever $X=\bigcup_{i\in I}U_i$ with each $U_i$ open, there exist $i_1,\dots,i_r\in I$ such that $X=U_{i_1}\cup\cdots\cup U_{i_r}$. This is the definition of compactness.
:::
:::
