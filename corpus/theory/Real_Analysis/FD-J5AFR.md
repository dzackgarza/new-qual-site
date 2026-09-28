---
schema: qual/card@1
id: FD-J5AFR
kind: definition
title: The $L^\infty$ norm
prompts:
- What is the infinity norm $\norm{f}_\infty$?
classification:
  areas:
  - real-analysis
  topics:
  - L∞
  - Norms
relations: []
review: draft
---

::: {.definition}
Let $(X,\mcm,m)$ be a [[D-QYLPH|measure]] space and let $f\colon X\to\CC$ be [[D-DHFN4|measurable]].
The \dfn{$L^\infty$ norm} of $f$ is
$$
\norm{f}_\infty \coloneqq \inf \theset{\alpha \geq 0 \suchthat m\qty{\theset{x\in X\suchthat \abs{f(x)} \geq \alpha}} = 0} \in[0,\infty].
$$
:::

::: {.remark}
When $\norm{f}_\infty<\infty$, it is the least real number $c$ with $\abs{f}\leq c$ almost everywhere.
:::
