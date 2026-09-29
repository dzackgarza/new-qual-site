---
schema: qual/card@1
id: P-BKS08-4A
kind: problem
title: Initial value problem $y''-2y'+y=e^{-x}$, $y(0)=y'(0)=0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the homogeneous solution, a particular solution, and
    both initial-condition equations against the vendored solution.
---

::: {.problem}
Find the solution of
$$
y''-2y'+y=e^{-x}
$$
satisfying
$$
y(0)=y'(0)=0.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #homogeneous-solution}
The general solution of the homogeneous equation
$$
y''-2y'+y=0
$$
is
$$
y_h(x)=(a+bx)e^x.
$$

::: pf-proof
The characteristic polynomial is
$$
r^2-2r+1=(r-1)^2,
$$
so the repeated root $r=1$ gives the displayed homogeneous solution.
:::

:::

::: {.pf-step #particular-solution}
A particular solution of
$$
y''-2y'+y=e^{-x}
$$
is
$$
y_p(x)=\frac14e^{-x}.
$$

::: pf-proof
For $y_p=ce^{-x}$,
$$
y_p''-2y_p'+y_p
=ce^{-x}+2ce^{-x}+ce^{-x}
=4ce^{-x}.
$$
Taking $c=1/4$ gives the forcing term $e^{-x}$.
:::

:::

::: {.pf-step #general-solution-form}
Hence every solution has the form
$$
y(x)=\frac14e^{-x}+ae^x+bxe^x.
$$

::: pf-proof
This is the sum of the homogeneous solution from step [](#homogeneous-solution){.pf-ref} and the
particular solution from step [](#particular-solution){.pf-ref}.
:::

:::

::: {.pf-step #constant-a}
The condition $y(0)=0$ gives
$$
a=-\frac14.
$$

::: pf-proof
Substituting $x=0$ into step [](#general-solution-form){.pf-ref} gives
$$
0=y(0)=\frac14+a.
$$
:::

:::

::: {.pf-step #constant-b}
The condition $y'(0)=0$ then gives
$$
b=\frac12.
$$

::: pf-proof
Differentiating step [](#general-solution-form){.pf-ref},
$$
y'(x)
=-\frac14e^{-x}+ae^x+b(1+x)e^x.
$$
Thus, using $a=-1/4$ from step [](#constant-a){.pf-ref},
$$
0=y'(0)=-\frac14-\frac14+b,
$$
so $b=1/2$.
:::

:::

::: {.pf-step #final-solution}
The required solution is
$$
\boxed{
y(x)=\frac14e^{-x}-\frac14e^x+\frac12xe^x.
}
$$

::: pf-proof
Substitute the constants from steps [](#constant-a){.pf-ref} and [](#constant-b){.pf-ref} into the general
solution in step [](#general-solution-form){.pf-ref}.
:::

:::

::: pf-qed
Step [](#final-solution){.pf-ref} is the unique solution satisfying the differential equation
and both initial conditions.
:::

:::

:::
