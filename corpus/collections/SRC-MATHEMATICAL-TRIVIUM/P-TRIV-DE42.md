---
schema: qual/card@1
id: P-TRIV-DE42
kind: problem
title: Boundary value problem for $u_{xx}+2u_{xy}+u_{yy}=0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 42, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $\partial _ { x } ^ { 2 } u + 2 \partial _ { x } \partial _ { y } u + \partial _ { y } ^ { 2 } u = 0$ with the boundary conditions $u ( x , 0 ) = \sin { x }$ and $u ( 0 , y ) = y ^ { 2 }$
:::

Introduce
\[
s=x+y,
\qquad
t=x-y,
\qquad
U(s,t)=u(x,y).
\]

::: pf

::: pf-step

The differential operator becomes
\[
(\partial_x+\partial_y)^2=4\partial_s^2,
\]
so the PDE is
\[
U_{ss}=0.
\]


::: pf-proof

Since $s_x=s_y=1$, $t_x=1$, and $t_y=-1$,
\[
\partial_x=\partial_s+\partial_t,
\qquad
\partial_y=\partial_s-\partial_t.
\]
Thus $\partial_x+\partial_y=2\partial_s$, and the given operator is its square.

:::

:::

::: pf-step

The general solution of the PDE is
\[
U(s,t)=sA(t)+B(t),
\]
or
\[
u(x,y)=(x+y)A(x-y)+B(x-y).
\]


::: pf-proof

For each fixed $t$, step <1>1 is the ordinary equation $U_{ss}=0$. Integrating twice in $s$ gives an affine function of $s$, whose two coefficients may be arbitrary functions of $t$.

:::

:::

::: pf-step

The boundary condition $u(x,0)=\sin x$ gives
\[
xA(x)+B(x)=\sin x.
\]


::: pf-proof

Set $y=0$ in step <1>2, so $s=t=x$.

:::

:::

::: pf-step

The boundary condition $u(0,y)=y^2$ gives
\[
yA(-y)+B(-y)=y^2,
\]
equivalently
\[
-tA(t)+B(t)=t^2.
\]


::: pf-proof

Set $x=0$, so $s=y$ and $t=-y$, and then rename $t=-y$.

:::

:::

::: pf-step

Solving steps <1>3--<1>4 gives, for $t\ne0$,
\[
A(t)=\frac{\sin t-t^2}{2t},
\qquad
B(t)=\frac{\sin t+t^2}{2}.
\]


::: pf-proof

Subtract the equation in step <1>4 from that in step <1>3:
\[
2tA(t)=\sin t-t^2.
\]
Adding them gives $2B(t)=\sin t+t^2$. Both expressions extend continuously to $t=0$, with $A(0)=1/2$ and $B(0)=0$.

:::

:::

::: pf-step

Hence the solution is
\[
\boxed{
u(x,y)=
(x+y)\frac{\sin(x-y)-(x-y)^2}{2(x-y)}
+\frac{\sin(x-y)+(x-y)^2}{2}},
\]
with the quotient interpreted by its continuous value $1/2$ when $x=y$.


::: pf-proof

Substitute the functions from step <1>5 into step <1>2. Steps <1>3--<1>4 show that the two boundary conditions hold, while step <1>2 ensures the PDE holds.

:::

:::

::: pf-qed

Step <1>6 gives the required solution, including its continuous extension across $x=y$.

:::

:::
