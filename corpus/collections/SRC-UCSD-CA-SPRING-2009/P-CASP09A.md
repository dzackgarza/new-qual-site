---
schema: qual/card@1
id: P-CASP09A
kind: problem
title: "Maximum modulus bounds on the coefficients of a polynomial"
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
Suppose $f(z) = \sum_{n=0}^{N} a_n z^n$ where $a_n \in \mathbb{C}$ and $N > 0$.
Let $M$ be the maximum of $|f(z)|$ on the unit circle about the origin.

(a) Show that $|a_0| \leq M$.

(b) Show that $|a_N| \leq M$.
:::

::: {.solution}
**Goal.** For $f(z) = \sum_{n=0}^N a_n z^n$ with $M = \max_{|z|=1} |f(z)|$, show $|a_0| \le M$ and $|a_N| \le M$.

::: pf

::: {.pf-step #s1}

(a) $|a_0| \le M$.

::: pf-proof

::: pf-step

$a_0 = \frac{1}{2\pi i}\oint_{|z|=1} \frac{f(z)}{z}\,dz$.

::: pf-proof

Cauchy's integral formula for the coefficient $a_0 = f(0)$.

:::

:::

::: pf-step

$|a_0| \le \frac{1}{2\pi}\int_0^{2\pi} |f(e^{i\theta})|\,d\theta \le M$.

::: pf-proof

parametrize $z = e^{i\theta}$; $|f(e^{i\theta})| \le M$ on the unit circle, so the average is $\le M$.

:::

:::

:::

:::

::: {.pf-step #s2}

(b) $|a_N| \le M$.

::: pf-proof

::: pf-step

$a_N = \frac{1}{2\pi i}\oint_{|z|=1} \frac{f(z)}{z^{N+1}}\,dz$.

::: pf-proof

Cauchy's integral formula for the coefficient $a_N$.

:::

:::

::: pf-step

$|a_N| \le \frac{1}{2\pi}\int_0^{2\pi} |f(e^{i\theta})|\,d\theta \le M$.

::: pf-proof

parametrize $z = e^{i\theta}$; $|z^{N+1}| = 1$ on the unit circle, so the integrand has modulus $|f(e^{i\theta})| \le M$.

:::

:::

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give (a) and (b).

:::

:::

:::
