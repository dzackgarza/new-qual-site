---
schema: qual/card@1
id: P-CASP06E
kind: problem
title: "Linear transformations preserving concentric circles preserve the ratio of radii"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Suppose that a linear transformation carries one pair of concentric circles into another pair of concentric circles.
Prove that the ratios of the radii must be the same.
:::

::: {.solution}

Here "linear transformation" is read in the classical complex-analysis sense of a linear fractional (Möbius) transformation of the Riemann sphere; the argument is the card's own, and the sets searched are recorded in the audit trail.

Let the first pair of concentric circles be the boundary circles of the annulus $A(r,R)=\{r<\abs{z-a}<R\}$ with $0<r<R$, and let their images under the transformation $T$ be the two concentric circles $\abs{w-b}=r'$ and $\abs{w-b}=R'$ with $0<r'<R'$, named so that the second pair bounds $A(r',R')=\{r'<\abs{w-b}<R'\}$.

::: pf

::: {.pf-step #mobius}
$T$ restricts to a conformal equivalence of $A(r,R)$ with $A(r',R')$.

::: pf-proof
A Möbius transformation is a homeomorphism of the Riemann sphere that is holomorphic with nonzero derivative, hence conformal wherever it is defined, and it carries each of the two circles $\abs{z-a}=r$ and $\abs{z-a}=R$ onto a circle; by hypothesis the images are the two concentric circles bounding $A(r',R')$. The complement of those two starting circles has three components — the disc $\{\abs{z-a}<r\}$, the annulus $A(r,R)$, and the exterior $\{\abs{z-a}>R\}$ — and $A(r,R)$ is the only one of them whose closure meets both circles; the same description singles out $A(r',R')$ among the three components of the complement of the image pair. A homeomorphism carries components to components and preserves whether the closure of a component meets a given circle, so $T$ maps $A(r,R)$ onto $A(r',R')$, and being conformal on it, $T$ restricts to a conformal equivalence of the two annuli.

:::

:::

::: {.pf-step #modulus}
The modulus $\operatorname{mod}A=\frac{1}{2\pi}\log\frac{R}{r}$ is a conformal invariant.

::: pf-proof
The modulus of an annulus is defined as the number $\rho>0$ for which the annulus is conformally equivalent to the standard annulus $\{\rho<\abs{w}<1\}$, and the modulus of $A(r,R)$ is computed by the logarithm map: $z\mapsto\log z$ carries $A(r,R)$ conformally onto the rectangle $\{\log r<\operatorname{Re}w<\log R,\ 0<\operatorname{Im}w<2\pi\}$, and the exponential normalisation of that rectangle gives the standard annulus with $\rho=r/R$, so $\operatorname{mod}A(r,R)=\frac{1}{2\pi}\log\frac{R}{r}$. Since conformal equivalence is transitive, two conformally equivalent annuli are equivalent to the same standard annulus and hence have the same modulus.
:::

:::

::: {.pf-step #conclusion}
$\dfrac{R}{r}=\dfrac{R'}{r'}$.

::: pf-proof
By steps [](#mobius){.pf-ref} and [](#modulus){.pf-ref}, $\frac{1}{2\pi}\log\frac{R}{r}=\frac{1}{2\pi}\log\frac{R'}{r'}$, so $\log\frac{R}{r}=\log\frac{R'}{r'}$ and, the logarithm being injective on $(0,\infty)$, $\frac{R}{r}=\frac{R'}{r'}$.
:::

:::

:::
:::
