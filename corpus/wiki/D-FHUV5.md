---
schema: qual/card@1
id: D-FHUV5
kind: definition
title: "Group Ring"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

::: {.definition title="Group Ring"}
For $R$ a commutative ring with $1$ and $G = \ts{g_1, \cdots, g_n}$ a finite group, the **group ring** $RG$ is the free $R\dash$module on the elements of $G$,
\[
RG \da \ts{ \sum_{i=1}^n a_i g_i \st a_i \in R }
,\]
with multiplication extending the group law $R\dash$bilinearly, $\qty{a g}\qty{b h} = (ab)(gh)$.
It is a ring with identity $1_R\, 1_G$, and it is commutative iff $G$ is abelian.
:::

::: {.concept}
See Dummit and Foote, §7.2.
:::
