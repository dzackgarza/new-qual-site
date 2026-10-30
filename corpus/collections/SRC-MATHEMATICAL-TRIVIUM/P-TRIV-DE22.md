---
schema: qual/card@1
id: P-TRIV-DE22
kind: problem
title: Reduction of order for $y''+P y'+Qy=0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 22, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the equation
$$
y''(x) + P(x)y'(x) + Q(x)y(x) = 0 \tag{35}
$$
and show that if $y_1$ is a solution to this equation, then also $y_2 = y_1 \int^x ds\, \frac{e^{-\int^s dt\, P(t)}}{[y_1(s)]^2}$ is.
:::

::: {.solution}

Work on an interval on which $y_1$ does not vanish, and define
$$
v(x)=\int^x\frac{e^{-\int^sP(t)\,dt}}{y_1(s)^2}\,ds,
\qquad y_2=y_1v.
$$

::: pf

::: {.pf-step #s1-1}

Substitution of $y_2=y_1v$ into the differential operator gives
$$
y_2''+Py_2'+Qy_2
=y_1v''+(2y_1'+Py_1)v'.
$$


::: pf-proof

Differentiate to obtain
$$
y_2'=y_1'v+y_1v',
\qquad
y_2''=y_1''v+2y_1'v'+y_1v''.
$$
Therefore
$$
y_2''+Py_2'+Qy_2
=v(y_1''+Py_1'+Qy_1)+y_1v''+(2y_1'+Py_1)v'.
$$
The first term vanishes because $y_1$ is a solution.

:::

:::

::: {.pf-step #s1-2}

The derivative of $v$ satisfies
$$
v'(x)=\frac{e^{-\int^xP(t)\,dt}}{y_1(x)^2}
$$
and
$$
v''=-\left(P+2\frac{y_1'}{y_1}\right)v'.
$$


::: pf-proof

The first identity is the fundamental theorem of calculus. Taking the logarithmic derivative of $v'$ gives
$$
\frac{v''}{v'}=-P-2\frac{y_1'}{y_1},
$$
which is the second identity.

:::

:::

::: {.pf-step #s1-3}

The function
$$
\boxed{y_2(x)=y_1(x)\int^x ds\,
\frac{e^{-\int^sP(t)\,dt}}{y_1(s)^2}}
$$
solves $y''+Py'+Qy=0$.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
y_1v''+(2y_1'+Py_1)v'
=y_1\left[-P-2\frac{y_1'}{y_1}\right]v'
+(2y_1'+Py_1)v'=0.
$$
Step [](#s1-1){.pf-ref} therefore gives $y_2''+Py_2'+Qy_2=0$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves the asserted reduction-of-order formula on every interval where its integrand is defined.

:::

:::

:::
