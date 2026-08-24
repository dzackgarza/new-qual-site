---
schema: qual/card@1
id: P-LHZGV
kind: problem
title: Log properties can fail
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Logarithm
  - Counterexamples
relations: []
review: draft
---

:::{.exercise title="Log properties can fail"}
Show that

- $\log(zw)\neq \log(z)\log(w)$
- $\log(\exp(z))\neq z$

:::

:::{.solution}
Counterexamples: 

- Take $z=\zeta_4^3$ and $w=\zeta_4^2$, noting that $\Arg(z) = {3\pi \over 4}$ and $\Arg(w) = {\pi \over 2}$
  Then $zw = e^{5\pi \over 4}$ but $\Arg(zw) = {-3\pi \over 4}$ because we are forced to use the domain $(-\pi, \pi]$.

- Showing that $\log(\exp(z))$ is a countably infinite set in $\CC$:
\[
\log(\exp(z)) 
&= \log(\exp(x+iy)) \\
&= \ln\qty{e^x} + (y+2k\pi)i \\
&= (x+iy) + 2k\pi i \\
&= z + 2k\pi
.\]

:::
