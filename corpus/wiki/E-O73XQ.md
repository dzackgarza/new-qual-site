---
schema: qual/card@1
id: E-O73XQ
kind: exercise
title: $G/Z(G)$ cyclic implies $G$ abelian; $G/N$ abelian iff $[G,G]\le N$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Commutators
  - Normal Subgroups
relations: []
review: draft
---

::: {.exercise title="?"}
\envlist

- Show that if $G/Z(G)$ is cyclic then $G$ is abelian.

- Show that $G/N$ is abelian iff $[G, G] \leq N$.

- Show that normal subgroups are not necessarily contained in $Z(G)$.

  - Hint: consider the order 3 subgroup of $S_3$.
:::

::: {.solution}
The $G/Z(G)$ theorem:

- Write $H\da Z(G)$ and $G/H = \gens{xH}$ as a cyclic quotient.

- Fix $a, b\in G$, then $aH = x^n H$ and $bH = x^m H$.

- So $ax^{-n} = h_1, bx^{-m} = h_2$ where the $h_i$ are now central.

- Now write $ab = (x^n h_1)(x^m h_2) = ba$ by commuting everything.
:::
