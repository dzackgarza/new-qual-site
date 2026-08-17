---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-W2
kind: problem
title: 'A continuous self-map of an interval has a fixed point'
classification:
  areas:
  - real-analysis
  topics:
  - fixed-points
  - continuity
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(c.f. June 2012 #1b) If $f:[0,1]\to[0,1]$ is continuous, show that $f(x)=x$ for some $x\in[0,1]$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Consider $g(x) = f(x) - x$ on $[0,1]$.
Proof: $g$ is continuous (difference of continuous functions).
At the endpoints: \[g(0) = f(0) - 0 = f(0) \ge 0 \quad (\text{as } f([0,1]) \subseteq [0,1]),\] \[g(1) = f(1) - 1 \le 0 \quad (\text{as } f(1) \le 1).\] <1>2. Apply the intermediate value theorem.
Proof: if $g(0) = 0$ or $g(1) = 0$, then $0$ or $1$ is a fixed point.
Otherwise $g(0) > 0$ and $g(1) < 0$, so by IVT there is $x \in (0,1)$ with $g(x) = 0$, i.e. $f(x) = x$.
<1>3. Q.E.D.
:::
