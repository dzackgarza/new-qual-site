---
schema: qual/card@1
id: P-6SR5N
kind: problem
title: $\int_0^{2\pi}\frac{1}{a+\cos\theta}\,d\theta=\frac{2\pi}{\sqrt{a^2-1}}$ for
  $a>1$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Trigonometry
relations: []
review: draft
---

:::{.problem title="?"}
Show 
\[
\int_0^{2\pi} {1\over a + \cos(\theta)} \dtheta = {2\pi \over \sqrt{a^2-1}}, && a> 1
.\]
:::

:::{.solution}
Sketch:

- Set $z=e^{i\theta}$ to get
\[
\frac{2}{i} \int_{|z|=1} \frac{\mathrm{d} z}{z^{2}+2 a z+1}
.\]

- Factor into two roots $r_1, r_2$.
  Use that without loss of generality, $r_1\in \DD$ and $r_2\in \DD^c$, with neither on $S^1$ to compute the residue $4\pi/(r_1 -r_2)$ 

:::



