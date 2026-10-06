---
schema: qual/card@1
id: P-PRECALC2-10
kind: problem
title: Volume and surface area of Gabriel's horn
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
(Gabriel’s Horn) Let $f ( x ) = 1 / x$ , for $x \in [ 1 , \infty )$ . Find the volume and surface area of the shape which results from rotating the graph of f about the x-axis.
:::

::: {.solution}
The curve is
\[
y=f(x)=\frac1x,
\qquad
x\ge1.
\]

## Volume

<1>1. Rotating the region under \(y=1/x\) about the \(x\)-axis gives disks
of radius
\[
\boxed{r(x)=\frac1x}.
\]

::: {.proof}
The distance from the graph to the \(x\)-axis is \(y=1/x\).
:::

<1>2. Therefore the volume is
\[
V
=
\pi\int_1^\infty
\frac{dx}{x^2}.
\]

::: {.proof}
The cross-sectional disk area is
\[
\pi r(x)^2
=
\frac{\pi}{x^2}.
\]
Integrate from \(x=1\) to infinity.
:::

<1>3. For \(R>1\),
\[
\int_1^R\frac{dx}{x^2}
=
\left[
-\frac1x
\right]_1^R
=
1-\frac1R.
\]

::: {.proof}
An antiderivative of \(x^{-2}\) is \(-x^{-1}\).
:::

<1>4. Letting \(R\to\infty\),
\[
\boxed{
V=\pi}.
\]

::: {.proof}
By steps <1>2--<1>3,
\[
V
=
\pi
\lim_{R\to\infty}
\left(
1-\frac1R
\right)
=
\pi.
\]
:::

## Surface area

<1>5. The derivative of the profile is
\[
\boxed{
f'(x)=-\frac1{x^2}}.
\]

::: {.proof}
Differentiate \(f(x)=x^{-1}\).
:::

<1>6. The surface area is
\[
S
=
2\pi
\int_1^\infty
\frac1x
\sqrt{1+\frac1{x^4}}
\,dx.
\]

::: {.proof}
The surface-area formula for rotating \(y=f(x)\ge0\) about the \(x\)-axis is
\[
S
=
2\pi
\int
f(x)
\sqrt{1+f'(x)^2}\,dx.
\]
Use \(f(x)=1/x\) and step <1>5.
:::

<1>7. For every \(x\ge1\),
\[
\sqrt{1+\frac1{x^4}}
\ge1.
\]

::: {.proof}
Since
\[
\frac1{x^4}\ge0,
\]
one has
\[
1+\frac1{x^4}\ge1.
\]
Taking square roots preserves the inequality.
:::

<1>8. Hence
\[
S
\ge
2\pi
\int_1^\infty
\frac{dx}{x}.
\]

::: {.proof}
Apply step <1>7 pointwise to the nonnegative integrand in step <1>6.
:::

<1>9. The comparison integral diverges:
\[
\int_1^\infty
\frac{dx}{x}
=
\infty.
\]

::: {.proof}
For \(R>1\),
\[
\int_1^R\frac{dx}{x}
=
\log R,
\]
and
\[
\log R\to\infty.
\]
:::

<1>10. Therefore
\[
\boxed{S=\infty}.
\]

::: {.proof}
By steps <1>8--<1>9, the surface-area integral dominates a divergent
nonnegative integral.
:::

<1>11. Thus Gabriel’s horn has
\[
\boxed{\text{finite volume } \pi}
\]
but
\[
\boxed{\text{infinite surface area}}.
\]

::: {.proof}
Combine steps <1>4 and <1>10.
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>11 gives both requested quantities.
:::
:::
