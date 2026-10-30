---
schema: qual/card@1
id: P-BKS77-9
kind: problem
title: Initial value problem $y''-2y'+y=0$, $y(0)=y'(0)=1$
classification: {areas: [prelim], topics: [Calculus]}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Solve
$$
y''-2y'+y=0
$$
subject to
$$
y(0)=1,
\qquad
y'(0)=1.
$$
:::

::: {.solution}
::: pf

::: pf-step
The characteristic polynomial of the differential equation is
$$
r^2-2r+1=(r-1)^2.
$$

::: pf-proof
Substituting a trial solution $y=e^{rx}$ gives
$$
(r^2-2r+1)e^{rx}=0.
$$
Since $e^{rx}\neq0$, the characteristic equation is the displayed polynomial equation.
:::

:::

::: {.pf-step #general-solution}
Every solution has the form
$$
y(x)=(C_1+C_2x)e^x.
$$

::: pf-proof
The characteristic root $r=1$ has multiplicity $2$. For a repeated root of multiplicity $2$, the two linearly independent solutions are
$$
e^x
\qquad\text{and}\qquad
xe^x.
$$
Their linear combinations give the displayed general solution.
:::

:::

::: {.pf-step #first-constant}
The condition $y(0)=1$ forces
$$
C_1=1.
$$

::: pf-proof
From [](#general-solution){.pf-ref},
$$
y(0)=C_1.
$$
Apply the initial condition.
:::

:::

::: {.pf-step #second-constant}
The condition $y'(0)=1$ forces
$$
C_2=0.
$$

::: pf-proof
Differentiating [](#general-solution){.pf-ref} gives
$$
y'(x)
=
(C_1+C_2x+C_2)e^x.
$$
Hence
$$
y'(0)=C_1+C_2.
$$
By [](#first-constant){.pf-ref} and the initial condition,
$$
1+C_2=1,
$$
so $C_2=0$.
:::

:::

::: pf-step
The unique solution is
$$
\boxed{y(x)=e^x}.
$$

::: pf-proof
Substitute the constants from [](#first-constant){.pf-ref} and [](#second-constant){.pf-ref} into the general solution from [](#general-solution){.pf-ref}.
:::

:::

:::

:::
