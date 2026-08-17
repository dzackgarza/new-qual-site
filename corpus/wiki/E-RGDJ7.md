---
schema: qual/card@1
id: E-RGDJ7
kind: exercise
title: "Cauchy formula and $\\sinh$"
classification:
  areas:
  - complex-analysis
  topics:
  - cauchy-integral-formula
  - contour-integration
  - hyperbolic-functions
relations: []
review: draft
solved: true
---
:::{.exercise title="Cauchy formula and $\sinh$"}
Compute
\[
\int_{S^1} {2 \sinh(z) \over z^n}\dz
.\]

:::

:::{.solution}
Write $f(z) = 2\sinh(z) = e^{z} - e^{-z}$ and apply the generalized Cauchy formula:
\[
f^{(n-1)}(0) 
&= {(n-1)! \over 2\pi i} \int_{S^1} {f(z) \over (z-0)^n}\dz \\ \\
\implies \int_{S^1}{f(z)\over z^n}\dz 
&= {2\pi i \over (n-1)!} f^{(n-1)}(0) \\
&= {2\pi i\over (n-1)!} 2\cdot \qty{e^z - (-1)^{n-1} e^z \over 2}\evalfrom_{z=0} \\
&= {2\pi i\over (n-1)!} 2\cdot \qty{1 + (-1)^{n} \over 2} \\
&=
\begin{cases}
{2\pi i \over (n-1)!} & n \text{ even } 
\\
0 & n \text{ odd }.
\end{cases}
.\]
:::

