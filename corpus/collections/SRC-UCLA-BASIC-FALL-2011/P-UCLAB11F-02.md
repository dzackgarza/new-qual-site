---
schema: qual/card@1
id: P-UCLAB11F-02
kind: problem
title: Strong monotonicity of the gradient implies convexity
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Fall 2011.
---

::: {.problem}
Problem 2. A function $f:\mathbb R^n\to\mathbb R$ is called convex if
\[
f(\alpha x+(1-\alpha)y)\le \alpha f(x)+(1-\alpha)f(y)
\]
for all $x,y\in\mathbb R^n$ and $0\le\alpha\le1$.

Assume that $f$ is continuously differentiable and that for some constant $c>0$,
\[
(\nabla f(x)-\nabla f(y))\cdot(x-y)\ge c\,(x-y)\cdot(x-y)
\]
for all $x,y\in\mathbb R^n$.
Show that $f$ is convex.
:::

Fix $x,y\in\mathbb R^n$ and define
\[
v=x-y,
\qquad
g(t)=f(y+tv),
\qquad
0\le t\le1.
\]

::: pf

::: pf-step

The derivative of $g$ is
\[
g'(t)=\nabla f(y+tv)\cdot v.
\]


::: pf-proof

This follows from the chain rule, since $f$ is continuously differentiable and the path $t\mapsto y+tv$ has derivative $v$.

:::

:::

::: pf-step

For $0\le s<t\le1$,
\[
g'(t)-g'(s)
\ge
c(t-s)\|v\|^2
\ge0.
\]


::: pf-proof

By step <1>1,
\[
\begin{aligned}
g'(t)-g'(s)
&=
\bigl(\nabla f(y+tv)-\nabla f(y+sv)\bigr)\cdot v.
\end{aligned}
\]
Apply the hypothesis to
\[
x_t=y+tv,
\qquad
x_s=y+sv.
\]
Since
\[
x_t-x_s=(t-s)v,
\]
the hypothesis gives
\[
\bigl(\nabla f(x_t)-\nabla f(x_s)\bigr)\cdot((t-s)v)
\ge
c(t-s)^2\|v\|^2.
\]
Divide by the positive number $t-s$ to obtain the displayed inequality.

:::

:::

::: pf-step

The function $g'$ is nondecreasing on $[0,1]$.


::: pf-proof

This is the second inequality in step <1>2.

:::

:::

::: pf-step

For every $0\le\alpha\le1$,
\[
g(\alpha)
\le
(1-\alpha)g(0)+\alpha g(1).
\]


::: pf-proof

For $0<\alpha<1$, the fundamental theorem of calculus gives
\[
g(\alpha)-g(0)
=
\int_0^\alpha g'(t)\,dt
\]
and
\[
g(1)-g(\alpha)
=
\int_\alpha^1g'(t)\,dt.
\]
Because $g'$ is nondecreasing by step <1>3,
\[
\frac1\alpha\int_0^\alpha g'(t)\,dt
\le
\frac1{1-\alpha}\int_\alpha^1g'(t)\,dt.
\]
Multiplying by $\alpha(1-\alpha)$ gives
\[
(1-\alpha)(g(\alpha)-g(0))
\le
\alpha(g(1)-g(\alpha)).
\]
Rearranging yields
\[
g(\alpha)
\le
(1-\alpha)g(0)+\alpha g(1).
\]
The cases $\alpha=0,1$ are equalities.

:::

:::

::: pf-step

One has
\[
f(\alpha x+(1-\alpha)y)
\le
\alpha f(x)+(1-\alpha)f(y)
\]
for all $x,y\in\mathbb R^n$ and $0\le\alpha\le1$.


::: pf-proof

By definition,
\[
g(0)=f(y),
\qquad
g(1)=f(x),
\]
and
\[
g(\alpha)
=
f(y+\alpha(x-y))
=
f(\alpha x+(1-\alpha)y).
\]
Substitute these identities into step <1>4.

:::

:::

::: pf-step

Therefore
\[
\boxed{f\text{ is convex}}.
\]


::: pf-proof

Step <1>5 is exactly the defining convexity inequality.

:::

:::

::: pf-qed

Step <1>6 is the required conclusion.

:::

:::
