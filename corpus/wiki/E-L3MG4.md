---
schema: qual/card@1
id: E-L3MG4
kind: exercise
title: $\sqrt{x^2-1}$
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
solved: true
---

:::{.exercise title="$\sqrt{x^2-1}$ "}
\[
I\da \int_{-1}^1 \sqrt{1-x^2} \dx = {\pi \over 2}
.\]

:::

:::{.solution title="Dogbone and residue at $\infty$"}
Take a branch cut $[-1, 1]$ and $\Gamma$ the standard dogbone contour:

![](../../assets/30_Complex_Analysis/040_Residues/figures/2021-12-28_01-50-50.png)

Orient $\Gamma$ positively about *infinity*, i.e. counterclockwise.

Contribution from $\gamma_1 \da\ts{t+i\eps \st t\in [-1, 1]}$, the upper horizontal piece:
\[
\int_{\gamma_1}f(z)\dz \to \int_{-1}^1 \sqrt{1-t^2} \dt = I
.\]

Contribution from $\gamma_2\da\ts{t-i\eps \st t\in [-1, 1]}$, the lower horizontal piece:
note that following $e^{2\pi i t}z$ to $t=1$ sends $\sqrt{z}$ to $-\sqrt{z}$, so
\[
\int_{\gamma_2}f(z)\dz \to \int_{1}^{-1} - \sqrt{1-t^2} \dt = I
.\]

Contributions from the circles: use that $f(z) \da \sqrt{z^2-1}$ is a continuous function and these arcs are compact, so they are uniformly bounded.
Thus $\int f\to 0$ by the ML estimate on these arcs.

The total contribution:
\[
\qty{\int_{\gamma_1} + \int_{\gamma_2}} f = 2I
.\]

The residue at infinity:
\[
\Res_{z=\infty}f(z) 
&= \Res_{z=0} - {1\over z^2}\sqrt{1 - {1\over z^2}} \\
&= \Res_{z=0} - {1\over z^2}\sqrt{z^2-1 \over z^2} \\
&= \Res_{z=0} - {i\over z^3}\sqrt{1-z^2} \\
&= \Res_{z=0} - {i\over z^3}\sum_{k\geq 0} {1/2\choose k}z^{2k} \\
&= \Res_{z=0} - {i\over z^3} \qty{1 - {1\over 2}z^2 - \bigo(z^3) } \\
&= {i\over 2}
,\]
thus
\[
2\pi i \cdot -{i\over 2} = 2I \implies I = {\pi \over 2}
.\]
:::

