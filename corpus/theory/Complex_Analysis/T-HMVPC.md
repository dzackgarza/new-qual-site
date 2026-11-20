---
schema: qual/card@1
id: T-HMVPC
kind: theorem
title: A continuous function with the mean value property is harmonic
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Mean Value Property
relations: []
review: draft
---

::: {.theorem}
Let $U\subseteq\RR^2$ be open and let $u\colon U\to\RR$ be continuous.
If
$$
u(z_0) = {1\over2\pi}\int_0^{2\pi}u\qty(z_0+re^{i\theta})\,d\theta
$$
for every $z_0\in U$ and every $r>0$ with $\overline{\DD_r(z_0)}\subseteq U$, then $u$ is harmonic on $U$.
:::

::: {.remark}
With this converse, the mean value property characterizes harmonic functions among the continuous ones; the forward direction is the mean value property of the real part of a holomorphic function.
:::
