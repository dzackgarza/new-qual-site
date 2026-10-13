---
schema: qual/card@1
id: P-PRECALC2-07
kind: problem
title: Volumes of revolution of the region between $y=x$ and $y=x^2$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
What volume is created if the area between $f ( x ) = x$ and $g ( x ) = x ^ { 2 }$ for $x \in [ 0 , 1 ]$ is revolved about the x-axis? What if the same area is revolved about the y-axis?
:::

::: {.solution}
On \(0\le x\le1\),
\[
x^2\le x,
\]
so the region lies between the upper curve \(y=x\) and the lower curve
\(y=x^2\).

## Rotation about the \(x\)-axis

<1>1. A vertical slice at \(x\) produces a washer with outer radius
\[
\boxed{R(x)=x}
\]
and inner radius
\[
\boxed{r(x)=x^2}.
\]

::: {.proof}
Both curves lie above the \(x\)-axis. The upper curve is farther from the
axis and gives the outer radius; the lower curve gives the inner radius.
:::

<1>2. The washer area is
\[
\boxed{
A(x)
=
\pi(R(x)^2-r(x)^2)
=
\pi(x^2-x^4)}.
\]

::: {.proof}
Use the area formula
\[
\pi R^2-\pi r^2.
\]
:::

<1>3. Hence the volume is
\[
V_x
=
\pi\int_0^1(x^2-x^4)\,dx.
\]

::: {.proof}
Integrate the cross-sectional washer area from \(x=0\) to \(x=1\).
:::

<1>4. Evaluating,
\[
\begin{aligned}
V_x
&=
\pi
\left[
\frac{x^3}{3}
-
\frac{x^5}{5}
\right]_0^1\\
&=
\pi
\left(
\frac13-\frac15
\right).
\end{aligned}
\]

::: {.proof}
Integrate powers term by term.
:::

<1>5. Therefore
\[
\boxed{
V_x=\frac{2\pi}{15}}.
\]

::: {.proof}
\[
\frac13-\frac15
=
\frac{5-3}{15}
=
\frac2{15}.
\]
:::

## Rotation about the \(y\)-axis

<1>6. A vertical slice at \(x\) produces a cylindrical shell of radius
\[
\boxed{x}
\]
and height
\[
\boxed{x-x^2}.
\]

::: {.proof}
The distance from the slice to the \(y\)-axis is \(x\). The vertical height
of the region is upper minus lower:
\[
x-x^2.
\]
:::

<1>7. The shell volume element is
\[
\boxed{
dV
=
2\pi x(x-x^2)\,dx}.
\]

::: {.proof}
A cylindrical shell of radius \(r\), height \(h\), and thickness \(dx\) has
volume
\[
2\pi r h\,dx.
\]
Use step <1>6.
:::

<1>8. Hence
\[
V_y
=
2\pi\int_0^1(x^2-x^3)\,dx.
\]

::: {.proof}
Expand the integrand from step <1>7 and integrate across the region.
:::

<1>9. Evaluating,
\[
\begin{aligned}
V_y
&=
2\pi
\left[
\frac{x^3}{3}
-
\frac{x^4}{4}
\right]_0^1\\
&=
2\pi
\left(
\frac13-\frac14
\right).
\end{aligned}
\]

::: {.proof}
Integrate powers term by term.
:::

<1>10. Therefore
\[
\boxed{
V_y=\frac{\pi}{6}}.
\]

::: {.proof}
\[
2\pi
\left(
\frac13-\frac14
\right)
=
2\pi\cdot\frac1{12}
=
\frac{\pi}{6}.
\]
:::

<1>11. Q.E.D.

::: {.proof}
Steps <1>5 and <1>10 give the two requested volumes.
:::
:::
