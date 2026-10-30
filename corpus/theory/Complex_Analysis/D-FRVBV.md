---
schema: qual/card@1
id: D-FRVBV
kind: definition
title: Möbius transformation
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations: []
review: draft
---

::: {.definition}
Let $a,b,c,d\in\CC$ with $ad-bc\neq0$.
The map
$$
T(z)\coloneqq\frac{az+b}{cz+d},
$$
defined for $z\in\CC$ with $cz+d\neq0$, is a \dfn{linear fractional transformation}, or \dfn{Möbius transformation}.
:::

::: {.proposition}
Let $T(z)=(az+b)/(cz+d)$ with $ad-bc\neq0$.

(i) $T$ is a bijection from $\{z\in\CC:cz+d\neq0\}$ onto $\{w\in\CC:-cw+a\neq0\}$, with inverse
$$
T^{-1}(w)=\frac{dw-b}{-cw+a}.
$$

(ii) $T$ is [[D-E7A5W|holomorphic]] on $\{z\in\CC:cz+d\neq0\}$, with
$$
T'(z)=\frac{ad-bc}{(cz+d)^2}\neq0,
$$
so $T$ is [[D-TM4TE|conformal]] there.
:::

::: {.remark}
The condition $ad-bc\neq0$ says that the vectors $(a,b)$ and $(c,d)$ are linearly independent.
In particular $(c,d)\neq(0,0)$, so the domain $\{z\in\CC:cz+d\neq0\}$ is $\CC$ minus at most one point, and $T$ is not constant there.
:::
