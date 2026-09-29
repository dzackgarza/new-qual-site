---
schema: qual/card@1
id: E-SS1.EX-12
kind: problem
title: Cauchy-Riemann equations at one point do not imply complex differentiability
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.exercise}
Consider the function
\[
f(x+iy)=\sqrt{|x||y|},
\qquad x,y\in\mathbb R.
\]
Show that $f$ satisfies the Cauchy-Riemann equations at the origin, yet $f$ is not holomorphic at $0$.
:::

::: {.solution}

::: pf

::: pf-step

Write $f=u+iv$, where
\[
u(x,y)=\sqrt{|x||y|},
\qquad
v(x,y)=0.
\]

::: pf-proof

The function $f$ is real-valued, so its imaginary part is identically zero.

:::

:::

::: {.pf-step #s2}

All four first partial derivatives $u_x(0,0)$, $u_y(0,0)$, $v_x(0,0)$, and $v_y(0,0)$ are zero.

::: pf-proof

Because $u(h,0)=u(0,h)=0$ for every real $h$, one has
\[
u_x(0,0)=\lim_{h\to0}\frac{u(h,0)-u(0,0)}h=0,
\]
and similarly $u_y(0,0)=0$. Since $v\equiv0$, also $v_x(0,0)=v_y(0,0)=0$.

:::

:::

::: pf-step

Hence the Cauchy-Riemann equations hold at the origin.

::: pf-proof

At $(0,0)$,
\[
u_x=v_y=0,
\qquad
u_y=-v_x=0,
\]
by step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

Along the real axis, the difference quotient of $f$ at $0$ is zero.

::: pf-proof

For real $t\ne0$,
\[
\frac{f(t)-f(0)}t=\frac{0}{t}=0,
\]
because $f(t)=u(t,0)=0$.

:::

:::

::: {.pf-step #s5}

Along the line $z=t(1+i)$ with $t>0$, the difference quotient is $1/(1+i)$.

::: pf-proof

For $t>0$,
\[
f(t+it)=\sqrt{|t||t|}=t,
\]
so
\[
\frac{f(t(1+i))-f(0)}{t(1+i)}=\frac1{1+i}.
\]

:::

:::

::: pf-step

Therefore $f$ is not complex differentiable at $0$, and hence is not holomorphic at $0$.

::: pf-proof

The limits in steps [](#s4){.pf-ref} and [](#s5){.pf-ref} approach different values as $t\to0^+$, so the complex difference quotient has no limit at the origin.

:::

:::

:::

:::
