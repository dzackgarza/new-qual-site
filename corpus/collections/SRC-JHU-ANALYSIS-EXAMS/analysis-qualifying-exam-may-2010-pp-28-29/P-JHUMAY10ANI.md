---
schema: qual/card@1
id: P-JHUMAY10ANI
kind: problem
title: "Differentiation under the integral sign with a dominated partial derivative"
classification:
  areas:
  - real-analysis
  topics:
  - Lebesgue Integration
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 7 of the JHU Analysis Qualifying Exam, May 2010, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f:[0,1]\times[0,1]\to\RR$ be continuous. Assume that for each $x$, the map $t\mapsto f(x,t)$ is differentiable and that
$$
\abs{\frac{\partial f}{\partial t}(x,t)}\le g(x)
$$
for some measurable $g\in L^1([0,1])$. Define
$$
F(t)=\int_0^1 f(x,t)\,dx.
$$
Prove that
$$
F'(t)=\int_0^1\frac{\partial f}{\partial t}(x,t)\,dx.
$$
:::

::: {.solution}

The argument is the card's own: difference quotients dominated by the integrable $g$, so that dominated convergence may be applied under the integral. No retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $f:[0,1]^{2}\to\RR$ be continuous with $t\mapsto f(x,t)$ differentiable for each $x$ and $\abs{\partial_{t}f(x,t)}\le g(x)$ for a measurable $g\in L^{1}([0,1])$, and let $F(t)=\int_{0}^{1}f(x,t)\,dx$.

::: pf

::: {.pf-step #defined}
For each $t$ the function $x\mapsto f(x,t)$ is integrable, so $F(t)$ is defined and finite.

::: pf-proof
$f$ is continuous on the compact set $[0,1]^{2}$, hence bounded there by some $M<\infty$; so $\abs{f(x,t)}\le M$ for every $(x,t)$ and $x\mapsto f(x,t)$ is measurable and bounded on a finite measure space, hence integrable, with $\abs{F(t)}\le M$.
:::

:::

::: {.pf-step #quotients}
For $t\in(0,1)$ and $h\ne0$ with $t+h\in[0,1]$, the difference quotient
$$
q_{h}(x)=\frac{f(x,t+h)-f(x,t)}{h}
$$
satisfies $q_{h}(x)\to\partial_{t}f(x,t)$ as $h\to0$ for every $x$.

::: pf-proof
For fixed $x$ the function $s\mapsto f(x,s)$ is differentiable at $t$ with derivative $\partial_{t}f(x,t)$, and $q_{h}(x)$ is exactly its difference quotient at $t$ with increment $h$; so it tends to that derivative.
:::

:::

::: {.pf-step #domination}
$\abs{q_{h}(x)}\le g(x)$ for every $x$ and every admissible $h$.

::: pf-proof
By the mean value theorem applied to $s\mapsto f(x,s)$ on the interval with endpoints $t$ and $t+h$, there is $\theta$ strictly between them with
$$
q_{h}(x)=\frac{f(x,t+h)-f(x,t)}{h}=\partial_{t}f(x,\theta),
$$
and $\abs{\partial_{t}f(x,\theta)}\le g(x)$ by hypothesis. The quotient is also measurable in $x$, being continuous in $x$ since $f$ is.
:::

:::

::: {.pf-step #limit}
$F$ is differentiable at every $t\in(0,1)$ with $\displaystyle F'(t)=\int_{0}^{1}\partial_{t}f(x,t)\,dx$; and at $t=0$ and $t=1$ the corresponding one-sided derivatives are given by the same integral.

::: pf-proof
For $h$ with $t+h\in[0,1]$,
$$
\frac{F(t+h)-F(t)}{h}=\int_{0}^{1}\frac{f(x,t+h)-f(x,t)}{h}\,dx=\int_{0}^{1}q_{h}(x)\,dx
$$
by linearity of the integral, both integrands being integrable by step [](#defined){.pf-ref}. By steps [](#quotients){.pf-ref} and [](#domination){.pf-ref} the quotients converge pointwise to $\partial_{t}f(\cdot,t)$ and are dominated by the integrable $g$, so the dominated convergence theorem gives
$$
\lim_{h\to0}\frac{F(t+h)-F(t)}{h}=\int_{0}^{1}\partial_{t}f(x,t)\,dx,
$$
which is the assertion for $t\in(0,1)$. At $t=0$ only $h>0$ with $t+h\in[0,1]$ is admitted, and at $t=1$ only $h<0$; the mean value theorem and dominated convergence are used on those one-sided families, giving $\lim_{h\to0^{+}}$ and $\lim_{h\to0^{-}}$ equal to the same integral.
:::

:::

:::
:::
