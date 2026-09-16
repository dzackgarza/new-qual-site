---
schema: qual/card@1
id: PR-RIJSC
kind: proposition
title: Internal direct sum of two submodules
classification:
  areas:
  - algebra
  topics:
  - Modules
relations: []
review: draft
---

::: {.proposition}
Let $R$ be a ring, $M$ an $R$-module, and $M_1, M_2 \leq M$ submodules.
The $R$-linear map $M_1\oplus M_2\to M$, $(x,y)\mapsto x+y$, is an isomorphism, so that $M = M_1 \oplus M_2$ internally, if and only if

- $M_1 + M_2 = M$, and

- $M_1 \cap M_2 = 0$.
:::

::: {.proof}
The image of the map is $M_1+M_2$, so it is surjective if and only if $M_1+M_2=M$.
Its kernel is $\theset{(x,-x)\suchthat x\in M_1\cap M_2}$, so it is injective if and only if $M_1\cap M_2=0$.
:::
