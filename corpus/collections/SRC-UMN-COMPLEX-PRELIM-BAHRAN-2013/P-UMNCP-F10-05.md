---
schema: qual/card@1
id: P-UMNCP-F10-05
kind: problem
title: Cauchy derivative estimate in the unit disk
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Fall 2010, 5 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Let \(f\) be holomorphic on the unit disk and suppose \(|f(z)|\le M\) there.
Prove that
\[
|f'(z)|\le \frac{M}{1-|z|}
\]
for every \(z\) in the unit disk.
:::

::: {.solution}

Fix
$$
z_0\in\DD.
$$

::: pf

::: {.pf-step #s1-1}

If
$$
0<r<1-|z_0|,
$$
then the closed disk
$$
\overline{D(z_0,r)}
$$
lies inside the unit disk.


::: pf-proof

If
$$
|\zeta-z_0|\le r,
$$
then
$$
|\zeta|
\le
|\zeta-z_0|+|z_0|
\le
r+|z_0|
<
1.
$$
Thus every point of the closed disk lies in $\DD$.

:::

:::

::: {.pf-step #s1-2}

For every such $r$, Cauchy's integral formula gives
$$
f'(z_0)
=
\frac1{2\pi i}
\int_{|\zeta-z_0|=r}
\frac{f(\zeta)}
{(\zeta-z_0)^2}
\,d\zeta.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, $f$ is holomorphic on an open neighborhood of the closed disk centered at $z_0$ of radius $r$. The derivative form of Cauchy's integral formula therefore applies.

:::

:::

::: {.pf-step #s1-3}

For every
$$
0<r<1-|z_0|,
$$
one has
$$
\boxed{
|f'(z_0)|
\le
\frac Mr}.
$$


::: pf-proof

Using step [](#s1-2){.pf-ref} and the ML estimate,
$$
\begin{aligned}
|f'(z_0)|
&\le
\frac1{2\pi}
\left(
2\pi r
\right)
\frac{M}{r^2}\\
&=
\frac Mr.
\end{aligned}
$$
Here
$$
|f(\zeta)|\le M
$$
by hypothesis and
$$
|\zeta-z_0|=r
$$
on the contour.

:::

:::

::: {.pf-step #s1-4}

Letting
$$
r\uparrow1-|z_0|
$$
gives
$$
\boxed{
|f'(z_0)|
\le
\frac{M}{1-|z_0|}}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} holds for every
$$
r<1-|z_0|.
$$
Choose any increasing sequence
$$
r_j\to1-|z_0|.
$$
Then
$$
|f'(z_0)|
\le
\frac{M}{r_j}
$$
for every $j$. Passing to the limit gives the displayed estimate.

:::

:::

::: {.pf-step #s1-5}

The estimate holds for every point of the unit disk.


::: pf-proof

The point
$$
z_0\in\DD
$$
was arbitrary.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} prove the required bound.

:::

:::

:::
