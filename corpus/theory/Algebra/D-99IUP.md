---
schema: qual/card@1
id: D-99IUP
kind: definition
title: Algebraic closure
prompts:
- What is an algebraic closure of a field?
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Field Extensions
relations: []
review: draft
---

::: {.definition}
Let $k$ be a field.
An \dfn{algebraic closure} of $k$ is an [[FD-NS5RF|algebraic]] extension $\bar k/k$ such that $\bar k$ is [[FD-3GZPO|algebraically closed]].
:::

::: {.proposition}
Every field $k$ has an algebraic closure.
If $\Omega_1$ and $\Omega_2$ are algebraic closures of $k$, then there is an isomorphism $\Omega_1\to\Omega_2$ that restricts to the identity on $k$ [@DF04, §13.4].
:::

::: {.remark}
The isomorphism is not unique: the $k$-automorphisms of $\bar\QQ$ form the infinite group $\Gal(\bar\QQ/\QQ)$, which contains complex conjugation.
For an algebraically closed field $\Omega$ containing $k$, the elements of $\Omega$ algebraic over $k$ form an algebraic closure of $k$; so $\bar\QQ$ is the field of algebraic numbers in $\CC$.
:::
