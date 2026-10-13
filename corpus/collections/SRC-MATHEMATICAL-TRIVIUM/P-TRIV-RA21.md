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
Find $\int _ { 0 } ^ { \infty } e ^ { - x ^ { 2 } } d x .$
:::

::: {.solution}
Let
$$
I=
\int_0^\infty e^{-x^2}\,dx.
$$

<1>1. One has
$$
I^2
=
\int_0^\infty
\int_0^\infty
e^{-(x^2+y^2)}
\,dx\,dy.
$$

::: {.proof}
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

<1>2. Passing to polar coordinates in the first quadrant gives
$$
I^2
=
\int_0^{\pi/2}
\int_0^\infty
e^{-r^2}r
\,dr\,d\theta.
$$

::: {.proof}
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

<1>3. The radial integral equals
$$
\int_0^\infty e^{-r^2}r\,dr
=
\frac12.
$$

::: {.proof}
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

<1>4. Therefore
$$
I^2
=
\frac\pi2\cdot\frac12
=
\frac\pi4.
$$

::: {.proof}
Substitute step <1>3 into step <1>2 and integrate $d\theta$ from $0$ to
$\pi/2$.
:::

<1>5. Since $I>0$,
$$
\boxed{
I=\frac{\sqrt\pi}{2}.
}
$$

::: {.proof}
Take the positive square root of step <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required value.
:::
:::
