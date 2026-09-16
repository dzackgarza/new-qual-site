---
schema: qual/card@1
id: D-FHUV5
kind: definition
title: Group ring
classification:
  areas:
  - topology
  topics:
  - Rings
  - Groups
  - Representation Theory
relations: []
review: draft
---

::: {.definition}
Let $R$ be a [[D-GURUB|commutative ring]] and $G = \ts{g_1, \ldots, g_n}$ a finite group.
The \dfn{group ring} $RG$ is the [[D-LIEMF|free]] $R$-module with basis the elements of $G$,
$$
RG\coloneqq\ts{ \sum_{i=1}^n a_i g_i \st a_i\in R },
$$
with the multiplication that extends the group law $R$-bilinearly: $(ag)(bh)\coloneqq(ab)(gh)$ for $a, b\in R$ and $g, h\in G$.
:::

::: {.proposition}
The group ring $RG$ is a ring with identity $1_R 1_G$.
If $R\neq 0$, then $RG$ is commutative if and only if $G$ is abelian.
:::

::: {.concept}
See [@DF04, §7.2].
:::
