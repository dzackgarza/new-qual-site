---
schema: qual/card@1
id: P-CALCPT3-09
kind: problem
title: "Evaluate $\\int_0^1 x/(2-x^2)\\,dx$"
classification:
  areas: [prelim]
  topics: [Integrals, u-Substitution]
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 9 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction, which drops choice (B); (B) was checked against the 300 dpi page render."
---

::: {.problem}
$$\int_0^1\frac{x}{2-x^2}\,dx=$$

(A) $-\frac12$
(B) $\frac53$
(C) $\frac{\log 2-e}{2}$
(D) $-\frac{\log 2}{2}$
(E) $\frac{\log 2}{2}$
:::

::: {.solution}
Here $\log$ is the natural logarithm.

::: pf

::: {.pf-step #antiderivative}
On $[0,1]$, the function $F(x)=-\frac12\log(2-x^2)$ is an antiderivative of $\frac{x}{2-x^2}$.

::: pf-proof
For $0\le x\le 1$ we have $2-x^2\ge 1>0$, so $F$ is differentiable there, and the chain rule gives $F'(x)=-\frac12\cdot\frac{-2x}{2-x^2}=\frac{x}{2-x^2}$.
:::

:::

::: pf-step
The integral equals $\boxed{\frac{\log 2}{2}}$, choice (E).

::: pf-proof
By the fundamental theorem of calculus and step [](#antiderivative){.pf-ref}, the integral is $F(1)-F(0)=-\frac12\log 1+\frac12\log 2=\frac{\log 2}{2}$.
:::

:::

:::

:::
