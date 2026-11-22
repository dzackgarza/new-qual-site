---
schema: qual/card@1
id: D-3QTVR
kind: definition
title: Riemann sphere
prompts:
- What is the Riemann sphere, and how is it topologized?
- What is the point at infinity on the Riemann sphere?
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Sphere
  - Extended Complex Plane
relations: []
review: draft
---

::: {.definition}
The \dfn{Riemann sphere} is $\CP^1\coloneqq\CC\cup\theset{\infty}$, the one-point compactification of $\CC$: its open sets are the open subsets of $\CC$ together with the sets $\theset{\infty}\cup(\CC\sm K)$ for $K\subseteq\CC$ compact.
The point $\infty$ is the image of $0$ under $z\mapsto1/z$, extended by $1/0\coloneqq\infty$ and $1/\infty\coloneqq0$.
Stereographic projection identifies $\CP^1$ with the sphere of diameter $1$ resting on the origin of $\CC$ at its south pole, the north pole corresponding to $\infty$ [@SS03, ch. 3, §3].
:::

::: {.remark}
A [[D-7DFVJ|meromorphic]] function on $\CC$ that is holomorphic or has a pole at $\infty$ extends to a holomorphic map $\CP^1\to\CP^1$, and those functions are exactly the rational ones ([[T-UBWL2]]).
The [[D-FRVBV|Möbius transformations]] are exactly the biholomorphisms of $\CP^1$, acting on $\CP^1$ by $z\mapsto(az+b)/(cz+d)$ and sending $-d/c$ to $\infty$ and $\infty$ to $a/c$: the automorphism group of $\CP^1$ is $\PSL_2(\CC)$ (C. McMullen, *Advanced Complex Analysis*, Theorem 2.8).
:::
