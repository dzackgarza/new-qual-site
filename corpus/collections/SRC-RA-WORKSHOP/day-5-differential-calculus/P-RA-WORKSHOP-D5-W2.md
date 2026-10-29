---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-W2
kind: problem
title: A quadratic difference bound forces constancy
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Mean Value Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
([Rud76, Exercise 5.1]) If $f:\RR\to\RR$ satisfies $\abs{f(x)-f(y)}\le(x-y)^2$ for all $x,y$, then $f$ is constant.
:::

::: {.solution}

::: pf

::: {.pf-step #zero-derivative}

The function $f$ is differentiable on $\RR$ and $f'\equiv0$.

::: pf-proof

Fix $y \in \RR$. For $x \ne y$,
$$
\abs{\frac{f(x) - f(y)}{x - y}} \le \frac{(x-y)^2}{\abs{x-y}} = \abs{x - y},
$$
which tends to $0$ as $x \to y$. Hence $f'(y)$ exists and equals $0$.

:::

:::

::: pf-step

The function $f$ is constant.

::: pf-proof

For $x<y$, the mean value theorem and step [](#zero-derivative){.pf-ref} give $\xi\in(x,y)$ with $f(y)-f(x)=f'(\xi)(y-x)=0$.

:::

:::

:::

:::
