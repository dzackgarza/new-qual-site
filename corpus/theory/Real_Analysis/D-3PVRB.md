---
schema: qual/card@1
id: D-3PVRB
kind: definition
title: Essential supremum norm and essentially bounded functions
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
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space and let $f\colon X\to\CC$ be [[D-DHFN4|measurable]].
The \dfn{essential supremum} of $\abs{f}$ is
$$
\norm{f}_\infty \coloneqq \inf \theset{\alpha \geq 0 \suchthat \mu\qty{\theset{x\in X \suchthat \abs{f(x)} \geq \alpha}} = 0} \in [0,\infty],
$$
with $\inf\emptyset=\infty$.
The function $f$ is \dfn{essentially bounded} if there exists a real number $c$ such that $\mu\qty{\theset{x\in X \suchthat \abs{f(x)} > c}} = 0$, equivalently $\norm{f}_\infty < \infty$.
:::

::: {.remark}
When $\norm{f}_\infty<\infty$, the set $\theset{\abs{f}>\norm{f}_\infty}=\bigcup_{k\geq 1}\theset{\abs{f}\geq\norm{f}_\infty+1/k}$ is a countable union of null sets, so $\abs{f(x)} \leq \norm{f}_\infty$ for almost every $x$, and $\norm{f}_\infty$ is the smallest constant with this property.
:::
