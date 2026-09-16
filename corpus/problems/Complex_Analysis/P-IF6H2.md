---
schema: qual/card@1
id: P-IF6H2
kind: problem
title: $\int_0^\infty\frac{x^{a-1}}{1+x^n}\,dx$ for $0<a<n$ and $\int_0^\infty\frac{\log
  x}{(1+x^2)^2}\,dx$
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

::: {.problem}
Compute the following integrals:

- $\displaystyle \int_0^\infty \frac{x^{a-1}}{1 + x^n} \, dx$, $0< a < n$

- $\displaystyle \int_0^\infty \frac{\log x}{(1 + x^2)^2}\, dx$
:::

::: {.solution}
For
\[
I(a,n)=\int_0^\infty\frac{x^{a-1}}{1+x^n}\,dx,
\qquad 0<a<n,
\]
put $u=x^n$. Then
\[
I(a,n)=\frac1n\int_0^\infty\frac{u^{a/n-1}}{1+u}\,du.
\]
For $0<s<1$, a keyhole-contour evaluation of
$z^{s-1}/(1+z)$ gives
\[
\int_0^\infty\frac{u^{s-1}}{1+u}\,du
=\pi\csc(\pi s).
\]
Taking $s=a/n$ yields
\[
\boxed{
\int_0^\infty\frac{x^{a-1}}{1+x^n}\,dx
=\frac\pi n\csc\frac{\pi a}{n}.}
\]

For the second integral, let
\[
J=\int_0^\infty\frac{\log x}{(1+x^2)^2}\,dx.
\]
Under $x=1/t$,
\[
J=-\int_0^\infty\frac{t^2\log t}{(1+t^2)^2}\,dt.
\]
Adding this to the original expression gives
\[
2J=\int_0^\infty
\log x\,\frac{1-x^2}{(1+x^2)^2}\,dx.
\]
Since
\[
\frac{d}{dx}\frac{x}{1+x^2}
=\frac{1-x^2}{(1+x^2)^2},
\]
integration by parts gives
\[
2J
=\left[\log x\frac{x}{1+x^2}\right]_0^\infty
-\int_0^\infty\frac{dx}{1+x^2}
=-\frac\pi2.
\]
The boundary term vanishes at both endpoints. Therefore
\[
\boxed{J=-\frac\pi4}.
\]
:::
