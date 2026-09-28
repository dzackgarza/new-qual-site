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
so $T$ is [[D-PCDNH|conformal]] there.
:::

::: {.proof}
(i) For $cz+d\neq0$, $-c\,T(z)+a=(ad-bc)/(cz+d)\neq0$, and
$$
\frac{d\,T(z)-b}{-c\,T(z)+a}=\frac{d(az+b)-b(cz+d)}{-c(az+b)+a(cz+d)}=\frac{(ad-bc)z}{ad-bc}=z.
$$
The map $w\mapsto(dw-b)/(-cw+a)$ has coefficients with $da-bc\neq0$, and the same computation shows that $T$ inverts it on $\{w:-cw+a\neq0\}$.

(ii) By the quotient rule,
$$
T'(z)=\frac{a(cz+d)-c(az+b)}{(cz+d)^2}=\frac{ad-bc}{(cz+d)^2},
$$
which is nonzero because $ad-bc\neq0$.
:::
