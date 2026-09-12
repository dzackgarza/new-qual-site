---
schema: qual/card@1
id: P-TOPF25D
kind: problem
title: $\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z\oplus\mathbb Z_2\oplus\mathbb Z_3,\mathbb Z\oplus\mathbb Z_4\oplus\mathbb Z_6)$
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: problem
Compute $\operatorname{Ext}(\mathbb{Z} \oplus \mathbb{Z}_2 \oplus \mathbb{Z}_3, \mathbb{Z} \oplus \mathbb{Z}_4 \oplus \mathbb{Z}_6)$.
(Here, $\operatorname{Ext}$ denotes $\operatorname{Ext}^1_{\mathbb{Z}}$.)
:::

::: {.solution}
<1>1. Ext is additive in each variable over finite direct sums, and $\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z,B)=0$.
::: {.proof}
The module $\mathbb Z$ is free, hence projective.
:::

<1>2. For every abelian group $B$,
$$\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,B)\cong B/nB.$$
::: {.proof}
Apply $\operatorname{Hom}(-,B)$ to the free resolution $0\to\mathbb Z\xrightarrow n\mathbb Z\to\mathbb Z/n\to0$.
:::

<1>3. For $B=\mathbb Z\oplus\mathbb Z_4\oplus\mathbb Z_6$,
$$B/2B\cong(\mathbb Z/2)^3,\qquad B/3B\cong(\mathbb Z/3)^2.$$
::: {.proof}
Modulo $2$, the three summands contribute respectively $\mathbb Z/2$, $\mathbb Z/2$, $\mathbb Z/2$. Modulo $3$, they contribute $\mathbb Z/3$, $0$, $\mathbb Z/3$.
:::

<1>4. Therefore
$$\boxed{\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z\oplus\mathbb Z_2\oplus\mathbb Z_3,\mathbb Z\oplus\mathbb Z_4\oplus\mathbb Z_6)\cong(\mathbb Z/2)^3\oplus(\mathbb Z/3)^2.}$$
::: {.proof}
Combine <1>1--<1>3.
:::
:::
