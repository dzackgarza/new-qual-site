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

::: {.proposition title="Tensoring preserves injections exactly when the factor is flat"}
Over a field $k$, every module is flat, so if $T:V \injects W$ is injective then $T\tensor \one_X: V\tensor_k X \injects W\tensor_k X$ is also injective for any $X$.

Over a general ring this fails.
Tensoring the injection $\ZZ \mapsvia{2} \ZZ$ with $\ZZ/2\ZZ$ gives the zero map $\ZZ/2\ZZ \to \ZZ/2\ZZ$, which is not injective.

The two properties are separate:

- $F(\wait) = (\wait \tensor_R X)$ is right-exact for every $X$ and every $R$, with no hypothesis.

- $F$ preserves injections exactly when $X$ is flat, and then $F$ is exact.

So right-exactness is not a consequence of preserving injections; preserving injections is the strictly stronger half.
:::
