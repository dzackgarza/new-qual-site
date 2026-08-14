---
schema: qual/card@1
id: E-ZGZYQ
kind: exercise
title: "$\\sin(x)/x$ and $\\cos(x)/x$"
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - contour-integration
  - integrals
  - trigonometry
relations: []
review: draft
---
:::{.exercise title="$\sin(x)/x$ and $\cos(x)/x$"}
Compute
\[
I_1 \da \operatorname{PV}\int_\RR {\sin(x) \over x}\dx = \pi \\
I_2 \da \operatorname{PV}\int_\RR {\cos(x) \over x}\dx = 0 
.\]

:::

:::{.solution}
Take $\Gamma$ an upper-half-plane semicircular contour indented at the origin; considering $f(z) = e^{iz}$, by Jordan's lemma $\int_{C_R}f \to 0$ and the pieces along $\RR$ converge to $\PV \int f$.
The singularity at $z_0 = 0$ contributes a fractional residue:
\[
\int_{C_\eps}f(z)\dz \to i\pi \Res_{z=z_0} f(z) = i\pi \lim_{z\to 0} {(z-0) e^{iz}\over z} = i\pi \cdot 1
.\]
Thus
\[
I \da \PV \int_\RR f(z)\dz = 0 + i\pi \implies I_1 = \Im(I) = \pi, \quad I_2 = \Re(I) = 0
.\]
:::

