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
<1>1. The general solution of the homogeneous equation
$$
y''-2y'+y=0
$$
is
$$
y_h(x)=(a+bx)e^x.
$$

::: {.proof}
The characteristic polynomial is
$$
r^2-2r+1=(r-1)^2,
$$
so the repeated root $r=1$ gives the displayed homogeneous solution.
:::

<1>2. A particular solution of
$$
y''-2y'+y=e^{-x}
$$
is
$$
y_p(x)=\frac14e^{-x}.
$$

::: {.proof}
For $y_p=ce^{-x}$,
$$
y_p''-2y_p'+y_p
=ce^{-x}+2ce^{-x}+ce^{-x}
=4ce^{-x}.
$$
Taking $c=1/4$ gives the forcing term $e^{-x}$.
:::

<1>3. Hence every solution has the form
$$
y(x)=\frac14e^{-x}+ae^x+bxe^x.
$$

::: {.proof}
This is the sum of the homogeneous solution from step <1>1 and the
particular solution from step <1>2.
:::

<1>4. The condition $y(0)=0$ gives
$$
a=-\frac14.
$$

::: {.proof}
Substituting $x=0$ into step <1>3 gives
$$
0=y(0)=\frac14+a.
$$
:::

<1>5. The condition $y'(0)=0$ then gives
$$
b=\frac12.
$$

::: {.proof}
Differentiating step <1>3,
$$
y'(x)
=-\frac14e^{-x}+ae^x+b(1+x)e^x.
$$
Thus, using $a=-1/4$ from step <1>4,
$$
0=y'(0)=-\frac14-\frac14+b,
$$
so $b=1/2$.
:::

<1>6. The required solution is
$$
\boxed{
y(x)=\frac14e^{-x}-\frac14e^x+\frac12xe^x.
}
$$

::: {.proof}
Substitute the constants from steps <1>4--<1>5 into the general
solution in step <1>3.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the unique solution satisfying the differential equation
and both initial conditions.
:::
:::
