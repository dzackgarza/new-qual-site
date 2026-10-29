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

::: pf

::: pf-step

By the fundamental theorem of calculus,
\[
\boxed{
f'(x)=\frac1{1+x^2}}.
\]


::: pf-proof

The integrand is continuous on \(\RR\), so differentiating the integral
with respect to its upper limit gives the integrand evaluated at \(x\).

:::

:::

::: {.pf-step #s1-2}

Therefore the slope at \(x=2\) is
\[
\boxed{
f'(2)=\frac15}.
\]


::: pf-proof

\[
f'(2)
=
\frac1{1+2^2}
=
\frac15.
\]

:::

:::

::: {.pf-step #s1-3}

An antiderivative of \(1/(1+t^2)\) is \(\arctan t\).


::: pf-proof

\[
\frac{d}{dt}\arctan t
=
\frac1{1+t^2}.
\]

:::

:::

::: pf-step

Hence
\[
f(2)
=
\arctan2-\arctan1.
\]


::: pf-proof

Apply the fundamental theorem of calculus using step [](#s1-3){.pf-ref}:
\[
f(2)
=
\left[
\arctan t
\right]_1^2.
\]

:::

:::

::: {.pf-step #s1-5}

Since
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


::: pf-proof

Substitute the standard value of \(\arctan1\).

:::

:::

::: {.pf-step #s1-6}

The tangent line at \((2,f(2))\) is
\[
y-f(2)
=
f'(2)(x-2).
\]


::: pf-proof

This is the point-slope equation for the tangent line to a differentiable
graph.

:::

:::

::: {.pf-step #s1-7}

Therefore
\[
\boxed{
y-
\left(
\arctan2-\frac{\pi}{4}
\right)
=
\frac15(x-2)}.
\]


::: pf-proof

Substitute steps [](#s1-2){.pf-ref} and [](#s1-5){.pf-ref} into step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the requested tangent-line equation.

:::

:::

:::
