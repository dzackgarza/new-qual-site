---
schema: qual/card@1
id: P-PRECALC2-07
kind: problem
title: Volumes of revolution of the region between $y=x$ and $y=x^2$
classification:
  areas:
  - prelim
  topics:
  - Volumes of Revolution
relations: []
review: draft
---

::: {.problem}
Let $R$ be the region between $f(x) = x$ and $g(x) = x^{2}$ for $x \in [0, 1]$.

(a) What volume is created if $R$ is revolved about the $x$-axis?

(b) What volume is created if $R$ is revolved about the $y$-axis?
:::

::: {.solution}

On $0\le x\le1$,
$$
x^2\le x,
$$
so the region lies between the upper curve $y=x$ and the lower curve
$y=x^2$.

## Rotation about the $x$-axis

::: pf

::: pf-step

A vertical slice at $x$ produces a washer with outer radius
$$
\boxed{R(x)=x}
$$
and inner radius
$$
\boxed{r(x)=x^2}.
$$


::: pf-proof

Both curves lie above the $x$-axis. The upper curve is farther from the
axis and gives the outer radius; the lower curve gives the inner radius.

:::

:::

::: pf-step

The washer area is
$$
\boxed{
A(x)
=
\pi(R(x)^2-r(x)^2)
=
\pi(x^2-x^4)}.
$$


::: pf-proof

Use the area formula
$$
\pi R^2-\pi r^2.
$$

:::

:::

::: pf-step

Hence the volume is
$$
V_x
=
\pi\int_0^1(x^2-x^4)\,dx.
$$


::: pf-proof

Integrate the cross-sectional washer area from $x=0$ to $x=1$.

:::

:::

::: pf-step

Evaluating,
$$
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
$$


::: pf-proof

Integrate powers term by term.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
V_x=\frac{2\pi}{15}}.
$$


::: pf-proof

$$
\frac13-\frac15
=
\frac{5-3}{15}
=
\frac2{15}.
$$

:::

:::

::: {.pf-step #s1-6}

A vertical slice at $x$ produces a cylindrical shell of radius
$$
\boxed{x}
$$
and height
$$
\boxed{x-x^2}.
$$


::: pf-proof

The distance from the slice to the $y$-axis is $x$. The vertical height
of the region is upper minus lower:
$$
x-x^2.
$$

:::

:::

::: {.pf-step #s1-7}

The shell volume element is
$$
\boxed{
dV
=
2\pi x(x-x^2)\,dx}.
$$


::: pf-proof

A cylindrical shell of radius $r$, height $h$, and thickness $dx$ has
volume
$$
2\pi r h\,dx.
$$
Use step [](#s1-6){.pf-ref}.

:::

:::

::: pf-step

Hence
$$
V_y
=
2\pi\int_0^1(x^2-x^3)\,dx.
$$


::: pf-proof

Expand the integrand from step [](#s1-7){.pf-ref} and integrate across the region.

:::

:::

::: pf-step

Evaluating,
$$
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
$$


::: pf-proof

Integrate powers term by term.

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
V_y=\frac{\pi}{6}}.
$$


::: pf-proof

$$
2\pi
\left(
\frac13-\frac14
\right)
=
2\pi\cdot\frac1{12}
=
\frac{\pi}{6}.
$$

:::

:::

::: pf-qed

Steps [](#s1-5){.pf-ref} and [](#s1-10){.pf-ref} give the two requested volumes.

:::

:::

:::
