---
schema: qual/card@1
id: P-PRECALC2-10
kind: problem
title: Volume and surface area of Gabriel's horn
classification:
  areas:
  - prelim
  topics:
  - Volumes of Revolution
  - Improper Integrals
relations: []
review: draft
---

::: {.problem}
(Gabriel's Horn) Let $f(x)=1/x$ for $x\in[1,\infty)$. Find the volume and surface area of the shape which results from rotating the graph of $f$ about the $x$-axis.
:::

::: {.solution}

The curve is
$$
y=f(x)=\frac1x,
\qquad
x\ge1.
$$

## Volume

::: pf

::: pf-step

Rotating the region under $y=1/x$ about the $x$-axis gives disks
of radius
$$
\boxed{r(x)=\frac1x}.
$$


::: pf-proof

The distance from the graph to the $x$-axis is $y=1/x$.

:::

:::

::: {.pf-step #s1-2}

Therefore the volume is
$$
V
=
\pi\int_1^\infty
\frac{dx}{x^2}.
$$


::: pf-proof

The cross-sectional disk area is
$$
\pi r(x)^2
=
\frac{\pi}{x^2}.
$$
Integrate from $x=1$ to infinity.

:::

:::

::: {.pf-step #s1-3}

For $R>1$,
$$
\int_1^R\frac{dx}{x^2}
=
\left[
-\frac1x
\right]_1^R
=
1-\frac1R.
$$


::: pf-proof

An antiderivative of $x^{-2}$ is $-x^{-1}$.

:::

:::

::: {.pf-step #s1-4}

Letting $R\to\infty$,
$$
\boxed{
V=\pi}.
$$


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref},
$$
V
=
\pi
\lim_{R\to\infty}
\left(
1-\frac1R
\right)
=
\pi.
$$

:::

:::

::: {.pf-step #s1-5}

The derivative of the profile is
$$
\boxed{
f'(x)=-\frac1{x^2}}.
$$


::: pf-proof

Differentiate $f(x)=x^{-1}$.

:::

:::

::: {.pf-step #s1-6}

The surface area is
$$
S
=
2\pi
\int_1^\infty
\frac1x
\sqrt{1+\frac1{x^4}}
\,dx.
$$


::: pf-proof

The surface-area formula for rotating $y=f(x)\ge0$ about the $x$-axis is
$$
S
=
2\pi
\int
f(x)
\sqrt{1+f'(x)^2}\,dx.
$$
Use $f(x)=1/x$ and step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

For every $x\ge1$,
$$
\sqrt{1+\frac1{x^4}}
\ge1.
$$


::: pf-proof

Since
$$
\frac1{x^4}\ge0,
$$
one has
$$
1+\frac1{x^4}\ge1.
$$
Taking square roots preserves the inequality.

:::

:::

::: {.pf-step #s1-8}

Hence
$$
S
\ge
2\pi
\int_1^\infty
\frac{dx}{x}.
$$


::: pf-proof

Apply step [](#s1-7){.pf-ref} pointwise to the nonnegative integrand in step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

The comparison integral diverges:
$$
\int_1^\infty
\frac{dx}{x}
=
\infty.
$$


::: pf-proof

For $R>1$,
$$
\int_1^R\frac{dx}{x}
=
\log R,
$$
and
$$
\log R\to\infty.
$$

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{S=\infty}.
$$


::: pf-proof

By steps [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref}, the surface-area integral dominates a divergent
nonnegative integral.

:::

:::

::: {.pf-step #s1-11}

Thus Gabriel’s horn has
$$
\boxed{\text{finite volume } \pi}
$$
but
$$
\boxed{\text{infinite surface area}}.
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} and [](#s1-10){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-11){.pf-ref} gives both requested quantities.

:::

:::

:::
