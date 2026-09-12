---
schema: qual/card@1
id: P-TOPS00B
kind: problem
title: $\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Q/\mathbb Z)$
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Ext
relations: []
review: draft
---

::: problem
Compute $\operatorname{Ext}^1(\mathbb{Z}/n, \mathbb{Q}/\mathbb{Z})$.
:::

::: {.solution}
<1>1. Use the free resolution
$$
0\longrightarrow\mathbb Z\xrightarrow{\;n\;}\mathbb Z\longrightarrow\mathbb Z/n\longrightarrow0.
$$
::: {.proof}
The cokernel of multiplication by $n$ on $\mathbb Z$ is $\mathbb Z/n$.
:::

<1>2. Applying $\operatorname{Hom}_{\mathbb Z}(-,\mathbb Q/\mathbb Z)$ gives
$$
\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Q/\mathbb Z)
\cong
(\mathbb Q/\mathbb Z)/n(\mathbb Q/\mathbb Z).
$$
::: {.proof}
The first Ext group is the cokernel of the map induced by multiplication by $n$ on the two Hom groups, both naturally isomorphic to $\mathbb Q/\mathbb Z$.
:::

<1>3. Multiplication by $n$ on $\mathbb Q/\mathbb Z$ is surjective.
::: {.proof}
Given $q+\mathbb Z$, the class $q/n+\mathbb Z$ maps to it under multiplication by $n$.
:::

<1>4. Hence
$$
\boxed{\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Q/\mathbb Z)=0}.
$$
::: {.proof}
The quotient in <1>2 is zero by <1>3. Equivalently, $\mathbb Q/\mathbb Z$ is divisible and therefore injective as a $\mathbb Z$-module.
:::
:::
