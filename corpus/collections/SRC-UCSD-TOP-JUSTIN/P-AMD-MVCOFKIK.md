---
schema: qual/card@1
id: P-AMD-MVCOFKIK
kind: problem
title: $\tor(\ZZ\oplus\ZZ_2\oplus\ZZ_8,\ZZ\oplus\ZZ_4\oplus\ZZ_4)$ and $\ext(\ZZ\oplus\ZZ_2\oplus\ZZ_3,\ZZ\oplus\ZZ_4\oplus\ZZ_5)$
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

1. $\tor(\ZZ \oplus \ZZ_2 \oplus \ZZ_8, \ZZ \oplus \ZZ_4 \oplus \ZZ_4)$

2. $\ext(\ZZ \oplus \ZZ_2 \oplus \ZZ_3, \ZZ \oplus \ZZ_4 \oplus \ZZ_5)$
:::

::: {.solution}
<1>1. Over $\mathbb Z$,
$$
\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/m,\mathbb Z/n)\cong\mathbb Z/\gcd(m,n),
$$
and $\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z,-)=0$.
::: {.proof}
Resolve $\mathbb Z/m$ by $0\to\mathbb Z\xrightarrow{m}\mathbb Z\to\mathbb Z/m\to0$. After tensoring with $\mathbb Z/n$, the Tor group is the kernel of multiplication by $m$ on $\mathbb Z/n$, which is cyclic of order $\gcd(m,n)$.
:::

<1>2. Hence
$$
\boxed{\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z\oplus\mathbb Z_2\oplus\mathbb Z_8,
\mathbb Z\oplus\mathbb Z_4\oplus\mathbb Z_4)
\cong (\mathbb Z/2)^2\oplus(\mathbb Z/4)^2.}
$$
::: {.proof}
Tor is additive in each variable. The two $\mathbb Z_4$ summands paired with $\mathbb Z_2$ each contribute $\mathbb Z_2$, and paired with $\mathbb Z_8$ each contribute $\mathbb Z_4$. Every term involving a free $\mathbb Z$ summand vanishes.
:::

<1>3. Over $\mathbb Z$,
$$
\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,B)\cong B/nB,
$$
and $\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z,B)=0$.
::: {.proof}
Apply $\operatorname{Hom}_{\mathbb Z}(-,B)$ to the same length-one free resolution of $\mathbb Z/n$.
:::

<1>4. For $B=\mathbb Z\oplus\mathbb Z_4\oplus\mathbb Z_5$,
$$
B/2B\cong(\mathbb Z/2)^2,
\qquad
B/3B\cong\mathbb Z/3.
$$
::: {.proof}
For $B/2B$, the free summand contributes $\mathbb Z/2$, the $\mathbb Z_4$ summand contributes $\mathbb Z/2$, and multiplication by $2$ is an automorphism of $\mathbb Z_5$. For $B/3B$, only the free summand survives, because multiplication by $3$ is an automorphism on both $\mathbb Z_4$ and $\mathbb Z_5$.
:::

<1>5. Therefore
$$
\boxed{\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z\oplus\mathbb Z_2\oplus\mathbb Z_3,
\mathbb Z\oplus\mathbb Z_4\oplus\mathbb Z_5)
\cong (\mathbb Z/2)^2\oplus\mathbb Z/3.}
$$
::: {.proof}
Ext is additive in the first variable over finite direct sums. Apply <1>3--<1>4.
:::
:::
