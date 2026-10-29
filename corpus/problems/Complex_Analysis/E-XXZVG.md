---
schema: qual/card@1
id: E-XXZVG
kind: problem
title: Uniform limit theorem for holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Morera
  - Uniform Convergence
  - Sequences of Functions
  - Holomorphic Functions
relations: []
review: draft
---

::: {.exercise}
Prove the uniform limit theorem for holomorphic functions: if $f_n\to f$ locally uniformly and each $f_n$ is holomorphic then $f$ is holomorphic.
:::

::: {.solution}
Let $\Omega$ be the open set on which the $f_n$ are holomorphic and $f_n\to f$ locally uniformly.
Holomorphy is local, so fix an open disc $D$ with $\bar D\subset\Omega$; it suffices to show $f$ is holomorphic on $D$.

::: pf

::: {.pf-step #continuous}
$f_n\to f$ uniformly on $\bar D$, and $f$ is continuous on $D$.

::: pf-proof
$\bar D$ is compact, so it is covered by finitely many neighbourhoods on which the convergence is uniform; a uniform limit of continuous functions is continuous.
:::

:::

::: {.pf-step #triangles}
$\int_{\partial T} f = 0$ for every closed triangle $T\subset D$.

::: pf-proof
By Goursat's theorem, $\int_{\partial T} f_n = 0$.
By step [](#continuous){.pf-ref}, $\abs{\int_{\partial T}(f_n - f)} \le \sup_{\bar D}\abs{f_n-f}\cdot L(\partial T)\to0$.
:::

:::

::: pf-step
$f$ is holomorphic on $D$.

::: pf-proof
By steps [](#continuous){.pf-ref} and [](#triangles){.pf-ref}, Morera's theorem applies on $D$.
:::

:::

:::

:::
