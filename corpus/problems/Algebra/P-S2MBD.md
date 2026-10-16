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
Let $\mathfrak p$ be prime and suppose $x^n\in\mathfrak p$. Repeated primality applied to
\[
x^n=x\cdot x^{n-1}
\]
shows $x\in\mathfrak p$. Thus $\mathfrak p=\sqrt{\mathfrak p}$.
:::