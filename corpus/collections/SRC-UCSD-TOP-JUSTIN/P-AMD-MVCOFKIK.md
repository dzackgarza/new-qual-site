---
schema: qual/card@1
id: P-AMD-MVCOFKIK
kind: problem
title: $\Tor(\ZZ\oplus\ZZ_2\oplus\ZZ_8,\ZZ\oplus\ZZ_4\oplus\ZZ_4)$ and $\Ext(\ZZ\oplus\ZZ_2\oplus\ZZ_3,\ZZ\oplus\ZZ_4\oplus\ZZ_5)$
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
relations: []
review: draft
---

::: {.problem}
Compute:

1. $\Tor(\ZZ \oplus \ZZ_2 \oplus \ZZ_8, \ZZ \oplus \ZZ_4 \oplus \ZZ_4)$

2. $\Ext(\ZZ \oplus \ZZ_2 \oplus \ZZ_3, \ZZ \oplus \ZZ_4 \oplus \ZZ_5)$
:::

::: {.solution}

::: pf

::: pf-step

Over $\ZZ$,
$$
\operatorname{Tor}_1^{\ZZ}(\ZZ/m,\ZZ/n)\cong\ZZ/\gcd(m,n),
$$
and $\operatorname{Tor}_1^{\ZZ}(\ZZ,-)=0$.

::: pf-proof

Resolve $\ZZ/m$ by $0\to\ZZ\xrightarrow{m}\ZZ\to\ZZ/m\to0$. After tensoring with $\ZZ/n$, the Tor group is the kernel of multiplication by $m$ on $\ZZ/n$, which is cyclic of order $\gcd(m,n)$.

:::

:::

::: pf-step

Hence
$$
\boxed{\operatorname{Tor}_1^{\ZZ}(\ZZ\oplus\ZZ_2\oplus\ZZ_8,
\ZZ\oplus\ZZ_4\oplus\ZZ_4)
\cong (\ZZ/2)^2\oplus(\ZZ/4)^2.}
$$

::: pf-proof

Tor is additive in each variable. The two $\ZZ_4$ summands paired with $\ZZ_2$ each contribute $\ZZ_2$, and paired with $\ZZ_8$ each contribute $\ZZ_4$. Every term involving a free $\ZZ$ summand vanishes.

:::

:::

::: {.pf-step #s3}

Over $\ZZ$,
$$
\operatorname{Ext}^1_{\ZZ}(\ZZ/n,B)\cong B/nB,
$$
and $\operatorname{Ext}^1_{\ZZ}(\ZZ,B)=0$.

::: pf-proof

Apply $\operatorname{Hom}_{\ZZ}(-,B)$ to the same length-one free resolution of $\ZZ/n$.

:::

:::

::: {.pf-step #s4}

For $B=\ZZ\oplus\ZZ_4\oplus\ZZ_5$,
$$
B/2B\cong(\ZZ/2)^2,
\qquad
B/3B\cong\ZZ/3.
$$

::: pf-proof

For $B/2B$, the free summand contributes $\ZZ/2$, the $\ZZ_4$ summand contributes $\ZZ/2$, and multiplication by $2$ is an automorphism of $\ZZ_5$. For $B/3B$, only the free summand survives, because multiplication by $3$ is an automorphism on both $\ZZ_4$ and $\ZZ_5$.

:::

:::

::: pf-step

Therefore
$$
\boxed{\operatorname{Ext}^1_{\ZZ}(\ZZ\oplus\ZZ_2\oplus\ZZ_3,
\ZZ\oplus\ZZ_4\oplus\ZZ_5)
\cong (\ZZ/2)^2\oplus\ZZ/3.}
$$

::: pf-proof

Ext is additive in the first variable over finite direct sums. Apply steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

:::

:::
