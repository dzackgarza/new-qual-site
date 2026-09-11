---
schema: qual/card@1
id: P-BKF77-6
kind: problem
title: Harmonic conjugate of $x^3-3xy^2$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
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
  note: "Verified harmonicity directly and integrated the Cauchy--Riemann equations to obtain the harmonic conjugate."
---

::: problem
Let $u:\mathbb R^2\to\mathbb R$ be defined by
\[
u(x,y)=x^3-3xy^2.
\]
Show that $u$ is harmonic and find $v:\mathbb R^2\to\mathbb R$ such that
\[
f(x+iy)=u(x,y)+iv(x,y)
\]
is analytic.
:::

::: solution
<1>1. Verify that $u$ is harmonic.
::: proof
We have
$$
u_x=3x^2-3y^2,
\qquad
u_y=-6xy.
$$
Therefore
$$
u_{xx}=6x,
\qquad
u_{yy}=-6x.
$$
Hence
$$
u_{xx}+u_{yy}=0
$$
everywhere on $\mathbb R^2$, so $u$ is harmonic.
:::

<1>2. Solve the Cauchy--Riemann equations for $v$.
::: proof
For
$$
f=u+iv
$$
to be analytic, the Cauchy--Riemann equations require
$$
v_y=u_x=3x^2-3y^2,
$$
and
$$
v_x=-u_y=6xy.
$$
Integrating the first equation with respect to $y$ gives
$$
v(x,y)=3x^2y-y^3+\phi(x)
$$
for some differentiable function $\phi$. Differentiating with respect to $x$,
$$
v_x=6xy+\phi'(x).
$$
Comparing with the second Cauchy--Riemann equation yields
$$
\phi'(x)=0.
$$
Thus $\phi$ is constant, and all harmonic conjugates are
$$
\boxed{v(x,y)=3x^2y-y^3+C.}
$$
:::

<1>3. Identify the analytic function.
::: proof
Since
$$
(x+iy)^3
=x^3-3xy^2+i(3x^2y-y^3),
$$
the resulting analytic function is
$$
\boxed{f(z)=z^3+iC,\qquad C\in\mathbb R.}
$$
:::
:::
