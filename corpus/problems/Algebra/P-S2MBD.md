---
schema: qual/card@1
id: P-S2MBD
kind: problem
title: Every prime ideal is radical
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
relations: []
review: draft
---

::: {.problem}
Show that every prime ideal is radical.
:::

::: {.solution}

Let $\mathfrak p$ be a prime ideal of a commutative ring $R$.

::: pf

::: {.pf-step #power}

If $x^n\in\mathfrak p$ with $n\ge1$, then $x\in\mathfrak p$.

::: pf-proof

By induction on $n$; the case $n=1$ is clear. If $n\ge2$, then $x\cdot x^{n-1}\in\mathfrak p$, so primality gives $x\in\mathfrak p$ or $x^{n-1}\in\mathfrak p$, and in the second case $x\in\mathfrak p$ by the inductive hypothesis.

:::

:::

::: pf-qed

Always $\mathfrak p\subseteq\sqrt{\mathfrak p}$, and step [](#power){.pf-ref} gives $\sqrt{\mathfrak p}\subseteq\mathfrak p$. Hence $\mathfrak p=\sqrt{\mathfrak p}$.

:::

:::

:::
