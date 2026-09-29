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
- Show that if $f\in C^1(\RR)$ and both $\lim_{x\to \infty} f(x)$ and $\lim_{x\to \infty} f'(x)$ exist, then $\lim_{x\to\infty} f'(x)$ must be zero.
:::
::: {.solution}

::: pf

::: {.pf-step #s1}
Apply the mean value theorem on $[x, x+1]$.

::: pf-proof
$f \in C^1(\RR)$, so for each $x$ there is $\xi_x \in (x, x+1)$ with \[ f(x+1) - f(x) = f'(\xi_x) . \]
:::

:::

::: {.pf-step #s2}
The left-hand side tends to $0$.

::: pf-proof
$\lim_{x\to\infty}f(x)$ exists, so $f(x+1) - f(x) \to L - L = 0$.
:::

:::

::: pf-step
Conclude $\lim_{x\to\infty}f'(x) = 0$.

::: pf-proof
$\xi_x \to \infty$ as $x \to \infty$, and $\lim_{x\to\infty}f'(x)$ exists (call it $b$); along the path $x \mapsto \xi_x$, $f'(\xi_x) \to b$.

By step [](#s1){.pf-ref} and step [](#s2){.pf-ref}, $b = 0$.
:::

:::

:::

:::
