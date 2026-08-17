---
schema: qual/card@1
id: E-M5MWL
kind: exercise
title: "Primitive in the complement of a branch cut"
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - contour-integration
  - complex-logarithm
  - cauchy-integral-theorem
relations: []
review: draft
solved: true
---
:::{.exercise title="Primitive in the complement of a branch cut"}
Compute the following integrals:
\[
\int_{\abs{z-1} = 1} {1\over z^2-1} \dz \\
\int_{\abs{z-0} = 2} {1\over z^2-1} \dz \\
.\]
Compute the 2nd integral by finding a primitive.

:::

:::{.solution}
For the first integral:
\[
\int_\gamma{1\over z^2-1}\dz 
&= {1\over 2}\int_\gamma {1\over z-1} + {1\over z+1}\dz \\
&= {1\over 2}\int_\gamma {1\over z-1} \\
&= {1\over 2}\cdot 2\pi i \Res_{z=1}f(z) \\
&= {1\over 2}\cdot 2\pi i \cdot 1 \\
&= \pi i
,\]
using that $f(z) = {1\over z-1}$ is already an expansion of $f$ about $z=1$ since it is a Laurent series in $(z-1)^k$, so the residue is $1$.

For the second integral:
attempt to define a primitive
\[
F(z) \da {1\over 2}\log\qty{z-1\over z+1} \implies F'(z) = {1\over z^2-1}
.\]
If this primitive is well-defined on $\gamma$, the integral will vanish because this is a closed curve.
Choose the branch cut $\CC\sm(-\infty, 0]$ and define $g(z) = {z-1\over z+1}$, so that $F(z) = {1\over 2}\log(g(z))$.
Then then $g(z)\in (-\infty, 0] \iff z\in [-1, 1]$, and this is well-defined on $\gamma$ since $[-1, 1]$ does not intersect $\gamma$.

Thus for $\gamma$ any parameterization of $\abs{z} = 2$,
\[
\int_{\abs{z} = 2} f(z) \dz
= \int_{\abs{z} = 2} F'(z)\dz
= F(\gamma(0)) - F(\gamma(1))
= 0
.\]

:::

