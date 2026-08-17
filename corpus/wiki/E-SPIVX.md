---
schema: qual/card@1
id: E-SPIVX
kind: exercise
title: "$\\cos(x) / x^2 + b^2$"
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - contour-integration
  - integrals
relations: []
review: draft
solved: true
---
:::{.exercise title="$\cos(x) / x^2 + b^2$"}
\[
I \da \int_{0}^{\infty} \frac{\cos (x)}{x^{2}+b^{2}} d x=\frac{\pi \mathrm{e}^{-b}}{2 b}
.\]

:::

:::{.solution}
The integrand is even, so 
\[
I = \Re{1\over 2} \tilde I \da {1\over 2} \int_\RR {e^{iz} \over (z+ib)(z-ib)}
\]

Since $f \sim 1/x^2$, the ML estimate on a semicircular contour works:

![figures/2021-07-29_18-42-38.png](../../assets/figures/2021-07-29_18-42-38.png)

Then $\int_{C_R} f\to 0$ and $\int_{C_1} f\to \tilde I$.
Thus
\[
\tilde I 
&= 2\pi i \Res_{z=ib} \\
&= 2\pi i \lim_{z\to ib}{e^{iz}\over (z+ib)} \\
&= 2\pi i {e^{-b} \over 2i b} \\
&= {\pi e^{-b} \over b}
\]
and 
\[
I = \Re {1\over 2} \tilde I = {\pi e^{-b} \over 2b}
.\]

:::

