---
schema: qual/card@1
id: E-FJJA6
kind: problem
title: $\int_0^\infty\frac{\log x}{1+x^2}\,dx$
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

::: {.exercise}
\[
I \definedas \int_0^\infty {\log(x) \over 1+x^2}\dx = 0
.\]

:::

::: {.solution}
The integrand $1/(1+x^2)$ is even, so the negative real axis contributes $I$ plus a multiple of $\int_0^\infty dx/(1+x^2)$. Take a branch cut for $\log$ along $\theta = -\pi/2$ and the upper semicircle of radius $R$ indented at $0$ by a semicircle of radius $\eps$:

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-22_05-21-05.png)

For $f(z) \definedas {\log(z) \over z^2 + 1}$, the large arc contributes $O\qty{(\log R)/R}$ and the small arc $O\qty{\eps\abs{\log\eps}}$, so only the horizontal contours contribute as $R\to \infty$ and $\eps\to 0$.
Parameterize, oriented counterclockwise:

- $\gamma_1 \definedas \theset{t+0i \st t\in [\eps, R]}$
- $\gamma_2 \definedas \theset{t+0i \st t\in [-\eps, -R]}$

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
2\pi i \Res_{z=i}f(z) = \lim\int_{\Gamma}f(z) \dz = \lim\qty{ \int_{\gamma_1} + \int_{\gamma_2}}f = 2I + {i\pi^2 \over 2} \\
\implies 2\pi i \cdot {\pi \over 4} = 2I + {i\pi^2\over 2} \\
\implies {i\pi^2\over 2} = 2I + {i\pi^2\over 2} \\
\implies I = 0
.\]

:::

