---
schema: qual/card@1
id: P-RA-WORKSHOP-D6-08
kind: problem
title: 'A weighted integral attains a point value'
classification:
  areas:
  - real-analysis
  topics:
  - mean-value-theorem
  - integrals
  - continuity
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(January 2009 #4b) Let $f$ be a continuous real-valued function on $[0,1]$.
Prove that there exists at least one point $\xi\in[0,1]$ such that $$\int_0^1x^4f(x)\,dx=\frac15f(\xi).$$
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Apply the weighted mean value theorem for integrals.
Proof: $f$ is continuous on $[0,1]$ and $x^4 \ge 0$ is continuous (and integrable with $\int_0^1 x^4\,dx = 1/5$). By the first mean value theorem for integrals, there is $\xi \in [0,1]$ with \[\int_0^1 x^4 f(x)\,dx = f(\xi)\int_0^1 x^4\,dx = \frac{1}{5}f(\xi).\] <1>2. Q.E.D. Proof: (Explicitly: let $m = \min f$, $M = \max f$ on $[0,1]$; then $m/5 \le \int x^4 f \le M/5$, so $5\int x^4 f \in [m, M]$, and by IVT there is $\xi$ with $f(\xi) = 5\int_0^1 x^4f$.)
:::
