---
schema: qual/card@1
id: P-BKF78-6
kind: problem
title: Solve a first-order linear differential equation
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 of the deterministic MinerU Flash extraction of the Berkeley Fall 1978 preliminary exam.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Multiplying y-3 by e^{-x^3/3} gives a quantity with zero derivative.
    The initial condition makes that constant -2, yielding
    y(x)=3-2e^{x^3/3}; direct differentiation verifies the solution.
---

::: {.problem}
Solve the differential equation
\[
\frac{dy}{dx}=x^2y-3x^2,
\qquad
y(0)=1.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #derivative-zero}
Every solution satisfies
$$
\frac{d}{dx}
\left(
e^{-x^3/3}(y-3)
\right)
=
0.
$$

::: pf-proof
By the product rule and the differential equation,
$$
\begin{aligned}
\frac{d}{dx}
\left(
e^{-x^3/3}(y-3)
\right)
&=
e^{-x^3/3}
\left(
y'-x^2(y-3)
\right)\\
&=
e^{-x^3/3}
\left(
x^2y-3x^2-x^2y+3x^2
\right)\\
&=
0.
\end{aligned}
$$
:::

:::

::: {.pf-step #initial-condition-value}
The initial condition forces
$$
e^{-x^3/3}(y-3)=-2.
$$

::: pf-proof
By step [](#derivative-zero){.pf-ref}, the left-hand side is constant. At $x=0$ it equals
$$
e^0(y(0)-3)=1-3=-2.
$$
:::

:::

::: {.pf-step #solution-formula}
The solution is
$$
\boxed{
y(x)=3-2e^{x^3/3}
}.
$$

::: pf-proof
Solving the identity in step [](#initial-condition-value){.pf-ref} for $y$ gives the displayed
formula.
:::

:::

::: {.pf-step #solution-verifies}
The function in step [](#solution-formula){.pf-ref} satisfies both the differential
equation and the initial condition.

::: pf-proof
For
$$
y(x)=3-2e^{x^3/3},
$$
we have
$$
y'(x)=-2x^2e^{x^3/3}.
$$
Also
$$
x^2y-3x^2
=
x^2\left(3-2e^{x^3/3}\right)-3x^2
=
-2x^2e^{x^3/3}
=
y'(x),
$$
and
$$
y(0)=3-2=1.
$$
:::

:::

::: pf-qed
Steps [](#derivative-zero){.pf-ref}, [](#initial-condition-value){.pf-ref} and [](#solution-formula){.pf-ref} show that any solution must be the function in step
[](#solution-formula){.pf-ref}, and step [](#solution-verifies){.pf-ref} verifies that this function is indeed a solution.
:::

:::
:::
