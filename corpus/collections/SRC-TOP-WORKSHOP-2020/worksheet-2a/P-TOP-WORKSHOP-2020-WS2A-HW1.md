---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2A-HW1
kind: problem
title: List the separation properties T0 through T4 (warm-up)
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
What are the properties $T_0$--$T_4$?
What other names are there for $T_2$--$T_4$?
:::

::: {.solution}
Using the standard conventions:

- \(T_0\): for any distinct \(x,y\), at least one has an open neighborhood not containing the other.
- \(T_1\): for any distinct \(x,y\), each has an open neighborhood not containing the other; equivalently, every singleton is closed.
- \(T_2\): distinct points have disjoint open neighborhoods. This is the **Hausdorff** axiom.
- \(T_3\): \(T_1\) and **regular**: if \(x\notin F\) with \(F\) closed, then \(x\) and \(F\) have disjoint open neighborhoods.
- \(T_4\): \(T_1\) and **normal**: disjoint closed sets have disjoint open neighborhoods.

Thus \(T_2,T_3,T_4\) are commonly called Hausdorff, regular, and normal, respectively, with the understanding that the \(T_1\) condition is included in the latter two names under this convention.
:::
