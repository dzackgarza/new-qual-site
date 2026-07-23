---
schema: qual/card@1
id: E-S6EOX
kind: exercise
title: "$x^\\alpha/(x+1)^2$"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="$x^\alpha/(x+1)^2$"}
\[
I \da \int_0^\infty {x^\alpha \over (x+1)^2}\dx && 0 < \alpha < 2
.\]

#complex/exercise/completed

:::

:::{.solution title="Keyhole contour"}
Note the single pole of order 2 at $z=-1$, and also the branch singularity.
Choose a branch cut of $\log$ by deleting $\theta=0$, and take a keyhole contour.

![Keyhole contour](../../assets/30_Complex_Analysis/040_Residues/figures/2021-12-24_04-00-31.png)

Write the contours as 

- $\gamma_\eps = \ts{\eps e^{it} \st t\in[0+\eps, 2\pi - \eps]}$
- $\gamma_+ = \ts{x+i\eps \st x\in [\eps, R]}$
- $\gamma_R = \ts{Re^{it} \st t\in [0+\eps, 2\pi - \eps]}$
- $\gamma_- = \ts{x-i\eps \st t\in [\eps, R]}$,

all oriented so that the total curve $\Gamma$ is traversed counter-clockwise.

The claim is that $\int_{\gamma_\eps} f, \int_{\gamma_R} f\to 0$, and $\int_{\gamma_+} f$ is a multiple of $\int{\gamma_-} f$. 
For $z=x-i\eps$ on $\gamma_-$, we have
\[
\log(z) = \log(x-i\eps) = \ln\abs{x-i\eps} + i\Arg(x-i\eps)\convergesto{\eps\to 0} \ln\abs{x} + 2\pi i = e^{2\pi i}z
,\]
and 
\[
f(e^{2\pi i}z) = {(e^{2\pi i}z)^\alpha \over ((e^{2\pi i}z)^2+1)^2 } = e^{2\pi i\alpha } {z \over z^2+1} = e^{2\pi i\alpha}f(z)
.\]
Thus
\[
\int_{\gamma_-} f(z)\dz 
&\too \int_R^\eps f(e^{2\pi i }z)\dz \\
&= \int_R^\eps e^{2\pi i \alpha}f(z)\dz \\
&= -e^{2\pi i \alpha}\int_\eps^R f(z)\dz \\
&= -e^{2\pi i\alpha}\int_{\gamma_+}f(z)\dz
.\]

Thus in the limit,
\[
2\pi i \sum_{z_k\in \CC\sm\RR_{\geq 0}} \Res_{z=z_k}f(z) 
&= \int_\Gamma f(z)\dz \\
&= \int_{\gamma_+}f(z)\dz + \int_{\gamma_-}f(z)\dz \\
&= (1-e^{2\pi i\alpha})\int_{\gamma_+}f(z)\dz \\
&= (1-e^{2\pi i\alpha})\int_{\RR}f(z)\dz \\
.\]

Computing the residue at $z_0 = -1$:
\[
\Res_{z=-1}f(z) 
&= \lim_{z\to -1} \dd{}{z} (z+1)^2 f(z) \\
&= \lim_{z\to -1} \dd{}{z} z^\alpha \\
&= \alpha (-1)^{\alpha - 1} \\
&= \alpha e^{i\pi(\alpha - 1)} \\
&= -\alpha e^{i\pi \alpha}
.\]
Thus
\[
\int_\RR f(z) \dz 
&= 2\pi i \cdot {-\alpha e^{i\pi \alpha}\over 1 - e^{2\pi i \alpha}} \\
&=-2\pi i \alpha {1\over e^{-i\pi\alpha} (1- e^{2\pi i \alpha})} \\
&=-2\pi i \alpha {1\over e^{-i\pi\alpha} - e^{i\pi\alpha}} \\
&=2\pi i \alpha {1\over e^{-i\pi\alpha} - e^{-i\pi\alpha}} \\
&= \pi \alpha \csc(\pi\alpha)
.\]

:::

