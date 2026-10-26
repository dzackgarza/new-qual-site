---
schema: qual/card@1
id: P-TRIV-PR14
kind: problem
title: No nonnegative solution of $\int \frac{x(t)\,dt}{(y-t)^2+1}=e^{-y^2}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 14, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains one or more nonprinting control bytes at this source position; they were removed from the authored card as nonsemantic extraction artifacts.
---

::: {.problem}
Prove that the equation

$$
\int _ { - \infty } ^ { \infty } { \frac { x ( t ) d t } { ( y - t ) ^ { 2 } + 1 } } = e ^ { - y ^ { 2 } }\tag{44}
$$

has no nonnegative solutions $x ( t )$
:::

Suppose, for contradiction, that $x(t)\geq0$ and that the displayed integral equals $e^{-y^2}$ for every real $y$.

::: pf

::: pf-step

Evaluating the equation at $y=0$ gives
\[
\int_{-\infty}^{\infty}\frac{x(t)}{t^2+1}\,dt=1.
\]


::: pf-proof

Set $y=0$ in the assumed equation. The right side is $e^0=1$.

:::

:::

::: pf-step

For every $y,t\in\mathbb R$,
\[
(y-t)^2+1\leq 2(1+y^2)(1+t^2).
\]


::: pf-proof

Using $(y-t)^2\leq2y^2+2t^2$ gives
\[
(y-t)^2+1\leq2y^2+2t^2+1
\leq2(1+y^2+t^2+y^2t^2)
=2(1+y^2)(1+t^2).
\]

:::

:::

::: pf-step

Since $x(t)\geq0$, steps <1>1--<1>2 imply
\[
\int_{-\infty}^{\infty}
\frac{x(t)}{(y-t)^2+1}\,dt
\geq\frac{1}{2(1+y^2)}.
\]


::: pf-proof

Step <1>2 implies
\[
\frac1{(y-t)^2+1}
\geq\frac1{2(1+y^2)(1+t^2)}.
\]
Multiply by the nonnegative function $x(t)$ and integrate. Step <1>1 evaluates the remaining integral.

:::

:::

::: pf-step

The assumed equation would therefore require
\[
e^{-y^2}\geq\frac1{2(1+y^2)}
\]
for every real $y$.


::: pf-proof

Replace the left side of the inequality in step <1>3 by the assumed value $e^{-y^2}$.

:::

:::

::: pf-step

The inequality in step <1>4 is false for sufficiently large $|y|$.


::: pf-proof

Equivalently, step <1>4 asserts
\[
e^{y^2}\leq2(1+y^2).
\]
But $e^{s}/(1+s)\to\infty$ as $s\to\infty$. For example, at $y=2$ it already fails because $e^4>10$.

:::

:::

::: pf-step

Hence the integral equation has no nonnegative solution $x(t)$.


::: pf-proof

Steps <1>4--<1>5 contradict the assumption preceding step <1>1.

:::

:::

::: pf-qed

Step <1>6 proves the claim.

:::

:::
