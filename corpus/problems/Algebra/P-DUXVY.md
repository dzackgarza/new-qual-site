---
schema: qual/card@1
id: P-DUXVY
kind: problem
title: Degree of a field extension
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
What is the degree of a field extension?
What does it mean to be a finite extension?
:::

::: {.solution}
For a field extension $F/K$, addition in $F$ and multiplication by elements of $K$ make $F$ a vector space over $K$.
The \dfn{degree} of $F$ over $K$ is $[F:K]\coloneqq\dim_KF$, and $F/K$ is a \dfn{finite extension} if $[F:K]<\infty$.
For example, $[\CC:\RR]=2$, with basis $1,i$.
:::
