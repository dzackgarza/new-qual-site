---
schema: qual/card@1
id: D-JNCUB
kind: definition
title: Characteristic
prompts:
- What is the characteristic of a ring?
classification:
  areas:
  - algebra
  topics:
  - Characteristic
  - Rings
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring.
The \dfn{characteristic} of $R$ is the smallest integer $n\geq 1$ such that $\sum_{k=1}^n 1_R = 0$ if such an integer exists, and $0$ otherwise.
:::

::: {.remark}
The characteristic of $R$ is the nonnegative generator $n$ of the kernel $n\ZZ$ of the unique ring homomorphism $\ZZ\to R$: an integer $m\geq 1$ lies in the kernel exactly when $\sum_{j=1}^m 1_R=0_R$, and the kernel is $0$ exactly when no such $m$ exists.
:::
