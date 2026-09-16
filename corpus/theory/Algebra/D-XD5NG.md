---
schema: qual/card@1
id: D-XD5NG
kind: definition
title: Normal closure of a field extension
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Splitting Fields
relations: []
review: draft
---

::: {.definition}
Let $K/k$ be an algebraic field extension.
A \dfn{normal closure} of $K/k$ is a field extension $N/K$ such that $N/k$ is [[D-LZTAK|normal]] and no proper subfield of $N$ containing $K$ is normal over $k$.
:::

::: {.remark}
A normal closure exists: inside an algebraic closure $\bar K$ of $K$, take the subfield generated over $k$ by all roots in $\bar K$ of the minimal polynomials over $k$ of the elements of $K$.
It is unique up to an isomorphism that restricts to the identity on $K$.
:::
