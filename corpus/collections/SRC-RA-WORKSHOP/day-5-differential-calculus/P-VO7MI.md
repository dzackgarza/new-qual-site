---
schema: qual/card@1
id: P-VO7MI
kind: problem
title: "The derivative as a limit of difference quotients"
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Use the definition of the derivative to prove that if $f$ and $g$ are differentiable at $x$, then $fg$ is differentiable at $x$.
:::
::: {.solution}
::: pf

::: {.pf-step #s1}
Write the difference quotient of $fg$.

::: pf-proof
for $h \neq 0$, \[ \frac{(fg)(x+h) - (fg)(x)}{h} = \frac{f(x+h)g(x+h) - f(x)g(x)}{h} = \frac{f(x+h) - f(x)}{h}\,g(x+h) + f(x)\,\frac{g(x+h) - g(x)}{h}. \]
:::

:::

::: {.pf-step #s2}
$g$ is continuous at $x$.

::: pf-proof
$g$ is differentiable at $x$, hence continuous at $x$: $g(x+h) \to g(x)$ as $h \to 0$.
:::

:::

::: pf-step
Pass to the limit.

::: pf-proof
as $h \to 0$, $\frac{f(x+h)-f(x)}{h} \to f'(x)$, $g(x+h) \to g(x)$ (step [](#s2){.pf-ref}), and $\frac{g(x+h)-g(x)}{h} \to g'(x)$; substituting into step [](#s1){.pf-ref}, \[ \lim_{h\to 0}\frac{(fg)(x+h)-(fg)(x)}{h} = f'(x)g(x) + f(x)g'(x), \] so $fg$ is differentiable at $x$ with derivative $f'(x)g(x) + f(x)g'(x)$.
:::

:::

:::
:::
