---
schema: qual/card@1
id: D-LZTAK
kind: definition
title: Normal field extension
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Splitting Fields
  - Galois Theory
relations: []
review: draft
---

::: {.definition}
Let $L/k$ be an algebraic field extension.
The extension $L/k$ is \dfn{normal} if every [[D-BVMTZ|irreducible]] polynomial $f\in k[x]$ that has a root in $L$ splits into linear factors in $L[x]$.
:::

::: {.remark}
Equivalently, for every $\alpha\in L$, all roots of the minimal polynomial of $\alpha$ over $k$ in an algebraic closure of $L$, the conjugates of $\alpha$ over $k$, lie in $L$.
Thus an irreducible $f\in k[x]$ either splits in $L[x]$ or has no root in $L$.
:::
