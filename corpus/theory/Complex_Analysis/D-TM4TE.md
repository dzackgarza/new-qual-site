---
schema: qual/card@1
id: D-TM4TE
kind: definition
title: Conformal maps and biholomorphisms
prompts:
- What is a conformal map?
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

::: {.remark}
The book's definition is geometric: [@Ahl73, ch. 3, §2.3, Conformal Mapping] defines a map to be conformal where it preserves angles, shows that an analytic function with nonvanishing derivative preserves both angles and the scale of small segments there, and shows conversely that a map with continuous partial derivatives which preserves angles satisfies the Cauchy--Riemann equations there or their conjugates, the second case being what the book calls indirectly conformal. Among maps with continuous partial derivatives, the directly conformal ones are therefore exactly the analytic maps with nonvanishing derivative, which is the definition above.
:::

::: {.proposition}
Let $\Omega\subseteq\CC$ be open and let $f$ be conformal on $\Omega$.

(i) $f$ preserves signed angles: if $\gamma_1,\gamma_2\colon(-1,1)\to\Omega$ are $C^1$ curves with $\gamma_1(0)=\gamma_2(0)=z_0$ and nonzero tangents $\gamma_1'(0),\gamma_2'(0)$, then the signed angle from $(f\circ\gamma_1)'(0)$ to $(f\circ\gamma_2)'(0)$ equals the signed angle from $\gamma_1'(0)$ to $\gamma_2'(0)$.

(ii) $f$ is locally injective: every $z_0\in\Omega$ has an open neighborhood on which $f$ is injective.

(iii) If $U,V\subseteq\CC$ are open and $f\colon U\to V$ is a holomorphic bijection, then $f'$ has no zeros and $f^{-1}\colon V\to U$ is holomorphic and conformal.
In particular, the inverse of a biholomorphism is a biholomorphism.
:::
