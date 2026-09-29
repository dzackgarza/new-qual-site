---
schema: qual/card@1
id: P-BKS12-5A
kind: problem
title: Initial value problem for the Euler equation $x^2y''+xy'+y=0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 2 of the retained Spring 2012 solution PDF and independently reviewed the Euler-equation solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the t=log x reduction, transformed initial conditions, and converse substitution.
---

::: {.problem}
Find the solution of the differential equation

$$
x ^ { 2 } { \frac { d ^ { 2 } y } { d x ^ { 2 } } } + x { \frac { d y } { d x } } + y = 0
$$

in $x > 0$ , such that $y ( 1 ) = 0$ and $\frac { d y } { d x } = 1$ at $x = 1$
:::

::: {.solution}
Set
$$
t\coloneqq\log x
$$
and define
$$
u(t)\coloneqq y(e^t).
$$

::: pf

::: {.pf-step #derivative-relations}
One has
$$
u'(t)=xy'(x)
$$
and
$$
u''(t)=x^2y''(x)+xy'(x),
$$
where $x=e^t$.

::: pf-proof
By the chain rule,
$$
u'(t)
=
y'(e^t)e^t
=
xy'(x).
$$
Differentiate once more:
$$
\begin{aligned}
u''(t)
&=
\frac{d}{dt}\bigl(xy'(x)\bigr)\\
&=
x\frac{d}{dx}\bigl(xy'(x)\bigr)\\
&=
x\bigl(y'(x)+xy''(x)\bigr)\\
&=
xy'(x)+x^2y''(x).
\end{aligned}
$$
:::

:::

::: {.pf-step #transformed-ode}
The differential equation is equivalent to
$$
u''(t)+u(t)=0.
$$

::: pf-proof
By step [](#derivative-relations){.pf-ref},
$$
x^2y''+xy'
=
u''.
$$
Also $y(x)=u(t)$. Substituting these identities into the given equation
gives the displayed constant-coefficient equation.
:::

:::

::: {.pf-step #transformed-initial-conditions}
The initial conditions become
$$
u(0)=0,
\qquad
u'(0)=1.
$$

::: pf-proof
The point $x=1$ corresponds to
$$
t=\log1=0.
$$
Therefore
$$
u(0)=y(1)=0.
$$
By step [](#derivative-relations){.pf-ref},
$$
u'(0)
=
1\cdot y'(1)
=
1.
$$
:::

:::

::: {.pf-step #u-solution}
The unique solution for $u$ is
$$
u(t)=\sin t.
$$

::: pf-proof
The general real solution of
$$
u''+u=0
$$
is
$$
u(t)=A\cos t+B\sin t.
$$
The conditions in step [](#transformed-initial-conditions){.pf-ref} give
$$
A=0,
\qquad
B=1.
$$
:::

:::

::: {.pf-step #y-solution}
The required solution is
$$
\boxed{
y(x)=\sin(\log x)
},
\qquad
x>0.
$$

::: pf-proof
Since $t=\log x$, step [](#u-solution){.pf-ref} gives
$$
y(x)=u(\log x)=\sin(\log x).
$$
The change of variables in steps [](#derivative-relations){.pf-ref} and [](#transformed-ode){.pf-ref} is reversible for $x>0$,
so this function satisfies the original differential equation and the
initial conditions.
:::

:::

::: pf-qed
Step [](#y-solution){.pf-ref} is the requested solution.
:::

:::

:::
