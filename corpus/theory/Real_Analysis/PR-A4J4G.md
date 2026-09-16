---
schema: qual/card@1
id: PR-A4J4G
kind: proposition
title: Subtraction of measures
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,m)$ be a [[D-QYLPH|measure]] space and let $A,C\in\mcm$ with $C\subseteq A$ and $m(C) < \infty$.
Then
$$
m(A\setminus C) = m(A) - m(C)
$$
[@Fol13].
:::

::: {.remark}
The hypothesis $m(C)<\infty$ cannot be dropped: for Lebesgue measure with $A = C = \RR$, the right-hand side $\infty-\infty$ is undefined.
:::
