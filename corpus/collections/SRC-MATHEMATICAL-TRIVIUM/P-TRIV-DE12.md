---
schema: qual/card@1
id: P-TRIV-DE12
kind: problem
title: Initial value problem $y'-y=e^{3t}$, $y(0)=2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 12, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $y ^ { \prime } - y = e ^ { 3 t }$ with $y ( 0 ) = 2$
:::

::: pf

::: pf-step

The equation
$$
y'-y=e^{3t}
$$
is first-order linear with integrating factor
$$
\mu(t)=e^{-t}.
$$


::: pf-proof

For an equation $y'+p(t)y=q(t)$, an integrating factor is
$$
e^{\int p(t)dt}.
$$
Here $p(t)=-1$.

:::

:::

::: pf-step

Multiplying by $e^{-t}$ gives
$$
\frac d{dt}
\left(
e^{-t}y
\right)
=
e^{2t}.
$$


::: pf-proof

The left-hand side expands as
$$
e^{-t}y'-e^{-t}y,
$$
and the right-hand side is $e^{-t}e^{3t}$.

:::

:::

::: pf-step

Integrating gives
$$
e^{-t}y
=
\frac12e^{2t}
+
C.
$$


::: pf-proof

An antiderivative of $e^{2t}$ is $e^{2t}/2$.

:::

:::

::: pf-step

Hence
$$
y(t)
=
\frac12e^{3t}
+
Ce^t.
$$


::: pf-proof

Multiply step <1>3 by $e^t$.

:::

:::

::: pf-step

The initial condition $y(0)=2$ gives
$$
C=\frac32.
$$


::: pf-proof

Substitute $t=0$ into step <1>4:
$$
2
=
\frac12
+
C.
$$

:::

:::

::: pf-step

Therefore
$$
\boxed{
y(t)
=
\frac12e^{3t}
+
\frac32e^t.
}
$$


::: pf-proof

Substitute step <1>5 into step <1>4.

:::

:::

::: pf-qed

Step <1>6 satisfies both the differential equation and the initial condition.

:::

:::
