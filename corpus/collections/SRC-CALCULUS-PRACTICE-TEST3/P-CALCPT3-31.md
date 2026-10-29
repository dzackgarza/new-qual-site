---
schema: qual/card@1
id: P-CALCPT3-31
kind: problem
title: "Integral of a quarter circle glued to a line on $[0,2]$"
classification:
  areas: [prelim]
  topics: [Integrals]
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 31 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction; they agree."
---

::: {.problem}
If
$$f(x)=\begin{cases}\sqrt{1-x^2} & \text{for } 0\le x\le 1,\\ x-1 & \text{for } 1<x\le 2,\end{cases}$$
then $\int_0^2 f(x)\,dx$ is

(A) $\frac{\pi}{2}$
(B) $\frac{\sqrt2}{2}$
(C) $\frac12+\frac{\pi}{4}$
(D) $\frac12+\frac{\pi}{2}$
(E) undefined
:::

::: {.solution}
The integral splits at $x=1$ into the two pieces of $f$.

::: pf

::: {.pf-step #quarter}
$\int_0^1\sqrt{1-x^2}\,dx=\frac\pi4$.

::: pf-proof
The region under $y=\sqrt{1-x^2}$ for $0\le x\le1$ is the quarter of the unit disk in the first quadrant, which has area $\frac14\pi$.
:::

:::

::: {.pf-step #line}
$\int_1^2(x-1)\,dx=\frac12$.

::: pf-proof
$\int_1^2(x-1)\,dx=\left[\frac{(x-1)^2}2\right]_1^2=\frac12$.
:::

:::

::: pf-step
$\int_0^2f(x)\,dx=\boxed{\frac12+\frac\pi4}$, choice (C).

::: pf-proof
$f$ is bounded with one jump at $x=1$, so it is Riemann integrable and (E) is wrong. Additivity over $[0,1]$ and $[1,2]$ with steps [](#quarter){.pf-ref} and [](#line){.pf-ref} gives $\frac12+\frac\pi4\approx1.285$, which differs from (A) $\approx1.571$, (B) $\approx0.707$, and (D) $\approx2.071$.
:::

:::

:::

:::
