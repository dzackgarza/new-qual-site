---
schema: qual/card@1
id: P-TOPF03F
kind: problem
title: $\operatorname{Tor}(\ZZ\oplus\ZZ_2\oplus\ZZ_8,\ZZ\oplus\ZZ_4\oplus\ZZ_4)$
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Tor
relations: []
review: draft
---

::: {.problem}
Compute $\operatorname{Tor}(\ZZ \oplus \ZZ_2 \oplus \ZZ_8, \ZZ \oplus \ZZ_4 \oplus \ZZ_4)$.
:::

::: {.solution}

::: pf

::: {.pf-step #tor-additive-free-flat}
Tor is additive in each variable, and $\operatorname{Tor}_1^{\ZZ}(\ZZ,-)=0$.

::: pf-proof
The functor $\operatorname{Tor}_1^{\ZZ}(-,-)$ preserves finite direct sums in each argument, while $\ZZ$ is free and hence flat.
:::

:::

::: {.pf-step #tor-cyclic-formula}
For cyclic groups,
$$
\operatorname{Tor}_1^{\ZZ}(\ZZ/r,\ZZ/s)\cong\ZZ/\gcd(r,s).
$$

::: pf-proof
Resolve $\ZZ/r$ by $0\to\ZZ\xrightarrow{r}\ZZ\to\ZZ/r\to0$ and tensor with $\ZZ/s$; the kernel of multiplication by $r$ on $\ZZ/s$ has order $\gcd(r,s)$.
:::

:::

::: {.pf-step #summand-contributions}
Thus the $\ZZ/2$ summand in the first variable contributes two copies of $\ZZ/2$, and the $\ZZ/8$ summand contributes two copies of $\ZZ/4$.

::: pf-proof
Apply step [](#tor-cyclic-formula){.pf-ref} to the two $\ZZ/4$ summands in the second variable:
$$
\gcd(2,4)=2,\qquad \gcd(8,4)=4.
$$
The free summands contribute zero by step [](#tor-additive-free-flat){.pf-ref}.
:::

:::

::: pf-step
Therefore
$$
\boxed{
\operatorname{Tor}_1^{\ZZ}(\ZZ\oplus\ZZ_2\oplus\ZZ_8,
\ZZ\oplus\ZZ_4\oplus\ZZ_4)
\cong (\ZZ/2)^2\oplus(\ZZ/4)^2.}
$$

::: pf-proof
Sum the nonzero contributions from step [](#summand-contributions){.pf-ref}.
:::

:::

:::

:::
