---
schema: qual/card@1
id: P-L52MJ
kind: problem
title: $\int_\Delta f=0$ for triangles when $f$ is holomorphic off one point and bounded nearby
classification:
  areas:
  - complex-analysis
  topics:
  - removable-singularities
  - morera
  - contour-integration
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Let $f(z)$ be analytic in an open set $\Omega$ except possibly at a
point $z_0$ inside $\Omega$. Show that if $f(z)$ is bounded in near
$z_0$, then $\displaystyle \int_\Delta f(z) dz = 0$ for all triangles
$\Delta$ in $\Omega$.
:::

:::{.solution}
Write $\DD_\eps(z_0)$ for a disc in which $f$ is bounded, say by $\abs{f}\leq M$ here.
Note that if $z_0$ is not in the region enclosed by $\Delta$, then $\int_\Delta f = 0$ since $f$ is holomorphic throughout $\Delta$, so suppose $z_0$ is in this region.

Since $f$ is holomorphic in $\Omega\smts{z_0}$, $\Delta$ can be deformed to $\bd \DD_\eps(z_0)$ without changing the integral. 
So
\[
\abs{ \oint_\Delta f } 
&= \abs{\oint_{\bd\DD_\eps(z_0)} f } \\
&\leq \oint_{\bd \DD_\eps(z_0)} \abs{f} \\
&\leq \oint_{\bd \DD_\eps(z_0)} M \\
&= M\cdot 2\pi \eps \\
&\convergesto{\eps\to 0} 0
,\]
noting that the bound $M$ is constant and remains an upper bound on smaller discs by the maximum modulus principle.
:::

