---
schema: qual/card@1
id: D-ITBUT
kind: definition
title: Quotient map
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Continuity
relations: []
review: draft
---

::: {.definition}
Let $X$ and $Y$ be topological spaces.
A map $q\colon X\to Y$ is a \dfn{quotient map} if $q$ is surjective and, for every $U\subseteq Y$, $U$ is open in $Y$ if and only if $q\inv(U)$ is open in $X$.
:::

::: {.remark}
The implication from $U$ open to $q\inv(U)$ open is [[D-AEAAD|continuity]] of $q$; a quotient map is a continuous surjection that also satisfies the converse implication.
:::

::: {.proposition}
A surjective map $q\colon X\to Y$ is a quotient map if and only if $q$ is continuous and $q(V)$ is open in $Y$ for every open subset $V\subseteq X$ that is [[D-KWWVL|saturated]] with respect to $q$.
The same holds with "open" replaced by "closed" throughout.
:::

::: {.concept}
See [@Mun00].
:::
