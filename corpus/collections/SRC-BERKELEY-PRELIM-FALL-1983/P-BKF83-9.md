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
<1>1. For every real value of $p$, the constant function
$$
y(x)\equiv3
$$
is a solution of the differential equation.

::: {.proof}
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

<1>2. This solution has infinitely many critical points.

::: {.proof}
A critical point of a differentiable real-valued function is a point where
its derivative vanishes. For the solution in step <1>1,
$$
y'(x)=0
$$
for every $x\in\mathbb R$. Thus every real number is a critical point.
:::

<1>3. The required set of parameters is
$$
\boxed{\mathbb R}.
$$

::: {.proof}
Steps <1>1 and <1>2 exhibit, for every real $p$, a solution with infinitely
many critical points. There are no other real parameter values to
consider.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the requested classification of the real parameters.
:::
:::
