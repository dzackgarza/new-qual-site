---
schema: qual/card@1
id: D-YWRVG
kind: definition
title: Essential supremum and infimum, essentially bounded functions
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
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space and let $f\colon X\to\RR$ be [[D-DHFN4|measurable]].

- An \dfn{essential lower bound} of $f$ is a real number $b$ such that $S_{b} \coloneqq \theset{x\in X\suchthat f(x) < b } = f\inv((-\infty, b))$ has measure zero.
  The \dfn{essential infimum} of $f$ is the supremum of its essential lower bounds:
  $$
  \ess\inf f \coloneqq \sup \theset{b\in\RR\suchthat \mu (S_b) = 0}.
  $$

- An \dfn{essential upper bound} of $f$ is a real number $c$ such that $T_c \coloneqq \theset{x\in X\suchthat f(x) > c} = f\inv((c, \infty))$ has measure zero.
  The \dfn{essential supremum} of $f$ is the infimum of its essential upper bounds:
  $$
  \ess\sup f \coloneqq \inf \theset{c\in\RR\suchthat \mu (T_c) = 0}.
  $$

- A measurable function $g\colon X\to\CC$ is \dfn{essentially bounded} if $\norm{g}_\infty \coloneqq \ess\sup \abs{g} < \infty$.
:::

::: {.remark}
The essential infimum is the largest $b$ with $f\geq b$ almost everywhere, and the essential supremum is the smallest $c$ with $f\leq c$ almost everywhere, when these are finite.
An essentially bounded function is bounded outside a set of measure zero.
:::
