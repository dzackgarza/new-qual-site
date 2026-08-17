---
schema: qual/card@1
id: P-R4EGZ
kind: problem
title: "Suppose that $f$ is continuous and $f(x)\\geq 0$"
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - continuity
relations: []
review: draft
---

::: problem
Suppose that $f$ is continuous and $f(x)\geq 0$ on $[0,1]$.
If $f(0)>0$, prove that $\int_0^1 f(x)dx>0$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Since $f(0) > 0$ and $f$ is continuous, there is $\delta \in (0,1)$ with $f(x) > f(0)/2$ for all $x \in [0,\delta]$.
    Proof: continuity at $0$ with $\eps = f(0)/2 > 0$ gives $|f(x) - f(0)| < f(0)/2$ for $|x| < \delta$, hence $f(x) > f(0) - f(0)/2 = f(0)/2$.
<1>2. $\int_0^1 f \ge \int_0^\delta f \ge \delta \cdot f(0)/2 > 0$.
    Proof: $f \ge 0$ on $[0,1]$ gives $\int_0^1 f \ge \int_0^\delta f$; and on $[0,\delta]$, $f \ge f(0)/2$ by <1>1, so $\int_0^\delta f \ge \delta f(0)/2 > 0$.
<1>3. Q.E.D.
:::
