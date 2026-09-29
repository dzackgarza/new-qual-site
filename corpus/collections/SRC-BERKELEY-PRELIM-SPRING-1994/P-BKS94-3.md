---
schema: qual/card@1
id: P-BKS94-3
kind: problem
title: Evaluation of $\int_{-\pi}^{\pi} d\theta/(3-\cos\theta)$
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
  note: Checked against the vendored UC Berkeley Spring 1994 preliminary examination.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used the tangent half-angle substitution to reduce the integral to the
    standard integral of 1/(1+2t^2) over the real line.
---

::: {.problem}
Evaluate

$$
\int _ { - \pi } ^ { \pi } { \frac { d \theta } { 3 - \cos \theta } } \cdotp
$$
:::

::: {.solution}

::: pf

::: pf-step

Under the substitution
$$
t=\tan\frac{\theta}{2},
$$
one has
$$
\cos\theta=\frac{1-t^2}{1+t^2},
\qquad
d\theta=\frac{2\,dt}{1+t^2}.
$$

::: pf-proof

These are the standard tangent half-angle identities.

:::

:::

::: {.pf-step #s2}

The integral becomes
$$
\int_{-\infty}^{\infty}\frac{dt}{1+2t^2}.
$$

::: pf-proof

As $\theta$ runs from $-\pi$ to $\pi$, the variable $t$ runs from
$-\infty$ to $\infty$. Moreover,
$$
3-\cos\theta
=
3-\frac{1-t^2}{1+t^2}
=
\frac{2+4t^2}{1+t^2}.
$$
Hence
$$
\frac{d\theta}{3-\cos\theta}
=
\frac{2\,dt}{1+t^2}
\frac{1+t^2}{2+4t^2}
=
\frac{dt}{1+2t^2}.
$$

:::

:::

::: {.pf-step #s3}

One has
$$
\int_{-\infty}^{\infty}\frac{dt}{1+2t^2}
=
\frac{\pi}{\sqrt2}.
$$

::: pf-proof

Set $u=\sqrt2\,t$. Then
$$
\int_{-\infty}^{\infty}\frac{dt}{1+2t^2}
=
\frac1{\sqrt2}
\int_{-\infty}^{\infty}\frac{du}{1+u^2}
=
\frac1{\sqrt2}
\left[\arctan u\right]_{-\infty}^{\infty}
=
\frac{\pi}{\sqrt2}.
$$

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{
\int_{-\pi}^{\pi}\frac{d\theta}{3-\cos\theta}
=
\frac{\pi}{\sqrt2}
}.
$$

::: pf-proof

Combine steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the requested value.

:::

:::

:::
