---
schema: qual/card@1
id: P-P5VOR
kind: problem
title: $\int_0^\infty\frac{x^{a-1}}{1+x^3}\,dx$ for $0<a<3$
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

:::{.problem title="?"}
Let $a \in \mathbb{R}$ with $0<a<3$. Evaluate 
\[
\int_{0}^{\infty} \frac{x^{a-1}}{1+x^{3}} d x
.\]

:::

:::{.solution}
Write $I$ for the integral, $\zeta_3\da e^{2\pi i\over 3}, \omega_3 \da e^{i\pi\pver 3}$.
Take a indented semicircular wedge $\Gamma$ at an angle of $2\pi/3$, noting the pole at $\omega_3 \da e^{i \pi \over 3}$:

![](../../assets/30_Complex_Analysis/999_Quals/figures/2021-12-30_06-01-59.png)

Choosing a branch cut of $\log$ along $\theta = -\pi/2$, so $\arg(z) \in (-\pi/2, 3\pi/2)$, this makes $f(z) \da z^{\alpha-1}/(1+z^3)$ meromorphic on $\Gamma$.

By the ML estimate, the integrals along $C_\eps, C_R$ will vanish in the limit.

The contribution from the contour: parameterize $\gamma_2$ as $\ts{\zeta_3 t\st t\in [\eps, R]}$, then
\[
\int_{\gamma_2}f(z) \dz 
&= \int_R^\eps {(\zeta_3 t)^{\alpha - 1} \over 1 + (\zeta_3 t)^3} \zeta_3\dt \\
&= \zeta_3 \zeta_3^{\alpha-1}\int_R^\eps {t^{\alpha-1} \over 1 + t^3}\dt \\
&\to -\zeta_3^\alpha I
,\]
so the total contribution is 
\[
\oint_\Gamma f \to \qty{\int_{\gamma_1} + \int_{\gamma_2}}f = (1-\zeta_3^{\alpha}) I
.\]

Computing the contributions from residues:
\[
\Res_{z=\omega_3} f(z) 
&= \lim_{z\to \omega_3} {(z-\omega_3) z^{\alpha-1} \over 1+z^3} \\
&\eqLH \lim_{z\to\omega_3} {z^{\alpha-1} \over 3z^2} \\
&= {1\over 3} \omega_3^{\alpha-3} \\
&= -{1\over 3}\omega_3^\alpha
.\]

Combining it all using the residue theorem:
\[
2\pi i \Res_{z=\omega_3} f(z) &= \oint_\gamma f \\
\implies I 
&= {-2\pi i\over 3} {\omega_3^\alpha \over 1-\zeta_3^\alpha } \\
&= {-2\pi i\over 3} {1 \over \omega_3^{-\alpha} - \omega_3^\alpha } \\
&= {-2\pi i\over 3} {1 \over -2i\sin\qty{\pi\alpha\over 3} } \\
&= {\pi\over 3}\csc\qty{\alpha\pi\over 3}
.\]


:::

