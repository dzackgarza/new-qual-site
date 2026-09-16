---
schema: qual/card@1
id: D-VAXQT
kind: definition
title: Isolated singularity
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
:::

::: {.proposition}
An isolated singularity $z_0$ of $f$ is of exactly one of three types, determined by the [[D-IWIA5|order]] $v_{z_0}(f)$ of the Laurent expansion of $f$ at $z_0$:

(a) a [[D-BQLJV|removable singularity]], when $v_{z_0}(f)\ge0$;

(b) a [[D-AUD6K|pole]], when $v_{z_0}(f)$ is a negative integer;

(c) an [[D-VKP6N|essential singularity]], when $v_{z_0}(f)=-\infty$.
:::

::: {.proof}
The three conditions on $v_{z_0}(f)\in\ZZ\cup\{\pm\infty\}$ are mutually exclusive and exhaustive, and each characterizes the corresponding type by the proposition on [[D-IWIA5]].
:::

::: {.example}
The function $\sin(1/z)$ has an essential singularity at $0$: its Laurent expansion $\sum_{m\ge0}\frac{(-1)^m}{(2m+1)!}z^{-(2m+1)}$ on $\CC\setminus\{0\}$ has infinitely many nonzero coefficients of negative index.
:::
