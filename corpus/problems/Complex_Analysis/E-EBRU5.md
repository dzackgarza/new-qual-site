---
schema: qual/card@1
id: E-EBRU5
kind: problem
title: $\int_0^1\frac{dx}{\sqrt{x^2-1}}$ by a dogbone contour
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
---

::: {.exercise}
\[
I \da \int_0^1 {1\over \sqrt{x^2-1}}\dx = {i\pi \over 2}
.\]

:::

::: {.solution}
On $(0,1)$ the radicand is negative, so $\sqrt{x^2-1}=\pm i\sqrt{1-x^2}$ and the value of $I$ depends on the branch. The stated value holds for $\sqrt{x^2-1}=-i\sqrt{1-x^2}$; the other branch gives $-i\pi/2$. Put $J\da\int_{-1}^1{dx\over\sqrt{1-x^2}}$.

::: pf

::: {.pf-step #boundary-values}
Let $g(z)\da\sqrt{z-1}\,\sqrt{z+1}$ with principal square roots. Then $g$ is holomorphic on $\CC\setminus[-1,1]$, and for $-1<x<1$ its boundary values are $g(x+i0)=i\sqrt{1-x^2}$ from above and $g(x-i0)=-i\sqrt{1-x^2}$ from below.

::: pf-proof
Each factor is holomorphic off its cut, $(-\infty,1]$ and $(-\infty,-1]$ respectively. On $(-\infty,-1)$ both factors change sign across the real axis, so their product is continuous there and extends holomorphically across it. For $-1<x<1$, $\sqrt{x+1}$ is continuous and positive, while $\sqrt{x-1\pm i0}=\pm i\sqrt{1-x}$.
:::

:::

::: {.pf-step #circle-integral-2pi-i}
$\oint_{\abs z=2}{dz\over g(z)}=2\pi i$.

::: pf-proof
For $\abs z>1$, $g(z)=z\sqrt{1-z^{-2}}$ with the principal branch, since both sides are holomorphic there, square to $z^2-1$, and are asymptotic to $z$ as $z\to+\infty$ along the real axis. So $1/g(z)=z^{-1}\qty{1+\tfrac12z^{-2}+\cdots}$ on $\abs z>1$, and only the term $z^{-1}$ contributes to the integral.
:::

:::

::: {.pf-step #circle-integral-2iJ}
$\oint_{\abs z=2}{dz\over g(z)}=2iJ$.

::: pf-proof
Let $\Gamma_\eps$ be the dogbone contour around the slit, oriented counterclockwise: the upper edge from $1$ to $-1$, the lower edge from $-1$ to $1$, and circles of radius $\eps$ about $\pm1$.

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-28_00-37-42.png)

By Cauchy's theorem on the region between them, $\Gamma_\eps$ and $\abs z=2$ give the same integral. On the circle about $\pm1$, $\abs{z^2-1}=\eps\abs{z\pm1}\ge\eps(2-\eps)\ge\eps$ for $\eps<1$, so that circle contributes at most $2\pi\eps\cdot\eps^{-1/2}\to0$. By step [](#boundary-values){.pf-ref} the edges contribute, as $\eps\to0$,
\[
\int_1^{-1}{dx\over i\sqrt{1-x^2}}+\int_{-1}^1{dx\over -i\sqrt{1-x^2}}
=\qty{-{1\over i}-{1\over i}}J=2iJ
.\]
:::

:::

::: pf-qed
Steps [](#circle-integral-2pi-i){.pf-ref} and [](#circle-integral-2iJ){.pf-ref} give $J=\pi$. The integrand $1/\sqrt{1-x^2}$ is even, so with $\sqrt{x^2-1}=-i\sqrt{1-x^2}$,
\[
I=\int_0^1{dx\over -i\sqrt{1-x^2}}=i\cdot{J\over2}={i\pi\over2}
.\]
:::

:::
