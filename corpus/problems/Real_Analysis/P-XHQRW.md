---
schema: qual/card@1
id: P-XHQRW
kind: problem
title: If $\lim_{x\to\infty}f(x)$ and $\lim_{x\to\infty}f'(x)$ exist, then $\lim f'=0$
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}

Show that if $f\in C^1(\RR)$ and both $\lim_{x\to \infty} f(x)$ and $\lim_{x\to \infty} f'(x)$ exist, then $\lim_{x\to\infty} f'(x)$ must be zero.

:::

::: {.solution}

Let $L = \lim_{x\to\infty} f(x)$ and $b = \lim_{x\to\infty} f'(x)$.

::: pf

::: {.pf-step #s1}

For each $x$ there is $\xi_x \in (x, x+1)$ with $f(x+1) - f(x) = f'(\xi_x)$.

::: pf-proof

This is the mean value theorem for the differentiable function $f$ on $[x, x+1]$.

:::

:::

::: {.pf-step #s2}

$f(x+1) - f(x) \to 0$ as $x \to \infty$.

::: pf-proof

Both terms tend to $L$.

:::

:::

::: pf-qed

Since $\xi_x > x$, $\xi_x \to \infty$ as $x \to \infty$, so $f'(\xi_x) \to b$. By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $f'(\xi_x) = f(x+1) - f(x) \to 0$, so $b = 0$.

:::

:::

:::
