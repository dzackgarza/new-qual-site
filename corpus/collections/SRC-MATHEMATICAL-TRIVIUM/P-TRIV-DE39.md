---
schema: qual/card@1
id: P-TRIV-DE39
kind: problem
title: First-order PDE $f_x+af_y+(x-2y)f=0$ by characteristics
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 39, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the most general solution of ${ \frac { \partial f } { \partial x } } + a { \frac { \partial f } { \partial y } } + ( x - 2 y ) f = 0$
:::

::: {.solution}
<1>1. The characteristic curves satisfy
\[
\frac{dy}{dx}=a,
\]
so
\[
\eta=y-ax
\]
is constant along each characteristic.

::: {.proof}
The transport part of the PDE is $f_x+af_y$, whose characteristic equations are $dx/ds=1$ and $dy/ds=a$. Dividing gives $dy/dx=a$, hence $y-ax$ is constant.
:::

<1>2. Along a characteristic $y=ax+\eta$, the function $F(x)=f(x,ax+\eta)$ satisfies
\[
F'(x)+\bigl((1-2a)x-2\eta\bigr)F(x)=0.
\]

::: {.proof}
By the chain rule,
\[
F'(x)=f_x(x,ax+\eta)+a f_y(x,ax+\eta).
\]
Substitute $y=ax+\eta$ into $x-2y$ in the PDE to obtain
\[
x-2(ax+\eta)=(1-2a)x-2\eta.
\]
:::

<1>3. Therefore
\[
F(x)=C(\eta)\exp\left(-\frac{1-2a}{2}x^2+2\eta x\right),
\]
where $C$ is an arbitrary function.

::: {.proof}
Step <1>2 is separable:
\[
\frac{F'}F=-((1-2a)x-2\eta).
\]
Integrating in $x$ gives
\[
\log F=-\frac{1-2a}{2}x^2+2\eta x+\log C(\eta).
\]
:::

<1>4. Substituting $\eta=y-ax$ into step <1>3 gives
\[
F(x)=C(y-ax)\exp\left(2xy-\left(a+\frac12\right)x^2\right).
\]

::: {.proof}
The exponent in step <1>3 becomes
\[
-\frac{1-2a}{2}x^2+2x(y-ax)
\;=
-\frac{x^2}{2}-ax^2+2xy.
\]
:::

<1>5. Hence, after simplification,
\[
\boxed{
f(x,y)=\Phi(y-ax)
\exp\left(2xy-\left(a+\frac12\right)x^2\right)}.
\]

::: {.proof}
Rename the arbitrary function $C$ in step <1>4 as $\Phi$. Every characteristic is labeled by $y-ax$, and $\Phi$ assigns its integration constant, so the family contains the general characteristic solution.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the most general solution.
:::
:::
