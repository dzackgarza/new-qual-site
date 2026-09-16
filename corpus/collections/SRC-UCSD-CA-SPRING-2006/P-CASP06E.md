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
Here “linear transformation” is understood in the classical complex-analysis
sense of a linear fractional (Möbius) transformation.

Let the first pair be the boundary circles of the annulus
\[
A(r,R)=\{r<|z-a|<R\},\qquad 0<r<R,
\]
and let the image pair bound
\[
A(r',R')=\{r'<|w-b|<R'\}.
\]
The Möbius transformation restricts to a conformal equivalence between these
annuli, possibly interchanging the two boundary components.

The conformal modulus of a round annulus is
\[
\operatorname{mod}A(r,R)=\frac1{2\pi}\log\frac{R}{r},
\]
and conformal equivalences preserve modulus. Hence
\[
\log\frac{R}{r}=\log\frac{R'}{r'},
\]
so
\[
\boxed{\frac{R}{r}=\frac{R'}{r'}}.
\]

If the transformation interchanges the two boundary circles, the unordered
ratio is unchanged, giving the same conclusion.
:::
