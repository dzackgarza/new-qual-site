---
schema: qual/card@1
id: PR-KX7L7
kind: proposition
title: Tensoring preserves injections exactly when the factor is flat
classification:
  areas:
  - algebra
  topics:
  - Tensor Products
  - Exact Sequences
  - Vector Spaces
relations: []
review: draft
---

::: {.proposition}
Let $R$ be a commutative ring and $X$ an $R$-module, and let $F \coloneqq (\wait) \tensor_R X$ on $R$-modules.

- $F$ is right exact.

- $F$ preserves injections, that is, $T \tensor \id_X\colon V \tensor_R X \to W \tensor_R X$ is injective for every injective $R$-linear map $T\colon V \injects W$, if and only if $X$ is [[D-DEFFLAT|flat]], and in that case $F$ is exact.

- If $R = k$ is a field, every $k$-module is flat, so $T \tensor \id_X\colon V \tensor_k X \injects W \tensor_k X$ is injective for every injective $k$-linear map $T\colon V \injects W$ and every $k$-vector space $X$.
:::

::: {.example}
Over $\ZZ$, tensoring does not preserve injections in general: $\ZZ/2\ZZ$ is not a flat $\ZZ$-module.
The map $\ZZ \mapsvia{2} \ZZ$ is injective, and tensoring it with $\ZZ/2\ZZ$ gives multiplication by $2$ on $\ZZ/2\ZZ$, which is the zero map and not injective.
:::
