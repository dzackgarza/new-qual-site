---
schema: qual/card@1
id: P-BKF92-4
kind: problem
title: The solution of $y''=-|y|$ with $y(0)=1,y'(0)=0$ has exactly one positive zero
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Constructed the unique solution explicitly as cos t up to pi/2 and
    -sinh(t-pi/2) thereafter, using uniqueness for the globally Lipschitz ODE.
---

::: {.problem}
Let $y:[0,\infty)\to\mathbb R$ solve
\[
y''=-|y|,
\qquad
y(0)=1,
\qquad
y'(0)=0.
\]
Prove that there is exactly one $t>0$ such that $y(t)=0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The initial-value problem has a unique solution on $[0,\infty)$.

::: pf-proof

Write the second-order equation as the first-order system
$$
\begin{pmatrix}y\\v\end{pmatrix}'
=
\begin{pmatrix}v\\-\abs y\end{pmatrix}.
$$
The vector field
$$
(y,v)\longmapsto(v,-\abs y)
$$
is globally Lipschitz on $\RR^2$, since the absolute-value function is Lipschitz with constant $1$. The standard existence-and-uniqueness theorem therefore gives a unique global solution for the prescribed initial data.

:::

:::

::: pf-step

Define
$$
\widetilde y(t)
\coloneqq
\begin{cases}
\cos t,&0\le t\le\pi/2,\\
-\sinh(t-\pi/2),&t\ge\pi/2.
\end{cases}
$$
Then $\widetilde y$ is $C^2$ on $[0,\infty)$.

::: pf-proof

At $t=\pi/2$, both formulas give the value $0$. Their first derivatives are
$$
-\sin t
\qquad\text{and}\qquad
-\cosh(t-\pi/2),
$$
which both equal $-1$ at $t=\pi/2$. Their second derivatives are
$$
-\cos t
\qquad\text{and}\qquad
-\sinh(t-\pi/2),
$$
which both equal $0$ there. Thus the two pieces join with matching derivatives through order $2$.

:::

:::

::: {.pf-step #s3}

The function $\widetilde y$ satisfies
$$
\widetilde y''=-\abs{\widetilde y},
\qquad
\widetilde y(0)=1,
\qquad
\widetilde y'(0)=0.
$$

::: pf-proof

For $0\le t\le\pi/2$, one has $\widetilde y(t)=\cos t\ge0$, so
$$
\widetilde y''(t)=-\cos t=-\abs{\widetilde y(t)}.
$$
For $t\ge\pi/2$, one has
$$
\widetilde y(t)=-\sinh(t-\pi/2)\le0,
$$
so
$$
\widetilde y''(t)
=
-\sinh(t-\pi/2)
=
\widetilde y(t)
=
-\abs{\widetilde y(t)}.
$$
The initial conditions follow directly from the first formula.

:::

:::

::: {.pf-step #s4}

The given solution is $y=\widetilde y$.

::: pf-proof

Step [](#s3){.pf-ref} shows that $\widetilde y$ solves the same initial-value problem as $y$. By uniqueness from step [](#s1){.pf-ref}, they coincide.

:::

:::

::: {.pf-step #s5}

The equation $y(t)=0$ for $t>0$ has the unique solution
$$
\boxed{t=\pi/2}.
$$

::: pf-proof

By step [](#s4){.pf-ref}, for $0<t<\pi/2$ one has
$$
y(t)=\cos t>0,
$$
while $y(\pi/2)=0$. For $t>\pi/2$,
$$
y(t)=-\sinh(t-\pi/2)<0.
$$
Thus no other positive zero exists.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is exactly the assertion.

:::

:::

:::
