---
schema: qual/card@1
id: P-TOPF03F
kind: problem
title: $\operatorname{Tor}(\mathbb Z\oplus\mathbb Z_2\oplus\mathbb Z_8,\mathbb Z\oplus\mathbb Z_4\oplus\mathbb Z_4)$
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Tor
relations: []
review: draft
---

::: problem
Compute $\operatorname{Tor}(\mathbb{Z} \oplus \mathbb{Z}_2 \oplus \mathbb{Z}_8, \mathbb{Z} \oplus \mathbb{Z}_4 \oplus \mathbb{Z}_4)$.
:::

::: {.solution}
<1>1. Tor is additive in each variable, and $\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z,-)=0$.
::: {.proof}
The functor $\operatorname{Tor}_1^{\mathbb Z}(-,-)$ preserves finite direct sums in each argument, while $\mathbb Z$ is free and hence flat.
:::

<1>2. For cyclic groups,
$$
\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/r,\mathbb Z/s)\cong\mathbb Z/\gcd(r,s).
$$
::: {.proof}
Resolve $\mathbb Z/r$ by $0\to\mathbb Z\xrightarrow{r}\mathbb Z\to\mathbb Z/r\to0$ and tensor with $\mathbb Z/s$; the kernel of multiplication by $r$ on $\mathbb Z/s$ has order $\gcd(r,s)$.
:::

<1>3. Thus the $\mathbb Z/2$ summand in the first variable contributes two copies of $\mathbb Z/2$, and the $\mathbb Z/8$ summand contributes two copies of $\mathbb Z/4$.
::: {.proof}
Apply <1>2 to the two $\mathbb Z/4$ summands in the second variable:
$$
\gcd(2,4)=2,\qquad \gcd(8,4)=4.
$$
The free summands contribute zero by <1>1.
:::

<1>4. Therefore
$$
\boxed{
\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z\oplus\mathbb Z_2\oplus\mathbb Z_8,
\mathbb Z\oplus\mathbb Z_4\oplus\mathbb Z_4)
\cong (\mathbb Z/2)^2\oplus(\mathbb Z/4)^2.}
$$
::: {.proof}
Sum the nonzero contributions from <1>3.
:::
:::
