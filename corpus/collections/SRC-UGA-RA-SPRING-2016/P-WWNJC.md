---
schema: qual/card@1
id: P-WWNJC
kind: problem
title: 'The norm of the functional $f\mapsto\int_0^1 f(x)e^x\,dx$ on $L^2([0,1])$, computed without the Riesz representation theorem'
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - L²
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Spring 2016 Problem 6 in the preserved UGA source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Without using the Riesz Representation Theorem, compute
$$
\sup \left\{\abs{\int_{0}^{1} f(x) e^{x} d x} \suchthat f \in L^{2}([0,1], m),~~ \norm{f}_{2} \leq 1\right\}
$$
:::

::: {.solution}

Let $e(x) \coloneqq e^x$ on $[0,1]$, so $\norm{e}_2^2 = \int_0^1 e^{2x}\,dx = \frac{e^2-1}{2}$.

::: pf

::: {.pf-step #upper}

$\abs{\int_0^1 f(x)e^x\,dx} \le \norm{e}_2$ whenever $\norm{f}_2 \le 1$.

::: pf-proof

By the Cauchy--Schwarz inequality, $\abs{\int_0^1 f(x)e^x\,dx} \le \norm{f}_2\norm{e}_2 \le \norm{e}_2$.

:::

:::

::: pf-step

The supremum is $\boxed{\sqrt{\frac{e^2-1}{2}}}$.

::: pf-proof

The function $f_0 \coloneqq e/\norm{e}_2$ has $\norm{f_0}_2 = 1$ and $\int_0^1 f_0(x)e^x\,dx = \norm{e}_2^2/\norm{e}_2 = \norm{e}_2$, so the bound of step [](#upper){.pf-ref} is attained.

:::

:::

:::

:::
