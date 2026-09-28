---
schema: qual/card@1
id: P-BKS81-4
kind: problem
title: Global dynamics approaching the unit circle
classification:
  areas: [prelim]
  topics: []
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
---

::: {.problem}
Consider
\[
\frac{dx}{dt}=y+x(1-x^2-y^2),
\qquad
\frac{dy}{dt}=-x+y(1-x^2-y^2).
\]

1. Show that for every initial condition $(x(0),y(0))=(x_0,y_0)$ there is a unique solution defined for all $t\in\mathbb R$.
2. Show that if $x_0\ne0$ and $y_0\ne0$, then the solution approaches the circle $x^2+y^2=1$ as $t\to\infty$.
:::

::: {.solution}
Put
$$
s(t)\coloneqq x(t)^2+y(t)^2,
\qquad
s_0\coloneqq x_0^2+y_0^2.
$$

<1>1. Every solution satisfies
$$
s'(t)=2s(t)(1-s(t)).
$$

::: {.proof}
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

<1>2. Part (1) is false as printed.

::: {.proof}
Take
$$
(x_0,y_0)=(2,0),
\qquad
s_0=4.
$$
The scalar equation in step <1>1 with this initial value has the solution
$$
s(t)=\frac{4}{4-3e^{-2t}}.
$$
Its denominator vanishes at
$$
t_*
=
\frac12\log\frac34
<0,
$$
and
$$
s(t)\longrightarrow+\infty
\qquad
\text{as }t\downarrow t_*.
$$
Any solution of the original system must have its squared radius satisfy
step <1>1, so no solution with this initial condition can extend to all
$t\in\RR$.
:::

<1>3. The corrected forward-time assertion is true: for every initial
condition there is a unique solution defined for all $t\ge0$.

::: {.proof}
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

<1>4. If $s_0>0$, then
$$
\lim_{t\to\infty}s(t)=1.
$$

::: {.proof}
The solution constructed in step <1>3 has
$$
s(t)=r(t)^2
=
\frac{s_0}{s_0+(1-s_0)e^{-2t}}.
$$
Since $e^{-2t}\to0$, the denominator tends to $s_0$, and the displayed
quotient tends to $1$.
:::

<1>5. Under the hypothesis of Part (2), the solution approaches the unit
circle:
$$
\boxed{
\operatorname{dist}\bigl((x(t),y(t)),\{x^2+y^2=1\}\bigr)\longrightarrow0
}.
$$

::: {.proof}
The assumptions $x_0\ne0$ and $y_0\ne0$ imply $s_0>0$. By step <1>4,
$$
\sqrt{x(t)^2+y(t)^2}
=
\sqrt{s(t)}
\longrightarrow1.
$$
The Euclidean distance from a point of radius $r$ to the unit circle is
$\abs{r-1}$, so the asserted distance tends to zero.
:::

<1>6. Thus Part (1) is false as stated, while its forward-time correction
and Part (2) are true.

::: {.proof}
Step <1>2 gives the counterexample to the printed Part (1), step <1>3 proves
the corrected forward-time assertion, and step <1>5 proves Part (2).
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 settles both printed requests, including the necessary correction
to the first.
:::
:::

::: {.remark}
Part (1) is false as printed. Replacing "defined for all $t\in\mathbb R$"
by "defined for all $t\ge0$" makes it correct for every initial condition.
The original two-sided statement is correct exactly for initial conditions
satisfying $x_0^2+y_0^2\le1$; when $x_0^2+y_0^2>1$, the radial solution
blows up at a finite negative time.
:::
