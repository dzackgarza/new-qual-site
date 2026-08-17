---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-BV1
kind: problem
title: 'Every bounded-variation function is a difference of increasing functions'
classification:
  areas:
  - real-analysis
  topics:
  - variation
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(January 2018) Let $f:[a,b]\to\mathbb R$.
Suppose $f\in\operatorname{BV}[a,b]$.
Prove $f$ is the difference of two increasing functions.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Prove that if $f \in \operatorname{BV}[a,b]$ then $f$ is the difference of two increasing functions.

<1>1. Define $v(x) := V_a^x f$, the total variation of $f$ on $[a,x]$.
Proof: $V_a^x f = \sup\sum_i|f(t_i) - f(t_{i-1})|$ over partitions $a = t_0 < \cdots < t_k = x$.
This is finite for each $x \in [a,b]$ since $f \in BV[a,b]$.

<1>2. $v$ is increasing on $[a,b]$.
Proof: if $a \le x < y \le b$, every partition of $[a,x]$ extends to a partition of $[a,y]$, so $V_a^x f \le V_a^y f$.

<1>3. $v - f$ is increasing on $[a,b]$.
Proof: for $a \le x < y \le b$, $V_a^y f \ge V_a^x f + |f(y) - f(x)|$, since the partition of $[a,x]$ plus the point $y$ gives $V_a^x f + |f(y)-f(x)|$ as a lower bound for $V_a^y f$.
Hence $(v-f)(y) - (v-f)(x) = V_a^y f - V_a^x f - (f(y) - f(x)) \ge |f(y) - f(x)| - (f(y) - f(x)) \ge 0$.

<1>4. $f = v - (v - f)$ is the difference of two increasing functions.
Proof: $v$ is increasing by <1>2 and $v - f$ is increasing by <1>3.

<1>5. Q.E.D. Proof: <1>4 is the claim.
:::
