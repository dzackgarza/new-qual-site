---
schema: qual/card@1
id: P-PSIBT
kind: problem
title: $\int_0^\infty\frac{\log x}{1+x^3}\,dx$
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
Compute the following integral carefully justifying each step:

\[
\int_{0}^{\infty} \frac{\log x}{1+x^{3}} \text {. }
\]
:::

::: {.solution}
For $0<s<3$, set
\[
I(s)=\int_0^\infty\frac{x^{s-1}}{1+x^3}\,dx.
\]
With $u=x^3$, so that $x=u^{1/3}$ and
$dx=\frac13u^{-2/3}\,du$, we obtain
\[
I(s)=\frac13\int_0^\infty\frac{u^{s/3-1}}{1+u}\,du.
\]
The Euler beta integral gives, for $0<s<3$,
\[
I(s)=\frac\pi3\csc\left(\frac{\pi s}{3}\right).
\]

On every compact subinterval of $(0,3)$, differentiation under the integral
sign is justified by domination near $0$ and $\infty$. Therefore
\[
I'(s)=\int_0^\infty\frac{x^{s-1}\log x}{1+x^3}\,dx.
\]
At $s=1$ this is the desired integral. Differentiating the closed formula,
\[
I'(s)
=-\frac{\pi^2}{9}
\csc\left(\frac{\pi s}{3}\right)
\cot\left(\frac{\pi s}{3}\right).
\]
Hence
\[
\int_0^\infty\frac{\log x}{1+x^3}\,dx
=-\frac{\pi^2}{9}
\cdot\frac{2}{\sqrt3}\cdot\frac1{\sqrt3}
=\boxed{-\frac{2\pi^2}{27}}.
\]
:::
