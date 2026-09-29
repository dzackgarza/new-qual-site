---
schema: qual/card@1
id: P-BERK98S-12
kind: problem
title: Integral of $e^{-(x^2+(y-x)^2+y^2)}$ over $\RR^2$
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Given
\[
\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt\pi,
\]
evaluate
\[
I=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}
e^{-(x^2+(y-x)^2+y^2)}\,dx\,dy.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Make the orthogonal change of variables
$$
u=\frac{x+y}{\sqrt2},
\qquad
v=\frac{x-y}{\sqrt2}.
$$
Its Jacobian has absolute value $1$.

::: pf-proof

The inverse transformation is
$$
x=\frac{u+v}{\sqrt2},
\qquad
y=\frac{u-v}{\sqrt2}.
$$
Its matrix is orthogonal, so the absolute value of its determinant is $1$.
Hence
$$
dx\,dy=du\,dv.
$$

:::

:::

::: {.pf-step #s2}

Under this change of variables,
$$
x^2+(y-x)^2+y^2=u^2+3v^2.
$$

::: pf-proof

Since the transformation is orthogonal,
$$
x^2+y^2=u^2+v^2.
$$
Also,
$$
y-x
=
\frac{u-v}{\sqrt2}
-
\frac{u+v}{\sqrt2}
=-\sqrt2\,v.
$$
Therefore
$$
x^2+(y-x)^2+y^2
=u^2+v^2+2v^2
=u^2+3v^2.
$$

:::

:::

::: {.pf-step #s3}

The integral factors as
$$
I
=
\left(\int_{-\infty}^{\infty}e^{-u^2}\,du\right)
\left(\int_{-\infty}^{\infty}e^{-3v^2}\,dv\right).
$$

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref},
$$
I
=
\int_{\RR^2}e^{-u^2-3v^2}\,du\,dv.
$$
The integrand is nonnegative, so Tonelli's theorem permits separation into
the product of the two one-dimensional integrals.

:::

:::

::: {.pf-step #s4}

The second factor is
$$
\int_{-\infty}^{\infty}e^{-3v^2}\,dv
=
\sqrt{\frac\pi3}.
$$

::: pf-proof

Set $w=\sqrt3\,v$. Then
$$
dv=\frac{dw}{\sqrt3},
$$
and the given Gaussian integral yields
$$
\int_{-\infty}^{\infty}e^{-3v^2}\,dv
=
\frac1{\sqrt3}
\int_{-\infty}^{\infty}e^{-w^2}\,dw
=
\frac{\sqrt\pi}{\sqrt3}.
$$

:::

:::

::: {.pf-step #s5}

Therefore
$$
\boxed{I=\frac{\pi}{\sqrt3}}.
$$

::: pf-proof

By the given formula, the first factor in step [](#s3){.pf-ref} is $\sqrt\pi$.
Multiplying it by the value from step [](#s4){.pf-ref} gives
$$
I
=
\sqrt\pi\,
\frac{\sqrt\pi}{\sqrt3}
=
\frac\pi{\sqrt3}.
$$

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required evaluation.

:::

:::

:::
