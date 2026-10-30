---
schema: qual/card@1
id: P-BKS81-4
kind: problem
title: Global dynamics approaching the unit circle
classification:
  areas: [prelim]
  topics:
  - Calculus
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
  note: >-
    Checked the radial logistic equation, the finite backward-time blow-up
    counterexample to Part 1, the explicit global forward solution, and the
    convergence of the radius to one.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Part 1 of the source asks for a unique solution defined for all real t, but for x_0^2+y_0^2>1 the radius blows up at a finite negative time. Part 1 now asks for a unique solution defined for all t >= 0.
---

::: {.problem}
Consider
$$
\frac{dx}{dt}=y+x(1-x^2-y^2),
\qquad
\frac{dy}{dt}=-x+y(1-x^2-y^2).
$$

(a) Show that for every initial condition $(x(0),y(0))=(x_0,y_0)$ there is a unique solution defined for all $t\geq 0$.

(b) Show that if $x_0\ne0$ and $y_0\ne0$, then the solution approaches the circle $x^2+y^2=1$ as $t\to\infty$.
:::

::: {.remark}
The exam asks in (a) for a solution defined for all real $t$. That fails backward in time: when $x_0^2+y_0^2>1$, the radius solves $r'=r(1-r^2)$ and blows up at a finite negative time. Part (a) therefore asks for $t\geq 0$.
:::

::: {.solution}
Put
$$
s(t)\coloneqq x(t)^2+y(t)^2,
\qquad
s_0\coloneqq x_0^2+y_0^2.
$$

::: pf

::: {.pf-step #radial-ode}
Every solution satisfies
$$
s'(t)=2s(t)(1-s(t)).
$$

::: pf-proof
Using the differential equations,
$$
\begin{aligned}
s'
&=2xx'+2yy'\\
&=2x\bigl(y+x(1-s)\bigr)
  +2y\bigl(-x+y(1-s)\bigr)\\
&=2(x^2+y^2)(1-s)\\
&=2s(1-s).
\end{aligned}
$$
:::

:::

::: {.pf-step #forward-solution-exists}
For every initial condition there is a unique solution defined for
all $t\ge0$. This is part (a).

::: pf-proof
The vector field is polynomial, hence locally Lipschitz, so the initial-value
problem has a unique local solution.

If $s_0=0$, then $(x,y)=(0,0)$ is the unique solution. Suppose $s_0>0$ and
choose $\theta_0\in\RR$ such that
$$
x_0=\sqrt{s_0}\cos\theta_0,
\qquad
y_0=\sqrt{s_0}\sin\theta_0.
$$
For $t\ge0$, put
$$
q(t)\coloneqq s_0+(1-s_0)e^{-2t},
\qquad
r(t)\coloneqq\sqrt{\frac{s_0}{q(t)}},
\qquad
\theta(t)\coloneqq\theta_0-t.
$$
If $0<s_0\le1$, then $q(t)>0$. If $s_0>1$, then
$$
q(t)
=
s_0-(s_0-1)e^{-2t}
\ge1.
$$
Thus these functions are defined for every $t\ge0$. A direct
differentiation gives
$$
r'=r(1-r^2),
\qquad
\theta'=-1.
$$
Consequently
$$
x(t)\coloneqq r(t)\cos\theta(t),
\qquad
y(t)\coloneqq r(t)\sin\theta(t)
$$
satisfy the given system and the prescribed initial condition for all
$t\ge0$. Local uniqueness makes this the unique forward solution.
:::

:::

::: {.pf-step #radius-limit-one}
If $s_0>0$, then
$$
\lim_{t\to\infty}s(t)=1.
$$

::: pf-proof
The solution constructed in step [](#forward-solution-exists){.pf-ref} has
$$
s(t)=r(t)^2
=
\frac{s_0}{s_0+(1-s_0)e^{-2t}}.
$$
Since $e^{-2t}\to0$, the denominator tends to $s_0$, and the displayed
quotient tends to $1$.
:::

:::

::: {.pf-step #approaches-unit-circle}
Under the hypothesis of part (b), the solution approaches the unit
circle:
$$
\boxed{
\operatorname{dist}\bigl((x(t),y(t)),\{x^2+y^2=1\}\bigr)\longrightarrow0
}.
$$

::: pf-proof
The assumptions $x_0\ne0$ and $y_0\ne0$ imply $s_0>0$. By step [](#radius-limit-one){.pf-ref},
$$
\sqrt{x(t)^2+y(t)^2}
=
\sqrt{s(t)}
\longrightarrow1.
$$
The Euclidean distance from a point of radius $r$ to the unit circle is
$\abs{r-1}$, so the asserted distance tends to zero.
:::

:::
:::
:::
