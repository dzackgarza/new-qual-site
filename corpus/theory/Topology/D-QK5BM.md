---
schema: qual/card@1
id: D-QK5BM
kind: definition
title: Euler characteristic of a finite CW complex
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
Let $X$ be a finite [[D-ZOU5G|CW complex]] with $c_n$ cells of dimension $n$.
The \dfn{Euler characteristic} of $X$ is
$$
\chi(X)\coloneqq\sum_{n\geq0}(-1)^nc_n.
$$
:::

::: {.theorem}
For a finite CW complex $X$,
$$
\chi(X)=\sum_{n\geq0}(-1)^n\rank H_n(X;\ZZ),
$$
where $H_n(X;\ZZ)$ is [[D-6BUWA|singular homology]] [@Hat02, Theorem 2.44].
Consequently $\chi(X)$ does not depend on the CW structure, and finite CW complexes that are homotopy equivalent have the same Euler characteristic.
:::
