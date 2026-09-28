---
schema: qual/card@1
id: P-KGHOG
kind: problem
title: The Fourier transform of a compactly supported continuous function is entire
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Integrals
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Suppose that $f: \RR\to\RR$ is a continuous function that vanishes outside of some finite interval.
For each $z\in \CC$, define
\[
g(z) = \int_{-\infty}^\infty f(t) e^{-izt} \,dt
.\]

Show that $g$ is entire.
:::

::: {.solution}
Choose $R>0$ such that $f(t)=0$ for $|t|>R$. Then
\[
g(z)=\int_{-R}^R f(t)e^{-izt}\,dt.
\]
Fix a compact set $K\subset\mathbb C$. If $M=\sup_{z\in K}|\Im z|$, then for
$z\in K$ and $|t|\le R$,
\[
|f(t)e^{-izt}|
\le |f(t)|e^{MR},
\]
and similarly
\[
|-it\,f(t)e^{-izt}|
\le R|f(t)|e^{MR}.
\]
These are integrable majorants on $[-R,R]$. Hence differentiation under the
integral sign is valid, giving
\[
g'(z)=\int_{-R}^R (-it)f(t)e^{-izt}\,dt.
\]
Thus $g$ is holomorphic on all of $\mathbb C$, i.e. $g$ is entire.

Iterating the same argument gives, for every $n\ge0$,
\[
g^{(n)}(z)=\int_{-R}^R(-it)^n f(t)e^{-izt}\,dt.
\]
:::
