---
schema: qual/card@1
id: P-X2GQL
kind: problem
title: A Noetherian ring has every ideal finitely generated
classification:
  areas:
  - algebra
  topics:
  - Noetherian Rings
  - Ideals
relations: []
review: draft
---

::: {.problem}
Show that a Noetherian ring has every ideal finitely generated.
:::

::: {.solution}
If "Noetherian" is defined by the ascending-chain condition, suppose an ideal $I$ were not finitely generated. Choose $a_1\in I$, then inductively choose
$$
a_{n+1}\in I\setminus(a_1,\ldots,a_n).
$$
This produces a strictly ascending chain
$$
(a_1)\subsetneq(a_1,a_2)\subsetneq(a_1,a_2,a_3)\subsetneq\cdots,
$$
contradicting the ACC. Hence every ideal is finitely generated.
:::