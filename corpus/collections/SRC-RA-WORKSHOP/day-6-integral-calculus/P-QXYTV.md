---
schema: qual/card@1
id: P-QXYTV
kind: problem
title: $\lim_{p\to\infty}\bigl(\int_a^b f^p\bigr)^{1/p}=\sup f$ for continuous $f\ge
  0$ on $[a,b]$
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - L∞
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Suppose that $f:[a,b]\to\mathbb{R}$ is continuous, $f\geq 0$ on $[a,b]$, and put $M=\sup\{f(x):x\in[a,b]\}$.
Prove that $$\lim_{p\to\infty}\left(\int_a^b f(x)^p\,dx\right)^{1/p}=M.$$
:::

::: {.solution}
::: pf

::: {.pf-step #s1}
Upper bound: $(\int_a^b f^p)^{1/p} \le M\,(b-a)^{1/p}$.

::: pf-proof
$0 \le f \le M$ on $[a,b]$, so $\int_a^b f^p \le M^p (b-a)$, and $(b-a)^{1/p} \to 1$.
:::

:::

::: {.pf-step #s2}
Hence $\limsup_{p\to\infty}(\int_a^b f^p)^{1/p} \le M$.

::: pf-proof
Step [](#s1){.pf-ref} and $(b-a)^{1/p} \to 1$.
:::

:::

::: {.pf-step #s3}
Lower bound: for each $0 < \eps < M$, $\liminf_{p\to\infty}(\int_a^b f^p)^{1/p} \ge M - \eps$.

::: pf-proof
since $f$ is continuous, it attains $M$ at some $x_0 \in [a,b]$.

The set $\{f > M - \eps\}$ is open (continuity) and contains $x_0$, so it contains an interval of length $\delta > 0$.
Hence \[ \int_a^b f^p \ge (M-\eps)^p \delta, \qquad \text{so} \qquad \Big(\int_a^b f^p\Big)^{1/p} \ge (M-\eps)\,\delta^{1/p} \to M - \eps . \]
:::

:::

::: pf-step
$\lim_{p\to\infty}(\int_a^b f^p)^{1/p} = M$.

::: pf-proof
Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} (letting $\eps \to 0$).
:::

:::

:::
:::
