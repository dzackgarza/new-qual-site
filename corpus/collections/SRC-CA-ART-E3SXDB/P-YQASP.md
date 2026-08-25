---
schema: qual/card@1
id: P-YQASP
kind: problem
title: $\lim_{x\to+\infty}\int_{\gamma_x}f=iAb$ when $f(x+iy)\to A$ independently
  of $y$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Limits
relations: []
review: draft
---

:::{.problem}
Assume $f$ is continuous in the region $\theset{x+iy \suchthat x\geq x_0, ~ 0\leq y \leq b}$, and the following limit exists independent of $y$:
\[
\lim_{x\to +\infty}f(x+iy) = A
.\]

Show that if $\gamma_x \definedas \theset{z = x+it \suchthat 0 \leq t \leq b}$, then
\[
\lim_{x\to +\infty} \int_{\gamma_x} f(z) \,dz = iAb
.\]
:::

:::{.solution}
The key insight:
\[
\int_\gamma A \dz 
&= \int_0^b A \cdot i \dt && z=x+it,\, \dz = i\dt \\
&=iA \int_0^b \dt \\
&= iAb
.\]

So now estimate the difference:
\[
\abs{
\int_{\gamma} f(z) \dz - iAb
}
&= \abs{ \int_\gamma f(z) \dz - \int_\gamma A \dz} \\
&= \abs{ \int_\gamma \qty{ f(z) - A } \dz} \\
&\leq\int_\gamma \abs{ f(z) - A } \dz \\
&\leq \sup_{z = x+iy\in \gamma} \abs{f(x+iy) - A} \cdot \length(\gamma_x) \\
&\convergesto{x\to \infty}0
,\]
using that $\length(\gamma_x) = b$ is constant.
:::
