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

::: {.problem}
Assume $f$ is continuous in the region $\theset{x+iy \suchthat x\geq x_0, ~ 0\leq y \leq b}$, and the following limit exists uniformly with respect to $y$ (and is independent of $y$):
$$
\lim_{x\to +\infty}f(x+iy) = A.
$$

Show that if $\gamma_x \definedas \theset{z = x+it \suchthat 0 \leq t \leq b}$, then
$$
\lim_{x\to +\infty} \int_{\gamma_x} f(z) \,dz = iAb.
$$
:::

::: {.solution}
::: pf

::: {.pf-step #parametrize}
$\int_{\gamma_x}f(z)\,dz = i\int_0^b f(x+it)\,dt$.

::: pf-proof
Parametrize $\gamma_x$ by $z=x+it$, $0\le t\le b$, so $dz=i\,dt$.
:::

:::

::: pf-step
$\lim_{x\to+\infty}\int_{\gamma_x}f(z)\,dz=iAb$.

::: pf-proof
By step [](#parametrize){.pf-ref},
$$
\abs{\int_{\gamma_x}f(z)\,dz-iAb}
=\abs{i\int_0^b\bigl(f(x+it)-A\bigr)\,dt}
\le b\sup_{0\le t\le b}\abs{f(x+it)-A}.
$$
Uniform convergence $f(x+iy)\to A$ for $0\le y\le b$ means exactly that the supremum tends to $0$ as $x\to+\infty$.
:::

:::

:::
:::
