---
schema: qual/card@1
id: PR-26CWE
kind: proposition
title: $L^1$ functions are finite almost everywhere
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space and let $f\colon X\to[-\infty,\infty]$ be [[D-DHFN4|measurable]] with $\int_X\abs{f}\dmu<\infty$.
Then
$$
\mu\qty{\theset{x\in X\suchthat \abs{f(x)} = \infty}} = 0 .
$$
:::

::: {.proof}
Let $A\coloneqq\theset{x\in X\suchthat \abs{f(x)}=\infty}$.
For every $t>0$, $\abs{f}\geq t\,\one_A$, so $t\,\mu(A)\le\int_X\abs{f}\dmu$.
Letting $t\to\infty$ gives $\mu(A)=0$.
:::
