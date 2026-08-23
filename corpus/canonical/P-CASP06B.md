---
schema: qual/card@1
id: P-CASP06B
kind: problem
title: "Subharmonic function growth estimate and Liouville-type theorem"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
solved: false
---

::: problem
Suppose that $u$ is a $C^2$ subharmonic function on the whole complex plane.

(a) Prove that for any positive $R_1$ and $R_2$ with $R_2 > R_1$, $$\int_0^{2\pi} \left(u(R_2 e^{i\theta}) - u(R_1 e^{i\theta})\right)d\theta \geq \int_{R_1 \leq |z| \leq R_2} \log\left(\frac{R_2}{|z|}\right) \Delta u \, dx\,dy.$$

(b) Show that if $u$ satisfies $\lim_{z \to \infty} \frac{u(z)}{\log|z|} = 0$, then $u$ must be a constant.
:::
