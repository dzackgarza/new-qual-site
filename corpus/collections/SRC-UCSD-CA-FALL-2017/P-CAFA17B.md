---
schema: qual/card@1
id: P-CAFA17B
kind: problem
title: "Minimum modulus bound for holomorphic function approximating e^z/z"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $U \subset \mathbb{C}$ be an open set that contains the closed unit disc $\overline{\mathbb{D}} \subset U$.
Show that for all holomorphic functions $f: U \to \mathbb{C}$ we have $$\max_{|z|=1} \left|f(z) - \frac{e^z}{z}\right| \geq 1.$$
:::

::: {.solution}
**Goal.** Show $\max_{|z|=1} |f(z) - e^z/z| \ge 1$ for every holomorphic $f$ on $U \supseteq \overline{\DD}$.

::: pf

::: pf-step

Suppose $\max_{|z|=1} |f(z) - e^z/z| < 1$.

::: pf-proof

assume for contradiction.

:::

:::

::: pf-step

Then $|f(z) - e^z/z| < 1$ on $|z| = 1$, so $|z f(z) - e^z| < 1$ on $|z| = 1$.

::: pf-proof

multiply by $|z| = 1$.

:::

:::

::: pf-step

$z f(z) - e^z$ is holomorphic on $U$.

::: pf-proof

$f$ is holomorphic and $e^z$ is entire.

:::

:::

::: pf-step

By the maximum modulus principle, $|z f(z) - e^z| < 1$ on all of $\overline{\DD}$.

::: pf-proof

the maximum of a holomorphic function on $\overline{\DD}$ is attained on the boundary $|z| = 1$.

:::

:::

::: {.pf-step #s5}

Evaluate at $z = 0$: $|0 \cdot f(0) - e^0| = |0 - 1| = 1 < 1$, a contradiction.

::: pf-proof

at $z = 0$, $z f(z) - e^z = -1$, so its modulus is $1$, contradicting $< 1$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} gives the contradiction, so $\max_{|z|=1} |f(z) - e^z/z| \ge 1$.

:::

:::

:::
