---
schema: qual/card@1
id: FD-LXZIW
kind: definition
title: Characteristic of a ring
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
Let $R$ be a [[D-GURUB|ring]].
If there is an integer $n\geq 1$ with $\sum_{j=1}^n 1_R = 0_R$, the \dfn{characteristic} of $R$ is the smallest such $n$; otherwise the characteristic of $R$ is $0$.
:::

::: {.remark}
The characteristic of $R$ is the nonnegative generator $n$ of the kernel $n\ZZ$ of the unique ring homomorphism $\ZZ\to R$: an integer $m\geq 1$ lies in the kernel exactly when $\sum_{j=1}^m 1_R=0_R$, and the kernel is $0$ exactly when no such $m$ exists.
:::
