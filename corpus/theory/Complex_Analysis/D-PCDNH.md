---
schema: qual/card@1
id: D-PCDNH
kind: definition
title: Conformal maps and biholomorphisms
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
A map $f\colon\Omega\to\CC$ is \dfn{conformal} on $\Omega$ if $f$ is [[D-E7A5W|holomorphic]] on $\Omega$ and $f'(z)\neq0$ for every $z\in\Omega$.

Let $U,V\subseteq\CC$ be open.
A bijective conformal map $f\colon U\to V$ is a \dfn{biholomorphism}, and $U$ and $V$ are \dfn{biholomorphic}, or \dfn{conformally equivalent}, if a biholomorphism $U\to V$ exists.
The biholomorphisms $\Omega\to\Omega$ form a group under composition, the \dfn{automorphism group} $\Aut_\CC(\Omega)$.
:::

::: {.proposition}
Let $\Omega\subseteq\CC$ be open and let $f$ be conformal on $\Omega$.

(i) $f$ preserves signed angles: if $\gamma_1,\gamma_2\colon(-1,1)\to\Omega$ are $C^1$ curves with $\gamma_1(0)=\gamma_2(0)=z_0$ and nonzero tangents $\gamma_1'(0),\gamma_2'(0)$, then the signed angle from $(f\circ\gamma_1)'(0)$ to $(f\circ\gamma_2)'(0)$ equals the signed angle from $\gamma_1'(0)$ to $\gamma_2'(0)$.

(ii) If $U,V\subseteq\CC$ are open and $f\colon U\to V$ is a holomorphic bijection, then $f'$ has no zeros and $f^{-1}\colon V\to U$ is holomorphic and conformal.
In particular, the inverse of a biholomorphism is a biholomorphism.
:::

::: {.proof}
(i) By the chain rule $(f\circ\gamma_j)'(0)=f'(z_0)\,\gamma_j'(0)$.
Multiplication by $f'(z_0)=\abs{f'(z_0)}e^{i\alpha}\neq0$ scales by $\abs{f'(z_0)}>0$ and rotates by $\alpha$, adding $\alpha$ to the argument of both tangent vectors, so the difference of their arguments is unchanged.

(ii) A holomorphic bijection $U\to V$ is [[D-OHFRH|univalent]], so by the proposition on that card $f'$ has no zeros and $f^{-1}$ is holomorphic.
Differentiating $f(f^{-1}(w))=w$ gives $(f^{-1})'(w)=1/f'(f^{-1}(w))\neq0$.
:::
