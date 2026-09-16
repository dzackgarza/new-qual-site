---
schema: qual/card@1
id: T-77SHB
kind: theorem
title: Cayley transform $\frac{i-z}{i+z}$ between the upper half-plane and the disc
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.theorem}
The [[D-DKJEU|fractional linear transformation]]
$$
G(w)=i\,\frac{1-w}{1+w}
$$
maps the unit disc $\DD$ biholomorphically onto the upper half-plane $\HH=\ts{z\st\Im z>0}$.
Its inverse is
$$
F(z)=\frac{i-z}{i+z},
$$
which maps $\HH$ biholomorphically onto $\DD$.
:::

::: {.proof}
For $w\in\DD$, $w\neq-1$ and
$$
\Im G(w)=\Re\frac{1-w}{1+w}=\frac{\Re\big((1-w)(1+\bar w)\big)}{\abs{1+w}^2}=\frac{1-\abs w^2}{\abs{1+w}^2}>0.
$$
For $z\in\HH$, $z$ is closer to $i$ than to $-i$, so $\abs{F(z)}<1$.
Solving $z=i\frac{1-w}{1+w}$ gives $z+zw=i-iw$, so $w(z+i)=i-z$ and $w=F(z)$; hence $F$ and $G$ are mutually inverse holomorphic maps.
:::
