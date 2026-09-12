---
schema: qual/card@1
id: P-BKF77-8
kind: problem
title: Second-order ODE with initial conditions
classification:
  areas:
  - prelim
  topics:
  - Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Solved the repeated-root homogeneous equation, found a trigonometric particular solution, and imposed both initial conditions."
---

::: problem
Find all solutions of
\[
x''-2x'+x=\sin t
\]
subject to $x(0)=1$ and $x'(0)=0$.
:::

::: solution
<1>1. Solve the homogeneous equation.
::: proof
The characteristic polynomial of
$$
x''-2x'+x=0
$$
is
$$
r^2-2r+1=(r-1)^2.
$$
Thus the homogeneous solutions are
$$
x_h(t)=(C_1+C_2t)e^t.
$$
:::

<1>2. Find a particular solution.
::: proof
Try
$$
x_p(t)=a\sin t+b\cos t.
$$
Then
$$
x_p'(t)=a\cos t-b\sin t,
$$
and
$$
x_p''(t)=-a\sin t-b\cos t.
$$
Therefore
$$
x_p''-2x_p'+x_p
=2b\sin t-2a\cos t.
$$
To make this equal to $\sin t$, take
$$
a=0,
\qquad
b=\frac12.
$$
Hence one particular solution is
$$
x_p(t)=\frac12\cos t.
$$
:::

<1>3. Impose the initial conditions.
::: proof
The general solution is
$$
x(t)=(C_1+C_2t)e^t+\frac12\cos t.
$$
The condition $x(0)=1$ gives
$$
C_1+\frac12=1,
$$
so
$$
C_1=\frac12.
$$

Differentiating,
$$
x'(t)=(C_1+C_2+C_2t)e^t-\frac12\sin t.
$$
Thus $x'(0)=0$ gives
$$
C_1+C_2=0,
$$
so
$$
C_2=-\frac12.
$$
Consequently the unique solution satisfying the two initial conditions is
$$
\boxed{
x(t)=\frac{(1-t)e^t+\cos t}{2}.}
$$
:::
:::
