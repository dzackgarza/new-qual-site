---
schema: qual/card@1
id: P-TRIV-RA21
kind: problem
title: Gaussian integral $\int_0^\infty e^{-x^2}\,dx$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 21, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find $\int_0^{\infty} e^{-x^2}\, dx$.
:::

::: {.solution}

Let
$$
I=
\int_0^\infty e^{-x^2}\,dx.
$$

::: pf

::: pf-step

One has
$$
I^2
=
\int_0^\infty
\int_0^\infty
e^{-(x^2+y^2)}
\,dx\,dy.
$$


::: pf-proof

Both one-dimensional integrals converge and the integrand is nonnegative, so
Tonelli's theorem gives
$$
I^2
=
\left(
\int_0^\infty e^{-x^2}\,dx
\right)
\left(
\int_0^\infty e^{-y^2}\,dy
\right)
=
\int_0^\infty
\int_0^\infty
e^{-(x^2+y^2)}
\,dx\,dy.
$$

:::

:::

::: {.pf-step #s1-2}

Passing to polar coordinates in the first quadrant gives
$$
I^2
=
\int_0^{\pi/2}
\int_0^\infty
e^{-r^2}r
\,dr\,d\theta.
$$


::: pf-proof

Use
$$
x=r\cos\theta,
\qquad
y=r\sin\theta,
$$
with
$$
r\geq0,
\qquad
0\leq\theta\leq\frac\pi2.
$$
The Jacobian is $r$.

:::

:::

::: {.pf-step #s1-3}

The radial integral equals
$$
\int_0^\infty e^{-r^2}r\,dr
=
\frac12.
$$


::: pf-proof

Set
$$
u=r^2,
\qquad
du=2r\,dr.
$$
Then
$$
\int_0^\infty e^{-r^2}r\,dr
=
\frac12
\int_0^\infty e^{-u}\,du
=
\frac12.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
I^2
=
\frac\pi2\cdot\frac12
=
\frac\pi4.
$$


::: pf-proof

Substitute step [](#s1-3){.pf-ref} into step [](#s1-2){.pf-ref} and integrate $d\theta$ from $0$ to
$\pi/2$.

:::

:::

::: {.pf-step #s1-5}

Since $I>0$,
$$
\boxed{
I=\frac{\sqrt\pi}{2}.
}
$$


::: pf-proof

Take the positive square root of step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required value.

:::

:::

:::
