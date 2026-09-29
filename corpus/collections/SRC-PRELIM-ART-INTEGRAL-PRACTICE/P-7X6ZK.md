---
schema: qual/card@1
id: P-7X6ZK
kind: problem
title: $\int_{0}^{\pi} \sqrt{1 + \cos(2x)} \, dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometry
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
1. $\displaystyle \int_{0}^{\pi} \sqrt {1 + \cos (2x)} ~dx= \color {blue} {2\sqrt {2}}$

- **Solution:** $\sqrt {1 + \cos (2x)} = \sqrt {2 \cos ^2 (x)} = \sqrt {2} \cos (x)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For all $x \in [0, \pi]$, $1 + \cos(2x) = 2\cos^2(x)$, hence $\sqrt{1 + \cos(2x)} = \sqrt{2}|\cos(x)|$.

::: pf-proof

By the cosine double-angle formula $\cos(2x) = 2\cos^2(x) - 1$.
Taking the principal square root gives $\sqrt{2\cos^2(x)} = \sqrt{2}\sqrt{\cos^2(x)} = \sqrt{2}|\cos(x)|$.

:::

:::

::: pf-step

Partitioning the integral over intervals of constant sign of $\cos(x)$: $$\int_0^\pi |\cos(x)| \, dx = \int_0^{\pi/2} \cos(x) \, dx + \int_{\pi/2}^\pi (-\cos(x)) \, dx.$$

::: pf-proof

::: pf-step

On $[0, \pi/2]$, $\cos(x) \ge 0$, so $|\cos(x)| = \cos(x)$.

:::

::: pf-step

On $[\pi/2, \pi]$, $\cos(x) \le 0$, so $|\cos(x)| = -\cos(x)$.

:::

::: pf-step

Splitting the domain of integration at $x = \pi/2$ and using these two identities gives the stated decomposition.

:::

:::

:::

::: {.pf-step #s3}

Computing each piece:

::: pf-proof

::: pf-step

$\int_0^{\pi/2} \cos(x) \, dx = [\sin(x)]_0^{\pi/2} = \sin(\pi/2) - \sin(0) = 1 - 0 = 1$.

:::

::: pf-step

$\int_{\pi/2}^\pi (-\cos(x)) \, dx = [-\sin(x)]_{\pi/2}^\pi = -\sin(\pi) - (-\sin(\pi/2)) = 0 + 1 = 1$.

:::

::: pf-step

Thus $\int_0^\pi |\cos(x)| \, dx = 1 + 1 = 2$.

:::

:::

:::

::: pf-step

Conclusion: $$\int_0^\pi \sqrt{1+\cos(2x)} \, dx = \sqrt{2} \int_0^\pi |\cos(x)| \, dx = 2\sqrt{2}.$$

::: pf-proof

::: pf-step

By step [](#s1){.pf-ref}, $\sqrt{1+\cos(2x)} = \sqrt{2}|\cos(x)|$, so the integral equals $\sqrt{2}\int_0^\pi|\cos(x)|\,dx$.

:::

::: pf-step

By step [](#s3){.pf-ref}, $\int_0^\pi|\cos(x)|\,dx = 2$, so the value is $\sqrt{2}\cdot 2 = 2\sqrt{2}$.

:::

:::

:::

:::

:::
