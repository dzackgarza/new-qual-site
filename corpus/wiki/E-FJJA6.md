---
schema: qual/card@1
id: E-FJJA6
kind: exercise
title: $\log(x)/1+x^2$
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

:::{.exercise title="$\log(x)/1+x^2$"}
\[
I \da \int_0^\infty {\log(x) \over 1+x^2}\dx = 0
.\]

:::

:::{.solution title="Semicircle, real reduction trick"}
Noting the partial $\zeta_2 = -1$ symmetry, take a branch cut for $\log$ along $\theta = -\pi/2$ and the following semicircular contour:

![](../../assets/30_Complex_Analysis/040_Residues/figures/2021-12-22_05-21-05.png)

Since $f(z) \da {\log(z) \over z^2 + 1}$ goes to zero as $\abs{R}\to \infty$ and $\eps\to 0$, only the horizontal contours will contribute.
Parameterize, oriented counterclockwise:

- $\gamma_1 \da \ts{t+0i \st t\in [\eps, R]}$
- $\gamma_2 \da \ts{t+0i \st t\in [-\eps, -R]}$

Then $\int_{\gamma_1} f(z)\dz \to I$. 
Computing the contribution from $\gamma_2$:
\[
\int_{\gamma_2} f(z) \dz 
&= \int_{-R}^{-\eps} f(t) \dt \qquad z=t+0i, \dz=\dt \\
&= \int_{-R}^{-\eps} {\log(t) \over t^2 + 1}\dt \\
&= -\int_{R}^{\eps} {\log(-x) \over (-x)^2 + 1 }\dx \qquad t=-x, \dt = -\dx \\
&= \int_{\eps}^{R} {\log(x) + i\pi \over x^2 + 1 }\dx  \\
&= I + i\pi \cdot {\pi \over 2} \\
&= I + {i\pi^2\over 2}
,\]
using the known antiderivative $\arctan$.

Note that there are two simple poles at $\pm i$, so only the residue at $z_0=i$ contributes:
\[
\Res_{z=i} = \lim_{z\to i} {\log(z) \over (z+i)} = {\log(i) \over 2i} = {i\pi/2 \over 2i} = {\pi \over 4}
,\]
so by the residue theorem,
\[
2\pi i \Res_{z=i}f(z) = \int_{\Gamma}f(z) \dz = \qty{ \int_{\gamma_1} + \int{\gamma_2}}f = 2I + {i\pi^2 \over 2} \\
\implies 2\pi i \cdot {\pi \over 4} = I + {i\pi^2\over 2} \\
\implies {i\pi^2\over 4} = I + {i\pi^2\over 4} \\
\implies I = 0
.\]

:::

