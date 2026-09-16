---
schema: qual/card@1
id: C-FVT4V
kind: corollary
title: Injective holomorphic maps have nonvanishing derivative
classification:
  areas:
  - complex-analysis
  topics:
  - Biholomorphisms
  - Conformal Maps
relations: []
review: draft
---

::: {.corollary}
Let $U,V\subseteq\CC$ be open and let $f\colon U\to V$ be [[D-E7A5W|holomorphic]] and injective.
Then $f'(z)\neq0$ for every $z\in U$, and the inverse $f^{-1}\colon f(U)\to U$ is holomorphic.
In particular, the inverse of a [[D-TM4TE|conformal map]] is conformal.
:::

::: {.example}
A nowhere-vanishing derivative does not imply injectivity: $f(z)=e^z$ satisfies $f'(z)=e^z\neq0$ on $\CC$, and $f(0)=f(2\pi i)$.
:::

::: {.remark}
Stein--Shakarchi, *Complex Analysis*, Chapter 8, Proposition 1.1.
:::
