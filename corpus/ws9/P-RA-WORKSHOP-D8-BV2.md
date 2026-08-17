---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-BV2
kind: problem
title: 'The reciprocal of a bounded-away-from-zero bounded-variation function'
classification:
  areas:
  - real-analysis
  topics:
  - variation
relations: []
review: draft
---

:::{.problem title="?"}
(January 2007, 6a) Let $f$ be a function of bounded variation on $[a,b]$. Furthermore, assume that for some $c>0$,
$|f(x)|\ge c$ on $[a,b]$. Show that $g(x)=1/f(x)$ is of bounded variation on $[a,b]$.
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** Show $g = 1/f$ is of bounded variation on $[a,b]$ given $f \in BV[a,b]$ and $|f(x)| \ge c > 0$.

<1>1. For any partition $a = x_0 < x_1 < \cdots < x_n = b$: $\sum_i |g(x_i) - g(x_{i-1})| \le \frac{1}{c^2}\sum_i |f(x_i) - f(x_{i-1})|$.
    Proof: $|g(x_i) - g(x_{i-1})| = \left|\frac{1}{f(x_i)} - \frac{1}{f(x_{i-1})}\right| = \frac{|f(x_{i-1}) - f(x_i)|}{|f(x_i)f(x_{i-1})|} \le \frac{|f(x_i) - f(x_{i-1})|}{c^2}$, since $|f(x_i)|, |f(x_{i-1})| \ge c$.

<1>2. $V_a^b g \le \frac{1}{c^2} V_a^b f < \infty$.
    Proof: take the supremum over all partitions in <1>1; the right-hand side is finite because $f \in BV[a,b]$.

<1>3. Q.E.D.
    Proof: <1>2 shows $g$ has finite total variation, i.e. $g \in BV[a,b]$.

:::
