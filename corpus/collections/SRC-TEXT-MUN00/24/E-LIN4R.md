---
schema: qual/card@1
id: E-LIN4R
kind: problem
title: Linear continua in the dictionary order
classification:
  areas:
  - topology
  topics:
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Consider the following sets in the dictionary order.
Which are linear continua?

(a) $\mathbb{Z}_+ \times [0, 1)$

(b) $[0, 1) \times \mathbb{Z}_+$

(c) $[0, 1) \times [0, 1]$

(d) $[0, 1] \times [0, 1)$
:::

::: {.solution}
The linear continua are exactly (a) and (c).

(a) $\mathbb Z_+$ is well ordered, so the preceding exercise applies directly: $\mathbb Z_+\times[0,1)$ is a linear continuum.

(b) The subset
\[
\{0\}\times\mathbb Z_+
\]
of $[0,1)\times\mathbb Z_+$ is bounded above, for example by $(1/2,1)$. It has no least upper bound: any upper bound must have positive first coordinate, and there is no least positive element of $[0,1)$. Hence the least-upper-bound property fails.

(c) The order is dense. For the least-upper-bound property, let $A$ be nonempty and bounded above. Let $s$ be the supremum of the first coordinates of points of $A$. If $s$ occurs as a first coordinate in $A$, take the supremum of the corresponding second coordinates in the complete interval $[0,1]$; this gives the least upper bound. If $s$ does not occur, $(s,0)$ is the least upper bound (and boundedness ensures $s<1$ whenever this point is needed). Thus $[0,1)\times[0,1]$ is a linear continuum.

(d) The subset
\[
\{0\}\times[0,1)
\]
of $[0,1]\times[0,1)$ is bounded above, for instance by $(1/2,0)$, but has no least upper bound: an upper bound must have first coordinate $>0$, and there is no least positive real number. Thus (d) is not a linear continuum.
:::
