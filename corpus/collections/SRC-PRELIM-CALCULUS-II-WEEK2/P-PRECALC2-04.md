---
schema: qual/card@1
id: P-PRECALC2-04
kind: problem
title: Integral of $\frac{1}{\cosh t}$ over $(-\infty,x]$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Perform the integral $\int _ { - \infty } ^ { x } { \frac { d t } { \cosh ( t ) } }$ . (Recall $\begin{array} { r } { \cosh ( t ) = \frac { e ^ { t } + e ^ { - t } } { 2 } ) } \end{array}$
:::

::: pf

::: pf-step

Rewrite the integrand as
\[
\boxed{
\frac1{\cosh t}
=
\frac{2e^t}{1+e^{2t}}}.
\]


::: pf-proof

Using
\[
\cosh t
=
\frac{e^t+e^{-t}}2,
\]
one gets
\[
\frac1{\cosh t}
=
\frac{2}{e^t+e^{-t}}.
\]
Multiply numerator and denominator by \(e^t\):
\[
\frac{2e^t}{e^{2t}+1}.
\]

:::

:::

::: pf-step

Set
\[
\boxed{u=e^t}.
\]


::: pf-proof

This substitution matches the numerator \(e^t\,dt\).

:::

:::

::: pf-step

Then
\[
\boxed{du=e^t\,dt}.
\]


::: pf-proof

Differentiate \(u=e^t\).

:::

:::

::: pf-step

As
\[
t\to-\infty,
\]
one has
\[
\boxed{u\to0}.
\]


::: pf-proof

\[
e^t\to0
\qquad(t\to-\infty).
\]

:::

:::

::: pf-step

At the upper endpoint \(t=x\),
\[
\boxed{u=e^x}.
\]


::: pf-proof

Substitute \(t=x\) into \(u=e^t\).

:::

:::

::: pf-step

Therefore
\[
\int_{-\infty}^{x}\frac{dt}{\cosh t}
=
2\int_0^{e^x}\frac{du}{1+u^2}.
\]


::: pf-proof

Apply steps <1>1--<1>5.

:::

:::

::: pf-step

Since
\[
\frac{d}{du}\arctan u
=
\frac1{1+u^2},
\]
one has
\[
2\int_0^{e^x}\frac{du}{1+u^2}
=
2\left[
\arctan u
\right]_0^{e^x}.
\]


::: pf-proof

Use the standard antiderivative of \(1/(1+u^2)\).

:::

:::

::: pf-step

Hence
\[
\boxed{
\int_{-\infty}^{x}\frac{dt}{\cosh t}
=
2\arctan(e^x)}.
\]


::: pf-proof

Since
\[
\arctan0=0,
\]
step <1>7 gives
\[
2\arctan(e^x).
\]

:::

:::

::: pf-qed

Step <1>8 is the requested antiderivative-with-limit.

:::

:::
