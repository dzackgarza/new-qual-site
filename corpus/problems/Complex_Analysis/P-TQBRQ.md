---
schema: qual/card@1
id: P-TQBRQ
kind: problem
title: A nonvanishing holomorphic function with $\abs{f}=1$ on the unit circle is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Schwarz Reflection
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Suppose $f$ is continuous and nonvanishing on $\bar \DD$, and holomorphic in $\DD$.
Prove that if $\abs{z} = 1 \implies \abs{f(z)} = 1$, then $f$ is constant.
:::

::: {.hint}
Extend $f$ to all of $\CC$ by $f(z) = 1/ \overline{f(1/\bar z)}$ for any $\abs{z} > 1$, and argue as in the Schwarz reflection principle.
:::

::: {.solution}

::: pf

::: {.pf-step #upper}

$\abs{f(z)} \leq 1$ for $z \in \DD$.

::: pf-proof

The function $f$ is continuous on the compact set $\bar\DD$ and holomorphic in $\DD$, so by the maximum modulus principle $\abs{f}$ attains its maximum over $\bar\DD$ on $\partial\DD$, where $\abs{f} = 1$.

:::

:::

::: {.pf-step #lower}

$\abs{f(z)} \geq 1$ for $z \in \DD$.

::: pf-proof

Since $f$ has no zero on $\bar\DD$, $1/f$ is continuous on $\bar\DD$ and holomorphic in $\DD$. The maximum modulus principle gives $\abs{1/f(z)} \leq \max_{\abs{\zeta}=1}\abs{1/f(\zeta)} = 1$ for $z \in \DD$.

:::

:::

::: pf-step

$f$ is constant.

::: pf-proof

By steps [](#upper){.pf-ref} and [](#lower){.pf-ref}, $\abs{f} = 1$ on $\DD$. Then $f(\DD)$ lies in the unit circle, which contains no nonempty open subset of $\CC$, so by the open mapping theorem $f$ is constant on $\DD$; by continuity it is constant on $\bar\DD$.

:::

:::

:::

:::
