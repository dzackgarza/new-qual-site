---
schema: qual/card@1
id: P-BKF83-9
kind: problem
title: Parameters yielding infinitely many critical points for a forced second-order ODE
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: "Checked the literal source wording: no nonconstant hypothesis is imposed, so the constant equilibrium y=3 answers the existence question for every real p."
---

::: {.problem}
For which real values of $p$ does the differential equation
\[
y''+2py'+y=3
\]
admit a solution with infinitely many critical points?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every real value of $p$, the constant function
$$
y(x)\equiv3
$$
is a solution of the differential equation.

::: pf-proof

For the constant function $y=3$,
$$
y'=0,
\qquad
y''=0.
$$
Hence, for every $p\in\mathbb R$,
$$
y''+2py'+y
=
0+0+3
=3.
$$

:::

:::

::: {.pf-step #s2}

This solution has infinitely many critical points.

::: pf-proof

A critical point of a differentiable real-valued function is a point where
its derivative vanishes. For the solution in step [](#s1){.pf-ref},
$$
y'(x)=0
$$
for every $x\in\mathbb R$. Thus every real number is a critical point.

:::

:::

::: {.pf-step #s3}

The required set of parameters is
$$
\boxed{\mathbb R}.
$$

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} exhibit, for every real $p$, a solution with infinitely
many critical points. There are no other real parameter values to
consider.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the requested classification of the real parameters.

:::

:::

:::
