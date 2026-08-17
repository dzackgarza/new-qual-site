---
schema: qual/card@1
id: P-RA-WORKSHOP-D6-05
kind: problem
title: 'A positive continuous function has positive integral'
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - continuity
relations: []
review: draft
---

::: {.problem title="?"}
(January 2006 #4b) Suppose that $f$ is continuous and $f(x)\ge0$ on $[0,1]$.
If $f(0)>0$, prove that $$\int_0^1f(x)\,dx>0.$$
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. $f$ stays positive on a neighborhood of $0$.
    Proof: $f$ is continuous at $0$ and $f(0) > 0$, so with $\epsilon = f(0)/2$ there is $\delta > 0$ such that $|f(x) - f(0)| < f(0)/2$ for $|x - 0| < \delta$; hence $f(x) > f(0)/2$ on $[0, \delta]$ (taking $\delta \le 1$).
<1>2. Bound the integral from below.
    Proof: $f \ge 0$ everywhere and $f \ge f(0)/2$ on $[0,\delta]$, so
    \[\int_0^1 f(x)\,dx \ge \int_0^\delta f(x)\,dx \ge \int_0^\delta \frac{f(0)}{2}\,dx = \delta\frac{f(0)}{2} > 0.\]
<1>3. Q.E.D.
:::
