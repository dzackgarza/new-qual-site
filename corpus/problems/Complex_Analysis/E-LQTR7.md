---
schema: qual/card@1
id: E-LQTR7
kind: problem
title: Schwarz reflection principle on a half-disk
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Reflection
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $S\coloneqq \theset{z\in \DD\suchthat \Im(z) \geq 0}$.
Suppose $f:S\to \CC$ is continuous on $S$, real on $S\intersect \RR$, and holomorphic on $S^\circ$.

Prove that $f$ is the restriction of a holomorphic function on $\DD$.

:::

::: {.solution}
Define $F:\DD\to\CC$ by $F(z)\coloneqq f(z)$ for $\Im z\ge0$ and $F(z)\coloneqq\overline{f(\bar z)}$ for $\Im z<0$.

::: pf

::: {.pf-step #lower}
$F$ is holomorphic on $\theset{z\in\DD\st\Im z<0}$.

::: pf-proof
Let $\Im w_0<0$, so $z_0\coloneqq\bar w_0\in S^\circ$ and $f(z)=\sum_{k\ge0}c_k(z-z_0)^k$ near $z_0$. For $z$ near $w_0$, $\bar z$ is near $z_0$ and
$$
\overline{f(\bar z)}=\sum_{k\ge0}\overline{c_k}\,\overline{(\bar z-z_0)}^{\,k}=\sum_{k\ge0}\overline{c_k}(z-w_0)^k,
$$
a power series about $w_0$.
:::

:::

::: {.pf-step #continuous}
$F$ is continuous on $\DD$.

::: pf-proof
$F$ is continuous on each closed half of $\DD$, and the two definitions agree on $\DD\cap\RR$ because $f$ is real there: $\overline{f(\bar x)}=\overline{f(x)}=f(x)$.
:::

:::

::: {.pf-step #morera}
$\int_{\partial T}F\,dz=0$ for every closed triangle $T\subset\DD$.

::: pf-proof
If $T$ lies in one closed half-disk, take triangles $T_\varepsilon$ in the open half-disk with $T_\varepsilon\to T$; $\int_{\partial T_\varepsilon}F=0$ by Goursat's theorem and steps [](#lower){.pf-ref}, and the integrals converge because $F$ is uniformly continuous on compact sets by step [](#continuous){.pf-ref}. A triangle that meets both halves is cut by $\RR$ into at most three triangles, each in one closed half-disk, and the integrals over the cut segments cancel.
:::

:::

::: pf-step
$F$ is holomorphic on $\DD$ and $F|_S=f$.

::: pf-proof
Morera's theorem applies to $F$ by steps [](#continuous){.pf-ref} and [](#morera){.pf-ref}; $F=f$ on $S$ by definition.
:::

:::

:::

:::
