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

::: {.solution}
<1>1. Rewrite the integrand as
\[
\boxed{
\frac1{\cosh t}
=
\frac{2e^t}{1+e^{2t}}}.
\]

::: {.proof}
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

<1>2. Set
\[
\boxed{u=e^t}.
\]

::: {.proof}
This substitution matches the numerator \(e^t\,dt\).
:::

<1>3. Then
\[
\boxed{du=e^t\,dt}.
\]

::: {.proof}
Differentiate \(u=e^t\).
:::

<1>4. As
\[
t\to-\infty,
\]
one has
\[
\boxed{u\to0}.
\]

::: {.proof}
\[
e^t\to0
\qquad(t\to-\infty).
\]
:::

<1>5. At the upper endpoint \(t=x\),
\[
\boxed{u=e^x}.
\]

::: {.proof}
Substitute \(t=x\) into \(u=e^t\).
:::

<1>6. Therefore
\[
\int_{-\infty}^{x}\frac{dt}{\cosh t}
=
2\int_0^{e^x}\frac{du}{1+u^2}.
\]

::: {.proof}
Apply steps <1>1--<1>5.
:::

<1>7. Since
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

::: {.proof}
Use the standard antiderivative of \(1/(1+u^2)\).
:::

<1>8. Hence
\[
\boxed{
\int_{-\infty}^{x}\frac{dt}{\cosh t}
=
2\arctan(e^x)}.
\]

::: {.proof}
Since
\[
\arctan0=0,
\]
step <1>7 gives
\[
2\arctan(e^x).
\]
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the requested antiderivative-with-limit.
:::
:::
