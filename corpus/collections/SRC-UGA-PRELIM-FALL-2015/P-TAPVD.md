---
schema: qual/card@1
id: P-TAPVD
kind: problem
title: Directional derivatives exist and equal $\nabla f\cdot\mathbf{u}$ when the
  first partials are continuous
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-reviewed
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced two overlapping solutions with one structured proof.
---

::: problem
Suppose $f:\mathbb R^2\to\mathbb R$ has continuous partial derivatives at $(0,0)$. Prove that $f$ has directional derivatives in every direction at the origin.
:::

::: {.solution}
Continuity of $f_x$ and $f_y$ at $(0,0)$ presupposes that both partial derivatives exist on some open disc $B$ about $(0,0)$.
Fix a direction $\mathbf u=(u_1,u_2)\in\mathbb R^2$.

<1>1. For every sufficiently small $h\neq0$ there are points $\xi_h$ between $0$ and $hu_1$ and $\eta_h$ between $0$ and $hu_2$ such that
\[
f(hu_1,hu_2)-f(0,0)=f_x(\xi_h,hu_2)\,hu_1+f_y(0,\eta_h)\,hu_2.
\]
::: {.proof}
Choose $h$ so small that the segments from $(0,hu_2)$ to $(hu_1,hu_2)$ and from $(0,0)$ to $(0,hu_2)$ lie in $B$, and split
\[
f(hu_1,hu_2)-f(0,0)=\bigl[f(hu_1,hu_2)-f(0,hu_2)\bigr]+\bigl[f(0,hu_2)-f(0,0)\bigr].
\]
The function $s\mapsto f(s,hu_2)$ is differentiable on the first segment with derivative $f_x(s,hu_2)$, so the mean value theorem gives $\xi_h$ with the first bracket equal to $f_x(\xi_h,hu_2)\,hu_1$; if $u_1=0$ the bracket is $0$ and any $\xi_h$ works.
The same argument applied to $t\mapsto f(0,t)$ gives $\eta_h$ for the second bracket.
:::

<1>2. $D_{\mathbf u}f(0,0)$ exists and equals $f_x(0,0)u_1+f_y(0,0)u_2$.
::: {.proof}
Dividing <1>1 by $h$,
\[
\frac{f(hu_1,hu_2)-f(0,0)}{h}=f_x(\xi_h,hu_2)\,u_1+f_y(0,\eta_h)\,u_2.
\]
As $h\to0$, the points $(\xi_h,hu_2)$ and $(0,\eta_h)$ tend to $(0,0)$ because $|\xi_h|\le|hu_1|$ and $|\eta_h|\le|hu_2|$.
Continuity of $f_x$ and $f_y$ at $(0,0)$ makes the right side tend to $f_x(0,0)u_1+f_y(0,0)u_2$, so the difference quotient has this limit.
:::

<1>3. Q.E.D.
::: {.proof}
The direction $\mathbf u$ was arbitrary, so by <1>2 every directional derivative of $f$ at the origin exists, with $D_{\mathbf u}f(0,0)=\nabla f(0,0)\cdot\mathbf u$.
:::
:::
