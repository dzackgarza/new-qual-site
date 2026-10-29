---
schema: qual/card@1
id: P-UFD6Y
kind: problem
title: The center of $S_3$ is trivial
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Permutations
relations: []
review: draft
---

::: {.problem}
Show that
$$
Z(S_3)=\{e\}.
$$
:::

::: {.solution}
The elements of $S_3$ are the identity, the three transpositions, and the two $3$-cycles.

::: pf

::: {.pf-step #transpositions}
No transposition lies in $Z(S_3)$.

::: pf-proof
A transposition does not commute with a different transposition that shares one point with it; conjugating, it suffices to note $(12)(23)=(123)\ne(132)=(23)(12)$.
:::

:::

::: {.pf-step #three-cycles}
No $3$-cycle lies in $Z(S_3)$.

::: pf-proof
$(123)(12)=(13)\ne(23)=(12)(123)$, and $(132)=(123)^{-1}$ is central exactly when $(123)$ is.
:::

:::

::: pf-step
$Z(S_3)=\{e\}$.

::: pf-proof
By steps [](#transpositions){.pf-ref} and [](#three-cycles){.pf-ref}, the identity is the only remaining element.
:::

:::

:::

:::
