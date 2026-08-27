---
schema: qual/card@1
id: D-QK5BM
kind: definition
title: Euler Characteristic
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Homology
  - Cell Complexes
relations: []
review: draft
---

::: {.definition}
For $X$ a finite CW complex with $c_n$ cells in dimension $n$,
\[
\chi(X) \da \sum_n (-1)^n c_n
.\]
This agrees with the homological Euler characteristic,
\[
\chi(X) = \sum_n (-1)^n \rank H_n(X;\ZZ)
,\]
so $\chi$ is independent of the cell structure and depends only on the homotopy type of $X$.
:::

::: {.concept}
See Hatcher, §2.2, Theorem 2.44, p. 146.
:::
