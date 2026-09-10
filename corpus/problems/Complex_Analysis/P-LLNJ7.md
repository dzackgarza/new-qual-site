---
schema: qual/card@1
id: P-LLNJ7
kind: problem
title: Integral of $f$ over a receding vertical segment equals $iAb$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Limits
relations: []
review: draft
---

::: problem
Assume $f$ is continuous in the region $\theset{x+iy \suchthat x\geq x_0, ~ 0\leq y \leq b}$, and the following limit exists uniformly with respect to $y$ (and is independent of $y$):
\[
\lim_{x\to +\infty}f(x+iy) = A
.\]

Show that if $\gamma_x \definedas \theset{z = x+it \suchthat 0 \leq t \leq b}$, then
\[
\lim_{x\to +\infty} \int_{\gamma_x} f(z) \,dz = iAb
.\]
:::

::: solution
Parametrize the vertical segment by
\[
z=x+it,
\qquad 0\le t\le b,
\qquad dz=i\,dt.
\]
Then
\[
\int_{\gamma_x}f(z)\,dz
=i\int_0^b f(x+it)\,dt.
\]
Since $f(x+iy)\to A$ uniformly for $0\le y\le b$,
\[
\sup_{0\le t\le b}|f(x+it)-A|\longrightarrow0.
\]
Therefore
\[
\begin{aligned}
\left|\int_{\gamma_x}f(z)\,dz-iAb\right|
&=\left|i\int_0^b\bigl(f(x+it)-A\bigr)\,dt\right|\\
&\le b\sup_{0\le t\le b}|f(x+it)-A|\longrightarrow0.
\end{aligned}
\]
Hence
\[
\lim_{x\to\infty}\int_{\gamma_x}f(z)\,dz=iAb.
\]
:::
