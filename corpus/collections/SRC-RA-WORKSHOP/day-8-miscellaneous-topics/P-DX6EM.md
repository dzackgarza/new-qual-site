---
schema: qual/card@1
id: P-DX6EM
kind: problem
title: A function of bounded variation is the difference of two increasing functions
classification:
  areas:
  - real-analysis
  topics:
  - Variation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $f \colon [a,b] \to \mathbb{R}$.
Suppose $f \in \text{BV}[a,b]$.
Prove $f$ is the difference of two increasing functions.
:::
::: {.solution}

::: pf

::: pf-step

Define the total variation $V(x) = \sup \sum_{i=1}^n |f(x_i) - f(x_{i-1})|$ over all partitions $a = x_0 < \cdots < x_n = x$ of $[a, x]$, for $a \le x \le b$.

::: pf-proof

$V$ is well-defined and finite because $f \in \text{BV}[a,b]$ (so $V(b) < \infty$), and $V(a) = 0$.

:::

:::

::: {.pf-step #s2}

$V$ is increasing on $[a,b]$: for $a \le x < y \le b$, $V(y) \ge V(x)$.

::: pf-proof

partitions of $[a,x]$ extend to partitions of $[a,y]$ by adding the point $y$, so the sup over the larger interval is $\ge$.

:::

:::

::: {.pf-step #s3}

$V + f$ and $V - f$ are increasing on $[a,b]$.

::: pf-proof

::: {.pf-step #s3-1}

For $a \le x < y \le b$: $V(y) - V(x) \ge |f(y) - f(x)|$.

::: pf-proof

$V(y) \ge V(x) + |f(y) - f(x)|$: a partition of $[a,x]$ achieving within $\eps$ of $V(x)$, extended by $y$, gives a partition of $[a,y]$ with variation $\ge V(x) + |f(y)-f(x)| - \eps$; let $\eps \to 0$.

:::

:::

::: pf-step

$(V + f)(y) - (V + f)(x) = (V(y) - V(x)) + (f(y) - f(x)) \ge |f(y)-f(x)| + (f(y)-f(x)) \ge 0$.

::: pf-proof

Step [](#s3-1){.pf-ref} and $|u| + u \ge 0$.

:::

:::

::: pf-step

$(V - f)(y) - (V - f)(x) = (V(y) - V(x)) - (f(y) - f(x)) \ge |f(y)-f(x)| - (f(y)-f(x)) \ge 0$.

::: pf-proof

Step [](#s3-1){.pf-ref} and $|u| - u \ge 0$.

:::

:::

:::

:::

::: pf-qed

: $f = \frac12(V + f) - \frac12(V - f)$ is a difference of two increasing functions.

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} show both $V + f$ and $V - f$ are increasing (multiplying by $1/2$ preserves monotonicity), and the identity $f = \frac12(V+f) - \frac12(V-f)$ is a direct algebraic rearrangement.

:::

:::

:::
