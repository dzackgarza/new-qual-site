---
schema: qual/card@1
id: P-TOPF25D
kind: problem
title: $\operatorname{Ext}^1_{\ZZ}(\ZZ\oplus\ZZ_2\oplus\ZZ_3,\ZZ\oplus\ZZ_4\oplus\ZZ_6)$
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: {.problem}
Compute $\operatorname{Ext}(\ZZ \oplus \ZZ_2 \oplus \ZZ_3, \ZZ \oplus \ZZ_4 \oplus \ZZ_6)$.
(Here, $\operatorname{Ext}$ denotes $\operatorname{Ext}^1_{\ZZ}$.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Ext is additive in each variable over finite direct sums, and $\operatorname{Ext}^1_{\ZZ}(\ZZ,B)=0$.

::: pf-proof

The module $\ZZ$ is free, hence projective.

:::

:::

::: {.pf-step #s2}

For every abelian group $B$,
$$\operatorname{Ext}^1_{\ZZ}(\ZZ/n,B)\cong B/nB.$$

::: pf-proof

Apply $\operatorname{Hom}(-,B)$ to the free resolution $0\to\ZZ\xrightarrow n\ZZ\to\ZZ/n\to0$.

:::

:::

::: {.pf-step #s3}

For $B=\ZZ\oplus\ZZ_4\oplus\ZZ_6$,
$$B/2B\cong(\ZZ/2)^3,\qquad B/3B\cong(\ZZ/3)^2.$$

::: pf-proof

Modulo $2$, the three summands contribute respectively $\ZZ/2$, $\ZZ/2$, $\ZZ/2$. Modulo $3$, they contribute $\ZZ/3$, $0$, $\ZZ/3$.

:::

:::

::: pf-step

Therefore
$$\boxed{\operatorname{Ext}^1_{\ZZ}(\ZZ\oplus\ZZ_2\oplus\ZZ_3,\ZZ\oplus\ZZ_4\oplus\ZZ_6)\cong(\ZZ/2)^3\oplus(\ZZ/3)^2.}$$

::: pf-proof

Combine steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
