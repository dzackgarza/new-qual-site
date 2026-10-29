---
schema: qual/card@1
id: P-UKIC7
kind: problem
title: Differentiable $f\le g$ with $f(x_0)=g(x_0)$ satisfy $f'(x_0)=g'(x_0)$
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
Suppose that $f,g:\RR\to\RR$ are differentiable, that $f(x)\leq g(x)$ for all $x\in\RR$, and that $f(x_0)=g(x_0)$ for some $x_0$.
Prove that $f'(x_0)=g'(x_0)$.
:::

::: {.solution}
Set $h \coloneqq g - f$. Then $h \ge 0$, $h(x_0) = 0$, and $h$ is differentiable with $h' = g' - f'$.

::: pf

::: {.pf-step #s2}

The right derivative satisfies $h'_+(x_0)\geq0$.

::: pf-proof

For $x > x_0$, $h(x) \ge 0 = h(x_0)$, so $(h(x) - h(x_0))/(x - x_0) \ge 0$. Hence $h'_+(x_0) = \lim_{x \to x_0^+}\frac{h(x)-h(x_0)}{x-x_0} \ge 0$.

:::

:::

::: {.pf-step #s3}

The left derivative satisfies $h'_-(x_0)\leq0$.

::: pf-proof

For $x < x_0$, $x - x_0 < 0$ and $h(x) - h(x_0) \ge 0$, so $(h(x)-h(x_0))/(x-x_0) \le 0$. Hence $h'_-(x_0) \le 0$.

:::

:::

::: pf-step

$f'(x_0) = g'(x_0)$.

::: pf-proof

Since $h$ is differentiable at $x_0$, $h'(x_0) = h'_+(x_0) = h'_-(x_0)$. By steps [](#s2){.pf-ref} and [](#s3){.pf-ref} this common value satisfies $0 \le h'(x_0) \le 0$, so $0=h'(x_0)=g'(x_0)-f'(x_0)$.

:::

:::

:::

:::
