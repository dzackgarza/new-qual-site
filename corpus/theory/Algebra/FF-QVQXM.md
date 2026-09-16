---
schema: qual/card@1
id: FF-QVQXM
kind: fact
title: One-step subgroup test
prompts:
- State the one-step subgroup test.
classification:
  areas:
  - algebra
  topics:
  - Subgroups
relations: []
review: draft
---

::: {.fact}
Let $G$ be a group and let $H\subseteq G$ be a nonempty subset.
If $ab^{-1}\in H$ for all $a,b\in H$, then $H$ is a [[D-IQ4OX|subgroup]] of $G$.
:::

::: {.proof}
Choose $a\in H$; then $e=aa^{-1}\in H$.
For $b\in H$, $b^{-1}=eb^{-1}\in H$.
For $a,b\in H$, $ab=a(b^{-1})^{-1}\in H$.
:::
