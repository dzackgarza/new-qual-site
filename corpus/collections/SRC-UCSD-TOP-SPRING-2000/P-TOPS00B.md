---
schema: qual/card@1
id: P-TOPS00B
kind: problem
title: $\operatorname{Ext}^1_{\ZZ}(\ZZ/n,\QQ/\ZZ)$
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Ext
relations: []
review: draft
---

::: {.problem}
Compute $\operatorname{Ext}^1(\ZZ/n, \QQ/\ZZ)$.
:::

::: {.solution}

::: pf

::: pf-step

Use the free resolution
$$
0\longrightarrow\ZZ\xrightarrow{\;n\;}\ZZ\longrightarrow\ZZ/n\longrightarrow0.
$$

::: pf-proof

The cokernel of multiplication by $n$ on $\ZZ$ is $\ZZ/n$.

:::

:::

::: {.pf-step #s2}

Applying $\operatorname{Hom}_{\ZZ}(-,\QQ/\ZZ)$ gives
$$
\operatorname{Ext}^1_{\ZZ}(\ZZ/n,\QQ/\ZZ)
\cong
(\QQ/\ZZ)/n(\QQ/\ZZ).
$$

::: pf-proof

The first Ext group is the cokernel of the map induced by multiplication by $n$ on the two Hom groups, both naturally isomorphic to $\QQ/\ZZ$.

:::

:::

::: {.pf-step #s3}

Multiplication by $n$ on $\QQ/\ZZ$ is surjective.

::: pf-proof

Given $q+\ZZ$, the class $q/n+\ZZ$ maps to it under multiplication by $n$.

:::

:::

::: pf-step

Hence
$$
\boxed{\operatorname{Ext}^1_{\ZZ}(\ZZ/n,\QQ/\ZZ)=0}.
$$

::: pf-proof

The quotient in step [](#s2){.pf-ref} is zero by step [](#s3){.pf-ref}. Equivalently, $\QQ/\ZZ$ is divisible and therefore injective as a $\ZZ$-module.

:::

:::

:::

:::
