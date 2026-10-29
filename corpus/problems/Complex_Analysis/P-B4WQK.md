---
schema: qual/card@1
id: P-B4WQK
kind: problem
title: Continuous on $\CC$ and holomorphic off $\RR$ implies entire
classification:
  areas:
  - complex-analysis
  topics:
  - Morera
  - Schwarz Reflection
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Suppose that $f: \CC\to\CC$ is continuous everywhere and analytic on $\CC\setminus \RR$ and prove that $f$ is entire.
:::

::: {.hint}
Take a disc $D$ centered at a point of $\RR$ and show $f$ is holomorphic in $D$ by Morera's theorem.
:::

::: {.solution}

Let $D$ be an open disc centered at a point of $\RR$.
By Morera's theorem it suffices to show $\int_{\partial\Delta}f=0$ for every closed triangle $\Delta\subset D$.

::: pf

::: {.pf-step #off-axis}
If $\Delta\cap\RR=\emptyset$, then $\int_{\partial\Delta}f=0$.

::: pf-proof
$\Delta$ lies in the convex set $D\cap\{\Im z>0\}$ or $D\cap\{\Im z<0\}$, on which $f$ is holomorphic, so Goursat's theorem applies.
:::

:::

::: {.pf-step #touching}
If $\Delta$ meets $\RR$ and lies in $\{\Im z\ge0\}$ (or in $\{\Im z\le0\}$), then $\int_{\partial\Delta}f=0$.

::: pf-proof
Treat $\Im z\ge0$; the other case is symmetric.
For small $\varepsilon>0$ the translate $\Delta_\varepsilon\coloneqq\Delta+i\varepsilon$ lies in $D\cap\{\Im z>0\}$, so $\int_{\partial\Delta_\varepsilon}f=0$ by step [](#off-axis){.pf-ref}.
Parametrize $\partial\Delta$ by a piecewise smooth $\gamma:[a,b]\to\CC$ with $\abs{\gamma'}\le M$; then
$$
\abs{\int_{\partial\Delta_\varepsilon}f-\int_{\partial\Delta}f}
\le\int_a^b\abs{f(\gamma(t)+i\varepsilon)-f(\gamma(t))}\,\abs{\gamma'(t)}\,dt
\le M(b-a)\sup_{t}\abs{f(\gamma(t)+i\varepsilon)-f(\gamma(t))}.
$$
$f$ is uniformly continuous on a compact neighborhood of $\partial\Delta$, so the right side tends to $0$ as $\varepsilon\to0$, and $\int_{\partial\Delta}f=0$.
:::

:::

::: pf-step
$\int_{\partial\Delta}f=0$ for every closed triangle $\Delta\subset D$.

::: pf-proof
If $\Delta$ meets both open half-planes, the real axis cuts $\Delta$ into at most three triangles, each lying in a closed half-plane.
The integral over $\partial\Delta$ is the sum of the integrals over their boundaries, because the added edges are traversed in opposite directions, and each summand vanishes by step [](#off-axis){.pf-ref} or step [](#touching){.pf-ref}.
:::

:::

::: pf-step
$f$ is entire.

::: pf-proof
By Morera's theorem $f$ is holomorphic on each such disc $D$, and $f$ is holomorphic off $\RR$ by hypothesis.
:::

:::

:::

:::

::: {.remark}
The proof of holomorphicity across the line is the same argument that proves the Schwarz reflection theorem.
:::
