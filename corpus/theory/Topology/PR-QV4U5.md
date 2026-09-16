---
schema: qual/card@1
id: PR-QV4U5
kind: proposition
title: Inclusion-exclusion for Euler characteristic
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Mayer-Vietoris
relations: []
review: draft
---

::: {.proposition}
Let $X$ be a finite CW complex and $U, V\subseteq X$ subcomplexes with $X = U\cup V$.
Then
$$
\chi(X) = \chi(U) + \chi(V) - \chi (U\cap V)
.$$
:::

::: {.remark}
This follows by counting cells, since the [[D-QK5BM|Euler characteristic]] of a finite CW complex is the alternating sum of its numbers of cells [@Hat02, Theorem 2.44, p. 146].
:::
