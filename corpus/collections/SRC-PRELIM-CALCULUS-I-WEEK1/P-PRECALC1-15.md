---
schema: qual/card@1
id: P-PRECALC1-15
kind: problem
title: Tangent line to $\int_1^x\frac{dt}{1+t^2}$ at $x=2$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\textstyle f ( x ) = \int _ { 1 } ^ { x } { \frac { d t } { 1 + t ^ { 2 } } }$ . Find an equation for the tangent line at $( 2 , f ( 2 ) )$ .
:::

::: {.solution}
Let
\[
f(x)
=
\int_1^x
\frac{dt}{1+t^2}.
\]

<1>1. By the fundamental theorem of calculus,
\[
\boxed{
f'(x)=\frac1{1+x^2}}.
\]

::: {.proof}
The integrand is continuous on \(\mathbb R\), so differentiating the integral
with respect to its upper limit gives the integrand evaluated at \(x\).
:::

<1>2. Therefore the slope at \(x=2\) is
\[
\boxed{
f'(2)=\frac15}.
\]

::: {.proof}
\[
f'(2)
=
\frac1{1+2^2}
=
\frac15.
\]
:::

<1>3. An antiderivative of \(1/(1+t^2)\) is \(\arctan t\).

::: {.proof}
\[
\frac{d}{dt}\arctan t
=
\frac1{1+t^2}.
\]
:::

<1>4. Hence
\[
f(2)
=
\arctan2-\arctan1.
\]

::: {.proof}
Apply the fundamental theorem of calculus using step <1>3:
\[
f(2)
=
\left[
\arctan t
\right]_1^2.
\]
:::

<1>5. Since
\[
\arctan1=\frac{\pi}{4},
\]
one has
\[
\boxed{
f(2)
=
\arctan2-\frac{\pi}{4}}.
\]

::: {.proof}
Substitute the standard value of \(\arctan1\).
:::

<1>6. The tangent line at \((2,f(2))\) is
\[
y-f(2)
=
f'(2)(x-2).
\]

::: {.proof}
This is the point-slope equation for the tangent line to a differentiable
graph.
:::

<1>7. Therefore
\[
\boxed{
y-
\left(
\arctan2-\frac{\pi}{4}
\right)
=
\frac15(x-2)}.
\]

::: {.proof}
Substitute steps <1>2 and <1>5 into step <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the requested tangent-line equation.
:::
:::
