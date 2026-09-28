---
schema: qual/card@1
id: P-DFHS3
kind: problem
title: $\int_0^\infty\frac{dx}{(1+x^2)(1+9x^2)}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
---

::: {.problem}
Calculate
\[
\int_0^\infty {dx \over (1+x^2)(1+9x^2)}
.\]
:::

::: {.solution}
Use the rational function
\[
F(z)={1\over(1+z^2)(1+9z^2)}
\]
and integrate over the upper semicircle of radius $R>1$. The arc integral
tends to $0$ because $F(z)=O(|z|^{-4})$.

The poles in the upper half-plane are $z=i$ and $z=i/3$. Their residues are
\[
\Res_{z=i}F
={1\over(2i)(1-9)}={i\over16},
\]
and
\[
\Res_{z=i/3}F
={1\over(1-1/9)(6i)}=-{3i\over16}.
\]
Thus
\[
\int_{-\infty}^{\infty}{dx\over(1+x^2)(1+9x^2)}
=2\pi i\left({i\over16}-{3i\over16}\right)
={\pi\over4}.
\]
The integrand is even, so
\[
\boxed{
\int_0^\infty {dx\over(1+x^2)(1+9x^2)}={\pi\over8}.}
\]
:::
