---
schema: qual/card@1
id: P-USAQT
kind: problem
title: Every proper ideal is contained in a maximal ideal
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
relations: []
review: draft
---

::: {.problem}
Let rings be commutative with identity. Show that every proper ideal is contained in a maximal ideal.
:::

::: {.solution}
Let $I\subsetneq R$. Consider the set of proper ideals containing $I$, ordered by inclusion. The union of a chain is again an ideal, and it is proper: if its union contained $1$, then one member of the chain would contain $1$. By Zorn's lemma there is a maximal member, i.e. a maximal ideal containing $I$.
:::