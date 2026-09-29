---
schema: qual/card@1
id: P-BKF93-3
kind: problem
title: Region of convergence of an exponential series in the complex plane
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Reduced convergence to the sign of Re(z/(z-2)) and rewrote that real part
    as (|z-1|^2-1)/|z-2|^2, yielding the closed unit disk centered at 1 with
    the undefined boundary point z=2 removed.
---

::: {.problem}
Describe and sketch the region in the complex plane where
\[
\sum_{n=1}^{\infty}\frac1{n^2}\exp\left(\frac{nz}{z-2}\right)
\]
converges.
:::

::: {.solution}
For $z\neq2$, put
$$
w\coloneqq\frac{z}{z-2}.
$$

::: pf

::: {.pf-step #s1}

The series converges if and only if
$$
\Re w\leq0.
$$

::: pf-proof

Its $n$th term has absolute value
$$
\frac1{n^2}\abs{e^{nw}}
=
\frac{e^{n\Re w}}{n^2}.
$$
If $\Re w<0$, these absolute values are bounded by a convergent geometric
series for all sufficiently large $n$, so the given series converges
absolutely. If $\Re w=0$, the series again converges absolutely because its
absolute values are $1/n^2$. If $\Re w>0$, then
$$
\frac{e^{n\Re w}}{n^2}\longrightarrow\infty,
$$
so the terms do not tend to zero and the series diverges.

:::

:::

::: {.pf-step #s2}

If $z=x+iy\neq2$, then
$$
\Re\left(\frac{z}{z-2}\right)
=
\frac{(x-1)^2+y^2-1}{(x-2)^2+y^2}
=
\frac{\abs{z-1}^2-1}{\abs{z-2}^2}.
$$

::: pf-proof

Multiplying numerator and denominator by $\overline z-2$ gives
$$
\frac{z}{z-2}
=
\frac{z(\overline z-2)}{\abs{z-2}^2}.
$$
The real part of the numerator is
$$
\abs z^2-2\Re z
=
x^2+y^2-2x
=
(x-1)^2+y^2-1.
$$
Since $z\neq2$, the denominator is positive.

:::

:::

::: {.pf-step #s3}

The region of convergence is
$$
\boxed{\{z\in\CC:\abs{z-1}\leq1\}\setminus\{2\}}.
$$

::: pf-proof

By step [](#s2){.pf-ref}, the inequality in step [](#s1){.pf-ref} is equivalent to
$$
\abs{z-1}^2-1\leq0,
$$
hence to $\abs{z-1}\leq1$. The point $z=2$ must be removed because the
summand is not defined there. Thus the sketch is the closed disk of radius
$1$ centered at $1$ on the real axis, with the boundary point $2$ deleted.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} determine and describe the complete convergence region.

:::

:::

:::
