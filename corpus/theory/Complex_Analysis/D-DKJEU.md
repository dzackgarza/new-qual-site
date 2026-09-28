---
schema: qual/card@1
id: D-DKJEU
kind: definition
title: Linear fractional transformation
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations:
- kind: variant-of
  target: D-FRVBV
review: draft
---

::: {.definition}
Let $a,b,c,d\in\CC$ with $ad-bc\neq0$.
The \dfn{linear fractional transformation} with coefficients $a,b,c,d$ is
$$
T(z)\coloneqq\frac{az+b}{cz+d},
$$
defined for $z\in\CC$ with $cz+d\neq0$.
:::

::: {.remark}
The condition $ad-bc\neq0$ says that the vectors $(a,b)$ and $(c,d)$ are linearly independent.
In particular $(c,d)\neq(0,0)$, so the domain $\{z\in\CC:cz+d\neq0\}$ is $\CC$ minus at most one point, and $T$ is not constant there.
:::

::: {.proposition}
Let $T$ be the linear fractional transformation with coefficients $a,b,c,d$, where $ad-bc\neq0$.
Then $T$ is a bijection from $\{z\in\CC:cz+d\neq0\}$ onto $\{w\in\CC:-cw+a\neq0\}$, with inverse the linear fractional transformation
$$
T^{-1}(w)=\frac{dw-b}{-cw+a}.
$$
:::

::: {.proof}
Let $S(w)\coloneqq(dw-b)/(-cw+a)$; its coefficients satisfy $da-(-b)(-c)=ad-bc\neq0$.
For $cz+d\neq0$,
$$
-c\,T(z)+a=\frac{-c(az+b)+a(cz+d)}{cz+d}=\frac{ad-bc}{cz+d}\neq0,
$$
so $T(z)$ lies in the domain of $S$, and
$$
S(T(z))=\frac{d(az+b)-b(cz+d)}{-c(az+b)+a(cz+d)}=\frac{(ad-bc)z}{ad-bc}=z.
$$
The same computation with the roles of $T$ and $S$ exchanged gives $c\,S(w)+d\neq0$ and $T(S(w))=w$ for $-cw+a\neq0$.
:::
