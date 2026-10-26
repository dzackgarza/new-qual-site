---
schema: qual/card@1
id: P-PRECALC2-19
kind: problem
title: First and second derivatives along a parametric curve
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Suppose that $( x ( t ) , y ( t ) )$ for $t \in [ a , b ]$ is the parameterization a curve and that $x ^ { \prime } ( t ) \neq 0$ for all $t \in [ a , b ]$ . Find $\textstyle { \frac { d y } { d x } }$ and $\textstyle { \frac { d ^ { 2 } y } { d x ^ { 2 } } }$ as functions of t.
:::

Assume
\[
x'(t)\ne0
\]
throughout the parameter interval.

::: pf

::: pf-step

By the chain rule,
\[
\boxed{
\frac{dy}{dt}
=
\frac{dy}{dx}\frac{dx}{dt}}.
\]


::: pf-proof

Locally, the condition \(x'(t)\ne0\) allows \(x\) to be used as a coordinate
along the curve. Thus
\[
y(t)=y(x(t)),
\]
and differentiating with respect to \(t\) gives the displayed identity.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\frac{dy}{dx}
=
\frac{y'(t)}{x'(t)}}.
\]


::: pf-proof

Solve step <1>1 for \(dy/dx\), using
\[
x'(t)\ne0.
\]

:::

:::

::: pf-step

Differentiation with respect to \(x\) along the curve is
\[
\boxed{
\frac{d}{dx}
=
\frac1{x'(t)}
\frac{d}{dt}}.
\]


::: pf-proof

For any differentiable quantity \(F(t)\),
\[
\frac{dF}{dt}
=
\frac{dF}{dx}\frac{dx}{dt}.
\]
Thus
\[
\frac{dF}{dx}
=
\frac1{x'(t)}
\frac{dF}{dt}.
\]

:::

:::

::: pf-step

Hence
\[
\frac{d^2y}{dx^2}
=
\frac1{x'(t)}
\frac{d}{dt}
\left(
\frac{y'(t)}{x'(t)}
\right).
\]


::: pf-proof

Apply step <1>3 to the function
\[
F(t)=\frac{dy}{dx}
=
\frac{y'}{x'}
\]
from step <1>2.

:::

:::

::: pf-step

The derivative in step <1>4 is
\[
\frac{d}{dt}
\left(
\frac{y'}{x'}
\right)
=
\frac{x'y''-y'x''}{(x')^2}.
\]


::: pf-proof

Apply the quotient rule.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\frac{d^2y}{dx^2}
=
\frac{x'(t)y''(t)-y'(t)x''(t)}
{(x'(t))^3}}.
\]


::: pf-proof

Substitute step <1>5 into step <1>4:
\[
\frac1{x'}
\cdot
\frac{x'y''-y'x''}{(x')^2}
=
\frac{x'y''-y'x''}{(x')^3}.
\]

:::

:::

::: pf-qed

Steps <1>2 and <1>6 give the requested first and second derivatives as
functions of \(t\).

:::

:::
