---
schema: qual/card@1
id: E-XJHKI
kind: problem
title: Primitive odd $n$th root of unity implies a primitive $2n$th root of unity
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Fields
  - Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the order argument directly instead of a divisor case split.
---

::: {.exercise}
Suppose $K$ has characteristic different from $2$ and contains a primitive $n$th root of unity for odd $n$. Prove that $K$ contains a primitive $2n$th root of unity.
:::

::: {.solution}
Let $\zeta\in K$ have order $n$, with $n$ odd.

::: pf

::: {.pf-step #order-divides}
If $(-\zeta)^m=1$, then $2n\mid m$.

::: pf-proof
From $(-\zeta)^m=1$ we get $\zeta^m=(-1)^m$.
If $m$ were odd, the group $\langle\zeta\rangle$ of odd order $n$ would contain $-1$, which has order $2$ because $\operatorname{char}K\ne2$; this is impossible by Lagrange's theorem.
Hence $m$ is even, so $\zeta^m=1$ and $n\mid m$.
Since $n$ is odd and $2\mid m$, $2n\mid m$.
:::

:::

::: pf-step
$-\zeta$ is a primitive $2n$th root of unity in $K$.

::: pf-proof
$(-\zeta)^{2n}=\zeta^{2n}=1$, and by step [](#order-divides){.pf-ref} no smaller positive exponent annihilates $-\zeta$.
:::

:::

:::

:::
