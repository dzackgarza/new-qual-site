---
schema: qual/card@1
id: D-OHFRH
kind: definition
title: Univalent functions and biholomorphisms onto their images
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Biholomorphisms
relations: []
review: draft
---

::: {.definition}
Let $\Omega\subseteq\CC$ be open.
A function $f\colon\Omega\to\CC$ is \dfn{univalent} if $f$ is [[D-E7A5W|holomorphic]] and injective.
:::

::: {.proposition}
Let $\Omega\subseteq\CC$ be open and let $f\colon\Omega\to\CC$ be univalent.
Then $f'(z)\neq0$ for every $z\in\Omega$, the image $f(\Omega)$ is open, and $f\colon\Omega\to f(\Omega)$ is a [[D-PCDNH|biholomorphism]].
Conversely, every biholomorphism from $\Omega$ onto an open subset of $\CC$ is univalent.
:::

::: {.proof}
Suppose $f'(z_0)=0$ for some $z_0\in\Omega$.
An injective function is not constant on any disc, so on a disc $D\subseteq\Omega$ about $z_0$, $f-f(z_0)$ has a [[D-65VIK|zero of order $n$]] at $z_0$ with $n\ge2$: $f(z)-f(z_0)=(z-z_0)^n g(z)$ with $g$ holomorphic and $g(z_0)\neq0$.
Shrinking $D$, $g$ has no zeros on $D$, so it has a holomorphic $n$-th root $k$ on $D$, and $f(z)-f(z_0)=\varphi(z)^n$ with $\varphi(z)\coloneqq(z-z_0)k(z)$.
Since $\varphi(z_0)=0$ and $\varphi'(z_0)=k(z_0)\neq0$, the holomorphic inverse function theorem gives a neighborhood $V\subseteq D$ of $z_0$ mapped by $\varphi$ bijectively onto a disc $D_\varepsilon(0)$.
For $0<\delta<\varepsilon$, the $n\ge2$ distinct points $\varphi^{-1}(\delta e^{2\pi ij/n})$, $j=0,\ldots,n-1$, all have image $f(z_0)+\delta^n$ under $f$, contradicting injectivity.
Hence $f'$ has no zeros.

By the [[C-FRF33|open mapping theorem]] applied on each connected component of $\Omega$, $f(\Omega)$ is open.
For $w_0=f(z_0)$, the holomorphic inverse function theorem gives open neighborhoods $V\ni z_0$ and $W\ni w_0$ with $f\colon V\to W$ bijective and holomorphic inverse; since $f$ is injective, $f^{-1}$ agrees with this local inverse on $W$.
Thus $f^{-1}\colon f(\Omega)\to\Omega$ is holomorphic.
The converse holds because a biholomorphism is holomorphic and bijective onto its image.
:::
