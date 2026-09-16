---
schema: qual/card@1
id: PR-U5CHT
kind: proposition
title: One-step subgroup test
classification:
  areas:
  - algebra
  topics:
  - Subgroups
relations: []
review: draft
---

::: {.proposition}
Let $G$ be a group and $H \subseteq G$ a nonempty subset.
If $ab^{-1}\in H$ for all $a,b\in H$, then $H$ is a [[D-IQ4OX|subgroup]] of $G$.
:::

::: {.proof}
Choose $a\in H$; then $1=aa^{-1}\in H$.
For $b\in H$, $b^{-1}=1\cdot b^{-1}\in H$.
For $a,b\in H$, $ab=a(b^{-1})^{-1}\in H$.
:::
