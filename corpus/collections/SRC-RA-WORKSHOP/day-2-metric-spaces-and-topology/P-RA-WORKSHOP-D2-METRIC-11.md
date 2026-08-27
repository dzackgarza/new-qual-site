---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-11
kind: problem
title: A monotone increasing function has at most countably many jump discontinuities
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Limits
  - Countability
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Show that if $f:\mathbb R\to\mathbb R$ is monotone increasing, then $f$ has at most a countable set of jump discontinuities.
:::

:::: {.solution}
<1>1. Every discontinuity of a monotone increasing $f$ is a jump.
Proof: at each $x$, the one-sided limits $f(x-) = \sup_{y<x}f(y)$ and $f(x+) = \inf_{y>x}f(y)$ exist (boundedness on compact intervals follows from monotonicity; for the extended real line they exist in $[-\infty,\infty]$). Continuity at $x$ holds iff $f(x-) = f(x) = f(x+)$, so a discontinuity is exactly a point where $f(x-) < f(x+)$, a jump of positive size.
<1>2. Associate to each jump point a distinct rational.
Proof: for a jump at $x$, pick a rational $q(x) \in (f(x-), f(x+))$ (possible since the interval is nonempty and $\mathbb{Q}$ is dense).
<1>3. Distinct jump points get distinct rationals.
Proof: if $x_1 < x_2$ are jump points, then $f(x_1+) \le f(x_2-)$ (as $f$ is increasing), so the intervals $(f(x_1-), f(x_1+))$ and $(f(x_2-), f(x_2+))$ are disjoint; hence $q(x_1) \ne q(x_2)$.
Thus $x \mapsto q(x)$ is injective from the set of jump discontinuities into $\mathbb{Q}$.
<1>4. Q.E.D. Proof: the jump set injects into the countable set $\mathbb{Q}$, so it is at most countable.
:::
