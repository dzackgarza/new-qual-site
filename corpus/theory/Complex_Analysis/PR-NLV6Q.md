---
schema: qual/card@1
id: PR-NLV6Q
kind: proposition
title: $\Gamma$ is holomorphic on the right half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
  - Holomorphic Functions
relations: []
review: draft
---

::: {.proposition}
For $\Re s>0$ the integral
$$
\Gamma(s)=\int_0^\infty e^{-t}t^{s-1}\dt
$$
converges absolutely, and it defines a [[D-E7A5W|holomorphic]] function on the right half-plane $\ts{s\in\CC\st\Re s>0}$.
:::

::: {.proof}
For $t>0$, $\abs{t^{s-1}}=\abs{e^{(s-1)\ln t}}=t^{\Re s-1}$.
For $0<\varepsilon<1$ put
$$
\Gamma_\varepsilon(s)\coloneqq\int_\varepsilon^{1/\varepsilon}e^{-t}t^{s-1}\dt.
$$
The integrand is continuous in $(t,s)$ and holomorphic in $s$, and the interval is compact, so each $\Gamma_\varepsilon$ is entire.

Fix $n\ge1$ and the strip $A_n\coloneqq\ts{s\st \frac1n<\Re s<n}$.
For $s\in A_n$,
$$
\abs{\Gamma(s)-\Gamma_\varepsilon(s)}\le\int_0^\varepsilon t^{1/n-1}\dt+\int_{1/\varepsilon}^\infty e^{-t}t^{n-1}\dt,
$$
using $t^{\Re s-1}\le t^{1/n-1}$ for $t\le1$ and $t^{\Re s-1}\le t^{n-1}$ for $t\ge1$.
Both integrals are finite (so the integral defining $\Gamma$ converges absolutely) and tend to $0$ as $\varepsilon\to0$, independently of $s$.
Hence $\Gamma_\varepsilon\to\Gamma$ uniformly on each $A_n$.
A uniform limit of holomorphic functions on an open set is holomorphic, so $\Gamma$ is holomorphic on each $A_n$, and the strips $A_n$ cover the right half-plane.
:::
