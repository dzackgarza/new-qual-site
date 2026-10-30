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
Perform the integral $\displaystyle \int_{-\infty}^{x} \frac{dt}{\cosh(t)}$. (Recall $\cosh(t) = \frac{e^{t} + e^{-t}}{2}$.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Rewrite the integrand as
$$
\boxed{
\frac1{\cosh t}
=
\frac{2e^t}{1+e^{2t}}}.
$$


::: pf-proof

Using
$$
\cosh t
=
\frac{e^t+e^{-t}}2,
$$
one gets
$$
\frac1{\cosh t}
=
\frac{2}{e^t+e^{-t}}.
$$
Multiply numerator and denominator by $e^t$:
$$
\frac{2e^t}{e^{2t}+1}.
$$

:::

:::

::: {.pf-step #s1-2}

Set
$$
\boxed{u=e^t}.
$$


::: pf-proof

This substitution matches the numerator $e^t\,dt$.

:::

:::

::: {.pf-step #s1-3}

Then
$$
\boxed{du=e^t\,dt}.
$$


::: pf-proof

Differentiate $u=e^t$.

:::

:::

::: {.pf-step #s1-4}

As
$$
t\to-\infty,
$$
one has
$$
\boxed{u\to0}.
$$


::: pf-proof

$$
e^t\to0
\qquad(t\to-\infty).
$$

:::

:::

::: {.pf-step #s1-5}

At the upper endpoint $t=x$,
$$
\boxed{u=e^x}.
$$


::: pf-proof

Substitute $t=x$ into $u=e^t$.

:::

:::

::: pf-step

Therefore
$$
\int_{-\infty}^{x}\frac{dt}{\cosh t}
=
2\int_0^{e^x}\frac{du}{1+u^2}.
$$


::: pf-proof

Apply steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Since
$$
\frac{d}{du}\arctan u
=
\frac1{1+u^2},
$$
one has
$$
2\int_0^{e^x}\frac{du}{1+u^2}
=
2\left[
\arctan u
\right]_0^{e^x}.
$$


::: pf-proof

Use the standard antiderivative of $1/(1+u^2)$.

:::

:::

::: {.pf-step #s1-8}

Hence
$$
\boxed{
\int_{-\infty}^{x}\frac{dt}{\cosh t}
=
2\arctan(e^x)}.
$$


::: pf-proof

Since
$$
\arctan0=0,
$$
step [](#s1-7){.pf-ref} gives
$$
2\arctan(e^x).
$$

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the requested antiderivative-with-limit.

:::

:::

:::
