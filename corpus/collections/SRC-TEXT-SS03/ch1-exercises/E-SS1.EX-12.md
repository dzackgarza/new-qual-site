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
<1>1. Write $f=u+iv$, where
\[
u(x,y)=\sqrt{|x||y|},
\qquad
v(x,y)=0.
\]
::: {.proof}
The function $f$ is real-valued, so its imaginary part is identically zero.
:::

<1>2. All four first partial derivatives $u_x(0,0)$, $u_y(0,0)$, $v_x(0,0)$, and $v_y(0,0)$ are zero.
::: {.proof}
Because $u(h,0)=u(0,h)=0$ for every real $h$, one has
\[
u_x(0,0)=\lim_{h\to0}\frac{u(h,0)-u(0,0)}h=0,
\]
and similarly $u_y(0,0)=0$. Since $v\equiv0$, also $v_x(0,0)=v_y(0,0)=0$.
:::

<1>3. Hence the Cauchy-Riemann equations hold at the origin.
::: {.proof}
At $(0,0)$,
\[
u_x=v_y=0,
\qquad
u_y=-v_x=0,
\]
by <1>2.
:::

<1>4. Along the real axis, the difference quotient of $f$ at $0$ is zero.
::: {.proof}
For real $t\ne0$,
\[
\frac{f(t)-f(0)}t=\frac{0}{t}=0,
\]
because $f(t)=u(t,0)=0$.
:::

<1>5. Along the line $z=t(1+i)$ with $t>0$, the difference quotient is $1/(1+i)$.
::: {.proof}
For $t>0$,
\[
f(t+it)=\sqrt{|t||t|}=t,
\]
so
\[
\frac{f(t(1+i))-f(0)}{t(1+i)}=\frac1{1+i}.
\]
:::

<1>6. Therefore $f$ is not complex differentiable at $0$, and hence is not holomorphic at $0$.
::: {.proof}
The limits in <1>4 and <1>5 approach different values as $t\to0^+$, so the complex difference quotient has no limit at the origin.
:::
:::
