---
schema: qual/card@1
id: P-CASP17A
kind: problem
title: The integral $\int_0^\infty\frac{\cos x}{(1+x^2)^2}\,dx$ by residues
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residue Theorem
relations: []
review: draft
---

::: {.problem}
Using the calculus of residues, compute
$$
\int_0^\infty \frac{\cos x}{(1 + x^2)^2} \, dx.
$$
:::

::: {.solution}

The computation is the card's own, by the standard semicircular contour; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Put $F(z)=e^{iz}/(1+z^{2})^{2}$, which is meromorphic on $\CC$ with poles at $\pm i$ only, and for $R>1$ let $\Gamma_{R}$ be the boundary of the upper half-disc $\{z:\abs{z}\le R,\ \operatorname{Im}z\ge0\}$, that is the segment $[-R,R]$ followed by the semicircle $C_{R}$.

::: pf

::: {.pf-step #poles}
The only pole of $F$ in the upper half-plane is $z=i$, of order $2$, with $\operatorname{Res}_{z=i}F=-\dfrac{i}{2e}$.

::: pf-proof
$1+z^{2}=(z-i)(z+i)$, so $F(z)=e^{iz}\big/(z-i)^{2}(z+i)^{2}$ has a pole of order $2$ at $i$ and at $-i$ and no others. For a pole of order $2$ at $a$ the residue is the derivative at $a$ of $(z-a)^{2}F(z)$ (the residue formula for a pole of order $m$, §4.3), so
$$
\operatorname{Res}_{z=i}F=\evaluated{\frac{d}{dz}\frac{e^{iz}}{(z+i)^{2}}}_{z=i}
=\evaluated{\frac{e^{iz}\big(i(z+i)-2\big)}{(z+i)^{3}}}_{z=i}
=\frac{e^{-1}\,(2i^{2}-2)}{(2i)^{3}}=\frac{-4e^{-1}}{-8i}=-\frac{i}{2e},
$$
using $i(z+i)=iz-1$, which at $z=i$ equals $-2$.
:::

:::

::: {.pf-step #arc}
$\lim_{R\to\infty}\int_{C_{R}}F(z)\,dz=0$.

::: pf-proof
On $C_{R}$ one has $\abs{e^{iz}}=e^{-\operatorname{Im}z}\le1$ and $\abs{1+z^{2}}\ge\abs{z}^{2}-1=R^{2}-1$, so $\abs{F}\le(R^{2}-1)^{-2}$ there. Hence
$$
\abs{\int_{C_{R}}F\,dz}\le\pi R\cdot(R^{2}-1)^{-2}\to0
$$
as $R\to\infty$, by the estimation lemma (ML-inequality) for the integral along a contour.
:::

:::

::: {.pf-step #residue}
$\displaystyle\int_{-\infty}^{\infty}\frac{e^{ix}}{(1+x^{2})^{2}}\,dx=\frac{\pi}{e}$.

::: pf-proof
For $R>1$ the function $F$ is holomorphic on a neighbourhood of the closed upper half-disc and has inside it only the pole $i$, so the residue theorem gives
$$
\int_{-R}^{R}F(x)\,dx+\int_{C_{R}}F(z)\,dz=2\pi i\operatorname{Res}_{z=i}F=2\pi i\left(-\frac{i}{2e}\right)=\frac{\pi}{e}.
$$
Letting $R\to\infty$ and using step [](#arc){.pf-ref} for the second term gives the display.
:::

:::

::: {.pf-step #answer}
$\displaystyle\int_{0}^{\infty}\frac{\cos x}{(1+x^{2})^{2}}\,dx=\boxed{\dfrac{\pi}{2e}}$.

::: pf-proof
Taking real parts in step [](#residue){.pf-ref}, $\int_{-\infty}^{\infty}\cos x\,(1+x^{2})^{-2}\,dx=\pi/e$, the imaginary part of the left-hand integral being $0$ because $\sin x\,(1+x^{2})^{-2}$ is odd. The integrand $\cos x\,(1+x^{2})^{-2}$ is even, so the integral over $[0,\infty)$ is half the integral over $\RR$.
:::

:::

:::
:::
