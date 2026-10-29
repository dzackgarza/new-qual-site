---
schema: qual/card@1
id: P-SWILN
kind: problem
title: Analyticity of $\int_\gamma \frac{g(w)}{w-z}\,dw$ on $\CC\setminus\gamma$
classification:
  areas:
  - complex-analysis
  topics:
  - Morera
  - Holomorphic Functions
  - Contour Integration
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The source does not say what g is. The statement now assumes g is continuous on gamma, which is the hypothesis the Morera argument uses.'
---

::: {.problem}
Let $\gamma$ be a smooth curve joining two distinct points $a, b\in \CC$, and let $g$ be continuous on $\gamma$.

Prove that the function
$$
f(z) \definedas \int_\gamma {g(w) \over w-z} \,dw
$$
is analytic in $\CC\setminus\gamma$.
:::

::: {.solution}
The set $\CC\setminus\gamma$ is open because $\gamma$ is compact. Fix an open disk $D\subset\CC\setminus\gamma$.

::: pf

::: {.pf-step #cont}

$f$ is continuous on $D$.

::: pf-proof

For $z_0\in D$ choose a closed disk $K\subset D$ around $z_0$. The function $(z,w)\mapsto g(w)/(w-z)$ is continuous on the compact set $K\times\gamma$, hence uniformly continuous there, so $f$ is continuous on $K$.

:::

:::

::: {.pf-step #morera}

$\oint_{\partial T}f(z)\,dz=0$ for every closed triangle $T\subset D$.

::: pf-proof

The integrand is continuous on the compact set $\partial T\times\gamma$, so Fubini's theorem allows
$$
\oint_{\partial T}f(z)\,dz=\int_\gamma g(w)\left(\oint_{\partial T}\frac{dz}{w-z}\right)dw.
$$
For fixed $w\in\gamma$, the function $z\mapsto1/(w-z)$ is holomorphic on $D$, since $w\notin D$, so the inner integral is $0$ by Goursat's theorem.

:::

:::

::: pf-step

$f$ is analytic on $\CC\setminus\gamma$.

::: pf-proof

By steps [](#cont){.pf-ref} and [](#morera){.pf-ref} and Morera's theorem, $f$ is analytic on every open disk $D\subset\CC\setminus\gamma$, and these disks cover $\CC\setminus\gamma$.

:::

:::

:::

:::
