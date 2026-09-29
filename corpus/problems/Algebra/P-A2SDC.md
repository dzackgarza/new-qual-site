---
schema: qual/card@1
id: P-A2SDC
kind: problem
title: Subgroups of index two are normal
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Prove that a subgroup of index two is normal.
:::

::: {.solution}
Let $H\le G$ with $[G:H]=2$.

::: pf

::: {.pf-step #s1}

For $g\notin H$, $gH=G\setminus H=Hg$.

::: pf-proof

The left cosets partition $G$ into two sets, one of which is $H$; since $g\notin H$, $gH\neq H$, so $gH=G\setminus H$.
The same argument with right cosets gives $Hg=G\setminus H$.

:::

:::

::: pf-step

$gH=Hg$ for every $g\in G$.

::: pf-proof

For $g\in H$, $gH=H=Hg$; for $g\notin H$, use step [](#s1){.pf-ref}.

:::

:::

::: pf-qed

Multiplying $gH=Hg$ on the right by $g^{-1}$ gives $gHg^{-1}=H$ for every $g\in G$, so $H\trianglelefteq G$.

:::

:::

:::
