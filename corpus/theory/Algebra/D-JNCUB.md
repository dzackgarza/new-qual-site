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
The characteristic of $R$ is the nonnegative generator of the kernel of the unique ring homomorphism
$$
\ZZ\longrightarrow R,
\qquad
n\longmapsto n\cdot1_R.
$$
Thus the kernel is $n\ZZ$ when $\characteristic R=n>0$, and is zero when $\characteristic R=0$.
:::
