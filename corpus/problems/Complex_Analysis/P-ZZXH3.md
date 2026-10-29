---
schema: qual/card@1
id: P-ZZXH3
kind: problem
title: The Fourier transform of a compactly supported continuous real function is
  entire
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Morera
  - Integrals
relations: []
review: draft
---

::: {.problem}
Suppose that $f: \RR\to\RR$ is a continuous function that vanishes outside of some finite interval.
For each $z\in \CC$, define
$$
g(z) = \int_{-\infty}^\infty f(t) e^{-izt} \,dt.
$$

Show that $g$ is entire.

:::

::: {.solution}
Let $f$ vanish outside $[-A,A]$, so $g(z)=\int_{-A}^Af(t)e^{-izt}\dt$.

::: pf

::: {.pf-step #cont}
$g$ is continuous on $\CC$.

::: pf-proof
The integrand $(z,t)\mapsto f(t)e^{-izt}$ is continuous on $\CC\times[-A,A]$, hence uniformly continuous on $K\times[-A,A]$ for each compact $K\subset\CC$, and integration over the bounded interval $[-A,A]$ preserves continuity in $z$.
:::

:::

::: {.pf-step #morera}
$\oint_T g(z)\dz=0$ for every triangle $T\subset\CC$.

::: pf-proof
The integrand is continuous on the compact set $T\times[-A,A]$, so Fubini's theorem applies:
$$
\oint_T g(z)\dz=\int_{-A}^A f(t)\qty(\oint_T e^{-izt}\dz)\dt=0,
$$
since $z\mapsto e^{-izt}$ is entire and Goursat's theorem makes the inner integral vanish.
:::

:::

::: pf-step
$g$ is entire.

::: pf-proof
By steps [](#cont){.pf-ref} and [](#morera){.pf-ref} and Morera's theorem.
:::

:::

:::

:::
