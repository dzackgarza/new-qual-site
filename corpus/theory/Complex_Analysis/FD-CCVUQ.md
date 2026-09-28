---
schema: qual/card@1
id: FD-CCVUQ
kind: definition
title: Removable singularity as a pole of order zero
prompts:
- What is a removable singularity, in terms of the order of a pole?
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Singularities
relations:
- kind: variant-of
  target: FD-BRJK5
review: draft
---

::: {.definition}
Let $f$ be [[D-E7A5W|holomorphic]] on a punctured disc $D_r(z_0)\setminus\{z_0\}$.
The point $z_0$ is a \dfn{removable singularity} of $f$ if there exist $0<\rho\le r$ and a holomorphic function $g\colon D_\rho(z_0)\to\CC$ with $f=g$ on $D_\rho(z_0)\setminus\{z_0\}$.
:::

::: {.proposition}
The point $z_0$ is a removable singularity of $f$ if and only if there are an integer $n\le0$ and a function $h$ holomorphic on a neighborhood of $z_0$ with $f(z)=(z-z_0)^{-n}h(z)$ for $z\neq z_0$ near $z_0$.
:::

::: {.proof}
If $z_0$ is removable, take $n=0$ and $h=g$.
Conversely, $(z-z_0)^{-n}h(z)$ is holomorphic near $z_0$ when $-n\ge0$.
:::

::: {.remark}
The factorization $f=(z-z_0)^{-n}h$ with $n\ge1$ defines a [[D-AUD6K|pole of order $n$]]; allowing $n=0$ in it gives exactly the removable singularities, which is the sense of the phrase "pole of order zero".
:::
