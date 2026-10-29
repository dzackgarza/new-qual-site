---
schema: qual/card@1
id: E-M5MWL
kind: problem
title: Primitive in the complement of a branch cut
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Complex Logarithm
  - Cauchy Integral Theorem
relations: []
review: draft
---

::: {.exercise}
Compute the following integrals:

(a) $\displaystyle\int_{\abs{z-1} = 1} {1\over z^2-1} \dz$

(b) $\displaystyle\int_{\abs{z-0} = 2} {1\over z^2-1} \dz$

Compute the 2nd integral by finding a primitive.

:::

::: {.solution}
Write $f(z)\coloneqq\frac1{z^2-1}=\frac12\qty(\frac1{z-1}-\frac1{z+1})$, with both circles positively oriented.

::: pf

::: pf-step
(a) $\int_{\abs{z-1}=1}f\,dz=\boxed{\pi i}$.

::: pf-proof
The pole $1$ lies inside the circle and $-1$ lies outside it. The term $-\frac{1}{2(z+1)}$ is holomorphic on a neighborhood of the closed disk, so its integral is $0$, and $\int_{\abs{z-1}=1}\frac{dz}{2(z-1)}=\frac12\cdot2\pi i$.
:::

:::

::: {.pf-step #primitive}
$F(z)\coloneqq\frac12\operatorname{Log}\frac{z-1}{z+1}$, with $\operatorname{Log}$ the principal branch on $\CC\setminus(-\infty,0]$, is holomorphic on $\CC\setminus[-1,1]$ with $F'=f$.

::: pf-proof
For $g(z)\coloneqq\frac{z-1}{z+1}$, $g(z)=t\le0$ if and only if $z=\frac{1+t}{1-t}\in[-1,1)$. So $F$ is holomorphic off $[-1,1]$, and $F'=\frac12\frac{g'}{g}=\frac12\qty(\frac1{z-1}-\frac1{z+1})=f$.
:::

:::

::: pf-step
(b) $\int_{\abs z=2}f\,dz=\boxed{0}$.

::: pf-proof
The circle $\abs z=2$ lies in $\CC\setminus[-1,1]$, where $f$ has the primitive $F$ of step [](#primitive){.pf-ref}, and the integral of a derivative over a closed curve is $0$.
:::

:::

:::

:::
