---
schema: qual/card@1
id: D-IWIA5
kind: definition
title: Isolated singularities and their classification
classification:
  areas:
  - complex-analysis
  topics:
  - Singularities
  - Poles
  - Essential Singularities
  - Removable Singularities
relations: []
review: draft
---

::: {.definition}
Let $z_0\in\CC$ and $r>0$, and let $f$ be [[D-E7A5W|holomorphic]] on the punctured disc $D_r(z_0)\setminus\{z_0\}$.
Then $z_0$ is an \dfn{isolated singularity} of $f$.
If $f(z)=\sum_{k\in\ZZ}c_k(z-z_0)^k$ is the Laurent expansion of $f$ on $D_r(z_0)\setminus\{z_0\}$, the \dfn{order} of $f$ at $z_0$ is
$$
v_{z_0}(f)\coloneqq\inf\{k\in\ZZ:c_k\neq0\}\in\ZZ\cup\{-\infty,+\infty\},
$$
with $v_{z_0}(f)=+\infty$ when every $c_k$ is $0$.
:::

::: {.proposition}
Let $z_0$ be an isolated singularity of $f$.
Then:

(a) $z_0$ is a [[D-BQLJV|removable singularity]] if and only if $v_{z_0}(f)\ge0$;

(b) $z_0$ is a [[D-AUD6K|pole]] if and only if $v_{z_0}(f)\in\ZZ$ and $v_{z_0}(f)<0$, and then the order of the pole is $-v_{z_0}(f)$;

(c) $z_0$ is an [[D-VKP6N|essential singularity]] if and only if $v_{z_0}(f)=-\infty$.
:::

::: {.example}
The function $\sin(1/z)$ has an essential singularity at $0$.
Its Laurent expansion on $\CC\setminus\{0\}$ is
$$
\sin(1/z)=\sum_{m\ge0}\frac{(-1)^m}{(2m+1)!}\,z^{-(2m+1)},
$$
which has nonzero coefficients $c_k$ for infinitely many $k<0$, so $v_0(\sin(1/z))=-\infty$.
:::
