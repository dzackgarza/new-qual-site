---
schema: qual/card@1
id: T-RA-WORKSHOP-D4-3-5
kind: theorem
title: Discontinuities of monotone functions
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Limits
relations: []
review: draft
---

::: {.theorem}
Let $a<b$ and let $f\colon(a,b)\to\RR$ be monotone.
Then the set $E\subseteq(a,b)$ of points at which $f$ is discontinuous is at most countable.
Moreover, every $x\in E$ is a jump discontinuity: the one-sided limits
$$
f(x-)\coloneqq\lim_{t\to x^-}f(t)\qquad\text{and}\qquad f(x+)\coloneqq\lim_{t\to x^+}f(t)
$$
both exist.
:::
