---
schema: qual/card@1
id: P-TOP-WORKSHOP-D4-W1
kind: problem
title: A neighborhood characterization of closure
classification:
  areas:
  - topology
  topics:
  - Closure
  - Point-Set Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked both directions of the equivalence
    against the definition of $\overline A$ as the intersection of the closed sets containing $A$: an
    open neighbourhood $U$ of $x$ missing $A$ gives the closed set $X\setminus U\supseteq A$ missing
    $x$, and conversely a closed $F\supseteq A$ missing $x$ gives the open set $X\setminus F$ meeting
    $A$ in nothing. Added: that $\overline A$ is contained in each such $F$, which is what the
    definition of the intersection supplies, and the identification of the second direction as the
    contrapositive. No defect found in the statement. The collection's provenance is the worksheet,
    so no retained solution set covers the item.
---

::: {.problem}
For a set $A\subset X$, $\overline A$ is defined to be the intersection of all closed sets containing $A$.
Using this definition, show: $x\in\overline A$ if and only if every open set $U$ containing $x$ intersects $A$.
:::

::: {.solution}
No retained solution set covers this item, the collection's provenance being the worksheet, so the argument is the card's own; it unpacks the definition of $\overline A$ as the intersection of the closed sets containing $A$.

::: pf

::: {.pf-step #inside}
If $x\in\overline A$ then every open set containing $x$ meets $A$.

::: pf-proof
Suppose $U$ is open, contains $x$, and satisfies $U\cap A=\varnothing$. Then $X\setminus U$ is closed and contains $A$, since $A\subseteq X\setminus U$. As $\overline A$ is the intersection of all closed sets containing $A$, it is contained in $X\setminus U$, so $x\in X\setminus U$, contradicting $x\in U$.
:::

:::

::: {.pf-step}
If every open set containing $x$ meets $A$, then $x\in\overline A$.

::: pf-proof
Suppose $x\notin\overline A$. Since $\overline A$ is an intersection of closed sets containing $A$, there is a closed $F\supseteq A$ with $x\notin F$. Then $X\setminus F$ is open, contains $x$, and is disjoint from $A$ because $A\subseteq F$. So a neighbourhood of $x$ misses $A$, which is the negation of the hypothesis. Hence $x\in\overline A$, and the two directions are steps [](#inside){.pf-ref} and this one.
:::

:::

:::
:::
