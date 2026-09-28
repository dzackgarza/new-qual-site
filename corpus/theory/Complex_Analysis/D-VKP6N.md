---
schema: qual/card@1
id: D-VKP6N
kind: definition
title: Essential singularity
classification:
  areas:
  - complex-analysis
  topics:
  - Essential Singularities
  - Singularities
  - Laurent Series
  - Principal Parts
relations: []
review: draft
---

::: {.definition}
Let $f$ be [[D-E7A5W|holomorphic]] on a punctured disc $D_r(z_0)\setminus\{z_0\}$.
The [[D-IWIA5|isolated singularity]] $z_0$ is an \dfn{essential singularity} of $f$ if it is neither a [[D-BQLJV|removable singularity]] nor a [[D-AUD6K|pole]] of $f$.
:::

::: {.proposition}
Let $f(z)=\sum_{k\in\ZZ}c_k(z-z_0)^k$ be the Laurent expansion of $f$ on $D_r(z_0)\setminus\{z_0\}$.
Then $z_0$ is an essential singularity of $f$ if and only if $c_k\neq0$ for infinitely many $k<0$, that is, if and only if the principal part $\sum_{k<0}c_k(z-z_0)^k$ has infinitely many nonzero terms.
:::

::: {.proof}
By the proposition on [[D-IWIA5]], $z_0$ is removable exactly when $c_k=0$ for all $k<0$, and a pole exactly when $c_k\neq0$ for some but only finitely many $k<0$.
The remaining case is that $c_k\neq0$ for infinitely many $k<0$.
:::
